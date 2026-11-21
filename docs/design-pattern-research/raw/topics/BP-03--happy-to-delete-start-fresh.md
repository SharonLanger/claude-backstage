---
topic_id: BP-03
title: Happy to delete / start fresh
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0003
    relationship: DIRECT
    strength: moderate
    finding: "A scheduled spec-only fresh generation improved final solve rate over continued repair at the later tested threshold across nine HumanEval model configurations."
  - id: SRC-0002
    relationship: DIRECT
    strength: moderate
    finding: "Anthropic recommends a conversation reset after repeated failed corrections and describes distinct conversation and file restore choices."
  - id: SRC-0008
    relationship: SUPPORTING
    strength: moderate
    finding: "Matched candidate-budget experiments show that the relative return on repairs and fresh samples varies by model, task set, and budget allocation."
  - id: SRC-0011
    relationship: SUPPORTING
    strength: low
    finding: "Open-source developers reported checking, editing, retrying, and reverting generated output during ordinary work."
pattern_ids: [PAT-0001, PAT-0004]
---

# BP-03 Happy to delete / start fresh

## When it comes up

- “Every patch changes a little more code and the same case still fails.”
- “I can describe what the change should do. Should I keep repairing this version or generate another?”
- “I want to leave this conversation behind. Some of its edits still look useful.”

The brief asks whether disposing of AI-generated code and starting again beats patching it. Published results support reserving a fresh attempt for some bounded problems. The cost and success of discarding a repository-wide change remain unmeasured.

## How the evidence fits

Adnan and Kuhn give unresolved HumanEval tasks up to six total attempts under either continued feedback-conditioned repair or a policy with a scheduled fresh generation from the original problem statement. In Table 2, all nine configurations improve at the later model-specific threshold. At the earlier threshold, seven improve and Codestral 22B and Devstral 24B decline. The counts come from the table because the accompanying prose conflicts with it. The fresh attempt removes the prior repair inputs and changes the request to generating anew. The experiment leaves context effects, fixation, and other mechanisms unresolved. `SRC-0003:C01`, `SRC-0003:C02`, `SRC-0003:C06`, `SRC-0003:C07`, `SRC-0003:C08`, `SRC-0003:C10`, `SRC-0003:C11`. [Dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Publisher article, RQ3 and Strategic fresh start](https://www.nature.com/articles/s41598-025-27846-5) · [Table 2](https://www.nature.com/articles/s41598-025-27846-5/tables/2)

Olausson et al. compare independent draws with policies that reserve some candidate slots for repair. For GPT-4 on APPS, ten initial candidates plus up to one repair apiece scored 66.1% versus 63.1% for 20 fresh draws. Two initial candidates plus up to ten sibling repairs apiece scored 61.8% versus 63.4% for 22 fresh draws. Each result has its own matched program cap. The sibling repairs share a starting program. Adnan and Kuhn’s baseline instead repairs successive predecessors. The studies have different investigators, share HumanEval in part, and offer different designs. APPS contributes a different set of tasks. The journal article and PMC record are versions of one contribution. Its protocol builds on PyCapsule, which shares investigators. The combined evidence leaves room for repair as well as another fresh draw. `SRC-0008:C01`, `SRC-0008:C02`, `SRC-0008:C05`, `SRC-0008:C06`, `SRC-0008:C07`, `SRC-0003:C02`, `SRC-0003:C06`. [Olausson dossier](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [ICLR §1 and Fig. 3b, pp. 2 and 6](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=6) · [Adnan and Kuhn provenance audit](../audits/SRC-0003--verification.md)

Anthropic separately advises resetting a conversation after two unsuccessful corrections to the same mistake. This is a heuristic for its product. Its rewind feature can address conversation, tracked code, or both. Shell-only edits fall outside the described checkpoint. Becker et al. independently report developers reverting outputs in real repositories. Their trial assigned AI availability, leaving reversion and repair choices to the developer. It supplies examples of the behavior, with no relative success estimate for the alternatives. `SRC-0002:C03`, `SRC-0002:C04`, `SRC-0011:C02`, `SRC-0011:C09`. [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session) · [Becker dossier](../sources/SRC-0011--review-work-and-developer-time.md) · [Becker article](https://arxiv.org/html/2507.09089v2) · [§C.1.4, p. 20](https://arxiv.org/pdf/2507.09089v2#page=20)

## Use in coding work

[PAT-0001, Recover a drifting coding session](../patterns/PAT-0001--recover-a-drifting-coding-session.md) helps when the conversation keeps restoring an obsolete assumption. Use [PAT-0004, Compare repair with fresh candidates](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) when one small, testable change could be repaired or attempted again. The methods treat a fresh session, preserving useful edits, and testing a replacement as separate choices. Keeping the current version recoverable and running common acceptance checks are catalog adaptations. A universal retry count, a human sunk-cost effect, and a general advantage for deleting working repository changes remain open. [PAT-0001 verification](../audits/PAT-0001--verification.md) · [PAT-0004 verification](../audits/PAT-0004--verification.md)

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/PAT-0004--verification.md](../audits/PAT-0004--verification.md) · [Local copy](../audits/PAT-0004--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [audits/SRC-0008--verification.md](../audits/SRC-0008--verification.md) · [Local copy](../audits/SRC-0008--verification.md)
- [audits/SRC-0011--verification.md](../audits/SRC-0011--verification.md) · [Local copy](../audits/SRC-0011--verification.md)
- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [patterns/PAT-0004--compare-repair-with-fresh-candidates.md](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) · [Local copy](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
- [sources/SRC-0008--self-repair-versus-fresh-samples.md](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Local copy](../sources/SRC-0008--self-repair-versus-fresh-samples.md)
- [sources/SRC-0011--review-work-and-developer-time.md](../sources/SRC-0011--review-work-and-developer-time.md) · [Local copy](../sources/SRC-0011--review-work-and-developer-time.md)
