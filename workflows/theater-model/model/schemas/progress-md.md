# Schema: progress.md

## File name

`progress.md` -- one per Play folder, at the root. The single coordination record for a Run.

**HARD: Only the Stage Manager writes this file.**

## Structure

Two elements in fixed order:

1. **Play status line** -- `**Play status:** \`<status>\``
2. **Progress table** -- one header row, then one row per Act and Gate in execution order.

## Play statuses

| Status | Meaning |
|--------|---------|
| `Ready` | Setup complete; execution has not started. |
| `Running` | Execution or recovery underway. |
| `Waiting for Director` | At a Gate or awaiting a Director decision. |
| `Stopped` | Execution ended without completion. |
| `Completed` | All Play completion conditions met. |

## Table columns

All 11 columns are required. The table header is:

```
| Item | Type | Status | Start time | End time | Duration | Attempt | Retries | Checklist | Result / details | Next action |
```

### Column definitions

| Column | Data type | Rules | Example |
|--------|-----------|-------|---------|
| **Item** | String | Act: `act-<NN>-<slug>`. Gate: `gate-<slug>`. Backtick-wrapped. | `act-02-apply-fixes` |
| **Type** | Enum | `Act` or `Gate`. | `Act` |
| **Status** | Enum | See Act statuses and Gate statuses below. | `Done` |
| **Start time** | Timestamp | **HARD: Includes date and timezone.** Format: `YYYY-MM-DD HH:MM +HH:MM`. Blank if not started. | `2026-10-08 09:32 +03:00` |
| **End time** | Timestamp | Same format as Start time. Blank if in progress or not started. | `2026-10-08 10:05 +03:00` |
| **Duration** | String | **HARD: Present only when both Start time and End time exist.** Human-readable. | `33 min` |
| **Attempt** | Integer | See Attempt/Retry counting. Right-aligned. Gates use `--`. | `2` |
| **Retries** | Fraction | Format: `used / 2`. Gates use `--`. Right-aligned. | `1 / 2` |
| **Checklist** | Links + verdict | Semicolon-separated verification links. Format: `[PASS/FAIL · attempt-NN](path)`. Gates use `--`. | `[FAIL · attempt-01](verifications/act-02/act-02-attempt-01.md); [PASS · attempt-02](verifications/act-02/act-02-attempt-02.md)` |
| **Result / details** | Free text | Evidence links, Director decision scope, exception records, recovery decisions. | See examples below. |
| **Next action** | Free text | What happens next. `--` when no action pending. | `Present final evidence and wait for Director approval.` |

## Act statuses

| Status | Meaning |
|--------|---------|
| `Pending` | Not started. |
| `Running` | Lead is working. |
| `Checking` | Checklist Agent is verifying. |
| `Done` | Completed and checklist passed, or a qualifying Stage Manager exception is recorded (checklist stays FAIL). |
| `Blocked` | Awaiting a dependency or Director decision. |
| `Failed` | Attempt failed; requires recovery assessment. |
| `Skipped` | Explicitly skipped by the Director. Record the decision; never imply checklist success. |

## Gate statuses

| Status | Meaning |
|--------|---------|
| `Closed` | Awaiting Director decision. No end time or duration yet. |
| `Open` | Director has decided. End time and duration are set. Decision recorded in Result / details. |

## Timing rules

- **HARD: All timestamps include date and timezone.**
- **HARD: Duration appears only when both Start time and End time exist.**
- Act duration: first start to verified completion or terminal stop. Includes retries and waiting time. A retry does not reset the start time.
- Gate duration: arrival to approval or terminal decision.

## Attempt / Retry counting

| Attempt value | Meaning |
|---------------|---------|
| `0` | Not started (Pending). |
| `1` | Initial attempt. |
| `2` | First corrective retry. |
| `3` | Second corrective retry (maximum). |

- **Retries** shows `used / 2`. Maximum 2 corrective retries per Act per Run.
- **HARD: Checklist reruns do not consume retries.** Only corrective Lead work increments the attempt count.
- A retry resumes the same Lead instance with retained context.
- Gates show `--` for both Attempt and Retries.

## What goes in Result / details

This cell carries the substantive record. Contents vary by row type:

- **Act (success):** Evidence links to handoffs, summary of what was produced or verified.
- **Act (retry):** What happened in the initial attempt, what correction was applied, link to the corrective verification.
- **Act (exception):** Failed check and report link, observed cause, evidence, affected dependencies, reason progression remains valid.
- **Gate:** Director decision text and exact approved scope. Include links to reviewed evidence.
- **Recovery:** Decisions and reasons when the Stage Manager assessed a failure.

## What goes in Checklist

- Semicolon-separated links to verification reports in `verifications/<act-folder>/`.
- Each link: `[PASS/FAIL · attempt-NN](path)` where NN is the verification execution number (starting at 01).
- Report file names: `<act-folder>-attempt-NN.md`, starting at 01.
- **HARD: Verification numbering is independent of Lead retry counting.**
- Stage Manager exceptions keep the Checklist cell showing FAIL; the exception record goes in Result / details.

## HARD rules

1. Only the Stage Manager writes progress.md.
2. Update progress.md before invoking the next Act and after results, verification, and Director decisions.
3. **Forward-only execution.** Acts proceed forward only; returning to an earlier Act to fix its output requires stopping and asking the Director.
4. Evidence links and Director decision scope go in Checklist and Result / details cells.
5. Recording dispatch is not proof that invocation completed.
6. An interruption alone is not a failure and does not consume a retry.
7. On resume, a Gate without recorded explicit Director approval remains closed.
8. Completed Acts do not open a Gate.
9. Skipped Acts are excluded from completion checks but never represented as verified.

## Template

```markdown
# Progress -- {{play-title}}

**Play status:** `Ready`

| Item | Type | Status | Start time | End time | Duration | Attempt | Retries | Checklist | Result / details | Next action |
|---|---|---|---|---|---|---:|---:|---|---|---|
| `{{act-01-folder}}` | Act | Pending | | | | 0 | 0 / 2 | | | |
| `{{gate-slug}}` | Gate | Closed | | | | -- | -- | -- | | |
| `{{act-02-folder}}` | Act | Pending | | | | 0 | 0 / 2 | | | |
| `{{act-03-folder}}` | Act | Pending | | | | 0 | 0 / 2 | | | |
| `{{gate-slug}}` | Gate | Closed | | | | -- | -- | -- | | |
```

## Constraints

- **No Act definitions.** Acts, checklists, and gates are defined in `play.md`.
- **No execution procedures.** Recovery logic, retry mechanics, and verification procedures belong in `management/` files.
- **No runtime settings.** Model, effort, and other runtime configuration belong in `management/play-rules.md`, Act files, or role files.
- **No checklist criteria.** Criteria live in `play.md`; verdicts live in `verifications/` reports. This table records links and outcomes only.
- **No file edits by other agents.** Only the Stage Manager writes this file. All other agents -- including the Checklist Agent, Leads, and Cast -- have read-only access.
