# SL SVG Diagram — make explanations move

Explain methods, APIs, data flow, and system behavior with animated SVGs embedded in Markdown. Show where a request travels, how a value changes, or which operations happen together.

## Pick a motion that explains the idea

![Animated showcase: traveling request packets, a filling gauge, and synchronized worker pulses](sl-diagrams/readme-motion-showcase.svg)

Illustrative designs, not a real API or live telemetry. These are reusable animation mechanisms, not alternative input scenarios. [Diagram meaning](sl-diagrams/readme-motion-showcase.agent.md) · [Editable motion JSON](sl-diagrams/readme-motion-showcase.spec.json)

| Try this | Ask Claude |
|---|---|
| **Follow the call** | “Explain this method with a packet moving through the calls it makes.” |
| **Watch it accumulate** | “Explain batch processing with a gauge that fills as items complete.” |
| **See work happen together** | “Explain these parallel workers with synchronized highlights.” |

Use one mechanism or combine them when it helps the explanation. Every diagram keeps its editable motion JSON and a concise `.agent.md` companion for readers that only need its meaning. SVG animation depends on the Markdown viewer; the labels remain readable when motion is disabled.

## Install and use

Requires Git, Bash, and Python 3.10+:

```sh
git clone https://github.com/SharonLanger/claude-backstage.git
cd claude-backstage
bash skills/sl-svg-diagram/scripts/setup-animdiagram.sh
```

Already have this repository checked out? Run only the setup command. It downloads and verifies the pinned dependency, runs its tests, installs the skill, and checks the installed configuration.

In **each project where you use this skill**, add the following line to that project's root `CLAUDE.md` (create the file if it does not exist). Do not add it to the Claude Backstage repository unless that is the project containing your diagrams. This gives Claude the guidance even when it has not loaded the skill:

> For diagram meaning, read surrounding Markdown or the matching `.agent.md` file. Read SVG source only when creating, editing, or debugging the visual.

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

### Avoid unnecessary SVG reads

Reading Markdown does not normally load the linked SVG source. The extra tokens are spent only if an agent opens the SVG to understand it. This skill already tells agents to read the surrounding Markdown or matching `.agent.md` for meaning, and to read SVG source for editing or debugging. The options below mainly help sessions that have not loaded the skill.

| Option | Benefit | Tradeoff |
|---|---|---|
| Keep the guidance only in the skill | No extra project-wide instruction tokens | Agents that have not loaded the skill may unnecessarily read SVG source |
| Add the setup line to your project's `CLAUDE.md` | Fresh sessions receive the same guidance without loading the skill | Small recurring instruction cost; guidance is not enforcement |
| Add a stateful Read hook (future option) | Intervenes when an SVG read is attempted, without a standing `CLAUDE.md` rule | Requires hook setup and state; a blocked read still costs a short tool response |

The setup line above is guidance, not enforcement. To monitor its effect, review Claude Code transcripts for SVG `Read` calls and check whether each read was needed to create, edit, or debug the visual.

Assuming approximately 40 tokens for the rule, one avoided SVG read pays for the following number of fresh instruction loads:

| Illustrative diagram | SVG source | Companion | Tokens saved per avoided read | Equivalent rule loads |
|---|---:|---:|---:|---:|
| Simple flow | 800 | 100 | 700 | 17.5 (about 18) |
| Detailed flow | 8,000 | 500 | 7,500 | 187.5 (about 188) |

Calculation: `(SVG tokens − companion tokens) / rule tokens`. This is a break-even comparison, not a waiting period: the saving occurs when the unnecessary read is avoided. With only one avoided read, enough subsequent instruction loads eventually consume that saving; additional avoided reads add savings. If the explanation is already in context, the examples become 20 and 200 loads. These are illustrative estimates, not tokenizer measurements.

Count fresh context loads, not elapsed time or every conversation turn. A restart, resume, or compaction counts only when instructions are loaded into a newly constructed context. Context capacity is per session; prompt caching and repeated input processing affect billing separately. [Detailed assumptions](audit/animdiagram-audit.md#agent-context-and-future-enforcement).

For advanced use, a small stateful hook could block the first SVG Read request in a session and point to its matching `.agent.md`, if present. Its short response would explain that retrying the same SVG Read permits source access when needed. A second read of that same resolved path in the same session would pass; reads of other files or in other sessions would not inherit that state. If no companion exists, the response must say so and explain the retry. This is a reminder against accidental context waste, not a security boundary; it does not cover shell or other-tool reads.

You can build that hook yourself, or follow [System One Harness](https://github.com/SharonLanger/system-one-harness) for a planned plugin flow. **The hook and plugin flow are not implemented or verified here.** The Claude Code hook contract and state handling must be checked before implementation.

[Skill instructions](SKILL.md) · [All skills](../README.md)
