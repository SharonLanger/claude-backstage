# Verification and Context Guidelines

Recommendations for verification design and context management. These are guidance, not mandatory rules — the mandatory constraints for verification live in [agents/golden-rules.md](../agents/golden-rules.md) and [execution/recovery.md](../execution/recovery.md).

## Fresh verification is a feature, not a cost

Every Checklist Agent invocation starts from scratch — no memory of prior runs, no carried-forward results. This is deliberate. The repeat investigation is the cost of independent, unbiased verification.

Resist the temptation to optimize this away. A Checklist Agent that remembers its last run is anchored to its previous judgments. Fresh context means every check is re-evaluated against current evidence without bias from prior conclusions.

## Use prior reports for understanding, not inheritance

The Checklist Agent may read earlier verification reports in `verifications/`. The purpose is understanding what was previously flagged and what corrections were attempted — not inheriting untested passes.

Every check must be rerun against current evidence. A check that passed in attempt 01 may fail in attempt 02 because the Lead's corrections introduced a regression. Carrying forward a prior pass without re-checking defeats the purpose of re-verification.

## Design for honest failure

Design criteria so that an honest FAIL or "unable to verify" report is useful, not treated as agent underperformance.

If the Checklist Agent reports "unable to verify" because evidence is genuinely missing, that is the correct behavior — not a sign that the agent failed at its job. The Stage Manager should treat "unable to verify" as actionable information: either the evidence needs to be produced, or the check needs to be reconsidered.

Similarly, a FAIL verdict that includes clear evidence and corrections is more valuable than a questionable PASS. The system works when honest reporting flows freely.

## Separate identity from context

A Lead's name (`lead-schema-check`) provides stable addressing for the Agent tool. But a name by itself does not preserve a Lead's context. When a Lead instance cannot be resumed — session lost, runtime limit hit — a fresh agent with the same name starts without the prior instance's accumulated knowledge.

Design recovery prompts (from Stage Manager to Lead on retry) to be self-contained enough for a fresh Lead to understand what failed and what to do differently. This is the degraded path, not the normal one — but it must work. Note: the details of instance continuity and resume behavior may evolve as the model matures; see [runtime/naming-and-identity.md](../runtime/naming-and-identity.md) for the current state.

## Use progress as the recovery starting point

`progress.md` is the single coordination record. On resume after interruption, start from `progress.md` and work outward:

1. Read the progress table for current Act statuses and attempt counts.
2. Follow links to verification reports and handoff files for evidence.
3. Inspect the evidence rather than trusting status alone.

A status of "Done" in the progress table means the Stage Manager decided to proceed — it does not guarantee every check passed (exceptions are possible). The linked verification report tells the full story.

## Evidence quality matters

Verification is only as good as its evidence. When writing Act definitions and checklists, consider what artifacts the Checklist Agent will need to examine:

- **Concrete artifacts beat verbal claims.** A file in `handoffs/` that the Checklist Agent can read is better than a Lead's assertion that the work is done.
- **Structured output beats narrative.** A JSON file with results is easier to verify mechanically than a prose summary.
- **Preserved artifacts beat transient state.** Files committed to `handoffs/` persist; a running process does not.

The Act's `## Outputs` section should describe artifacts that are both useful to downstream Acts and verifiable by the Checklist Agent.

---

**Related files:**

- [agents/checklist-agent.md](../agents/checklist-agent.md) — the Checklist Agent's role and fresh-instance design
- [agents/golden-rules.md](../agents/golden-rules.md) — the 8 mandatory golden rules
- [execution/recovery.md](../execution/recovery.md) — retry mechanics and crash recovery
- [runtime/naming-and-identity.md](../runtime/naming-and-identity.md) — instance identity and resume behavior
