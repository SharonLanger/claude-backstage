# How a Play Runs

A narrative walkthrough of execution from start to finish. No rules here — just the story of what happens.

## Before execution: Setup

The Director (or a helper agent) prepares a fresh Play folder: creates the folder structure, writes `play.md` with the workflow definition, populates `reference/` and `props/` with input files, and places the management definitions (`play-rules.md`, `stage-manager.md`, `checklist-agent.md`). The Stage Manager does not participate in setup.

## Execution begins

The Stage Manager reads `play.md` and `play-rules.md`, initializes `progress.md`, and starts the first Act.

### Running an Act

1. The Stage Manager calls the Act's Lead with a short prompt pointing to the Act definition and relevant inputs.
2. The Lead reads its role file, the Act definition, and shared rules. If the Act has Cast, the Lead assigns them subtasks — each Cast gets fresh context and works within its defined scope.
3. Cast write their results to `stage/` and may also write to `handoffs/<act>/`. The Lead consolidates the work and the Act's agents publish final outputs to `handoffs/<act>/`.

### Verification

4. The Stage Manager calls the Checklist Agent — a fresh instance with no memory of prior checks.
5. The Checklist Agent runs every check in the Act's checklist against the current outputs. It writes a report to `verifications/<act>/` with a verdict: PASS or FAIL.

### If verification passes

6. The Stage Manager marks the Act as Done in `progress.md` and checks what's next.

### If verification fails

7. The Stage Manager reads the failure report, reasons about the cause, and sends the Lead corrective instructions. The same Lead instance resumes with its retained context. Up to 2 retries are allowed per Act per Run (3 total attempts including the initial).
8. After correction, a new Checklist Agent instance re-verifies from scratch — all checks, not just the failed ones.
9. If retries are exhausted without success, the Stage Manager stops and asks the Director.

### At a Gate

10. The Stage Manager stops. It presents the Director with a summary of completed work, links to evidence, and the Gate's decision prompt.
11. The Director reviews, decides, and responds. The decision and its scope are recorded in `progress.md`.
12. Only after explicit Director approval does the Stage Manager proceed to the next Act.

### Completion

13. When all required Acts are Done, all verifications have passed (or have qualifying documented exceptions), and all Gates have Director approval — the Play is complete. The Stage Manager records this in `progress.md`.

## What can interrupt this flow

- **A Lead reports failure directly** — doesn't have to wait for checklist verification.
- **The Director skips an Act** — recorded as Skipped, not Done. Checklists are not falsely marked as passed.
- **An earlier Act's output turns out to be wrong** — execution is forward-only. The Stage Manager cannot go back. It stops and asks the Director.
- **The Director overrides a rule** — within stated scope only, recorded in progress.
