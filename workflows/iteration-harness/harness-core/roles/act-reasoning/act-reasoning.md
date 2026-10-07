# Act: act-reasoning

Every actor in this act MUST load this file first.

---

## Purpose

Analyze evidence (test results, review findings, version comparisons) and produce decisions that drive the next step of the iteration. This act is the brain — it reasons, decides, and writes instructions for other acts.

---

## Shared Rules (all actors in this act)

1. You are NOT allowed to modify `~/.claude/skills/example-skill/` or any `.claude/` project files.
2. You are NOT allowed to modify test files (`blueprint.md`, `asserts.md`, `input/`). Tests are locked after the Director approves them.
3. You do NOT implement fixes — you describe what to fix. The Skill-Change-Agent does the work.
4. You do NOT approve milestone progression — you recommend it. the Director decides at the GATE.
5. Never pass task details in sub-agent prompts — point actors to their role file.
6. All actors: Model = opus, Effort = high.

---

## Actors

| Role | Actor | File | Spawned By |
|------|-------|------|-----------|
| Lead | Reasoner | `reasoner.md` | Main Agent |
| Cast | Comparator | `comparator.md` | Reasoner |

---

## Flow

```text
Reasoner (Lead)
  ├── reads evidence (test results / review findings / version diffs)
  ├── spawns Comparator (if multiple versions to compare)
  ├── applies delta acceptance rules
  ├── writes decision file to decisions/
  └── writes fix instructions to skill/ (if fixes needed)
```

---

## Delta Acceptance Rules

| Category | Threshold | Decision |
|----------|-----------|----------|
| Correctness | Any delta (even tiny) | Fix it |
| Token savings | Must be >10% improvement | Fix if above, skip if below |
| Robustness | Hard failure on valid input | Fix it |
| All other | Large or critical only | Skip unless blocking progression |

**Key principle:** Small improvements that aren't correctness-related are NOT worth the churn. The risk of introducing bugs outweighs marginal gains. But if it's 10%+, it's worth the change.

---

## Inputs

| Input | Source |
|-------|--------|
| Test results | `implementation/<milestone>/tests/test-NN-*/results.md` |
| Review findings | `skill-review/<milestone>/review-<N>/results.md` |
| Version backups | `~/.claude/skills/example-skill/backups/` |
| Previous decisions | `decisions/decision-*.md` |

---

## Outputs

| Output | Location |
|--------|----------|
| Decision file | `decisions/decision-<run-ID>.md` |
| Fix instructions | `harness-core/skill/fix-NN-*.md` |
| Suggested tests (optional) | Section within fix instructions |

---

## Boundaries

- This act reasons and decides. It NEVER modifies skill files or runs tests.
- Decisions drive the next act: `act-skill-change` (for fixes), `act-test-runner` (for re-validation), or Director (for GATE).
- If stuck after 3 fix cycles on the same issue: STOP and escalate to the Director.
- If all versions are worse than baseline: STOP and escalate to the Director.
