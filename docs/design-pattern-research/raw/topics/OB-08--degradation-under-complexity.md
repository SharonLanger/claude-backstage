---
topic_id: OB-08
title: "Degradation under complexity"
coverage: partially supported
source_edges:
  - id: SRC-0016
    relationship: DIRECT
    strength: high
    finding: "Benchmark completion declined on tasks that took humans longer, with limited evidence about the causal contribution of dependent steps."
  - id: SRC-0003
    relationship: SUPPORTING
    strength: low
    finding: "Declining rescue rates across HumanEval repair attempts are compatible with error compounding and with changes in the remaining task pool."
  - id: SRC-0006
    relationship: SUPPORTING
    strength: low
    finding: "Pocock recommends independently testable behaviors as implementation units and gives a rework anecdote, without a matched comparison of task sizes."
pattern_ids: [PAT-0003]
publication_status: published
---

# OB-08 — Degradation under complexity

“The assistant can do each part in isolation, but the complete change keeps breaking at the boundaries.” “A fix for the first problem introduced two more, and now the original requirement is getting lost.” The brief asks whether reliability falls as task size grows, whether small mistakes accumulate and where multi-step reasoning fails. The strongest evidence concerns overall success on tasks with different human completion times. Individual failure examples illustrate how rework can compound. They leave the general causal mechanism unresolved.

## What gets harder

Kwa et al. compared benchmark success against the time tasks took human baselines. Aggregate success fell as human task duration rose. The reported o3 50% time horizon of about 110 minutes is the midpoint of a fitted success curve on the **human** duration scale for that evaluation. An 80% success target yields horizons approximately four to six times shorter across the tested models. Task families and evaluation protocols vary along the duration axis. A discontinuity near one minute also shows why the fitted curve is an aggregate description. Repository familiarity changes the human clock. In one of five internal issues, top-scoring maintainer and contractor fixes took five and 81 minutes respectively. These differences make a model's quoted horizon a poor standalone time budget for a particular repository. SRC-0016:C01–C05, C09–C10, §§2.1–3.2, Figs. 3–4 and Appendix C.2 Table 3. [Dossier](../sources/SRC-0016--task-duration-and-reliability.md) · [Versioned paper](https://arxiv.org/html/2503.14499v4)

The same study reports that, among HCAST tasks, a higher score on an exploratory measure of task properties was associated with lower agent success after accounting for duration. The ratings covered a limited range. The selected debugging example shows an attempted correction introducing indentation and duplicate-method problems. The example establishes a plausible failure sequence, while the study leaves open how often that sequence occurs and which dependent steps independently cause a drop. SRC-0016:C07–C08, Appendix D.2 and Appendix F.2 Fig. 13. [Versioned paper](https://arxiv.org/html/2503.14499v4)

Adnan and Kuhn examine sequential feedback-conditioned repairs on short Python functions. A declining rescue rate among cases that remain unresolved can reflect a harder surviving task pool as well as worsening repairs. Context saturation, error propagation and repeated use of a failing approach are proposed mechanisms. The experiments use independent coding runs from Kwa et al. and answer a different question. Neither varies the number of dependent steps while holding a repository deliverable fixed. The NeurIPS paper, versioned preprint and METR launch post for the horizon work are records of the same study. SRC-0003:C02–C03, C10–C11, protocol p. 5 and Discussion pp. 9–10. [Dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Paper](https://www.nature.com/articles/s41598-025-27846-5)

## Where the pattern applies

[Slice a change for review](../patterns/PAT-0003--slice-a-change-for-review.md) gives a reviewer one observable behavior that can be checked through the system before the next behavior is introduced. Pocock independently describes that decomposition and its genuine prerequisites. Checks at boundaries can reveal where an incorrect assumption first enters the work. That is the catalog's application of the advice. The benchmark does not measure reliability gains from decomposing the same task, and the practitioner account has no such comparator. Multi-step reasoning limits, repository integration effects and error propagation rates remain open. SRC-0006:C02–C05, C07, C10. [Dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Tracer bullets and review workflow](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers)

## Drive navigation

- [audits/PAT-0003--verification.md](../audits/PAT-0003--verification.md) · [Local copy](../audits/PAT-0003--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [audits/SRC-0006--verification.md](../audits/SRC-0006--verification.md) · [Local copy](../audits/SRC-0006--verification.md)
- [audits/SRC-0016--verification.md](../audits/SRC-0016--verification.md) · [Local copy](../audits/SRC-0016--verification.md)
- [patterns/PAT-0003--slice-a-change-for-review.md](../patterns/PAT-0003--slice-a-change-for-review.md) · [Local copy](../patterns/PAT-0003--slice-a-change-for-review.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
- [sources/SRC-0006--vertical-slices-for-agent-tickets.md](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Local copy](../sources/SRC-0006--vertical-slices-for-agent-tickets.md)
- [sources/SRC-0016--task-duration-and-reliability.md](../sources/SRC-0016--task-duration-and-reliability.md) · [Local copy](../sources/SRC-0016--task-duration-and-reliability.md)
