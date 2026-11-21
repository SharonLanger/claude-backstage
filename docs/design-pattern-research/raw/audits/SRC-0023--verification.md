---
artifact_id: SRC-0023
artifact_type: source_verification
reviewer: review_trust
reviewed: "2026-11-21"
initial_verdict: PASS WITH CHANGES
verdict: PASS
---

# Independent source review of SRC-0023

I reopened the 13-page preprint linked by the ICSE program and checked all nine claims. Section VI.B(c) supplies direct evidence for AP-02 at the point of accepting an individual suggestion. Figure 4 measures the fate of suggestions by session end. Its headline percentage cannot serve as a measure of unchecked acceptance. [Source dossier](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md) · [Preprint, Figure 4 and §VI.B(c)][p8] · [ICSE program][icse]

## Numbered findings

| Finding | Claim | Independent check |
|---|---|---|
| 1 | SRC-0023:C01 | The paper defines trust through the action of relying on a suggestion. Researchers recorded screen and audio and clarified ambiguous actions. The sample comprises five students and five professionals, all regular LLM users with more than three years of programming experience. The methods specify 60 minutes and a 15-minute interview. Results describe sessions lasting 60–90 minutes. [§II, p. 2][p2] · [§III.B, Table II, p. 4][p4] · [§VI.A, p. 7][p7] |
| 2 | SRC-0023:C02 | The 29 initial respondents included 15 graduate students and 14 professionals. The two upper rating categories contain all 29 for correctness and 25 for comprehensibility. Coding of respondents’ definitions puts correctness first. Coding of their reasons for trusting Python snippets puts comprehensibility first. The survey’s one-line project descriptions constrain which properties participants could judge. [§III.A, pp. 2–3][p3] · [§IV.A, pp. 4–5][p5] · [§V.B and Fig. 3, p. 7][p7] |
| 3 | SRC-0023:C03 | Figure 4 partitions 142 suggestions into 117 accepted and 25 rejected. Its two branches below acceptance contain 75 kept and 42 edited or removed. Ignoring counts as rejecting. Editing can preserve a useful part of an accepted proposal. [§VI.A, pp. 7–8][p7] · [Fig. 4, p. 8][p8] |
| 4 | SRC-0023:C04 | I recomputed the shares from the figure. All-suggestion shares are (25 + 42)/142 = 47.2% and 75/142 = 52.8%. Within initial acceptances, 42/117 = 35.9% and 75/117 = 64.1%. Section VI.A attaches 52% to the latter retention count, section I describes 48% as mistaken trust, and section VIII.A invokes errors. Neither rejection nor editing establishes a defect. [§I, p. 2][p2] · [§VI.A and Fig. 4][p8] · [§VIII.A, p. 10][p10] |
| 5 | SRC-0023:C05 | The authors identify 13 cases where unchecked acceptance preceded revision or removal. Eight of those thirteen needed revision for incorrectness. The paper separately mentions four retained cases of blindly trusted code. Its criterion is absence of evaluation before accepting. The unit is a suggestion event, and the observation ends within the session. [§VI.B(c), p. 8][p8] |
| 6 | SRC-0023:C06 | The 61/117 count describes a reason for initial acceptance. Nine of the ten participants used testing at some point, including OP5’s immediate parser test. The paper supplies no corresponding fraction of all suggestions tested. [§VI.A, pp. 7–8][p8] |
| 7 | SRC-0023:C07 | I checked the six revisions after presumed correctness and the seven following changes outside the request. The new application tab and CSS sizing examples illustrate those groups. The authors present common reasons and supply no exhaustive attribution for the 42 modified or removed suggestions. [§VI.B(a–b), p. 8][p8] |
| 8 | SRC-0023:C08 | G3 recommends evaluating externally suggested code before acceptance, including unit tests for higher-risk work. G4 covers unexpected features and undefined entities. Seven researchers and eight returning survey participants rated the draft guidelines and supplied feedback. That design measures perceived impact and practicality. The catalog’s dashboard example and provisional branch workflow are clearly attributed adaptations. [§III.C, p. 4][p4] · [Fig. 5 and G3, p. 9][p9] · [G4, p. 10][p10] |
| 9 | SRC-0023:C09 | Section IX discusses the restricted Python survey, limited session time, side projects or backlog work, and limits on inter-developer inference. The 142 observations repeat across ten people. The paper supplies no measure of production merges, population prevalence or comparative intervention effectiveness. [§IX, p. 11][p11] |

## Provenance, rights and repairs

1. **Publication date.** IEEE’s Crossref deposit gives April 26, 2025 in both publication-date fields, pages 1678–1690 and the seven authors in preprint order. The program lists the May 1 presentation. June 23 is the date IEEE added the work to Xplore and the date the DOI record was created. On recheck the dossier uses April 26 in its publication field and assigns each of the other two dates its correct meaning. [DOI metadata][crossref] · [IEEE Xplore][ieee] · [ICSE program][icse]
2. **Tool counts.** The draft repeated the methods paragraph’s six ChatGPT-only and two Copilot-only users. I counted seven ChatGPT-only rows and one Copilot-only row in Table II. Both presentations have two multi-tool participants. I rechecked the corrected dossier, which preserves the disagreement. [§III.B, Table II, p. 4][p4]
3. **Rights and originality.** The freely readable Amazon preprint is the version the researchers and ICSE link. The DOI metadata lists version-specific sharing policies. I found no article-wide license authorizing full republication. The dossier contains original analytical prose, selected counts and attributed locations. The dossier now attributes the supplement notice to its analyst and claims no redistribution permission. Direct access returned HTTP 403 in this review, so I could not independently verify its displayed license. All nine ledger findings use the paper itself. [Amazon Science reading route][amazon] · [DOI metadata][crossref] · [Supplement][supp]

**Final disposition: PASS.** The first pass required changes to the publication date and the tool mix. I reread both corrected passages and the updated rights statement. The audit closes both findings. The supplement access limitation does not affect the analysis of the paper.

[amazon]: https://www.amazon.science/publications/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications
[crossref]: https://api.crossref.org/works/10.1109/ICSE55347.2025.00199
[ieee]: https://ieeexplore.ieee.org/document/11029928/
[icse]: https://conf.researchr.org/details/icse-2025/icse-2025-research-track/231/Trust-Dynamics-in-AI-Assisted-Development-Definitions-Factors-and-Implications
[supp]: https://figshare.com/s/7ace13271c37bc3eadbf
[p2]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=2
[p3]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=3
[p4]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=4
[p5]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=5
[p7]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=7
[p8]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=8
[p9]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=9
[p10]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=10
[p11]: https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=11

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0023--trust-and-unchecked-code-acceptance.md](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md) · [Local copy](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md)
