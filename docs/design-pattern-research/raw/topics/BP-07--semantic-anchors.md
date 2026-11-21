---
topic_id: BP-07
title: Semantic anchors
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0009
    relationship: DIRECT
    strength: moderate
    finding: "Pocock documents agreeing on recurring domain terms with concrete cases and reusing short glossary definitions at naming boundaries."
  - id: SRC-0004
    relationship: SUPPORTING
    strength: low
    finding: "CloudAPIBench reports a call-validity gap between common and rare APIs and a strong benefit from including a relevant signature in one controlled condition."
pattern_ids: [PAT-0006]
---

# BP-07 Semantic anchors

## When it comes up

- “The ticket and the generated code both say ‘active account,’ but they count different customers.”
- “We agreed what ‘settled’ means. A new session just used the everyday meaning again.”
- “Can I refer to our model by name, or should every prompt explain its behavior?”

The brief proposes that a familiar term can bring a stable behavior to mind for the model and stand in for a longer prompt. The accepted evidence directly documents a narrower practice. A team can establish a concise term with a discoverable definition and use it across design, implementation and review. Reliable model activation from a term alone and equivalent results with fewer prompt tokens are open questions.

## What the sources establish

Pocock’s domain-modeling workflow probes vague terms with examples, resolves conflicting meanings against the team and the code, and records an agreed definition. The glossary keeps vocabulary at the scope where it applies. The published article, skill definition and format file describe one practitioner contribution. His FAQ explicitly raises plain English as a plausible alternative and warns that unreviewed definitions can give a guess the appearance of agreement. He reports skipped automatic skill invocation, which makes mere availability of definitions an uncertain way to expose them to a session. SRC-0009:C01–C03, SRC-0009:C06 and SRC-0009:C07. [Domain-modeling dossier](../sources/SRC-0009--domain-language-and-decisions.md) · [Intended workflow](https://www.aihero.dev/skills-domain-modeling#what-it-does) · [Glossary format](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/GLOSSARY-FORMAT.md#rules) · [Invocation and scope](https://www.aihero.dev/skills-domain-modeling#when-to-reach-for-it) · [FAQ](https://www.aihero.dev/skills-domain-modeling#common-questions)

A separate coding study gives a reason to distinguish a label from the information attached to it. In CloudAPIBench, every tested configuration had a lower rate of signature-valid calls for the rarest API slice than for the commonest. The frequency bins are based on approximate public exposure and the comparison does not isolate how often a model has learned a term. In a controlled StarCoder2-3B condition with the correct document, the signature plus description used less than one-seventh of the added tokens of longer documentation and scored 87.14% versus 88.75% validity. That comparison concerns the compression of a specific technical reference for a syntactic call check. It gives no success rate for using a well-known design term to get the desired semantics. Retrieved material for the wrong operation can also hurt. SRC-0004:C01, SRC-0004:C02, SRC-0004:C05 and SRC-0004:C06. [API documentation dossier](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Task and frequency bins, §II and Table II](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=4) · [Documentation length, §III-B and Fig. 6](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5) · [Retrieval precision, Fig. 7](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=7)

## How to use an agreed term

[PAT-0006, Resolve a domain term before coding](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) starts with a case that separates the readings. For “active account,” ask whether an account with an unpaid invoice and a login last week belongs in the reported total. An owner can settle the result, the glossary can name the concept within the reporting domain, and the review can check that case. Supplying the short definition where the model can see it and preserving the deciding example in an acceptance check are ways to apply the practitioner method. Consistent names and the length of a ticket are observable locally. A claim about equivalent model behavior would need a comparison of a term alone, a term plus definition, and plain English on the same behavior. [Pattern verification](../audits/PAT-0006--verification.md)

## Drive navigation

- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/SRC-0004--verification.md](../audits/SRC-0004--verification.md) · [Local copy](../audits/SRC-0004--verification.md)
- [audits/SRC-0009--verification.md](../audits/SRC-0009--verification.md) · [Local copy](../audits/SRC-0009--verification.md)
- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0004--api-documentation-and-hallucinations.md](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Local copy](../sources/SRC-0004--api-documentation-and-hallucinations.md)
- [sources/SRC-0009--domain-language-and-decisions.md](../sources/SRC-0009--domain-language-and-decisions.md) · [Local copy](../sources/SRC-0009--domain-language-and-decisions.md)
