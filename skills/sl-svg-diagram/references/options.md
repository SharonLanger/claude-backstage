# Optional settings and native authoring

Read only for a requested override or a layout/motion outside the presets.

## Saved settings

Add numeric `settings` to the semantic JSON; saved values override versioned defaults. The builder does not read preferences. Unknown keys, booleans and nonfinite/out-of-range values fail. Example: `"settings":{"outer_margin":40,"gap":80,"font_size":16}`.

| Setting | Range | Default |
|---|---|---|
| outer_margin | 20–100 | 28 |
| panel_gutter / panel_width | 20–100 / 140–400 | 24 / 220 |
| node_width / node_height | 100–320 / 48–240 | 176 / 64 |
| gap / font_size | 40–160 / 12–24 | 56 / 14 |
| document_width | 320–2000 | 1000 |
| travel / pause | 0.1–10 / 0.5–10 seconds | 0.7 / 1.2 |
| reset / setup | 0.2–5 / 0.1–5 seconds | 0.4 / 0.3 |
| effect_tail | 0.5–3 seconds | 0.5 |

Colors use the fixed dark palette. `document_width` is the intended embedding width: layouts scaling text below 11px fail. Narrower embeds may need a separate diagram. Maximum 30 top-level steps per scenario, 120 simple steps total, 250-second loop; split longer explanations. Parallel groups contain 2–8 distinct simple steps without nesting. Title/claim max 160 characters, explanation 3000, node label 240, tag 120, scenario label 160, outcome/caption/side-panel item 240. At most 20 HTTP(S) sources and 12 side-panel strings. Unknown schema fields fail.

`build <spec> --out <svg> --debug-normalized <new.json>` optionally writes diagnostic geometry/motion/windows. It is not another maintained input. The builder refuses manual/linked outputs. Validation or compilation failure preserves existing SVG/companion; each replacement is atomic, but filesystem failure is not a multi-file transaction. Semantic JSON is authoritative; edit it and rebuild.

## Native fallback

For merges, cycles, unusual layout or streams/bars/moving groups, choose a fresh manual output and author native SVG/motion JSON. Preserve the actual relationships; never drop links to fit a preset. Use only the verified wrapper:

```sh
python3 -I <skill>/scripts/run-animdiagram.py template <absolute-svg>
# Author static geometry, retaining template styles and motion markers.
python3 -I <skill>/scripts/run-animdiagram.py timeline <absolute-motion.json> --inject <absolute-svg>
python3 -I <skill>/scripts/run-animdiagram.py check <absolute-svg>
```

Resolve the dependency via `.installation.json`; read only needed `references/layout.md`, `storyboard.md` or `motion-grammar.md`. Use `after`/`gap` for order, `with` for true concurrency and `via` for bends. Keep node positions fixed across cases; reserve room for wrapped labels, tags, side explanations, bottom captions and effect bounds. Author the companion from supplied facts, including conditions, order/concurrency, outcomes, assumptions and sources. Retain script-free self-contained SVG without external resources, event handlers or foreignObject.

Only on explicit request, `preview <svg>` creates native HTML playback controls. Scenario selection is deferred; native pause does not reliably freeze CSS, so inspect scrub/static frames. `skin <svg> --to light` uses the upstream fixed palette. These commands preserve native compatibility, not semantic rebuild inputs. Rebuild the semantic SVG before reapplying a derivative skin. Rendering requires outbound network denial covering browser subprocesses; structural checks do not prove visual quality.
