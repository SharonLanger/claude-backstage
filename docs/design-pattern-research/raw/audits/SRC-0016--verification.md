---
artifact_id: SRC-0016
artifact_type: source_verification
reviewer: review_complexity
reviewed: "2026-11-21"
verdict: PASS
---

# Independent source review of SRC-0016

**PASS.** The study supports using human task duration as an indicator of aggregate success in this benchmark. Its contribution to OB-08 is narrower than a causal account of complexity. The dossier preserves that distinction throughout its ten claims and labels the checkpoint and boundary-check examples as catalog adaptations. [Source dossier](../sources/SRC-0016--task-duration-and-reliability.md)

## Numbered findings

I reopened the versioned HTML, both publication records and the conference PDF. I checked the claims in §§2–4, Figures 2–4, Tables 1–3, and the cited appendix passages. The conference PDF's Figure 3 was also inspected visually. This review checks the published evidence and its interpretation. It does not reproduce the benchmark runs. [ArXiv v4](https://arxiv.org/html/2503.14499v4) · [Conference paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/85069585133c4c168c865e65d72e9775-Paper-Conference.pdf)

| Finding | Record | Independent check |
|---|---|---|
| 1 | Bibliography | The first arXiv submission is March 18, 2025, and v4 is July 10, 2026. The two lead authors share contribution credit. Chris Painter appears in v4 and on the conference PDF byline. The proceedings landing page omits Painter. The DOI, proceedings volume and METR attribution match. The arXiv metadata abstract gives the Claude example, while the v4 full text and conference PDF give the o3 example. [Version history](https://arxiv.org/abs/2503.14499v4) · [Proceedings record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/85069585133c4c168c865e65d72e9775-Abstract-Conference.html) |
| 2 | SRC-0016:C01 | Pass. §2.1 enumerates 97 HCAST items, all seven RE-Bench tasks and 66 SWAA items. The Figure 2 total and the denominator in §2.2 differ by one in both editions. The dossier correctly preserves both. Section 2.2 also verifies the total baseline hours and the 21 estimates. |
| 3 | SRC-0016:C02 | Pass. §3.1 gives the successful-baseline geometric mean and the RE-Bench exception. Appendix C.1 distinguishes the timing protocols and discusses selection from successful attempts and instruction overhead. |
| 4 | SRC-0016:C03 | Pass. §2.3 reports 12 frontier and four near-frontier models, approximately eight attempts per evaluated pair, and an across-model association. Figure 3 shows the family weighting and the human-duration axis. Appendix C.3 confirms scaffold variation, the SWAA exception and the imputed GPT-2 results. The comparison varies tasks as well as duration. |
| 5 | SRC-0016:C04 | Pass. The equation in §3.1 gives the 50% crossing on the scale of human time. Figure 4 identifies the abrupt change between the short SWAA items and HCAST. The curve describes the specified task mix. |
| 6 | SRC-0016:C05 | Pass. §§2.3 and 3.2–3.2.1 support the o3 midpoint, observed successes above four hours and lower 80% horizons. The authors explicitly discuss difficulty estimating a 95% horizon. The dossier distinguishes a fitted human-duration measure from an agent's runtime. |
| 7 | SRC-0016:C06 | Pass. Both pairs of counts match Table 2. Appendix D.1 and the caption specify the failure-only sample and the harder mix of o1 failures. These rows cannot supply failure rates across all runs. |
| 8 | SRC-0016:C07 | Pass. The Python examples in D.2.1 distinguish the unsuccessful GPT-4 Turbo repair from the Claude 3.5 Sonnet rewrite following indentation and duplicate-method problems. D.2.2 discusses weak feedback and missed information. These selected examples illustrate possible paths through a failure. |
| 9 | SRC-0016:C08 | Pass. Appendix F.2 reports mean 3.2 of 16 across HCAST and RE-Bench, and a maximum no greater than eight. The residual coefficient in the HCAST analysis is −0.081. Figure 13 concerns success conditional on rated duration. Figure 12 concerns improvement across model release dates. The dossier keeps those analyses distinct. |
| 10 | SRC-0016:C09 | Pass. Appendix C.2 reports five original issues from one repository. One issue was split for evaluation. Table 3 verifies the five- and 81-minute fixes with the same top score. Table 5 records missing or partial-credit comparisons. The authors present compatibility with the contractor baseline as a small external-validity check. |
| 11 | SRC-0016:C10 | Pass. Appendix B and B.2 describe automatic scoring, limited initial context, and little interaction with external actors or changing environments. Appendix C.2 separately describes manual review in the internal PR exercise. |
| 12 | Overlap and transfer | The conference and arXiv editions and the METR launch account cover the same study. The follow-up changed both task composition and evaluation infrastructure and remeasured models already studied. The reward-hacking report shares investigators and benchmark families. Its footnote 5 confirms screening of reported successes. Specific shared runs remain unverified. Becker et al. studied developers randomized to AI access by issue, a different experiment with four overlapping authors. [Launch](https://evals.alignment.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) · [Time Horizon 1.1](https://metr.org/blog/2026-01-29-time-horizon-1-1/) · [Reward-hacking report](https://metr.org/blog/2025-06-05-recent-reward-hacking/) · [Becker et al.](https://arxiv.org/html/2507.09089v2) |
| 13 | Rights and original work | The v4 HTML displays CC BY 4.0, and the metadata links the license. The dossier limits this finding to the covered arXiv material. Its paraphrases, discussion and practitioner examples are original. No trajectory transcript or third-party figure is republished. [ArXiv license record](https://arxiv.org/abs/2503.14499v4) · [License terms](https://creativecommons.org/licenses/by/4.0/) |

## Disposition

All ten ledger claims pass. No dossier correction was required. The primary evidence leaves the causal contribution of dependent steps, the frequency of error propagation, and the effectiveness of splitting the same deliverable unresolved. The staged [vertical-slicing dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) and [benchmark-shortcuts dossier](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) resolve at their cited paths. Publication and Drive readback are tracked by the orchestrator.

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0016--task-duration-and-reliability.md](../sources/SRC-0016--task-duration-and-reliability.md) · [Local copy](../sources/SRC-0016--task-duration-and-reliability.md)
