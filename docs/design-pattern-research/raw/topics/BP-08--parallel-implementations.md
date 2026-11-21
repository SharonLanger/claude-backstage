---
topic_id: BP-08
title: Parallel implementations
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0008
    relationship: DIRECT
    strength: high
    finding: "Olausson and colleagues compare fresh and repair allocations under matched candidate caps using shared executable tests."
  - id: SRC-0019
    relationship: SUPPORTING
    strength: moderate
    finding: "Repeated identical prompts generated candidates with different test outcomes, and retrospective best-of-five selection used the benchmark tests."
  - id: SRC-0003
    relationship: SUPPORTING
    strength: moderate
    finding: "A scheduled fresh generation sometimes improved final accuracy within the same attempt cap as continued sequential repair."
pattern_ids: [PAT-0004]
---

# BP-08 Parallel implementations

## When it comes up

- “The first patch fails one known case. An alternative would be cheap to generate.”
- “Two versions pass. Which one should I keep?”
- “I can run three agents at the same time. Will that save time after review?”

The brief asks about generating alternatives concurrently and picking the best. Controlled coding studies directly support the value of sampling and testing alternatives under specific budgets. They leave the elapsed-time benefit of simultaneous work, human selection quality, and how to rank equally passing patches in a repository unresolved.

## What the comparisons show

Olausson and colleagues compare fresh program samples with initial samples followed by test-informed repairs. In the simulation, the mixed strategy draws on precomputed repairs only when the sampled initial batch has no passing program. The fresh-only and mixed allocations are evaluated at a matched maximum program count in each comparison. On GPT-4 and the study’s APPS sample, ten initial programs with one repair per failure reached 66.1% versus 63.1% fresh-only at a 20-program cap. An allocation of two initial programs with up to ten sibling repairs per initial program reached 61.8% versus 63.4% fresh-only at a 22-program cap. The respective caps compare strategies within each pair. The study estimates how often a budget and strategy yield at least one test-passing program. When simulated early stopping and generated tokens enter the comparison, sequential search generally reduces relative gains from repair, especially with a strong baseline. The results give conflicting directions under different allocations and leave the deployed scheduling question open. SRC-0008:C01–C07 and SRC-0008:C11. [Self-repair dossier](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Candidate budgets, §§3.2–4.1 and Fig. 3b](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=6) · [Token and stopping sensitivity, Appendix A](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=13)

Ouyang and colleagues repeated an identical prompt five times per task. At temperature one, 39.63% of HumanEval tasks had both an all-pass and a zero-pass candidate. Groups also shared some errors, and the retrospectively highest-scoring candidate was defined by the available tests. One HumanEval example shows an omitted input restriction even in the best-scoring illustrated candidate. Choice grouping influenced agreement in some settings. This is evidence about alternate samples and test-based ranking. Concurrent repository edits and reviewer choice were outside the design. SRC-0019:C01–C05, SRC-0019:C08 and SRC-0019:C12. [Repeatability dossier](../sources/SRC-0019--repeatability-of-code-generation.md) · [ACM §§4.1, 4.3 and 7.2](https://kclpure.kcl.ac.uk/ws/files/365277933/An_Empirical_Study_of_the_Non-Determinism_of_ChatGPT_in_Code_Generation_Version_of_Record.pdf) · [Companion appendix example, pp. 5–6](https://github.com/ShuyinOuyang/LLM-is-a-box-of-chocolate/blob/main/Appendix.pdf)

Adnan and Kuhn test a fresh generation substituted for a later repair along a sequential trajectory. The later schedule improved final accuracy in all nine rows of Table 2 and the earlier schedule lost against baseline in two rows. The research teams and intervention designs are separate across the three studies, while all three reuse HumanEval and the Olausson and Ouyang studies draw from APPS. Dataset reuse limits claims about breadth, and same-task samples share model, prompt or checks. Across-study agreement supports trying alternatives in bounded conditions. It cannot supply independent per-attempt odds or a universal allocation. SRC-0003:C06, SRC-0003:C08, SRC-0003:C11, SRC-0008:C04, SRC-0019:C01 and SRC-0019:C08. [Restart study dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Restart study, Table 2](https://www.nature.com/articles/s41598-025-27846-5/tables/2)

## Choosing among patches

[PAT-0004, Compare repair with fresh candidates](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) applies the comparative setup to a bounded change. Fix the requirement and checks, give fresh candidates a common base, keep changes isolated, and test and inspect the survivors. If two pass, judge their diffs against compatibility, the full contract and any untested case that might distinguish them. A small cap, separate checkouts and elapsed-time scheduling are catalog choices. Concurrency may suit a wait dominated by generation, while sequential attempts allow stopping early when checks or review dominate. Total generation, testing and review effort still matters to the choice. [Pattern verification](../audits/PAT-0004--verification.md)

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
