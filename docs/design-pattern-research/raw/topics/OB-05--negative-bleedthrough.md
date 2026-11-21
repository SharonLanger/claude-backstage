---
topic_id: OB-05
title: "Negative bleedthrough"
coverage: partially supported
source_edges:
  - id: SRC-0012
    relationship: DIRECT
    strength: moderate
    finding: "Models often had difficulty when a benchmark instruction reversed which of the supplied answers should be selected."
  - id: SRC-0021
    relationship: SUPPORTING
    strength: moderate
    finding: "A generated response used a segmented format despite an explicit prohibition, without a comparison to prompts that omit the prohibition."
pattern_ids: []
publication_status: published
---

# OB-05 — Negative bleedthrough

“I told the assistant to leave the snapshots alone and it regenerated them.” “Did mentioning the forbidden action make it more likely?” The accepted evidence establishes difficulty following some reversed instructions. The brief’s specific claim that a prohibition itself makes the forbidden action more likely, through increased activation of its tokens, remains untested by these sources.

## What the sources measure

- **Reversing an instruction can expose a persistent default.** Jang et al. manually reversed the selection criterion in nine language tasks and evaluated the same 300 items per dataset under both conditions. The model ranked supplied answers, and several distractors could qualify under the reversed criterion. Figure 1 shows one case where GPT-3 selects the same answer under both wordings. Across model sizes, the reported trend for zero-shot GPT-3 and OPT pairs rising ordinary-task accuracy with declining reversed-task accuracy. An unchanged answer earns one point across a pair with complementary scoring, but a two-condition average near 50% leaves the actual frequency of unchanged answers unidentified. In-context GPT-3 175B on QA was a reported exception to that approximate mean. SRC-0012:C01–C08, Fig. 1, §§2.1–3.2 Figs. 2–3 and Appendix A Fig. 4. [Dossier](../sources/SRC-0012--negated-instructions.md) · [Original paper](https://proceedings.mlr.press/v203/jang23a.html)
- **A prohibition can be violated in generated text.** In one selected Inverse IFEval error case, a model divided an answer into sections despite an explicit prohibition on segmentation. The benchmark also includes a code category that forbids comments, and its illustrated prompt constrains naming and response format as well. A category score cannot attribute a coding failure to inclusion of a comment. The paper also has an unresolved category-weighting discrepancy, so the rate for that constraint remains open. This experiment was run independently of Jang’s and evaluates generated output with rubrics. It does not compare how often the same behavior occurs with and without naming it in the prompt. SRC-0021:C03, C05, C07, C13, §§2.4–2.5 Fig. 3, §3.1 Table 2, Appendix D Figs. 9–10 and Appendix F Fig. 16. [Dossier](../sources/SRC-0021--instructions-against-learned-conventions.md) · [Original paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf)

Jang et al. propose a training bias toward ordinary continuations, but measure ranked choices. They do not compare prohibitions to equivalent prompts that omit the forbidden action, or intervene on internal model representations. The results cannot tell whether mentioning an action raises its probability above a no-mention baseline or whether a positive instruction preserves a coding constraint more reliably. SRC-0012:C04, C11, §3.1 “A Conjecture on Why Inverse Scaling Exists” and the companion scorer. [Dossier](../sources/SRC-0012--negated-instructions.md) · [Original paper](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5)

## Pattern coverage

There is no accepted pattern for a polarity-specific mitigation. An agent violating a prohibition is a behavior a developer can verify. Attributing it to the prohibition’s wording would require a comparison that holds the required behavior fixed and measures the forbidden action under each wording and a suitable baseline.

## Drive navigation

- [audits/SRC-0012--verification.md](../audits/SRC-0012--verification.md) · [Local copy](../audits/SRC-0012--verification.md)
- [audits/SRC-0021--verification.md](../audits/SRC-0021--verification.md) · [Local copy](../audits/SRC-0021--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0012--negated-instructions.md](../sources/SRC-0012--negated-instructions.md) · [Local copy](../sources/SRC-0012--negated-instructions.md)
- [sources/SRC-0021--instructions-against-learned-conventions.md](../sources/SRC-0021--instructions-against-learned-conventions.md) · [Local copy](../sources/SRC-0021--instructions-against-learned-conventions.md)
