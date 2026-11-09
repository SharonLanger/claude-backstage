# Phase 2 validation

Compact semantic generation is implemented. Phase 3 scenario selection and actual installed Claude acceptance remain separate. The audited pin/manifest are unchanged; new generation code is project-owned and independently reviewed.

## Runnable examples

| Preset | Input | Animated output | Meaning |
|---|---|---|---|
| Ordered flow | [Spec](../../../skills/sl-svg-diagram/tests/fixtures/flow.spec.json) | [SVG](../../../skills/sl-svg-diagram/tests/fixtures/flow.svg) | [Companion](../../../skills/sl-svg-diagram/tests/fixtures/flow.agent.md) |
| Boolean branch | [Spec](../../../skills/sl-svg-diagram/tests/fixtures/branch.spec.json) | [SVG](../../../skills/sl-svg-diagram/tests/fixtures/branch.svg) | [Companion](../../../skills/sl-svg-diagram/tests/fixtures/branch.agent.md) |
| Independent grid | [Spec](../../../skills/sl-svg-diagram/tests/fixtures/grid.spec.json) | [SVG](../../../skills/sl-svg-diagram/tests/fixtures/grid.svg) | [Companion](../../../skills/sl-svg-diagram/tests/fixtures/grid.agent.md) |

## Checks run

On Python 3.12.14 with cached audited checkout `a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486`:

```sh
python3 -I skills/sl-svg-diagram/tests/run.py /workspace/animdiagram-audited
python3 -I skills/sl-svg-diagram/scripts/run-animdiagram.py setup --skill-dir /workspace/svg-review-artifacts/phase2-candidate-3 --dependency-dir /workspace/animdiagram-audited
python3 -I skills/sl-svg-diagram/tests/smoke.py --skill-dir /workspace/svg-review-artifacts/phase2-candidate-3 --output-dir /workspace/svg-review-artifacts/phase2-smoke-3
python3 -I skills/sl-svg-diagram/tests/measure_cost.py --skill-dir /workspace/svg-review-artifacts/phase2-candidate-3 --output-dir /workspace/svg-review-artifacts/phase2-cost-3
unshare --user --map-root-user --net python3 skills/sl-svg-diagram/tests/browser_layout.py --examples-dir /workspace/svg-review-artifacts/phase2-smoke-3 --output-dir /workspace/svg-review-artifacts/phase2-browser-3
```

All commands exited 0. The normal suite passed 15 wrapper and 10 generation tests. Smoke verified real compiler/checker integration, generated companions, repeatability, invalid inputs, protected manual files, changed actual HEAD in a hash-named directory, modified tracked code, and legacy commands. All installation/profile/dependency mutation fixtures were disposable.

The root agent also installed a fresh candidate (`phase2-root-installed`), ran installed smoke (`phase2-root-smoke`, 25 integration tests), and ran six isolated browser renders (`phase2-root-browser`); all required structural/clearance checks passed. The grid screenshot was inspected for side/bottom fit. Narrow readability limitations remain as described below.

Independent SOL review reran the 25 tests and installed smoke. Two findings were fixed and rechecked: malformed source URLs now return schema diagnostics, and wide Unicode labels wrap conservatively. The shared grid fixture includes a bilingual label; actual Chromium glyph bounds fit inside nodes.

Six real Chromium layout checks covered all three fixtures at 1000px and 360px, including tags, side explanation, bottom caption, and reduced motion. No text overflow or clearance failures remained. At 360px the branch (10.86px effective labels) and grid (5.36px) are **unreadable**; the vertical flow remains readable. These are not passes for narrow readability. Request a narrower alternate layout rather than treating scaling as a solution. A requested narrow `document_width` that cannot retain 11px labels is rejected at generation time. Full scenario playback/selector checks remain phase 3.

Browser execution used Chromium `/usr/bin/chromium` with Playwright in a separate OS network namespace; no default route existed and an external socket failed. Local bytes were supplied inline because managed Chromium blocks file URLs. This establishes local visual checks, not a live Claude skill invocation.

## Creation/refinement measurements

The same three-node example and one label refinement were exercised through both wrapper routes. Manual inputs reconstruct equivalent static SVG/motion JSON locally; they are not captured Claude output. Character counts measure the authoring surface and changed lines, not model tokens.

| Proxy | Manual route | Semantic route |
|---|---:|---:|
| Creation input characters | 5751 | 915 |
| Refinement changed characters | 3093 | 87 |
| Creation wrapper calls | 3 | 1 |
| Refinement wrapper calls | 2 | 1 |
| Creation returned tool-output characters | 398 | 330 |
| Refinement returned tool-output characters | 446 | 336 |

Returned-output lengths include paths and can vary with directory names. These runs did not return SVG source to the model. Actual model usage and model SVG-read counts are unavailable; no percentage token saving is claimed. The reproducible report is `phase2-cost-3/report.json` in review artifacts.

Logs, browser screenshots, normalized debug output and JSON reports are retained under `/workspace/svg-review-artifacts`, outside the repository. Source tests and runnable examples are committed. Live Claude acceptance is unrun because Claude Code and approved credentials are unavailable in this environment; deterministic scripts and browser renders do not replace it.
