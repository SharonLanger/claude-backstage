---
topic_id: BP-01
title: Knowledge checkpointing
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0002
    relationship: DIRECT
    strength: moderate
    finding: "Anthropic describes saving a specification after a design interview and giving it to a fresh implementation session."
  - id: SRC-0006
    relationship: SUPPORTING
    strength: low
    finding: "Pocock describes carrying the specification into planning and handing bounded tickets to fresh implementation sessions."
  - id: SRC-0003
    relationship: SUPPORTING
    strength: low
    finding: "A fixed original problem statement was sufficient input for the fresh-generation arm of a HumanEval retry comparison."
pattern_ids: [PAT-0001]
---

# BP-01 Knowledge checkpointing

## When it comes up

- “We agreed on the edge cases in chat. If I start a new session, I’ll have to work out those decisions again.”
- “I want to try a different implementation, but the current branch is the only record of what we agreed.”
- “The handoff says what we changed. It leaves out how we’ll know whether it worked.”

The brief asks whether saving the plan before implementation preserves the reasoning needed for inexpensive retries. There is direct practitioner guidance for the handoff. The effect on retry cost and the value of preserving planning relative to preserving working code are open.

## How the evidence fits

Anthropic’s rate-limiter example has the assistant interview the developer about unsettled design choices, save a specification, and start implementation in a fresh session. The guide then uses the specification as a review reference. The example backs preserving agreed behavior before changes begin and carrying it into a subsequent attempt. Writing down a success condition is also explicit guidance. These recommendations come from the same living product guide. `SRC-0002:C05`, `SRC-0002:C06`, `SRC-0002:C10`. [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Brainstorm with Claude first](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first) · [Review against your spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

Pocock independently describes a similar boundary for larger work. A plan or specification feeds the ticket breakdown, then each ticket goes to a fresh implementation session. Where a tracker may truncate the specification, he advises keeping specification and decomposition in the same planning context. The two guides therefore agree on a handoff before implementation. Pocock’s caveat identifies a case where resetting *before* the handoff can lose required information. His tutorial and companion skill definition describe one practice. `SRC-0006:C01`, `SRC-0006:C02`, `SRC-0006:C09`. [Dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [What it does](https://www.aihero.dev/skills-to-tickets#what-it-does) · [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions)

Adnan and Kuhn independently tested generating anew from a fixed original specification after failed attempts on HumanEval. The original problem statement was supplied by the benchmark. The experiment estimates outcomes of changing the retry policy and reports average token costs for two model configurations. The cost of producing, validating, or maintaining a developer’s written plan was outside the design. `SRC-0003:C01`, `SRC-0003:C06`, `SRC-0003:C09`, `SRC-0003:C11`. [Dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Publisher article, RQ3, Strategic fresh start, and Discussion and limitations](https://www.nature.com/articles/s41598-025-27846-5)

## Use in coding work

In [PAT-0001, Recover a drifting coding session](../patterns/PAT-0001--recover-a-drifting-coding-session.md), carry the confirmed behavior, key constraints, and a distinguishing check into a new session. That field selection and the decision to inspect the existing diff for useful changes are catalog adaptations. For a pre-implementation checkpoint, use the guide’s earlier timing for the same handoff. If the written plan still has open decisions or describes an outdated expectation, settle it against the current specification before using it to guide another attempt. [Pattern verification](../audits/PAT-0001--verification.md)

There is no direct comparison here of transcript-only work with a checked written plan, and no measured amount of planning time saved. The cost of another attempt still depends on how much work must be reproduced and verified.

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [audits/SRC-0006--verification.md](../audits/SRC-0006--verification.md) · [Local copy](../audits/SRC-0006--verification.md)
- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
- [sources/SRC-0006--vertical-slices-for-agent-tickets.md](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Local copy](../sources/SRC-0006--vertical-slices-for-agent-tickets.md)
