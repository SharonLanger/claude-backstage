---
source_id: SRC-0004
status: accepted
original_title: "On Mitigating Code LLM Hallucinations with API Documentation"
authors: ["Nihal Jain", "Robert Kwiatkowski", "Baishakhi Ray", "Murali Krishna Ramanathan", "Varun Kumar"]
publisher: "IEEE, 2025 IEEE/ACM International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)"
source_type: empirical_paper
published: unknown
publication_year: 2025
preprint_submitted: 2024-07-13
updated: unknown
accessed: 2026-11-21
original_url: "https://www.amazon.science/publications/on-mitigating-code-llm-hallucinations-with-api-documentation"
source_version: "First public preprint arXiv:2407.09726v1 (2024-07-13). ICSE-SEIP proceedings 2025, DOI 10.1109/ICSE-SEIP66354.2025.00027. Conference manuscript and preprint inspected."
full_text_reuse: not_authorized_or_unverified
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [AP-02, BP-06, BP-07, OB-09, OB-10]
related_patterns: [PAT-0002]
review: PASS
delivery: published
---

# On Mitigating Code LLM Hallucinations with API Documentation

## Provenance and scope read

Jain, Nihal, Robert Kwiatkowski, Baishakhi Ray, Murali Krishna Ramanathan, and Varun Kumar. *On Mitigating Code LLM Hallucinations with API Documentation*. 2025 IEEE/ACM 47th International Conference on Software Engineering, Software Engineering in Practice (ICSE-SEIP), pp. 237–248. DOI `10.1109/ICSE-SEIP66354.2025.00027`. The conference program dates the presentation to May 1, 2025. The frontmatter date is the first public preprint submission, July 13, 2024. arXiv lists v1 as its sole version. The Amazon Science entry is dated 2025 and lists Robert as Rob. The Amazon-hosted PDF and conference program use Robert. [Amazon Science publication][landing] · [ICSE 2025 program][program] · [Proceedings DOI][doi] · [arXiv record][arxiv]

The free 12-page Amazon-hosted conference manuscript and free arXiv v1 full text were inspected for their introduction, benchmark and evaluation methods, documentation experiments, selective retrieval, conclusion, relevant appendices and author-stated limitations. The DOI redirects to IEEE Xplore document `11121691`, whose page returned a JavaScript verification wall during this read. The PDF below is the Amazon-hosted manuscript. Its numbering differs from the preprint and it adds a downstream completion experiment in §II-A, Table I. The primary quantitative comparison appears in PDF Table IV and arXiv Table 3. These are versions of the same authors' study. Page locators below are one-based Amazon PDF viewer pages. The experiments were read and compared across versions without rerunning the benchmark. [Amazon manuscript][pdf] · [Version-pinned preprint][v1]

This is primary empirical research by AWS-affiliated authors evaluating AWS and Azure SDKs. The manuscript lists Kwiatkowski's research as completed while at Amazon. The affiliation is relevant to the scope of the benchmark and its focus on public cloud SDKs. [Amazon manuscript, title page][pdf]

## Reader's orientation

The paper asks why a code model can produce a plausible SDK call that fails a basic check, and whether documentation supplied during generation improves the next attempt. It identifies three problems a reviewer can tell apart. The name can be invented, the operation can exist but solve a different task, or the correct operation can be invoked with invalid arguments. In this study, these failures were much more common for APIs rarely seen in the public Python corpus the authors sampled. [Amazon manuscript, pp. 3–4 and 9–10][p3] · [arXiv v1, §§2.2–2.3 and App. A.5–A.6][v1]

The document intervention depends on both its contents and how reliably it reaches the correct operation. The reliable target-document ablation favored a concise signature as evidence for call syntax. When the retrieval system supplied one document drawn with a controlled 50% target-document inclusion rate, retrieving every time helped the rare calls and harmed the common ones. An automated trigger recovered most of that high-frequency loss while improving average validity for all five model variants tested in that comparison. The transfer to a developer selecting and checking version-matched documentation is a practical adaptation. The experiments measure model completions and benchmark validity, with no developer workflow arm. [Amazon manuscript, §III-B and §IV-C][p5] · [arXiv v1, §§3.2, 4.3 and 7][v1]

## Detailed analytical reading

### What CloudAPIBench validates

CloudAPIBench comprises 622 synthetic Python completion tasks for AWS and Azure APIs. A prompt supplies imports, variable setup and an intent comment before the call. To create the benchmark, the authors obtained official boto3 documentation and derived signatures from stubs for boto3 1.34.108. Azure API source docstrings and definitions supplied documentation and signatures for the Azure examples. The authors used Claude 3 Sonnet to turn API descriptions into developer-style comments, inspected a subset and corrected noticed issues. A target API can appear under up to three prompts. Where inspection found several suitable APIs for a task, the authors could enumerate multiple targets. [Amazon manuscript, §II-B, App. A][p3] · [arXiv v1, §§2.2, A.2–A.3][v1]

The evaluation takes the first generated call from greedy decoding. Its syntax must bind to a stub for an acceptable target operation. The stub records the documented argument slots and which are required. The combination can catch a missing parameter or wrong keyword alongside an invented method or wrong target. The gate ends at the call boundary. Correct parameter values, response fields, error behavior, side effects and the rest of the program require their own evidence. In particular, a typed or importable method can still be the wrong operation for the requested outcome. [Amazon manuscript, §II-B–C, Fig. 3 and App. B][p3] · [arXiv v1, §§2.2–2.3 and A.3–A.5][v1]

### What frequency means and how the failures differ

The authors counted same-named calls and function definitions in provider-relevant portions of The Stack v2, using import and file-path signals to identify likely AWS or Azure files. They sampled APIs across frequency and required-argument complexity. The benchmark bins are low (0–10 occurrences), medium (11–100) and high (101 or more), as defined in §II-B/§2.2. These heuristic counts estimate public-code exposure. Counts in a particular closed model's training data, dates when APIs shipped, and a developer's own familiarity are different quantities. New or project-specific APIs may merit the same scrutiny in practice, with no corpus-bin assignment implied. [Amazon manuscript, §II-B and App. A][p3] · [arXiv v1, §§2.2, 7 and A.2][v1]

All 12 model configurations in the baseline table score highest on the high-frequency slice and lowest on the low-frequency slice. The evaluated GPT-4o snapshot (`gpt-4o-2024-05-13`) achieves 93.66% valid on high-frequency calls, 78.67% on medium, and 38.58% on low. The same table reports 90.20% HumanEval pass@1 from a different benchmark. The contrast shows why general coding scores alone tell a developer little about the reliability of a particular unfamiliar SDK method in this setup. The study shows an association across sampled APIs. It does not identify how many training examples would make a particular API reliable. [Amazon manuscript, §II-C, Table II][p4] · [arXiv v1, §2.3, Table 1][v1]

For the evaluated GPT-4o snapshot, 61.42% of low-frequency calls fail the benchmark check. **Among those invalid calls**, 53.05% use a nonexistent operation, 33.54% use the target operation incorrectly, and 13.41% use an existing operation that misses the task. The last two categories total 46.95% of this failure subset. A reviewer who only checks that a model-suggested method exists misses both kinds. One arXiv example shows CodeGemma-7B choosing `get_application_health` for a task targeting `get_deployed_application_health`. The listed distinction is the scope of the operation, even though the two names resemble one another. [Amazon manuscript, App. B–C and Table V][p10] · [arXiv v1, App. A.5–A.6, Fig. 14(a) and Table 4][v1]

### What happens to code that follows an invented call

In the conference manuscript's additional experiment, the authors took 171 Python programs that used AWS APIs from The Stack v2 and prompted models with each program cut immediately after the API name. They compared continuations prompted with the actual name to continuations prompted with an invented substitute, using edit similarity against the original suffix. For StarCoder2-15B, similarity was 43.85% with the actual name and 39.67% with the invented one. All three rows move in the same direction. That perturbation tests whether subsequent generation changes once an invented name is already in the prompt. Edit similarity measures resemblance to one original suffix. Behavioral equivalence, compilation success and production failure rates need other measures. Table I labels its smallest row “StarCoder2-2B” while §II-C lists a 3B smallest StarCoder2 benchmark model. The 15B row has a consistent model label. [Amazon manuscript, §II-A, Table I, p. 2][p2] · [§II-C, p. 3][p3]

### What the model was shown and what changed

The authors call their method Documentation Augmented Generation (DAG). The first draft gives the system search terms. It selects API docs with a BM25-based setup that can deliberately vary how often the correct target document appears. Selected material is prepended to the original prompt as a Python docstring and the model generates a new answer. That design lets the study compare help from relevant material and distraction from another official document. For example, a valid description of a neighboring API can still be irrelevant to the intended call. A controlled target-inclusion rate measures the authors' experimental condition. Real-world top result quality will depend on the question, index and retrieval process. [Amazon manuscript, §III-A, Fig. 4–5][p4] · [arXiv v1, §3.1][v1]

The document-content experiment uses StarCoder2-3B and one guaranteed-correct target document. It compares five ways of representing that source. Valid calls across all tasks were 41.80% without documentation, 52.73% with the operation name, 53.22% with name and short description, 86.82% with the signature, 87.14% with the description plus signature, and 88.75% with the longer documentation condition. The signature contains the operation name and its required and optional arguments. The authors used description plus signature in later tests, averaging 94.55 extra tokens on this model's tokenizer, compared with 685.24 for the longer-document condition. The longer condition could itself be truncated at 5,000 characters. It delivered the highest score in this comparison and may contain semantic details the signature omits. The evidence favors including the relevant signature for this syntax task and has no universal optimum for snippet length. [Amazon manuscript, §III-B, Fig. 6 and App. D][p5] · [arXiv v1, §3.2 and App. B.1][v1]

The precision experiment on StarCoder2-3B changes how often the right document appears while returning one document. At 50% target inclusion, high-frequency validity falls from 84.39% to 67.32%. The authors report that matching that model's high-frequency baseline requires more than 80% precision in the one-document ablation. Low-frequency results benefit from a much lower starting baseline. In the separate 50%-precision document-count ablation, the high-frequency drop from giving one document partially recovers when more are included. The results make the usefulness of the evidence and the starting strength of the model more informative than a general rule about sending more or less text. [Amazon manuscript, §III-B, Fig. 7, pp. 5–6][p5] · [arXiv v1, §3.2][v1]

### Selective retrieval does something narrower than code review

An index-only check retrieved documentation when the draft method name failed to resolve. It could accept a known but wrong operation and a known operation with invalid arguments. With StarCoder2-3B and one document at 50% precision, adding the index gate to unconditional retrieval changed high-frequency validity from 67.32% to 85.37% and low-frequency validity from 46.07% to 35.96%. The low-frequency result still exceeded the 11.61% no-retrieval baseline. The tradeoff follows directly from allowing a real operation name to bypass retrieval even when its role or call shape is wrong. [Amazon manuscript, §IV-A, Table III, pp. 5–6][p5] · [arXiv v1, §4.1, Table 2][v1]

The authors also measured a specific model signal, the minimum next-token probability among the sub-tokens forming the operation name. DAG++ uses an OR rule. It retrieves if the name is missing from the index or that confidence falls below 0.8 in the combined experiment. The authors report a relationship between this score and successful calls on their benchmark. The value is an experiment setting chosen after a StarCoder2-3B threshold study, and it depends on access to the appropriate model probabilities. An assistant's confident wording is a different signal with no reported calibration here. The practitioner-facing contribution is the idea of using independent evidence to identify a questionable call. [Amazon manuscript, §IV-B–C, Figs. 8–9 and Table IV][p6] · [arXiv v1, §§4.2–4.3][v1]

**GPT-4o benchmark comparison.** The automated conditions used the same one-document retrieval setup with 50% controlled target inclusion. Percentages in the validity columns are valid calls in the indicated slice. The overall rate is across benchmark tasks. [Amazon manuscript, §IV-C, Table IV][p7] · [arXiv v1, §4.3, Table 3][v1]

| Method | High-frequency validity | Medium-frequency validity | Low-frequency validity | Overall validity |
|---|---:|---:|---:|---:|
| No retrieval | 93.66% | 78.67% | 38.58% | 66.40% |
| Always retrieve (DAG) | 54.63% | 53.33% | 47.94% | 51.45% |
| Selective retrieval (DAG++) | 94.15% | 82.00% | 55.43% | 74.60% |

The paper reports the high-frequency drop with always-on retrieval as 39.02 percentage points. Subtracting the displayed rounded rates yields 39.03. The selective method retrieved for 3.41% of high-frequency, 9.33% of medium-frequency and 50.56% of low-frequency GPT-4o tasks. It gained 8.20 percentage points overall against no retrieval. Across the five model variants, selective retrieval gave the highest aggregate result each time. Individual slices still varied. For example, high-frequency DeepSeekCoder-33B fell from 90.24% without retrieval to 86.83% selectively, and low-frequency CodeGemma-7B fell from 46.44% under always-on retrieval to 43.07% selectively. Residual errors remained substantial even for GPT-4o's selective rare-API result. [Amazon manuscript, §IV-C, Table IV][p7] · [arXiv v1, §4.3, Table 3][v1]

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support / caveat |
|---|---|---|---|---|
| SRC-0004:C01 | CloudAPIBench tests 622 synthetic Python tasks for AWS and Azure. It checks the first generated call against an accepted target signature through stub binding. | Benchmark method | [PDF, §II-B–C, Fig. 3, App. A][p3] · [arXiv v1, §§2.2–2.3 and A.2–A.3][v1] | Direct, high within the benchmark. Binding checks invocation syntax and target identity. Semantic behavior needs additional evidence. |
| SRC-0004:C02 | Low, medium and high correspond to heuristic counts of 0–10, 11–100 and ≥101 in provider-related source from The Stack v2. All 12 model configurations score lower on the rarest slice than on the commonest. Tested GPT-4o scores 93.66%, 78.67%, and 38.58% from high to low. | Method and empirical result | [PDF, §II-B–C, Table II and App. A][p4] · [arXiv v1, §§2.2–2.3, Table 1 and A.2][v1] | Direct, high for this benchmark. Counts approximate public exposure and the design establishes association. |
| SRC-0004:C03 | For GPT-4o's invalid low-frequency calls, 53.05% use a nonexistent method, 33.54% misuse the target, and 13.41% choose the wrong existing method. | Empirical failure analysis | [PDF, App. B–C and Table V][p10] · [arXiv v1, App. A.5–A.6, Fig. 14 and Table 4][v1] | Direct, high in this slice. Use the invalid-call denominator for the breakdown. |
| SRC-0004:C04 | In 171 AWS-using Python programs, substituting a fabricated name in the prefix lowered downstream edit similarity in all three reported model rows. StarCoder2-15B moved from 43.85% to 39.67%. | Empirical result | [PDF, §II-A, Table I][p2] | Direct, moderate. Specific perturbation and text-similarity outcome. Available only in the conference manuscript among the versions inspected. |
| SRC-0004:C05 | With one guaranteed-correct document and StarCoder2-3B, a signature raised overall validity from 41.80% to 86.82%. Description plus signature reached 87.14%; longer documentation reached 88.75% and used over seven times as many added tokens as description plus signature. | Empirical ablation | [PDF, §III-B, Fig. 6 and App. D][p5] · [arXiv v1, §3.2, Fig. 6 and B.1][v1] | Direct, high within the oracle condition. Supporting for a human supplying a verified signature. |
| SRC-0004:C06 | At 50% controlled correct-document inclusion with one retrieval, unconditional DAG moved GPT-4o from 38.58% to 47.94% on low-frequency calls and from 93.66% to 54.63% on high-frequency calls. Varying precision on StarCoder2-3B also showed asymmetric effects. | Empirical result and ablation | [PDF, §III-B, Fig. 7 and §IV-C, Table IV][p7] · [arXiv v1, §§3.2 and 4.3, Fig. 7 and Table 3][v1] | Direct, high within the controlled-retrieval setup. A caution about injecting potentially irrelevant material, including official docs for the wrong operation. |
| SRC-0004:C07 | An index-only trigger skipped existing names, including wrong existing operations and malformed calls to the right one. For StarCoder2-3B, the gate raised high-frequency validity from 67.32% to 85.37% and lowered low-frequency validity from 46.07% to 35.96% relative to unconditional DAG. | Method and empirical result | [PDF, §IV-A and Table III][p5] · [arXiv v1, §4.1, Table 2][v1] | Direct, high within the ablation. Supports distinguishing lookup from checking the intended behavior and arguments. |
| SRC-0004:C08 | DAG++ triggers for a missing index name or a minimum API-name sub-token probability below the fixed 0.8 threshold. GPT-4o selective retrieval is triggered on 3.41% of high-frequency and 50.56% of low-frequency tasks and scores 94.15% and 55.43% valid in those slices, with 74.60% overall versus 66.40% without retrieval. | Method and empirical result | [PDF, §IV-B–C, Figs. 8–9 and Table IV][p7] · [arXiv v1, §§4.2–4.3, Table 3][v1] | Direct, high within the benchmark. Supporting for selective retrieval as an idea; the threshold and gain cannot be assumed in a human workflow. |
| SRC-0004:C09 | The authors limit their scope to short synthetic Python prompts, acknowledge heuristic frequency counts and note that iterative generation adds overhead. They advise human review and sandbox execution for generated code in real applications. | Author limitations and guidance | [arXiv v1, §§7–8][v1] · [PDF, §VI, future work][p8] | Direct for limitations and stated advice. The advice is distinct from experimental outcomes. |

## Extractable practitioner insights

### Start verification at the generated operation

If the assistant suggests a method unfamiliar to the engineer, writes a surprisingly named argument, or switches between similar operations after a failure, check three things before asking it to extend the patch. Verify that the operation belongs to the installed package and version, that its documented behavior matches the intended effect, and that the call matches its argument contract. If downstream code already handles the response, check those assumptions against the same reference. This is a catalog adaptation inferred from the study's three failure classes and the conference-only continuation experiment. The paper did not compare individual review checklists. [SRC-0004:C01, C03–C04][p2] · [Failure classes and example][v1]

For example, when a patch is intended to read health information about a specific deployment, an API documented for an entire application might exist and accept the arguments supplied while returning the wrong scope. Check the description against the requested target, then verify the arguments against the right operation. If the rest of the patch consumes response fields the old operation supplied, confirm the replacement response contract before retaining that code. This illustrative adaptation uses the real similar-name distinction from Fig. 14(a). The follow-on review steps are original engineering guidance. [arXiv v1, App. A.5, Fig. 14(a)][v1] · [Amazon manuscript, §II-A, Table I][p2]

### Choose documentation against the dependency and the question

A practical adaptation is to look up the exact API using the repository's dependency version, confirm the correct language, SDK and service, then give the assistant the relevant operation description and signature along with the smallest set of constraints or response details needed for the task. Where official docs and the installed interface differ, check a version-matched reference, installed types or source and preserve the discrepancy until resolved. A test exercising the behavior can complement those static checks when the response, exceptions, values or side effects matter. The closest direct result concerns syntax given assured relevance. Version matching, selective manual lookup, response checking and testing extend beyond the intervention and measured outcome. [SRC-0004:C01, C05–C08][p5] · [arXiv v1, §§3.1–3.2, 4 and 7–8][v1]

Common operations can still be high-impact or version-sensitive. A familiar call that affects deletion, money or an external system warrants verification based on consequence even if a model often gets its syntax right. The observed degradation under deliberately imperfect automatic retrieval is a reason to check the usefulness of extra context. It does not show that consultation of correct official docs harms common API calls. There is no reason to estimate an API's public-code frequency before consulting its documentation or checking its behavior. [SRC-0004:C02, C06 and C08][p7] · [arXiv v1, §§2.2, 3.2 and 7][v1]

### Topic and pattern relationships

- **OB-09, Hallucination in code.** Direct evidence for invented operations, wrong existing operations and invalid call shape in a specific Python cloud SDK task. See SRC-0004:C01–C04 and C06–C08. [Benchmark and failure analysis][p3]
- **AP-02, Flying blind / vibe coding.** Supporting evidence for the value of an external check at an API boundary and for reviewing dependent code after correcting it. No studied human workflow or adoption outcome. See SRC-0004:C03–C04 and C09. [Continuation experiment][p2] · [Authors' ethics statement][v1]
- **BP-06, Context management discipline.** Supporting evidence for verifying the relevance of material inserted into a short prompt. Reset policies, long coding sessions, and repository agent context budgets fall outside these experiments. See SRC-0004:C05–C06 and C09. [Documentation ablations][p5] · [Preprint limitations][v1]
- **Candidate pattern idea.** Verify generated SDK calls against a version-matched reference before extending dependent code. See the linked pattern and independent verification below.

## Related work, conflicts, and limitations

- The paper cites prior research on code hallucination categories and documentation retrieval. The evidence ledger uses this study's own measurements and design. The Amazon-hosted PDF, arXiv version and repeated abstract corroborate version provenance for a single publication. [Amazon manuscript, §V][p8] · [arXiv v1, §5][v1]
- The benchmark tests one Python call from a short intent prompt against predefined target signatures. Its overall rate uses the study's task mix. It does not estimate production prevalence or failure rates for multi-call workflows, private libraries, newer models, other languages, or longer coding sessions. Appendix A also allows multiple prompts for an API, making the number of tasks different from a count of independently sampled APIs. [Amazon manuscript, §II-B and App. A][p3] · [arXiv v1, §§2.2, 7 and A.2–A.3][v1]
- The study compares generating with automatic documents to generating without them. The document in the oracle ablation is guaranteed to be the target. The imperfect-retrieval comparison has a controlled mix of correct and incorrect documents. Choosing a precise document manually could reduce that specific mismatch, but no human-selection group measured its error rate, effort, or effect on quality. The reported scores also stop short of proving that asking the model for a citation can substitute for opening it. [Amazon manuscript, §§III–IV][p4] · [arXiv v1, §§3.1–3.2, 4 and 7][v1]
- The preprint frames overhead from repeated generation as a limit in latency-sensitive settings. It also names long-context tests as future work. The paper's speculation about models memorizing syntax more efficiently is an author interpretation of the observed trigger rates, with no direct access to all training histories. [arXiv v1, §§4.3, 6–7][v1]

## Retrieval hints

User symptoms include “The method the assistant gave me does not exist,” “This parameter is rejected by my installed SDK,” “This call works but retrieves the wrong object,” “It also made up the shape of the response,” and “The code got worse when I pasted the docs for a similar operation.” Families and tags include API hallucination, dependency/version mismatch, checking method identity and purpose, validating a signature, externally verified documentation, and review of dependent code.

## Original article access and copyright/permission record

The original [Amazon Science publication][landing] links to the freely readable [conference manuscript PDF][pdf]. The [arXiv record][arxiv] links to the [version-pinned HTML][v1] and its license. The arXiv perpetual non-exclusive distribution license grants distribution rights to arXiv. It supplies no public full-text redistribution grant for this dossier. Reuse permission for the Amazon-hosted copy was unverified. This dossier uses original analysis, bibliographic metadata, factual measurements and identifiers, with no wholesale source text. [arXiv license terms][license]

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0004--verification.md)

[landing]: https://www.amazon.science/publications/on-mitigating-code-llm-hallucinations-with-api-documentation
[program]: https://conf.researchr.org/details/icse-2025/icse-2025-software-engineering-in-practice/33/On-Mitigating-Code-LLM-Hallucinations-with-API-Documentation
[doi]: https://doi.org/10.1109/ICSE-SEIP66354.2025.00027
[arxiv]: https://arxiv.org/abs/2407.09726
[v1]: https://arxiv.org/html/2407.09726v1
[license]: https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html
[pdf]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf
[p2]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=2
[p3]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=3
[p4]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=4
[p5]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5
[p6]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=6
[p7]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=7
[p8]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=8
[p10]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=10

## Drive navigation

- [audits/PAT-0002--verification.md](../audits/PAT-0002--verification.md) · [Local copy](../audits/PAT-0002--verification.md)
- [audits/SRC-0004--verification.md](../audits/SRC-0004--verification.md) · [Local copy](../audits/SRC-0004--verification.md)
- [patterns/PAT-0002--verify-an-unfamiliar-api-call.md](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) · [Local copy](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/AP-02--flying-blind-vibe-coding.md](../topics/AP-02--flying-blind-vibe-coding.md) · [Local copy](../topics/AP-02--flying-blind-vibe-coding.md)
- [topics/BP-06--context-management-discipline.md](../topics/BP-06--context-management-discipline.md) · [Local copy](../topics/BP-06--context-management-discipline.md)
- [topics/BP-07--semantic-anchors.md](../topics/BP-07--semantic-anchors.md) · [Local copy](../topics/BP-07--semantic-anchors.md)
- [topics/OB-09--hallucination-in-code.md](../topics/OB-09--hallucination-in-code.md) · [Local copy](../topics/OB-09--hallucination-in-code.md)
- [topics/OB-10--limited-attention-focus.md](../topics/OB-10--limited-attention-focus.md) · [Local copy](../topics/OB-10--limited-attention-focus.md)
