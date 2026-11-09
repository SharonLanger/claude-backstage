# Commit 3: optional scenario preview and end-to-end acceptance

Part of the [implementation plan](sl-svg-diagram-mini-design.md), following [JSON generation](sl-svg-diagram-generation-design.md). Keep the PR open for user review; no direct default-branch pushes or automatic merge.

## 1. Preview behavior

HTML remains optional. The animated SVG and its Markdown embedding work without HTML or JavaScript. The existing preview already supplies play/pause, scrubbing, static frame, background selection, and zoom; retain these controls.

| Selection | Behavior |
|---|---|
| `All` | Play all scenarios in authored order with their pauses and resets, then repeat. Initial selection. |
| A boolean scenario | Repeat only the complete `enabled=true` or `enabled=false` scenario. |
| An enum scenario | Repeat only the named enum scenario. Labels come from the spec. |

Changing selection must preserve geometry, colors, speed, and ordering within a scenario. Other routes may remain visible and muted. Reset to the chosen scenario's start while preserving play/pause state. Scrubbing and static-frame selection use its range. A keyboard-operated dropdown must not trigger the page's arrow/space playback shortcuts.

Use the same normalized result as generation, not a second independent timeline calculation. Include scenario ID, label, start, and end times in preview metadata. Ranges are start-inclusive and end-exclusive and include setup, outcome pause, reset, and complete effect tails.

For legacy coordinate-based specs, optional namespaced `sl.scenarios` metadata may supply these ranges. Validate unique IDs, ordered non-overlapping ranges within the loop, and valid boundaries. Do not infer scenarios from phase captions: several phases may describe one scenario. Old specs without scenario metadata keep the ordinary preview. A selector is useful when there are at least two scenarios.

## 2. Implement around the existing dependency

Add a Claude Backstage-owned preview extension exposed through the verified wrapper. Preserve the pinned upstream files and manifest. Keep existing plain preview behavior available.

For generated diagrams, a proposed `build ... --preview` option emits HTML from the same SVG and normalized scenario metadata. Keep the editable scenario definitions in the semantic spec and generate the numeric windows. Do not attach stale ranges to a changed SVG; rebuild the pair together or detect and reject a mismatch.

The current preview uses the Web Animations API for CSS animations. Restrict the story clock to the selected window. Independent streams and idle ticks need separate clock handling so they retain their intended motion instead of restarting on every frame. Confirm play/pause actually pauses all relevant animations.

Keep controls and scripts in HTML. SVG remains self-contained and script-free. Escape metadata and labels safely, including text containing `</script>`. Avoid external resources and automatic browser launching. The existing requirement for enforced outbound network denial during rendering still applies.

## 3. Automated preview checks

Use a real browser in the approved offline rendering environment, and inspect animation state as well as screenshots.

- Boolean and four-value enum fixtures show exactly the authored choices plus `All`.
- `All` visits scenarios in order; a selected scenario repeats without entering others.
- Boundary transitions include complete arrivals, effect tails, outcome pauses, and resets.
- Switching while playing or paused, scrubbing, and the static-frame action obey the selected range.
- Pausing freezes motion; resuming preserves speed. Ambient streams keep their independent periods.
- Background and zoom controls still work; keyboard interaction and focus remain usable.
- Missing metadata preserves the old preview; malformed or mismatched metadata produces a clear error.
- Opening/changing the preview does not modify the SVG. The standalone SVG still animates when embedded as an image, and reduced motion remains meaningful.
- Inspect bottom/side clearances at the intended document width and a narrow width, including long tags and moving labels. Distinguish real layout failures from intentionally overlapping effects such as a glow over its node.

Add these checks to the smoke/test documentation. If a required rendering environment is unavailable, report the checks as unrun; do not silently pass them or substitute XML checks.

## 4. Invoke the installed skill for real

Automated script tests are necessary, but the user also wants proof that Claude can use the skill correctly.

Install the candidate branch in a disposable Claude Code configuration and project using supported isolation options for the installed Claude version. Keep test dependencies and personal preferences separate from real user files. Record the Claude version, model, skill commit, and test commands. Use the existing approved model connection and normal permission handling.

Use repository fixtures with known behavior, rather than relying on the agent to invent a convincing example. For example:

```text
/sl-svg-diagram docs/design.md Explain the fixture's enabled=true and enabled=false paths.
```

Inspect tool calls and resulting artifacts; do not accept the final assistant message as evidence that generation or verification ran.

| Trial | What to verify |
|---|---|
| Boolean branch | Agent uses the installed wrapper and semantic spec; each scenario matches fixture behavior; SVG, spec, companion, and Markdown links exist. |
| Independent peers | Six independent items use the grid default, with a side explanation and long tags; generation reserves bottom and side space. |
| Four enum values | All four scenarios are represented; preview selects each independently and `All` cycles through them correctly. |
| Preference refinement | A temporary profile changes an observable setting. A one-time correction edits that diagram without persisting a new global rule. An explicit “remember this” request updates only the temporary profile. |
| Fresh reading session | With the README's suggested instruction installed in the temporary project, asking for diagram meaning uses prose/the companion. Record unnecessary SVG or full-skill reads if they occur. |

At least one creation and one refinement must use the preset generator. Inspect timing, links, emitted diagnostics, and source-based semantics. A deterministic build cannot by itself prove the model selected the correct behavior.

If Claude Code, authentication, or the approved renderer is unavailable, complete independent tests and document the exact missing acceptance step. Keep the PR draft until required checks are completed or the user explicitly accepts the remaining limitation. Do not label mocked agent calls as a live skill test.

## 5. Evidence and completion

Provide a concise report with:

- Commands, environment/version details, exit statuses, and failed or unrun checks.
- Links to input fixtures, generated Markdown/SVG/spec/companions, and optional previews.
- A few representative frames or a short recording covering scenario selection and spacing.
- Actual creation/refinement usage measurements where available; otherwise clearly labeled proxies.
- Confirmation that personal settings and the audited dependency were preserved.

Use disposable, non-sensitive fixtures; avoid attaching entire private transcripts or local state. Keep a checklist for the three implementation commits in the PR description. Mark it ready for review only when required tests pass and known implementation issues are resolved.

Return the separate PR link to the user and stop before merging. The user's explicit approval after review remains required.
