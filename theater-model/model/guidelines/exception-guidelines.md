# Exception Assessment Guidelines

Recommendations for the Stage Manager when evaluating whether to exercise exception authority. These are guidance, not mandatory rules — the mandatory boundary and recording requirements live in [agents/stage-manager.md](../agents/stage-manager.md) and [execution/recovery.md](../execution/recovery.md).

## The three conditions

The Stage Manager may continue despite a failed check only when all three conditions hold (defined as mandatory in [agents/stage-manager.md](../agents/stage-manager.md)):

1. The cause is clearly understood with evidence.
2. The failure does not invalidate the Act's required outputs or the next Acts' assumptions.
3. The risk of proceeding is effectively negligible.

The guidance below helps assess whether each condition is genuinely met.

## Condition 1: Compare against baseline evidence

"Clearly understood" means the Stage Manager can point to specific evidence explaining the failure — not just a plausible theory.

**Compare against baseline.** If the failure is alleged to be a pre-existing issue (e.g., "this test was already flaky"), compare against baseline evidence. Does a prior verification report show the same failure? Is there documentation of the known issue? Do not accept the label "pre-existing" without evidence that the condition existed before the current Act's work.

**Evidence, not inference.** "The test probably failed because of a timeout" is inference. "The test log shows a 30-second timeout at line 47, and the same timeout appears in the baseline run from before this Act" is evidence.

## Condition 2: Check downstream dependencies

"Does not invalidate the next Acts' assumptions" requires looking beyond the failed check itself.

**Check what downstream Acts depend on.** Read the next Act's `## Inputs` section. If it references an artifact that the failed check was supposed to validate, the exception may not be safe — even if the failure looks minor in isolation.

**Percentage of passing checks is not the criterion.** 95% of checks passing does not mean the remaining 5% are safe to skip. A single failed check on a critical output can invalidate everything downstream. Assess impact, not ratios.

**Consider the transitive chain.** If Act 2 depends on Act 1's output, and Act 3 depends on Act 2's output, a failure in Act 1's verification may ripple through both.

## Condition 3: Distinguish the verdict from the decision

A justified exception is not a passing check. The Checklist Agent's FAIL verdict stays FAIL. The exception is the Stage Manager's decision to continue despite the failure — a separate act recorded separately in `progress.md`.

**The recording must include:**

- Which check failed.
- The observed cause and supporting evidence.
- Which downstream dependencies were assessed.
- Why proceeding is valid despite the failure.

This recording exists so the Director can review the exception decision and so future crash recovery can understand why the Act was marked Done despite a FAIL verdict.

## When to stop instead

If any of the following apply, do not exercise exception authority — stop and ask the Director:

- The cause is unclear or speculative.
- The failed check validates an artifact that downstream Acts depend on.
- The failure could mean false information flows to the next Act.
- You are uncertain whether the risk is negligible.
- A Gate follows this Act (exception authority never bypasses a Gate).

Stopping is not a failure of the Stage Manager. It is the correct behavior when the exception conditions are not clearly met. The Director exists precisely to make decisions the Stage Manager cannot.

## The boundary: what exception authority is not

Exception authority is narrowly scoped:

- It cannot bypass a Gate.
- It cannot expand the Stage Manager's permissions.
- It cannot change or reinterpret the checklist verdict.
- It cannot retroactively modify earlier verification reports.

The Stage Manager decides whether to proceed despite a failure. It does not decide whether the failure should have been a pass.

---

**Related files:**

- [agents/stage-manager.md](../agents/stage-manager.md) — exception authority definition and three conditions
- [execution/recovery.md](../execution/recovery.md) — retry limits, exception recording, and crash recovery
- [rules/authority.md](../rules/authority.md) — Gate enforcement and authority hierarchy
