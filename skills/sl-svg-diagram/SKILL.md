---
name: sl-svg-diagram
description: Create animated SVG explanations from semantic JSON using audited local AnimDiagram.
argument-hint: "[Markdown path] [flow or scenarios to explain]"
user-invocable: true
---

# Animated diagrams

Resolve `<skill>` from this installed file. Invoke only `python3 -I <skill>/scripts/run-animdiagram.py`. Each call verifies the pin/hashes. Stop on verification failure; never bypass it or change the pin. Installation and repair require an installation request.

1. Establish the target document and inspect relevant sources. Identify nodes, conditions, order, real concurrency and outcomes. Label hypothetical behavior and illustrative timing. Read `~/.claude/sl-svg-diagram/preferences.md` only if present; task directions win. Save a preference only on explicit request or an accepted suggestion.
2. Choose `flow` for one ordered chain, `branch` for a rooted tree, or `grid` for independent peers; choose grid above five peers. Grid has no links; branch has no merges or cycles. Preserve the actual relationships. Unsupported layouts or unusual motion need [the optional reference](references/options.md); never discard meaning to fit a preset.
3. Write `<stem>.spec.json` beside the intended SVG. Use the following shape; replace the illustrative content with grounded facts:

```json
{"format":"sl-diagram/v1","defaults_version":"v1","title":"Request","claim":"An accepted request is stored.","explanation":"Illustrative example.","sources":[],"layout":"flow","nodes":[{"id":"receive","label":"Receive"},{"id":"store","label":"Store"}],"links":[{"id":"save","from":"receive","to":"store"}],"scenarios":[{"id":"accepted","label":"Accepted request","steps":[{"link":"save"}],"outcome":"Stored."}]}
```

IDs are unique ASCII identifiers starting with a letter. Node fields: `id`, `label`, optional `tag`. Link fields: `id`, `from`, `to`. Sources are `{label,url}` with HTTP(S) URLs. Each scenario has `id`, `label`, `steps`, `outcome`. A step is `{"link":"id"}`, `{"node":"id"}`, or `{"parallel":[simple steps]}`; ordinary steps are sequential, parallel groups cannot nest. Up to 20 nodes, 30 links and eight scenarios. Boolean/enum cases share the same drawing and play in authored order. Use scenario labels for inputs/conditions and explanation for assumptions. Optional `side_panel` is a list of explanation strings; `caption` supplies bottom text.

Omit `settings` for standard appearance. Scripts own geometry, wrapping, clearance, colors and timings. For a requested override, consult only [the optional reference](references/options.md) and save supported numeric settings in the JSON. Do not read scripts or defaults during ordinary creation.

4. Run `build <absolute-spec.json> --out <absolute-diagram.svg>`. It creates the drawing, passes native motion JSON to AnimDiagram, checks the result and formats a companion from the supplied facts. Edit the JSON and rebuild for corrections; do not hand-edit generated SVG. On validation failure, fix the reported field and retry. Create native `preview <svg>` HTML only on explicit request; scenario selection is deferred.
5. Verify that `<stem>.agent.md` faithfully explains the purpose, conditions, sequence/concurrency, outcomes, assumptions and sources. Keep the three files together under the document's asset convention, otherwise sibling `diagrams/`. Embed a relative image and a separate companion link; encode spaces in URLs.
6. Inspect intended and narrow widths, labels, side/bottom clearance and scenario meaning with an approved renderer enforcing outbound network denial for the browser and subprocesses. Structural checks alone do not prove visual quality. If rendering is unavailable, report visual checks pending. No automatic browser install, external service, resource loading or publication.

Report artifact links and verification status. For reading, use [the short guide](references/reading-diagrams.md). No automatic commits or CLAUDE.md edits.
