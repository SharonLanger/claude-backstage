# Repair or try a fresh implementation

## Purpose

Choose the next attempt on a bounded coding task using an agreed requirement and comparable checks.

## When to use this guide

- Repeated patches are not producing a satisfactory implementation.
- Two plausible implementations disagree and you need to decide which to review.

You need a common starting revision, a requirement you can judge, and control over the checks and candidate edits. Separate saved patches or workspaces suffice; parallel agents are optional.

## Quick tip

Keep repairing when observed failure identifies a correction you can verify. If each patch rests on another guess and the task is cheap to reconstruct, preserve the current attempt and try a fresh implementation of the same requirement. Compare both against the same checks. This choice is judgment, not a universal retry rule.

## Guide content

1. Confirm the contract with a failing input, expected result, and an already-working case. If the expected behavior is disputed, settle it first.
2. Set a local attempt or time budget that includes review. Save the existing edits; do not erase useful work to get a clean conversation.
3. Give a repair attempt the requirement, faulty implementation, observed failure, and any supported diagnosis. Give a fresh attempt the same requirement, baseline, interfaces, and constraints, without the failed implementation or its speculative diagnosis. Keep edits separate.
4. Apply the same checks to both. Passing qualifies a candidate for review, not automatic acceptance. Inspect scope, compatibility, and behavior the checks omit. Resolve disagreements against the requirement, not majority vote.
5. If neither is acceptable at the budget, investigate or seek help. If a check was wrong, correct it from the agreed requirement and rerun it on every candidate.

**Original illustration:** A label formatter must preserve the user's order. Both candidates pass a one-label check. With `Zebra, Apple`, a candidate that sorts alphabetically fails. Compare on this agreed case and inspect other behavior before choosing. Agreement between candidates can still hide a shared error.

## Trade-offs and limits

| Choice | Useful when | Cost or limitation |
|---|---|---|
| Repair | Evidence points to a specific correction | A mistaken diagnosis can prolong the loop |
| Fresh attempt | The bounded task can be restated without the failed approach | Reconstructing context and reviewing another diff costs time |
| Clarify or investigate | No trustworthy acceptance condition exists | More candidates do not settle the requirement |

The procedure adapts PAT-0004. It does not claim that regeneration usually wins, establish an ideal retry count, or measure a policy's success rate from one task. For an aligned session, retain useful investigation. For repeatedly lost decisions, use session recovery instead.

## Related patterns

- [Root-Cause-Before-Retry](../patterns/root-cause-before-retry.md#in-a-session-assess-before-naming-a-fix) — examine a proposed diagnosis.
- [Session recovery](../patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work) — preserve decisions across a reset.
- [Bounded Retry](../patterns/bounded-retry.md) — bound implemented retry loops.
- [Review Pass](../../D-verification-evaluation/patterns/D05-review-pass.md) — review survivors.

## Sources

- Theo X. Olausson et al. — [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf), ICLR 2024, §§3–5. Compares repair and fresh samples under matched program budgets; outcomes depend on allocation and feedback. The experiments use self-contained Python tasks with executable tests, not developer selection among repository patches. The manual budget, saved revisions, selection procedure, and illustration are catalog adaptations.
