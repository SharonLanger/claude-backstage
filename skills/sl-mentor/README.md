# SL Mentor

Ask Claude Code about a problem you’re seeing with an AI agent. Describe what happened and what you expected. The mentor asks for any context it needs, looks up the symptom in the installed pattern catalog, and suggests a next step with the local file that supports it.

## Install

From the root of your Claude Backstage checkout, run:

```sh
./skills/sl-mentor/setup.sh
claude
```

Setup uses a POSIX shell and standard file utilities. It installs the command at `~/.claude/skills/sl-mentor/SKILL.md` and copies the catalog, bridge and inventory into `~/.cache/sl-mentor/`. The skill reads its data from there, so you can use it from any project. Catalog lookup requires no network access.

## Try it

Paste this into Claude Code:

```text
/sl-mentor I asked my agent to fix the padding on a button. It made CI green by disabling the failing check. How should I scope its access next time?
```

Look for an explanation grounded in [Overpowered Coding Agent](catalog/anti-patterns/AP10-overpowered-coding-agent.md), which describes this failure. You can also type `/sl-mentor` on its own and describe your situation conversationally. If the catalog covers only part of a question, the mentor identifies the remaining gap.

## Update or repair

From the checkout, run:

```sh
git pull --ff-only
./skills/sl-mentor/setup.sh
```

Setup refreshes files supplied by the checkout, so keep local additions in files with their own names. If the installed catalog is missing, rerun setup. If Claude reports that it cannot read the cache, check your Claude Code read permissions for `~/.cache/sl-mentor/`.

## Catalog coverage

The [bridge](bridge-file.md) maps familiar symptoms to candidate entries. The [lookup](catalog/catalog-lookup.md) offers another way in when a symptom has no bridge row. Recommendations come from reading the entries themselves. Future patterns can use this same layout and add bridge routes as they are approved.
