# Semantic generation (sl-diagram/v1)

Use `python3 -I <skill>/scripts/run-animdiagram.py build <absolute-spec.json> --out <absolute-diagram.svg>`. The wrapper verifies the actual dependency HEAD, tracked-file set, and audited bytes before loading project-owned generation code. Generation uses a temporary low-level motion spec and the pinned compiler, then parses SVG and runs the supplementary upstream structural checker. It never reads personal Markdown or calls a model.

Save the semantic `.spec.json` alongside its generated `.svg` and `.agent.md`, preferably with the same stem. The semantic spec is authoritative: edit it and rebuild. The build prints paths and a short summary; `--debug-normalized <new-file.json>` explicitly writes geometry, scenario windows, and intermediate motion for diagnosis. This is not another maintained input. Outputs are reproducible from the versioned defaults and saved overrides. Input is never rewritten. Add `--preview` to emit optional scenario-selecting HTML from the same normalized result; [preview details](preview.md) cover controls, pairing and legacy metadata. Existing plain preview remains available.

Build refuses existing SVGs/companions without its generated ownership marker and symlink outputs. Migrate a manual diagram explicitly by choosing a fresh generated output path; the existing manual template/timeline route stays supported. Validation/compilation failure leaves existing outputs unchanged. All files are staged before replacement; filesystem failure during replacement is not a transactional multi-file rollback.

## Schema and topology

Start from the [flow](../tests/fixtures/flow.spec.json), [boolean branch](../tests/fixtures/branch.spec.json), or [six independent peers](../tests/fixtures/grid.spec.json) fixture. Unknown fields and versions, duplicate JSON keys/IDs, broken references, invalid dimensions/times and unsupported topology are errors. IDs match `[A-Za-z][A-Za-z0-9_-]{0,47}`; node and link IDs share a namespace. Scenario IDs are separate.

| Field | Contents |
|---|---|
| `format`, `defaults_version` | Exactly `sl-diagram/v1`, `v1`. |
| `title`, `claim`, `explanation` | Grounded text; title/claim max 160 characters, explanation max 3000. |
| `sources` | List of `{label, url}` with HTTP(S) source links; empty for a self-contained hypothetical fixture. |
| `layout` | `flow`, `branch`, or `grid`. |
| `nodes` | 1–20 `{id, label, tag?}` objects. Labels/tags wrap before the canvas grows. |
| `links` | `{id, from, to}` objects referencing nodes; max 30. |
| `scenarios` | 1–8 `{id, label, steps, outcome}` objects. Captions/outcomes come from these fields. |
| `settings` | Optional typed numeric overrides; only keys shipped in versioned defaults. |
| `side_panel` | Optional list of explanation/key entries (max 12). Dedicated right region and gutter. |
| `caption` | Optional bottom text; otherwise explicitly labels timing as illustrative. |

`flow` supports one vertical ordered chain. Six ordered steps keep their order. `branch` supports a connected rooted tree: one parent per non-root node, no merges/cycles. Children follow link input order, leaves define columns. `grid` supports independent peers only, no links, up to three columns; selecting it explicitly also supports five or fewer peers. For more than five independent items choose grid by default. Other topologies require the manual route; unsupported links are never discarded.

A step is exactly one of `{"link":"link-id"}`, `{"node":"node-id"}`, or `{"parallel":[simple steps...]}`. Ordinary steps run sequentially. Parallel groups contain 2–8 simple distinct steps, with no nesting. A link animates a routed packet and destination glow; a node pulses in place. The spec chooses meaningful order/concurrency; the generator does not infer program behavior or require every scenario to traverse every node. Max 30 top-level steps per scenario and 120 simple steps total. The versioned compiler precision budget additionally limits loops to 250 seconds; split longer explanations. Keep each scenario concise; split larger explanations.

Normalized scenario windows use the compiler centisecond loop clock, are ordered, start-inclusive/end-exclusive, and include setup, full step effects, outcome pause, and reset. Adjacent simple steps wait for travel plus effect tail; parallel steps share their start. Phase captions use positive fades with a guard inside setup/reset to survive rounded keyframe percentages without leaking between scenarios. No moving labels are positioned outside node regions. Geometry never changes between scenarios.

## Settings, spacing, and rendering

[Versioned defaults](../defaults/v1.json) are the sole numeric/color authority. The agent translates relevant personal/task preferences into explicit numeric `settings` once. Changing personal Markdown later does not change a saved spec. Unknown settings fail. Colors use the fixed upstream-compatible dark palette; arbitrary color overrides are not supported. Existing `skin --to light` uses upstream's fixed conversion palette.

| Settings | Allowed range |
|---|---|
| `outer_margin` | 20–100 |
| `panel_gutter` | 20–100 |
| `panel_width` | 140–400 |
| `node_width`, `node_height` | 100–320; 48–240 |
| `gap` | 40–160 |
| `font_size` | 12–24 |
| `document_width` | 320–2000 |
| `travel`, `pause` | 0.1–10; 0.5–10 seconds |
| `reset`, `setup` | 0.2–5; 0.1–5 seconds |
| `effect_tail` | 0.5–3 seconds |

The generator reserves title/claim, nodes, side explanation, scenario/outcome, caption, and outer regions. It uses conservative monospace width estimates (double units for wide Unicode glyphs), expands node heights for wrapped tags, includes pulse/stroke extents inside nodes, and keeps packets/glows on reserved routes/nodes. Canvas dimensions round up to the upstream four-unit grid. No external fonts/resources are loaded.

`document_width` is the intended embedding width. A layout that would scale its labels below 11px is rejected with alternate-layout guidance; growing the canvas alone is insufficient. At narrower embedding widths, ask for an alternate diagram/layout rather than silently treating shrunken text as readable. Browser typography checks remain necessary for actual glyph bounds. Upstream's single-story budget/off-grid/typography warnings are supplementary and do not disable multiple scenarios: project limits above govern schema complexity. A successful structural check does not establish visual layout or privacy.

Use only an approved renderer with enforced outbound network denial. Inspect the intended and narrow widths, text clipping, node/tag containment, bottom/side clearance, scenario meaning, and reduced motion. If rendering cannot run, mark visual verification pending.

## Existing motion recipes

For mechanisms beyond semantic packets/pulses use the manual route and load the dependency's `references/motion-grammar.md` or `references/storyboard.md` from `.installation.json` only as needed. Streams use `kind: stream` with endpoints/period/count, pulses use `kind: pulse` with center/time, bars use `kind: bar` with timed fractions, and moving groups use the upstream motion grammar. Preserve markers and compile with `timeline`; do not invent new semantic step fields or bypass the wrapper.

## Deterministic checks and smoke runner

Requires Git and Python 3.10+ plus a cached checkout at the exact audited commit. Setup can download it when installation is requested; the following tests do not need a network connection:

```sh
python3 -I skills/sl-svg-diagram/tests/run.py /absolute/cached/animdiagram
bash skills/sl-svg-diagram/scripts/setup-animdiagram.sh --skill-dir /temporary/skill --dependency-dir /absolute/cached/animdiagram
python3 -I skills/sl-svg-diagram/tests/smoke.py --skill-dir /temporary/skill --output-dir /temporary/fresh-output
python3 -I skills/sl-svg-diagram/tests/measure_cost.py --skill-dir /temporary/skill --output-dir /temporary/fresh-cost-output
```

Use disposable locations, never the user's installed skill/profile/dependency as a mutation fixture. The smoke runner builds all three examples through the installed wrapper, checks XML/companions/repeatability, and runs schema/integrity/legacy tests in disposable clones. It returns nonzero on required failure and reports retained artifact paths. `--output-dir` must be fresh; omit it for a retained temporary directory.

`measure_cost.py` compares layout-equivalent manual static SVG plus motion JSON against compact semantic JSON for a creation and label refinement. It records authoring-character proxies, changed-character proxies, actual wrapper-call counts and returned tool-output characters. The manual inputs are reconstructed locally, not measured live Claude output. These measurements do not establish token savings; actual usage/model SVG reads are unavailable. Browser and actual installed Claude acceptance are separate gates.
