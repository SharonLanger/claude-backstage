#!/bin/sh
# Run from any directory. All writes go to a disposable home.
set -eu
skill=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
sandbox=$(mktemp -d)
trap 'rm -rf "$sandbox"' EXIT
test_home="$sandbox/test home"
cache="$test_home/.cache/sl-mentor"
entry="$test_home/.claude/skills/sl-mentor/SKILL.md"

cd "$sandbox"
env HOME="$test_home" "$skill/setup.sh"
cmp "$skill/SKILL.md" "$entry"
diff -r "$skill/catalog" "$cache/catalog"
cmp "$skill/bridge-file.md" "$cache/bridge-file.md"
cmp "$skill/catalog-inventory.md" "$cache/catalog-inventory.md"

# The first end-to-end route starts at a real symptom and ends at the primary entry.
ap=anti-patterns/AP10-overpowered-coding-agent.md
grep -F 'deletes failing tests' "$cache/bridge-file.md" | grep -Fq "(catalog/$ap)"
grep -Fq "($ap)" "$cache/catalog/catalog-lookup.md"
grep -Fq 'CSS styling task' "$cache/catalog/$ap"
grep -Fq 'Read-only access to non-CSS files' "$cache/catalog/$ap"
printf 'Covered route reaches %s\n' "catalog/$ap"

# Simulate stale installed content and a user addition between installs.
printf 'stale file\n' > "$cache/catalog/$ap"
printf 'local addition\n' > "$cache/catalog/local-note.md"
env HOME="$test_home" "$skill/setup.sh"
cmp "$skill/catalog/$ap" "$cache/catalog/$ap"
grep -Fxq 'local addition' "$cache/catalog/local-note.md"
test ! -e "$cache/catalog/catalog"
rm "$cache/catalog/local-note.md"
diff -r "$skill/catalog" "$cache/catalog"
printf 'Second install restored the entry and preserved the addition. No nested catalog.\n'

mv "$cache/catalog" "$sandbox/absent-catalog"
test ! -f "$cache/catalog/catalog-lookup.md"
grep -F 'From your Claude Backstage checkout, run' "$entry"
printf 'Missing-catalog fixture created and installed recovery instruction verified.\n'
