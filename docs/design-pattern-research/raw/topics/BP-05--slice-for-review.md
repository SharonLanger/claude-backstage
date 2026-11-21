---
topic_id: BP-05
title: Slice for review
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0006
    relationship: DIRECT
    strength: moderate
    finding: "Pocock describes slicing planned feature work into individually demonstrable behaviors that cross the necessary layers."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic recommends a runnable check and review of a diff against the specification and edge-case tests."
  - id: SRC-0011
    relationship: SUPPORTING
    strength: moderate
    finding: "Recorded work on open-source issues shows contributors spent measurable time inspecting and cleaning AI output."
  - id: SRC-0018
    relationship: SUPPORTING
    strength: low
    finding: "The shared Moby policy asks for focused diffs and excludes trivial fragmentation without a concrete benefit."
  - id: SRC-0024
    relationship: SUPPORTING
    strength: low
    finding: "A study of selected merged pull requests proposes examining commits and affected files alongside line counts during triage."
pattern_ids: [PAT-0003]
---

# BP-05 Slice for review

## When it comes up

- “The first three pull requests only add infrastructure. I can’t try any part of the feature yet.”
- “The assistant touched several features, and I can’t tell what belongs to the change I asked for.”
- “We have smaller diffs now, but reviewers still need all of them open to verify one behavior.”

The brief asks whether a large AI-produced change can be made reviewable by splitting it into vertical pieces. There is specific guidance for designing demonstrable feature slices before generation and checking their diffs afterward. Comparative outcomes for splitting an already-generated patch, reviewer workload, and defect detection remain open.

## How the evidence fits

Pocock’s ticketing guide proposes one demonstrable or testable behavior per ticket. The ticket can cross UI, service, and storage boundaries, with dependencies explicitly recorded. A test or demo starting from the appropriate revision makes the proposed split observable. The guide also describes when this structure is a poor fit. A widespread mechanical change can be staged with a compatible intermediate form, or verified as a whole if intermediate batches cannot stay green. The tutorial and companion skill definition document the same workflow. The article’s layer-ticket rework account is an anecdote whose comparator and underlying postmortem were unavailable. The guide shows how to choose a boundary and supplies no measurements of review outcomes. `SRC-0006:C02`, `SRC-0006:C05`, `SRC-0006:C06`, `SRC-0006:C07`, `SRC-0006:C08`, `SRC-0006:C10`. [Dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Tracer bullets, not layers](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) · [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions) · [The wide-refactor exception](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception)

Anthropic’s independently authored guide supplies verification advice at the other end of the handoff. Give the agent an interpretable check, ask for execution evidence, then compare the resulting diff to the specification and edge-case tests. It gives no criterion for choosing a vertical slice. The Moby maintainers’ separate policy asks contributors to keep proposed changes focused on the intended behavior and warns against trivial fragmentation. Together these sources support a review question with a useful outcome and a clear check. The combination is a catalog application. Neither publication measures how the size or shape of a change affects review. `SRC-0002:C07`, `SRC-0002:C08`, `SRC-0002:C10`, `SRC-0018:C03`, `SRC-0018:C05`. [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Checks](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Spec review](https://code.claude.com/docs/en/best-practices#review-against-your-spec) · [Moby dossier](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Shared policy](https://github.com/moby/.github/blob/main/AI_POLICY.md) · [Reviewed revision, lines 24–78](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L24-L78)

Becker et al.’s independent study shows why inspection belongs in the workflow. In 44 analyzed recordings where AI use was permitted, approximately 9% of recorded time went to reviewing and cleaning up AI output. This records the contributor’s work in a subset. Other reviewers’ time and the contribution of review to the overall task-time effect remain open. The trial randomized AI permission, and contributors chose their own workflows. Its later follow-up includes some returning participants and studies productivity under a different recruitment and tool setting. It supplies no independent slicing test. `SRC-0011:C02`, `SRC-0011:C03`, `SRC-0011:C07`, `SRC-0011:C08`, `SRC-0011:C10`, `SRC-0011:C11`, `SRC-0011:C12`, `SRC-0011:C13`. [Dossier](../sources/SRC-0011--review-work-and-developer-time.md) · [Becker article](https://arxiv.org/html/2507.09089v2) · [§3.2, Fig. 6, pp. 9–10](https://arxiv.org/pdf/2507.09089v2#page=10) · [§C.1.4, p. 20](https://arxiv.org/pdf/2507.09089v2#page=20) · [METR follow-up](https://metr.org/blog/2026-02-24-uplift-update/)

Ogenrwot and Businge propose using commit counts and affected files alongside line counts to triage PRs. In their selected merged AIDev sample, Human-labeled PRs ranked higher on cumulative additions plus deletions. Cumulative churn can differ from the final diff, and the file comparison counts unique paths for Agentic-labeled PRs and sums per-commit file counts for Human-labeled PRs. This independent analysis uses different data from Becker et al.’s work recordings. It supplies a reason to inspect the specific change before choosing a boundary. Pocock supplies the guidance for choosing that boundary, and the AIDev analysis leaves slicing outcomes and review effort unmeasured. `SRC-0024:C01`, `SRC-0024:C03`, `SRC-0024:C04`, `SRC-0024:C05`, `SRC-0024:C09`. [Dossier](../sources/SRC-0024--sizes-of-agent-pull-requests.md) · [Versioned article](https://arxiv.org/html/2601.17581v3) · [RQ1 and Table 1, PDF p. 3](https://arxiv.org/pdf/2601.17581v3#page=3) · [RQ1 notebook, cells 4, 7–8 and 13](https://github.com/unlv-evol/AgenticPR-MSR-2026/blob/v1.0.0/notebooks/RQ1_patch_characteristics.ipynb) · [Conclusion, §7, PDF p. 4](https://arxiv.org/pdf/2601.17581v3#page=4)

## Use in coding work

[PAT-0003, Slice a change for review](../patterns/PAT-0003--slice-a-change-for-review.md) links one behavior to a starting revision, a real entry point, and a check that a reviewer can run. It asks the reviewer to inspect that bounded diff before a later request widens it. That per-slice review step incorporates Anthropic’s review guidance into Pocock’s ticket structure. A small change may already have a clear review question, and a coupled migration may require a compatible stage or an integration review. Faster reviews, lower fatigue, and improved defect detection remain hypotheses for these procedures. [Pattern verification](../audits/PAT-0003--verification.md)

## Drive navigation

- [audits/PAT-0003--verification.md](../audits/PAT-0003--verification.md) · [Local copy](../audits/PAT-0003--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0006--verification.md](../audits/SRC-0006--verification.md) · [Local copy](../audits/SRC-0006--verification.md)
- [audits/SRC-0011--verification.md](../audits/SRC-0011--verification.md) · [Local copy](../audits/SRC-0011--verification.md)
- [audits/SRC-0018--verification.md](../audits/SRC-0018--verification.md) · [Local copy](../audits/SRC-0018--verification.md)
- [audits/SRC-0024--verification.md](../audits/SRC-0024--verification.md) · [Local copy](../audits/SRC-0024--verification.md)
- [patterns/PAT-0003--slice-a-change-for-review.md](../patterns/PAT-0003--slice-a-change-for-review.md) · [Local copy](../patterns/PAT-0003--slice-a-change-for-review.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0006--vertical-slices-for-agent-tickets.md](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Local copy](../sources/SRC-0006--vertical-slices-for-agent-tickets.md)
- [sources/SRC-0011--review-work-and-developer-time.md](../sources/SRC-0011--review-work-and-developer-time.md) · [Local copy](../sources/SRC-0011--review-work-and-developer-time.md)
- [sources/SRC-0018--accountability-for-ai-assisted-contributions.md](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Local copy](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md)
- [sources/SRC-0024--sizes-of-agent-pull-requests.md](../sources/SRC-0024--sizes-of-agent-pull-requests.md) · [Local copy](../sources/SRC-0024--sizes-of-agent-pull-requests.md)
