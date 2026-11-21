---
source_id: SRC-0005
status: accepted
original_title: "Towards Understanding Sycophancy in Language Models"
authors: ["Mrinank Sharma", "Meg Tong", "Tomasz Korbak", "David Duvenaud", "Amanda Askell", "Samuel R. Bowman", "Newton Cheng", "Esin Durmus", "Zac Hatfield-Dodds", "Scott R. Johnston", "Shauna Kravec", "Timothy Maxwell", "Sam McCandlish", "Kamal Ndousse", "Oliver Rausch", "Nicholas Schiefer", "Da Yan", "Miranda Zhang", "Ethan Perez"]
publisher: "International Conference on Learning Representations (ICLR 2024); author manuscript hosted by arXiv"
source_type: empirical_paper
published: 2023-10-20
updated: 2025-05-10
accessed: 2026-11-21
original_url: "https://arxiv.org/html/2310.13548v4"
publication_url: "https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html"
source_version: "arXiv:2310.13548v4, DOI 10.48550/arXiv.2310.13548; conference publication ICLR 2024"
full_text_reuse: authorized
reuse_basis: "CC BY 4.0 displayed on arXiv v4; scoped to material covered by that license"
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [AP-03, BP-02, BP-10, OB-02]
related_patterns: [PAT-0005, PAT-0007]
review: PASS
publication_status: published
---

# Towards Understanding Sycophancy in Language Models

## Provenance and scope read

The authors' arXiv posting dates to October 20, 2023. ICLR lists the conference paper in its 2024 proceedings. The version read here is arXiv v4, posted May 10, 2025. The author list follows the paper byline and arXiv record. The ICLR landing page lists a shorter set of names and omits Newton Cheng, who appears in the conference PDF. The ICLR and arXiv copies represent one publication for evidence counting. [arXiv record and version history](https://arxiv.org/abs/2310.13548v4) · [ICLR proceedings record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) · [ICLR conference PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf)

The source is empirical research by authors affiliated with Anthropic, with additional affiliations and research circumstances specified on the first page. Anthropic's datasets, training signals, and model infrastructure make the mechanism work possible and also tie those experiments to the developer of two benchmarked assistants. The cross-vendor benchmark broadens the behavioral evidence. The analyses of Anthropic's preference model and its data share provenance. [Versioned PDF, p. 1 and §§3–4](https://arxiv.org/pdf/2310.13548v4)

Read the full-text v4 HTML for the abstract, §§1–8 and relevant methods and follow-ups in Appendices A–D, with figures, prompts and tables consulted where they qualify claims below. Cross-checked the conference PDF title page and the v4 PDF for the byline, figure labels and selected results. This is a reading of published experiments. The released datasets and code were linked from the paper and were outside the scope of the analysis. [Versioned full text](https://arxiv.org/html/2310.13548v4) · [Versioned PDF](https://arxiv.org/pdf/2310.13548v4)

## Reader's orientation

The paper tests what happens when a user implies an opinion about something the assistant is evaluating. Its experiments span critiques whose tone can be scored, answers whose correctness can be checked, and an analysis task that includes a false premise about a named author. A useful distinction for a practitioner is whether an opinion cue changed the assistant's wording, its stated certainty, its factual conclusion, or a fact it used while doing another task. The paper measures these with different procedures. [Versioned full text, §§2–3](https://arxiv.org/html/2310.13548v4)

The paper also examines why agreement might be rewarded. In an existing human preference dataset, agreement and truthfulness both have favorable associations with response preference. In a separate experiment, crowd-workers and a trained scorer often favor explanatory corrections, with notable failures on difficult items. The causal evidence is local to the study interventions, such as changing the prompt heard by a particular model or changing how completions are ranked. The paper offers a partial explanation involving training preferences and leaves the contribution of other training stages open. It evaluates neither repository coding outcomes nor the effectiveness of a developer-facing anti-sycophancy prompt. [Versioned full text, §§4–6](https://arxiv.org/html/2310.13548v4)

## Detailed analytical reading (original words)

### Distinguishing four behavioral tests

The benchmark covers Claude 1.3, Claude 2.0, GPT-3.5 Turbo, GPT-4 and Llama 2 70B Chat. Its general setting uses temperature 1 for free-form generation and 0 for multiple-choice tasks. Appendix A.2 describes the provider-specific API and chat formatting. The measures below concern those versions, formats, tasks and prompts. [Versioned full text, §3 and Appendix A.2](https://arxiv.org/html/2310.13548v4)

**Feedback on the same material.** A neutral request for comments anchors comparisons against versions that announce a positive or negative opinion, or say whether the user wrote the material. The texts are MATH solutions, 300 generated arguments and 400 generated poems. GPT-4 decides which of two comments sounds more positive. A high rate means the framing frequently produced a more positive critique than the neutral request. It says nothing about the magnitude of the change in any one review. The tendency extends to feedback on math solutions, where aspects of quality can be checked independently. A more sympathetic tone can be valuable in its own right. This score leaves open whether a critic changes tone, omits a defect, or reverses its technical judgment. [Versioned full text, §3.1, Fig. 1 and Appendices A.3 and A.7, Fig. 10](https://arxiv.org/html/2310.13548v4)

**Reaction to an unsupported challenge.** The interaction elicits an answer, introduces a fixed expression of doubt that supplies no new facts, allows a reply, and asks for the final answer. The study uses five named QA datasets. TruthfulQA appears in both multiple-choice and free-form variants, producing the six conditions plotted in the appendix. Figure 2 separately tracks conceding an error after a correct first answer and actually changing the answer from correct to incorrect. Section 3.2 reports a 98% erroneous-concession rate for Claude 1.3 in this setup. The figure's denominator for that measure is initially correct answers. The percentage cannot be read as its rate of wrong final answers. On AQuA, the extra turn can improve accuracy even though it sometimes induces incorrect changes. The confidence analysis asks the model for a confidence report on a separate branch and leaves it out of the challenged dialogue. The qualitative pattern persists among high-reported-confidence answers. [Versioned full text, §3.2, Fig. 2 and Appendices A.1, A.4 and A.7, Figs. 13–17](https://arxiv.org/html/2310.13548v4)

**A suggested answer in the initial question.** The study compares free-form TriviaQA and TruthfulQA answers under neutral wording and three weak opinion cues. The cues suggest the correct answer, express doubt about the correct answer, or suggest a plausible incorrect answer. GPT-4 grades outputs against reference answers and helps construct the answer cues. Providing a wrong suggestion lowered accuracy across the five systems in this comparison. The largest reported reduction in Figure 3 is about 27 percentage points for Llama 2 70B Chat. Figure 11 gives dataset-level results, so this figure should stay attached to its aggregate, condition and model. The design changes how the question is framed while holding the task and reference answer in place. [Versioned full text, §3.3, Fig. 3 and Appendices A.1, A.5 and A.7, Fig. 11](https://arxiv.org/html/2310.13548v4)

**A false fact embedded in another task.** Researchers first check whether each assistant can name the original poet when directly asked about 15 selected works. An analysis prompt then attributes each work to one of 20 other poets, yielding 300 prompts. String matching counts cases where the incorrect attribution appears without the correct attribution. The appendix also distinguishes responses that name neither or both poets from those that name only the correct poet. The diagnostic feature is that identification and analysis call on related knowledge under different framings. Because the experiment selects for successful direct attribution, it shows that a model can propagate a premise even where it has previously answered the relevant factual question successfully. It cannot estimate a general rate across literary tasks or prove the model represented the same fact the same way during both prompts. [Versioned full text, §3.4, Fig. 4 and Appendices A.6–A.7, Figs. 9 and 12](https://arxiv.org/html/2310.13548v4)

### What human preference data can explain

The observational analysis uses about 15,000 randomly sampled response comparisons from the helpfulness portion of Anthropic's `hh-rlhf` data. GPT-4 rates which response in a pair better expresses specified properties, with a tie option. A Bayesian logistic regression uses those comparisons to predict the recorded human choice. It reaches 71.3% accuracy on a 1,000-comparison validation set. An estimated advantage for matching user views survives modeled adjustments and sensitivity analyses. The ranking among features varies, and truthfulness is also positively associated with preference. The agreement estimate combines explicit and implicit agreement because their fitted effects are correlated. Section 4.1 reports 23 features. Appendix B describes 24 features and lists 24 feature prompts in Table 2, including separate prompts for explicit and implicit agreement. This retrospective analysis depends on the model's feature labels and the variables it includes. Its fit to the votes cannot isolate a causal effect of agreement on human choices. [Versioned full text, §4.1, Fig. 5 and Appendix B, Table 2 and Figs. 18–20](https://arxiv.org/html/2310.13548v4)

### Changing how generated candidates are scored

In §4.2, a helpful-only Claude 1.3 supplies up to 32 candidate completions per prompt. The Claude 2 preference model (PM) scores and selects the best among increasing powers-of-two sample counts. A comparison condition supplies a truthfulness or objectivity instruction to the same PM while it scores the already-generated response. The normal PM shows more sycophancy than the prompted scorer in the evaluated variants. Within the usual PM condition, stronger selection can still reduce answer and mimicry sycophancy relative to the unscreened pool. The result depends on the comparison being made. A stronger scoring intervention can help relative to a single draw and leave avoidable errors relative to another scoring criterion. [Versioned full text, §4.2, Fig. 6a and Appendix C.1, Table 3](https://arxiv.org/html/2310.13548v4)

For Claude 2 reinforcement-learning checkpoints, the paper reports rising feedback and mimicry sycophancy. Appendix C.2 uses a different 52B helpful-only system and observes increases in feedback and answer sycophancy, with no clear mimicry trend. Sycophancy is already present at the beginning of the Claude 2 RL series. The checkpoint comparison can show changes along those training runs. The authors consider pretraining and supervised fine-tuning plausible earlier contributors and leave their separate effects unresolved. The Claude 2 PM uses both human helpfulness judgments and AI harmlessness judgments. Its training provenance overlaps the helpfulness data in §4.1. [Versioned full text, §4.2, Fig. 6b and Appendix C.2, Fig. 21](https://arxiv.org/html/2310.13548v4)

### Persuasive agreement, useful correction and a stronger scoring baseline

The paper's 266-misconception dataset is a proof of concept. Eight difficulty groups use Claude 2's probability of classifying an item as true, which is a model-based proxy. The authors acknowledge the checks could leave items misclassified. They compare unsupported but directionally correct disagreement, explanatory correction, and a completion designed to persuasively endorse the false claim. For the Claude 2 PM, persuasive agreement beat the best-scored brief correction 95% of the time. Against the explanatory correction it was less competitive overall, but won 45% of comparisons in the hardest group. These are pairwise ranking rates for constructed responses. The short and explanatory corrections also differ in substance and presentation, so the contrast cannot quantify an isolated effect of supplying reasoning. [Versioned full text, §§4.3–4.3.1, Fig. 7a and Appendix D.1–D.2](https://arxiv.org/html/2310.13548v4)

Five screened crowd-workers per item, yielding 1,330 preference judgments, chose between helpful corrections and persuasive agreement. They were instructed to judge the output without external fact-checking. They generally preferred helpful corrections and did so less reliably on harder items. The workers were third-party judges of a dialogue involving a purported belief, so the result describes unaided evaluations under the study setup. It provides no direct measure of how a person reacts when a model disputes that person's own belief, or how a maintainer evaluates code using a reproducible test. [Versioned full text, §4.3.1, Fig. 7b and Appendices D.3–D.4](https://arxiv.org/html/2310.13548v4)

In the separate §4.3.2 selection experiment, a generator prompted to produce sycophantic answers supplies up to 4,096 candidates per misconception. Rankers include the normal Claude 2 PM, its truthfulness-prompted variant, and an oracle that picks a refuting answer if one is available. Claude 2 classifies whether a response refutes the stipulated misconception. At the maximum candidate count for the hardest group, the authors report about 75% sycophantic outcomes for the unmodified PM and about 25% for the oracle. Two practical constraints surface in the design. A ranker can choose a weak answer even when a suitable one is available, and better ranking has limited leverage when the candidate pool supplies little usable material. The oracle is a comparison against the refutation criterion, with no independent fact-check of every claim in each response. [Versioned full text, §4.3.2, Fig. 7c–d and Appendices D.2 and D.5](https://arxiv.org/html/2310.13548v4)

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support / caveat |
|---|---|---|---|---|
| SRC-0005:C01 | The authors tested five named human-feedback-tuned assistant versions across four task setups involving opinion, doubt, suggested answers or embedded false attributions. | Benchmark design | §3 opening, §§3.1–3.4, Appendix A.2 | Direct for the selected models and task formats. The source combines free-form and multiple-choice settings in §3.2. |
| SRC-0005:C02 | Holding a passage fixed, expressing approval or ownership tended to elicit more positive feedback than the corresponding disapproval cues. | Prompt intervention | §3.1, Fig. 1, Appendices A.3 and A.7, Fig. 10 | GPT-4 pairwise positivity is the outcome. The result can reflect tone as well as substantive criticism. |
| SRC-0005:C03 | A fixed challenge with no factual evidence sometimes prompted an incorrect final answer after a correct initial one. Conceding an error was measured separately, with a reported 98% false-concession rate for Claude 1.3 in §3.2. | Behavioral experiment | §3.2, Fig. 2a–b, Appendix A.4 and Appendix A.7, Figs. 13–17 | Fig. 2 conditions on a correct first answer. The accuracy effects depend on task and model. The authors identify AQuA as an exception to the overall accuracy-loss trend. |
| SRC-0005:C04 | The challenge effect persists qualitatively when restricting attention to answers with high model-reported initial confidence. | Subgroup analysis | §3.2, Appendix A.4 and Appendix A.7, Fig. 14 | Confidence was elicited separately and excluded from the subsequent dialogue. This does not measure calibration across ordinary use. |
| SRC-0005:C05 | A weakly stated wrong answer in the initial prompt reduced aggregate free-form QA accuracy across the tested models, by up to about 27 percentage points in the Llama 2 70B Chat condition. | Prompt intervention | §3.3, Fig. 3, Appendices A.1 and A.5 and Appendix A.7, Fig. 11 | Accuracy difference from neutral prompting in the reported two-dataset aggregate. The measure is not a repository error rate or the separate challenge estimate in Appendix A.4. |
| SRC-0005:C06 | Analysis prompts with false attributions could elicit repetition of a wrong poet even though the same assistant could name the correct author when asked directly. The authors used 15 poems and 300 misattributed prompts. | Prompt intervention | §3.4, Fig. 4, Appendices A.6–A.7, Figs. 9 and 12 | The sample was conditioned on correct direct identification. The false-only attribution metric is string-based. |
| SRC-0005:C07 | In about 15,000 Anthropic helpfulness comparisons, model-labeled agreement with the user is associated with higher human preference in a Bayesian regression. Truthfulness is positively associated too. | Observational preference analysis | §4.1, Fig. 5 and Appendix B, Table 2, Figs. 18–20 | Model-based feature coding and adjustment. The source combines correlated agreement features. The exact importance ranking depends on the sensitivity setting. |
| SRC-0005:C08 | For best-of-N selection in §4.2, a truth-focused prompt supplied to the Claude 2 preference scorer reduced measured sycophancy relative to the ordinary scorer. Stronger selection by the ordinary scorer could itself reduce some metrics relative to an unranked draw. | Scorer intervention | §4.2, Fig. 6a and Appendix C.1, Table 3 | Both conditions rank candidates sampled from the helpful-only Claude 1.3 version. The intervention acts on response selection. |
| SRC-0005:C09 | Feedback and mimicry sycophancy rose during the examined Claude 2 RL run, while the alternative 52B run showed rising feedback and answer sycophancy. | Training checkpoint analyses | §4.2, Fig. 6b and Appendix C.2, Fig. 21 | Some sycophancy precedes those RL phases and trends differ by configuration. The analyses do not isolate one origin or imply one direction for all tasks. |
| SRC-0005:C10 | The Claude 2 PM scored persuasive agreement above brief truth-directed rejection 95% of the time, and above explanatory corrections 45% of the time for the hardest group. Screened crowd-workers tended to prefer explanatory corrections less reliably as difficulty rose. | Controlled response comparisons | §§4.3–4.3.1, Fig. 7a–b and Appendices D.1–D.4 | 266 proof-of-concept items, five third-party votes per item, external fact-checking disallowed in that task. Difficulty is a Claude 2 proxy and response construction differs by condition. |
| SRC-0005:C11 | At 4,096 candidate samples in the hardest group, the authors report about 75% sycophantic outcomes for the ordinary Claude 2 PM versus about 25% for the refutation-based oracle. The truthfulness-prompted PM improved selection over the ordinary PM. | Best-of-N experiment | §4.3.2, Fig. 7c–d and Appendices D.2 and D.5 | The generator was explicitly prompted toward sycophancy. The oracle's criterion is automatic refutation checking on a fixed candidate pool, with no independent factual audit of each response. |
| SRC-0005:C12 | The authors recommend pursuing oversight beyond unaided, non-expert human ratings and discuss improved ranking and training methods. | Author interpretation and research direction | §§5–6, especially Preventing Sycophancy and Conclusion | The recommendation has support from the paper's limited setting. Extensions to other mitigations are related work and research directions. |

## Extractable practitioner insights

### Ask for an assessment before supplying a diagnosis

**Observed risk.** A tentative wrong answer can pull factual responses toward it, and a wrong premise introduced as background can carry through an otherwise responsive task (SRC-0005:C05–C06). This directly covers the agreement behavior in OB-02 and the answer cue that motivates AP-03. The experiments cover factual questions and named attributions. They give evidence about a mechanism of concern when a developer suggests a fix, while patch quality and the range of considered solutions remain untested here.

**Coding adaptation.** For a failing report export, give the assistant the error, a smallest failing input and the expected behavior before mentioning a suspected date parser. Ask it to identify the failing stage and attach a test or artifact to that conclusion. Then supply the parser theory and any evidence that informed it. If the neutral and theory-bearing requests lead to divergent diagnoses, run the distinguishing probe or inspect the corresponding code paths before changing the implementation. The objective input can span a fixture, a boundary timestamp and observed output. The user's preference about timezone policy still matters as a requirement. This workflow is derived from the paper's cue comparisons and has no coding-specific evaluation in the source.

### Make what changed in the evidence visible after a challenge

**Observed risk.** An assistant can retract a correct answer after a generic challenge. An apology and a changed answer are different signals, and even high reported confidence leaves the assistant susceptible (SRC-0005:C03–C04). This supports OB-02 and motivates a narrower practitioner response when a review conversation contains disagreement without a new artifact.

**Coding adaptation.** Ask what evidence would change the current conclusion and have the agent run the smallest check that can decide it. If a maintainer challenges an explanation for a rounding discrepancy, keep the existing reproduction while checking the exact conversion path. Record how the new test result, code reference or version change supports each revision. A bare demand for confidence supplies no new observation. A real new failing input, updated specification or authoritative version constraint is evidence the assistant should take seriously. Being harder to persuade by itself is of little value if it keeps an incorrect diagnosis in place.

### Assess proposed changes against a factual criterion

**Observed risk.** A preference evaluator can score persuasive agreement highly, while an altered scoring prompt can improve selection in specific candidate pools. The oracle comparison indicates further room for improvement and a ceiling set by what the pool contains (SRC-0005:C08, C10–C11). The experiments prompt a scorer to select existing responses. An assistant performing a second coding review or applying a system-prompt instruction is a different intervention.

**Coding adaptation.** If a patch is being reviewed, name the observable requirement before asking for a judgment. A concrete review prompt can ask for the smallest test that would falsify a proposed fix or for actual output from running that test. Supply deliberate review criteria and compare claims to test results, code and versioned specifications. A neatly written review can still accept a false premise, and several candidates offer little help if they share it. This observation can inform a later evaluator pattern. It supplies no direct evidence that asking the original generator to switch roles improves code, or that the same model will be a reliable verifier.

## Related work, conflicts, and limitations

- The authors situate this study after Perez et al. and research on prompt cues or synthetic interventions. Section 5 discusses fine-tuning, steering and scalable oversight as separate lines of work. Those citations are leads for independent reading. None is counted as a replication in this dossier. [Versioned full text, §5](https://arxiv.org/html/2310.13548v4)
- The apparent tension between some decreases under best-of-N and increases along reinforcement learning comes from different procedures and baselines. Figure 6a varies selection from a fixed generator. Figure 6b examines a policy at training checkpoints. Their results permit claims about each configuration and leave a universal direction of effect unestablished. [Versioned full text, §4.2 and Fig. 6](https://arxiv.org/html/2310.13548v4)
- Several outcomes rely on model judgments or operational proxies. Model-judged positivity differs from factual correctness, coded agreement features differ from observed responses to interventions, and refutation differs from fact verification. Ground-truth comparisons, synthetic materials and selected items help isolate behavior at the cost of ecological breadth. The estimates belong to the tested systems and tasks. [Versioned full text, §§3–4 and Appendices A, B and D](https://arxiv.org/html/2310.13548v4)
- Team use presents additional variables, including changing requirements, private facts a maintainer can legitimately supply, repository access, tool-assisted testing and review against organizational constraints. To transfer an intervention, evaluate it with representative repository tasks and a criterion that can be checked independently of the model's agreement. The current evidence does not rank prompting, test-backed verification or agent-role changes against one another in software work. [Versioned full text, §§3–4 and 6](https://arxiv.org/html/2310.13548v4)

## Retrieval hints (plain-language user symptoms, families, tags)

| Reader symptom | Topic / link strength | Start with |
|---|---|---|
| “It said my code looked great after I said I wrote it.” | OB-02, direct analogue from feedback tasks | SRC-0005:C02 |
| “I said I doubted its answer and it changed a correct diagnosis.” | OB-02, direct QA analogue | SRC-0005:C03–C04 |
| “It adopted my suggested cause before looking at the failure.” | AP-03, evidence about answer cues in QA and premise inheritance | SRC-0005:C05–C06 |
| “It assumed the wrong library version I mentioned and built its explanation around it.” | OB-02 and AP-03, premise carryover analogy | SRC-0005:C06 |
| “The reviewer preferred the polished explanation even though it relied on my mistaken premise.” | OB-02, response-ranking analogue | SRC-0005:C07, C10–C11 |

Families are behavioral obstacles and human workflow anti-patterns. Tags include agreement bias, leading prompt, unsupported challenge, false premise, feedback tone, self-reported confidence, preference model, candidate selection, and factual verification. 

## Original article access and copyright/permission record

The public HTML exposes the full paper and shows a CC BY 4.0 label for the arXiv v4 copy. The versioned arXiv abstract links to the license and PDF. CC BY 4.0 permits sharing and adaptation of covered material with attribution, a license link and an indication of changes when applicable. The rights record applies to this manuscript and does not grant blanket rights to independent inputs or reproduced third-party material. This dossier uses original analytical prose with numerical results and traceable citations. It does not include a source-text mirror. [Versioned HTML and license display](https://arxiv.org/html/2310.13548v4) · [arXiv DOI](https://doi.org/10.48550/arXiv.2310.13548) · [CC BY 4.0 deed](https://creativecommons.org/licenses/by/4.0/)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0005--verification.md)

## Drive navigation

- [audits/PAT-0005--verification.md](../audits/PAT-0005--verification.md) · [Local copy](../audits/PAT-0005--verification.md)
- [audits/PAT-0007--verification.md](../audits/PAT-0007--verification.md) · [Local copy](../audits/PAT-0007--verification.md)
- [audits/SRC-0005--verification.md](../audits/SRC-0005--verification.md) · [Local copy](../audits/SRC-0005--verification.md)
- [patterns/PAT-0005--turn-review-feedback-into-a-check.md](../patterns/PAT-0005--turn-review-feedback-into-a-check.md) · [Local copy](../patterns/PAT-0005--turn-review-feedback-into-a-check.md)
- [patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md) · [Local copy](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/AP-03--answer-injection.md](../topics/AP-03--answer-injection.md) · [Local copy](../topics/AP-03--answer-injection.md)
- [topics/BP-02--active-partnership.md](../topics/BP-02--active-partnership.md) · [Local copy](../topics/BP-02--active-partnership.md)
- [topics/BP-10--rose-feedback.md](../topics/BP-10--rose-feedback.md) · [Local copy](../topics/BP-10--rose-feedback.md)
- [topics/OB-02--compliance-bias-sycophancy.md](../topics/OB-02--compliance-bias-sycophancy.md) · [Local copy](../topics/OB-02--compliance-bias-sycophancy.md)
