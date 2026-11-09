# Review the candidate SVG skill

The candidate branch implements preferences, compact generation and optional scenario selection. Review the separate draft PR; no merge is automatic. Script/browser checks and live Claude trials are distinct. The environment used for implementation has no Claude Code CLI or approved credentials, so **live trials remain pending**.

The [validation report](phase3-validation.md) includes representative frames, completed checks and the exact remaining gate.

## Review examples and controls

| Example | Spec | Animated SVG | Meaning |
|---|---|---|---|
| Ordered flow | [Input](../../../skills/sl-svg-diagram/tests/fixtures/flow.spec.json) | [SVG](../../../skills/sl-svg-diagram/tests/fixtures/flow.svg) | [Companion](../../../skills/sl-svg-diagram/tests/fixtures/flow.agent.md) |
| Boolean | [Input](../../../skills/sl-svg-diagram/tests/fixtures/branch.spec.json) | [SVG](../../../skills/sl-svg-diagram/tests/fixtures/branch.svg) | [Companion](../../../skills/sl-svg-diagram/tests/fixtures/branch.agent.md) |
| Six peers | [Input](../../../skills/sl-svg-diagram/tests/fixtures/grid.spec.json) | [SVG](../../../skills/sl-svg-diagram/tests/fixtures/grid.svg) | [Companion](../../../skills/sl-svg-diagram/tests/fixtures/grid.agent.md) |
| Four enums | [Input](../../../skills/sl-svg-diagram/tests/fixtures/enum.spec.json) | [SVG](../../../skills/sl-svg-diagram/tests/fixtures/enum.svg) | [Companion](../../../skills/sl-svg-diagram/tests/fixtures/enum.agent.md) |

From this candidate checkout, use a **fresh disposable** installation and dependency path:

```sh
svg_trial_root=$(mktemp -d /tmp/sl-svg-review.XXXXXX)
bash skills/sl-svg-diagram/scripts/setup-animdiagram.sh --skill-dir "$svg_trial_root/skill" --dependency-dir "$svg_trial_root/dependency"
python3 -I skills/sl-svg-diagram/tests/smoke.py --skill-dir "$svg_trial_root/skill" --output-dir "$svg_trial_root/examples"
python3 -I "$svg_trial_root/skill/scripts/run-animdiagram.py" preview "$svg_trial_root/examples/branch.svg"
python3 -I "$svg_trial_root/skill/scripts/run-animdiagram.py" preview "$svg_trial_root/examples/enum.svg"
```

Setup downloads the exact audited commit only when the dependency path is absent. To work offline, provide an already cached audited checkout; tests mutate disposable clones, never that cache. The setup path does not replace your existing installation or preferences. Open generated HTML only in your approved browser environment with enforced outbound network denial; setup does not establish that policy.

Inspect `branch.preview.html` and `enum.preview.html`: `All` must visit each choice in order, and each named choice must repeat only itself. Switch while playing/paused. Scrub, static frame, pause/resume, background, zoom and dropdown keyboard focus should work. At selected-window ends, no other scenario caption should appear. Inspect bottom/side clearance and long tags; the grid includes wide Unicode labels. At 360px branch/grid labels are unreadable and require alternate layouts; the preview reports that limitation.

## Prepare real Claude acceptance safely

Use your normal approved Claude connection/authentication. Do not export credentials or disable permission handling. Commands below assume this candidate branch is already checked out. Record the actual Claude version/model and candidate commit; do not assume a particular CLI's isolation flags are supported.

```sh
claude --version
git rev-parse HEAD
svg_live_root=$(mktemp -d /tmp/sl-svg-live.XXXXXX)
mkdir -p "$svg_live_root/project/docs"
bash skills/sl-svg-diagram/scripts/setup-animdiagram.sh --skill-dir "$svg_live_root/project/.claude/skills/sl-svg-diagram" --dependency-dir "$svg_live_root/dependency"
cp skills/sl-svg-diagram/tests/fixtures/*.spec.json "$svg_live_root/project/docs/"
cat > "$svg_live_root/project/CLAUDE.md" <<EOF_INSTRUCTIONS
This is a disposable candidate-skill acceptance project.
Use the candidate skill at $svg_live_root/project/.claude/skills/sl-svg-diagram/SKILL.md and its wrapper only.
For this trial, the personal-preference path is $svg_live_root/preferences.md instead of the normal profile location. Do not read or write real personal preferences. This task direction overrides the default path in the skill.
Do not install or overwrite a global skill. If slash-command resolution selects another skill, stop and correct candidate resolution using your installed Claude version's supported mechanism before continuing.
When reading a diagram, follow $svg_live_root/project/.claude/skills/sl-svg-diagram/references/reading-diagrams.md only when needed; read surrounding Markdown and its matching companion before SVG source.
EOF_INSTRUCTIONS
cat > "$svg_live_root/preferences.md" <<'EOF_PREFERENCES'
| Rule ID | Condition | Behavior | Strength |
|---|---|---|---|
| layout.outer-padding | This disposable trial | Use settings.outer_margin=44 in newly generated diagrams. | required |
EOF_PREFERENCES
cd "$svg_live_root/project"
claude
```

Project-scoped skill resolution must be checked in your installed Claude version. Before the first trial, confirm the active skill is the candidate path, and verify every generation tool call uses that path. If a global same-name skill takes precedence, stop this trial and use the version's documented isolation/resolution option. Do not remove/overwrite your global installation. A run using the old skill does not count.

The temporary preference path is explicit task guidance, not a claim that `CLAUDE_CONFIG_DIR` or another unverified option redirects this skill's hardcoded default. No `HOME` override is used. Keep normal approvals enabled and confirm any proposed “remember” write targets only the temporary preference file.

## Trial prompts and evidence checklist

Use fresh target Markdown documents. Specs in `docs/` are complete hypothetical fixtures; tell Claude to preserve their known routes and label them illustrative.

| Trial | Prompt | Evidence to inspect |
|---|---|---|
| Boolean | `/sl-svg-diagram docs/boolean.md Explain enabled=true and enabled=false using docs/branch.spec.json as the complete hypothetical behavior fixture. Use the semantic generator and optional scenario preview.` | Candidate wrapper `build` actually ran; two correct routes, SVG/spec/companion and Markdown links; selector `All` plus both labels. |
| Six peers | `/sl-svg-diagram docs/peers.md Explain all six independent workers using docs/grid.spec.json. Preserve the side explanation and long tags, and apply this trial's temporary preferences.` | Three-column grid; saved `outer_margin=44`; no claimed execution order; long Unicode/tag/bottom bounds at intended width. |
| Four enums | `/sl-svg-diagram docs/enum.md Explain all four modes from docs/enum.spec.json. Use compact semantic JSON and scenario preview.` | Four routes and authored outcomes; selector repeats each independently; `All` cycles all four. |
| One-time refinement | `For this diagram only, increase the outer margin to 52 and rebuild. Do not save a personal rule.` | Changed spec setting and rebuilt output; temporary preferences byte-identical. |
| Explicit remember | `Remember this for future diagrams in this disposable trial: prefer outer margin 48. Update only the temporary preference path named in CLAUDE.md, using the existing layout.outer-padding ID, then rebuild this example with the resolved setting.` | Only temporary file updated, no duplicate/conflicting rule ID; diagram settings explicitly saved; global profile untouched. |
| Fresh reading | Start a new session in the same disposable project: `Explain the diagram in docs/boolean.md.` | Reads surrounding prose/companion through actual SVG link. Record unnecessary SVG/full-skill reads; source reads are justified only for missing information/edit/debug. |

For each trial retain non-sensitive tool-call evidence, version/model/commit, command exit statuses, source spec and actual emitted paths. Confirm Markdown image/companion links resolve from the document directory, including nested paths/spaces. Inspect resulting behavior and tool calls; the final assistant message alone is not evidence. Record actual creation/refinement usage if available; otherwise leave it unavailable and keep character proxies labeled as such.

Do not declare live acceptance complete until these trials actually run. Keep the PR draft while required evidence is pending unless the user explicitly accepts the remaining limitation. Merge still requires the user's later review and explicit approval.
