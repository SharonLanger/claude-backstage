---
topic_id: BP-02
title: Active partnership
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0002
    relationship: DIRECT
    strength: moderate
    finding: "Anthropic recommends an assistant-led interview to resolve design choices before implementation."
  - id: SRC-0009
    relationship: DIRECT
    strength: moderate
    finding: "Pocock’s domain-modeling workflow asks the assistant to surface vague or conflicting requirements and discuss them before editing."
  - id: SRC-0013
    relationship: SUPPORTING
    strength: moderate
    finding: "Question framing reduced measured agreement compared with stating a view in tested advisory scenarios."
  - id: SRC-0005
    relationship: SUPPORTING
    strength: moderate
    finding: "Incorrect suggestions reduced accuracy in factual questions, and unsupported challenges sometimes displaced correct initial answers."
  - id: SRC-0007
    relationship: SUPPORTING
    strength: moderate
    finding: "Surveyed developers often chose AI for implementation brainstorming and colleagues for clarifying business logic."
  - id: SRC-0022
    relationship: SUPPORTING
    strength: moderate
    finding: "Public coding-agent logs show cases where developers surfaced an ambiguous requirement or corrected an agent after a divergence."
pattern_ids: [PAT-0006, PAT-0007]
---

# BP-02 Active partnership

## When it comes up

- “It starts coding while we still disagree about what the feature should do.”
- “I get an implementation of my first idea when I wanted help deciding whether it was sound.”
- “The ticket and the existing behavior clash, and the assistant picked one without asking.”

The brief asks how to get a two-way technical dialogue, including appropriate pushback. The accepted guidance describes specific forms of that dialogue. The cognitive and task-outcome effects of assigning the assistant a collaborator role remain open.

## How the evidence fits

Anthropic’s example asks the assistant to interview the developer about a design before choosing behavior. Pocock’s example gives the assistant a concrete reason to push back by checking the requested behavior against existing code and raising the discrepancy for discussion. These separately authored guides propose complementary actions. Neither evaluates a general instruction to disagree proactively or reports how often the assistant catches genuine contradictions. Pocock’s tutorial and linked skill definition describe the same workflow. `SRC-0002:C05`, `SRC-0002:C06`, `SRC-0009:C01`, `SRC-0009:C03`, `SRC-0009:C05`. [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Brainstorm with Claude first](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first) · [Pocock dossier](../sources/SRC-0009--domain-language-and-decisions.md) · [Cross-referencing, and where it stops](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops)

Dubois et al. found less expressed sycophancy on largely subjective advisory questions than on matched declarations. Their tested question rewrites also outperformed their explicit anti-sycophancy instruction on that rubric. The question still concerned the same proposition. In Sharma et al.’s experiment, a suggested but incorrect answer reduced accuracy even in a factual question. They also observed that an unsupported user challenge sometimes made a correct answer become incorrect. These results suggest limiting stance cues while a diagnosis is open and asking what evidence would distinguish the alternatives. The studies provide separate advisory and factual experiments with different outcomes. Dubois’s additional forced-choice arm uses Perez et al.’s political materials, whose byline overlaps Sharma’s. Sharma’s experiment and Anthropic’s later product advice contribute different types of evidence. `SRC-0013:C02`, `SRC-0013:C04`, `SRC-0013:C07`, `SRC-0013:C08`, `SRC-0005:C03`, `SRC-0005:C05`. [Dubois dossier](../sources/SRC-0013--ask-without-supplying-the-answer.md) · [Dubois §§2.1–2.2 and 2.5](https://arxiv.org/html/2602.23971v4) · [Sharma dossier](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Sharma §§3.2–3.3, Figs. 2–3](https://arxiv.org/html/2310.13548v4)

Salomon et al.’s separate organizational study describes where developers take different questions. Respondents frequently chose AI for implementation brainstorming (77 of 131) and colleagues for clarifying business logic or requirements (85 of 131). Interviews also describe AI exploration followed by conversations with teammates about context and tradeoffs. The survey choices capture stated preferences in an AI-using sample. They help delimit where a colleague supplies decision authority or project history. `SRC-0007:C01`, `SRC-0007:C02`, `SRC-0007:C06`, `SRC-0007:C07`, `SRC-0007:C08`. [Dossier](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Table 3G, p. 8](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=8) · [§§4.3–4.4, pp. 10–11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=10)

Tang et al. add observations from public coding-agent sessions. In one example, the assistant interpreted pagination as infinite scrolling and the developer then asked how to reach the next page. Among the 1,504 episodes with visible resolution, 91.49% were coded as agent fixes after developer pushback. Resolution was unknown in 90.67% of all validated episodes. The study selects divergences that developers made visible in the log, so these figures describe observed correction and leave the benefit of proactive clarification unmeasured. The session analysis contributes evidence distinct from surveys and prompted experiments, and it reuses the SpecStory collection and SWE-chat data. `SRC-0022:C01`, `SRC-0022:C09`, `SRC-0022:C13`, `SRC-0022:C17`, `SRC-0022:C18`. [Dossier](../sources/SRC-0022--observed-developer-agent-misalignment.md) · [ACL record](https://aclanthology.org/2026.emnlp-main.1011/) · [Scope and sample, §§3.1–3.2, p. 23266](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=3) · [Figure 2 and Table 4, p. 23270](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=7) · [Design implications, §5, p. 23272](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=9) · [Pagination episode, Appendix C, p. 23277](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=14)

## Use in coding work

[PAT-0006, Resolve a domain term before coding](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) makes disagreement actionable by tracing a disputed term to code and examples and asking the responsible person to settle its meaning. [PAT-0007, Ask for an assessment before naming a fix](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md) starts an open diagnosis with observations and asks what would distinguish plausible explanations. Both retain confirmed requirements. Inviting disagreement, testing a rival explanation, and assigning decision authority are catalog applications of narrower evidence. There is no controlled test here of a general pushback instruction, multi-turn collaboration quality, or improved repository outcomes. [PAT-0006 verification](../audits/PAT-0006--verification.md) · [PAT-0007 verification](../audits/PAT-0007--verification.md)

## Drive navigation

- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/PAT-0007--verification.md](../audits/PAT-0007--verification.md) · [Local copy](../audits/PAT-0007--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0005--verification.md](../audits/SRC-0005--verification.md) · [Local copy](../audits/SRC-0005--verification.md)
- [audits/SRC-0007--verification.md](../audits/SRC-0007--verification.md) · [Local copy](../audits/SRC-0007--verification.md)
- [audits/SRC-0009--verification.md](../audits/SRC-0009--verification.md) · [Local copy](../audits/SRC-0009--verification.md)
- [audits/SRC-0013--verification.md](../audits/SRC-0013--verification.md) · [Local copy](../audits/SRC-0013--verification.md)
- [audits/SRC-0022--verification.md](../audits/SRC-0022--verification.md) · [Local copy](../audits/SRC-0022--verification.md)
- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md) · [Local copy](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0005--sycophancy-and-user-beliefs.md](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Local copy](../sources/SRC-0005--sycophancy-and-user-beliefs.md)
- [sources/SRC-0007--developer-collaboration-and-ai.md](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Local copy](../sources/SRC-0007--developer-collaboration-and-ai.md)
- [sources/SRC-0009--domain-language-and-decisions.md](../sources/SRC-0009--domain-language-and-decisions.md) · [Local copy](../sources/SRC-0009--domain-language-and-decisions.md)
- [sources/SRC-0013--ask-without-supplying-the-answer.md](../sources/SRC-0013--ask-without-supplying-the-answer.md) · [Local copy](../sources/SRC-0013--ask-without-supplying-the-answer.md)
- [sources/SRC-0022--observed-developer-agent-misalignment.md](../sources/SRC-0022--observed-developer-agent-misalignment.md) · [Local copy](../sources/SRC-0022--observed-developer-agent-misalignment.md)
