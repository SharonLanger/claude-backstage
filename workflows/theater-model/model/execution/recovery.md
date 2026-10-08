# Recovery

How the Stage Manager handles failures and retries.

## Retry limits

**2 retries per Act per Run**, in addition to the initial attempt. Maximum 3 total attempts (1 initial + 2 corrective).

## Failure sources

- **Checklist failure** — the Checklist Agent reports FAIL.
- **Lead-reported failure** — the Lead reports it cannot complete the work. This does not require waiting for checklist verification.

## Recovery decision

When an Act fails, the Stage Manager reasons about the cause:

| Situation | Action |
|---|---|
| Current Act issue, retries remaining | Retry: send corrective instructions to the same Lead instance (retained context). |
| No clear recovery path | Stop and ask the Director. |
| Scope or permission change needed | Stop and ask the Director. |
| Retries exhausted | Stop and ask the Director. |
| Earlier Act's output is wrong | Stop and ask the Director (forward-only — cannot go back). |

## Retry mechanics

- The **same Lead instance** resumes with its retained context and corrective instructions. If the Lead instance is unavailable (context lost, session ended), the Stage Manager's corrective prompt must be self-contained enough for a fresh instance to proceed.
- After correction, a **new Checklist Agent instance** re-verifies from scratch — all checks, not just the failed ones. The corrected Act's checklist must pass before any dependent work resumes.
- Checklist reruns alone do not consume Lead retries.
- Recovery never bypasses a Gate.

## Stage Manager exception authority

The Stage Manager may continue despite a failed check **only** when all three conditions hold:

1. The cause is clearly understood with evidence.
2. The failure does not invalidate the Act's required outputs or the next Acts' assumptions.
3. The risk of proceeding is effectively negligible.

When recording an exception in `progress.md`:
- Checklist stays marked **FAIL** with its report link.
- Result / details records: failed check, observed cause, evidence, affected dependencies, reason progression is valid.
- The Act may be marked **Done** on this basis — but Done does not imply the failed check passed.

If there is uncertainty or plausible risk that downstream Acts will use false information — stop and ask the Director. This authority never bypasses a Gate, expands permissions, or changes the checklist verdict.

## Crash recovery

`progress.md` is the single coordination record. On resume after interruption:

1. Read `progress.md` and linked evidence.
2. Continue from the last confirmed state.
3. If the outcome of an interrupted step is uncertain — ask the Director before repeating work.
