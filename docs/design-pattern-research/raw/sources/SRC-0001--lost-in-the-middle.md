---
source_id: SRC-0001
status: accepted
original_title: "Lost in the Middle: How Language Models Use Long Contexts"
authors: ["Nelson F. Liu", "Kevin Lin", "John Hewitt", "Ashwin Paranjape", "Michele Bevilacqua", "Fabio Petroni", "Percy Liang"]
publisher: "MIT Press"
source_type: empirical_paper
published: "2024-02-19"
updated: unknown
accessed: "2026-11-21"
original_url: "https://aclanthology.org/2024.tacl-1.9/"
source_version: "Journal version of record, TACL 12, pp. 157–173, DOI 10.1162/tacl_a_00638"
full_text_reuse: authorized
reuse_license: "CC BY 4.0"
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [AP-08, BP-06, OB-01, OB-10]
related_patterns: [PAT-0001]
review: PASS
publication_status: published
---

# Lost in the Middle: How Language Models Use Long Contexts

## Provenance and scope read

- The ACL Anthology bibliographic record identifies the title, seven authors in the order above, MIT Press, volume 12 of *Transactions of the Association for Computational Linguistics*, pages 157–173 and DOI `10.1162/tacl_a_00638`. The TACL journal's own article record gives the publication date as February 19, 2024. The first page of the issue PDF specifies February 2024 at month precision. [ACL Anthology record](https://aclanthology.org/2024.tacl-1.9/) · [TACL journal record](https://transacl.org/index.php/tacl/article/view/5757) · [Published PDF, p. 157](https://aclanthology.org/2024.tacl-1.9.pdf#page=1)
- Scope was the publicly accessible 17-page journal PDF, including the introduction, both benchmarks, the three follow-up comparisons, open-domain case study, related work, conclusion, acknowledgments, references and Appendices A–E. The reading used the PDF's searchable text, including its figure captions and Table 1. Numbers quoted below are reported in prose or tables. Experiments and underlying datasets were outside this reading. [Published PDF](https://aclanthology.org/2024.tacl-1.9.pdf)
- This is a peer-reviewed benchmark study whose authors list affiliations at Stanford, UC Berkeley and Samaya AI. The first-page footnote notes work undertaken partly during an internship at Samaya AI. The acknowledgments report Stanford CRFM support, OpenAI API credits through a grant to Stanford CRFM and access via Anthropic's academic program. Model providers therefore supported access to systems included in the evaluation. [Published PDF, p. 157](https://aclanthology.org/2024.tacl-1.9.pdf#page=1) · [Acknowledgments, p. 167](https://aclanthology.org/2024.tacl-1.9.pdf#page=11)

## Reader's orientation

A model can receive the paragraph that answers a question and still perform worse if that same paragraph is moved into the middle of the supplied material. Liu et al. estimate this effect by keeping the expected answer fixed while moving the evidence, and by changing the amount of surrounding material. The distinction matters when evaluating a coding assistant that reports having read a long transcript, file bundle or tool result. The experiments measure answer or lookup accuracy in individual prompts. Multi-turn instruction retention, repository edits and the effect of a session reset require separate evidence. [§§1–3, pp. 157–163](https://aclanthology.org/2024.tacl-1.9.pdf#page=1)

## Detailed analytical reading

### What the controlled comparison holds fixed

The first task uses 2,655 NaturalQuestions-Open items whose annotated long answer is a paragraph. Each prompt supplies one designated answer paragraph from Wikipedia and, for a 10-, 20- or 30-document condition, fills remaining slots with retrieved passages filtered against annotated answer strings. The default distractors are semantically plausible because they come from a query-conditioned Contriever retrieval step and are ranked by decreasing relevance. Moving the answer paragraph changes where the useful evidence appears while preserving the other documents for that example and length. Increasing document count adds distractors. Eligibility depended on model input limits. The study uses greedy decoding and counts a response as correct if it contains any annotated answer. That metric leaves citation quality, use of an irrelevant document and the quality of any accompanying explanation outside the measured outcome. [§§2.1–2.3, Figs. 2–5 and Table 1, pp. 159–162](https://aclanthology.org/2024.tacl-1.9.pdf#page=3)

The two baselines distinguish prior knowledge from access to especially clean evidence. Closed-book prompts give the question without documents, while oracle prompts give only the designated answer passage. Standard GPT-3.5-Turbo scores 56.1% and 88.3% respectively on these baselines, and the 16K variant scores 56.0% and 88.6%. Section 2.3 describes worst placements in the 20- and 30-document conditions falling below the 56.1% benchmark under the GPT-3.5-Turbo family name. Figure 5 plots the 16K variant alone in the 30-document panel for that family. The stronger placement conditions form the ends of a U-shaped curve for many of the models. In the overlapping 10- and 20-document settings, position-performance curves for standard and 16K GPT-3.5-Turbo are nearly superimposed. For these versions, a larger advertised window expands what fits, while adding little difference to performance on those shared inputs. [§2.3, Fig. 5 and Table 1, pp. 161–162](https://aclanthology.org/2024.tacl-1.9.pdf#page=5)

The appendices probe whether distracting text or the ranking convention alone explains the pattern. With ambiguity-filtered questions, the position trend remains. Replacing retrieved distractors with random Wikipedia passages improves overall accuracy while leaving a position effect. Shuffling retrieved distractors and telling the model about the shuffle also leaves a middle dip. These conditions support taking the position effect seriously even where the obvious relevance and ordering confounds are reduced. A separate GPT-4 (8K) experiment, on 500 randomly sampled 20-document examples, retains a dip with higher overall scores. Appendix E shows a different curve shape for the 7B Llama-2 versions, whose preference is chiefly for recent evidence, alongside U-shaped curves for the tested 13B and 70B versions. [Apps. A–E, Figs. 12–16, pp. 171–173](https://aclanthology.org/2024.tacl-1.9.pdf#page=15)

### Simple lookup and passage interpretation respond differently to the same prompt change

The second benchmark serializes a JSON object of unique random UUIDs and asks for the value associated with one key. It uses 500 examples per tested size of 75, 140 or 300 pairs and scores whether the requested value appears in the output. The task removes most semantic interpretation, leaving exact identification and reproduction from a long input. Claude-1.3 and Claude-1.3 (100K) score nearly perfectly at evaluated lengths, whereas the tested GPT-3.5-Turbo variants and MPT-30B-Instruct have middle-position lows. The authors also observe a distinct LongChat-13B (16K) failure at 140 pairs near the start. It tends to return code for retrieving the value, which the scoring procedure does not execute. This is one reason to treat accuracy as an observable task outcome rather than a direct measurement of internal recall. [§§3.1–3.2, Figs. 6–7, pp. 162–163](https://aclanthology.org/2024.tacl-1.9.pdf#page=6)

The original layout puts the query after the data. Section 4.2 places the query on both sides of the same data, so a decoder-only model can condition its intermediate representations on query tokens while processing the intervening material. The change lifts GPT-3.5-Turbo (16K) from a 45.6% worst-position score to perfect performance in its 300-pair lookup condition. In passage-based QA, the same change offers a small gain for evidence at the very start and small declines elsewhere. A practitioner testing where to place a lookup key has a stronger reason to try this layout than one evaluating a query about the meaning of several files. The experiment compares adding a leading query while keeping the trailing one. The effect of moving the query to the front and omitting its final copy remains unmeasured in that comparison. [§4.2, Figs. 7 and 9, pp. 163–165](https://aclanthology.org/2024.tacl-1.9.pdf#page=7)

### Model and training comparisons set bounds on the finding

Flan-UL2 varies by 1.9 percentage points across best and worst evidence positions when evaluated inside its 2,048-token encoder training limit. Middle placement becomes a liability beyond that length. Flan-T5-XXL shows larger degradation as inputs extend beyond its shorter training regime. The authors suggest that a bidirectional encoder may help rank information by letting the representation of a passage account for what follows it. Model and training settings differ in this comparison, so the explanation remains a hypothesis. Similarly, the base MPT-30B and MPT-30B-Instruct share a U-shaped curve even though instruction tuning improves scores and reduces the reported gap in that pair. Appendix E finds a tuning-related reduction for the 13B Llama-2 variant and comparatively little position-effect change at 70B. Absolute accuracy, worst-position accuracy and the difference between best and worst positions consequently answer different evaluation questions. [§§4.1, 4.3, Figs. 8 and 10, pp. 163–166](https://aclanthology.org/2024.tacl-1.9.pdf#page=7) · [App. E, Fig. 16, pp. 172–173](https://aclanthology.org/2024.tacl-1.9.pdf#page=16)

### When retrieval keeps improving but answers plateau

The open-domain case study relaxes the controlled benchmark's assumption that the prompt always includes one designated answer paragraph. The researchers forward top-ranked Wikipedia retrieval results as context and track both recall and reader answer accuracy by document count. Moving from 20 to 50 passages improves reader accuracy by approximately 1.5 percentage points for GPT-3.5-Turbo (16K) and 1 point for Claude-1.3 (100K), with recall still improving. The practical question is whether any additional answer coverage benefits the task enough to justify reading all the additional material. The authors identify better ranking toward the beginning of the input and cutting the list where appropriate as promising next directions. Figure 11 measures the number of retrieved passages under the case study's ranking setup. It leaves the performance of a proposed reranker and the choice of an optimal cutoff open. [§5, Fig. 11, p. 166](https://aclanthology.org/2024.tacl-1.9.pdf#page=10)

## Claim-level evidence ledger

| Claim ID | Source-supported proposition | Nature | Exact source locator | Support and scope |
|---|---|---|---|---|
| SRC-0001:C01 | The QA setup varies answer position and distractor count over 2,655 NaturalQuestions-Open questions selected for paragraph long answers. Any annotated answer in the generated text counts toward accuracy. | Experimental method | [§2.1, Figs. 2–4, pp. 159–160](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) | Direct. One designated supporting paragraph per controlled example. Temporal ambiguity can leave some plausible answers in distractors. |
| SRC-0001:C02 | In the 10-, 20- and 30-document experiment, many models use evidence less successfully in the middle than at the first or last document position. Section 2.3 reports worst placements in the 20- and 30-document conditions below the standard GPT-3.5-Turbo closed-book benchmark of 56.1%. The 30-document plot shows only the 16K variant for this model family. | Empirical result | [§2.3, Fig. 5 and Table 1, pp. 161–162](https://aclanthology.org/2024.tacl-1.9.pdf#page=5) | Direct for tested positions and model variants where input fits. Table 1 gives distinct closed-book and oracle baselines for standard GPT-3.5-Turbo (56.1% and 88.3%) and the 16K variant (56.0% and 88.6%). |
| SRC-0001:C03 | GPT-3.5-Turbo and its 16K version have nearly coincident position curves when both can handle the 10- and 20-document inputs. | Empirical result | [§2.3, Fig. 5, pp. 161–162](https://aclanthology.org/2024.tacl-1.9.pdf#page=5) | Direct for the tested 0613 versions and overlapping conditions. |
| SRC-0001:C04 | The UUID lookup benchmark tests 75, 140 and 300 pairs with 500 examples per size. Claude-1.3 variants achieve nearly perfect retrieval at evaluated lengths. Several other models dip in the middle, and LongChat-13B (16K) sometimes emits lookup code near the start in the 140-pair condition. | Experimental method and empirical result | [§§3.1–3.2, Figs. 6–7, pp. 162–163](https://aclanthology.org/2024.tacl-1.9.pdf#page=6) | Direct for simple lookup. The code-output observation is qualitative. |
| SRC-0001:C05 | The supported-length Flan-UL2 condition shows a 1.9-point best–worst spread. Flan-UL2 and Flan-T5-XXL become more position-sensitive as inputs extend beyond their training lengths. | Empirical result | [§4.1, Fig. 8, pp. 163–164](https://aclanthology.org/2024.tacl-1.9.pdf#page=7) | Direct in the studied models. An architectural explanation is tentative. |
| SRC-0001:C06 | Adding a copy of the final query before the data brings GPT-3.5-Turbo (16K) to perfect 300-pair UUID retrieval, versus its previous worst placement of 45.6%. QA shows only small gains at the first position and small decreases elsewhere. | Empirical result | [§4.2, Figs. 7 and 9, pp. 163–165](https://aclanthology.org/2024.tacl-1.9.pdf#page=7) | Direct for the two tested layouts and tasks. The contrast constrains general advice to repeat the query. |
| SRC-0001:C07 | Base MPT-30B exhibits the same overall U-shaped position curve as its instruction-tuned counterpart, with lower absolute scores. | Empirical result | [§4.3, Fig. 10, pp. 164–165](https://aclanthology.org/2024.tacl-1.9.pdf#page=8) | Direct for this comparison. The curve can occur without instruction tuning. |
| SRC-0001:C08 | In a separate NaturalQuestions-Open retrieval-and-reading case study, increasing the passage count from 20 to 50 improves answer accuracy by approximately 1.5 points for GPT-3.5-Turbo (16K) and 1 point for Claude-1.3 (100K), while recall continues to improve. | Empirical result | [§1, p. 159](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) · [§5, Fig. 11, p. 166](https://aclanthology.org/2024.tacl-1.9.pdf#page=10) | Direct for this ranking, dataset and the model variants named in the figure legend. A universal document cutoff is outside the evidence. |
| SRC-0001:C09 | The authors propose more effective reranking to bring relevant passages toward the front, or cutting the ranked list when appropriate, as promising ways to improve use of retrieved material. | Author proposal | [§5, final paragraph, p. 166](https://aclanthology.org/2024.tacl-1.9.pdf#page=10) | Supporting for selecting useful context. The paper leaves those interventions for subsequent evaluation. |
| SRC-0001:C10 | QA position effects persist with an ambiguity-filtered subset, randomly selected distractors and shuffled retrieved distractors accompanied by a cue about the order. | Empirical robustness checks | [Apps. A–C, Figs. 12–14, pp. 171–172](https://aclanthology.org/2024.tacl-1.9.pdf#page=15) | Direct in the variants tested. Random passages make the benchmark easier, and the shuffle and prompt cue are combined in App. C. |
| SRC-0001:C11 | GPT-4 (8K) retains a middle dip on 500 sampled 20-document QA examples. Tested Llama-2 7B models predominantly favor recency, while 13B and 70B variants have U-shaped curves. | Empirical scope checks | [Apps. D–E, Figs. 15–16, pp. 172–173](https://aclanthology.org/2024.tacl-1.9.pdf#page=16) | Direct for the indicated subsets and checkpoints. Position-effect shape varies with model and condition. |
| SRC-0001:C12 | The authors propose testing performance with evidence at different positions and assessing the best–worst gap as part of evaluating long-context robustness. | Author evaluation recommendation | [§1, final paragraph, p. 159](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) · [§7, p. 167](https://aclanthology.org/2024.tacl-1.9.pdf#page=11) | Direct for the proposed benchmark criterion. A workflow built around this idea should pick its own task-appropriate success measure. |

## Extractable practitioner insights

### Probe whether important evidence is usable in a long brief

**Study precedent.** Vary the position of the evidence while preserving the answer and judge performance across positions. A strong result at one position leaves other positions untested. `SRC-0001:C01`, `SRC-0001:C02`, `SRC-0001:C03`, `SRC-0001:C10`, `SRC-0001:C11`, `SRC-0001:C12`.

**Coding-workflow adaptation.** When a long investigation packet already contains the rule for deciding which module owns a compatibility change, ask the assistant to identify that rule, cite its file location and explain which module it implies before permitting edits. If the answer is wrong or vague, try the same question with the same evidence order except for moving the governing passage to the front, then compare both answers with the checked-in file. A single improved answer suggests trying the layout with more representative tasks. Repository state, conflicting instructions, missing material and assistant variation can independently influence results. This supports part of **OB-01** and the position effect in **OB-10**. 

### Choose supporting context for its value to the current decision

**Study precedent.** In the open-domain question-answering case, additional material continued to improve retrieval recall after answer accuracy had largely leveled off. The authors suggest ranking and selectively stopping as possible responses. `SRC-0001:C08`, `SRC-0001:C09`.

**Coding-workflow adaptation.** For a decision about whether a small behavior change passes an interface contract, try a brief containing the relevant contract, the implementation path and a representative test. Retain locators to the rest of the repository so the assistant can retrieve additional material if the narrow brief cannot resolve a dependency, a conflicting contract or a counterexample. Local validation is needed because disposing of a document also removes any evidence available only there. This supports **BP-06** and the distractor-load component of **OB-10**. The study's retrieval plateau cannot set an assistant's ideal context budget.

### Test prompt layout on the operation people actually need

**Study precedent.** Query duplication around the data yielded very different benefits for exact UUID lookup and Wikipedia QA. `SRC-0001:C04`, `SRC-0001:C06`.

**Coding-workflow adaptation.** Put a precise lookup question near the data when evaluating a long response that contains one identifier or configuration value, and verify the returned value against the file. For a cross-file interpretation, check that the explanation accounts for each relevant file. Probe each operation on its own examples before treating a layout as standard practice for **BP-06**.

## Related work, conflicts, and limitations

- The paper relates its controlled QA to the needle-placement experiments of Ivgi et al. in §2.1 and places the result alongside earlier recency studies in §§4.3 and 6. Experiments inside this paper count as one publication. Related-work results mentioned here require their own primary-source verification before counting as independent support. The analogy to serial-position effects in humans in §6.3 does not establish a shared mechanism. [§2.1, pp. 159–160](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) · [§§6.2–6.3, p. 167](https://aclanthology.org/2024.tacl-1.9.pdf#page=11)
- Evidence is strongest for **OB-10**, where the tasks directly manipulate position and add distractors. For **OB-01**, the single-prompt experiments support performance degradation while relevant material is still in the input. Persistence of an earlier instruction across turns, the effects of automatic conversation compaction and fixed context quality zones remain open. For **BP-06**, the proposed coding practices are adaptations, informed by the benchmark and its limited prompt intervention. [§§2–5, pp. 159–166](https://aclanthology.org/2024.tacl-1.9.pdf#page=3)
- The evaluated releases and tasks define the evidence boundary. The paper measures short-answer presence or exact-value presence, mainly with greedy decoding. Results for current coding agents with tools, cross-file dependencies, changing state and multiple interdependent constraints require validation in that setting. Strong simple-retrieval results can coexist with a position effect in semantic question answering. [§§2.1–2.2, 3.1 and 4.2](https://aclanthology.org/2024.tacl-1.9.pdf#page=3)

## Retrieval hints

- “The relevant rule is in the prompt, but the agent missed it.”
- “The answer improves when I bring the same note closer to the start or end.”
- “A bigger context window fits all my files, but the answers are still weak.”
- “The assistant found the identifier but missed how the contract applies.”
- Families and tags: context management, long context, position effects, recency, evidence retrieval, distractors, task-specific evaluation.

## Original article access and copyright record

The ACL Anthology PDF is the open journal copy used for this dossier. Its first page gives copyright © 2024 Association for Computational Linguistics and specifies the CC BY 4.0 license. The journal entry confirms that license. It permits sharing and adaptation under its terms, including providing appropriate credit and a license link and marking modifications to licensed material. This dossier independently describes the results and links to the paper. It includes bibliographic metadata and factual benchmark figures, with no reproduced charts, experiment prompts or passages. Reuse of linked software, data or separately credited material requires checking its own terms. The DOI resolver returned HTTP 403 in the browsing tool. The ACL PDF and TACL article record were accessible. [Published PDF](https://aclanthology.org/2024.tacl-1.9.pdf) · [TACL journal record](https://transacl.org/index.php/tacl/article/view/5757) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0001--verification.md)

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/SRC-0001--verification.md](../audits/SRC-0001--verification.md) · [Local copy](../audits/SRC-0001--verification.md)
- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/AP-08--obsessing-over-rules.md](../topics/AP-08--obsessing-over-rules.md) · [Local copy](../topics/AP-08--obsessing-over-rules.md)
- [topics/BP-06--context-management-discipline.md](../topics/BP-06--context-management-discipline.md) · [Local copy](../topics/BP-06--context-management-discipline.md)
- [topics/OB-01--context-rot.md](../topics/OB-01--context-rot.md) · [Local copy](../topics/OB-01--context-rot.md)
- [topics/OB-10--limited-attention-focus.md](../topics/OB-10--limited-attention-focus.md) · [Local copy](../topics/OB-10--limited-attention-focus.md)
