---
topic_id: AP-09
title: "Silent misalignment"
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0022
    relationship: SUPPORTING
    strength: moderate
    finding: "Public coding-session logs show agents acting on an inferred intent or reporting completion before the developer surfaces a mismatch."
  - id: SRC-0009
    relationship: DIRECT
    strength: low
    finding: "Pocock documents a workflow that challenges conflicting domain meanings and surfaces discrepancies between stated and current behavior before edits."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic recommends eliciting a specification through questions and checking the resulting diff against requirements and edge cases."
  - id: SRC-0021
    relationship: SUPPORTING
    strength: low
    finding: "A constructed question-correction benchmark shows varying ability to identify and correct faulty premises or invalid answer choices."
pattern_ids: [PAT-0006]
---

# AP-09 Silent misalignment

- “The agent said it understood both requirements, then built something that satisfies only one.”
- “I found out in the demo that ‘paginate’ meant infinite scroll to the agent.”
- “It said all flows were verified, but the first run in my environment failed.”

The brief asks whether an agent accepts contradictory or nonsensical instructions without challenging them, leaving a mismatch undetected. Available studies show coding mismatches that developers later surfaced and errors on a constructed task for correcting faulty premises. Practitioner guidance describes how to ask for a decision before editing and expose divergent behavior afterward. How often coding agents raise an actual contradiction on their own, how many mismatches go entirely unnoticed, and whether a particular clarification procedure changes either rate remain open.

## How the mismatch became visible

Tang and colleagues used public logs from **20,574 sessions** and retained **16,118 episodes** after checking supporting evidence. The entry criterion requires visible subsequent developer correction or dissatisfaction. One agent implemented infinite scroll before the developer asked how to move to the next page, suggesting an unresolved choice about pagination. Another declared functionality complete before the developer reported a runtime failure. These examples establish divergent behavior or reporting without identifying an expression of contradictory instructions in either request. The study codes **38.33%** of retained episodes as explicit constraint violations and **26.95%** as misread intent, with multiple labels allowed. SRC-0022:C01–C03, C07, C09, C11. [Dossier](../sources/SRC-0022--observed-developer-agent-misalignment.md) · [§§3.1–3.2, sampling and scope](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=3) · [§4.1, Table 3](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=6) · [Appendix C, pagination](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=13) · [Appendix C, completion claim](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=15)

In the **1,504** retained cases with a visible resolution, **91.49%** were fixed by the agent after explicit developer pushback. This measures observed repair after a human raised the problem. An agent that flags and resolves a contradiction before a divergence would give the study no episode to count. Mismatches fixed or missed outside the visible conversation can also escape the sample. The proceedings paper and its preprint represent one study, which re-crawled the public SpecStory collection used in earlier work and reused SWE-chat sessions. Dataset overlap precludes treating those publications as fully independent replication. SRC-0022:C01, C13, C18. [§4.2, Table 4](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=7) · [Limitations](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=10) · [Earlier SpecStory collection](https://arxiv.org/html/2604.00436v1#S3.SS1) · [SWE-chat dataset methodology](https://arxiv.org/html/2604.20779v1#S2)

Inverse IFEval independently scores a form of pushback through its Question Correction category. The model earns credit for detecting and correcting a bad premise or missing valid answer. An illustrated item has a computable answer absent from the choices, and an error example shows a model calculating the result and then choosing an offered answer anyway. Scores vary by model and category. This is evidence about premise correction under an explicit benchmark rubric. Ordinary repository work adds longer interaction and competing sources of authority that the task does not cover. It leaves open whether an agent will identify a contradiction between a product requirement and a repository rule before acting. SRC-0021:C06, C08, C10, C12. [Dossier](../sources/SRC-0021--instructions-against-learned-conventions.md) · [§§2.2–2.4, categories and tasks](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=4) · [§3.1, Table 2](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=7) · [Appendix F, example errors](https://proceedings.iclr.cc/paper_files/paper/2026/file/d1a1e8713fcd5626656553c82f7c3b26-Paper-Conference.pdf#page=21)

## Surface the decision and check its outcome

Pocock’s documented practice cross-references a term or statement against code and committed decisions, then asks about a discrepancy before editing. The article and its companion skill instructions describe a single method. A user report illustrates its discovery limit when a decision lives only in an issue tracker. Anthropic’s separately authored guide recommends interviewing for a spec, getting a runnable check and comparing the resulting diff with the agreed spec. Agreement with a written spec can still preserve an assumption that the spec never made explicit. These procedures are documented guidance. Neither source supplies an experimental comparison for detecting contradictions or preventing unnoticed failures. SRC-0009:C01, C03, C05 and SRC-0002:C05, C07–C10. [Domain-modeling dossier](../sources/SRC-0009--domain-language-and-decisions.md) · [Cross-reference scope and example](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops) · [Claude Code dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Specification interview](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first) · [Review against the spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

[PAT-0006, Resolve a domain term before coding](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) gives a concrete checkpoint for ambiguous terms and claims that conflict with existing behavior. Ask the agent to point to the two statements or behaviors, state what each implies for one input, and take the resulting decision to the owner before editing the affected behavior. For pagination, a ticket can ask whether loading the next page requires an explicit action and what happens when the visitor returns to an earlier page. Preserve the owner’s answer as an acceptance check. For an already-produced patch, inspect the observable results against that check. The pattern is a way for a developer to solicit and verify a distinction. Its applicability assumes the project can identify the requirements and an owner who can settle a consequential disagreement. [Pattern verification](../audits/PAT-0006--verification.md)

## Drive navigation

- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0009--verification.md](../audits/SRC-0009--verification.md) · [Local copy](../audits/SRC-0009--verification.md)
- [audits/SRC-0021--verification.md](../audits/SRC-0021--verification.md) · [Local copy](../audits/SRC-0021--verification.md)
- [audits/SRC-0022--verification.md](../audits/SRC-0022--verification.md) · [Local copy](../audits/SRC-0022--verification.md)
- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0009--domain-language-and-decisions.md](../sources/SRC-0009--domain-language-and-decisions.md) · [Local copy](../sources/SRC-0009--domain-language-and-decisions.md)
- [sources/SRC-0021--instructions-against-learned-conventions.md](../sources/SRC-0021--instructions-against-learned-conventions.md) · [Local copy](../sources/SRC-0021--instructions-against-learned-conventions.md)
- [sources/SRC-0022--observed-developer-agent-misalignment.md](../sources/SRC-0022--observed-developer-agent-misalignment.md) · [Local copy](../sources/SRC-0022--observed-developer-agent-misalignment.md)
