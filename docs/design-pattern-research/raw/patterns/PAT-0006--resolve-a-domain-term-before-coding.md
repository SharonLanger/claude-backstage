---
pattern_id: PAT-0006
status: accepted
name: "Resolve a domain term before coding"
type: workflow
families: [requirements, collaboration, code-review]
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
topic_ids: [AP-05, AP-09, BP-02, BP-07, BP-09, OB-04]
symptoms: ["The agent and the ticket both say ‘visit’, but the totals differ", "A teammate and the proposed implementation use the same word for different events", "The assistant wants to simplify a choice whose reason lives in someone’s memory"]
source_ids: [SRC-0009, SRC-0007, SRC-0002]
review: PASS
publication_status: published
---

# Resolve a domain term before coding

## When users need this

A ticket asks for “daily visits.” The assistant has found a table of successful door scans and proposes counting its rows. Everyone recognizes the word *visit*. Would someone who steps outside and comes back count twice? If either answer sounds plausible and it changes the report, implementation depends on a decision the ticket leaves open.

## Context and prerequisites

Use this when a local term affects an observable outcome, such as an invoice amount, a permission, or a report count. You need the request, some evidence of existing usage and a person authorized to settle the meaning for that part of the product. An approved specification can already settle the case. A familiar industry label or a name in the schema is a lead to investigate.

## Core principle

Choose one case where competing meanings predict different results. Let the agent locate the evidence and let the person responsible for the requirement decide the expected behavior. Carry that decision into the change in a form a reviewer can check.

## How to work this way

1. **Trace the word to behavior.** Ask the assistant where the request, current implementation and local glossary or decision records use it. Request the specific function, query, or definition and the result each implies. If the team normally settles these decisions in issues, consult the relevant history. If the case is already settled and the implementation agrees, reuse the definition and proceed. [Evidence for step 1](#why-it-might-work)
2. **Ask one question that changes the answer.** Give the domain owner a concrete input and the two outcomes, along with current behavior. Ask which outcome the new feature must produce. A discrepancy might reflect a deliberate change, an existing bug, or two groups talking about different things. If the owner is unavailable or two owners disagree, leave the expected result open and pause the affected implementation. [Evidence for step 2](#why-it-might-work)
3. **Preserve the agreement at the right scope.** For a recurring concept, put a short, reviewed definition in the team's glossary for that domain. Name a confusing synonym if readers are likely to encounter it. Use the agreed term in the ticket or relevant identifier. Offer a separate architectural decision record (ADR) only when reversing the choice would be costly, a future maintainer could reasonably find it surprising, and the team actually weighed alternatives. Capture the choice, the reason and the cost the team accepted. [Evidence for step 3](#why-it-might-work)
4. **Verify the owner's answer in the change.** Turn the deciding example into an acceptance check with an expected result. Add a nearby case that should yield a different result, then compare the code and observed outputs with both. Where a deliberate exception affects the implementation, point the reviewer to its rationale. A mismatch reopens the change. [Evidence for step 4](#why-it-might-work)

## Concrete example of using the pattern

**Original illustration.** A museum wants daily visits by members. Admissions already stores a successful scan for each entry through a door. The ticket says to count visits. The proposed report counts rows. The developer brings the reporting owner an example involving one member who enters at 10 a.m. and re-enters through another door at noon. The proposed count is two. The owner specifies one visit, confirms that another member counts separately and that a return on the following local calendar day counts again.

The developer adds this definition to the reporting glossary, with the owner's agreement. “A member visit counts one member admitted to this museum on one museum-local calendar date. Re-entry on that date belongs to the same visit.” Admissions keeps *scan* for the individual door event. Both teams can now use their own terms in their interfaces.

The team considered storing only one scan per member per day. That would simplify counting, but it would discard the door-entry history Admissions uses for incident reconstruction. The alternative costs storage. Once discarded, a second scan cannot be recovered from a daily total. A future editor optimizing duplicates could easily miss this distinction. The team records the decision to retain successful scans and group them in the report, along with those reasons.

| Successful scans supplied to the report | Expected result |
|---|---|
| Lea twice on Monday, at different doors | Monday has one member visit |
| Add Mo once on Monday | Monday has two member visits |
| Add Lea once on Tuesday | Monday still has two member visits and Tuesday has one |

The reviewer can reject a row-count implementation on the first case and a lifetime distinct-member count on the third. They can also inspect whether four input scans survive report generation. Deleting the second scan would make the counts look right while undoing the documented Admissions decision.

## Why it might work

| Guidance | Accepted claim IDs | Original source and pinpoint locator | Evidence type and catalog contribution |
|---|---|---|---|
| 1. Trace the term and check for a prior decision. | SRC-0009:C01, SRC-0009:C03, SRC-0009:C05 | Pocock, [What it does, relationship and naming examples](https://www.aihero.dev/skills-domain-modeling#what-it-does) and [Cross-referencing, first two paragraphs](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops) | The skill checks code and committed records. A linked user report describes missing earlier issue history. Asking for the actual result and checking the tracker where appropriate are our application. |
| 2. Present a distinguishing case to the responsible person and defer that branch if unresolved. | SRC-0009:C01, SRC-0009:C03, SRC-0007:C07 | Pocock, [Cross-referencing, order-cancellation example](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops). Salomon et al., [§4.3, p. 11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=11) and [Table 3G, p. 8](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=8) | Pocock directly advises raising contradictions. In a survey question about where developers would take a question, 85 of 131 chose a colleague for requirements or business logic. Selecting the accountable person, stating both outcomes and deferring unresolved behavior are our workflow design. |
| 3. Record terms locally and reserve an ADR for a consequential choice. | SRC-0009:C02, SRC-0009:C04, SRC-0009:C07 | Pocock, [Two artifacts, two bars, table and following discussion](https://www.aihero.dev/skills-domain-modeling#two-artifacts-two-bars) and [Common questions, glossary value](https://www.aihero.dev/skills-domain-modeling#common-questions) | The glossary convention, naming boundaries and three-part ADR threshold are practitioner guidance from Pocock. We apply them to an agreement between the reporting owner and a developer. |
| 4. Check the resulting behavior and review the diff. | SRC-0002:C07, SRC-0002:C10, SRC-0009:C04 | Anthropic, [Give Claude a check to run, opening and examples](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) and [Review against your spec, requirements and edge cases](https://code.claude.com/docs/en/best-practices#review-against-your-spec). Pocock, [Two artifacts, two bars, ADR row](https://www.aihero.dev/skills-domain-modeling#two-artifacts-two-bars) | Anthropic recommends an interpretable check and a review against requirements. Using the owner's deciding case alongside a neighboring case, and checking preservation of a documented trade-off, are our synthesis. |

## Different source perspectives

Pocock describes his own skill. Its companion instructions and format files share its origin. His FAQ raises a fair objection that plain English might produce the same agent response. The independent study by Salomon and colleagues reports whom developers said they would ask. It supplies context for involving a colleague and offers no outcome comparison for this clarification procedure. Anthropic's separately authored vendor guidance concerns checking implementations. None of the three measures whether terminology shortens prompts, reliably steers a model, or prevents future edits. [Pocock, FAQ](https://www.aihero.dev/skills-domain-modeling#common-questions) · [Salomon et al., §4.3](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=11) · [Anthropic, specification review](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

## Tradeoffs, failure modes and when to skip it

A plausible glossary entry written before anyone answers can give a guess the appearance of policy. Keep an unresolved question in the ticket until the decision owner confirms it. For a one-off task, a plain-language expected result in the ticket may be all a reviewer needs. For a broadly shared term with a settled meaning, check the definition and spend review time on behavior. Two teams can legitimately use the same word differently. In that case, qualify the term at their interface and preserve each team's local definition. An ADR records the reason known at the time. A change in that reason can justify revisiting the choice. [SRC-0009:C02, scope of glossary](https://www.aihero.dev/skills-domain-modeling#prerequisites) · [SRC-0009:C04, decision threshold](https://www.aihero.dev/skills-domain-modeling#two-artifacts-two-bars) · [SRC-0009:C07, FAQ](https://www.aihero.dev/skills-domain-modeling#common-questions)

## Variations and practical adaptations

For an asynchronous team, leave the two predicted outputs on the issue and have the owner reply with the expected result. If the disagreement concerns an interface between teams, have each owner describe what an example means on their side and record the conversion at the interface. These are catalog adaptations of the clarification step.

## Related patterns, topics and families

AP-09 covers silent misalignment. BP-02 covers active partnership and BP-07 covers semantic anchors. The optional rationale record addresses BP-09 decision guards. AP-05 concerns AI isolation more broadly. This workflow addresses the narrower question of when an engineer should consult a colleague. Once the requirement is settled, a larger implementation can be divided into reviewable changes. [PAT-0003, Slice a change for review](PAT-0003--slice-a-change-for-review.md)

## Sources and verification

- Matt Pocock. *The /domain-modeling Skill*. AI Hero. Displayed update August 24, 2026. [Original](https://www.aihero.dev/skills-domain-modeling) · [SRC-0009 dossier](../sources/SRC-0009--domain-language-and-decisions.md) · [Local dossier](../sources/SRC-0009--domain-language-and-decisions.md) · [Source verification](../audits/SRC-0009--verification.md)
- Marie Salomon, Ekaterina Koshchenko, Agnia Sergeyuk, Reid Holmes, Gail C. Murphy and Thomas Fritz. *From Disruptions to Discussions: How GenAI Impacts Human Interactions in Software Development*. IEEE Transactions on Software Engineering, 2026. [Accepted manuscript](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf) · [SRC-0007 dossier](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Local dossier](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Source verification](../audits/SRC-0007--verification.md)
- Anthropic. *Best practices for Claude Code*. Claude Code Docs. Publication date unavailable, consulted November 21, 2026. [Original](https://code.claude.com/docs/en/best-practices) · [SRC-0002 dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Local dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Source verification](../audits/SRC-0002--verification.md)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/PAT-0006--verification.md)

## Drive navigation

- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0007--verification.md](../audits/SRC-0007--verification.md) · [Local copy](../audits/SRC-0007--verification.md)
- [audits/SRC-0009--verification.md](../audits/SRC-0009--verification.md) · [Local copy](../audits/SRC-0009--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0007--developer-collaboration-and-ai.md](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Local copy](../sources/SRC-0007--developer-collaboration-and-ai.md)
- [sources/SRC-0009--domain-language-and-decisions.md](../sources/SRC-0009--domain-language-and-decisions.md) · [Local copy](../sources/SRC-0009--domain-language-and-decisions.md)
- [topics/AP-05--ai-isolation.md](../topics/AP-05--ai-isolation.md) · [Local copy](../topics/AP-05--ai-isolation.md)
- [topics/AP-09--silent-misalignment.md](../topics/AP-09--silent-misalignment.md) · [Local copy](../topics/AP-09--silent-misalignment.md)
- [topics/BP-02--active-partnership.md](../topics/BP-02--active-partnership.md) · [Local copy](../topics/BP-02--active-partnership.md)
- [topics/BP-07--semantic-anchors.md](../topics/BP-07--semantic-anchors.md) · [Local copy](../topics/BP-07--semantic-anchors.md)
- [topics/BP-09--decision-guards.md](../topics/BP-09--decision-guards.md) · [Local copy](../topics/BP-09--decision-guards.md)
- [topics/OB-04--selective-hearing.md](../topics/OB-04--selective-hearing.md) · [Local copy](../topics/OB-04--selective-hearing.md)
