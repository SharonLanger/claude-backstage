---
source_id: SRC-0012
reviewed: 2026-11-21
reviewer: independent source reviewer
initial_verdict: PASS WITH CHANGES
verdict: PASS
---

# SRC-0012 verification

**PASS after correction.** The reviewed dossier supports a narrow behavioral finding for OB-05. Reversing which answers receive credit exposed failures to follow the changed instruction in these benchmarks. The experiments leave open whether mentioning a forbidden action increases its probability. [Reviewed dossier](../sources/SRC-0012--negated-instructions.md) · [Proceedings paper](https://proceedings.mlr.press/v203/jang23a.html)

## Claim checks

| Finding | Claim | Independent result |
|---|---|---|
| 1 | SRC-0012:C01 | Verified all nine template pairs in Table 1. The authors chose ordinary templates for their performance with OPT, then reversed them by hand. This selection matters when interpreting the difference. [§2.1 and Table 1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) |
| 2 | SRC-0012:C02 | Verified paired evaluation of 300 items per dataset, multiple accepted alternatives for some tasks, input-word distractors for Lambada and the training-answer sampling rule for QA. [§2.1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) |
| 3 | SRC-0012:C03 | Visually checked the green prediction in both panels of Figure 1. GPT-3 selects water flowing from the faucet in both. This is a single example. [Fig. 1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=2) |
| 4 | SRC-0012:C04 | Inspected the option-loss calculation, both minimum-score selections and the prediction-in-label-set test. The released scorer supports the account of both variants. The paper leaves the mapping of variants to particular plots unspecified. [Scoring functions](https://github.com/joeljang/negated-prompts-for-llms/blob/main/utils.py#L348-L472) |
| 5 | SRC-0012:C05 | Verified the reported direction and approximate two-condition average. The caption and panel axes cover different lists of OPT sizes. Correction rechecked below. [§3.1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=4) · [Fig. 4](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=8) |
| 6 | SRC-0012:C06 | Verified the analyst's deduction. Complementary labels give one hit across two conditions for an unchanged answer. Two items with changed answers can produce the same aggregate if one receives two hits and the other zero. The aggregate alone leaves agreement unidentified. [Label construction and paired metric](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) |
| 7 | SRC-0012:C07 | The introductory results and Appendix B substantiate the authors' account of persistent difficulty for instruction-adapted models and their stated inverse trend. [Results summary](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=2) · [App. B](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=9) |
| 8 | SRC-0012:C08 | Figure 3 and §3.2 identify GPT-3 175B in-context QA as the exception and give the eight-shot token limit for the omitted Lambada comparison. The methods separately describe the OPT-66B demonstration experiments. [Fig. 3 and §3.2](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) |
| 9 | SRC-0012:C09 | Checked the size of all three fine-tuned OPT models, negated training prompts, data cap, learning rate, epochs and checkpoint against §2.2. Appendix B reports the tradeoff with ordinary-prompt performance. [Training procedure](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) · [App. B](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=10) |
| 10 | SRC-0012:C10 | Confirmed participant ages and count, the three tasks and disjoint 50-item conditions. The paper gives 31.3% as an average gap on a percentage-accuracy plot. The dossier credits the authors for the estimate and limits its scope to this comparison. [§2.2](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=4) · [Fig. 3 and §3.2](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) |
| 11 | SRC-0012:C11 | The authors explicitly describe the pretraining account as a conjecture and call for further analysis. The experiment lacks a no-mention control or intervention on internal states. [§3.1, conjecture](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) |
| 12 | SRC-0012:C12 | The closing section urges caution before reliance in real-world decisions. The paper measured choices on language tasks. The dossier attributes the broader judgment to the authors. [§4](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) |

## Provenance, rights and related evidence

The volume confirms publication on January 19, 2023, following the December 3, 2022 workshop in New Orleans. The title, citation authors, volume and page range agree with the proceedings record. The PDF has a transposition in the second author's given name. The workshop and arXiv records support the spelling used in the dossier. The acknowledgments list the three funding awards. [Volume 203](https://proceedings.mlr.press/v203/) · [Workshop listing](https://tl4nlp.github.io/accepted_work.html) · [arXiv v1](https://arxiv.org/abs/2209.12711v1) · [Acknowledgments](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=6)

I followed the preprint's license link to CC BY 4.0 and checked §§2–4 of PMLR's standard agreement. The dossier records the distinction between the preprint's explicit license and the unsigned publisher form. It uses original analysis and links back to figures, templates and code without reproducing them. [arXiv license](https://arxiv.org/abs/2209.12711v1) · [License deed](https://creativecommons.org/licenses/by/4.0/) · [Publisher agreement](https://proceedings.mlr.press/pmlr-license-agreement.html)

The adjacent NeQA study uses transformed questions and documents several scaling shapes. It cites the Jang preprint. The later mechanistic study examines two named model families and reports causal intervention results on negated questions. Each lead is accurately scoped. The file-selection example is labeled as the dossier author's analogy. No efficacy claim for rewriting a developer instruction follows from these comparisons. [Zhang et al., introduction and related work](https://aclanthology.org/2023.findings-acl.472.pdf) · [Zhou et al., abstract](https://proceedings.mlr.press/v306/zhou26bq.html)

## Correction and disposition

The initial review requested one change to SRC-0012:C05 and its narrative. Appendix A's caption stops at 66B. Visual inspection shows a 175B label on several panel axes, including Web Questions and Natural Questions. On rereading both corrected passages, I verified that the dossier now distinguishes the methods list, the caption and the axes. All twelve claims pass. Verification covered the publications and the released scoring logic. It did not rerun the experiments. [Fig. 4, PDF p. 8](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=8)

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0012--negated-instructions.md](../sources/SRC-0012--negated-instructions.md) · [Local copy](../sources/SRC-0012--negated-instructions.md)
