---
topic_id: OB-09
title: "Hallucination in code"
coverage: partially supported
source_edges:
  - id: SRC-0004
    relationship: DIRECT
    strength: high
    finding: "CloudAPIBench documents fabricated method names, incorrect signatures, and selection of existing operations that do not satisfy the task."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic recommends giving a coding agent an executable check and reviewing the resulting diff against the spec."
  - id: SRC-0017
    relationship: SUPPORTING
    strength: low
    finding: "The prose QA experiments illustrate why reference-token recall and API signature validity measure different parts of correctness."
pattern_ids: [PAT-0002]
publication_status: published
---

# OB-09 — Hallucination in code

“The method looks real, but I can't find it in our installed package.” “The code imports and runs, yet it calls a different operation than the one we need.” The accepted research directly documents these API failure modes. It gives less coverage of grammatical syntax errors across languages or how their causes relate to factual errors in prose.

## What the code evidence establishes

Jain et al. use 622 synthetic Python tasks for AWS and Azure. Their benchmark checks the first generated call against an accepted target signature. In GPT-4o's invalid calls for the low-frequency slice, 53.05% use a nonexistent method, 33.54% misuse the target and 13.41% choose another existing method. The denominator is invalid calls in that slice. The model scored 38.58% valid on low-frequency tasks and 93.66% on high-frequency tasks. The frequency categories are estimated from code in The Stack v2. Those estimates establish an association with usage frequency, with the actual training exposure of each model unknown. SRC-0004:C01–C03, §II-B–C, Fig. 3, Table II and Appendix B–C Table V. [Dossier](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Conference manuscript](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf)

Evidence quality matters when supplying a repair. With guaranteed correct documentation, a signature alone raised StarCoder2-3B's overall valid-call rate from 41.80% to 86.82%. At 50% controlled correct-document inclusion, always retrieving raised GPT-4o from 38.58% to 47.94% on low-frequency calls but dropped it from 93.66% to 54.63% on high-frequency calls. Both results can hold because identifying the correct operation is part of the practical problem. Binding to a matching stub verifies a call form under the benchmark assumptions. Production behavior can also depend on the installed version, configuration, permissions and what the caller needs. SRC-0004:C05–C09, §III-B Figs. 6–7 and §IV-C Table IV. [Conference manuscript](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5)

## How this differs from text evidence

An unfamiliar invocation offers three separable questions. Does the symbol exist in the environment? Do its receiver and arguments match? Does it produce the required behavior? That makes some code claims executable and still leaves domain semantics to verify. For comparison, Zhang et al.'s independent short-answer QA study scores gold-token recall, which can credit an answer containing a correct fact alongside extraneous or conflicting text. The metrics capture different failure modes. This comparison supplies no estimate of relative hallucination rates or of a shared mechanism across prose and code. The CloudAPIBench preprint and conference manuscript are versions of one study. SRC-0017:C02 and C05, §§3.1–3.2 and Tables 2–3. [Dossier](../sources/SRC-0017--verbosity-and-uncertainty.md) · [Published QA study](https://aclanthology.org/2025.uncertainlp-main.14.pdf#page=3)

[Verify an unfamiliar API call](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) traces the dependency version, checks the actual API contract and exercises a minimal expected behavior. Anthropic's separate practitioner guidance supports executable checks and diff review against the spec. It does not replicate the API study or measure the pattern's effect in repositories. SRC-0002:C07–C10. [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run)

## Drive navigation

- [audits/PAT-0002--verification.md](../audits/PAT-0002--verification.md) · [Local copy](../audits/PAT-0002--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0004--verification.md](../audits/SRC-0004--verification.md) · [Local copy](../audits/SRC-0004--verification.md)
- [audits/SRC-0017--verification.md](../audits/SRC-0017--verification.md) · [Local copy](../audits/SRC-0017--verification.md)
- [patterns/PAT-0002--verify-an-unfamiliar-api-call.md](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) · [Local copy](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0004--api-documentation-and-hallucinations.md](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Local copy](../sources/SRC-0004--api-documentation-and-hallucinations.md)
- [sources/SRC-0017--verbosity-and-uncertainty.md](../sources/SRC-0017--verbosity-and-uncertainty.md) · [Local copy](../sources/SRC-0017--verbosity-and-uncertainty.md)
