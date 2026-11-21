---
source_id: SRC-0011
reviewed: 2026-11-21
reviewer: independent source reviewer
initial_verdict: PASS WITH CHANGES
verdict: PASS
---

# SRC-0011 verification

The early trial measured the time contributors spent delivering issues with or without permission to use AI. The screen-recording analysis answers a narrower question about observable activities. METR’s later experiment changed the sample and exposed new problems measuring time. I checked all 13 claims against these publications, including the outcome instructions, survey and recording protocol in the v2 PDF. [Dossier](../sources/SRC-0011--review-work-and-developer-time.md) · [Original v2 paper](https://arxiv.org/html/2507.09089v2) · [METR follow-up](https://metr.org/blog/2026-02-24-uplift-update/)

## Findings

| Finding | Claim | Evidence checked and disposition |
|---|---|---|
| 1 | SRC-0011:C01 | Confirmed 16 experienced contributors, 246 completed issues and five years’ average experience on their study projects. Recruitment and issue submission narrow the population. [§§2.1–2.2](https://arxiv.org/pdf/2507.09089v2#page=4) |
| 2 | SRC-0011:C02 | Developers forecast each issue before treatment assignment and could decline to use an allowed tool. Cursor Pro and Claude 3.5/3.7 Sonnet predominated. Excluding 25 early block-randomized issues gave a 20% slowdown. [§2.2](https://arxiv.org/pdf/2507.09089v2#page=5) · [§E.3](https://arxiv.org/pdf/2507.09089v2#page=33) |
| 3 | SRC-0011:C03 | The outcome sums two intervals of contributor work. First review separates them. Calendar waits and the reviewing colleague’s labor fall outside that clock. The analysis filled 27 missing post-review observations with the corresponding arm mean. [§2.3](https://arxiv.org/pdf/2507.09089v2#page=6) · [§C.3.4](https://arxiv.org/pdf/2507.09089v2#page=27) · [§G.2.1, time instructions](https://arxiv.org/pdf/2507.09089v2#page=41) |
| 4 | SRC-0011:C04 | Confirmed 136 allowed and 110 disallowed completions. The raw mean time difference was +34%. The log-time regression adjusting for forecast difficulty gave +19% with a reported 95% interval of +2% to +39%. The default uses HC3 errors. The attrition account required a qualification, recorded below. [§§3–3.1](https://arxiv.org/pdf/2507.09089v2#page=8) · [§§D.1–D.2](https://arxiv.org/pdf/2507.09089v2#page=28) · [METR’s published interval](https://metr.org/blog/2026-02-24-uplift-update/) |
| 5 | SRC-0011:C05 | The 24% forecast reduction precedes assignment. The 20% retrospective reduction comes from developers’ post-study estimates, weighted by completed issue count. Both describe beliefs. [§3.1](https://arxiv.org/pdf/2507.09089v2#page=8) · [§D.6](https://arxiv.org/pdf/2507.09089v2#page=31) |
| 6 | SRC-0011:C06 | On a common recording subset, recording duration gave +25% and developer timings +24%. The two one-hour-versus-zero imputation scenarios yielded +14% and +23%. These sensitivity results have different meanings from interval endpoints. [§C.3.4](https://arxiv.org/pdf/2507.09089v2#page=27) |
| 7 | SRC-0011:C07 | Verified that 128 labeled recordings (143 hours) yielded 74 usable recordings (84 hours) after filtering. Labelers prioritized shorter recordings and developers sometimes omitted small revisions. [§2.4](https://arxiv.org/pdf/2507.09089v2#page=8) · [§G.8](https://arxiv.org/pdf/2507.09089v2#page=45) |
| 8 | SRC-0011:C08 | Both Appendix C estimates use the 44 valid AI-allowed recordings. About 9% was categorized as review and cleanup and 4% as waiting. Separate testing and debugging labels limit what the review category captures. The full-sample causal time effect cannot be apportioned using those percentages. [§C.1.4](https://arxiv.org/pdf/2507.09089v2#page=20) · [§C.2.9](https://arxiv.org/pdf/2507.09089v2#page=25) · [§G.8 labels](https://arxiv.org/pdf/2507.09089v2#page=49) |
| 9 | SRC-0011:C09 | Confirmed the below-44% Cursor acceptance figure. Footnote 13 excludes three developers with pre-existing subscriptions. The accounts of retrying and discarding suggestions are supported. The survey percentages in the accompanying narrative required a qualification about the code respondents used. [§C.1.4 and footnote 13](https://arxiv.org/pdf/2507.09089v2#page=20) · [§G.5.1, questions 12–13](https://arxiv.org/pdf/2507.09089v2#page=45) |
| 10 | SRC-0011:C10 | The 15 versus nine minutes are mean post-review *author* time in the allowed and disallowed arms respectively. METR calls the difference statistically insignificant. The claim preserves uncertainty about PR quality. [§C.2.7](https://arxiv.org/pdf/2507.09089v2#page=23) · [§C.3.4, units](https://arxiv.org/pdf/2507.09089v2#page=27) |
| 11 | SRC-0011:C11 | Table 1 groups proposed mechanisms using exploratory evidence. The five-point per-issue effort question and mixed interview accounts supply limited evidence about subjective ease. The study did not measure change in fatigue through a review session. [§3.3 and Table 1](https://arxiv.org/pdf/2507.09089v2#page=10) · [§C.2.6](https://arxiv.org/pdf/2507.09089v2#page=23) · [§G.2.1](https://arxiv.org/pdf/2507.09089v2#page=41) |
| 12 | SRC-0011:C12 | Matched signed change in time, cohort and interval separately. Returning developers had −18% (−38% to +9%) and new recruits −4% (−15% to +9%). The later sample included 10 returners and 47 new participants across 143 repositories and over 800 tasks. Both intervals span zero. [Follow-up, opening estimates and study details](https://metr.org/blog/2026-02-24-uplift-update/) |
| 13 | SRC-0011:C13 | The 30–50% figure counts surveyed developers who withheld some tasks. Pay fell from $150 to $50 per hour, and one developer completed zero AI-disallowed tasks. The authors discuss changes in output and the difficulty of timing overlapping work. The data establish neither the gains on omitted tasks nor a statistical lower bound on population gains. [Follow-up, selection discussion and items 1–6](https://metr.org/blog/2026-02-24-uplift-update/#wider-adoption-of-ai-has-made-it-more-difficult-to-measure-task-level-productivity) |

## Provenance and relevance

The byline reads Beth Barnes and the arXiv metadata reads Elizabeth Barnes. The submission record confirms both July 2025 dates and links to CC BY 4.0. The July 10 METR article describes the same experiment. The February 2026 article discusses a later, partly overlapping sample. The dossier attributes both sources and presents original explanatory prose. Its reuse record distinguishes the preprint license from the later post’s copyright notice. [Version record](https://arxiv.org/abs/2507.09089v2) · [License deed](https://creativecommons.org/licenses/by/4.0/) · [Companion write-up](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) · [Follow-up](https://metr.org/blog/2026-02-24-uplift-update/)

OB-11 receives direct evidence about the contributor’s review work. Cognitive fatigue and team queue effects remain open questions. The BP-05 slicing procedure and AP-01 stopping decision are catalog adaptations. The trial never assigned either practice. This audit verifies publication fidelity. It did not reanalyze participant data or view private screen recordings. [§§3.2–3.3](https://arxiv.org/pdf/2507.09089v2#page=9)

## Corrections and disposition

1. For SRC-0011:C04, requested that the dropout account include the 24 deliberately dropped issues in addition to the six AI-allowed and seven AI-disallowed issues left unfinished. The paper reports a manual review of reasons for the 24 withdrawals. [§C.3.3](https://arxiv.org/pdf/2507.09089v2#page=26)
2. For SRC-0011:C09, requested that the accompanying 75% and 56% survey figures explicitly refer to developers’ usual treatment of code they used. The questionnaire is more specific than the Appendix C shorthand. [Exit survey, questions 12–13](https://arxiv.org/pdf/2507.09089v2#page=45)

**Final disposition: PASS.** I reread both amended passages alongside §C.3.3 and survey items 12–13. The revised dossier distinguishes intentionally withdrawn issues from uncompleted assignments and scopes survey responses to retained code. All 13 ledger claims pass. No outstanding source corrections.

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0011--review-work-and-developer-time.md](../sources/SRC-0011--review-work-and-developer-time.md) · [Local copy](../sources/SRC-0011--review-work-and-developer-time.md)
