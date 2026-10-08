# Execution Examples

Annotated progress tables showing how `progress.md` evolves during a Run. These examples use the "Review, Fix, and Test a Skill" Play — three Acts, two Gates.

## Example 1: Initial state (just started)

The Stage Manager has initialized `progress.md` and is about to call the first Lead.

```
Play status: Running

| Item | Type | Status | Start time | End time | Duration | Attempt | Retries | Checklist | Result / details | Next action |
|---|---|---|---|---|---|---:|---:|---|---|---|
| act-01-review-quality | Act | Running | 2026-10-08 09:00 | — | — | 1 | 0 / 2 | — | — | Lead called with assignment prompt |
| gate-approve-fixes | Gate | Closed | — | — | — | — | — | — | — | — |
| act-02-apply-fixes | Act | Pending | — | — | — | — | — | — | — | — |
| act-03-run-tests | Act | Pending | — | — | — | — | — | — | — | — |
| gate-accept-result | Gate | Closed | — | — | — | — | — | — | — | — |
```

**What to notice:**

- All future Acts are Pending. Gates are Closed.
- Attempt is 1 (initial), retries 0 / 2 (none used, 2 available).
- No Checklist or Result columns populated yet — work hasn't completed.

## Example 2: Mid-run with a retry

Act 1 completed successfully. The Director approved the Gate. Act 2 failed its first verification, the Stage Manager retried the Lead, and the second verification passed.

```
Play status: Running

| Item | Type | Status | Start time | End time | Duration | Attempt | Retries | Checklist | Result / details | Next action |
|---|---|---|---|---|---|---:|---:|---|---|---|
| act-01-review-quality | Act | Done | 09:00 | 09:20 | 20 min | 1 | 0 / 2 | PASS · attempt-01 | Review report identifies three proposed fixes: F01, F02, F03. | — |
| gate-approve-fixes | Gate | Open | 09:20 | 09:25 | 5 min | — | — | — | Director: "Approve F01 and F02; exclude F03. Proceed." | — |
| act-02-apply-fixes | Act | Done | 09:25 | 09:55 | 30 min | 2 | 1 / 2 | FAIL · attempt-01; PASS · attempt-02 | First attempt omitted F02. SM resumed same Lead with corrective prompt. Fresh CA reran all checks. F01 and F02 confirmed. | — |
| act-03-run-tests | Act | Running | 09:55 | — | — | 1 | 0 / 2 | — | — | Lead called |
| gate-accept-result | Gate | Closed | — | — | — | — | — | — | — | — |
```

**What to notice:**

- Act 2 shows Attempt 2 and Retries 1 / 2 — one retry used, one remaining.
- The Checklist column records both verification attempts: FAIL on attempt-01, PASS on attempt-02.
- The Result column explains what happened and what was corrected.
- The same Lead instance was resumed (retained context), but a fresh Checklist Agent ran all checks from scratch.

## Example 3: Completed Play waiting for final Gate

All Acts done, final Gate waiting for Director approval.

```
Play status: Waiting for Director

| Item | Type | Status | Start time | End time | Duration | Attempt | Retries | Checklist | Result / details | Next action |
|---|---|---|---|---|---|---:|---:|---|---|---|
| act-01-review-quality | Act | Done | 09:00 | 09:20 | 20 min | 1 | 0 / 2 | PASS · attempt-01 | Review report with F01, F02, F03 identified. | — |
| gate-approve-fixes | Gate | Open | 09:20 | 09:25 | 5 min | — | — | — | Director approved F01, F02; excluded F03. | — |
| act-02-apply-fixes | Act | Done | 09:25 | 09:55 | 30 min | 2 | 1 / 2 | FAIL · attempt-01; PASS · attempt-02 | F01 and F02 implemented, F03 untouched. | — |
| act-03-run-tests | Act | Done | 09:55 | 10:10 | 15 min | 1 | 0 / 2 | PASS · attempt-01 | 12/12 required tests pass. | — |
| gate-accept-result | Gate | Closed | 10:10 | — | — | — | — | — | Final acceptance requested. | Present evidence, wait for Director |
```

**What to notice:**

- Play status is "Waiting for Director" — the final Gate is Closed.
- All Acts are Done. The Stage Manager has presented evidence and is waiting.
- The Gate does not open automatically when Acts complete. Only explicit Director approval opens it.

## Example 4: Exception scenario

Act 2 has a failed check, but the Stage Manager exercises exception authority to continue.

```
| act-02-apply-fixes | Act | Done | 09:25 | 09:50 | 25 min | 1 | 0 / 2 | FAIL · attempt-01 | Check 3 (lint-clean) failed: 2 pre-existing lint warnings in unchanged files. Exception: cause is pre-existing (verified against baseline), does not affect required outputs (F01/F02 changes are lint-clean), negligible risk. Proceeding per exception authority. | — |
```

**What to notice:**

- The Act is marked Done despite a FAIL checklist verdict.
- The Result column records the exception with all three condition assessments: cause understood, outputs not invalidated, risk negligible.
- The FAIL verdict is preserved — Done does not mean the failed check passed.
- This exception could not bypass a Gate. If `gate-approve-fixes` followed this Act, the Stage Manager would still stop and present evidence.

## Recovery scenario walkthrough

**Situation:** Act 2's checklist fails. The Checklist Agent reports that fix F02 was not applied.

**Step 1 — Stage Manager reads the report.** The verification report in `verifications/act-02-apply-fixes/act-02-apply-fixes-attempt-01.md` shows: check "F02 applied" failed. Evidence: the target file was not modified.

**Step 2 — Stage Manager decides: retry.** This is a current-Act issue with retries remaining (0 / 2 used). The SM resumes the same Lead instance via `SendMessage(to: "lead-fix-applier")` with a short corrective prompt: "F02 was not applied — see verification report attempt-01. Please apply F02 and re-publish to handoffs/."

**Step 3 — Lead corrects.** The Lead, retaining context from its first attempt, applies F02 and updates `handoffs/act-02-apply-fixes/`.

**Step 4 — Stage Manager triggers re-verification.** A fresh Checklist Agent instance runs the complete checklist from scratch — all checks, not just the failed one. This is attempt-02.

**Step 5 — Verification passes.** The Stage Manager marks Act 2 as Done with attempt 2, retries 1 / 2.

**If retry had failed again:** The SM would have one more retry (attempt 3, retries 2 / 2). After that, retries exhausted — stop and ask the Director.

**If the failure pointed to Act 1's output:** Forward-only execution. The SM cannot go back to Act 1. It stops and asks the Director.

---

For status definitions, see [lifecycle.md](lifecycle.md). For the full recovery decision tree, see [recovery.md](recovery.md). For the execution sequence, see [flow.md](flow.md).
