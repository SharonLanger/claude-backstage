---
topic_id: AP-01
title: Sunk cost / over-iteration
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0002
    relationship: DIRECT
    strength: moderate
    finding: "Anthropic recommends clearing the conversation when two corrections of the same mistake have failed."
  - id: SRC-0003
    relationship: DIRECT
    strength: moderate
    finding: "Model-specific schedules for one specification-only retry beat continued repair at the later tested threshold in nine HumanEval configurations."
  - id: SRC-0008
    relationship: SUPPORTING
    strength: moderate
    finding: "Under matched program caps, the relative yield of fresh candidates and repair varies with model, tasks, and how attempts are allocated."
  - id: SRC-0011
    relationship: SUPPORTING
    strength: low
    finding: "Developers working in familiar repositories reported retrying and reverting AI output."
pattern_ids: [PAT-0001, PAT-0004]
---

# AP-01 Sunk cost / over-iteration

## When it comes up

- “The same case still fails after several corrections, but I’ve already spent half an hour in this chat.”
- “I keep explaining the same requirement and the agent brings back the old version.”
- “The latest edit is different. I can’t tell whether I learned anything that makes another attempt worthwhile.”

The brief asks whether repeatedly correcting a failing conversation wastes effort and proposes diminishing returns after three or four tries. Field accounts establish that developers sometimes retry or revert. A benchmark provides evidence about returns to model repair attempts. The evidence leaves the proposed attempt count and the psychological role of prior investment open.

## Which attempts show diminishing returns?

Adnan and Kuhn start with a generated function, then give failed HumanEval problems up to five feedback-conditioned repairs. Their per-attempt effectiveness counts successes among tasks still unsolved at that step. Earlier successes leave the pool, so later attempts may face harder problems. Table 1 reports variable fit quality across models. In Table 2 an intervention reserves one of the six available attempts for a fresh generation from the original specification. All nine rows improve over continued repair at the later, model-specific threshold and seven improve at the earlier threshold. The other two, Codestral 22B and Devstral 24B, do worse at that earlier threshold. These are the table values, which conflict with parts of the surrounding prose. The policy changes both conversational inputs and the task from repair to generation. The study leaves their separate effects and the cause of the apparent decay unresolved. `SRC-0003:C02`, `SRC-0003:C03`, `SRC-0003:C05`, `SRC-0003:C06`, `SRC-0003:C07`, `SRC-0003:C08`, `SRC-0003:C10`, `SRC-0003:C11`. [Dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Publisher article, Debugging protocol and RQ3](https://www.nature.com/articles/s41598-025-27846-5) · [Table 1](https://www.nature.com/articles/s41598-025-27846-5/tables/1) · [Table 2](https://www.nature.com/articles/s41598-025-27846-5/tables/2)

Olausson et al. compare model repair with independent draws. For GPT-4 on APPS, ten starting programs with up to one repair each beat the 20-fresh-candidate baseline. Two starting programs with up to ten sibling repairs each underperform their own 22-fresh-candidate baseline. Sibling repairs share a parent and differ from a sequence of edits to the previous repair. The differently authored studies share HumanEval in part, and APPS adds distinct tasks. Taken together, they support an opportunity-cost question about the next try, with room for another repair when a developer has useful new failure evidence. `SRC-0008:C01`, `SRC-0008:C02`, `SRC-0008:C04`, `SRC-0008:C05`, `SRC-0008:C06`, `SRC-0008:C11`. [Dossier](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [ICLR paper, §1 and Fig. 3b](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=6)

Becker et al. supply independently collected evidence from real repositories. Developers described retrying as well as checking, editing, and reverting generated output. The study randomly assigned AI availability to issues, leaving individual recovery choices discretionary. It gives no comparison of stop rules or measurement of how prior time investment affects those choices. Anthropic’s separate product guide advises a reset after two unsuccessful corrections of the same mistake. Its rewind feature can restore the conversation, tracked edits, or both. Shell-only changes fall outside the documented checkpoint. The guide’s advice is a working heuristic with a different unit from the benchmark’s model attempts. `SRC-0011:C02`, `SRC-0011:C09`, `SRC-0002:C03`, `SRC-0002:C04`. [Becker dossier](../sources/SRC-0011--review-work-and-developer-time.md) · [Becker et al., §C.1.4, p. 20](https://arxiv.org/pdf/2507.09089v2#page=20) · [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Anthropic, Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session)

## Choosing what to do next

Use [PAT-0001, Recover a drifting coding session](../patterns/PAT-0001--recover-a-drifting-coding-session.md) when the same misunderstanding keeps resurfacing despite clear correction. Preserve the observed failure, settled constraints, and any useful changes before replacing the conversation. If the session still understands the requirement and each attempt produces informative evidence, the recovery pattern offers a focused summary or a continuation. For a bounded change with a reliable check, [PAT-0004, Compare repair with fresh candidates](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) gives the next repair and the fresh draft the same acceptance conditions. Using new evidence as a trigger and accounting for preservation and review costs are workflow judgments. The source record leaves general repository-level returns and the three-to-four-iteration rule unmeasured. [PAT-0001 verification](../audits/PAT-0001--verification.md) · [PAT-0004 verification](../audits/PAT-0004--verification.md)

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
