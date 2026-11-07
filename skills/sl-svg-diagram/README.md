# SL SVG diagram

Create animated SVG walkthroughs showing how inputs select different branches, API calls, and method chains. Each diagram includes a concise `.agent.md` companion.

## Install and use

Requires Git, Bash, and Python 3.10+. While this skill is in draft PR #1:

```sh
git clone --branch skill/svg-diagram https://github.com/SharonLanger/claude-backstage.git
cd claude-backstage
bash skills/sl-svg-diagram/scripts/setup-animdiagram.sh
```

Already have this branch checked out? Run only the setup command. It downloads and verifies the pinned dependency, runs its tests, installs the skill, and checks the installed configuration.

Start a new Claude Code session:

```text
/sl-svg-diagram docs/design.md Show enabled=true and enabled=false and the methods each calls
```

Claude may also select it for relevant documentation work. This illustrates scenarios, not live execution.

Check installation at any time:

```sh
python3 -I ~/.claude/skills/sl-svg-diagram/scripts/run-animdiagram.py verify
```

Success prints `Integrity: PASS`. Normal commands verify **silently on every invocation**, with no extra model call.

## Installation and integrity

The skill lives in `~/.claude/skills/sl-svg-diagram/`; its dependency lives separately in `~/.local/share/sl-svg-diagram/animdiagram/<commit>/`. Optional setup arguments: `--skill-dir /absolute/project/.claude/skills/sl-svg-diagram` and `--dependency-dir /absolute/cache/path`.

The wrapper requires commit **`a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486`** and verifies all 62 audited file hashes before executing a temporary snapshot of those bytes. A different commit, changed/missing file, or altered tracked-file set blocks execution—even if you accidentally pull a newer version. Untracked code is not executed.

There are no automatic updates or repairs. Setup refuses to overwrite a different/customized installation. Back up and move a mismatched installation/dependency out of its configured location, then rerun setup. Do not alter the manifest to accept unknown changes.

## Audit and privacy

Uses MIT-licensed [animdiagram](https://github.com/praveenvijayan/animdiagram), pinned to an audited commit, not a release tag. The November 7, 2026 audit found **no network syscalls during tested core generation**: 8/8 upstream tests passed and 11/11 example specs regenerated exactly.

**The whole checkout is not guaranteed offline.** Its gallery loads Google Fonts, Chromium attempted background connections, and the SVG checker misses some external-resource forms. Test connections were blocked. This wrapper excludes gallery execution, automatic browser opening, and video export. Visual inspection requires an externally enforced offline browser; setup does not configure that policy. Your approved enterprise Claude connection is separate.

[Full audit, results, and limitations](audit/animdiagram-audit.md). Hash checks detect dependency changes; they do not certify arbitrary generated SVG, your runtime, or malicious changes to the wrapper itself. Re-audit before changing the pin.

## Files and agent context

```text
docs/design.md
docs/diagrams/design-request-flow.svg
docs/diagrams/design-request-flow.spec.json
docs/diagrams/design-request-flow.agent.md
```

Existing asset conventions or explicit destinations take precedence. Markdown links to the animated image and its semantic companion; the spec preserves editable timing.

To discourage fresh agents from reading verbose SVG source, add to your project's `CLAUDE.md`:

> For diagram meaning, read surrounding Markdown or the matching `.agent.md` file. Read SVG source only when editing or debugging the visual.

Illustrative break-even: a ~40-token rule offsets one avoided simple SVG read after ~18 fresh context loads, or a detailed read after ~188. These are estimates; caching and repeated input processing affect billing separately. [Calculation and future enforcement](audit/animdiagram-audit.md#agent-context-and-future-enforcement).

A future script/hook or [System One Harness](https://github.com/SharonLanger/system-one-harness) flow could redirect reads to companions. That integration is **not implemented or verified** here.

[Skill instructions](SKILL.md) · [All skills](../README.md)
