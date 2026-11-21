---
topic_id: AP-03
title: Answer injection
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0005
    relationship: DIRECT
    strength: moderate
    finding: "Supplying an incorrect candidate answer inside a factual question decreased accuracy in the tested aggregate."
  - id: SRC-0013
    relationship: DIRECT
    strength: moderate
    finding: "Questions scored lower than matched declaratives on a rubric for expressed sycophancy in a controlled set of advisory scenarios."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic recommends identifying symptoms and success criteria, and offers exploration as an appropriate use of open questions."
pattern_ids: [PAT-0005, PAT-0007]
---

# AP-03 Answer injection

## When it comes up

- “I asked how to fix a race condition, and the agent added locking before checking whether any requests overlapped.”
- “Every answer starts from my proposed design. I wanted a second opinion.”
- “My review comment asks for a certain edit, but I’m still unsure what causes the failure.”

The brief asks whether putting a tentative answer in the question steers the assistant away from other plausible solutions. Experiments show effects on factual correctness, expressed agreement, and alignment with a stated persona. The number or quality of alternative implementations an agent actually considers remains unmeasured.

## Which part of the question changes the answer?

Sharma et al. vary whether a weakly stated candidate answer is supplied inside an otherwise factual question. Across the reported two-dataset free-form aggregate, suggesting a wrong answer lowered accuracy for all tested models. The largest reported loss was about 27 percentage points in one model condition. A separate challenge after an answer sometimes shifted a correct answer to an incorrect one without adding evidence. The two manipulations cover different stages. An opening question can set the model’s direction, and a later unsupported challenge can change a diagnosis already given. `SRC-0005:C03`, `SRC-0005:C05`. [Dossier](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Original, §§3.2–3.3 and Figs. 2–3](https://arxiv.org/html/2310.13548v4)

Dubois et al. vary how the same issue is worded, including as a declaration or a question. Questions score lower than matched declarations on a model-graded rubric covering undue agreement, flattery, and related behaviors. The tested question-reframing interventions also score lower than the study’s direct anti-sycophancy instruction. The rewrite can still present the same proposition. The rubric outcome comes from subjective advisory scenarios, leaving factual correctness open. In the companion fixed-choice political-persona task, GPT-5 picked the persona-aligned option less often with a question stem, while the certainty wording effect in the persona clause was near zero. The main advisory experiment uses newly constructed materials and cites Sharma. The political-persona experiment draws on earlier benchmark research with some authors in common with Sharma. These designs contribute distinct observations without replicating one common outcome. `SRC-0013:C01`, `SRC-0013:C02`, `SRC-0013:C03`, `SRC-0013:C04`, `SRC-0013:C07`, `SRC-0013:C08`. [Dossier](../sources/SRC-0013--ask-without-supplying-the-answer.md) · [Original, §§2.1–2.2 and Figs. 1–2](https://arxiv.org/pdf/2602.23971v4#page=4) · [§2.5 and Fig. 5](https://arxiv.org/pdf/2602.23971v4#page=9)

The two experiments support keeping a developer’s suspicion and the observations that motivated it distinguishable. Anthropic’s product guidance separately recommends specifying the symptom and what success means, with open-ended requests for exploration. It shares an institutional connection with Sharma’s research and supplies workflow advice with a separate provenance and no outcome experiment. In a real codebase, a fixed policy or already verified reproduction can narrow the requested change legitimately. Holding those facts back would weaken the assessment. `SRC-0002:C06`, `SRC-0002:C07`, `SRC-0013:C08`. [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Anthropic, Write a specific prompt](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt)

## Which method fits the work?

Before an edit, [PAT-0007, Ask for an assessment before naming a fix](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md) starts from the symptom, contract, and available evidence. Bring the suspected cause into the conversation after the initial assessment, then compare what the explanations predict and test the difference. Once a patch already exists, [PAT-0005, Turn review feedback into a check](../patterns/PAT-0005--turn-review-feedback-into-a-check.md) helps express a review concern as an observable behavior with room for different implementations. The sequence of those steps and the extra diagnostic probe are coding adaptations. The experiments leave open whether another assessment widens useful search enough to improve repository changes. [PAT-0007 verification](../audits/PAT-0007--verification.md) · [PAT-0005 verification](../audits/PAT-0005--verification.md)

## Drive navigation

- [audits/PAT-0005--verification.md](../audits/PAT-0005--verification.md) · [Local copy](../audits/PAT-0005--verification.md)
- [audits/PAT-0007--verification.md](../audits/PAT-0007--verification.md) · [Local copy](../audits/PAT-0007--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0005--verification.md](../audits/SRC-0005--verification.md) · [Local copy](../audits/SRC-0005--verification.md)
- [audits/SRC-0013--verification.md](../audits/SRC-0013--verification.md) · [Local copy](../audits/SRC-0013--verification.md)
- [patterns/PAT-0005--turn-review-feedback-into-a-check.md](../patterns/PAT-0005--turn-review-feedback-into-a-check.md) · [Local copy](../patterns/PAT-0005--turn-review-feedback-into-a-check.md)
- [patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md) · [Local copy](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0005--sycophancy-and-user-beliefs.md](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Local copy](../sources/SRC-0005--sycophancy-and-user-beliefs.md)
- [sources/SRC-0013--ask-without-supplying-the-answer.md](../sources/SRC-0013--ask-without-supplying-the-answer.md) · [Local copy](../sources/SRC-0013--ask-without-supplying-the-answer.md)
