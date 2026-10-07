# Act: act-review

Every actor in this act MUST load this file first.

---

## Purpose

Evaluate the skill's specification quality — clarity, consistency, completeness, and efficiency. This act does NOT fix anything — it measures and reports.

---

## Shared Rules (all actors in this act)

1. You are NOT allowed to modify `~/.claude/skills/example-skill/` or any `.claude/` project files.
2. You are NOT allowed to modify test files (`blueprint.md`, `asserts.md`, `input/`). Tests are locked after the Director approves them.
3. You evaluate the SPECIFICATION quality — not implementation correctness. Tests validate behavior; the review validates that the spec is clear enough to reliably produce correct implementations.
4. Never pass task details in sub-agent prompts — point actors to their role file + the dimension/criteria they need.
5. All actors: Model = opus, Effort = high.
6. Scores are ABSOLUTE (fresh each review), not relative to previous reviews.

---

## Actors

| Role | Actor | File | Spawned By |
|------|-------|------|-----------|
| Lead | Review Skill Agent | `review-skill.md` | Main Agent |
| Cast | Dimension Reviewer (x8) | `dimension-reviewer.md` | Review Skill Agent |
| Cast | Protocol Verifier (x1) | `protocol-verifier.md` | Review Skill Agent |
| Cast | Synthesis Agent (x1) | `synthesis.md` | Review Skill Agent |

---

## Flow

```text
Review Skill Agent (Lead)
  ├── Phase 1: Preparation (no spawn)
  ├── Phase 2: spawns 8 Dimension Reviewers (parallel) → score D1-D8
  ├── Phase 3: spawns Protocol Verifier → checks inter-actor protocols
  ├── Phase 4: spawns Synthesis Agent → aggregates findings → verdict
  └── Phase 5: Output (no spawn) → writes final results
```

---

## Dimensions (8 total)

| ID | Name | Core Question |
|----|------|---------------|
| D1 | Structural Clarity | Does each file have one clear purpose? |
| D2 | Single Source of Truth | Is every concept defined in exactly one place? |
| D3 | Token Efficiency | Do agents read only what they need? |
| D4 | Flow Coherence | Can agents follow the flow without ambiguity? |
| D5 | Scenario Completeness | Are all scenarios for the current scope fully specified? |
| D6 | Contract Stability | Are outputs defined precisely enough for testing? |
| D7 | Restriction Consistency | Do boundary rules agree across files? |
| D8 | Extensibility | Can new phase types be added without modifying core files? |

---

## Delta Acceptance Rules (for finding classification)

| Category | Threshold | Action |
|----------|-----------|--------|
| Correctness | Any delta | Always fix |
| Token savings | >10% improvement | Fix. Below 10% = skip |
| Robustness | Hard failure on valid input | Fix. Soft/cosmetic = skip |
| All other | Blocks progression or causes confusion | Fix. Otherwise skip |

Note: The review TAGS findings with these categories. The Synthesis Agent CLASSIFIES them. The Reasoner (downstream, not in this act) DECIDES whether to act.

---

## Reference Files

| File | Path | What It Covers | Read By |
|------|------|----------------|---------|
| Universal checklist | `skill-review/resources/checklist-universal.md` | 42 fixed structural/quality checks organized by dimension (D1-D4, D6-D8) | Dimension Reviewers |
| Checklist template | `skill-review/resources/checklist-template.md` | Template for generating milestone-specific checklists (D5, D7 additions, protocols, D8 additions) | Review Skill Agent (to generate milestone checklist) |
| Scoring criteria | `skill-review/resources/criteria.md` | Universal rubric: 0-10 per dimension with calibration anchors, verdict rules, delta acceptance rules | Dimension Reviewers, Synthesis Agent |
| Tasks definition | `skill-review/tasks.md` | Full review process definition (procedure, triggers, limits) | Review Skill Agent |
| Anti-patterns catalog | `harness-core/skill-review/resources/anti-patterns.md` (sections 5-7) | Pattern IDs for findings (X1-X5, H1-H8, M1-M7) | Dimension Reviewers |

---

## Inputs

| Input | Source |
|-------|--------|
| Skill source | `~/.claude/skills/example-skill/` |
| Universal checklist | `skill-review/resources/checklist-universal.md` |
| Milestone checklist | `skill-review/<milestone>/checklist-milestone.md` |
| Scoring criteria | `skill-review/resources/criteria.md` |
| Review task definition | `skill-review/tasks.md` |
| Anti-patterns | `harness-core/skill-review/resources/anti-patterns.md` |
| Previous review (if any) | `skill-review/<milestone>/review-<N-1>/results.md` |

---

## Outputs

```text
skill-review/<milestone>/review-<N>/
  results.md              ← Final scorecard + verdict
  d1-structural.md
  d2-ssot.md
  d3-tokens.md
  d4-flow.md
  d5-completeness.md
  d6-contracts.md
  d7-restrictions.md
  d8-extensibility.md
  protocols.md
```

---

## Boundaries

- This act evaluates and reports. It NEVER modifies skill files, test files, or makes progression decisions.
- After this act completes, `act-reasoning` reads the results and decides what to fix.
- Maximum 3 full reviews per milestone. After 3rd: escalate to the Director.
