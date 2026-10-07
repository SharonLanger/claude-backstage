# Iteration Guide

How the skill development cycle works — from test verification to milestone progression.

---

## What is an Iteration?

One cycle of: **test → fix → review → decide**.

An iteration operates on a single milestone (MT). It can run multiple times on the same MT until the skill is good enough to progress.

---

## Iteration Flow

```text
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  1. VERIFY TESTS                                                    │
│     the Director reviews and approves test definitions for this MT.       │
│     After approval, tests are LOCKED — agents never modify them.    │
│                                                                     │
│  2. RUN TESTS                                                       │
│     Runner agent executes the full test suite.                      │
│     Results written to results/ folder.                             │
│                                                                     │
│  3. TESTS FAIL? → REASON + FIX SKILL                               │
│     Reasoner analyzes failures, writes decision + fix instructions. │
│     Fix instructions written to: skill/ folder.                     │
│     skill-change-agent reads skill/, backs up, applies fix.         │
│     Can try multiple variations (V<N>.1, V<N>.2, V<N>.3).          │
│     Reasoner compares results, picks best version.                  │
│     → Go back to step 2.                                           │
│                                                                     │
│  4. TESTS PASS → RUN SKILL REVIEW                                  │
│     Review Skill Agent spawns dimension reviewers + protocol        │
│     verifier + synthesis agent.                                     │
│     Findings stored in skill-review/<milestone>/review-<N>/.        │
│                                                                     │
│  5. REASON ABOUT FINDINGS                                           │
│     Reasoner applies delta acceptance rules:                        │
│       - Correctness: any delta → fix                                │
│       - Token savings: >10% → fix, <=10% → skip                    │
│       - Robustness: hard failure → fix, soft → skip                 │
│     Writes fix instructions to skill/ if needed.                    │
│     → If fixes needed: go back to step 2.                          │
│                                                                     │
│  6. NO CRITICAL FINDINGS → MILESTONE COMPLETE                      │
│     [GATE] the Director approves progression to next milestone.           │
│     This is a hard gate — NO agent can pass it autonomously.        │
│     → Transition to next milestone.                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Versioning System

Before **every** skill change, the skill-change-agent backs up the current state.

### Backup Location

```text
~/.claude/skills/example-skill/backups/
├── v1/          ← initial state
├── v2/          ← after first fix
├── v3/          ← after second fix
├── v6/          ← current baseline
├── v6.1/        ← exploratory change 1
├── v6.2/        ← exploratory change 2
└── v6.3/        ← exploratory change 3
```

### Rules

1. **Always backup before changing** — copy all skill files (except backups/) to `backups/V<N>/`
2. **Sub-versions for exploration** — when trying multiple fixes for the same issue:
   - `V<N>.1` — first attempt
   - `V<N>.2` — second attempt
   - `V<N>.3` — third attempt (max 3)
3. **Compare and decide** — run tests on each sub-version, keep the one with best results
4. **Revert if all bad** — if all sub-versions are worse, revert to `V<N>` (the pre-change baseline)
5. **Log every version** — record what changed and why in a version log

### Version Log

The skill-change-agent maintains a log at:

```text
~/.claude/skills/example-skill/backups/version-log.md
```

Format:
```markdown
| Version | Date | Change | Result |
|---------|------|--------|--------|
| v6 | YYYY-MM-DD | Consolidated execution flow to orchestrator.md | Tests: 5/7 PASS |
| v6.1 | YYYY-MM-DD | Relaxed phase agent log requirement | Tests: 7/7 PASS |
| v6.2 | YYYY-MM-DD | Added custom props section to planner | Tests: 7/7 PASS |
| v7 | YYYY-MM-DD | Kept v6.1 + v6.2 merged | Baseline for M2 |
```

---

## Progression Criteria

To advance from MT<N> to MT<N+1>, ALL of these must be true:

1. **All tests pass** — full green on the MT's test suite
2. **No critical review findings** — the skill review has no blocking issues remaining
3. **[GATE] the Director approves** — explicit approval to progress. NO agent can pass this autonomously.

**Every milestone progression is a GATE.** The Reasoner can recommend progression, but only the Director executes it.

### What counts as "critical"?

| Critical (must fix) | Not critical (skip) |
|---------------------|---------------------|
| Correctness bugs — wrong output (any delta) | Style preferences |
| Robustness holes — skill breaks on valid input | Minor token waste (<10%) |
| Massive token waste (>10% of run) | Cosmetic inconsistencies |
| Security/safety issues | "Nice to have" features |

---

## Delta Acceptance Rules

The Reasoner uses these thresholds to decide what's worth fixing:

| Category | Delta Threshold | Action |
|----------|----------------|--------|
| Correctness | Any delta (even tiny) | **Fix** — always |
| Token savings | Must be >10% improvement | Fix if above, skip if below |
| Robustness | Hard failure on valid input | **Fix** |
| All other | Large or critical only | Skip unless blocking progression |

**Key principle:** Small improvements that aren't correctness-related are NOT worth the churn. The risk of introducing bugs outweighs marginal gains. Token savings below 10% are noise.

---

## Review Integration

### When to Review

After tests pass on a milestone, run a skill review.

### How to Review

The Review Skill Agent (lead of `act-review`) orchestrates the full review:

1. Spawns Dimension Reviewers (D1-D8) — each scores one dimension
2. Spawns Protocol Verifier — checks inter-actor protocol consistency
3. Spawns Synthesis Agent — combines findings into scorecard + verdict

See `roles/act-review/act-review.md` for the act definition and `roles/act-review/review-skill.md` for the full process.

Review criteria inputs:
```text
- Skill files: ~/.claude/skills/example-skill/
- Criteria: skill-review/<milestone>/criteria.md
- Checklist: skill-review/<milestone>/checklist.md
- Dimensions: skill-review/<milestone>/dimensions.md
- Anti-patterns: harness-core/skill-review/resources/anti-patterns.md
```

### Review Output

Stored at:
```text
skill-review/<milestone>/review-<N>/
├── results.md              ← final scorecard + verdict
├── d1-structural.md        ← per-dimension findings
├── d2-ssot.md
├── ...
├── d7-restrictions.md
├── d8-extensibility.md
└── protocols.md            ← protocol verification
```

### After Review → Reasoning

The Reasoner (lead of `act-reasoning`) reads the review results and applies delta acceptance rules to decide what to fix. Fix instructions are written to `skill/`.

### Fix Priority

When the Reasoner produces findings, it classifies using delta acceptance rules:

1. **Correctness** — any delta → always fix
2. **Robustness** — hard failure on valid input → fix
3. **Token savings** — only if >10% savings possible
4. Everything else: skip. Keep the skill easy to change for the next milestone.

---

## When to STOP and Ask the Director

| Situation | Action |
|-----------|--------|
| You think a test is wrong | STOP — explain why, ask the Director to change it |
| Something isn't working after 3 attempts | STOP — explain what you tried, what failed |
| Unsure about a design decision | STOP — present options, ask |
| You want to change test definitions | STOP — only the Director changes tests |
| A fix would require major architecture change | STOP — discuss scope |

the Director is always here. Asking is cheap. Wasting iterations is expensive.

---

## Milestone Transition

When progressing from MT<N> to MT<N+1>:

1. **Backup skill state** — this becomes the "MT<N+1> baseline"
2. **Copy forward relevant tests** — see "Milestone Promotion" in [`implementation/test-rules.md`](implementation/test-rules.md)
3. **Adapt assertions** — update for new behavior in the next MT
4. **Add new tests** — for the new MT's capabilities
5. **the Director verifies tests** — tests are locked after approval
6. **Start new iteration cycle** — from step 1 of the flow

---

## File-Based Communication

All agent coordination happens through files, not prompts.

### Agent Spawn Pattern

```text
Agent(
  description: "<role> (<context>)",
  prompt: """
You are the <role> agent for <act>.
Read <act-file-path> first (act-level rules), then read <role-file-path> (your specific task).

TOP RULE: You are NOT allowed to modify ~/.claude/skills/example-skill/
or any .claude/ project files. Only the skill-change-agent has this permission.
"""
)
```

### Why Files?

- **Reproducible** — same file produces same behavior across sessions
- **Auditable** — you can read what any agent was told
- **Updatable** — change the file, all future agents get the update
- **Token-efficient** — agents read only what they need, not everything
