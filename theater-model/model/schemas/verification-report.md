# Schema: Verification Report

Reference card and template for `<act-folder>-attempt-NN.md` files written by the Checklist Agent.

## File naming

- Pattern: `<act-folder>-attempt-NN.md` where NN is a two-digit number starting at 01.
- NN counts verification executions, independently of Lead retries.
- Example: `act-02-apply-fixes-attempt-01.md`, `act-02-apply-fixes-attempt-02.md`.

## Location

`verifications/<act-folder>/` -- one subfolder per Act, matching the full Act folder name.

## Required sections

| Section | Req? | Type | Description |
|---|---|---|---|
| `# Verification Report -- Act NN: <Title> (Attempt NN)` | Required | HARD | H1 heading. Identifies the Act and attempt number. |
| Header: Checklist Agent instance | Required | HARD | Always `fresh`. Every verification is a new instance with fresh context. |
| Header: Date | Required | HARD | ISO 8601 with timezone (e.g., `2026-10-06T11:22+03:00`). |
| Header: Verdict | Required | HARD | `PASS` or `FAIL`. No other values. |
| `## Checks` | Required | CONFIGURABLE | Table of checks performed against the Act's checklist. |
| `## Summary` | Required | CONFIGURABLE | Pass count, overall verdict, key failures or gaps. |

**HARD** -- structure and constraints baked into the model; not Play-specific.
**CONFIGURABLE** -- content varies per Act and attempt.

## Checks table

| Column | Description |
|---|---|
| # | Sequential check number within this report. |
| Check | What was verified. Matches or derives from the Act's checklist in `play.md`. |
| Result | `PASS`, `FAIL`, or `unable to verify`. No other values. |
| Evidence | File references, counts, observations, or quotes supporting the result. For FAIL, must include expected vs. observed. |

## Failed check detail

Every FAIL or `unable to verify` result must include enough information for the Stage Manager to decide recovery:

- **Requirement** -- what the check expected.
- **Expected vs. observed** -- concrete difference.
- **Evidence** -- file paths, line references, tool output.
- **Missing information** -- what could not be found or verified.
- **Corrections needed** -- what the Lead must fix.

This detail appears in the Evidence column or, if lengthy, in a subsection below the table.

## Verdict rules

- `PASS` — every check in the table is PASS.
- `FAIL` — one or more checks are FAIL or `unable to verify`.
- No partial pass, conditional pass, or "pass with notes." If any check fails, the verdict is FAIL.

This is the canonical terminology. The definition log historically used "OK" in some places — `PASS` is the approved term.

## HARD rules

1. **Only the Checklist Agent writes these files.** The Stage Manager and all other agents have read-only access to `verifications/`.
2. **Earlier reports are never modified or deleted.** Each execution creates exactly one new report.
3. **One new report per verification execution.** Never append to or overwrite an existing report.
4. **Fresh instance per verification.** No context carried from prior verifications or forked from other agents.
5. **Full recheck every time.** The complete current Director-authorized checklist runs against current files. Previous passes are never carried forward.
6. **Verdict integrity.** PASS requires every required check to pass. Pressure, desired outcomes, or progress concerns do not change the evidence.
7. **No invented evidence.** Never fabricate tool output, file contents, check results, or evidence that was not directly observed.
8. **No softened failures.** An observed failure is reported as FAIL, not reframed as a pass or omitted.
9. **Honest uncertainty.** When evidence is missing or a check cannot run, use `unable to verify`. Uncertainty is not a pass.
10. **Scope boundary.** The report must not fix outputs, change checklist criteria, edit progress.md, modify earlier reports, or delegate work.

## Template

```markdown
# Verification Report -- Act {{NN}}: {{Title}} (Attempt {{attempt-NN}})

**Checklist Agent instance:** fresh
**Date:** {{YYYY-MM-DDTHH:MM+TZ}}
**Verdict:** {{PASS or FAIL}}

## Checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | {{check description}} | {{PASS / FAIL / unable to verify}} | {{evidence, file refs, expected vs. observed}} |
| 2 | {{check description}} | {{PASS / FAIL / unable to verify}} | {{evidence}} |

## Summary

{{X/Y checks pass.}} {{Overall verdict and key failures/gaps, or confirmation that outputs are complete.}}
```

## Constraints -- what must NOT appear

- Recommendations or fixes to the Act's outputs.
- Changes to checklist criteria or play.md.
- Progress updates or status changes (belong in progress.md, written by Stage Manager).
- Delegation to other agents.
- References to prior verification results as evidence for current checks (each verification stands alone).
- Runtime settings or actor definitions.
