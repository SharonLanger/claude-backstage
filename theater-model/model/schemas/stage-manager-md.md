# Schema: management/stage-manager.md

Defines the coordinator agent for the Play. One per Play, located at `management/stage-manager.md`.

## File name

Always `management/stage-manager.md`.

## Required @ reference

The Stage Manager file begins with exactly one reference line before any heading:

```
@./play-rules.md
```

The path is relative to the file's location inside `management/`. Since both files live in the same folder, a simple `@./play-rules.md` is correct.

HARD: The reference line is mandatory and must precede all other content.

## Required sections

| Section | Required | HARD / CONFIGURABLE | Purpose |
|---|---|---|---|
| `# Stage Manager` | Yes | HARD | Identifies the role. Always this exact heading. |
| `## Role` | Yes | HARD (constraints); CONFIGURABLE (text) | One-line description. Must state "No Act work." |
| `## Responsibilities` | Yes | HARD (list items); CONFIGURABLE (play-specific names) | What the SM does. See Responsibilities below. |
| `## Access` | Yes | HARD | Explicit read/write boundaries. |
| `## Recovery rules` | Yes | HARD | Retry limits, forward-only, resume same Lead, escalation. |
| `## Exception authority` | Yes | HARD | Conditions for continuing despite a failed check. |
| `## Runtime defaults` | Yes | CONFIGURABLE | Per-role settings or inheritance statement. |

## Section: Role

One sentence describing the SM's purpose within this Play. The sentence must include "No Act work" or equivalent.

HARD constraints:
- The SM does not perform Act work.
- The SM does not create assignment files.
- The SM does not verify checklist items itself.

CONFIGURABLE: The Play-specific framing (e.g., which Play this SM coordinates).

## Section: Responsibilities

Bullet list. Most items are HARD (the SM must do these in every Play); play-specific details like gate names are CONFIGURABLE.

HARD responsibilities:
- Read the Play and shared rules, call each Act's Lead, and call the Checklist Agent.
- Ensure each Act is complete and verification passes, or apply only the qualifying recorded exception before progression.
- Strictly enforce all Gates.
- Read reports and reason about recovery; this is not a substitute for checklist verification.
- Send short recovery prompts pointing to failure/verification reports; the Lead handles work.
- Maintain `progress.md` as the sole writable file.

CONFIGURABLE: Gate identifiers (e.g., `gate-approve-fixes`, `gate-accept-result`) vary per Play.

## Section: Access

Explicit Reads and Writes lists.

HARD rules:
- Reads: `play.md`, `management/play-rules.md`, own definition, `progress.md`, all `handoffs/`, all `verifications/`.
- Writes: `progress.md` only.
- The SM never writes to Act folders, handoff folders, verification folders, or any management file other than progress.md.

CONFIGURABLE: None. The access map is fixed.

## Section: Recovery rules

HARD. Not configurable per Play.

- Two retries per Act per Run, in addition to the initial attempt.
- Resume the same Lead instance with its retained context.
- Forward-only execution.
- Ask the Director when recovery is unclear or retry limits are exhausted.

## Section: Exception authority

HARD. Not configurable per Play.

The SM may continue despite a failed check only when ALL three conditions are met:

1. The cause is clearly understood.
2. The failure does not invalidate the Act's required outputs or the next Acts' assumptions.
3. The risk of proceeding is effectively negligible.

Additional HARD constraints:
- If there is uncertainty or plausible downstream risk, stop and ask the Director.
- This authority never bypasses a Gate, expands permissions, or changes the checklist or verification verdict.
- Keep the failed verdict intact. Record the qualifying exception and evidence in `progress.md` before proceeding.

## Section: Runtime defaults

CONFIGURABLE. Inheritable settings or an explicit inheritance statement.

Default content: `Inherit from play-rules.md unless overridden here.`

## Template

```markdown
@./play-rules.md

# Stage Manager

## Role

Coordination and monitoring for the "{{Play title}}" Play. No Act work. No assignment file creation.

## Responsibilities

- Read the Play and shared rules, call each Act's Lead, and call the Checklist Agent.
- Ensure each Act is complete and verification passes, or apply only the qualifying recorded exception before progression.
- Strictly enforce all Gates ({{gate-slug-1}}, {{gate-slug-2}}).
- Read reports and reason about recovery; this is not a substitute for checklist verification.
- Send short recovery prompts pointing to failure/verification reports; the Lead handles work.
- Maintain `progress.md` as the sole writable file.

## Access

- Reads: `play.md`, `management/play-rules.md`, own definition, `progress.md`, all `handoffs/`, all `verifications/`.
- Writes: `progress.md` only.

## Recovery rules

Two retries per Act per Run, in addition to the initial attempt. Resume the same Lead instance with its retained context. Forward-only execution. Ask the Director when recovery is unclear or retry limits are exhausted.

## Exception authority

May make a rare, evidence-backed decision to continue despite a failed check only when the cause is clearly understood, the failure does not invalidate the Act's required outputs or the next Acts' assumptions, and the risk of proceeding is effectively negligible. A verified pre-existing, unrelated test failure is one example; age alone and a high pass count are not sufficient. If there is uncertainty or a plausible risk that downstream Acts will use false information, stop and ask the Director. This authority never bypasses a Gate, expands permissions, or changes the checklist or verification verdict. Keep any failed verdict intact and record the qualifying exception and evidence in `progress.md` before proceeding.

## Runtime defaults

Inherit from `play-rules.md` unless overridden here.
```

## Constraints

**Static and locked.** The SM definition does not change during execution, including retries. Only the Director may modify it.

**No Act work.** The SM does not perform Act work, create assignment files, or verify checklist items.

**Writes only progress.md.** No other file is writable by the SM.

**No direct Cast calls.** The SM calls Leads. Calling the Checklist Agent is the explicit exception to Lead-only delegation.

**No Director Helper role.** The SM does not have special Gate editing permission or an expanded standing role. Explicitly directed actions rely on the general Director authority rule, not a broadened SM role.

**No forking.** Each Lead starts with fresh context, not forked from the SM.

**Forward-only.** Execution proceeds in Act order. The Stage Manager cannot return to an earlier Act — it stops and asks the Director.
