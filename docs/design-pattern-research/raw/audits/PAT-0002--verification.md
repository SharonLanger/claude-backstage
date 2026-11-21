---
artifact_id: PAT-0002
artifact_type: pattern_verification
reviewer: review_ground
reviewed: "2026-11-21"
verdict: PASS
---

# Independent verification of PAT-0002

**PASS.** A reviewer can follow the four steps to distinguish a missing operation, an invalid invocation and an existing operation with the wrong effect. The procedure also identifies what remains uncertain when only local types or a mock are available. I reviewed the submitted draft independently of its author, read both accepted dossiers, reopened both original publications and ran two local checks. [Pattern](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) · [Jain et al. dossier](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md)

## Findings

1. **Describe the effect.** SRC-0002:C06 supports specifying a symptom and a success criterion. SRC-0004:C03 distinguishes wrong target, missing name and incorrect usage. C04 measures how changing a name in the prompt affects similarity of the generated continuation. The entry accurately labels the order in which a reviewer should inspect dependent calls as an editorial choice. [Anthropic, specific prompts](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt) · [Jain et al., conference §II-A, Table I](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=2)

2. **Match the reference to the receiver.** SRC-0004:C01, C03 and C06–C07 support checking target identity and taking care with retrieved documentation. I verified all three error percentages against the GPT-4o row of Appendix A.6, Table 4. The denominator is the invalid low-frequency calls. Table IV confirms that unconditional retrieval under the stated one-document, 50% target-inclusion condition improved the rare-call result and hurt the common-call result. The pattern confines those results to the experimental conditions. Matching the installed package version is sensible original advice. [Preprint, Appendix A.6](https://arxiv.org/html/2407.09726v1#A1) · [Conference Table III](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5) · [Conference Table IV](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=7)

3. **Check arguments and consumers.** SRC-0004:C01 and C04–C06 distinguish the first-call binding test, downstream edit similarity and the model's response to supplied documentation. The entry correctly assigns the 41.80% to 86.82% validity gain to StarCoder2-3B with the correct document guaranteed. The paper checks invocation syntax and target identity. The entry explicitly extends the check to what the application's caller expects back. [Conference §III-B, Fig. 6](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5) · [Preprint §§2.2–2.3](https://arxiv.org/html/2407.09726v1#S2)

4. **Exercise behavior.** SRC-0002:C07–C08 support requesting a runnable check and inspecting its command and result. SRC-0004:C01 and C09 support the limits of binding as evidence and identify the authors' guidance on human review and sandbox execution. Choosing a fixture with a known distinguishing result is marked as an adaptation. The entry gives workable stopping conditions for a remote dependency and for a fault already traced past the API boundary. [Anthropic, execution evidence](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Preprint §§7–8](https://arxiv.org/html/2407.09726v1#S7)

## Usability checks

5. **Replay.** I executed the entry's unmodified code block via Python standard input. Python 3.12.14 printed `3.12.14 (name)` and `size=4, missing=KeyError`. Separately, evaluating the original `read(...).file_size` raised `AttributeError` on bytes. Runtime help for the corrected operation identified a named member's `ZipInfo`, whose size was 4. The draft's conclusion accurately covers library behavior and leaves application rendering open.

6. **Transfer to another unfamiliar call.** For a validator that must accept a complete four-character identifier, I tested a proposed `re.Pattern.match` call and inspected the locally installed `fullmatch` documentation and bound signature. With pattern `[A-Z]{2}[0-9]{2}` and inputs `AB12`, `AB12junk` and `junkAB12`, the proposed method returned matches for the first two. The replacement matched only the first. Both use the same receiver and accept a string. The false positive on trailing text shows why a correct name, signature and positive example are insufficient. This reviewer-created fixture tests applicability to a second case. Neither replay measures how the workflow affects developer performance.

## Provenance, rights and disposition

7. **Independence and scope.** The Amazon Science manuscript and the arXiv preprint are versions of one empirical study. The benchmark contains 622 short synthetic Python tasks involving AWS and Azure. Anthropic's separate guide provides direct practitioner advice about verifying work. It supplies no independent replication of the experiment. Confidence is high in the cited observations under their reported conditions. Team review cost and defect reduction from this manual workflow are open questions. The study's support for BP-06 extends only to documentation selection. [Amazon Science record](https://www.amazon.science/publications/on-mitigating-code-llm-hallucinations-with-api-documentation) · [Anthropic guide](https://code.claude.com/docs/en/best-practices)

8. **Original expression and traceability.** The entry uses an original archive example, independent prose and a short verification fixture. The API names, titles and reported measurements can be traced to their stated origins. I found no copied source example, prose passage or figure. The preprint identifies an arXiv distribution license. No whole-work reuse grant is assumed for either source. The four local links to dossiers and source audits resolve, and each claimed ledger identifier exists. [Preprint and license notice](https://arxiv.org/html/2407.09726v1) · [SRC-0004 audit](SRC-0004--verification.md) · [SRC-0002 audit](SRC-0002--verification.md)

**Disposition.** No substantive changes required. Publication status, reciprocal catalog links and Drive readback belong to the integrator.

## Drive navigation

- [patterns/PAT-0002--verify-an-unfamiliar-api-call.md](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) · [Local copy](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
