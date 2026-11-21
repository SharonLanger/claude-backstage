---
topic_id: OB-12
title: "Excess verbosity"
coverage: partially supported
source_edges:
  - id: SRC-0017
    relationship: DIRECT
    strength: high
    finding: "Five QA benchmarks showed redundant output despite concise-answer prompts, with a context-dependent association between redundancy, reference-token recall and uncertainty."
  - id: SRC-0018
    relationship: SUPPORTING
    strength: low
    finding: "Moby advises a short contribution summary with longer review evidence available separately."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic advises keeping always-loaded repository guidance short and scoping detailed procedures to when they apply."
pattern_ids: [PAT-0008]
publication_status: published
---

# OB-12 — Excess verbosity

“The reply repeats the task and gives me background, but I still can't tell which setting to change.” “The project notes keep growing, and the one exception we rely on is hard to find.” The brief asks whether models default to verbose outputs, whether excess makes the answer less useful and whether persistent knowledge files degrade. Redundancy is measured in short answers even under concision instructions. The default rate under neutral prompts, effects on code review and the long-term accumulation of redundant guidance remain open.

## What the QA study can tell us

Zhang, Das and Zhang used five QA datasets and 14 models. Their main prompt already requested concision. A detector with access to the reference answer marked some outputs redundant in every tested model–dataset combination. GPT-4o was flagged on 50.40% of NarrativeQA answers, 31.79% of Qasper answers and 15.00% of modified MMLU answers. The detector agreed with manual labels on 93 of 100 checked samples. The study's content categories include repetition, needless enumeration and detail, and ambiguity where a precise answer is expected. They illustrate ways an answer can obscure the needed result. The categories were annotated in selected flagged outputs whose recall was below one. SRC-0017:C01–C04, §§3.1, 4.1–4.2 and 5.1, Fig. 2, Table 1 and Appendix B.1 Table 9. [Dossier](../sources/SRC-0017--verbosity-and-uncertainty.md) · [Published paper](https://aclanthology.org/2025.uncertainlp-main.14/)

Mean gold-token recall was higher for the judged-concise group on average in each dataset. Individual comparisons went both ways, including higher recall for Claude 3.5 Sonnet's verbose NarrativeQA answers. Gold-token recall can credit answers that contain conflicting material. The outcome groups also contain different questions, and the shared-item supplemental analysis compares different models. Figure 4's within-model uncertainty scores generally increase across length bins. This is an aggregate association and supplies no per-output diagnostic. The proposed explanation about less informative first tokens comes from selected examples. Truncating already verbose Llama-3-8B Qasper responses to their first four tokens reduced recall from 44.93% to 43.13% in Appendix B.4's comparison. Editing for meaning would require a different test. SRC-0017:C05–C09, C13, §5.2 Tables 2–3, §5.3 Fig. 4, Appendix B.4 p. 172 and Appendix C.4. [Tables and figures](https://aclanthology.org/2025.uncertainlp-main.14.pdf#page=6) · [Truncation experiment](https://aclanthology.org/2025.uncertainlp-main.14.pdf#page=13)

## Where the evidence transfers

Moby's contribution policy independently asks for a short explanation up front and room for supporting details. Anthropic's product guide addresses another artifact, the always-loaded repository notes. It recommends keeping them focused on information the agent needs and loading narrower procedures when they are relevant. These recommendations apply to finding the material a reviewer or agent needs. Neither independently replicates the QA results or follows knowledge files long enough to estimate document rot. Retaining precise compatibility constraints, rationale and verification evidence can justify more detail. SRC-0018:C02–C03, policy lines 18–44. SRC-0002:C13–C14, “Keep CLAUDE.md short” and scoped rules. [Moby dossier](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Policy](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L18-L44) · [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Guide](https://code.claude.com/docs/en/best-practices#keep-claudemd-short)

[Take ownership before submitting AI-assisted code](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) applies the policy to a contribution summary and its verification evidence. The catalog has no dedicated pattern for shortening general model answers or maintaining persistent knowledge files against document rot. A catalog adaptation for a bounded answer is to ask for the result and what verifies it, then inspect whether both survived any edit. Its usefulness depends on preserving the scope and evidence the decision requires.

## Drive navigation

- [audits/PAT-0008--verification.md](../audits/PAT-0008--verification.md) · [Local copy](../audits/PAT-0008--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0017--verification.md](../audits/SRC-0017--verification.md) · [Local copy](../audits/SRC-0017--verification.md)
- [audits/SRC-0018--verification.md](../audits/SRC-0018--verification.md) · [Local copy](../audits/SRC-0018--verification.md)
- [patterns/PAT-0008--take-ownership-before-submitting-ai-code.md](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) · [Local copy](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0017--verbosity-and-uncertainty.md](../sources/SRC-0017--verbosity-and-uncertainty.md) · [Local copy](../sources/SRC-0017--verbosity-and-uncertainty.md)
- [sources/SRC-0018--accountability-for-ai-assisted-contributions.md](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Local copy](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md)
