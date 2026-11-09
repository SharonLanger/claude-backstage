# Commit 2: compact JSON generation and layout verification

Part of the [implementation plan](sl-svg-diagram-mini-design.md). All work belongs on its dedicated branch and separate PR; no direct default-branch pushes or automatic merge.

## 1. What changes

Add a project-owned layout generator that accepts compact diagram JSON, applies defaults, emits static SVG, and invokes the existing verified motion compiler. Claude describes nodes and behavior; the script handles repeated geometry and SVG markup.

Start with three presets: **sequential flow**, **branching flow**, and **grid of independent peers**. Support only the documented topology for each preset. Report unsupported layouts and use the existing manual workflow instead of silently dropping links or inventing behavior.

Keep the existing motion primitives, relative timing, theme conversion, and marker-based regeneration. Add short recipes for streams, pulses, bars, and moving groups where useful. Do not rewrite the upstream compiler.

## 2. Input and file ownership

Retain three primary assets: `.spec.json`, `.svg`, and `.agent.md`. The optional HTML preview is a derivative.

Extend the wrapper with a proposed `build <spec.json> --out <diagram.svg>` command. This command is planned, not currently available. Recognize a versioned semantic input format, for example `format: "sl-diagram/v1"`. Existing coordinate-based `loop/events` specs continue to work through the current timeline command.

The semantic input should contain:

| Field | Purpose |
|---|---|
| Format and defaults version | Unambiguous validation and reproducible interpretation. |
| Title, claim, explanation, source links | Grounded text for the visual and companion. |
| Layout preset | Flow, branch, or independent grid. |
| Nodes and links with stable IDs | Labels and relationships, without repeated SVG coordinates. |
| Scenarios with IDs, labels, ordered steps and outcomes | One source for animation and preview selection. |
| Typed settings overrides | Effective personal/task preferences relevant to this diagram. |

Steps reference links or nodes by ID. Support relative order and explicit parallel groups; ordinary adjacent steps are sequential. The generator resolves endpoints, orthogonal routes, glow rectangles, durations, pauses, and scenario boundaries. Distinguish illustrative durations from measured timings.

For semantic inputs, the saved spec is authoritative. Generate the low-level motion spec temporarily; an explicit debug option may expose it, but do not create another routinely maintained JSON file. Run that intermediate through the pinned compiler. Share the normalized result with the preview feature in commit 3.

Generate the companion from supplied explanations, scenarios, and source links, never from invented interpretations of coordinates. Make generated-file ownership clear: edit the semantic spec and rebuild. The legacy manual workflow remains available for hand-authored SVGs; do not overwrite them as generated assets without an explicit migration.

Versioned defaults plus saved overrides must reproduce the same output. A later edit to personal preferences affects a diagram only when the agent deliberately updates its spec. Unknown format versions or unsupported default versions should produce a clear error.

## 3. Resolve preferences once and apply them consistently

Keep machine defaults in a small versioned file owned by Claude Backstage. Use named roles for colors, typography, node sizing, margins, and motion settings. Respect upstream theme conversion's fixed palette; do not claim arbitrary custom colors can be converted by its existing script.

The agent reads applicable preferences and records their resolved values in the input JSON. The script validates and applies numeric/enumerated settings without reading prose or invoking a model. Qualitative rules such as truthful concurrency remain authoring checks.

Use one authority for settings shared by layout, rendering, and checks. Where upstream guides and checks disagree, document the chosen default rather than copying inconsistent limits. Apply complexity budgets sensibly to scenarios; upstream's single-story recommendation should not silently disable our multi-scenario output.

## 4. Prevent the reported spacing problems

Use measured layout regions for title, flow, side explanation, outcome/caption, and outer clearance. Reserve side-panel width and a gutter before placing nodes. Start with upstream's 28-unit outer margin and a 24-unit panel gutter as proposed defaults; the user may override them. These replace the earlier draft's provisional 24-unit outer-margin example.

Calculate the canvas from content. Include labels, tag backgrounds, arrows, strokes, expanding rings, glows, and moving labels in bounds checks. Text baseline coordinates alone do not establish clearance. Use conservative text-width estimates during generation and check actual font/rendered bounds during browser validation.

Keep supporting legends or explanatory grids at the side at the intended document width. At narrow widths, report an unreadable arrangement and propose an alternate layout instead of silently shrinking text or overlapping content. Growing the canvas is not sufficient if it makes the embedded diagram unreadably small.

Upstream `check.py` is supplementary: it does not detect text clipping or overlaps. Its structural pass must not be reported as a visual-layout pass.

## 5. Keep generation inexpensive to the model

- Reuse templates and script-generated elements; avoid asking Claude to write repeated XML or calculate every coordinate.
- Edit the compact semantic spec when refining a generated diagram, then rebuild.
- Return paths, a short summary, and actionable diagnostics. Full SVG, expanded JSON, and long traces should require a debug request.
- Let scripts inspect files locally. File processing does not put those bytes into model context unless the tool returns them.
- Load only the references needed for the chosen preset or motion feature.
- Prefer idempotent rebuilding and preserved manual files over speculative automatic repair.

Measure a creation and one refinement on the same example before and after this feature. Record model usage when available, file/tool content returned to the model, tool-call count, and SVG source reads. Generated file size alone is not a token-saving measurement. If actual token usage is unavailable, label character counts as proxies and report no percentage token savings.

## 6. Tests included in this commit

Use the real pinned compiler in integration tests. Keep deterministic tests independent of model access and run them through the repository's normal test entry point.

| Test area | Required evidence |
|---|---|
| Schema | Reject duplicate IDs, missing references, unknown fields/versions, non-finite or invalid dimensions/times, and unsupported topology with useful errors. |
| Defaults and overrides | Defaults apply when omitted; overrides affect output; changes to personal Markdown do not silently change a saved spec. |
| Preset boundaries | Five versus six independent items; six ordered steps keep their order; branch scenarios select the correct routes. |
| Spacing | Long labels, bottom captions, side tags, and a side explanation grid reserve space; failed fitting is explicit. |
| SVG and meaning | Parse generated SVG and compiler output; verify intended connections, event order, concurrency, and scenario captions. Check companion content and source links. |
| Escaping | Labels containing XML/HTML metacharacters remain literal text and cannot introduce SVG elements or preview script content. |
| Rebuilds | Same versioned input produces identical output; a changed label or setting updates expected content; failed validation does not leave partial output or overwrite a manual diagram. |
| Integrity regression | Existing wrapper tests pass. A different actual HEAD inside the same hash-named folder and a modified tracked file both block generation before upstream code executes. |
| Compatibility | Existing low-level specs and manual template/timeline workflows still work. |

Prefer assertions about output behavior and relationships over snapshots of every coordinate. Keep a small visual example for each preset; structural assertions alone do not establish typography or animation quality.

## 7. A single smoke command

Add a project-owned smoke runner, for example:

```sh
python3 -I skills/sl-svg-diagram/tests/smoke.py --skill-dir <temporary-install>
```

This is a proposed interface. Document the actual command in the implementation.

The runner should call the installed wrapper as a subprocess, build the three preset fixtures, run the upstream checker, parse the generated outputs, check companion links and repeatability, and exercise invalid input and integrity failure cases in disposable copies. It must exit nonzero for failed required checks and print a short pass/fail summary with artifact paths.

Use temporary installation, dependency, and output directories through supported arguments. Never alter the user's real skill installation, preferences, or dependency checkout. Install/download requirements must be documented; a cached pinned checkout can support offline test runs.

This runner proves script integration. The actual Claude invocation and browser checks are separate requirements in [commit 3](sl-svg-diagram-preview-design.md).

## Commit 2 review package

Provide runnable input fixtures, generated example links, the smoke command/result, regression results, and the creation/refinement cost comparison. Include visual checks when the required offline renderer is available; otherwise mark them pending and keep the PR draft.

Do not expand this stage into an arbitrary graph-layout engine, a new animation compiler, or a dependency upgrade.
