---
artifact_id: SRC-0021
artifact_type: source_verification
reviewer: review_conventions
reviewed: "2026-11-21"
initial_verdict: PASS
verdict: PASS
---

# Independent source review of SRC-0021

**PASS.** All 13 ledger entries are traceable to the conference version or to a reproducible calculation using its printed values. The evidence for OB-04 is strongest in the selected responses where an explicit exception is observable in the prompt and absent from the result. The proposed account of how training produced those errors remains untested. [Source dossier](../sources/SRC-0021--instructions-against-learned-conventions.md) · [ICLR proceedings record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d1a1e8713fcd5626656553c82f7c3b26-Abstract-Conference.html) · [Conference paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf)

## Numbered findings

| Finding | Claim | Evidence independently checked |
|---|---|---|
| 1 | SRC-0021:C01 | Pass. The authors describe both participation in annotation discussions and inspection of SFT datasets. Their eight reversals informed the evaluation design. The reported experiments vary models, tasks and inference settings. They do not isolate the causal contribution of any training convention. [§§1–2.2](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=2) |
| 2 | SRC-0021:C02 | Pass. The pipeline includes seed review, model expansion, filtering, expert calibration and translation. Chinese and English each contribute 506 prompts. Translation and equal within-category counts matter to the independence of language comparisons. The authors report 23 domains. [§§2.2–2.4 and Figs. 2–3](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=4) |
| 3 | SRC-0021:C03 | Pass. The code demonstration constrains comments, variable names and text outside the code block. The prose example restricts both paragraphing and list formats. A score on either composite task alone cannot identify the specific requirement that failed. [Figs. 9–10](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=15) |
| 4 | SRC-0021:C04 | Pass. A change of instructions appears inside a single message. The following figure makes a supplied passage authoritative. The suffix example in the error analysis confirms that the published counterfactual category also contains a different kind of response constraint. [Figs. 13–14](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=18) · [Fig. 17](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=22) |
| 5 | SRC-0021:C05 | Pass. The trip-planning response has segments despite an explicit prohibition. All five factual answers in the Doubao example are ordinarily correct despite the requested limit of one. These are author-selected observations with no frequency denominator. [Fig. 16](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=21) · [Fig. 19](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=24) |
| 6 | SRC-0021:C06 | Pass. The cup example gives enough information to recover 75 grams, which the model identifies before choosing the offered 45 grams. The modified instruction in the next figure produces both the unwanted summary and part of the requested new output. [Figs. 16–17](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=21) |
| 7 | SRC-0021:C07 | Pass. The two percentages describe judge agreement with expert-verified scores before and after tuning. Table 3 confirms category-specific models and template inputs. A visible all-requirements scoring template in the dataset corroborates the dossier's example. Generalization of the reported agreement to other judges or tasks remains open. [§2.5](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=6) · [Table 3](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=14) · [Dataset viewer](https://huggingface.co/datasets/m-a-p/Inverse_IFEval) |
| 8 | SRC-0021:C08 | Pass. I counted 22 entries in each language block and verified both ranges, winners and the four quoted category values. In Figure 5, five of eight Question Correction values fall below 30 and the minimum Counterfactual Answering value is 68.52. The prose's “half” is imprecise, and its subset is narrower than Table 2. [Table 2](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=7) · [Fig. 5](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=9) |
| 9 | SRC-0021:C09 | Pass. In the rendered Figure 6b, the first two models retain their ranks and Qwen3-235B-A22B-Instruct moves from fifth to thirteenth. The adjacent paragraph gives fifteenth. The decline is supported under both readings. Rank comparisons are conditional on the models and exercises in the figure. [§3.2.3 and Fig. 6](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=10) |
| 10 | SRC-0021:C10 | Pass. Both Qwen3-235B overall comparisons and both opposite-direction Question Correction comparisons agree with Table 2. Figure 4b independently shows always-thinking highest in each language, with adaptive mode below direct response in Chinese. This within-model comparison uses the Doubao 0615 version. Table 2 displays 0715. [Table 2](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=7) · [Fig. 4 and §3.2.1](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=8) |
| 11 | SRC-0021:C11 | Pass. Figure 15 shows five models at three sample-pool sizes. The paper selects the highest-scored of the independent outputs. “Approach or surpass” is the authors' characterization of four models at 32 and includes scores below 90. A production retry requires its own selection criterion. [Appendix E.1 and Fig. 15](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=17) |
| 12 | SRC-0021:C12 | Pass. The conclusion favors adaptability as an evaluation target. The ethics and limitations sections describe possible biases from the human and model contributors, two languages, eight instruction types and text-only coverage. The repository fixture and parser checks in the dossier are explicitly practitioner adaptations. [§5 and ethics statement](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=10) · [Appendix A](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=14) |
| 13 | SRC-0021:C13 | Pass. I independently computed both candidate weighted means for every row. The two reported o3-high figures and the stated limits on interpreting their difference are accurate. The calculation below also verifies the GPT-5 and DeepSeek examples. [Fig. 3 and Table 2](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=6) |

## Arithmetic recheck

In printed column order I used category counts of 90, 86, 198, 82, 186, 154, 108 and 108. I multiplied each displayed category score by its count and divided the sum by 1,012. The within-language half counts give identical means. I repeated the calculation after exchanging the third and fourth weights. Both calculations assume equally weighted items. [Fig. 3 and Table 2](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=6)

| English row | Printed overall | Mean with printed weights | Mean with exchanged weights |
|---|---:|---:|---:|
| o3-high | 75.66 | 77.3297 | 75.6585 |
| GPT-5-high | 73.72 | 74.9791 | 73.7170 |
| DeepSeek-V3.1 | 34.42 | 44.4684 | 39.6943 |

Across all 44 model-language rows, 43 exchanged-weight means come within 0.01 points of the printed overall. DeepSeek-V3.1 English is the exception. The exchanged weights reconcile many printed totals. Recovering the authors' actual scoring or column-assignment procedure would require additional evidence. [Table 2](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=7)

## Publication, rights and disposition

The ICLR publisher supplies a 24-page paper. I checked all 20 names in conference PDF order and the different 21-name arXiv v1 record dated September 4, 2025. The search-indexed OpenReview record displays January 26, 2026, June 15, 2026 and CC BY 4.0 as reported. A direct request reached browser verification. The license link on the arXiv v1 record opens the CC0 1.0 deed. The dossier gives original analytical prose, separately attributes the version-specific statements, and makes no claim of verified permission to reproduce the proceedings paper in full. [ICLR title page](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=1) · [OpenReview record](https://openreview.net/forum?id=sTwMHXReLc) · [arXiv v1](https://arxiv.org/abs/2509.04292v1) · [CC0 deed](https://creativecommons.org/publicdomain/zero/1.0/)

**Repairs required:** none. The source discrepancies are preserved in the dossier. Its assignment to OB-04 is bounded to observable response behavior. A causal account of training, a prevalence estimate for deployed coding agents and a claim that a particular prompt repair works would each require different evidence.

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0021--instructions-against-learned-conventions.md](../sources/SRC-0021--instructions-against-learned-conventions.md) · [Local copy](../sources/SRC-0021--instructions-against-learned-conventions.md)
