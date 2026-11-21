---
artifact_id: SRC-0008
artifact_type: source_verification
reviewer: review_selfrepair
reviewed: "2026-11-21"
initial_verdict: PASS
verdict: PASS
---

# Independent source review of SRC-0008

**PASS.** All eleven ledger claims have support at the cited locations. The decisive distinction for practitioners is what the evaluator can observe. A complete executable test bed identifies a passing candidate in this experiment. The paper leaves open how reliably a developer can select among patches with incomplete tests. [Reviewed dossier](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Original conference paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)

## Numbered findings

| # | Item | Independent check and disposition |
|---|---|---|
| 1 | Provenance and rights | **Pass.** The ICLR proceedings record and p. 1 confirm the title, five authors in order, affiliations and 2024 conference version. The acknowledgments support the funding disclosures. The authors' repository dates the presentation to May. The v5 record confirms June 16, 2023 and February 2, 2024 for the first and fifth arXiv versions. The v5 HTML header displays CC BY 4.0. The dossier limits that finding to the manuscript, records the conference PDF's redistribution terms as unverified, and uses its own prose without reproducing the paper's text, tables or figures. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/9ddc141bdbf9d1db510cefff56c586ad-Abstract-Conference.html) · [Authors' repository](https://github.com/theoxo/self-repair) · [Version record](https://arxiv.org/abs/2306.09896v5) · [Manuscript license](https://arxiv.org/html/2306.09896v5) |
| 2 | SRC-0008:C01 | **Pass.** Sections 2–3.1 and Figure 2 establish the full executable test set, generation and failure-evidence inputs, and the joint completion for same-model diagnosis and repair. Multiple repair draws from a single initial program are siblings in this design. The account preserves the distinction between evaluator access to tests and model input. |
| 3 | SRC-0008:C02 | **Pass.** Section 3.2 counts generated programs at the maximum tree width. A separate feedback completion adds model work without adding a program to this count. The method terminates when a program passes the tests. Neither the headline budget nor its success measure gives the cost or accuracy of a human selection process. |
| 4 | SRC-0008:C03 | **Pass.** Section 3.2 specifies 50 original draws per specification and 1,000 resampled trees with replacement for each configuration. Section 5 acknowledges the finite-pool risk. Section 4.2's smaller feedback pool is stated separately. |
| 5 | SRC-0008:C04 | **Pass.** Section 4 and footnotes 4–6 verify the model snapshots, fixed temperature and APPS counts of 60 introductory, 180 interview and 60 competition tasks. Appendix H documents proportional sampling from the test set, and Appendix B supplies the two model–dataset combinations omitted from the main heatmaps. Appendix G confirms the distinct prompting arrangement for HumanEval initial generation. |
| 6 | SRC-0008:C05 | **Pass.** I checked the two numerical comparisons against p. 2 and the ratios against Figure 3b. The ten-start configuration has up to 20 programs and gains 3.0 percentage points against fresh-only generation. The two-start configuration has up to 22 and loses 1.6 points against its own fresh-only comparator. Comparing the two ratios directly would mix budgets. |
| 7 | SRC-0008:C06 | **Pass.** Figures 3–5, 12–16 and Appendix C show variation across datasets, models and difficulty. Table 2 defines repair success per sampled repair and shows 28.8% versus 8.6% for GPT-4 on introductory and competition problems. Lower conditional repair success can coexist with a larger relative gain against a weaker fresh baseline. The diversity explanation remains an author hypothesis. |
| 8 | SRC-0008:C07 | **Pass.** Appendix A, Algorithms 1–2, counts generated feedback and program tokens under two stopping policies and plots mean success against mean tokens. Its depth-first schedule can stop before drawing another base program. Figures 6a and 9a have no displayed GPT-3.5/APPS cell above parity. The dossier excludes input tokens, model pricing, elapsed time and reviewer attention from this measure. |
| 9 | SRC-0008:C08 | **Pass.** Section 4.2 and Figure 5 identify distinct tested model pairings on APPS and HumanEval. Fixing one diagnosis and one repair per failed initial generation yields improvements relative to the weaker programming model's curves. Separating the feedback and repair calls also changes the prompting protocol. This comparison supports a diagnostic hypothesis while leaving the equal-price choice of programming model open. |
| 10 | SRC-0008:C09 | **Pass.** I independently summed all 40 rows in Appendix E. The two GPT-4 diagnosis columns give 353 + 313 = 666 passing repairs; the two human columns give 486 + 566 = 1,052. Each condition has 40 × 2 × 25 = 2,000 candidates. This reproduces the 33.30% and 52.60% in Table 1. Task 2923 contributes zero successes in both arms. Appendix D confirms the intentionally easier task mix, 16 participants, and access to two model explanations with their code blocks removed. The dossier retains clustering by task, faulty program and diagnosis. |
| 11 | SRC-0008:C10 | **Pass.** Section 4.3 reports 32 versus seven explanations marked obviously inaccurate out of 80 in each group. Seven human explanations expressed uncertainty and two contained code or pseudocode blocks under the authors' definition. The dossier attributes these judgments to the researchers and treats the role of individual feedback properties as unresolved. |
| 12 | SRC-0008:C11 | **Pass.** Section 5 identifies the self-contained Python task restriction, missing specifications and tests in wider software practice, and human debugging time as an unmeasured cost. A suggested session duration for participants in Appendix D is separate from measured human effort. |
| 13 | Topic mapping, independence and adaptation | **Pass.** BP-08 has direct evidence for sampling and checking multiple candidates, with wall-clock parallel speed and manual selection left open. BP-04 has direct evidence about feedback source for test failures and indirect relevance to a general producer-to-evaluator role switch. OB-06, AP-01 and BP-03 receive bounded support for stochastic draws or fresh alternatives. No fixed restart threshold or psychological sunk-cost effect follows here. The comparison to SRC-0003 distinguishes sequential repairs and a later replacement generation from the sibling repair draws in SRC-0008, and discloses shared HumanEval tasks. [Comparison source](../sources/SRC-0003--debugging-effectiveness-decay.md) |

## Disposition

Initial and final verdict **PASS** on the submitted dossier. No correction was required. This is a source-fidelity review and arithmetic cross-check of the published results. The models were not rerun.

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0008--self-repair-versus-fresh-samples.md](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Local copy](../sources/SRC-0008--self-repair-versus-fresh-samples.md)
