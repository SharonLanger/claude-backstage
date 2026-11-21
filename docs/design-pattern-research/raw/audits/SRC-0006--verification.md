---
source_id: SRC-0006
artifact_type: source_verification
verdict: PASS
reviewed: 2026-11-21
reviewer: review_slices
---

# SRC-0006 independent verification

**PASS.** I reopened Matt Pocock’s article, compared all ten ledger claims with their cited passages, and checked the author’s repository and the two linked issue reports. The dossier can support advice about dividing a feature into demonstrable tickets. Evidence about reviewer effort or accuracy would need to come from a different study. [Reviewed dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Original article](https://www.aihero.dev/skills-to-tickets)

## Findings

1. **Bibliography and access.** The public article identifies Matt Pocock as the author of *The /to-tickets Skill*, published on AI Hero. Its visible date is an update on August 24, 2026. A separate first-publication date is unknown. The scenarios, tracker table, case anecdote and exception were accessible on November 21, 2026. The linked skill definition describes the same author's implementation and shares its provenance with the article. [Article](https://www.aihero.dev/skills-to-tickets) · [Skill definition](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md)
2. **SRC-0006:C01 and SRC-0006:C02.** The opening two paragraphs support the list of inputs, the requirement to record predecessors, and the intended unit of delivery. The dossier correctly lets a ticket have prerequisites while requiring a demonstrable outcome once it lands. A fresh session is a sizing constraint in the guidance. [What it does](https://www.aihero.dev/skills-to-tickets#what-it-does)
3. **SRC-0006:C03 and SRC-0006:C04.** The scenario table gives separate routes for unsettled decisions and a change small enough for one session. The article describes a human decision before publication. The skill definition’s process steps 2–5 confirm the check for preparatory refactoring, the proposed outcome and dependencies shown to the user, and revision until approval. [When to reach for it](https://www.aihero.dev/skills-to-tickets#when-to-reach-for-it) · [Repository process](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md#process)
4. **SRC-0006:C05.** The troubleshooting paragraphs on layer-shaped tickets and acceptance criteria support asking for a demonstration and checking whether the criterion for a new behavior can fail at the starting revision. The article describes the demo-path field as a suggestion from users. The dossier’s invoice-search example is explicitly an original application. [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions)
5. **SRC-0006:C06.** The article’s tracker comparison and repository publication step establish the intended ordering, local representation, native dependency links and ready condition. The issue bodies confirm two distinct historical failures. Issue 513 describes a prerequisite recorded only as prose. Issue 554 describes a missing parent link to the specification. Neither report evaluates slicing effectiveness. [Blocking edges](https://www.aihero.dev/skills-to-tickets#blocking-edges) · [Repository publish step](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md#5-publish-the-tickets-to-the-configured-tracker) · [Issue 513](https://github.com/mattpocock/skills/issues/513) · [Issue 554](https://github.com/mattpocock/skills/issues/554)
6. **SRC-0006:C07.** The article recounts one team’s 26-ticket experience. Its figures are approximately 20 agent runs per closed ticket, with around three quarters of runs described as rework. The team’s explanation reaches the reader through Pocock. This paragraph supplies neither raw observations nor a comparison group. The dossier preserves both the approximate units and the attribution. [Tracer bullets, second paragraph](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers)
7. **SRC-0006:C08.** The stated exception covers a broadly coupled mechanical migration. The dossier correctly distinguishes compatible batches that keep CI passing individually from batches that need a shared branch and a final verification ticket. [The wide-refactor exception](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception)
8. **SRC-0006:C09 and SRC-0006:C10.** The troubleshooting and workflow sections support retaining planning context when retrieving a large specification is problematic, using fresh sessions for implementation, and placing code review downstream. The complete article gives no comparative review measurements. AP-07 has direct practitioner guidance, BP-06 has specific guidance on a planning-to-implementation handoff, and BP-05 has support for choosing a verifiable unit of work. A reduction in review time or fatigue remains unmeasured. [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions) · [Where it fits](https://www.aihero.dev/skills-to-tickets#where-it-fits)
9. **Rights and originality.** The site’s general terms address copying in section 2. The repository’s MIT license covers software and associated documentation under its notice condition. The dossier distinguishes these records, uses original explanatory prose and an independently constructed example, and includes no article reproduction. [Site terms](https://www.aihero.dev/privacy) · [Repository license](https://github.com/mattpocock/skills/blob/main/LICENSE)

## Disposition

All ten claims passed on first review. No corrections requested. The underlying team postmortem and a measured PR-review effect remain unavailable from the cited article. Publication and Drive readback are separate checks for the integrator.

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0006--vertical-slices-for-agent-tickets.md](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Local copy](../sources/SRC-0006--vertical-slices-for-agent-tickets.md)
