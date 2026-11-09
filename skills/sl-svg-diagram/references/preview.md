# Scenario preview

Animated SVG remains self-contained and script-free. Optional HTML keeps controls/scripts in the page; no browser is launched and no external resources are added. Preview HTML embeds active content, so render only inside an approved environment with enforced outbound network denial covering browser subprocesses.

```sh
python3 -I <skill>/scripts/run-animdiagram.py build /absolute/flow.spec.json --out /absolute/flow.svg --preview
python3 -I <skill>/scripts/run-animdiagram.py preview /absolute/flow.svg
python3 -I <skill>/scripts/run-animdiagram.py preview /absolute/flow.svg --spec /absolute/flow.spec.json --out /absolute/review.html
```

`build --preview` publishes `.preview.html` with the SVG and companion from the same normalized result. Without the flag, the three primary assets remain the normal contract. `preview` detects generated metadata and validates the complete SVG digest and semantic spec hash (using the recorded relative spec path unless `--spec` is supplied). Changed/missing specs or changed SVG bytes require rebuilding. Do not edit the generated SVG to refine a semantic diagram. Preview never rewrites its input SVG/spec; aliases via symlinks/hardlinks are rejected as output paths. `skin --to light`/`--to dark` still uses the verified palette converter and restamps validated metadata/digests for generated variants, including variants in another directory.

The generated SVG includes inert metadata with normalized scenario ID/label/start/end, version and spec provenance. The digest detects stale/mismatched bytes, not malicious edits to both content and digest. HTML is a derivative snapshot; rebuild it whenever its SVG/spec changes. A standalone SVG remains animated without HTML or JavaScript.

## Controls

`All` is initial: play scenarios in order with their outcome pauses and resets, then repeat. For at least two scenarios a keyboard-operated dropdown offers each authored label. Selecting one repeats only that complete window and resets to its start while preserving play/pause state. Ranges are start-inclusive/end-exclusive. Scrub, static frame, keyboard stepping, and displayed absolute story time stay inside the selection. The selector is hidden for a single scenario.

Play/pause freezes both story effects and ambient streams/ticks. Story time wraps inside the selection; ambient animations keep their own unbounded elapsed clock and period across scenario changes, scrubs and repeats. Resuming preserves speed. Background and zoom controls remain available. Input/select/button focus suppresses page arrow/space shortcuts. These controls are adapted from pinned animdiagram; [full MIT notice](../notices/animdiagram-MIT.txt).

At narrow widths, the page reports when labels scale below 11px. The branch/grid examples need alternate layouts at 360px; shrinking them does not count as readability. Keep the original SVG/spec/companion and inspect the intended document width too. Reduced motion hides animated effects/captions and preserves static structure; the companion retains full scenario meaning.

## Legacy motion specs

Metadata-free legacy SVGs retain upstream plain preview behavior. Use `preview <svg> --plain` explicitly for that route, including generated SVGs when a selector is not wanted. Automatic browser launch remains blocked.

For a coordinate-based spec, add a namespaced `sl` object with exactly:

```json
{
  "sl": {
    "svg_sha256": "SHA-256 of the complete compiled SVG bytes",
    "scenarios": [
      {"id": "true", "label": "enabled=true", "start": 0, "end": 4},
      {"id": "false", "label": "enabled=false", "start": 4, "end": 8}
    ]
  }
}
```

Then call `preview <svg> --spec <legacy-spec>`. Compile with `timeline` before computing the SVG hash; the compiler ignores `sl`. Ranges require unique IDs, finite boundaries, order, no overlap, and containment within the loop. The wrapper invokes the real pinned compiler in a verified snapshot to resolve relative times and verify that motion exactly matches the SVG. Complete packet fade/ring/glow, pulse and phase/show pre/post fades must fit in one range. Ambient streams remain independent. Phase/show edges must be positive and large enough to survive the compiler's two-decimal percentage precision; zero/negative/nonfinite edges are rejected. Loop duration must be representable in centiseconds. Rounded emitted keyframe bounds are checked as well as declared times. Actual emitted CSS is rejected when percentage rounding collapses zero/visible opacity stops, including packet/pulse/ring/glow effects; use `--plain`, shorter loops or longer effects.

Legacy selector support is deliberately limited to packets, pulses, phase/show windows, and ambient streams. Bars/moving groups require the ordinary `--plain` preview or migration to a supported semantic input. Cross-boundary or truncated effects fail with advice to adjust ranges/timing. Do not infer scenarios from phase captions: several phases can belong to one scenario.

## Verification

The [smoke runner](generation.md#deterministic-checks-and-smoke-runner) exercises four semantic fixtures and a legacy ambient fixture. In an approved OS network namespace with Python Playwright and Chromium already available, run:

```sh
unshare --user --map-root-user --net python3 <skill>/tests/browser_layout.py --examples-dir /temporary/smoke-output --output-dir /temporary/layout-evidence
unshare --user --map-root-user --net python3 <skill>/tests/browser_preview.py --examples-dir /temporary/smoke-output --output-dir /temporary/playback-evidence
```

The scripts require no default route and a failed external socket probe. The playback test drives full cycles using virtual browser time, checks real computed effect opacity/transforms, and separately measures real elapsed playback speed. It covers boolean/four-enum choices, exclusive repetition and captions at boundaries, complete outcome/reset windows, pause/resume, selection changes, scrubbing, static frame, keyboard focus, background/zoom, ambient periods, standalone image animation and reduced motion. For standalone SVG images this Chromium requires a separate browser with `--force-prefers-reduced-motion=reduce`; per-page reduced-motion emulation does not propagate into image documents. Screenshots and JSON evidence are written outside the repository.

Real Claude acceptance is a separate requirement. See the repository's `docs/design/sl-svg-diagram/user-review-guide.md` for disposable installation, temporary preferences, fixture prompts, transcript/artifact checks and a fresh reading session. A script or a model's final “done” message does not prove live skill use.
