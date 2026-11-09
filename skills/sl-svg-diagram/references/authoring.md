# Authoring diagrams

Detailed manual workflow. Resolve `<skill>` from the installed skill directory; invoke every dependency tool through its verified wrapper.

## Target and scenarios

Use `$ARGUMENTS` and conversation context to identify the Markdown file and explanation. Resolve a relative document path against the caller's working directory once. If no document or output destination is established, ask one short question before writing.

Read relevant source code or specifications through the organization's approved Claude connection when needed to establish behavior. When the user supplies a complete hypothetical scenario, use that instead and label it illustrative. Do not invent methods, branches, concurrency, or measured timings.

Identify inputs, branch conditions, calls, and outcomes. For a boolean example, explicitly storyboard:
- `enabled=true`: input enters, true route activates, called methods activate in order; false route remains muted.
- Reset/pause.
- `enabled=false`: input enters, false route and its methods activate; true route remains muted.

Keep the active input visible during each scenario. Use packets, timed captions, and destination glows. Parallel calls animate together only when actually concurrent. Allow a readable pause between scenarios and at loop end. This is a repeating illustrated walkthrough, not a live execution trace. Label proposed behavior as planned.

## Files and placement

Honor an explicit destination, then an established repository asset convention. Otherwise create `diagrams/` beside the Markdown file; use `<document-stem>-<topic>` filenames. Multiple diagrams share that folder and use distinct topic names. Root README diagrams naturally live in root `diagrams/`; nested docs keep theirs nearby.

For every diagram retain:
- `design-request-flow.svg`: the animated visual.
- `design-request-flow.spec.json`: editable motion schedule.
- `design-request-flow.agent.md`: concise scenario semantics, without coordinates or styling.

The companion must explain inputs, conditions, ordered calls, concurrent calls if any, and outcomes. Update all representations together. Include the source/specification links needed to distinguish current and proposed behavior, without copying implementation code.

Do not read other SVGs merely to understand documentation: read the surrounding Markdown and matching companion first. SVG source reads are appropriate for creating, editing, or debugging this visual. This instruction is not enforcement for agents that have not loaded the skill.

## Build with the verified wrapper (manual route)

1. Copy a template:
   `python3 -I <skill>/scripts/run-animdiagram.py template <absolute-svg-path>`
   Add `--light` if appropriate. The command refuses to overwrite an existing file.
2. Draw readable nodes and routes in that local SVG. Keep the motion marker comments. Keep SVG self-contained: no scripts, event attributes, external resources, web fonts, `foreignObject`, stylesheet processing instructions, or DTDs.
3. Author a JSON schedule with `loop` and `events`. Use `packet` with `from`, `to`, optional `via`, `travel`, `label`, and `glow`; chain with `after` or synchronize with `with`. Use `phase` captions with `at`, `until`, `text`, `x`, and `y` for the input scenarios. A `show` window can highlight an entire active route. Keep untaken routes muted.
4. Compile:
   `python3 -I <skill>/scripts/run-animdiagram.py timeline <absolute-spec-path> --inject <absolute-svg-path>`
5. Check:
   `python3 -I <skill>/scripts/run-animdiagram.py check <absolute-svg-path>`
6. If useful, derive a light variant with `skin <absolute-svg-path> --to light`.
7. Create a local preview HTML file with `preview <absolute-svg-path>`. This does not open a browser.

The setup configuration `.installation.json` identifies the dependency directory if you need to read its local `references/storyboard.md`, `references/motion-grammar.md`, or design references. Load only what is needed. Use these as authoring references; our invocation, destination, privacy, and multi-scenario rules take precedence over upstream instructions.

## Privacy and visual verification

Core generation runs locally without an external diagram service. Do not upload diagrams, code, or specs to another tool/service. The approved enterprise Claude connection is separate.

The bundled gallery loads Google Fonts; do not use it in the local-only workflow. The upstream checker is not a security sanitizer. Preview HTML embeds SVG verbatim and must be treated as active content. The wrapper blocks `preview --open` and does not expose video export.

Render/inspect only in an already available environment with enforced outbound networking denial covering the browser and its subprocesses. Do not assume a local file, private browsing, prompt instruction, or page-request interception establishes that boundary. Do not install a browser or alter network policy automatically. If safe rendering is unavailable, complete generation and structural checks and state that visual verification remains pending.

When rendering is available, inspect each scenario at normal and narrow document widths: active input, branch exclusivity, call order, pauses, text clipping, and reduced-motion behavior. Keep the diagram meaningful for readers with reduced motion. Animation must remain the normal output.

## Embed and finish

Embed with a Markdown image reference relative to the document directory, and link the companion:

```markdown
![Animated true and false request paths](diagrams/design-request-flow.svg)
[Diagram semantics](diagrams/design-request-flow.agent.md)
```

Use forward slashes and URL-encode spaces. Never paste raw SVG into Markdown. Keep alt text and nearby prose short. Preserve unrelated content and existing filenames when updating.

Report links to the Markdown and SVG, what the scenarios explain, and whether visual verification completed. Show an animated preview only where supported; a terminal may show only links. No automatic commits, pushes, publishing, or changes to project `CLAUDE.md`. Personal preference updates follow [diagram rules](diagram-rules.md#saved-preferences).
