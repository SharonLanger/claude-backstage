---
artifact_id: SRC-0020
artifact_type: source_verification
reviewer: review_rules
reviewed: "2026-11-21"
initial_verdict: PASS
verdict: PASS
---

# Independent source review of SRC-0020

**PASS.** All ten claims are traceable to the September 2026 revision. The study supports a cost and behavior claim about including repository guidance. It leaves open whether adding another rule makes existing instructions harder to follow. [Source dossier](../sources/SRC-0020--repository-context-files.md) · [Versioned primary text](https://arxiv.org/html/2602.11988v3)

## Numbered findings

| Finding | Claim or item | Independent check and disposition |
|---|---|---|
| 1 | Publication, version, and reuse | Pass. The version record and title page match the five credited authors, affiliations, February 12 initial submission, September 29 revision, and DOI. The February version called the benchmark AGENTbench and described directional performance changes. The dossier uses the v3 name CTXbench and v3 significance tests. Both versions concern the same study. The arXiv record links to CC BY 4.0. The dossier reports results in original prose with attribution and reproduces no source figures. Appendix D gives separate terms for the benchmark assets and tools. [v3 record](https://arxiv.org/abs/2602.11988v3) · [v1 §4.2](https://arxiv.org/html/2602.11988v1#S4.SS2) · [v3 paper and rights notice](https://arxiv.org/html/2602.11988v3) · [License deed](https://creativecommons.org/licenses/by/4.0/) |
| 2 | SRC-0020:C01 | Pass. The 300 SWE-bench Lite tasks span 11 Python repositories. CTXbench retained 138 tasks from 5,694 PRs across 12 repositories. Its tests cover 75% of modified code on average. The dossier correctly identifies the three conditions, four agent/model configurations, single sampled completion, developer-file condition specific to CTXbench, and test-based endpoint. The Appendix C example removes an overly restrictive error-message assertion. [§§3–4.1](https://arxiv.org/pdf/2602.11988v3#page=4) · [Appendix C, Fig. 16](https://arxiv.org/pdf/2602.11988v3#page=19) |
| 3 | SRC-0020:C02 and SRC-0020:C03 | Pass. Figure 3, the rounded mean differences in §4.2, and the four tests in Table 3 support the comparisons. Only the developer-file versus generated-file contrast meets the paper's 0.05 threshold (p=0.038). Comparisons against omission give p=0.87, 0.37, and 0.21. The dossier appropriately leaves equivalence open. The caption and surrounding text identify Table 5's second block with CTXbench despite its inconsistent printed label. [Fig. 3 and Table 3](https://arxiv.org/pdf/2602.11988v3#page=6) · [Appendix A.4](https://arxiv.org/pdf/2602.11988v3#page=15) |
| 4 | SRC-0020:C04 | Pass. Checked the cost magnitudes and example dollar amounts against §4.2 and Table 2, and all six cost and step p-values against Table 6. For generated files on CTXbench, Table 6 prints p=0.00064 for cost, qualifying the blanket threshold in §4.2. The dossier uses the benchmark-specific figure and identifies locally deployed Qwen's price estimate. [§4.1 and Table 2](https://arxiv.org/pdf/2602.11988v3#page=6) · [Table 6](https://arxiv.org/pdf/2602.11988v3#page=16) |
| 5 | SRC-0020:C05 and SRC-0020:C06 | Pass. Verified test-running direction, tool-mention frequencies, reasoning-token examples, and the navigation measure. The authors counted framework tools and used a model to classify shell commands. Figure 4 excludes the 3% of runs without contact with an original patch file. The repeated file search and reading occurred in inspected GPT-5.1 mini traces. These measures leave adherence to other individual rules unscored. [§4.3, Figs. 4–6](https://arxiv.org/pdf/2602.11988v3#page=7) |
| 6 | SRC-0020:C07 and SRC-0020:C08 | Pass. Figure 13 groups CTXbench files by words. Table 7 instead evaluates GPT-5.2 after GPT-5.4 removed one category from generated files. Checked all three reported cost reductions and their p-values. None of the six accuracy tests reaches 0.05. These designs support the dossier's distinction between file length, category content, and individual rule count. [Appendix B, Fig. 13 and Table 7](https://arxiv.org/pdf/2602.11988v3#page=17) |
| 7 | SRC-0020:C09 | Pass. Appendix B removes documentation after generating files and excludes Claude Code. The 2.7-point estimate is the authors' reported mean in this modified setting. The text and figure give no significance test for that estimate. [Appendix B, Fig. 12](https://arxiv.org/pdf/2602.11988v3#page=16) |
| 8 | SRC-0020:C10 and practitioner relevance | Pass. The advice on generated files, repository-specific instructions absent from the README, and evaluation before adoption is attributed to the authors. AP-08 has evidence on the work that instructions induce. The causal rule-count hypothesis remains untested. BP-09 receives indirect support from specific tool use. The proposed compatibility example and its check are clearly catalog adaptations. [§1](https://arxiv.org/pdf/2602.11988v3#page=2) · [§6](https://arxiv.org/pdf/2602.11988v3#page=9) |

## Disposition

No dossier correction was required. This review independently checked the published analyses and their interpretation. It did not rerun benchmark tasks or reclassify raw agent traces. [Reviewed dossier](../sources/SRC-0020--repository-context-files.md)

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0020--repository-context-files.md](../sources/SRC-0020--repository-context-files.md) · [Local copy](../sources/SRC-0020--repository-context-files.md)
