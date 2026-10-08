# The Stage Manager

The Stage Manager coordinates and monitors execution of a Play. It reads the Play definition and shared rules, calls each Act's Lead in sequence, calls the Checklist Agent for verification, and tracks progress. It does not perform Act work, create assignment files, or verify checklist items itself.

The Stage Manager definition lives in `management/stage-manager.md` within each Play folder.

## Role

The Stage Manager is the execution coordinator — it ensures Acts run in order, verification happens after each Act, Gates are enforced, and the Director is consulted when things go wrong. It sits between the Director (who owns the Play) and the Leads (who do the work).

The Stage Manager never does Act-level work. It reads, reasons, delegates, and records progress.

## Responsibilities

The Stage Manager does five things during a Run:

1. **Sequence execution** — read the Play, call each Act's Lead with a short assignment prompt, and wait for the Act to complete before moving on.
2. **Trigger verification** — after each Act completes, call the Checklist Agent to verify the Act's outputs against its bound checklist.
3. **Enforce Gates** — when a Gate follows an Act's verification, stop and address the Director: identify the Gate, summarize the completed work, link relevant outputs, and use the Play's hints to remind the Director what to inspect or decide. Then wait for explicit Director approval before continuing. No agent, no checklist result, and no prior approval can bypass a Gate.
4. **Manage recovery** — when verification fails or a Lead reports failure, decide whether to retry the Act or escalate to the Director. Send short recovery prompts pointing to failure and verification reports; the Lead handles the actual work.
5. **Maintain progress** — record Act statuses, timestamps, verification results, exceptions, and recovery decisions in `progress.md`.

Reading reports and reasoning about recovery is part of the Stage Manager's job, but it is not a substitute for checklist verification. The Checklist Agent always produces the formal verdict.

## Delegation

The Stage Manager delegates through Leads — one per Act. It does not call Cast agents directly. Each Lead receives a short assignment prompt and loads its own context independently; it is not forked from the Stage Manager's context.

The one exception to Lead-only delegation is the Checklist Agent. The Stage Manager calls the Checklist Agent directly after each Act completes. This is a verification call, not a work assignment.

There is no Director Helper role and no special Gate editing permission. The Stage Manager operates within its defined authority.

## Recovery

When an Act fails — whether reported by the Lead or surfaced by the Checklist Agent — the Stage Manager has a bounded recovery process.

Each Act gets two retries per Run, in addition to the initial attempt (three total attempts). On retry, the Stage Manager resumes the same Lead instance with its retained context. It does not start a fresh Lead. The recovery prompt is short and points to the failure evidence; the Lead decides how to fix it.

Execution is forward-only. If a downstream Act discovers that an earlier Act produced wrong output, the Stage Manager cannot go back. It stops and asks the Director.

The decision tree:

- **Current Act issue** — retry the Lead with corrective instructions.
- **Earlier Act issue** — stop and ask the Director (forward-only execution).
- **No clear recovery path or retries exhausted** — stop and ask the Director.

## Exception authority

The Stage Manager may continue past a failed checklist item only when all three conditions are met:

1. The cause is clearly understood.
2. The failure does not invalidate the Act's required outputs or the next Acts' assumptions.
3. The risk of proceeding is effectively negligible.

When these conditions hold, the Stage Manager records the exception in `progress.md` before proceeding. The failed verdict stays intact — FAIL remains FAIL. The exception is a decision to continue despite the failure, not a reclassification of the result.

The Stage Manager never bypasses a Gate, expands its own permissions, or changes a verification verdict.

## Access

The Stage Manager has narrow, defined access:

**Reads:**

- `play.md` — the Play definition
- `management/play-rules.md` — shared rules (loaded via @ reference)
- Its own definition (`management/stage-manager.md`)
- `progress.md` — execution state
- All `handoffs/` folders — Act outputs
- All `verifications/` folders — checklist results

**Writes:**

- `progress.md` only

The Stage Manager never writes to Act folders, handoff folders, verification folders, or management files other than `progress.md`. The shared rules in `play-rules.md` are static and locked during execution — only the Director can modify them.

---

For the file format specification — sections, fields, and heading syntax for `management/stage-manager.md` — see [schemas/stage-manager-md.md](../schemas/stage-manager-md.md).
