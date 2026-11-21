---
artifact_id: SRC-0010
artifact_type: source_verification
reviewer: review_rose
reviewed: "2026-11-21"
verdict: PASS
---

# Independent source review of SRC-0010

**PASS.** All seven claims are supported at the stated level. The lesson documents how to teach and use ROSE after an agent produces work. It offers an optional agent trial and reports no results from it. BP-10 has direct support for the practice description. The efficacy of the approach remains an open question. [Source dossier](../sources/SRC-0010--rose-feedback-exercise.md) · [Complete published lesson](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html)

## Numbered findings

| Finding | Item | Independent check |
|---|---|---|
| 1 | Authorship, date and version | The lesson footer credits Ivett Ördög and the contributor profile lists her as an independent consultant. Neither publication nor revision date appears in the lesson. The Samman repository recorded the lesson addition on June 26, 2026 UTC and credits Claude Opus 4.8 in the commit message. I compared the lesson Markdown at the addition commit with the file on the main branch. The text matched. [Contributor and publisher](https://sammancoaching.org/society/contributors/devill.html) · [Original commit](https://github.com/sammancoaching/website/commit/176f1057ab290b4355dfc9cb31fd48a4a49e7f7a) |
| 2 | SRC-0010:C01 | Pass. The opening supplies the author's rationale and the concept section identifies the occasion for feedback as a requested change to an agent's existing solution. The opening asserts a benefit without reporting a comparison. [Opening and concept](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) |
| 3 | SRC-0010:C02 | Pass. The four definitions distinguish the potential harm, what the developer sees in the work, the requested action and the desired result. [Concept, four definitions](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) |
| 4 | SRC-0010:C03 | Pass. The author allows omission and reordering of elements. Pointing to selected code is explicitly conditional on the agent's ability to read the IDE selection. [Concept, paragraphs after definitions](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) |
| 5 | SRC-0010:C04 | Pass. The closing concept bullets distinguish potential longer-term harm from an immediate benefit or change the agent can validate. They supply no quantified outcome. [Concept, final two bullets](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) |
| 6 | SRC-0010:C05 | Pass. The author's test example uses side effects to choose between a real class and a stateful fake. Readability and reduced maintenance burden furnish the motivation. The source supplies neither a patch nor a measured change in either outcome. [Concept, mock example](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) |
| 7 | SRC-0010:C06 | Pass. I checked the lesson sequence, target drawing and optional final step in the kata. Participants draw before seeing the target, annotate example prompts and write feedback on existing code. Sending that feedback to an agent depends on available time. Classroom reactions are facilitator prompts. The published lesson gives no participant observations, agent outputs, study sample or efficacy estimate. [Drawing](https://sammancoaching.org/assets/images/blind_drawing_exercise.png) · [Kata steps](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#write-rose-prompts-for-the-tennis-kata-25-min) |
| 8 | SRC-0010:C07 | Pass. I read all five prompt blocks in the publisher's SVG. The coordinate example specifies where passing individual axis values is permitted. The dependency-management example requests concrete changes and further suggestions. Even where a prompt recounts a previous difficulty, it does not record the result of applying ROSE. [Handout at the addition commit](https://github.com/sammancoaching/website/blob/176f1057ab290b4355dfc9cb31fd48a4a49e7f7a/assets/images/rose_pattern_handout.svg) |
| 9 | Worked example | The Python method repeats point-label selection for ordinary scores. I traced its equal-score, advantage and winning branches for the five given inputs. In order they yield `Thirty-All`, `Deuce`, `Advantage player1`, `Advantage player2` and `Win for player1`. The dossier identifies the proposed refactor, review prompt and acceptance checks as its own application. No execution result is claimed. [Kata description](https://sammancoaching.org/kata_descriptions/tennis.html) · [Python method](https://github.com/emilybache/Tennis-Refactoring-Kata/blob/main/python/tennis2.py#L12-L83) |
| 10 | Dependence | The repository addition of the Lexler entry on April 17, 2026 UTC precedes Samman's June addition. Both have the same GitHub author account. Lexler credits Ördög in the document metadata and supplies the same framework and mock example. Samman adds the teaching activities. Counting the two records as independent evidence would duplicate the practitioner account. [Lexler commit](https://github.com/lexler/augmented-coding-patterns/commit/d3132dbd8d9c78ea5129fdbbdb50b6fe92101134) · [Lexler text at addition](https://raw.githubusercontent.com/lexler/augmented-coding-patterns/d3132dbd8d9c78ea5129fdbbdb50b6fe92101134/documents/patterns/rose-feedback.md) |
| 11 | Rights and originality | The footer expressly attributes the lesson and grants CC BY-SA 4.0. The site requests licensing and attribution information when covered material is reused. The dossier supplies the original credit and license links, identifies ShareAlike for distributed adaptations, and uses its own explanatory prose and worked example. The linked kata software carries a separate MIT license. No figure, full handout or substantial code listing is reproduced in the dossier. [Lesson footer](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html) · [Site reuse instructions](https://sammancoaching.org/LICENSE.html) · [License conditions](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en#s3) · [Kata license](https://github.com/emilybache/Tennis-Refactoring-Kata/blob/main/license.txt) |

## Disposition

No content repairs required. The dates verify repository additions only. This review checked the published exercise and traced its linked code by inspection. It did not run the class, test a coding agent or verify a Drive copy.

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0010--rose-feedback-exercise.md](../sources/SRC-0010--rose-feedback-exercise.md) · [Local copy](../sources/SRC-0010--rose-feedback-exercise.md)
