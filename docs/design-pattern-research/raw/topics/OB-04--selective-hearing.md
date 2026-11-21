---
topic_id: OB-04
title: "Selective hearing"
coverage: partially supported
source_edges:
  - id: SRC-0021
    relationship: DIRECT
    strength: moderate
    finding: "Generated responses sometimes used familiar formats or routines despite explicit exceptions, with results varying by benchmark category and inference setting."
  - id: SRC-0012
    relationship: SUPPORTING
    strength: moderate
    finding: "Some tested models favored ordinary answers after the instruction reversed the answer-selection criterion."
  - id: SRC-0022
    relationship: SUPPORTING
    strength: moderate
    finding: "Explicit constraint violations were the most common coded symptom among surfaced misalignment episodes in public coding-agent logs."
  - id: SRC-0020
    relationship: SUPPORTING
    strength: moderate
    finding: "Some repository guidance corresponded to observable changes in testing and tool use, while adherence to individual counter-conventional rules was unmeasured."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic distinguishes prompt guidance from application controls that enforce a rule in the product."
pattern_ids: [PAT-0006]
publication_status: published
---

# OB-04 — Selective hearing

“I asked for one paragraph and it keeps adding headings.” “The agent read the local exception and then applied the usual convention.” The brief asks whether explicit requirements fail when they conflict with a learned default and whether prompting can resolve the conflict. Selected outputs demonstrate missed exceptions. Training causation and the claim that rewording cannot help are open.

## What the sources measure

- **A response can satisfy the ordinary task and break the exception.** Zhang et al. scored generated responses across 1,012 English and Chinese prompts in eight categories, using category-specific model judges with an expert-scored validation comparison. One selected result segments a travel plan despite an explicit instruction to keep it unsegmented. Another produces all five answers that are ordinarily correct where the prompt asked for only one. The code category includes requests to omit comments, and its illustrated prompt also constrains variable naming and code-block output. A miss on that composite item cannot by itself establish that the comments requirement failed. The paper’s code and formatting category counts and table scores show a weighting discrepancy, so these examples support a qualitative finding rather than category-specific failure rates. SRC-0021:C02–C05, C07–C08, C13, §§2.2–2.5 Fig. 3, §3.1 Table 2, Appendix D Figs. 9–10 and Appendix F Figs. 16, 19. [Dossier](../sources/SRC-0021--instructions-against-learned-conventions.md) · [Original paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf)
- **The failures are sensitive to what is tested.** The same study reports category and model differences. The tested Doubao model’s always-thinking setting scored highest across the two language sets compared with direct response and adaptive mode. Selecting the highest rubric score from multiple independent samples also improved reported results. Neither comparison isolates an alternative wording of a fixed requirement. The benchmark was informed by common conventions the authors saw in supervised fine-tuning data. It did not vary training exposure, and its comparison with IFEval combines differences in task mix and judging. SRC-0021:C01, C08–C12, §§1–2.2, §3.2 Figs. 4–6 and Appendix E.1 Fig. 15. [Dossier](../sources/SRC-0021--instructions-against-learned-conventions.md) · [Original paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=8)
- **Independent experiments show both default persistence and some response to guidance.** Jang et al. reversed task criteria while holding the item fixed and documented cases in which a model picked the ordinary answer anyway. Their scoring concerned ranking supplied answers, distinct from Zhang et al.’s evaluation of generated outputs. Gloaguen et al. compared repository context files with omission on Python bug-fix benchmarks. Runs with files executed more tests and were more likely to use named tools. The authors did not track adherence to specific exceptions and file packages bundled several changes, so the trace differences do not identify when a prompt can override a convention. SRC-0012:C01–C06, Fig. 1 and §§2.1–3.1. SRC-0020:C01, C05, §§3.2, 4.1 and 4.3 Fig. 5. [Negation dossier](../sources/SRC-0012--negated-instructions.md) · [Original proceedings](https://proceedings.mlr.press/v203/jang23a.html) · [Repository files dossier](../sources/SRC-0020--repository-context-files.md) · [Versioned paper](https://arxiv.org/html/2602.11988v3)
- **Coding-session logs also document missed constraints.** Tang et al. coded explicit constraint violations in 38.33% of 16,118 validated misalignment episodes. The study required a later developer response that made the divergence visible. Of the cause assignments for constraint violations, 73.68% received the residual instruction-following label, which records a clear instruction followed by divergence without evidence of a more specific cause. These shares describe surfaced episodes and their labels. The study leaves open the prevalence across all coding requests and the role of training conventions. SRC-0022:C01, C03, C07–C08, §§3.2–3.3, §4.1 Table 3 and Fig. 2, and Appendix D.3. [Dossier](../sources/SRC-0022--observed-developer-agent-misalignment.md) · [Original paper and Table 3](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=6) · [Figure 2](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=7)

Inverse IFEval’s conference paper, earlier preprint and dataset are one project. Tang et al. add observational evidence from public log collections independent of the three benchmark studies. Their analysis reuses the SpecStory collection and SWE-chat data, with the exact session overlap with the earlier SpecStory crawl unverified. Examples of missed requirements and successful changes in behavior can coexist. The evidence leaves open which wording or conditions would reliably preserve a particular exception through repository tools and turns. SRC-0022:C02, C18, §§2.1 and 3.1. [Log study and collection method](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=3)

## Where the pattern applies

There is no accepted workflow shown to improve compliance with counter-conventional instructions in general. When the exception reflects a surprising project decision, [Resolve a domain term before coding](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) applies the narrower practice of preserving the approved reason and using an acceptance check that distinguishes the local behavior from the ordinary one. For requirements the application can enforce, Anthropic documents the scope of controls such as hooks and deny rules. These product controls are practitioner guidance, with no measured effect on model compliance. SRC-0002:C11–C12, “Enforce the check with a Stop hook” and “Deterministic and non-deterministic instructions.” [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Original guide](https://code.claude.com/docs/en/best-practices#deterministic-and-non-deterministic-instructions)

## Drive navigation

- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0012--verification.md](../audits/SRC-0012--verification.md) · [Local copy](../audits/SRC-0012--verification.md)
- [audits/SRC-0020--verification.md](../audits/SRC-0020--verification.md) · [Local copy](../audits/SRC-0020--verification.md)
- [audits/SRC-0021--verification.md](../audits/SRC-0021--verification.md) · [Local copy](../audits/SRC-0021--verification.md)
- [audits/SRC-0022--verification.md](../audits/SRC-0022--verification.md) · [Local copy](../audits/SRC-0022--verification.md)
- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0012--negated-instructions.md](../sources/SRC-0012--negated-instructions.md) · [Local copy](../sources/SRC-0012--negated-instructions.md)
- [sources/SRC-0020--repository-context-files.md](../sources/SRC-0020--repository-context-files.md) · [Local copy](../sources/SRC-0020--repository-context-files.md)
- [sources/SRC-0021--instructions-against-learned-conventions.md](../sources/SRC-0021--instructions-against-learned-conventions.md) · [Local copy](../sources/SRC-0021--instructions-against-learned-conventions.md)
- [sources/SRC-0022--observed-developer-agent-misalignment.md](../sources/SRC-0022--observed-developer-agent-misalignment.md) · [Local copy](../sources/SRC-0022--observed-developer-agent-misalignment.md)
