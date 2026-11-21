---
topic_id: AP-05
title: AI isolation
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0007
    relationship: DIRECT
    strength: moderate
    finding: "Developers reported routing some routine technical questions to AI for immediate and private help while continuing to rely on colleagues for local judgment."
  - id: SRC-0009
    relationship: SUPPORTING
    strength: low
    finding: "A domain-modeling workflow advises surfacing disagreements with stakeholders when local terminology and code imply different outcomes."
pattern_ids: [PAT-0006]
---

# AP-05 AI isolation

## When it comes up

- “I ask the assistant things I used to ask a teammate, especially when the question feels basic.”
- “I used to get informal feedback when I asked around. Now I only talk to someone when I’m stuck on a major decision.”
- “The assistant answered the ticket quickly, but I still need someone who understands the history of that rule.”

The brief asks whether the comfort of asking an assistant causes developers to withdraw from collaboration. There is evidence of changes in whom developers ask, and of comfort as one reason for sending questions to AI. A lasting decline in interaction, mentoring, or pair programming remains unmeasured.

## Which interactions change?

Salomon et al. collected repeated short reports from 30 professional developers and interviewed 22 of that same group. A later survey included 131 eligible respondents whose teams already used generative AI. In phase two, 66 of 131 agreed or strongly agreed that they had shifted technical help toward AI, and 62% found it easier to ask AI without fear of embarrassment. Some described quicker help in asynchronous settings. A private assistant query might replace a teammate question or make it possible to ask something that otherwise would have gone unasked. The study lacks a baseline to estimate either share. The authors collected individual reports through an IDE plugin. These reports are a different measure from interaction logs. `SRC-0007:C01`, `SRC-0007:C02`, `SRC-0007:C03`, `SRC-0007:C11`. [Dossier](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Author manuscript, §§3–4.1, pp. 4–9](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=8) · [§§6.3–6.4, pp. 13–15](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=13)

The same study qualifies a general withdrawal interpretation. While 93 of 131 survey respondents would ask AI about implementing an algorithm, 85 would ask a colleague to clarify business logic or requirements. About 40% reported collaborating more intentionally, and 96 said that working with teammates surfaced alternatives AI had missed. On whether colleague interruptions fell, 37 agreed, 42 disagreed, and 52 were neutral. Some study participants sought social interaction with teammates alongside AI use. Those results describe different activities and fit selective routing and changes in the character of collaboration. They also leave open the authors’ concern about losing incidental learning and informal contact. The survey built on phase one and the published journal record and author manuscript are versions of one study. `SRC-0007:C04`, `SRC-0007:C06`, `SRC-0007:C07`, `SRC-0007:C08`, `SRC-0007:C09`, `SRC-0007:C10`. [Author manuscript, §§4.2–4.4, pp. 9–11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=10) · [§5 and Fig. 3, pp. 11–13](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=12)

## Where a method fits

[PAT-0006, Resolve a domain term before coding](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) gives one concrete reason to involve a teammate. The agent traces two interpretations of a local rule through to observable consequences, and the person responsible settles the intended result. Pocock’s separately authored skill offers practitioner guidance on surfacing contradictions. Its documentation and companion instructions describe one workflow. The guideline and reported preferences support this narrow division of work, with no measured effect on social contact. Team-level evidence would be needed to assess whether practices such as intentional mentoring or informal touchpoints preserve those interactions over time. `SRC-0009:C01`, `SRC-0009:C03`, `SRC-0007:C07`, `SRC-0007:C10`, `SRC-0007:C11`. [Pocock dossier](../sources/SRC-0009--domain-language-and-decisions.md) · [Pocock, Cross-referencing](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops) · [Salomon et al., §5, pp. 11–13](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=12) · [PAT-0006 verification](../audits/PAT-0006--verification.md)

## Drive navigation

- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/SRC-0007--verification.md](../audits/SRC-0007--verification.md) · [Local copy](../audits/SRC-0007--verification.md)
- [audits/SRC-0009--verification.md](../audits/SRC-0009--verification.md) · [Local copy](../audits/SRC-0009--verification.md)
- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0007--developer-collaboration-and-ai.md](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Local copy](../sources/SRC-0007--developer-collaboration-and-ai.md)
- [sources/SRC-0009--domain-language-and-decisions.md](../sources/SRC-0009--domain-language-and-decisions.md) · [Local copy](../sources/SRC-0009--domain-language-and-decisions.md)
