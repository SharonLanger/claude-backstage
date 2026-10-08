# Examples: Play Definitions

Annotated snippets from two Play examples. Each example shows a different Act ordering for the same domain (skill improvement), demonstrating that Play structure follows from the goal.

## Two Plays, same domain, different sequences

Both examples work with a skill baseline, requirements, and quality criteria. They differ in what they do first:

| Play | Sequence | Why this order |
|------|----------|----------------|
| Skill Improvement | Test → Fix → Review | Starts with evidence of what's broken, then fixes, then reviews the result. |
| Review and Improve | Review → Fix → Test | Starts with analysis, then fixes, then verifies the fixes hold up. |

Neither order is universally better — the right sequence depends on whether you want evidence-first or analysis-first.

---

## Example 1: Goal section

```markdown
## Goal

Test a skill, approve a specific fix list, apply the approved fixes, and review the result.
```

**What makes this good:** One sentence, four verbs, clear sequence. You can read the goal and predict the Act structure.

---

## Example 2: Shared references

```markdown
## Shared references

- `reference/skill-baseline/` — original skill files.
- `reference/requirements.md` — expected behavior and scope.
- `reference/quality-criteria.md` — review criteria.
```

**What makes this good:** Each reference has a path and a short description. A reader immediately knows what shared context exists. Both examples use the same references — the shared data is stable even when Act order changes.

---

## Example 3: Acts and Actors table

**Version A** — grouped by Act:

```markdown
| Act | Lead | Cast |
| --- | --- | --- |
| act-01-run-tests | Test Coordinator | Test Runner; Result Verifier |
| act-02-apply-fixes | Skill Fixer | None |
| act-03-review-quality | Quality Reviewer | Dimension Reviewer; Findings Synthesizer |
```

**Version B** — one row per actor:

```markdown
| Act | Type | Actor | Called by |
| --- | --- | --- | --- |
| Review Quality | Lead | Review Coordinator | Stage Manager |
| Review Quality | Cast | Dimension Reviewer | Review Coordinator |
| Review Quality | Cast | Findings Synthesizer | Review Coordinator |
| Apply Fixes | Lead | Skill Fixer | Stage Manager |
```

**Annotation:** Both layouts are valid. Version A is compact — one row per Act, Cast semicolon-separated. Version B makes delegation explicit with a "Called by" column. Choose based on whether your readers need the delegation chain at a glance.

> **Note:** The column set for this table is not yet finalized as a HARD schema rule. Both layouts appear in the working examples.

---

## Example 4: Act section with inputs and outputs

```markdown
## act

Name: `act-02-apply-fixes`
Lead: `acts/act-02-apply-fixes/lead-skill-fixer.md`

Prepare changes in acts/act-02-apply-fixes/stage/.
Inputs: baseline, Act 01 handoffs, and approved action scope recorded
  in progress.md and identified in the Stage Manager's short prompt.
Outputs: handoffs/act-02-apply-fixes/skill/ and
  handoffs/act-02-apply-fixes/change-report.md.
```

**What makes this good:**
- Names the workspace (`stage/`).
- Inputs include both static references and prior Act handoffs.
- Inputs reference the Director's approved scope from `progress.md` — this Act depends on a Gate decision.
- Outputs are specific: a folder for the updated skill and a named report file.

---

## Example 5: Checklist with verifiable criteria

```markdown
## checklist

For: `act-02-apply-fixes`

- The updated skill and change report exist.
- The action list in the report matches the Director's approval.
- Every approved action is implemented and mapped to the affected files.
- No unapproved changes were introduced.
- No approved action remains unresolved.
```

**What makes this good:**
- Every check is verifiable by reading files — no need to rerun work.
- Checks cover both presence ("exist") and correctness ("matches the Director's approval").
- The last two checks are *negative* conditions — things that should not be true. These catch scope creep and incomplete work.

---

## Example 6: Gate with decision prompt

```markdown
## gate

Name: `gate-approve-fixes`

Present test failures, evidence, proposed fixes, and risks.
Help the Director verify scope and select the exact approved action IDs.
Decision needed: explicit approval of the fixes authorized for Act 02.
```

**What makes this good:**
- **Presentation instructions** tell the Stage Manager what to show: failures, evidence, fixes, risks.
- **Decision hints** guide the Director: verify scope, select action IDs.
- **Decision needed** is specific: "explicit approval of the fixes" — not "decide what to do next."
- The Gate name (`gate-approve-fixes`) is 2 words, well within the 3-word max.

---

## Example 7: Lead-only Act vs multi-Cast Act

**Lead-only** (Act 02 — Apply Fixes):
```
Lead: acts/act-02-apply-fixes/lead-skill-fixer.md
Actor files: lead-skill-fixer.md.
```

One agent does all the work. Appropriate when the task is straightforward and doesn't benefit from decomposition.

**Multi-Cast** (Act 01 — Run Tests):
```
Lead: acts/act-01-run-tests/lead-test-coordinator.md
Actor files: lead-test-coordinator.md, cast-test-runner.md, cast-result-verifier.md.
```

The Lead coordinates. Test Runner executes tests, Result Verifier checks evidence. The Lead consolidates their work in `stage/` and publishes final outputs to `handoffs/`.

**When to add Cast:** When the Act's work has natural subtasks that benefit from focused agents with different scopes. Not every Act needs Cast — Act 02 works fine with a single Lead.
