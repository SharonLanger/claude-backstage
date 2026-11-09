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

> When reading a diagram, follow `~/.claude/skills/sl-svg-diagram/references/reading-diagrams.md`: read surrounding Markdown and the matching `.agent.md` before SVG source.

Use the actual installed path if you chose a custom installation. This is a plain path reference, not an `@` import; load the guide only when reading diagrams.

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

Setup installs an explicit 17-file runtime bundle: `SKILL.md`, the five authoring/reading references, four wrapper/generation/preview scripts, versioned defaults, the audited hash manifest, MIT notice, and four compact specs in `examples/`. It generates `.installation.json` for the selected dependency path. Repository README/audit prose, tests, generated example SVGs/companions and showcase assets stay in this checkout. Unknown source files and caches are never copied. The complete pinned dependency checkout remains separate and unchanged.

A lean installation can rerun its setup script to another fresh destination using the same supported arguments. Setup refuses installations with different contents or extra files, including earlier larger bundles; back up/move those yourself or choose a fresh `--skill-dir`. It never deletes user files or changes personal preferences.

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

## Preferences and authoring

Personal settings belong in `~/.claude/sl-svg-diagram/preferences.md`, outside the installation. Missing preferences use [shipped defaults](references/diagram-rules.md); setup never creates or overwrites personal settings. Task instructions take precedence, followed by personal preferences, then defaults. Correctness, integrity, and privacy remain mandatory.

The skill adapts to your saved preferences. A one-time correction updates the current diagram; an explicit “remember this” request or accepted proposal saves a scoped rule. See [the preference workflow](references/diagram-rules.md#saved-preferences). Reinstallation preserves personal settings.

[Authoring commands and verification](references/authoring.md) cover the usable manual template/timeline route, light variants, and optional HTML previews with the existing playback controls. Compact semantic JSON and three layout presets are available through `build`; see [schema and examples](references/generation.md). Add `--preview` to build optional [scenario-selecting HTML](references/preview.md) with `All` and named scenario choices, preserving pause/scrub/static/background/zoom controls. HTML is optional; animated SVG remains the normal deliverable.

[Reading guide](references/reading-diagrams.md) gives fresh reading sessions a short route to meaning without loading the full authoring skill. Guidance is not enforcement; review transcripts to assess unnecessary SVG reads. Token savings depend on actual avoided reads and have not been measured for these changes.

## Development checks

Run repository test code against a disposable installed runtime; tests are not installed. Requires Git/Python 3.10+ and a cached checkout at the audited commit. Setup downloads only when installation is requested and its dependency destination is absent. Reuse a verified cached checkout for offline runs; tests mutate disposable clones.

```sh
python3 -I skills/sl-svg-diagram/tests/run.py /absolute/cached/animdiagram
bash skills/sl-svg-diagram/scripts/setup-animdiagram.sh --skill-dir /temporary/skill --dependency-dir /absolute/cached/animdiagram
python3 -I skills/sl-svg-diagram/tests/run.py /absolute/cached/animdiagram --skill-dir /temporary/skill
python3 -I skills/sl-svg-diagram/tests/smoke.py --skill-dir /temporary/skill --output-dir /temporary/fresh-output
python3 -I skills/sl-svg-diagram/tests/measure_cost.py --skill-dir /temporary/skill --output-dir /temporary/fresh-cost-output
```

Use fresh disposable destinations, never the user's installed skill/profile/dependency as a mutation fixture. The smoke runner uses installed `examples/` and wrapper, parses generated SVG/companions, checks repeatability and legacy ambient metadata, and calls repository integration/integrity tests against that installed runtime. It exits nonzero on required failure and reports artifacts. `--output-dir` must be fresh; omit it for a retained temporary directory. `--skip-integration` runs only the fixture smoke and explicitly reports that the integration suite was skipped.

The cost runner uses the installed generator/defaults/example and verified wrapper. It compares equivalent reconstructed manual static SVG/motion JSON against compact semantic JSON for a creation and label refinement, recording authoring/changed-character proxies, wrapper calls and returned tool-output characters. These are not token measurements or live Claude runs; model usage/source-read counts are unavailable and no percentage token saving is claimed.

Browser checks are separate. In an approved OS network namespace with Python Playwright and Chromium already installed:

```sh
unshare --user --map-root-user --net python3 skills/sl-svg-diagram/tests/browser_layout.py --examples-dir /temporary/fresh-output --output-dir /temporary/layout-evidence
unshare --user --map-root-user --net python3 skills/sl-svg-diagram/tests/browser_preview.py --examples-dir /temporary/fresh-output --output-dir /temporary/playback-evidence
```

The runners require no default route and a failed external socket probe. Four semantic fixtures are checked at intended/narrow widths; auxiliary legacy fixtures are covered by playback. Full browser cycles inspect actual opacity/transforms, choices/exclusivity, boundaries/tails/pauses/reset, controls, real speed, ambient periods, standalone image animation and reduced motion. For SVG image documents Chromium here requires a separate browser with `--force-prefers-reduced-motion=reduce` plus explicit page context; page-level emulation alone does not propagate into those images. Screenshots/JSON are retained outside the repository. Narrow branch/grid/enum labels still need alternate layouts at 360px; passing bounds does not establish readability.

Actual installed Claude acceptance remains separate and pending when CLI/authentication are unavailable. Verify real tool calls and artifacts for boolean/grid/enum creation, one-time versus remembered preferences in an explicit temporary profile, and a fresh reading session. Deterministic tests, browser renders and a final assistant message do not prove live skill use.

[Skill instructions](SKILL.md) · [All skills](../README.md)
