# Family D — Verification & Evaluation: Patterns

Navigation hub for the 12 pattern files in this folder.

---

## Key Insight

Verification must be externalized. Per Hamel Husain & Shreya Shankar: run end-to-end task success (D11) first to confirm something is actually broken, then use step-level diagnostics (D12) to find which step caused it. Never design targeted evals before you have inspected real failing traces.

---

## File Tree

```
patterns/
├── README.md                          ← this file
├── D01-deterministic-validator.md     ← schema / regex / constraint checks at zero LLM cost
├── D02-test-before-done.md            ← passing a test suite defines task completion
├── D03-evidence-based-completion.md   ← completion requires cited, retrievable artefacts
├── D04-independent-verifier.md        ← context-isolated agent re-checks the output
├── D05-review-pass.md                 ← structured checklist scan over required properties
├── D06-generator-critic.md            ← separate critic issues binary approve / revise
├── D07-evaluator-optimizer.md         ← graded evaluator score drives iterative revision
├── D08-multi-review-ensemble.md       ← N independent reviewers, majority or unanimous gate
├── D09-llm-as-judge.md                ← LLM scores output on a rubric for qualitative criteria
├── D10-human-calibration.md           ← spot-check LLM judge scores against human labels
├── D11-end-to-end-task-success.md     ← pass/fail verdict on the real outcome of a full task
└── D12-step-level-diagnostic.md       ← isolate which pipeline step introduced a failure
```

---

## Schema

Each engineering pattern follows this structure:

| Section | Contents |
|---------|----------|
| **Intent** | One-sentence summary and common aliases |
| **Problem** | What failure mode the pattern addresses |
| **Solution** | The mechanism that resolves it |
| **Structure** | Mermaid component diagram (collapsed `<details>` block) |
| **When to Use** | Preconditions that make this pattern appropriate |
| **When NOT to Use** | Cases where a different pattern is better |
| **Implementation Notes** | Pseudocode, prompt templates, or design rules |
| **Cost Profile** | Latency / token cost / implementation / false-positive risk table |
| **Related Patterns** | Cross-links to complementary or alternative patterns |
| **Anti-Patterns Addressed** | Named anti-patterns this pattern prevents |
| **Sources** | Attributed primary sources with URLs |

---

## How to Navigate

**Starting from a blank slate** — use `../guides/eval-type-selector.md`. Answer the decision-tree questions; each branch names a pattern code (D01–D12) that links here.

**Starting from cost constraints** — use `../guides/verification-ladder.md`. Each rung maps directly to a pattern group: Rung 1 = D01/D02, Rung 2 = D03/D05, Rung 3 = D04/D06/D08, Rung 4 = D07/D09/D12, Rung 5 = D10/D11.

**Starting from a failure** — go to D11 first (was the full task actually wrong?), then D12 (which step?). Then use eval-type-selector to pick targeted patterns for the root-cause step.

**Stacking patterns** — patterns compose. A coding agent typically runs D01 → D02 → D04. A research agent runs D03 → D05 → D09 → D10. See `../guides/eval-type-selector.md` for common stacks.

---

Last updated: 2026-08-24
