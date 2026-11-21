---
topic_id: OB-10
title: "Limited attention / focus"
coverage: partially supported
source_edges:
  - id: SRC-0001
    relationship: DIRECT
    strength: high
    finding: "The same evidence yielded different answer accuracy depending on its position, and adding more retrieved passages had diminishing gains in the tested pipeline."
  - id: SRC-0004
    relationship: SUPPORTING
    strength: moderate
    finding: "Adding documentation helped when it matched the target call, while imperfect retrieval harmed some previously easy calls."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "The coding guide recommends short always-loaded instructions and scoped rules alongside a less aggressive default for managing current context windows."
pattern_ids: [PAT-0001, PAT-0002]
publication_status: published
---

# OB-10 — Limited attention / focus

“The assistant had the relevant declaration, but it followed an example from another version.” “The answer got less accurate after I pasted more files.” The brief asks whether the quantity of supplied context dilutes quality and whether all loaded material competes for attention. The evidence establishes that placement and relevance affect measured performance. It leaves the internal mechanism and any universal usable-context limit open.

## Placement, relevance and quantity

Liu et al. place the same answer-bearing paragraph at different locations among other documents in a single prompt. Many tested models achieved lower open-domain question-answering accuracy when the evidence sat in the middle of the input. The effect varied across checkpoints and tasks. Claude-1.3 variants were nearly perfect on the separate UUID lookup at evaluated lengths. Giving the question both before and after the key-value data brought GPT-3.5-Turbo (16K) to perfect 300-pair retrieval, but the corresponding layout gave small gains at the first position and small losses elsewhere in question answering. In the open-domain retrieval pipeline, moving from 20 to 50 passages raised answer accuracy roughly one to 1.5 percentage points for the named model variants even as recall kept improving. That is diminishing return in those conditions, with some useful extra material still reaching the model. SRC-0001:C01–C06, C08, C10–C11, §2.3 Fig. 5, §3 Fig. 7, §4.2 Fig. 9 and §5 Fig. 11. [Dossier](../sources/SRC-0001--lost-in-the-middle.md) · [Original paper](https://aclanthology.org/2024.tacl-1.9/)

Jain et al. reach a complementary result in a distinct coding benchmark. With guaranteed correct documentation, a signature plus description gave StarCoder2-3B 87.14% valid calls, and the longer document gave 88.75% using over seven times the added tokens. With a controlled 50% inclusion rate for the correct document, unconditional retrieval helped GPT-4o's low-frequency call slice and hurt its high-frequency slice. That contrast concerns the contents of the retrieved material and the difficulty of the target operation. It cannot be attributed to token count alone. SRC-0004:C05–C08, §III-B Figs. 6–7 and §IV-C Table IV. [Dossier](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Conference manuscript](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5)

## What transfers to a coding session

Anthropic's current Claude Code guide advises short repo-wide guidance and loading narrower rules when their scope applies. It also says most current models with automatic compaction need less aggressive window management by default while still recommending clearing between unrelated tasks. That product recommendation can coexist with the benchmark effects because the guide addresses a managed multi-turn workflow and supplies no measured performance curve across context loads. Liu and Jain offer independently originated behavioral comparisons. Anthropic is a separate practitioner account, with no replication of either experiment. Neither benchmark measures competition between every file in an agent's session or proves a particular attention mechanism. Multi-turn loss of an earlier requirement is a related question in OB-01. SRC-0002:C01–C02, C13–C14 and C17. [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Current guide](https://code.claude.com/docs/en/best-practices#what-you-can-stop-doing)

[Recover a drifting coding session](../patterns/PAT-0001--recover-a-drifting-coding-session.md) is applicable once a live task repeatedly misses a clear constraint and a checked handoff is possible. [Verify an unfamiliar API call](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) fits when the ambiguity is which version or operation applies. These are task-specific responses. The experiments supply no universal passage limit, file count, context utilization percentage or guarantee that repeating key text helps.

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/PAT-0002--verification.md](../audits/PAT-0002--verification.md) · [Local copy](../audits/PAT-0002--verification.md)
- [audits/SRC-0001--verification.md](../audits/SRC-0001--verification.md) · [Local copy](../audits/SRC-0001--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0004--verification.md](../audits/SRC-0004--verification.md) · [Local copy](../audits/SRC-0004--verification.md)
- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [patterns/PAT-0002--verify-an-unfamiliar-api-call.md](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) · [Local copy](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0001--lost-in-the-middle.md](../sources/SRC-0001--lost-in-the-middle.md) · [Local copy](../sources/SRC-0001--lost-in-the-middle.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0004--api-documentation-and-hallucinations.md](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Local copy](../sources/SRC-0004--api-documentation-and-hallucinations.md)
