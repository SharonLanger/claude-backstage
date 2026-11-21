"""Check local Markdown links in the skill. Requires Python 3 and Pandoc."""

import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def nodes(node):
    if isinstance(node, dict):
        yield node
        yield from nodes(node.get("c"))
    elif isinstance(node, list):
        for child in node:
            yield from nodes(child)


def main():
    root = Path(__file__).resolve().parents[1]
    headings = {}
    links = []
    for path in sorted(root.rglob("*.md")):
        document = subprocess.check_output(
            ["pandoc", "-f", "gfm", "-t", "json", str(path)], text=True
        )
        headings[path] = set()
        for item in nodes(json.loads(document)["blocks"]):
            kind = item.get("t")
            if kind == "Header":
                headings[path].add(item["c"][1][0])
            elif kind in {"Link", "Image"}:
                href = item["c"][-1][0]
                uri = urlsplit(href)
                if not (uri.scheme or uri.netloc):
                    links.append((path, href, uri))

    failed = 0
    for source, href, uri in links:
        target = (source.parent / unquote(uri.path)).resolve() if uri.path else source
        if target.is_dir():
            target = target / "README.md"
        if not target.is_file() or (
            uri.fragment and unquote(uri.fragment) not in headings.get(target, set())
        ):
            print(f"{source.relative_to(root)} -> {href}", file=sys.stderr)
            failed += 1
    print(f"{len(links)} local Markdown links checked, {failed} unresolved.")
    return bool(failed)


if __name__ == "__main__":
    sys.exit(main())
