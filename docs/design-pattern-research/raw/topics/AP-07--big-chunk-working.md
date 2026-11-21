---
topic_id: AP-07
title: "Big chunk working"
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0024
    relationship: CONTRADICTORY
    strength: moderate
    finding: "In a selected sample of merged pull requests, Agentic-labeled changes ranked lower on distinct commits and cumulative line changes than Human-labeled changes."
  - id: SRC-0006
    relationship: DIRECT
    strength: moderate
    finding: "Pocock describes a workflow that breaks planned features into demonstrable behaviors, with guidance for dependencies and coupled refactors."
  - id: SRC-0011
    relationship: SUPPORTING
    strength: low
    finding: "Recorded sessions document contributor time spent checking and cleaning generated output, leaving any effect of batch size on review effort unmeasured."
pattern_ids: [PAT-0003]
---

# AP-07 Big chunk working

- “I asked for one feature. The assistant implemented three and refactored every caller.”
- “The change is too broad to explain in one review. Can we land something useful first?”
- “We split it into smaller diffs. None can be exercised until the final one lands.”

The brief connects AI-enabled batch size to unreviewable pull requests and loss of incremental delivery. A study of selected merged PRs challenges the claim that agent-associated contributions usually arrive at merge in larger batches. Practitioner guidance explains how to make a proposed change inspectable one behavior at a time. The causal chain from agent use to broad drafts to reviewer overload remains open.

## What the merged PR comparison shows

Ogenrwot and Businge’s released notebook aggregates **24,014 Agentic-labeled PRs** and **5,080 Human-labeled PRs** after filtering for merge and joining commit details. The pooled rank comparisons favor higher Human observations for distinct commits (Cliff’s δ **0.5429**) and cumulative additions plus deletions (**0.3158**). Cumulative line changes can include an edit subsequently reverted within the same PR. These results run counter to a general claim that agent-associated work reaches merge in larger batches. The paper also reports a file-breadth difference, but the code counts distinct filenames for Agentic PRs and sums per-commit file counts for Human PRs. Its tool-specific plots pair data and labels in different orders, and reported valid-patch totals correspond to joined file-detail rows in the released code. The pooled commit and line rank comparisons are the usable evidence for direction. SRC-0024:C01, C04–C07. [Dossier](../sources/SRC-0024--sizes-of-agent-pull-requests.md) · [§2, steps 2–4](https://arxiv.org/pdf/2601.17581v3#page=2) · [§3, Table 1](https://arxiv.org/pdf/2601.17581v3#page=3) · [Replication notebook, cells 2–4, 8, 13–16](https://github.com/unlv-evol/AgenticPR-MSR-2026/blob/v1.0.0/notebooks/RQ1_patch_characteristics.ipynb) · [Independent verification](../audits/SRC-0024--verification.md)

The study inherits labels based on visible attribution. Some Human-labeled PRs could contain undisclosed assistance, and the groups may work on different kinds of tasks. Merge selection excludes unfinished and rejected drafts. Available commit and patch data add another selection step, with unknown impact. The study therefore leaves open whether agents produce oversized drafts, how often humans split them, and whether reviewers find a diff difficult. The paper, its preprint and tagged notebooks describe the same analysis. AIDev supplies the inputs, so other studies of its PRs may share observations. The practitioner guide and the developer-time study below use different evidence and supply no replication of the size comparison. SRC-0024:C01–C03, C08–C09. [§§2 and 6–7](https://arxiv.org/html/2601.17581v3) · [AIDev label development, §§3.1–3.2 and Table 2](https://arxiv.org/html/2507.15003v1#S3)

## Where a reviewable boundary comes from

Pocock describes finding one observable feature behavior, carrying it through the necessary layers, and naming dependencies that really must land first. A demo or test from the appropriate starting revision lets a human assess whether that boundary is useful. His account of extensive rework on a layer-split effort is one practitioner anecdote. It lacks a comparator and an accessible underlying postmortem. The tutorial and its skill definition document the same approach. The guidance favors keeping a small coherent change together. When a wide mechanical migration cannot stay green as behavioral slices, the guide proposes a compatible intermediate stage where feasible, or integration verification after batching when it cannot be. The source supplies no estimate of reviewer time, defect detection or whether splitting changes those outcomes. SRC-0006:C02–C08, C10. [Dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Vertical slices](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) · [Acceptance and when to skip decomposition](https://www.aihero.dev/skills-to-tickets#common-questions) · [Wide refactors](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception)

Becker and colleagues’ independently conducted developer-time study found that about **9%** of observed time in 44 analyzed AI-allowed recordings went to review and cleanup of generated output. This shows contributor work needed to inspect a draft. Human reviewer time falls outside the main outcome, which includes the contributor’s initial work and their later response to human review. The study randomized AI permission and left change boundaries to the normal workflow. Neither higher inspection cost per line nor lower effort after splitting follows from its results. SRC-0011:C02–C03, C07–C10. [Dossier](../sources/SRC-0011--review-work-and-developer-time.md) · [§2.3, outcome definition](https://arxiv.org/pdf/2507.09089v2#page=6) · [§3.2, Fig. 6](https://arxiv.org/pdf/2507.09089v2#page=10) · [Appendix C.1.4, recorded activity](https://arxiv.org/pdf/2507.09089v2#page=20)

## Apply the accepted method

[PAT-0003, Slice a change for review](../patterns/PAT-0003--slice-a-change-for-review.md) starts with one useful result a reviewer can check through a real command, screen or service operation. Name the starting revision and true prerequisites, then ask the agent to implement only the code path needed for that result. For a requested reporting feature, a first behavioral change might let the user filter the on-screen list before a separate export change. A base comparison and an adjacent existing-behavior check show what the slice adds and what it preserves. Inspect the diff and run the relevant checks before asking for the next outcome. If a reviewer needs two changes to exercise the same behavior, combine them or find a compatible boundary. The accepted method documents planned decomposition. Applying it to salvage an already bundled patch requires identifying a coherent base and staging work so each intermediate patch can be verified. No cited source compares that salvage procedure, estimates a universal size limit, or evaluates the effect of slicing on review accuracy. [Pattern verification](../audits/PAT-0003--verification.md) · [BP-05, Slice for review](BP-05--slice-for-review.md)

## Drive navigation

- [audits/PAT-0003--verification.md](../audits/PAT-0003--verification.md) · [Local copy](../audits/PAT-0003--verification.md)
- [audits/SRC-0006--verification.md](../audits/SRC-0006--verification.md) · [Local copy](../audits/SRC-0006--verification.md)
- [audits/SRC-0011--verification.md](../audits/SRC-0011--verification.md) · [Local copy](../audits/SRC-0011--verification.md)
- [audits/SRC-0024--verification.md](../audits/SRC-0024--verification.md) · [Local copy](../audits/SRC-0024--verification.md)
- [patterns/PAT-0003--slice-a-change-for-review.md](../patterns/PAT-0003--slice-a-change-for-review.md) · [Local copy](../patterns/PAT-0003--slice-a-change-for-review.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0006--vertical-slices-for-agent-tickets.md](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Local copy](../sources/SRC-0006--vertical-slices-for-agent-tickets.md)
- [sources/SRC-0011--review-work-and-developer-time.md](../sources/SRC-0011--review-work-and-developer-time.md) · [Local copy](../sources/SRC-0011--review-work-and-developer-time.md)
- [sources/SRC-0024--sizes-of-agent-pull-requests.md](../sources/SRC-0024--sizes-of-agent-pull-requests.md) · [Local copy](../sources/SRC-0024--sizes-of-agent-pull-requests.md)
