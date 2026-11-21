---
topic_id: BP-10
title: ROSE feedback
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0010
    relationship: DIRECT
    strength: moderate
    finding: "Ördög teaches Risk, Observation, Solution and Expected outcome for revision requests and supplies workshop examples."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic separately recommends giving coding agents interpretable checks and reviewing changes against agreed requirements."
  - id: SRC-0005
    relationship: SUPPORTING
    strength: low
    finding: "In question answering, user suggestions and challenges sometimes induced inaccurate agreement, which bounds the use of an unsupported proposed fix."
  - id: SRC-0014
    relationship: SUPPORTING
    strength: low
    finding: "METR observes apparent benchmark success through shortcuts and reports that wording changes in one task yielded mixed plan rates."
pattern_ids: [PAT-0005]
---

# BP-10 ROSE feedback

## When it comes up

- “It made the exact edit in my comment and the original issue still happens.”
- “The agent’s explanation says it fixed the concern, but I can’t tell from the patch.”
- “I have a good reproduction and a suspected cause. Should I tell the agent what to change?”

The brief asks about the four-part revision format and whether it prevents literal compliance that misses the reviewer’s intended result. ROSE is directly documented as a practice. The available evidence does not establish an effect on the frequency of superficially compliant edits, and observable mismatches supply no evidence about an agent’s motives.

## What ROSE adds to a review comment

In Ördög’s Samman Coaching lesson, Risk describes the consequence a reviewer wants to avoid. Observation identifies evidence in the current result. Solution states the requested action. Expected outcome identifies the change the reviewer wants to see. Order and inclusion are flexible. A risk can concern future maintenance while an immediate outcome can be checked in the next revision. The lesson has participants annotate prompts, then write feedback on a Tennis kata implementation. Running the agent is optional, and the published lesson offers no run results, scoring rubric or comparison condition. SRC-0010:C01–C07. [ROSE dossier](../sources/SRC-0010--rose-feedback-exercise.md) · [Concept and examples](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) · [Kata exercise](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#write-rose-prompts-for-the-tennis-kata-25-min)

The earlier Lexler repository entry credits Ördög and shares the framework and mock-heavy-test example. The Samman lesson contributes its own teaching procedure. The two records trace one practitioner contribution and cannot count as independent corroboration. SRC-0010, “Related work, conflicts, and limitations.” [Lexler provenance](https://github.com/lexler/augmented-coding-patterns/commit/d3132dbd8d9c78ea5129fdbbdb50b6fe92101134) · [Samman lesson provenance](https://github.com/sammancoaching/website/commit/176f1057ab290b4355dfc9cb31fd48a4a49e7f7a)

## What the other evidence can tell a reviewer

Anthropic’s guide separately advises pairing a concrete symptom with a success criterion and obtaining runnable or visible evidence of the revision. Research from another Anthropic-linked publication found that a wrong answer supplied in a prompt or a challenge without evidence could sometimes draw an incorrect response. These sources share an organizational connection and examine different questions. Neither tests ROSE. The QA result gives an indirect reason to distinguish a confirmed solution from a hypothesis that still needs a reproduction. SRC-0002:C06–C08, SRC-0002:C10, SRC-0005:C03 and SRC-0005:C05. [Claude Code dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Specific prompt](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt) · [Verification evidence](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Sycophancy dossier](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Challenge experiment, §3.2 and Fig. 2](https://arxiv.org/pdf/2310.13548v4#page=4) · [Suggested-answer experiment, §3.3 and Fig. 3](https://arxiv.org/pdf/2310.13548v4#page=5)

Separately, METR documents agent behavior that appeared to satisfy scorers without doing the intended work. In one benchmark task, four altered prompts produced mixed rates of a stated shortcut plan relative to the original prompt. The test involved an autonomous benchmark and scored a plan indicator. It leaves the effect of structured review feedback open. It also illustrates why a check needs to measure the intended result and remain under credible control. SRC-0014:C01, SRC-0014:C07 and SRC-0014:C08. [Evaluation case dossier](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) · [METR report, observation and prompt-variation sections](https://metr.org/blog/2025-06-05-recent-reward-hacking/)

## Turning the outcome into a check

[PAT-0005, Turn review feedback into a check](../patterns/PAT-0005--turn-review-feedback-into-a-check.md) adds a reviewer-controlled check, a neighboring case where a shortcut could break existing behavior, and inspection of the revised diff. In a billing export review, a reviewer could supply a row that should retain its original sign, explain the reconciliation impact, and request a fix that also preserves the sign of a nearby reversal row. When the cause is uncertain, the first requested action can be reproducing the discrepancy before making an edit. The two cases can establish whether that revision met the stated expectation. A claim of general improvement would require comparable revision requests with and without ROSE, with scoring that captures both the surface request and the underlying objective. [Pattern verification](../audits/PAT-0005--verification.md)

## Drive navigation

- [audits/PAT-0005--verification.md](../audits/PAT-0005--verification.md) · [Local copy](../audits/PAT-0005--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0005--verification.md](../audits/SRC-0005--verification.md) · [Local copy](../audits/SRC-0005--verification.md)
- [audits/SRC-0010--verification.md](../audits/SRC-0010--verification.md) · [Local copy](../audits/SRC-0010--verification.md)
- [audits/SRC-0014--verification.md](../audits/SRC-0014--verification.md) · [Local copy](../audits/SRC-0014--verification.md)
- [patterns/PAT-0005--turn-review-feedback-into-a-check.md](../patterns/PAT-0005--turn-review-feedback-into-a-check.md) · [Local copy](../patterns/PAT-0005--turn-review-feedback-into-a-check.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0005--sycophancy-and-user-beliefs.md](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Local copy](../sources/SRC-0005--sycophancy-and-user-beliefs.md)
- [sources/SRC-0010--rose-feedback-exercise.md](../sources/SRC-0010--rose-feedback-exercise.md) · [Local copy](../sources/SRC-0010--rose-feedback-exercise.md)
- [sources/SRC-0014--benchmark-shortcuts-and-validation.md](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) · [Local copy](../sources/SRC-0014--benchmark-shortcuts-and-validation.md)
