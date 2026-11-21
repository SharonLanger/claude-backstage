---
topic_id: OB-06
title: "Non-determinism"
coverage: partially supported
source_edges:
  - id: SRC-0019
    relationship: DIRECT
    strength: high
    finding: "Identical Python generation requests yielded different results across five calls, including at temperature zero."
  - id: SRC-0008
    relationship: SUPPORTING
    strength: moderate
    finding: "Against a matched fresh-sample cap, allocating attempts to repairs sometimes improved and sometimes reduced the share of tasks with a passing candidate."
  - id: SRC-0003
    relationship: SUPPORTING
    strength: moderate
    finding: "Sequential feedback-conditioned repair and scheduled specification-only restarts yielded different cumulative solve rates on HumanEval."
pattern_ids: [PAT-0004]
publication_status: published
---

# OB-06 — Non-determinism

“Same request and settings, different patch.” “At temperature zero, a retry fixed one case and broke another.” The evidence directly supports variation from identical code-generation requests and a temperature effect in the tested configurations. It leaves open whether long feedback-driven retry sequences converge in real repositories and what causes the residual variation at zero.

## What the sources measure

- **Identical requests can produce materially different behavior.** Ouyang et al. generated five Python candidates from the same zero-shot task prompt on each of 829 CodeContests, APPS and HumanEval problems. At GPT-3.5 temperature one, 39.63% of HumanEval problems had both an all-pass and a zero-pass candidate among the five. For CodeContests, the share with no tested input on which all five agreed dropped from 75.76% at temperature one to 43.64% at zero. Agreement is distinct from passing the suite. Separately, at zero on CodeContests, mean pairwise agreement excluding exceptions was 0.81 for five choices in one request and 0.46 for five one-choice requests. Request grouping changed the measured agreement. It did not test concurrent development workflows. The manuscript’s settings prose and reported temperature table diverge, so the results here follow the tables. SRC-0019:C01–C06, §§2–3.4 Fig. 1, §4.1.1 Table 2 and §§4.2–4.5 Tables 5–7. [Dossier](../sources/SRC-0019--repeatability-of-code-generation.md) · [Original paper](https://doi.org/10.1145/3697010)
- **A useful repair and a fresh sample spend the budget differently.** Olausson et al. held temperature at 0.8 and assessed whether any candidate passed executable tests. On GPT-4/APPS, ten initial programs with one repair each yielded 66.1% versus 63.1% for a fresh-only cap of 20. Two initial programs with ten repairs each gave 61.8% versus 63.4% at a cap of 22. Repairs from the same start were siblings. Repeated estimates resampled a frozen candidate pool, and neither comparison measures the convergence of a long repair chain. SRC-0008:C01–C06, §§2–3.2 and §4.1 Fig. 3b. [Dossier](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Original paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=6)
- **Sequential retries answer a different question.** Adnan and Kuhn pass earlier code and failure feedback into repairs, up to a six-attempt total cap. A scheduled specification-only retry improved final solve rates for each of the nine Table 2 entries at one or both schedules, while two entries worsened at the earlier schedule. The unsolved pool changes after each attempt, and a restart changes the task input. The comparison cannot estimate how repeatedly submitting an identical prompt converges. Adjacent prose and table values disagree, so use the table for the result. SRC-0003:C02–C03, C06–C08, C11–C12, RQ3 pp. 4–5, Table 2 pp. 6–7 and Discussion pp. 9–10. [Dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Original paper](https://www.nature.com/articles/s41598-025-27846-5)

These are separate experiments with HumanEval reuse across all three, APPS reuse across two, and different model settings, prompts and endpoints. Identical inputs yielding different programs, better candidate pools under an executable check, and repair schedules improving accumulated solve rates are compatible findings. The backend source of variation and whether retries approach any stable answer or reliably find the intended behavior in time remain open.

## Where the pattern applies

[Compare repair with fresh candidates](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) fits a bounded contract with a common test and a fixed budget. It asks the developer to compare candidates with the same acceptance criteria and inspect successful ones for uncovered behavior. Ouyang et al. found repeated error types in some groups where all attempts failed and show an example in which the best illustrated candidate still misses part of the requirement. SRC-0019:C08, C12, §7.2 and companion Appendix pp. 5–6. [Dossier](../sources/SRC-0019--repeatability-of-code-generation.md) · [Original paper](https://doi.org/10.1145/3697010)

## Drive navigation

- [audits/PAT-0004--verification.md](../audits/PAT-0004--verification.md) · [Local copy](../audits/PAT-0004--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [audits/SRC-0008--verification.md](../audits/SRC-0008--verification.md) · [Local copy](../audits/SRC-0008--verification.md)
- [audits/SRC-0019--verification.md](../audits/SRC-0019--verification.md) · [Local copy](../audits/SRC-0019--verification.md)
- [patterns/PAT-0004--compare-repair-with-fresh-candidates.md](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) · [Local copy](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
- [sources/SRC-0008--self-repair-versus-fresh-samples.md](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Local copy](../sources/SRC-0008--self-repair-versus-fresh-samples.md)
- [sources/SRC-0019--repeatability-of-code-generation.md](../sources/SRC-0019--repeatability-of-code-generation.md) · [Local copy](../sources/SRC-0019--repeatability-of-code-generation.md)
