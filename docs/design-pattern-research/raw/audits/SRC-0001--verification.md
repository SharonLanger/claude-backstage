---
artifact_id: SRC-0001
artifact_type: source_verification
reviewer: review_liu
reviewed: "2026-11-21"
initial_verdict: PASS WITH CHANGES
verdict: PASS
---

# Independent source review of SRC-0001

**Initial disposition — PASS WITH CHANGES.** The methods, rights record, and principal result are supported. The first draft attached two findings to model families where the figures identify particular versions. Findings 3 and 9 record the corrections requested.

**Material inspected.** I opened the ACL bibliographic record and the 17-page version of record independently, then compared the [source dossier](../sources/SRC-0001--lost-in-the-middle.md) with the original. I inspected the plotted series and legends in Figures 5, 7, 9 and 11, the numerical baselines in Table 1, the reported experimental conditions, and the appendix text. The author’s source files, datasets and model experiments were outside this verification. [ACL record](https://aclanthology.org/2024.tacl-1.9/) · [Journal PDF](https://aclanthology.org/2024.tacl-1.9.pdf)

## Numbered findings

| Finding | Item | Check against the original | First-pass disposition |
|---|---|---|---|
| 1 | Provenance, rights and expression | All seven authors, title, volume 12, pages 157–173, publisher and DOI agree with the ACL record. The journal gives February 19, 2024. The paper credits Stanford CRFM, OpenAI API credits and Anthropic academic access in the acknowledgments. Printed p. 157 identifies ACL as the copyright holder and specifies CC BY 4.0. The journal independently links that license. I found original explanations and attributed factual values in the dossier, with no reproduced figure or extended passage. [TACL publication and license](https://transacl.org/index.php/tacl/article/view/5757) · [PDF first page](https://aclanthology.org/2024.tacl-1.9.pdf#page=1) · [Acknowledgments](https://aclanthology.org/2024.tacl-1.9.pdf#page=11) · [License](https://creativecommons.org/licenses/by/4.0/) | Pass |
| 2 | SRC-0001:C01 | The 2,655 questions have paragraph long answers. For a given question and bundle size, the study moves the designated answer passage. Retrieved distractors are screened for annotated answers. Accuracy credits a response containing any annotated answer. Appendix A checks ambiguity introduced by the corpus and annotation dates. [§2.1, pp. 159–160](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) · [Appendix A, p. 171](https://aclanthology.org/2024.tacl-1.9.pdf#page=15) | Pass |
| 3 | SRC-0001:C02 and baseline discussion | The positional finding holds. Figure 5 includes both GPT-3.5-Turbo traces at 20 documents and only the 16K trace at 30. Table 1 gives standard model closed-book/oracle accuracy of 56.1%/88.3% and 16K accuracy of 56.0%/88.6%. Section 2.3 uses the family name across conditions. The first draft's wording allowed the 30-document dip to be attributed to the standard model. Identify the variant at 30 documents and keep the baselines with the matching versions. [Fig. 5 and Table 1, p. 161](https://aclanthology.org/2024.tacl-1.9.pdf#page=5) | Change requested |
| 4 | SRC-0001:C03 | For shared 10- and 20-document inputs, §2.3 describes nearly overlapping standard and 16K curves. The model-version footnote identifies the 0613 snapshots. [§§2.2–2.3, Fig. 5, pp. 161–162](https://aclanthology.org/2024.tacl-1.9.pdf#page=5) | Pass |
| 5 | SRC-0001:C04 | The UUID task uses 500 examples per size. The two Claude variants achieved near-perfect accuracy on the lengths each could handle. The LongChat code-output observation is specific to the 140-pair series and is identified as qualitative. [§§3.1–3.2, Figs. 6–7, pp. 162–163](https://aclanthology.org/2024.tacl-1.9.pdf#page=6) | Pass |
| 6 | SRC-0001:C05 | Section 4.1 reports a 1.9-percentage-point difference for Flan-UL2 in its in-range condition. It reports greater position sensitivity at longer lengths for the two encoder-decoder models. The dossier appropriately distinguishes the proposed architectural explanation from that observation. [§4.1, Fig. 8, pp. 163–164](https://aclanthology.org/2024.tacl-1.9.pdf#page=7) | Pass |
| 7 | SRC-0001:C06 | With a 300-pair object, §4.2 compares the 16K model's 45.6% worst position against perfect lookup when the key appears on both sides of the object. Figure 9 shows why repeating the query cannot be prescribed as a general fix for passage QA. [§4.2, p. 164](https://aclanthology.org/2024.tacl-1.9.pdf#page=8) · [Fig. 9, p. 165](https://aclanthology.org/2024.tacl-1.9.pdf#page=9) | Pass |
| 8 | SRC-0001:C07 | Figure 10 shows both MPT versions share the U-shape and the instruction-tuned version scores higher throughout. The interpretation stays within that model comparison. [§4.3, Fig. 10, p. 165](https://aclanthology.org/2024.tacl-1.9.pdf#page=9) | Pass |
| 9 | SRC-0001:C08 and open-domain case study | The 20-to-50 passage comparison and approximate absolute gains are consistent with §1 and Figure 11. The legend names GPT-3.5-Turbo (16K) and Claude-1.3 (100K). Record these variants wherever this comparison is attributed. [§1, p. 159](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) · [§5, Fig. 11, p. 166](https://aclanthology.org/2024.tacl-1.9.pdf#page=10) | Change requested |
| 10 | SRC-0001:C09 | Section 5 proposes ranking and truncation after the retrieval case study. The source does not evaluate an alternative reranker or establish a universal optimal passage count. The dossier labels the proposal correctly. [§5, p. 166](https://aclanthology.org/2024.tacl-1.9.pdf#page=10) | Pass |
| 11 | SRC-0001:C10 | Appendices A–C cover the ambiguity-filtered questions, random passages and shuffling with a prompt cue. The dossier retains the easier random-passage condition and the combined manipulation in C. [Appendices A–C, Figs. 12–14, pp. 171–172](https://aclanthology.org/2024.tacl-1.9.pdf#page=15) | Pass |
| 12 | SRC-0001:C11 | Appendix D uses a random 500-example subset with 20 documents for GPT-4 (8K). Appendix E's 20-document results distinguish the predominantly recency-driven 7B models from the 13B and 70B models. [Appendices D–E, Figs. 15–16, pp. 172–173](https://aclanthology.org/2024.tacl-1.9.pdf#page=16) | Pass |
| 13 | SRC-0001:C12 | The final introduction paragraph proposes testing how much accuracy varies with evidence position. The dossier identifies evaluation across positions as the authors' criterion and leaves selection of a repository-specific success measure to practitioners. [§1, p. 159](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) | Pass |
| 14 | Topic relevance, examples and independence | The single-prompt design directly supports a position effect under OB-10 and indirectly informs OB-01 and BP-06. No experiment tests changing repository state, conversation compaction, recovery after a reset, or the suggested file-citation check. The dossier identifies these coding applications as adaptations. The ablations and appendices count as one publication. [§§2–5, pp. 159–166](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) | Pass |

## Correction record

**Final disposition — PASS on recheck, November 21, 2026.** I compared the revised C02 row and baseline paragraph with the plotted entries in Figure 5 and the four numbers in Table 1. Both passages now identify the 16K-only family entry at 30 documents. I compared the revised C08 row and case-study paragraph with Figure 11. Both use the two extended-variant labels. Findings 3 and 9 are closed. All twelve ledger claims pass. No substantive blockers remain for source acceptance. [Figure 5 and Table 1](https://aclanthology.org/2024.tacl-1.9.pdf#page=5) · [Figure 11](https://aclanthology.org/2024.tacl-1.9.pdf#page=10)

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0001--lost-in-the-middle.md](../sources/SRC-0001--lost-in-the-middle.md) · [Local copy](../sources/SRC-0001--lost-in-the-middle.md)
