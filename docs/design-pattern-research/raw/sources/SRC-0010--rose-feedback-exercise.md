---
source_id: SRC-0010
status: accepted
original_title: "ROSE Feedback"
authors: ["Ivett Ördög"]
publisher: "Samman Technical Coaching Society"
source_type: workshop_lesson
published: unknown
updated: unknown
accessed: 2026-11-21
original_url: "https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html"
source_version: "Live Learning Hours page. Matching lesson text in the publisher repository at commit 176f1057ab290b4355dfc9cb31fd48a4a49e7f7a, June 26, 2026."
full_text_reuse: authorized
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [BP-10]
related_patterns: [PAT-0005]
review: PASS
publication_status: published
---

# ROSE Feedback

## Provenance and scope read

Ivett Ördög is credited in the footer of this Samman Technical Coaching Society Learning Hour and on the linked contributor page, which identifies her as an independent consultant. The complete public lesson is freely accessible and displays neither a publication date nor an update date. The publisher’s repository records the lesson’s addition on June 26, 2026, and the lesson Markdown at that revision matches the current repository file. The commit credits Claude Opus 4.8 as a co-author of the commit. The published lesson’s attribution names Ördög. This is a practitioner teaching resource. [Published lesson and footer](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html) · [Contributor profile](https://sammancoaching.org/society/contributors/devill.html) · [Publisher repository commit](https://github.com/sammancoaching/website/commit/176f1057ab290b4355dfc9cb31fd48a4a49e7f7a)

Read the entire lesson from its opening through facilitator conclusions, inspected the target drawing and the five prompts in the SVG handout through the publisher’s repository, and inspected the linked Tennis kata description and its Python implementation of `TennisGame2`. The dossier covers the documented exercise and a worked reading of the Python code. Running the exercise with an agent was outside this source review. [Lesson and embedded assets](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html) · [Handout source](https://github.com/sammancoaching/website/blob/main/assets/images/rose_pattern_handout.svg) · [Kata description](https://sammancoaching.org/kata_descriptions/tennis.html) · [Python exercise code](https://github.com/emilybache/Tennis-Refactoring-Kata/blob/main/python/tennis2.py)

## Reader's orientation

Ördög introduces ROSE for a specific moment in AI-assisted coding. The agent has returned work and the developer wants a revision. A directive alone can tell the agent which edit to make while leaving the purpose and success conditions unstated. The method puts the goal and the relevant evidence back into that conversation. The lesson’s description of responses that feel like “malicious compliance” describes an experienced mismatch between action and intent. It attributes no motive to an agent and supplies no estimate of how commonly that mismatch occurs. [Opening and “Concept: The ROSE feedback pattern”](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern)

## Detailed analytical reading (original words)

### Give the reviewer’s rationale and a check

Each element supplies a different kind of information. **Risk** states the plausible harm of leaving the current approach in place. **Observation** points to the present evidence that gives rise to the concern, such as a repeated setup in named tests or an IDE selection that the agent can access. **Solution** tells the agent what change the reviewer wants. **Expected outcome** specifies what the improved work should deliver. The risk may be a future maintenance problem. The outcome is nearer-term and can be an observable improvement the agent can check. The lesson allows the elements to appear in any order and to be omitted when unnecessary. Its statement that most people give only the solution is a practitioner observation without a supporting survey or count. [“Concept,” definitions and qualifications](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern)

The lesson illustrates the distinction with test readability. Repetitive mock preparation is the evidence. Fragile tests that demand more effort to maintain are the potential consequence. The suggested revision is conditional on side effects. Use the real dependency when it is side-effect-free and use a stateful fake otherwise. More compact tests whose intent is easier to inspect are the hoped-for immediate result. That example gives a developer a way to explain why merely relocating a block of mocks could leave the underlying problem in place. This last interpretation is an inference from the example. [“Concept,” the test example](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern)

### Practice on supplied material

The facilitator first has participants draw from verbal steps without seeing the target and then reveals a house with a triangular roof and a sun. The class discusses what information would have helped their drawings converge. The comparison is an analogy for feedback that communicates operations but leaves the recipient to infer the objective. It is part of the planned activity, with no participant observations or comparison data presented on the page. [“Connect: Blind drawing”](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#connect-blind-drawing) · [Target drawing](https://sammancoaching.org/assets/images/blind_drawing_exercise.png)

The handout asks participants to find the elements inside ordinary review prompts. Its examples cover where to put scoring logic for reuse, mock-heavy tests, nested loops that bypass an existing iterator, inconsistent coordinate conventions, and dependency installation policy. A coordinate example makes the desired shape of the code unusually concrete by restricting where bare axis values can cross a boundary. The exercise encourages reading for what the words do, even when a phrase serves more than one purpose. It includes a prompt that asks the agent to suggest further actions alongside specific corrective instructions. [“Active reading” and facilitator note](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#active-reading-10-min) · [Handout, coordinate and package-installation examples](https://github.com/sammancoaching/website/blob/main/assets/images/rose_pattern_handout.svg)

In the second exercise, the participant reads a version of `TennisGame2`, finds a problem and writes feedback as though an agent had produced that implementation. Sending the prompt to an agent is optional, time permitting. The plan ends by asking people to explain the four parts in their own words. The page provides the activity and illustrative material. It reports no agent transcripts, model settings, participant sample, comparison group, scoring rubric, or measured results. [“Write ROSE prompts for the Tennis kata”](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#write-rose-prompts-for-the-tennis-kata-25-min) · [Complete lesson](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html)

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support / caveat |
|---|---|---|---|---|
| SRC-0010:C01 | Ördög recommends ROSE when asking a coding agent to revise an existing result. Her proposed rationale is to make the developer’s intent visible alongside the requested edit. | Practitioner advice | [Opening and “Concept,” first paragraph](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) | Direct guidance for BP-10. Claimed benefit is the author’s rationale. |
| SRC-0010:C02 | Risk explains the cost of the current approach, Observation points to evidence, Solution requests a change, and Expected outcome describes the desired result. | Practitioner advice | [“Concept,” four bullets](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) | Direct definitions. |
| SRC-0010:C03 | The order and number of elements are flexible. An IDE selection can serve as an observation when the agent can read it. | Practitioner advice | [“Concept,” after the four bullets](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) | Direct. Selection support depends on the tool. |
| SRC-0010:C04 | The lesson distinguishes potential downstream harm from an immediate benefit or change that can be checked. | Practitioner advice | [“Concept,” final two bullets](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) | Direct. Actual checkability depends on the chosen outcome. |
| SRC-0010:C05 | The worked test example connects repetitive mocks to upkeep and proposes the real dependency where side-effect-free or a stateful fake in other cases, with more readable tests as the aim. | Illustrative example | [“Concept,” examples attached to each element](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) | Direct example. A resulting diff or follow-up evaluation is absent. |
| SRC-0010:C06 | The lesson uses a drawing analogy, prompt annotation and feedback writing on the Tennis kata. The optional agent run invites participants to inspect whether the output moved in the intended direction. | Teaching procedure and scope assessment | [Session outline](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#session-outline) · [Kata exercise, steps 1–4](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#write-rose-prompts-for-the-tennis-kata-25-min) | Direct lesson plan. The page reports no evaluation results. |
| SRC-0010:C07 | The prompt handout includes both a concrete code boundary for a coordinate conversion and an open request for further mitigation ideas alongside prescribed changes. | Teaching examples | [Handout, coordinate and package-installation blocks](https://github.com/sammancoaching/website/blob/main/assets/images/rose_pattern_handout.svg) | Direct examples. The handout supplies prompts as material for discussion. |

## Extractable practitioner insights

### Worked case for BP-10

Consider a hypothetical review of the Python Tennis kata version inspected for this dossier. Several branches in `TennisGame2.score` repeat the translation from point totals to display labels for the two players. “Replace the branches with a lookup” could be interpreted as moving advanced scoring into the lookup as well. A narrow change can give the agent a stable boundary by specifying the ordinary point labels as the target and treating the special score cases as acceptance checks. The following is original example feedback constructed from the source’s kata prompt and the observed Python code. [Kata instructions, SRC-0010:C06](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#write-rose-prompts-for-the-tennis-kata-25-min) · [`TennisGame2.score`](https://github.com/emilybache/Tennis-Refactoring-Kata/blob/main/python/tennis2.py#L12-L82)

| Element | Feedback to the agent |
|---|---|
| Risk | A scoring-label change can leave the two players displaying different labels for the same point total if someone edits only one branch. |
| Observation | In `TennisGame2.score`, the ordinary point-to-label mapping is repeated across the branches for ties and both player leads. |
| Solution | Use one shared mapping for the ordinary zero-to-three point labels and use it for either player. Keep the scope of the refactor on label selection. |
| Expected outcome | Ordinary label lookup has one definition. The current score strings for 2–2, 3–3, 4–3, 3–4 and 5–3 still match the existing behavior. Run the scoring tests and inspect the diff for changes to the special-case conditions. |

The labels for those five cases are `Thirty-All`, `Deuce`, `Advantage player1`, `Advantage player2` and `Win for player1` in the inspected Python implementation. Those checks serve different purposes. A reviewer can inspect the shared definition in the diff, while assertions guard behavior at the edge of the refactor. The test-and-diff checks are this dossier’s proposed application of a checkable outcome. The lesson supplies no evidence that this example prompt would produce a correct patch. [Scoring implementation](https://github.com/emilybache/Tennis-Refactoring-Kata/blob/main/python/tennis2.py#L12-L82) · [Source framework, SRC-0010:C02–C04](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern)

Use as direct practitioner evidence for **BP-10**. The best fit is a review where the symptom is clear enough to anchor to the artifact and the desired change has a meaningful reason or acceptance check. Where the cause is uncertain, describe the observed behavior and treat the proposed fix as provisional. Where an IDE selection is unavailable, give a file, symbol or failing case. The first suggestion is a dossier inference about use under uncertainty. The second adapts the tool-specific recommendation in `SRC-0010:C03`. [“Concept,” SRC-0010:C01–C04](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern)

## Related work, conflicts, and limitations

The project’s Lexler collection contains a ROSE entry credited to Ördög. It shares the framework and the mock-heavy-test example. Its April 17, 2026 repository addition predates the Samman lesson’s June 26 repository addition and identifies Ördög in its authored-by metadata. The publications share practitioner provenance. The Lexler material is a provenance check here and supplies no independent evidence of effectiveness. The Samman lesson’s own contribution is the documented way to teach and practice the technique. [Lexler repository provenance](https://github.com/lexler/augmented-coding-patterns/commit/d3132dbd8d9c78ea5129fdbbdb50b6fe92101134) · [Samman repository provenance](https://github.com/sammancoaching/website/commit/176f1057ab290b4355dfc9cb31fd48a4a49e7f7a)

BP-10 has direct coverage as a practice description. Comparative effectiveness remains open. In particular, the lesson cannot tell a practitioner how much benefit comes from stating the risk, grounding the observation, naming the outcome, adding prompt detail generally or simply giving the agent another attempt. A correct-looking response still leaves the developer with the work of verifying that the proposed change meets the intended outcome. [Complete lesson, including optional kata run](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html)

## Retrieval hints (plain-language user symptoms, families, tags)

- “The agent made the edit I asked for and the underlying problem is still there.”
- “My review comments name a fix but leave out why I care.”
- “The agent rewrote more than I expected because I left the success criteria implicit.”
- “I want to show my team how to give actionable feedback on generated code.”

Families and tags include agent collaboration, code review, corrective feedback, success criteria, review comments, and ROSE.

## Original article access and copyright/permission record

The lesson was publicly accessible on November 21, 2026. Its footer attributes the lesson to Ivett Ördög and sammancoaching.org and explicitly applies Creative Commons Attribution–ShareAlike 4.0 International. The license authorizes sharing the covered lesson with attribution. When sharing an adaptation, indicate changes and apply CC BY-SA 4.0 or a permitted compatible license. This record uses original analysis and an original feedback example. The exercise repository has its own MIT license. [Lesson footer](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html) · [Samman site license](https://sammancoaching.org/LICENSE.html) · [CC BY-SA 4.0 legal code](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en) · [Tennis kata repository license](https://github.com/emilybache/Tennis-Refactoring-Kata/blob/main/license.txt)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0010--verification.md)

## Drive navigation

- [audits/PAT-0005--verification.md](../audits/PAT-0005--verification.md) · [Local copy](../audits/PAT-0005--verification.md)
- [audits/SRC-0010--verification.md](../audits/SRC-0010--verification.md) · [Local copy](../audits/SRC-0010--verification.md)
- [patterns/PAT-0005--turn-review-feedback-into-a-check.md](../patterns/PAT-0005--turn-review-feedback-into-a-check.md) · [Local copy](../patterns/PAT-0005--turn-review-feedback-into-a-check.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/BP-10--rose-feedback.md](../topics/BP-10--rose-feedback.md) · [Local copy](../topics/BP-10--rose-feedback.md)
