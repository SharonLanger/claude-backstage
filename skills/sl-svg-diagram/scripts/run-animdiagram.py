#!/usr/bin/env python3
"""Pinned local animdiagram runner. Standard library only; no runtime downloads."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile

COMMIT = "a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486"
REPOSITORY = "https://github.com/praveenvijayan/animdiagram.git"
SKILL = Path(__file__).resolve().parent.parent
CONFIG = ".installation.json"
TOOLS = {"timeline": "timeline.py", "check": "check.py", "skin": "skin.py",
         "preview": "preview.py", "test": "test_timeline.py"}
REQUIRED = ("SKILL.md", "README.md", "audit/animdiagram-audit.md",
            "audit/verified-files.sha256", "scripts/setup-animdiagram.sh",
            "scripts/run-animdiagram.py")


class IntegrityError(Exception):
    pass


def manifest() -> dict[str, str]:
    for name in REQUIRED:
        if not (SKILL / name).is_file():
            raise IntegrityError("incomplete skill installation")
    if "name: sl-svg-diagram\n" not in (SKILL / "SKILL.md").read_text():
        raise IntegrityError("unexpected skill identity")
    entries = {}
    for line in (SKILL / "audit/verified-files.sha256").read_text().splitlines():
        digest, name = line.split("  ", 1)
        path = PurePosixPath(name)
        if (len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest)
                or path.is_absolute() or ".." in path.parts or ".git" in path.parts
                or "\\" in name or name in entries):
            raise IntegrityError("invalid audit manifest")
        entries[name] = digest
    if not entries or not all("scripts/" + name in entries for name in TOOLS.values()):
        raise IntegrityError("incomplete audit manifest")
    return entries


def git(*args: str, cwd: Path | None = None) -> str:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(GIT_TERMINAL_PROMPT="0", GIT_CONFIG_NOSYSTEM="1",
               GIT_CONFIG_GLOBAL=os.devnull)
    return subprocess.check_output(
        ["git", "-c", "core.hooksPath=" + os.devnull, *args], cwd=cwd,
        env=env, stderr=subprocess.PIPE, text=True).strip()


def dependency() -> Path:
    data = json.loads((SKILL / CONFIG).read_text())
    if (not isinstance(data, dict) or data.get("commit") != COMMIT
            or not isinstance(data.get("dependency"), str)
            or not Path(data["dependency"]).is_absolute()):
        raise IntegrityError("invalid installation configuration")
    return Path(data["dependency"])


def verified_bytes(root: Path, entries: dict[str, str]) -> dict[str, bytes]:
    if root.is_symlink() or not root.is_dir():
        raise IntegrityError("dependency missing or linked")
    if git("rev-parse", "HEAD", cwd=root) != COMMIT:
        raise IntegrityError("commit mismatch")
    # All audited tracked files must still exist; additions also require a new audit.
    tracked = set(git("ls-files", cwd=root).splitlines())
    if tracked != set(entries):
        raise IntegrityError("tracked-file set changed")
    data = {}
    for name, expected in entries.items():
        path = root / name
        if any(root.joinpath(*PurePosixPath(name).parts[:i]).is_symlink()
               for i in range(1, len(PurePosixPath(name).parts) + 1)):
            raise IntegrityError("linked dependency file")
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise IntegrityError("file mismatch")
        data[name] = raw
    return data


def setup(args) -> int:
    entries = manifest()
    target = args.skill_dir.expanduser().absolute()
    root = args.dependency_dir.expanduser().absolute()
    if target.is_symlink():
        raise IntegrityError("linked skill installation")
    if target == root or target in root.parents or root in target.parents:
        raise IntegrityError("skill and dependency locations must be separate")
    files = {p.relative_to(SKILL): p.read_bytes() for p in SKILL.rglob("*")
             if p.is_file() and p.name != CONFIG and "__pycache__" not in p.parts}
    if target.exists():
        # Never replace another version or customized installation silently.
        for rel, raw in files.items():
            dest = target / rel
            if dest.is_symlink() or not dest.is_file() or dest.read_bytes() != raw:
                raise IntegrityError("existing skill differs; choose a fresh destination")
        if (target / CONFIG).exists():
            old = json.loads((target / CONFIG).read_text())
            if old != {"commit": COMMIT, "dependency": str(root)}:
                raise IntegrityError("existing installation uses another dependency path")
    if not root.exists():
        root.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".animdiagram-setup-", dir=root.parent) as tmp:
            checkout = Path(tmp) / "checkout"
            git("clone", "--no-checkout", REPOSITORY, str(checkout))
            git("checkout", "--detach", COMMIT, cwd=checkout)
            verified_bytes(checkout, entries)
            if root.exists():
                raise IntegrityError("dependency destination appeared during setup")
            checkout.rename(root)
    data = verified_bytes(root, entries)
    # Tests execute a verified temporary snapshot, never unverified checkout extras.
    if execute(data, "test", []) != 0:
        raise IntegrityError("upstream smoke tests failed")
    target.mkdir(parents=True, exist_ok=True)
    for rel, raw in files.items():
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(raw)
    (target / CONFIG).write_text(json.dumps({"commit": COMMIT, "dependency": str(root)}, indent=2) + "\n")
    subprocess.run([sys.executable, "-I", str(target / "scripts/run-animdiagram.py"), "verify"], check=True)
    print("Installed: " + str(target))
    print("Dependency: " + str(root))
    return 0


def execute(data: dict[str, bytes], tool: str, arguments: list[str], quiet=False) -> int:
    # Snapshot the actual hashed bytes to avoid a check-then-read race and prevent
    # untracked Python modules/bytecode in the checkout from entering execution.
    with tempfile.TemporaryDirectory(prefix="sl-svg-diagram-") as tmp:
        snapshot = Path(tmp)
        for name, raw in data.items():
            dest = snapshot / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(raw)
        result = subprocess.run([sys.executable, "-I", "-S",
                                 str(snapshot / "scripts" / TOOLS[tool]), *arguments],
                                capture_output=quiet, text=quiet)
        if quiet and result.returncode:
            print((result.stdout + result.stderr)[-2000:], file=sys.stderr)
        return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    install = commands.add_parser("setup", help="install skill and pinned dependency; network permitted here only")
    install.add_argument("--skill-dir", type=Path, default=Path.home() / ".claude/skills/sl-svg-diagram")
    install.add_argument("--dependency-dir", type=Path,
                         default=Path.home() / ".local/share/sl-svg-diagram/animdiagram" / COMMIT)
    commands.add_parser("verify", help="check installation and dependency; print one status line")
    for tool in TOOLS:
        cmd = commands.add_parser(tool, add_help=False)
        cmd.add_argument("arguments", nargs=argparse.REMAINDER)
    copy = commands.add_parser("template", help="copy an audited SVG template without overwriting")
    copy.add_argument("destination", type=Path)
    copy.add_argument("--light", action="store_true")
    build = commands.add_parser("build", help="build versioned semantic JSON with verified compiler")
    build.add_argument("spec", type=Path)
    build.add_argument("--out", type=Path, required=True)
    build.add_argument("--debug-normalized", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "setup":
            return setup(args)
        data = verified_bytes(dependency(), manifest())
        if args.command == "verify":
            print("Integrity: PASS")
            return 0
        if args.command == "template":
            name = "assets/template-light.svg" if args.light else "assets/template.svg"
            args.destination.parent.mkdir(parents=True, exist_ok=True)
            with args.destination.open("xb") as dest:
                dest.write(data[name])
            return 0
        if args.command == "build":
            import importlib.util
            module_spec = importlib.util.spec_from_file_location("sl_generate", SKILL / "scripts/generate.py")
            generator = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(generator)
            try:
                return generator.build(args.spec, args.out, SKILL / "defaults/v1.json", data,
                                       lambda d, tool, a: execute(d, tool, a, quiet=True), args.debug_normalized)
            except (generator.BuildError, OSError) as exc:
                print("Build: FAIL. " + str(exc), file=sys.stderr)
                return 2
        arguments = args.arguments
        if arguments[:1] == ["--"]:
            arguments = arguments[1:]
        if args.command == "preview" and any(a.startswith("--") and a != "--out"
                                             and not a.startswith("--out=") for a in arguments):
            print("Blocked: automatic browser launch requires a separately enforced offline renderer.", file=sys.stderr)
            return 2
        return execute(data, args.command, arguments)
    except (IntegrityError, OSError, ValueError, KeyError, subprocess.CalledProcessError):
        print("Integrity: FAIL. Installation or audited dependency mismatch; execution blocked. Restore the pinned installation.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
