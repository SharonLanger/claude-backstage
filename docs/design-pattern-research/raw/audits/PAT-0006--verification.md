---
pattern_id: PAT-0006
reviewer: review_terms
reviewed: 2026-11-21
verdict: PASS
source_ids: [SRC-0009, SRC-0007, SRC-0002]
---

# Independent pattern review of PAT-0006

**PASS.** A reader can use one example to settle a requirement, record the owner's decision and detect an implementation that produces the wrong behavior. The study cited by the pattern establishes whom developers said they would ask. Effectiveness of the combined workflow remains unmeasured. [Pattern under review](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)

## Findings

1. **Step 1, trace the term.** SRC-0009:C01, C03 and C05 match Pocock's discussion of comparing a stated rule with existing code and consulting committed definitions and decisions. I also reopened the linked contributor report. The contributor found one naming collision already settled in an issue and a second whose meaning was still open. The pattern makes checking the tracker conditional on where the team records these decisions. Its request for an observable result is an identified adaptation. [Pocock, cross-referencing](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops) · [Contributor's account, issue 717](https://github.com/mattpocock/skills/issues/717)

2. **Step 2, ask the person responsible.** Pocock's partial-cancellation example directly supports raising a contradiction. I checked the original survey question and results paragraph in Salomon et al. Table 3G asks respondents where they would take a question. Section 4.3 reports that 85 of 131 selected a colleague for questions about business logic or requirements. SRC-0007:C07 accurately supports the reason for involving a colleague. Presenting two possible outputs, identifying a decision owner and pausing only the disputed work are the catalog authors' choices. [Pocock, cross-referencing](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops) · [Table 3G, p. 8](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=8) · [§4.3, p. 11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=11)

3. **Step 3, choose how to record the decision.** SRC-0009:C02, C04 and C07 support concise, domain-specific entries, reuse at naming boundaries and a selective ADR. All three of Pocock's conditions survive in the pattern. The museum decision meets them because the team weighed storage against lost entry history, deleted events cannot be recovered from totals, and a later reporting developer could mistake re-entries for expendable duplicates. The FAQ also supplies the stated objection about plain language and the risk of recording an unchecked model guess. [Pocock, glossary and ADR table](https://www.aihero.dev/skills-domain-modeling#two-artifacts-two-bars) · [Common questions](https://www.aihero.dev/skills-domain-modeling#common-questions)

4. **Step 4, verify observed behavior.** SRC-0002:C07 and C10 support a runnable check with readable results and review of the change against requirements and edge cases. SRC-0009:C04 supports keeping the rationale available to the reviewer. The entry credits its own authors for pairing the deciding example with a neighboring case and checking that the intended trade-off survives. The procedure works with an ordinary issue, code diff and test runner. [Anthropic, checks](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Anthropic, specification review](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

5. **Museum walkthrough.** Using the supplied rows as cumulative fixtures, I grouped by local date and member. The first two scans give Monday one visit. Adding Mo gives Monday two. Adding Lea on Tuesday gives Monday two and Tuesday one. Counting rows fails the first case. Assigning a member only to their first day misses Tuesday. Verifying the four underlying events adds a separate preservation check that those correct daily totals could otherwise conceal. The illustration supplies the inputs, decision authority, expected results, alternative and review criteria needed for a reader to repeat it.

6. **Independence, rights and navigation.** The skills guide and its companion instructions share an author. The separately authored survey and vendor guide contribute a reported preference and implementation advice. The museum scenario, its table and the operational workflow use original expression. The paper's factual count is attributed and the manuscript carries a CC BY-NC-ND 4.0 notice. No article text, interview extract, figure or source example is reproduced at length. I verified the seven relative file links, the accepted status of all three dossiers and their separate PASS audits. No substantive correction or recheck was required. [SRC-0009](../sources/SRC-0009--domain-language-and-decisions.md) · [SRC-0007](../sources/SRC-0007--developer-collaboration-and-ai.md) · [SRC-0002](../sources/SRC-0002--claude-code-best-practices.md) · [Manuscript license notice, p. 1](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=1)

## Drive navigation

- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
