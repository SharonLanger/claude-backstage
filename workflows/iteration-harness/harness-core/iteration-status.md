# Iteration Status — M1

> **This is a mock example** showing the format and purpose of the iteration status file. The Main Agent updates this file after each act completes. The Director reads it to see current progress. On session resume, the Main Agent reads it to pick up where it left off. Replace with real data from your own runs.

## Current State

- **Latest review:** M1 review-1 → 52/80 (65%, "Ready with caveats")
- **Reasoner decision:** `decisions/decision-m1-review-findings-mock.md` — accepted 4 fixes, skipped 2
- **Fix instructions written:** fix-01 (in `skill/`)
- **Batching:** Single fix, safe to apply alone

---

## What's Next

| Step | Act | Input |
|------|-----|-------|
| **Now** | `act-skill-change` | Fix file: `skill/fix-01-restore-execution-loop-mock.md` |
| **After** | `act-test-runner` | Re-run tests (2 tests) on the new version |
| **If pass** | `act-review` | Review-2 on the new version — check if score improves and no new threshold-crossing findings |
| **If no findings** | `[GATE]` | Present results to the Director for milestone progression approval |

---

## Iteration Cycle

```
┌─────────────────────────────────────────────────────────────┐
│  act-skill-change  →  act-test-runner  →  act-review        │
│        ↑                                       │            │
│        └───────── act-reasoning ←──────────────┘            │
│                   (filter findings, write fixes)             │
└─────────────────────────────────────────────────────────────┘
```

Repeat this cycle until **convergence**: the latest review produces **zero findings** that cross any of the 8 delta acceptance thresholds:

| Category | Threshold |
|----------|-----------|
| Correctness | Any delta (even tiny) |
| Token savings | >10% improvement |
| Robustness | Hard failure on valid input |
| Extensibility | Blocks the next milestone's phase type |
| Duplication | >3 instances of same content across files |
| Clarity | Causes misinterpretation in tests or review |
| Consistency | Same concept uses >2 different phrasings |
| All other | Large or critical only |

When zero findings cross any threshold → write decision "ready for progression gate" → iteration complete.

---

## Instructions for Executing Agent

You are responsible for driving this iteration cycle to completion. Execute the following loop:

1. **Run `act-skill-change`** — apply all fix instructions from the current round
2. **Run `act-test-runner`** — run all milestone tests. If any fail, go to step 4.
3. **Run `act-review`** — full 8-dimension review on the new skill version
4. **Run `act-reasoning`** — Reasoner evaluates findings against delta thresholds
5. **Check Reasoner decision:**
   - If "fix issues" → new fix instructions written → go to step 1
   - If "ready for progression" → **STOP — iteration complete**
   - If "STOP and ask the Director" → **STOP — escalate**

### Rules

- Each round increments: `skill/round-1/`, `skill/round-2/`, etc.
- Each round produces one version backup (Backup Agent handles this)
- Never skip steps. Never skip the review after tests pass.
- If tests fail, the Reasoner still runs (on test results instead of review findings)
- Report progress after each act completes: which act finished, pass/fail, score if review
