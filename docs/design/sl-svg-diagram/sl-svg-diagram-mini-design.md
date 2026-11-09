# SL SVG Diagram: implementation plan and documentation

**Status:** design for handoff; implementation and tests have not run. This is the entry point for three linked design files.

## Delivery and review

Use one dedicated feature branch and one separate pull request in Claude Backstage. Organize the work into the three logical commits below, with each commit's tests and documentation included. Keep every intermediate commit usable. Update the draft PR as each stage completes so the user can review progress by commit.

**Never push directly to `main` or `master`. Do not merge or enable automatic merging. The user must review the PR and explicitly approve a merge.** Inspect the current repository and applicable instructions before implementation. If a stage cannot be kept reviewable, explain the proposed split rather than burying additional scope in it.

| Commit | Design | Deliverable | Review checkpoint |
|---|---|---|---|
| 1. Organize instructions and preferences | This file | Clear user/agent documentation, reading guide, defaults and personal preference workflow. Existing generation remains usable. | Installation and instruction checks; small documentation diff. |
| 2. Add JSON generation and layout checks | [Generation design](sl-svg-diagram-generation-design.md) | Three layout presets, compact input, consistent spacing, existing verified animation compiler, script tests and smoke runner. | Generated examples, deterministic results, integrity regressions, token-cost comparison. |
| 3. Add scenario preview and verify the skill | [Preview and acceptance design](sl-svg-diagram-preview-design.md) | Optional scenario selector, browser tests, actual installed-skill acceptance runs. | Working boolean/enum demonstrations, playback and layout evidence, final test summary. |

This is three design files and three logical implementation commits, not a restriction to three source files. Each implementation commit may contain the scripts, tests, fixtures, and docs needed for its behavior.

## Goals and boundaries

Reduce repetitive SVG authoring, respect saved preferences, improve bottom and side spacing, and optionally select scenarios in HTML. Animated SVG remains the normal standalone deliverable, accompanied by editable JSON and a linked `.agent.md`.

Keep the audited animdiagram commit and SHA-256 manifest unchanged. New project-owned scripts need their own tests and review; they do not inherit the upstream audit. Preserve verification before every dependency invocation, and preserve the existing rendering/privacy constraints.

The generator is a new feature. Upstream already compiles motion JSON, but still requires hand-authored static SVG. Our current skill correctly uses its template, compiler, checker, preview, and theme converter. Retain that functionality and the manual route for unusual diagrams.

## 1. Documents with distinct responsibilities

| File | Audience and contents | Load when |
|---|---|---|
| `README.md` | Users: setup, examples, preference location, preview options, integrity guarantees and limitations. Include the line users can copy into their own `CLAUDE.md`. | Installation or help. |
| `SKILL.md` | Authoring agents: short workflow, wrapper requirement, correctness/privacy constraints, reference routing, output contract. | Creating or updating diagrams. |
| `references/authoring.md` | Authoring agents: detailed commands, input formats, motion recipes, layout and verification procedure. | Needed for the current task. |
| `references/reading-diagrams.md` | Reading agents: find the explanation without loading the authoring skill. | Understanding an existing diagram. |
| `references/diagram-rules.md` | Authoring agents: design defaults, hints, and things to avoid, identified by stable rule IDs. | Planning a diagram. |
| Personal `preferences.md` outside the installation | User-specific overrides and accepted lessons from feedback. | Alongside defaults during authoring. |
| Existing `audit/` | Audit evidence and verification data. | Audit review or troubleshooting; the wrapper reads the manifest itself. |

Keep `SKILL.md` focused: understand behavior, load relevant preferences, choose a preset or manual route, build through the wrapper, verify, and embed with the companion link. Preserve required installed filenames; moving or removing files named in the wrapper's `REQUIRED` list can break verification.

The reading guide should be short: read surrounding Markdown first; resolve the actual SVG link; read the matching `.agent.md` beside that SVG; use SVG source for editing, debugging, or resolving missing information. Asset folders may be named `diagrams`, `sl-diagrams`, or something else.

Offer a plain path reference to the guide for the user's general or project `CLAUDE.md`. Avoid an `@` import when conditional loading is intended. This is guidance rather than enforcement.

## 2. Defaults and personal preferences

Proposed personal location: `~/.claude/sl-svg-diagram/preferences.md`. Keep it outside the installed bundle so reinstalling the skill preserves it and does not trigger the installer's customized-file conflict. If missing, use defaults; setup should not overwrite or automatically populate personal preferences.

Use rule IDs, conditions, behavior, and strength. These are proposed starting rules for review:

| Rule ID | Condition | Behavior |
|---|---|---|
| `layout.independent-grid` | More than five independent peer items | Use a grid, initially up to three columns. |
| `layout.ordered-flow` | Steps have an execution order | Keep the order clear through placement and arrows; item count alone must not choose a grid. |
| `layout.side-explanation` | Legend, tag key, or explanatory grid supports the main flow | Reserve a dedicated side panel, preferably on the right. |
| `layout.outer-padding` | Every diagram | Reserve clearance around all visible content, including bottom labels and moving tags. |
| `text.readability` | Labels do not fit | Wrap or rearrange before reducing type size. |
| `animation.scenario-pause` | Scenario transitions | Include a readable outcome pause and reset. |
| `style.avoid` | Every diagram | Avoid cramped edges, overlapping tags, decorative motion, and moving node positions between scenarios. |

Strength can be **default**, **required**, or **avoid**. Explain an unsatisfied required preference. Task-specific directions override personal preferences, which override shipped defaults. Factual correctness, integrity checks, and privacy requirements remain mandatory.

Commit 2 introduces versioned machine defaults for numeric settings. Those become the source of truth; documentation should reference or generate their values rather than maintaining a second independent table. The agent translates applicable Markdown preferences into typed JSON overrides. The runtime must not depend on interpreting arbitrary Markdown or on another model call.

## 3. Improve from feedback

Describe the behavior as “adapts to your saved preferences.” Persistence is explicit.

Fix the current diagram when corrected. If feedback appears reusable, propose a concise rule and its scope. Save it when the user asks to remember it or accepts the proposal. Keep one-time exceptions in that diagram's JSON. Do not prompt to save preferences after every successful diagram.

Update existing rule IDs instead of accumulating contradictory entries. Resolve conflicting instructions with the user. Never modify dependency code or its manifest to implement a preference.

## 4. Commit 1 acceptance checks

- Verify setup in a disposable installation, all reference paths, and preservation of an existing personal preference file. Do not use the user's real profile as a test fixture.
- Verify missing preferences use defaults and that existing template/timeline/check commands still work.
- Review the instructions against two examples: a one-time style correction and an explicit “remember this” request. They must lead to different persistence behavior.
- Check the Markdown image and companion links in a generated document, including nested documents and paths containing spaces.
- Do not add tests that merely assert exact prose. Test installation behavior and reference resolution; inspect prose for clarity.

## 5. Common review requirements

Use a shared set of small fixtures across all three stages. Include the user's spacing example if it becomes available; do not claim its precise defect is fixed without examining it.

Each PR update should identify completed work, validation commands and outcomes, and remaining issues. Include representative visuals when the required offline renderer is available. Keep required unrun checks explicitly pending and the PR in draft.

The final PR must distinguish deterministic script tests, actual Claude skill invocations, and visual verification. A model saying “done” is not a validation result. See the two linked designs for the corresponding checks.

## Research basis

Upstream `main` matched our audited commit `a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486` during research. Reuse its good ideas with MIT attribution when copying substantial code or text.

- [Upstream skill](https://github.com/praveenvijayan/animdiagram/blob/a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486/SKILL.md): references, storyboard, templates, compiler, verification.
- [Layout guide](https://github.com/praveenvijayan/animdiagram/blob/a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486/references/layout.md): spacing and connector rules. Its four-unit grid is coordinate alignment, not automatic multi-column layout.
- [Storyboard](https://github.com/praveenvijayan/animdiagram/blob/a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486/references/storyboard.md): motion JSON currently uses coordinates from hand-authored SVG.
