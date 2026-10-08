# Lifecycle

Status definitions for Plays, Acts, and Gates.

## Play statuses

| Status | Meaning |
|---|---|
| **Ready** | Setup complete. Execution has not started. |
| **Running** | Execution or recovery underway. |
| **Waiting for Director** | At a Gate or awaiting a Director decision. |
| **Stopped** | Execution ended without completion. |
| **Completed** | All completion conditions met (see below). |

### Completion conditions

A Play is complete only when:
- All required Acts are Done.
- Each required verification has passed (or has a qualifying documented Stage Manager exception).
- Every required Gate has explicit Director approval.

Skipped Acts are excluded from completion checks but recorded as Skipped — their checklists are not marked as passed.

## Act statuses

| Status | Meaning |
|---|---|
| **Pending** | Not started. |
| **Running** | Lead is working. |
| **Checking** | Checklist Agent is verifying. |
| **Done** | Checklist passed, or a qualifying SM exception is recorded (checklist retains FAIL). |
| **Blocked** | Awaiting a dependency or Director decision. |
| **Failed** | An attempt failed; requires recovery assessment. |
| **Skipped** | Explicitly skipped by the Director. |

## Gate statuses

Gates have two states, independent of Act status:

| Status | Meaning |
|---|---|
| **Closed** | Waiting for Director approval. |
| **Open** | Director has approved; execution may proceed. |

Gates only move from Closed to Open. Once a Gate is opened and execution moves past it, all prior Acts and their outputs are locked.
