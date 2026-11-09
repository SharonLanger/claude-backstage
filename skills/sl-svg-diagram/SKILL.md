---
name: sl-svg-diagram
description: Create animated SVG walkthroughs with native AnimDiagram SVG/motion JSON and a grounded companion.
argument-hint: "[Markdown path] [flow or scenarios to explain]"
user-invocable: true
---

# Animated SVG walkthrough

Resolve `<skill>` from this installed SKILL.md, not the caller's directory. Use only `python3 -I <skill>/scripts/run-animdiagram.py <command>`. Every invocation silently verifies the pin/hashes and runs verified bytes. On failure stop; use the [repository setup instructions](https://github.com/SharonLanger/claude-backstage/blob/main/skills/sl-svg-diagram/README.md#install-and-use). Never bypass verification, change the pin/manifest, or repair/download without an installation request.

1. Resolve the target Markdown and grounded behavior from the task/sources. Ask if no destination is established. Establish inputs/conditions, order, real concurrency and outcomes; label hypothetical/planned behavior and illustrative timing.
2. Read `~/.claude/sl-svg-diagram/preferences.md` only if present. Task directions override preferences/defaults. Fix current feedback; save a scoped rule outside the bundle only on explicit request or accepted proposal. Explain unmet requirements. Setup preserves preferences.
3. Honor the target's asset convention; otherwise use `diagrams/` beside it. Keep sibling `<stem>.svg`, `<stem>.spec.json`, `<stem>.agent.md`. Run `template <absolute-svg>` (optional `--light`); it refuses overwrites. Author static nodes/routes/labels, preserving markers, palette, typography and reduced-motion rules.
4. Author native motion JSON; coordinates refer to that static SVG. Example (illustrative):

```json
{"events":[{"id":"request","kind":"packet","at":0.3,"from":[208,148],"to":[320,148]}]}
```

Omit optional styling/timing fields to reuse upstream defaults. Use `after`/`gap` for order, `with` only for true concurrency, `via` for elbows, and phase captions for inputs/outcomes. Boolean/enum cases play in authored order with inactive routes muted, readable outcome pauses and reset. Run `timeline <spec> --inject <svg>`, then `check <svg>`. Optional `skin <svg> --to light` derives a variant. Create `preview <svg>` HTML **only when explicitly requested**; it adds a tool call and output file. Native preview has ordinary playback controls; scenario dropdowns are deferred.
5. Claude authors the companion from grounded meaning: purpose, inputs/conditions, ordered and concurrent events, outcomes, assumptions and source links. Do not infer it from SVG coordinates; keep all assets/prose consistent. Embed relative image and companion links, URL-encoding spaces:

```markdown
![Animated request flow](diagrams/request.svg)
[Diagram meaning](diagrams/request.agent.md)
```

Layout defaults: 660px canvas, height on a 4px grid, 28px outer margin, title region above y=88, aligned orthogonal routes and visible arrow direction. Retain template typography; wrap/rearrange before shrinking. Ordered steps retain order; more than five independent peers usually use up to three columns. Reserve a right panel/gutter for explanations; clear all bottom labels, side tags and motion/effect bounds. No cramped edges, overlaps or decorative motion; node positions stay fixed across cases. Inspect at intended/narrow document widths.

Load only needed dependency `references/layout.md`, `storyboard.md` or `motion-grammar.md` via `.installation.json`; skip full-skill reads. Keep SVG script-free/self-contained: no external resources, fonts, event handlers or foreignObject. No external diagram service, gallery, browser launch or export. Render only with enforced outbound network denial covering browser subprocesses; checker success is structural, not a visual/security pass. Otherwise report visual checks pending; no automatic browser install/policy changes.

Report paths/checks; no automatic commits/publishing or CLAUDE.md edits. Read existing diagrams via [the short reading guide](references/reading-diagrams.md).
