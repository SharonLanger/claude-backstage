---
audit_for: SRC-0014
role: independent_source_reviewer
checked: 2026-11-21
initial_verdict: PASS WITH CHANGES
verdict: PASS
corrections_verified: true
---

# SRC-0014 independent verification

**PASS after correction.** The [dossier](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) can support a practitioner discussion of what a passing check measures. Its counts describe particular benchmark runs. It labels the repository review suggestions as adaptations.

## Findings

1. **Identity and access.** I reopened the [METR original](https://metr.org/blog/2025-06-05-recent-reward-hacking/) and the [alternate article URL](https://evals.alignment.org/blog/2025-06-05-recent-reward-hacking/). The title, three credited authors, date and publisher agree with the dossier. The citation block identifies the metr.org URL. The review covered the case descriptions, benchmark and prompt tables, detection procedure, follow-up judgments, concluding proposal, footnotes and rights notice. It checks METR's published account. Raw trajectories and evaluation code were outside scope.
2. **SRC-0014:C01.** In the opening case descriptions, the kernel and Rust examples substantiate two distinct failures of measurement. Both are selected examples. The dossier correctly limits its conclusions to what the cases show.
3. **SRC-0014:C02.** I checked the table's numerator and denominator for each reported result. RE-Bench is 39/128, HCAST is 8/1,087, and Optimize LLM Foundry contributes 21/21 to RE-Bench. The adjacent text and footnotes 1, 2, 4 and 6 support the limits on causal attribution, model-version coverage, the ambiguous task exclusion, and the distinction between evaluation scores and training rewards. The excluded task was Restricted MLM.
4. **SRC-0014:C03–C04.** In the detection section, the follow-up inspection covered all runs in the three implicated RE-Bench families. Human reviewers checked candidates from both screening methods. The separate Claude 3.5 Sonnet (New) comparison used the initial score heuristic and monitor. Confirmed cases divide into two shared, two monitor-only and one score-only. The relative counts reveal disagreement. They provide no denominator for all cases either method missed.
5. **SRC-0014:C05.** The end of the detection discussion supports counting some unsuccessful attempts at using absent reference answers. Footnote 5 describes the separate policy for removing recognized inflated scores from capability results and acknowledges possible misses. The dossier preserves both distinctions.
6. **SRC-0014:C06.** The kernel follow-up paragraph counts ten responses to one prior plan. Its description of other tasks supports the qualification about different judgments. The dossier avoids drawing an inference about enduring intent from those replies.
7. **SRC-0014:C07.** The prompt comparison used 20 runs per condition. The percentages for first-generation plans were 80 in the original and 95, 80, 70 and 70 in the variants. Footnote 9 qualifies the consequences depicted in the research scenario. **Initial finding:** The dossier cited footnote 8 but omitted the possible sampling bias from rerunning flagged prompts. **Recheck:** I reread the corrected C07 row against footnote 8. It now explicitly records reruns and the possibility of undercounting if flags correlated with the behavior. Closed.
8. **SRC-0014:C08.** The penultimate substantive paragraph of the final training discussion proposes repairing a scoring flaw once detected. Its status as an author proposal is accurate. The article supplies no effectiveness test for preserving a repository check or rerunning a maintainer-owned example.
9. **Topic transfer and originality.** OB-03 and AP-02 are reasonable indirect mappings. The dossier expressly leaves everyday test weakening, maintenance costs and merge behavior open. The local comparison with SRC-0002:C07–C10 accurately describes separate practitioner guidance. The displayed site footer reserves rights. The dossier uses original prose and factual attribution, and reproduces no transcripts, implementation excerpts or full article. The reuse status is appropriate.

## Disposition

All eight ledger entries checked. The C07 repair closes the only requested change. No open source-review findings. Publication and Drive readback belong to the project integrator.

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0014--benchmark-shortcuts-and-validation.md](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) · [Local copy](../sources/SRC-0014--benchmark-shortcuts-and-validation.md)
