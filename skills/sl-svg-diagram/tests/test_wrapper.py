#!/usr/bin/env python3
"""Offline integration tests. Pass an existing audited checkout as the first arg."""
import importlib.util
import json
import os
import re
from urllib.parse import unquote, urlsplit
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]
CHECKOUT = Path(sys.argv.pop(1)).resolve() if len(sys.argv) > 1 else None
PIN = "a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486"

RUNTIME = SOURCE
if '--skill-dir' in sys.argv:
    runtime_index = sys.argv.index('--skill-dir')
    RUNTIME = Path(sys.argv[runtime_index + 1]).resolve()
    del sys.argv[runtime_index:runtime_index + 2]

BUNDLE = {'SKILL.md', 'references/reading-diagrams.md', 'scripts/run-animdiagram.py',
          'audit/verified-files.sha256', 'notices/animdiagram-MIT.txt'}


class WrapperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="sl diagram tests ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.dep = self.base / "dependency"
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(CHECKOUT), str(self.dep)], check=True)
        subprocess.run(["git", "checkout", "--quiet", "--detach", PIN], cwd=self.dep, check=True)
        self.skill = self.base / "installed skill"
        shutil.copytree(RUNTIME, self.skill, ignore=shutil.ignore_patterns("__pycache__", ".installation.json"))
        (self.skill / ".installation.json").write_text(json.dumps({"commit": PIN, "dependency": str(self.dep)}))
        self.runner = self.skill / "scripts/run-animdiagram.py"

    def run_tool(self, *args, env=None, profile=None):
        command = [sys.executable, "-I"]
        if profile is not None:
            command += [str(SOURCE / "tests/isolated_home.py"), str(profile)]
        return subprocess.run([*command, str(self.runner), *map(str, args)],
                              cwd=self.base, capture_output=True, text=True, env=env)

    def blocked(self, *args):
        result = self.run_tool(*args)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("execution blocked", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_valid_install_and_silent_template(self):
        result = self.run_tool("verify")
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "Integrity: PASS\n", ""))
        output = self.base / "docs with spaces/diagrams/design-flow.svg"
        result = self.run_tool("template", output)
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))
        self.assertEqual(output.read_bytes(), (self.dep / "assets/template.svg").read_bytes())
        original = output.read_bytes()
        self.assertNotEqual(self.run_tool("template", output).returncode, 0)
        self.assertEqual(output.read_bytes(), original)

    def test_inline_native_example_uses_pinned_defaults(self):
        example = re.search(r'```json\s*(.*?)```', (self.skill / 'SKILL.md').read_text(), re.DOTALL)
        self.assertIsNotNone(example)
        value = json.loads(example.group(1))
        spec, svg = self.base / 'inline.spec.json', self.base / 'inline.svg'
        spec.write_text(json.dumps(value))
        self.assertEqual(self.run_tool('template', svg).returncode, 0)
        compiled = self.run_tool('timeline', spec, '--inject', svg)
        self.assertEqual(compiled.returncode, 0, compiled.stdout + compiled.stderr)
        self.assertIn('loop 9s', compiled.stdout)
        self.assertIn('request-ring', svg.read_text())
        # Compare actual output to explicit pinned defaults, rather than duplicated prose.
        implicit = svg.read_bytes()
        value['loop'] = 9
        for event in value['events']:
            event.update(travel=.6, ring=True)
        spec.write_text(json.dumps(value))
        self.assertEqual(self.run_tool('timeline', spec, '--inject', svg).returncode, 0)
        self.assertEqual(svg.read_bytes(), implicit)

    def test_changed_script_is_not_executed(self):
        sentinel = self.base / "executed"
        (self.dep / "scripts/timeline.py").write_text(f"open({str(sentinel)!r}, 'w').write('BAD')\n")
        self.blocked("timeline", "anything.json")
        self.assertFalse(sentinel.exists())

    def test_missing_file_blocks(self):
        (self.dep / "references/layout.md").unlink()
        self.blocked("verify")

    def test_malformed_configuration_fails_concisely(self):
        for data in (None, [], {"commit": PIN, "dependency": None}):
            with self.subTest(data=data):
                (self.skill / ".installation.json").write_text(json.dumps(data))
                self.blocked("verify")

    def test_different_commit_even_identical_tree_blocks(self):
        # New commit with the same tree: hashes pass, but pin must fail.
        tree = subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=self.dep, text=True).strip()
        env = {**os.environ, "GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.invalid",
               "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "test@example.invalid"}
        commit = subprocess.check_output(["git", "commit-tree", tree, "-p", PIN, "-m", "Test newer commit"], cwd=self.dep, env=env, text=True).strip()
        subprocess.run(["git", "update-ref", "HEAD", commit], cwd=self.dep, check=True)
        self.blocked("verify")

    def test_symlink_with_same_bytes_blocks(self):
        original = self.dep / "scripts/timeline.py"
        copy = self.base / "external.py"
        copy.write_bytes(original.read_bytes())
        original.unlink()
        original.symlink_to(copy)
        self.blocked("verify")

    def test_added_tracked_file_blocks(self):
        (self.dep / "extra.py").write_text("pass\n")
        subprocess.run(["git", "add", "extra.py"], cwd=self.dep, check=True)
        self.blocked("verify")

    def test_python_environment_cannot_inject_code(self):
        sentinel = self.base / "injected"
        poison = self.base / "poison"
        poison.mkdir()
        payload = f"open({str(sentinel)!r}, 'w').write('BAD')\n"
        (poison / "sitecustomize.py").write_text(payload)
        (self.dep / "scripts/json.py").write_text(payload)
        env = {**os.environ, "PYTHONPATH": str(poison)}
        result = self.run_tool("timeline", self.dep / "assets/example-async-jobs.spec.json", "--table", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(sentinel.exists())
        self.assertNotIn("Integrity:", result.stdout)

    def test_preview_launch_and_abbreviation_blocked(self):
        for flag in ("--open", "--op", "--ope", "--open=true"):
            with self.subTest(flag=flag):
                result = self.run_tool("preview", self.dep / "assets/example-async-jobs.svg", flag)
                self.assertEqual(result.returncode, 2)
                self.assertIn("automatic browser launch", result.stderr)
        self.assertNotEqual(self.run_tool("export", "anything.svg").returncode, 0)

    def test_preview_file_only_and_real_compile(self):
        svg = self.base / "example.svg"
        svg.write_bytes((self.dep / "assets/example-async-jobs.svg").read_bytes())
        for args in (("timeline", self.dep / "assets/example-async-jobs.spec.json", "--inject", svg),
                     ("check", svg, "--strict"), ("skin", svg, "--to", "light"),
                     ("preview", svg, "--out", self.base / "preview.html")):
            result = self.run_tool(*args)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.base / "preview.html").is_file())

    def test_installer_existing_dependency_and_rerun(self):
        target = self.base / "new skill"
        args = ("setup", "--skill-dir", target, "--dependency-dir", self.dep)
        first = self.run_tool(*args)
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertTrue((target / "SKILL.md").is_file())
        again = self.run_tool(*args)
        self.assertEqual(again.returncode, 0, again.stdout + again.stderr)
        (target / "SKILL.md").write_text("customized")
        self.assertEqual(self.run_tool(*args).returncode, 2)
        self.assertEqual((target / "SKILL.md").read_text(), "customized")

    def test_installed_references_and_personal_preferences_are_separate(self):
        profile = self.base / "isolated home"
        preferences = profile / ".claude/sl-svg-diagram/preferences.md"
        target = profile / ".claude/skills/sl-svg-diagram"
        args = ("setup", "--skill-dir", target, "--dependency-dir", self.dep)
        # An absent profile stays absent: setup does not manufacture preferences.
        result = self.run_tool(*args, profile=profile)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(preferences.exists())
        preferences.parent.mkdir(parents=True)
        original = b"Personal rule: preserve this exact file.\n"
        preferences.write_bytes(original)
        shutil.rmtree(target)
        result = self.run_tool(*args, profile=profile)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(preferences.read_bytes(), original)
        self.assertFalse((target / "preferences.md").exists())
        # Authoring references resolve from the installed bundle, not cwd.
        for document in [target / "SKILL.md", *sorted((target / "references").glob("*.md"))]:
            prose = re.sub(r"```.*?```", "", document.read_text(), flags=re.DOTALL)
            for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", prose):
                parsed = urlsplit(link)
                if parsed.scheme:
                    continue
                path = unquote(parsed.path)
                if path:
                    self.assertTrue((document.parent / path).is_file(), (document, link))
        self.assertTrue((target / "references/reading-diagrams.md").is_file())
        # Missing preferences still permit the current manual workflow.
        preferences.unlink()
        runner = target / "scripts/run-animdiagram.py"
        result = subprocess.run([sys.executable, "-I", str(SOURCE / "tests/isolated_home.py"), str(profile), str(runner), "template",
                                 str(self.base / "without preferences.svg")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(preferences.exists())

    def test_nested_document_links_resolve_with_spaces(self):
        document = self.base / "nested docs/design notes.md"
        assets = document.parent / "custom assets"
        assets.mkdir(parents=True)
        svg = assets / "request flow.svg"
        companion = svg.with_suffix(".agent.md")
        result = self.run_tool("template", svg)
        self.assertEqual(result.returncode, 0, result.stderr)
        companion.write_text("Illustrative request flow.\n")
        document.write_text("![Flow](custom%20assets/request%20flow.svg)\n"
                            "[Diagram semantics](custom%20assets/request%20flow.agent.md)\n")
        links = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", document.read_text())
        resolved = [(document.parent / unquote(link)).resolve() for link in links]
        self.assertEqual(resolved, [svg.resolve(), companion.resolve()])
        self.assertTrue(all(path.is_file() for path in resolved))

    def test_exact_lean_bundle_excludes_unknown_source_files_and_regenerates_config(self):
        for name in ('unexpected.txt', 'preferences.md', 'private/review.log', 'tests/leak.py',
                     'scripts/unknown.py', '__pycache__/secret.pyc'):
            path = self.skill / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b'not a runtime asset')
        # Setup must generate its own configuration, never copy this source config.
        (self.skill / '.installation.json').write_text('{"commit":"old","dependency":"/do-not-copy"}')
        target = self.base / 'lean runtime'
        result = self.run_tool('setup', '--skill-dir', target, '--dependency-dir', self.dep)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        def installed_files(root):
            return {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
        expected = BUNDLE | {'.installation.json'}
        self.assertEqual(installed_files(target), expected)
        self.assertEqual(json.loads((target / '.installation.json').read_text()),
                         {'commit': PIN, 'dependency': str(self.dep)})
        for name in BUNDLE:
            self.assertEqual((target / name).read_bytes(), (self.skill / name).read_bytes())
        runner = target / 'scripts/run-animdiagram.py'
        native = self.base / 'native.svg'
        result = subprocess.run([sys.executable, '-I', str(runner), 'template', str(native)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(installed_files(target), expected)
        for destination in (target, self.base / 'second lean runtime'):
            result = subprocess.run([sys.executable, '-I', str(runner), 'setup',
                                     '--skill-dir', str(destination), '--dependency-dir', str(self.dep)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(installed_files(destination), expected)

    def test_every_runtime_file_is_required_before_verification_or_setup(self):
        for name in sorted(BUNDLE):
            with self.subTest(name=name):
                path = self.skill / name
                original = path.read_bytes()
                path.unlink()
                try:
                    if name == 'scripts/run-animdiagram.py':
                        # Python itself must refuse a missing entrypoint.
                        self.assertNotEqual(self.run_tool('verify').returncode, 0)
                    else:
                        self.blocked('verify')
                finally:
                    path.write_bytes(original)
        missing = self.skill / 'references/reading-diagrams.md'
        missing.unlink()
        target = self.base / 'incomplete install'
        result = self.run_tool('setup', '--skill-dir', target, '--dependency-dir', self.dep)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(target.exists())

    def test_extra_or_linked_installed_content_is_preserved_and_refused(self):
        target = self.base / 'lean runtime'
        args = ('setup', '--skill-dir', target, '--dependency-dir', self.dep)
        self.assertEqual(self.run_tool(*args).returncode, 0)
        extra = target / 'personal note.md'
        extra.write_text('keep my note')
        before = {p.relative_to(target):p.read_bytes() for p in target.rglob('*') if p.is_file()}
        self.assertEqual(self.run_tool(*args).returncode, 2)
        self.assertEqual(before, {p.relative_to(target):p.read_bytes() for p in target.rglob('*') if p.is_file()})
        extra.unlink()
        # A linked expected directory must not redirect writes outside the install.
        original = target / 'references'
        external = self.base / 'external references'
        original.rename(external)
        original.symlink_to(external, target_is_directory=True)
        self.assertEqual(self.run_tool(*args).returncode, 2)
        self.assertTrue(original.is_symlink())
        self.assertEqual((external / 'reading-diagrams.md').read_bytes(), (self.skill / 'references/reading-diagrams.md').read_bytes())

    def test_repository_smoke_uses_installed_runtime_without_installed_tests(self):
        target = self.base / 'lean runtime'
        self.assertEqual(self.run_tool('setup', '--skill-dir', target, '--dependency-dir', self.dep).returncode, 0)
        self.assertFalse((target / 'tests').exists())
        output = self.base / 'smoke outputs'
        result = subprocess.run([sys.executable, '-I', str(SOURCE / 'tests/smoke.py'),
                                 '--skill-dir', str(target), '--output-dir', str(output), '--skip-integration'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        svg = output / 'nested docs/diagrams/request flow.svg'
        self.assertTrue(svg.is_file())
        self.assertTrue(svg.with_suffix('.agent.md').is_file())
        self.assertFalse(list(output.rglob('*.html')))
        preview_output = self.base / 'explicit preview outputs'
        result = subprocess.run([sys.executable, '-I', str(SOURCE / 'tests/smoke.py'),
                                 '--skill-dir', str(target), '--output-dir', str(preview_output),
                                 '--skip-integration', '--preview'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((preview_output / 'nested docs/diagrams/request flow.preview.html').is_file())
        self.assertFalse((target / 'tests').exists())

    def test_installer_refuses_bad_dependency(self):
        (self.dep / "scripts/skin.py").write_text("changed")
        target = self.base / "new skill"
        result = self.run_tool("setup", "--skill-dir", target, "--dependency-dir", self.dep)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(target.exists())

    def test_snapshot_uses_verified_bytes_after_checkout_changes(self):
        spec = importlib.util.spec_from_file_location("audited_runner", self.runner)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        data = module.verified_bytes(self.dep, module.manifest())
        sentinel = self.base / "race"
        (self.dep / "scripts/check.py").write_text(f"open({str(sentinel)!r}, 'w').write('BAD')\n")
        rc = module.execute(data, "check", [str(self.dep / "assets/template.svg")])
        self.assertEqual(rc, 0)
        self.assertFalse(sentinel.exists())


if __name__ == "__main__":
    if CHECKOUT is None:
        raise SystemExit("Usage: test_wrapper.py /path/to/audited/animdiagram")
    unittest.main(verbosity=2)
