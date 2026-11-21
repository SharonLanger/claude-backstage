#!/bin/sh
set -eu

: "${HOME:?Set HOME to the directory where Claude Code should find the skill}"
cd -P "$(dirname "$0")"

# Validate the bundle before changing either install location.
for source in SKILL.md catalog/catalog-lookup.md bridge-file.md catalog-inventory.md; do
    if [ ! -f "$source" ] || [ ! -r "$source" ]; then
        printf 'Missing or unreadable %s in the checkout. Restore the skill files and rerun setup.\n' "$source" >&2
        exit 1
    fi
done

skill_dir="$HOME/.claude/skills/sl-mentor"
cache_dir="$HOME/.cache/sl-mentor"
printf 'Installing catalog and navigation files in %s\n' "$cache_dir"
mkdir -p "$cache_dir/catalog"
cp -R catalog/. "$cache_dir/catalog/"
cp bridge-file.md catalog-inventory.md "$cache_dir/"

printf 'Installing skill in %s\n' "$skill_dir"
mkdir -p "$skill_dir"
cp SKILL.md "$skill_dir/SKILL.md"
printf 'Done. Open Claude Code and run /sl-mentor.\n'
