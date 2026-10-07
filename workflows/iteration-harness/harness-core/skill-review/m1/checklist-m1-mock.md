> **Mock example** — this file demonstrates the format and content generated during the iteration process. Replace with real data from your own runs.

# Review Checklist — M1

Concrete pass/fail items grouped by dimension. Each item gets a verdict (PASS/FAIL/PARTIAL) during the review.

---

## D1 — Structural Clarity

- [ ] Entry point is under 100 lines
- [ ] Each agent spec is 80-230 lines
- [ ] File tree matches the layout documented in entry point
- [ ] No orphan files (every file referenced by at least one other)
- [ ] Agent specs follow standard template (Identity, Responsibilities, Boundaries, Procedure)

## D2 — Single Source of Truth

- [ ] Execution flow described in ONE place (not duplicated)
- [ ] Log format defined once and consistently applied
- [ ] Workspace structure defined once
- [ ] Error handling lives in ONE authoritative location
- [ ] Return formats defined once per protocol

## D3 — Token Efficiency

- [ ] Entry point does not repeat what agent specs already say
- [ ] Spawn prompts are under 3 sentences (point to files, don't relay content)
- [ ] No boilerplate in generated artifacts that the agent already knows from its spec

## D4 — Flow Coherence

- [ ] Phase request format matches between orchestrator and planner
- [ ] Phase completion report format matches between orchestrator and planner
- [ ] Response formats are parseable without ambiguity
- [ ] No circular dependencies between agents

## D5 — Scenario Completeness

- [ ] Single-phase happy path fully specified
- [ ] Multi-phase sequential flow fully specified
- [ ] All error scenarios have defined behavior
- [ ] Edge cases documented (empty input, timeout, partial failure)

## D6 — Contract Stability

- [ ] Log entry format has a single definition
- [ ] Workspace folder naming is deterministic
- [ ] Success/failure report format is defined per agent

## D7 — Restriction Consistency

- [ ] Every restriction in phase-type is mirrored in agent spec
- [ ] Restriction wording is identical (not just semantically similar)
- [ ] No agent performs work outside its declared boundaries

## D8 — Extensibility

- [ ] No hardcoded paths that would require edits for new phase types
- [ ] Core files handle unknown types gracefully (or document the extension point)
- [ ] Adding a new agent type does not require modifying existing agent specs
