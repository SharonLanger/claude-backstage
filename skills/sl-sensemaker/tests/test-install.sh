#!/bin/sh
# Run from any directory. All writes go to a disposable home.
set -eu
skill=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
sandbox=$(mktemp -d)
trap 'rm -rf "$sandbox"' EXIT
test_home="$sandbox/test home"
cache="$test_home/.cache/sl-knowledge-atlas"
entry="$test_home/.claude/skills/sl-sensemaker/SKILL.md"

cd "$sandbox"
env HOME="$test_home" "$skill/setup.sh"
cmp "$skill/SKILL.md" "$entry"
grep -Fxq 'name: sl-sensemaker' "$entry"
grep -Fxq "  - 'Read(~/.cache/sl-knowledge-atlas/**)'" "$entry"
diff -r "$skill/catalog" "$cache/catalog"
cmp "$skill/bridge-file.md" "$cache/bridge-file.md"
cmp "$skill/catalog-inventory.md" "$cache/catalog-inventory.md"

# The first end-to-end route starts at a real symptom and ends at the primary entry.
ap=anti-patterns/AP10-overpowered-coding-agent.md
test_pattern=families/D-verification-evaluation/patterns/D02-test-before-done.md
grep -F 'deletes failing tests' "$cache/bridge-file.md" | grep -Fq "(catalog/$ap)"
grep -F 'deletes failing tests' "$cache/bridge-file.md" | grep -Fq "(catalog/$test_pattern)"
grep -F 'Agent changes or deletes the regression test' "$cache/catalog/catalog-lookup.md" | grep -F "($ap)" | grep -Fq "($test_pattern)"
grep -Fq 'test suite is authored independently of the agent and cannot be modified by it' "$cache/catalog/$test_pattern"
grep -Fq 'CSS styling task' "$cache/catalog/$ap"
grep -Fq 'Read-only access to non-CSS files' "$cache/catalog/$ap"
printf 'Covered route reaches %s and %s\n' "catalog/$ap" "catalog/$test_pattern"
test -z "$(find "$cache" -name practitioner-coverage.md -print)"

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
grep -F './skills/sl-sensemaker/setup.sh`, then try `/sl-sensemaker' "$entry"
printf 'Missing-catalog fixture created and installed recovery instruction verified.\n'
