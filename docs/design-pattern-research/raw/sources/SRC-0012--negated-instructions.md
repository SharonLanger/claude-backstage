---
source_id: SRC-0012
status: accepted
original_title: "Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts"
authors: ["Joel Jang", "Seonghyeon Ye", "Minjoon Seo"]
publisher: "Proceedings of Machine Learning Research"
source_type: empirical_paper
published: 2023-01-19
updated: unknown
accessed: 2026-11-21
original_url: "https://proceedings.mlr.press/v203/jang23a.html"
full_text_url: "https://proceedings.mlr.press/v203/jang23a/jang23a.pdf"
source_version: "PMLR 203, pp. 52–62, pmlr-v203-jang23a. Author preprint arXiv:2209.12711v1, 2022-09-26."
full_text_reuse: not_authorized_or_unverified
reuse_basis: "PMLR provides a standard CC BY 4.0 publication agreement. Article-specific terms for the proceedings PDF were unverified. ArXiv explicitly licenses v1 under CC BY 4.0."
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [OB-04, OB-05]
related_patterns: []
review: PASS
publication_status: published
---

# Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts

## Provenance and scope read

Joel Jang, Seonghyeon Ye and Minjoon Seo of KAIST authored this empirical case study for the first Transfer Learning for Natural Language Processing Workshop, held on December 3, 2022, in New Orleans alongside NeurIPS. PMLR released volume 203 on January 19, 2023. The PDF spells the second author's given name “Seongheyon.” This dossier follows the PMLR citation record, the workshop's accepted-work listing and the arXiv record, which agree on “Seonghyeon.” The September 2022 arXiv v1 and the proceedings paper represent one study. The acknowledgements identify three Korean government-funded IITP grants. [PMLR paper record](https://proceedings.mlr.press/v203/jang23a.html) · [PMLR volume 203](https://proceedings.mlr.press/v203/) · [Workshop accepted work](https://tl4nlp.github.io/accepted_work.html) · [ArXiv submission record](https://arxiv.org/abs/2209.12711v1) · [PMLR PDF, p. 6](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=6)

The public proceedings paper has 11 PDF pages. Reading covered the introduction and task construction, Table 1, the two results sections, the conclusion, the references and the text and figure captions in Appendices A–B. The paper and its documented approximations supply the numerical claims below. The author's repository and scoring functions clarify the candidate-ranking setup, but the experiments were outside this dossier's reproduction scope. Locators use the PDF's internal page numbers, with PDF page 1 corresponding to proceedings page 52. [Proceedings PDF](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf) · [Author repository](https://github.com/joeljang/negated-prompts-for-llms) · [Released scoring code](https://github.com/joeljang/negated-prompts-for-llms/blob/main/utils.py)

## Reader's orientation

An answer can be factually right and still violate the instruction. This study asks whether a model that can find the ordinarily correct answer will change its selection when the same question and answer options call for an incorrect answer instead. On the tested GPT-3 and OPT series, larger checkpoints tended to score better under ordinary instructions and worse when the scoring criterion was reversed. The paper also assesses a limited set of instruction-adapted, few-shot and fine-tuned models. This directly bears on the behavioral part of **OB-05 Negative bleedthrough**. The outcome measures candidate preferences under two prompt conditions. Whether a prohibited action's mention increases its likelihood relative to an unmentioned baseline, or whether any internal representation causes an error, remains outside the evidence of this study. [Proceedings PDF, Fig. 1, Table 1, §§3.1–3.2 and App. A](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=2)

## Detailed analytical reading

### The benchmark changes the criterion for success

The authors selected three commonsense reasoning datasets (PIQA, ARC-Easy and COPA), three sentence completion datasets (HellaSwag, StoryCloze and Lambada) and three question-answering datasets (Web Questions, Natural Questions and TriviaQA). They began with Promptsource templates that performed well with OPT and manually reversed the target. Table 1 uses lexical reversals such as asking for an inappropriate ending or an incorrect answer. This operationalization differs from a user asking a chat agent to perform an open-ended task with a side constraint. Figure 1 illustrates a binary COPA item where opening a faucet can be followed by water flowing from it or by a toilet filling. GPT-3 selects the faucet outcome under both instructions. The ordinarily sensible answer earns credit only under the original instruction. [Proceedings PDF, Fig. 1, §2.1 and Table 1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=2)

The same 300 sampled instances per dataset were used under each instruction, yielding 600 item-condition evaluations per dataset. The authors accepted multiple distractors under the reversed instruction when the candidate set had more than two options, as in ARC-Easy, Lambada and HellaSwag. For Lambada, they formed distractors from words in the input. For the three question-answering tasks they drew the alternative from training answers while excluding overlaps with test answer candidates. Candidate construction affects task difficulty. Recognizing that one supplied answer looks out of place can satisfy the reversed instruction without generating a credible alternative from scratch. [Proceedings PDF, §2.1, pp. 2–3 and Table 1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3)

The released causal-language-model scorer calculates the conditional cross-entropy of each supplied option under the prompt. It computes picks using total and per-token mean cross-entropy, then measures accuracy by checking whether the predicted option is in the condition's acceptable label set. The paper does not identify a scoring variant for every plotted series. This setup measures constrained ranking and accuracy. The scoring code is a companion artifact and the local reading did not reproduce the historical runs. [Proceedings PDF, §2.1 and Table 1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) · [Released scoring code, `inference_autobatch` and `fwd`](https://github.com/joeljang/negated-prompts-for-llms/blob/main/utils.py#L348-L471)

### Model size changed the scores in opposite directions

The zero-shot GPT-3 comparison uses Ada, Babbage, Curie and Davinci, displayed in Figure 2 as 350M, 1.3B, 6.7B and 175B. The methods list OPT checkpoints from 125M through 175B. Appendix A's Figure 4 caption enumerates eight sizes ending at 66B. Several panel axes, including Web Questions and Natural Questions, also label 175B. The caption is incomplete as an inventory of the panel labels. Across the tested tasks, the authors describe a tendency for negated accuracy to decline with scale even as ordinary accuracy climbs, leaving their two-condition mean around 50%. This is a trend in the benchmark and model series, with parameter count varying across available checkpoints. The comparison leaves open other differences between checkpoints and performance on a later model family. [Proceedings PDF, §§2.2 and 3.1, Fig. 2](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=4) · [App. A, Fig. 4](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=8)

The two-condition mean has a useful interpretation and a limit. For an item with complementary sets of acceptable answers, a model that picks the same option on both prompts earns one correct answer out of two. That holds even when several options are acceptable under the negated instruction. A mean near 50% is compatible with that behavior. It can also arise when some changed selections improve the paired score and others worsen it. Determining the frequency of identical selections requires item-level paired predictions. A uniform random guesser's chance of success for each polarity depends on the count of its acceptable candidates, even though the mean chance across complementary conditions is 50%. [Proceedings PDF, §2.1 and §3.1, Fig. 2](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=4)

### The tested interventions had different limits

The instruction-adapted comparisons included T0 at 3B and 11B and four InstructGPT variants carrying the GPT-3 family names. The authors report some improvement with instruction adaptation and also describe larger instruction-following variants scoring worse on negated prompts in Appendix B. For in-context learning, the methods list OPT-66B with 2, 4 and 8 demonstrations. Figure 3 also discusses a GPT-3 175B in-context comparison. The paper singles out GPT-3 175B on question answering as the exception to the approximately 50% paired mean among the displayed methods. Its in-context result for Lambada was omitted because eight demonstrations exceeded the API's token limit. This leaves a missing condition in the comparison. [Proceedings PDF, §1, §2.2, §3.2 and Fig. 3](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) · [App. B and Figs. 5–13](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=9)

The fine-tuning arm used OPT at 125M, 350M and 1.3B. The authors used negated prompts, trained for five epochs at a fixed learning rate of 0.001 and evaluated the final checkpoint. They used the available training data up to 10,000 instances per task. Appendix B reports that gains on the negated side came with weaker ordinary-prompt accuracy and an average near 50% across the two conditions. That tradeoff describes the particular training setup. It leaves mixed-polarity training, other objectives and larger instruction-following models outside that finding. [Proceedings PDF, §2.2, p. 3](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) · [App. B, pp. 9–10](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=9)

### The human reference and the proposed explanation

The human evaluation covered COPA, Lambada and Natural Questions, one task per category. Three 13-year-olds were evaluated using 100 of the 300 sampled instances per task, with 50 in the original condition and a disjoint 50 in the negated condition. This differs from the model benchmark that pairs both instructions with every item. The authors report an average gap of about 31.3 points on the percentage accuracy scale between the best compared method and the human reference for the two-condition scores. This is the reported summary of a small three-task reference. The paper gives no interval for that estimate and the human set cannot support a nine-task population-level comparison. [Proceedings PDF, §2.2 and §3.2, Fig. 3](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=4)

The authors conjecture that pretraining may favor ordinary continuations because negatively worded tasks occur less often, and that larger models' stronger priors might make the reversal harder. Their tests alter wording and observe scored choices. They do not measure the relevant corpus frequencies, experimentally rebalance the corpora or intervene on internal representations. The study therefore supports a behavioral sensitivity failure under tested conditions. The hypothesized training explanation and the claim that a forbidden action's tokens become causally more active require separate evidence. [Proceedings PDF, §3.1, “A Conjecture on Why Inverse Scaling Exists,” and §4](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5)

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support / caveat |
|---|---|---|---|---|
| SRC-0012:C01 | The authors manually reverse Promptsource instructions for nine tasks in three categories, holding the evaluated instance constant across the two model prompt conditions. | Study design | [§2.1, pp. 2–3, Table 1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) | Direct. The prompts mostly reverse the criterion lexically. The experiment does not survey the syntax of real-world prohibitions. |
| SRC-0012:C02 | Model evaluation uses 300 items per dataset under both prompt conditions. The reversed scoring can accept multiple options. Lambada and the three QA datasets use constructed alternatives. | Study design | [§2.1, p. 3](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) | Direct. Inference count is 600 item-condition evaluations per dataset. Acceptance depends on the candidate set. |
| SRC-0012:C03 | In the faucet example, GPT-3 selects the same ordinarily appropriate outcome when the instruction changes to ask for the inappropriate one. | Illustrative observation | [Fig. 1, p. 2](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=2) | Direct. One worked binary example. |
| SRC-0012:C04 | The released causal-model scorer ranks given options using conditional cross-entropy and reports separate total and token-mean ranking variants. A hit is a predicted option in the accepted label set. | Companion-code observation | [`utils.py`, `inference_autobatch` and `fwd`](https://github.com/joeljang/negated-prompts-for-llms/blob/main/utils.py#L348-L471) | Direct for the code as read. The paper gives no per-plot scoring-variant mapping. |
| SRC-0012:C05 | The authors report a tendency for larger zero-shot GPT-3 and OPT variants to improve under ordinary task prompts and decline under reversed prompts, with a two-condition mean near 50%. | Empirical result | [§3.1 and Fig. 2, p. 4](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=4) · [App. A and Fig. 4, p. 8](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=8) | Direct as a reported trend. The OPT chart caption ends at 66B while §2.2 and some panel axes include 175B. No universal or strictly monotone size effect is inferred. |
| SRC-0012:C06 | With complementary labels, an unchanged choice on both prompts scores 50% on that pair. The aggregate mean by itself does not identify the fraction of unchanged choices. | Analyst interpretation of metric | [§2.1, p. 3 and §3.1, p. 4](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=4) | Deduction from complementary acceptance. Item-level agreement would answer the frequency question. |
| SRC-0012:C07 | T0 and InstructGPT still show difficulty on the negated tasks after instruction adaptation. Appendix B reports inverse scaling among the adapted variants. | Empirical result | [§1, p. 2](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=2) · [§2.2, p. 3](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) · [App. B, pp. 9–11](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=9) | Direct as an author-reported result about the tested variants. |
| SRC-0012:C08 | GPT-3 175B with in-context learning on QA is the authors' stated exception to the approximately 50% two-condition mean in Figure 3. The corresponding Lambada comparison was omitted at eight shots because of the API token limit. | Empirical result and reporting limit | [§3.2 and Fig. 3 caption, p. 5](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) | Direct. The supplement's OPT-66B demonstration experiments are a separate comparison. |
| SRC-0012:C09 | Fine-tuning small OPT checkpoints on negated instructions improved negated-task accuracy at the expense of original-task accuracy, leaving the paired mean around 50%. | Empirical result | [§2.2, p. 3](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3) · [App. B, pp. 9–10](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=9) | Direct for 125M, 350M and 1.3B and the authors' specific five-epoch procedure. |
| SRC-0012:C10 | The human reference uses three 13-year-olds and three tasks, with disjoint sets of 50 original and 50 reversed items per task. The authors report an average human advantage of 31.3 points on the two-condition percentage-accuracy scale over the best compared method. | Reference design and reported result | [§2.2, pp. 3–4](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=4) · [§3.2 and Fig. 3, p. 5](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) | Direct as reported. Small participant pool and limited task selection. The percentage gap is not a relative improvement or a rate for all nine tasks. |
| SRC-0012:C11 | The authors propose a bias toward ordinary textual continuations from pretraining as one explanation and explicitly call for further experiments. | Author hypothesis | [§3.1, conjecture subsection, p. 5](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) | Speculative. The work reports choice outcomes and provides no causal test of token activation or corpus composition. |
| SRC-0012:C12 | The authors urge further work on instruction following before trusting models with consequential decisions. | Author interpretation | [§4, p. 5](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) | Direct as the authors' conclusion. The study evaluates language tasks rather than decisions or actions in deployed systems. |

## Extractable practitioner insights

### Recognize a model that keeps the default answer when the criterion reverses

The source's most transferable insight is diagnostic. When the same candidate can be scored under opposite instructions, separate accuracy by condition preserves information that a single average can hide. Item-level agreement adds a check on whether the model kept the ordinary answer. Consider an offline decision with two editable files. One is generated and one is a source file. If selecting the generated file is correct for one labeled test and invalid after the instruction reverses, selection of that file in both records is observable even without knowing the model's reasoning. This is an analyst analogy for an evaluation instrument. Coding-agent execution and developer outcomes were outside this study. Relevant to OB-05 through SRC-0012:C01–C06. [Proceedings PDF, Fig. 1, Table 1 and §3.1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=2)

### A mitigation can shift which instruction polarity fails

The fine-tuning arm shows why better scores on reversed instructions alone can give an incomplete picture. Under the tested setup, the improvement co-occurred with a drop on ordinary instructions. The in-context result also shows condition dependence, with a reported QA exception and a missing Lambada measurement. These are useful distinctions when interpreting a benchmark claim about a model or intervention. The study provides no comparison of ordinary negative constraints with equivalent positively framed constraints on a real task. Relevant to OB-05 through SRC-0012:C07–C10. [Proceedings PDF, §3.2 and Fig. 3](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5) · [App. B](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=9)

## Related work, conflicts, and limitations

- **OB-05 is partially supported.** The benchmark demonstrates a behavioral analogue of doing what the instruction reverses. The project topic also suggests a causal boost from mentioning a prohibited action. The benchmark lacks a neutral or omitted-action condition for estimating that boost, and the paper examines neither agent execution nor internal causal mechanisms. Its authors' pretraining account remains conjectural. [Proceedings PDF, Fig. 1, Table 1 and §3.1](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=5)
- **Inverse scaling is conditional.** Zhang et al. (2023) report inverse, U-shaped and positive scaling on NeQA depending on the model family and prompting method. Its negated questions differ from reversing the instruction over an unchanged question and candidate set. It limits cross-benchmark generalization from Jang et al. and uses a distinct benchmark even though it cites their preprint. [Zhang et al., Findings of ACL 2023, abstract and §4](https://aclanthology.org/2023.findings-acl.472/)
- **Interpretability requires its own experiment.** Zhou et al. (2026) use causal interventions with Mistral-7B and Llama-3.1-8B and report competing internal computations on negated questions, including suppression and constructive representations. This is a primary lead for a separate review of mechanism claims. Transport to open-ended instructions and agents would need evidence in that setting. [Zhou et al., ICML 2026, abstract](https://proceedings.mlr.press/v306/zhou26bq.html)
- **External validity is bounded by the evaluation.** Original templates selected for strong OPT performance, distractors constructed for some datasets and a limited sample of prompts all affect the interpretation. The models were evaluated on provided answer sets. Their ranking behavior gives no direct estimate of how frequently present-day chat assistants violate constraints during free-form generation or tool execution. [Proceedings PDF, §§2.1–2.2, pp. 2–4](https://proceedings.mlr.press/v203/jang23a/jang23a.pdf#page=3)

## Retrieval hints

- “I asked for the wrong answer and it still gave the right one.”
- “The answer stayed the same after I reversed the instruction.”
- “Can a model follow a negative instruction, or is it picking the usual answer?”
- Topics and tags: OB-05, negative bleedthrough, negated instructions, polarity reversal, candidate ranking, inverse scaling, GPT-3, OPT, paired accuracy, instruction following.

## Original article access and copyright/permission record

The proceedings record and PDF are publicly readable. PMLR's standard publication agreement grants CC BY 4.0 under its terms and asks for a citation and link to the proceedings paper. The individual PDF and records inspected do not establish the specific agreement for this copy. The arXiv v1 record links directly to a CC BY 4.0 license. The docket uses original prose and attributed facts, with the author's figures, prompts and paper available via the original links. Rights for upstream datasets and code were outside the license review. [PMLR paper](https://proceedings.mlr.press/v203/jang23a.html) · [PMLR model agreement, §§2–4](https://proceedings.mlr.press/pmlr-license-agreement.html) · [ArXiv v1 license link](https://arxiv.org/abs/2209.12711v1) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0012--verification.md)

## Drive navigation

- [audits/SRC-0012--verification.md](../audits/SRC-0012--verification.md) · [Local copy](../audits/SRC-0012--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/OB-04--selective-hearing.md](../topics/OB-04--selective-hearing.md) · [Local copy](../topics/OB-04--selective-hearing.md)
- [topics/OB-05--negative-bleedthrough.md](../topics/OB-05--negative-bleedthrough.md) · [Local copy](../topics/OB-05--negative-bleedthrough.md)
