---
artifact_id: PAT-0001
artifact_type: pattern_verification
reviewer: review_context
reviewed: "2026-11-21"
verdict: PASS
---

# Independent verification of PAT-0001

**PASS.** A practitioner can distinguish a repeated misunderstanding from productive debugging, preserve useful changes, and check whether the assistant has recovered. The evidence supports the component advice. The combined workflow’s effect on coding outcomes remains unmeasured. [Reviewed pattern](../patterns/PAT-0001--recover-a-drifting-coding-session.md)

## Findings by step

| Finding | Evidence checked and disposition |
|---|---|
| 1. Identify the mismatch | SRC-0001:C01, C02 and C04 describe controlled position changes in single-prompt QA and key lookup. The dependence on position differed across tasks and models. SRC-0002:C06 provides direct guidance on giving a concrete symptom and success criterion. Selecting an input that distinguishes two behaviors is explicitly a pattern adaptation. The paper cannot identify the cause of drift in a live conversation. Pass. [Liu et al., §§2.1–2.3](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) · [§3.2 and Figure 7](https://aclanthology.org/2024.tacl-1.9.pdf#page=7) · [Anthropic, specific prompts](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt) |
| 2. Save a handoff | SRC-0002:C05–C06 cover a written specification, a fresh implementation session and giving the location of the problem. C02 covers naming what to preserve in a summary. The handoff fields, distinction between verified and open decisions, and inspection of the actual changes are the pattern author’s operational choices. Each is practicable with an issue, an editor and a diff. Pass. [Written spec](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first) · [Focused compaction](https://code.claude.com/docs/en/best-practices#keep-cost-and-context-down) |
| 3. Choose the session boundary | SRC-0002:C01–C04 and C17 substantiate the options for separate tasks, bulky history and repeated unsuccessful corrections. The original limits checkpoints to qualifying edits by file tools in the main conversation. Step 3 calls for inspecting the diff and leaves the file decision with the practitioner. It treats two corrections as a vendor heuristic and supplies an alternative when summarization still serves the task. Pass. [Session steering](https://code.claude.com/docs/en/best-practices#steer-the-session) · [Cost and context](https://code.claude.com/docs/en/best-practices#keep-cost-and-context-down) · [Revised recommendations](https://code.claude.com/docs/en/best-practices#what-you-can-stop-doing) |
| 4. Verify the missed case | SRC-0002:C07–C08 and C10 support supplying a check, asking for the observable result, and examining requirements and edge-case tests during review. The pre-edit prediction, selecting the original missed input, and checking the assertion itself are identified as adaptations. The procedure distinguishes an accurate prediction from an observed execution result and limits its conclusion to what was exercised. Pass. [Runnable checks and execution evidence](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Spec review](https://code.claude.com/docs/en/best-practices#review-against-your-spec) |

## Independent usability check

5. I followed the playlist example from the pattern alone. The recurring mistake was an alphabetical sort, the governing rule was input order, and the earlier escaped-title fix was useful work to retain. Two repeated reversions selected a new conversation with a written handoff. Given the alternative of a still-aligned session full of parser traces, the same criteria selected a focused summary. Conflicting requirements would instead require a decision before either route.

6. I executed a small in-memory Python check for the example’s acceptance criteria. Its input contained Zebra, Apple and a Unicode-escaped spelling of Café in that order. Applying a sort failed the order assertion while decoding still passed. Preserving input order made both checks pass. This verifies that the illustrative checks can distinguish the error and preserve a separate behavior. It is a reviewer-created fixture. The example’s repository and pytest invocation are hypothetical, and this exercise measured no effect of restarting an agent.

## Evidence strength, independence and rights

7. Evidence is strong for position sensitivity in the paper’s tested QA conditions. Its relevance to diagnosing a coding session is indirect. Anthropic’s guide is direct evidence of vendor recommendations for Claude Code, with moderate support for trying the described operations in that setting. Comparative effectiveness of the portable workflow has low evidential support. The two publications supply different kinds of evidence. The paper acknowledges Anthropic academic program access among other assistance. Neither publication independently tests the coding-session intervention. The pattern appropriately covers a useful exception in the vendor’s current guidance on long sessions. [Paper acknowledgments](https://aclanthology.org/2024.tacl-1.9.pdf#page=11) · [Current vendor guidance](https://code.claude.com/docs/en/best-practices#what-you-can-stop-doing)

8. I reopened the [ACL record](https://aclanthology.org/2024.tacl-1.9/), the [published PDF](https://aclanthology.org/2024.tacl-1.9.pdf) and the [official guide](https://code.claude.com/docs/en/best-practices). The PDF displays CC BY 4.0 on its first printed page. No comparable reuse grant was established for the guide. The pattern uses independent prose, a distinct example and original dialogue. It reproduces no source figure, sample prompt or substantial passage.

9. All 13 named claim IDs resolve in the two accepted dossiers. Local links to the catalog, both dossiers and both source audits resolved during review. Hosting and Drive readback belong to the publication record. [SRC-0001](../sources/SRC-0001--lost-in-the-middle.md) · [SRC-0002](../sources/SRC-0002--claude-code-best-practices.md) · [Source audit 1](SRC-0001--verification.md) · [Source audit 2](SRC-0002--verification.md)

**Disposition.** No substantive corrections or open blockers for pattern acceptance.

## Revision review on 2026-11-21 — addition of SRC-0003

**PASS for the three-source revision.** Step 3 now offers a specification-only retry for a bounded function with a clear test. Evidence row 6 and the source comparison establish the scope of that option. Findings 1–9 above concern the earlier two-source version. I checked the new material against the independently accepted [SRC-0003 dossier](../sources/SRC-0003--debugging-effectiveness-decay.md), its [source audit](SRC-0003--verification.md), and the version of record. The canonical Nature URL redirected to a cookie challenge in the retrieval tool. The publisher PDF, Table 2 and PMC copy opened successfully. [Publisher PDF](https://www.nature.com/articles/s41598-025-27846-5.pdf?code=7b2&error=cookies_not_supported) · [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12715212/)

10. **Step 3 intervention and scope.** SRC-0003:C01, C02 and C06 match the RQ3 intervention and HumanEval protocol on pp. 4–5. The baseline permits one generation and up to five repairs. The intervention spends a slot within the same six-attempt ceiling to generate again from the original problem statement. Ordinary repair includes prior generated code and test feedback. The paper does not specify enough to reconstruct every earlier message visible to each repair. The pattern accurately treats what to save from the real working tree and how to compare candidate diffs as practitioner adaptations. [RQ3 and protocol](https://www.nature.com/articles/s41598-025-27846-5.pdf?code=7b2&error=cookies_not_supported#page=4)

11. **Step 3 results.** For SRC-0003:C07 and C08, I compared each of the nine Table 2 rows with its own baseline. All nine later-threshold cells are higher. At the earlier threshold seven are higher and Codestral 22B and Devstral 24B are lower. These are observed point estimates. The table supplies no confidence intervals for the gains. The PAT makes no significance or universally optimal retry claim. [Original Table 2](https://www.nature.com/articles/s41598-025-27846-5/tables/2?code=7b2&error=cookies_not_supported)

12. **Mechanisms and portability.** SRC-0003:C02, C03, C06, C10 and C11 support the account of dependent repairs, shrinking task pools and an intervention that changes both the inputs and the requested operation. Discussion pp. 9–10 identifies possible explanations and limits transfer. The new study provides independent empirical evidence about one component. It leaves the cost and value of a retained handoff in repository work open. Anthropic's two-correction cue and the fitted benchmark schedules address different decisions. The pattern keeps them distinct. [Protocol, p. 5](https://www.nature.com/articles/s41598-025-27846-5.pdf?code=7b2&error=cookies_not_supported#page=5) · [Discussion, pp. 9–10](https://www.nature.com/articles/s41598-025-27846-5.pdf?code=7b2&error=cookies_not_supported#page=9)

13. **Usability and rights.** Applied to the playlist example, a replacement listing function could receive the input-order contract and be judged by the same order check. The earlier decoder edit remains separately inspectable, with its own escaped-title check. For a change whose behavior depends on unresolved cross-file contracts, the pattern's small-function prerequisite rules out that branch. This is a walkthrough of the revised decision, alongside the executed fixture described in finding 6. The authors' paper carries CC BY-NC-ND 4.0. The new text independently describes factual results and the catalog's application, without reproducing the authors' figures, table or expressive passages. The article, table and PMC record count as one source. [Rights notice, p. 11](https://www.nature.com/articles/s41598-025-27846-5.pdf?code=7b2&error=cookies_not_supported#page=11)

**Revision disposition.** No substantive corrections or open evidence blockers. The publication readback for this revision belongs to the orchestrator.

## Drive navigation

- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
