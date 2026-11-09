# SL SVG Diagram — make explanations move

Create animated SVG explanations embedded in Markdown. Claude writes grounded semantic JSON; a bounded layout generator computes the drawing and native motion JSON, the pinned [AnimDiagram](https://github.com/praveenvijayan/animdiagram) compiler animates it, and the builder formats a companion from the supplied facts. Common creation needs no reference reads beyond task sources and optional personal preferences.

![Traveling packets, a filling gauge and synchronized worker pulses](sl-diagrams/readme-motion-showcase.svg)

Illustrative native mechanisms, not live telemetry. [Meaning](sl-diagrams/readme-motion-showcase.agent.md) · [Native editable JSON](sl-diagrams/readme-motion-showcase.spec.json). This showcase uses the supported native route for motion beyond the semantic presets.

## Install and use

Requires Git, Bash and Python 3.10+:

```sh
git clone https://github.com/SharonLanger/claude-backstage.git
cd claude-backstage
bash skills/sl-svg-diagram/scripts/setup-animdiagram.sh
```

If already cloned, reuse that checkout: update to the reviewed revision and run setup. The shell launcher stays in the repository; the installed Python wrapper also supports `setup`.

Default skill: `~/.claude/skills/sl-svg-diagram/`. Separate dependency: `~/.local/share/sl-svg-diagram/animdiagram/a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486/`. Override with `--skill-dir /absolute/fresh/skill --dependency-dir /absolute/cache/animdiagram`. A clean matching cached checkout is reused. Setup can download the pinned dependency when absent; runtime calls never download or repair it.

The runtime allowlist copies exactly **eight assets**: `SKILL.md`, `references/reading-diagrams.md`, `references/options.md`, `scripts/run-animdiagram.py`, `scripts/generate.py`, `defaults/v1.json`, `audit/verified-files.sha256`, and `notices/animdiagram-MIT.txt`. Setup generates `.installation.json`, making nine installed files. Tests, examples, README, audit prose, showcase, setup launcher and caches stay in the repository. The separate dependency checkout stays complete. Setup runs upstream tests and verifies the installed configuration.

Setup refuses differing/customized installations, extra files and symlinks, preserving user files. Earlier bundles require a fresh `--skill-dir` or backing up/moving the old destination before reinstalling. For reinstalling, moving/removing only the old skill directory is sufficient; keeping the clean pinned dependency cache is fine. To uninstall, remove the skill directory after checking for user additions. Cache deletion is optional when no longer needed. Personal preferences live outside both.

Start a new Claude session:

```text
/sl-svg-diagram docs/design.md Explain enabled=true and enabled=false and their actual method calls
```

In projects with diagrams, optionally add this plain path guidance to their `CLAUDE.md` (adjust custom paths):

> When reading a diagram, follow `~/.claude/skills/sl-svg-diagram/references/reading-diagrams.md`: read surrounding Markdown and the matching `.agent.md` before SVG source.

This is conditional guidance, not an import or access restriction. Setup never changes project/global `CLAUDE.md`.

## Semantic creation and rebuild

The installed [skill](SKILL.md) includes a complete valid JSON example. Repository fixtures show [flow](examples/flow.spec.json), [true/false branch](examples/branch.spec.json), [six peers](examples/grid.spec.json) and [enum cases](examples/enum.spec.json). Examples are test fixtures and are not copied into the installation.

`<skill>` is the absolute installed directory. Save semantic JSON beside the desired SVG:

```sh
python3 -I <skill>/scripts/run-animdiagram.py build /absolute/diagrams/request.spec.json --out /absolute/diagrams/request.svg
```

The builder validates `sl-diagram/v1`, applies versioned defaults and explicit saved overrides, generates static SVG plus intermediate motion JSON, runs the verified compiler/checker, checks XML and emitted animation visibility boundaries, then writes SVG and `.agent.md`. Successful output is a short paths/summary message. Intermediate motion is temporary; `--debug-normalized /absolute/new.json` explicitly saves diagnostic geometry, motion and scenario windows. The semantic input is never rewritten.

Presets preserve meaning:

| Preset | Supported relationships |
|---|---|
| `flow` | One ordered chain, including six or more ordered steps. |
| `branch` | Connected rooted tree, one parent per non-root node; no merges/cycles. |
| `grid` | Independent peers, no links, up to three columns. Choose it above five independent items. |

Boolean and enum cases share fixed geometry and play sequentially in authored order. A scenario step is a node pulse, a routed link packet, or an explicitly parallel group. Ordinary steps are sequential; the generator never infers program behavior or drops unsupported links. Use scenario labels for inputs/conditions and explanation for context/assumptions. Companions format those supplied facts, sequence/concurrency, outcomes, notes, timing assumptions and source links; Claude verifies they faithfully describe the task.

Limits: 1–20 nodes, at most 30 links, 1–8 scenarios, 30 top-level steps per scenario, 120 simple steps total, and a 250-second compiler precision budget. Parallel groups contain 2–8 distinct simple steps without nesting. Unknown schema/settings fields, duplicate JSON keys/IDs, bad references, nonfinite numbers and unsupported topology fail. See the small [optional reference](references/options.md) for settings ranges, text limits and native fallback. No arbitrary graph engine is included; Archify and scenario selectors remain deferred.

Scripts own margins/gaps, wrapping, tag heights, title/claim, side panel/gutter, scenario/outcome/footer clearance, palette and timing defaults. Intended `document_width` defaults to 1000; layouts shrinking text below 11px at that width fail. Actual narrow embeds can still be unreadable and need a separate layout. Keep feedback in semantic JSON and rebuild; generated SVG/companion ownership markers prevent overwriting manual files. Symlink outputs fail. Validation/compilation failure preserves previous outputs. Each output replacement is atomic; a filesystem failure during replacements does not provide multi-file rollback.

Earlier `sl-diagram/v1` inputs remain supported. Generated outputs no longer carry selector metadata or custom HTML/JavaScript. Manual/native inputs remain a separate supported route.

Keep `<stem>.spec.json`, `<stem>.svg`, and `<stem>.agent.md` together under the target document's asset convention, otherwise sibling `diagrams/`. Embed relative image and companion links, encoding spaces:

```markdown
![Animated request flow](diagrams/request.svg)
[Diagram meaning](diagrams/request.agent.md)
```

Read existing `~/.claude/sl-svg-diagram/preferences.md` only if present. Task directions override preferences/defaults. Save supported overrides into the semantic JSON for reproducible rebuilds; changing personal Markdown later does not change saved diagrams. Save a personal rule only on explicit request or an accepted suggestion. Setup never writes preferences.

## Native authoring and optional preview

For merges/cycles, custom layout, streams/bars or moving groups, follow [the optional reference](references/options.md). The wrapper retains `template`, `timeline`, `check`, `skin`, `preview` and upstream `test`. Native authoring uses static SVG coordinates plus native motion JSON and a companion authored from grounded facts. Choose a fresh output when migrating manual work.

Only on explicit request, create native HTML:

```sh
python3 -I <skill>/scripts/run-animdiagram.py preview /absolute/diagrams/request.svg
```

Preview provides upstream playback controls; scenario dropdowns are deferred. Its pause handler does not reliably freeze CSS animations, so inspect scrub/static frames. Default `build` creates no HTML. Optional `skin <svg> --to light` derives the upstream fixed light palette; reapply derivatives after semantic rebuilds.

Render with enforced outbound network denial covering browser subprocesses. Inspect intended/narrow widths, labels/tags, side/footer clearance, route/order/concurrency meaning, effect tails, outcome pauses/reset and reduced motion. If rendering is unavailable, report visual checks pending. Structural success does not prove visual quality. No automatic browser install/policy changes or publishing.

## Integrity and privacy

Pin: **`a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486`**. Every wrapper call verifies actual HEAD, complete tracked-file set and all 62 audited hashes before executing a temporary snapshot of the verified bytes. Changed/missing files or another commit block execution; untracked code is excluded. There are no automatic updates/repairs. Troubleshoot with `python3 -I <skill>/scripts/run-animdiagram.py verify`.

[Audit and limitations](audit/animdiagram-audit.md): tested core generation made no network syscalls; upstream tests passed 8/8 and 11/11 examples regenerated exactly during that audit. The whole checkout is not guaranteed offline: its gallery loads Google Fonts, browser background traffic was blocked, and its checker misses some external-resource forms. The wrapper blocks gallery execution, browser launch and export. Keep SVG script-free/self-contained: no external fonts/resources, event handlers or `foreignObject`. Never upload private diagrams/source/specs to external diagram services; the approved Claude connection is separate.

The wrapper/generator are project-owned code; dependency hashes do not certify their changes or arbitrary authored SVG. [MIT notice](notices/animdiagram-MIT.txt) accompanies dependency attribution. Re-audit before changing the pin or manifest.

## Development checks

Tests live in the repository and run against disposable copies and installations. Reuse an exact audited checkout offline:

```sh
bash skills/sl-svg-diagram/scripts/setup-animdiagram.sh --skill-dir /temporary/fresh-skill --dependency-dir /absolute/cached/animdiagram
python3 -I skills/sl-svg-diagram/tests/run.py /absolute/cached/animdiagram --skill-dir /temporary/fresh-skill
python3 -I skills/sl-svg-diagram/tests/smoke.py --skill-dir /temporary/fresh-skill --output-dir /temporary/fresh-output
# Explicit native preview variant:
python3 -I skills/sl-svg-diagram/tests/smoke.py --skill-dir /temporary/fresh-skill --output-dir /temporary/other-fresh-output --preview
```

Script smoke builds four repository semantic fixtures through the installed wrapper, checks companions/XML/repeatability/links, exercises native template/timeline/check and runs integration/integrity tests. Default smoke creates no HTML; `--preview` exercises separate native preview. `--skip-integration` reports the skipped suite. Output directories must be fresh; omitting the option retains a temporary directory. No tests/examples are installed and no real user files/profiles are mutated.

`tests/browser_layout.py` checks fixture text bounds at intended/narrow widths. `tests/browser_motion.py` samples each expected packet/pulse, parallel starts, caption exclusivity, reduced motion and text clearance, saving scenario screenshots and `motion.json`. Both repository-only helpers require Chromium and Playwright plus enforced network denial. Example Linux runner (the network namespace covers browser subprocesses):

```sh
unshare --user --map-root-user --net python3 -I skills/sl-svg-diagram/tests/browser_motion.py --examples-dir /temporary/fresh-output/examples --output-dir /temporary/browser-motion
```

Both helpers refuse a default network route or a working external socket. `--names flow branch` selects motion fixtures; the default covers all four. Browser checks complement structural tests. Script smoke is **not a live Claude invocation**: where Claude CLI/API/authentication are unavailable, live skill acceptance remains pending. No token-saving percentage is measured or claimed.

[Skill instructions](SKILL.md) · [All skills](../README.md)
