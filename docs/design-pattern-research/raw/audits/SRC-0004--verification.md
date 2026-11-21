---
audit_id: SRC-0004-verification
source_id: SRC-0004
role: independent_source_reviewer
reviewed: 2026-11-21
verdict: PASS
initial_verdict: PASS WITH CHANGES
recheck: completed
---

# Independent verification of SRC-0004

**Initial disposition — PASS WITH CHANGES.** All nine evidence propositions trace to the study. The initial dossier attached the preprint submission date to an IEEE publication in its structured record and listed the expected audit filename as plain text. The reviewer requested that the owner separate the dates and link the audit. [Source dossier](../sources/SRC-0004--api-documentation-and-hallucinations.md)

**Final disposition — PASS after independent recheck, November 21, 2026.** The corrected record distinguishes the 2025 proceedings year from the July 2024 preprint submission, leaves the exact proceedings date unverified, and links to this audit. I opened the revised dossier and checked those fields and the reciprocal relative paths. There are no remaining source-review blockers.

## Original material independently opened

1. Amazon Science lists the five authors, publication year 2025 and the ICSE venue. The title page and conference program give Robert Kwiatkowski's full first name, shortened to Rob on the Amazon page. The program records a presentation on May 1, 2025. The DOI resolves to IEEE Xplore document 11121691, where a JavaScript check prevented reading the IEEE-hosted text. The conference-text checks here used the 12-page manuscript linked directly by Amazon. [Publication listing](https://www.amazon.science/publications/on-mitigating-code-llm-hallucinations-with-api-documentation) · [Program](https://conf.researchr.org/details/icse-2025/icse-2025-software-engineering-in-practice/33/On-Mitigating-Code-LLM-Hallucinations-with-API-Documentation) · [DOI](https://doi.org/10.1109/ICSE-SEIP66354.2025.00027) · [Amazon manuscript][pdf]
2. The arXiv submission history gives July 13, 2024 for v1. The preprint offers explicit limitations and ethics sections, while the conference manuscript supplies a downstream code experiment absent from v1. Matching core results and authorship make these manifestations of one study. [Submission history](https://arxiv.org/abs/2407.09726) · [Preprint §§2.1, 7–8][v1] · [Conference manuscript §II-A][p2]

## Claim findings

| Finding and claim | Independent verification and limits | Disposition |
|---|---|---|
| 1 · SRC-0004:C01 | §II-B–C and preprint Appendix A confirm 622 short Python tasks for AWS and Azure, first-call greedy evaluation, and the accepted target signature check. Some prompts admit multiple targets, and the same API may appear in up to three prompts. Binding establishes the tested call shape. The authors did not run completed applications to score behavior. [Benchmark and scoring][s2] | PASS |
| 2 · SRC-0004:C02 | The benchmark bins in §2.2 use 0–10, 11–100, and 101+ occurrences. Table 1's 12 rows support the reported frequency ordering. The GPT-4o snapshot's three values and HumanEval comparison match the table. These counts are a proxy based on The Stack v2. The study did not establish counts in GPT-4o's training data. [Benchmark and Table 1][s2] | PASS |
| 3 · SRC-0004:C03 | Appendix A.6, Table 4 puts the GPT-4o failure rate at 61.42% of rare-call prompts. The shares among failures sum to 100% and match the dossier. Wrong selection and wrong arguments together account for 46.95% of failures. Figure 14(a) confirms the two similar method names and names CodeGemma-7B as the model. [Preprint Appendix A][ap] | PASS |
| 4 · SRC-0004:C04 | I inspected Table I visually and checked §II-A against preprint §2.1. The 171 programs use AWS. Each pair of continuations is compared with one original suffix. All three score differences favor the original name. The 15B values are 43.85 and 39.67. The dossier preserves the table's anomalous label for its smallest row and does not use that row as evidence for a named model size. [Conference experiment][p2] · [Preprint §2.1][s2] | PASS |
| 5 · SRC-0004:C05 | The numeric entries in Fig. 6 match across the conference page and preprint. With the right document guaranteed, StarCoder2-3B scored 86.82% for the signature and 87.14% with the description added. The longer condition scored 88.75%, with about 7.25 times the added tokens of description plus signature. The 5,000-character cap and the absence of a human arm are retained. [Conference Fig. 6][p5] · [Preprint §3.2 and Appendix B][v1] | PASS |
| 6 · SRC-0004:C06 | The authors deliberately controlled whether the target was retrieved. With one document and 50% target inclusion, the direction reversed across rare and common GPT-4o calls. Table IV gives 47.94% and 54.63% respectively for always-on retrieval. The paper itself gives the common-call drop as 39.02 points. Fig. 7 and §III-B support the separate precision and document-count ablations. [Conference Table IV][p7] · [Conference §III-B][p5] | PASS |
| 7 · SRC-0004:C07 | Table III confirms both changes for StarCoder2-3B when enabling the index check. Name lookup cannot resolve a real method with the wrong purpose or arguments. Conditioning retrieval on a missing name explains why some erroneous calls bypass the gate. [Conference §IV-A and Table III][p5] · [Preprint §4.1][s4] | PASS |
| 8 · SRC-0004:C08 | Checked the disjunction, the minimum over name-token probabilities, the fixed 0.8 threshold and the GPT-4o trigger frequencies and scores in Table IV. Overall validity rises 8.20 points. Selective retrieval leads on overall validity for all five tested variants. The CodeGemma-7B rare slice and DeepSeekCoder-33B common slice preserve concrete exceptions. The algorithm did not measure self-reported certainty. [Conference Table IV][p7] · [Preprint §4][s4] | PASS |
| 9 · SRC-0004:C09 | Preprint §§7–8 explicitly discuss the language and prompt restrictions, approximation of code frequency, and added latency. Human review and sandbox execution appear as author guidance. The accepted evidence does not quantify either practice's effect. [Preprint §§7–8][s7] | PASS |

## Application, independence, and rights

The type and topic labels fit the evidence. OB-09 is a direct match for the three observed failure modes. AP-02 and BP-06 are supporting connections. A human consulting their installed SDK's signature, validating return values or testing dependent code is a catalog adaptation with no measured developer-workflow effect here. The strongest result for including a signature assumes the document actually matches the task.

The dossier summarizes the study in independently worded prose. Method names, numeric facts, bibliographic metadata and a few necessary API identifiers are attributed. No paper page, figure or extended expressive passage is reproduced in the dossier or audit. The nonexclusive license linked by arXiv grants distribution to arXiv. I found no broader grant in the material inspected. The original authors' AWS ties and the experimental limits are disclosed. I did not independently run the experiments. [arXiv record](https://arxiv.org/abs/2407.09726) · [License](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html)

[pdf]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf
[p2]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=2
[p5]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5
[p7]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=7
[v1]: https://arxiv.org/html/2407.09726v1
[s2]: https://arxiv.org/html/2407.09726v1#S2
[s4]: https://arxiv.org/html/2407.09726v1#S4
[s7]: https://arxiv.org/html/2407.09726v1#S7
[ap]: https://arxiv.org/html/2407.09726v1#A1

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0004--api-documentation-and-hallucinations.md](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Local copy](../sources/SRC-0004--api-documentation-and-hallucinations.md)
