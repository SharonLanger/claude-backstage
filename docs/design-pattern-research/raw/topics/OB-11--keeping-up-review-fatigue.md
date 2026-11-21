---
topic_id: OB-11
title: "Keeping up / review fatigue"
coverage: partially supported
source_edges:
  - id: SRC-0011
    relationship: DIRECT
    strength: high
    finding: "Early-2025 AI access increased estimated author implementation time in one randomized trial, with generated-output review and cleanup directly observed in a recording subset."
  - id: SRC-0015
    relationship: SUPPORTING
    strength: low
    finding: "A separate workplace ethnography describes pressure and concurrent AI activity while leaving code review fatigue unmeasured."
  - id: SRC-0018
    relationship: SUPPORTING
    strength: low
    finding: "Moby maintainers report checking burdens from unverified submissions and set contributor review and ownership requirements."
  - id: SRC-0007
    relationship: SUPPORTING
    strength: low
    finding: "An independent developer collaboration study documents a shift in some routine help seeking without measuring peer review demand."
  - id: SRC-0006
    relationship: SUPPORTING
    strength: low
    finding: "Pocock gives practitioners a way to scope work into observable behaviors without evaluating review effort or fatigue."
pattern_ids: [PAT-0003, PAT-0008]
publication_status: published
---

# OB-11 — Keeping up / review fatigue

“The patch was ready in minutes. Checking it took the afternoon.” “I don't know whether the team is shipping faster or just reviewing more drafts.” The brief connects quick generation, the gap between perceived and measured productivity, and a human verification bottleneck. The evidence documents verification work and a perception gap in one trial. Review fatigue, how output rate affects review accuracy and whether a queue outgrows team capacity are separate unresolved questions.

## What the trial measured

Becker et al. randomized permission to use early-2025 AI tools by issue. Sixteen experienced developers completed 246 real issues in familiar, mature repositories using their usual contribution process. In this setting, allowing AI increased forecast-adjusted implementation time by **19%** (reported 95% interval **+2% to +39%**). The retrospective developer estimate implied **20% shorter** time. Implementation time includes the author's initial work and later response to human review. Human reviewers' active time and calendar waiting for them fall outside the measure. SRC-0011:C01–C05, §§2.2–2.3, Fig. 1 and §3.1. [Dossier](../sources/SRC-0011--review-work-and-developer-time.md) · [Versioned paper](https://arxiv.org/html/2507.09089v2)

Of the 74 recordings used for activity analysis, the 44 valid AI-allowed recordings examined in Appendix C show about **9%** of time in AI-output review and cleanup and about **4%** waiting for AI. Testing and debugging had separate labels. Rejected and retained outputs both consumed time. The assignment was randomized, and time spent reviewing was a subsequent developer behavior. Those activity shares cannot decompose the full-sample slowdown or establish how much faster the assistant produced work than the author could verify it. Post-human-review work averaged 15 versus 9 minutes with and without AI allowed, a statistically insignificant difference in contributor rework. Effort reports were mixed. Neither result estimates the time other people spent reviewing or changes in reviewer alertness. SRC-0011:C07–C11, §3.2 Fig. 6, Appendix C.1.4, C.2.6–C.2.7 and tracking instructions in Appendix G. [Activity chart](https://arxiv.org/pdf/2507.09089v2#page=10) · [Detailed recording evidence](https://arxiv.org/pdf/2507.09089v2#page=20) · [Effort and post-review work](https://arxiv.org/pdf/2507.09089v2#page=23)

## Evidence beyond the early trial

- **Same trial and related follow-up.** METR's July companion post summarizes the early trial. The February 2026 post reports new late-2025 data from a related experiment with partial participant overlap. Its implementation-time point estimates were −18% for returning developers (interval −38% to +9%) and −4% for new recruits (−15% to +9%). Both intervals include zero. Participation, task withholding and completion, and difficulty apportioning time when agents ran concurrently limit comparison. The later estimates leave the review mechanism unresolved while limiting any application of the earlier slowdown to current tools. SRC-0011:C12–C13, follow-up opening estimates and methods. [Companion post](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) · [Follow-up](https://metr.org/blog/2026-02-24-uplift-update/)
- **Different workflows and outcomes.** In a workplace ethnography, Ye describes overlapping agent runs, work encroaching on breaks and reports of greater overall pressure alongside a sense of momentum in individual interactions. The interview gives no causal or quantitative estimate of review effort. Salomon et al.'s independent developer study found that some routine questions moved to AI, while high-context requests still reached peers and reports of fewer colleague interruptions were mixed. That result qualifies an assumption that displaced conversations automatically free reviewer capacity. The data are self-reports on collaboration and help seeking. SRC-0015:C04–C07, Q3–Q5. SRC-0007:C03–C04, C07–C11, §§4.1–4.4 and §§6.3–6.4.3. [Ethnography dossier](../sources/SRC-0015--work-intensification-and-task-expansion.md) · [Haas interview](https://newsroom.haas.berkeley.edu/ai-promised-to-free-up-workers-time-uc-berkeley-haas-researchers-found-the-opposite/) · [Collaboration dossier](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Author manuscript](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf)
- **Review work transferred to maintainers.** Moby's policy independently reports that unchecked submissions leave maintainers to do validation contributors could have done. It requires the human submitter to review, verify and own their work. This is a concrete maintainer perspective and policy. It supplies no workload counts or before-and-after evaluation. SRC-0018:C01–C03, C07, policy lines 3–44 and 92–115. [Dossier](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Policy rationale](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L92-L115)

## Where the patterns apply

[Slice a change for review](../patterns/PAT-0003--slice-a-change-for-review.md) gives a reviewer a narrower behavioral question and an observable check. It adapts Pocock's independent advice on implementation boundaries. [Take ownership before submitting AI-assisted code](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) fits when a contributor has a candidate diff and needs to make its claims and checks inspectable for the next reviewer. Their effects on throughput and fatigue remain untested. SRC-0006:C02, C05 and C10, “Tracer bullets, not layers,” “Common questions” and downstream workflow. SRC-0018:C02–C04, policy lines 18–53. [Slicing dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Workflow](https://www.aihero.dev/skills-to-tickets#where-it-fits) · [Contribution policy](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L18-L53)

For the workload question itself, a local comparison could distinguish time to first candidate, author time through verification and feedback, active human review and pending changes. This is a catalog adaptation of the trial's distinctions. A fatigue claim would additionally require evidence such as changing effort or review accuracy over a session.

## Drive navigation

- [audits/PAT-0003--verification.md](../audits/PAT-0003--verification.md) · [Local copy](../audits/PAT-0003--verification.md)
- [audits/PAT-0008--verification.md](../audits/PAT-0008--verification.md) · [Local copy](../audits/PAT-0008--verification.md)
- [audits/SRC-0006--verification.md](../audits/SRC-0006--verification.md) · [Local copy](../audits/SRC-0006--verification.md)
- [audits/SRC-0007--verification.md](../audits/SRC-0007--verification.md) · [Local copy](../audits/SRC-0007--verification.md)
- [audits/SRC-0011--verification.md](../audits/SRC-0011--verification.md) · [Local copy](../audits/SRC-0011--verification.md)
- [audits/SRC-0015--verification.md](../audits/SRC-0015--verification.md) · [Local copy](../audits/SRC-0015--verification.md)
- [audits/SRC-0018--verification.md](../audits/SRC-0018--verification.md) · [Local copy](../audits/SRC-0018--verification.md)
- [patterns/PAT-0003--slice-a-change-for-review.md](../patterns/PAT-0003--slice-a-change-for-review.md) · [Local copy](../patterns/PAT-0003--slice-a-change-for-review.md)
- [patterns/PAT-0008--take-ownership-before-submitting-ai-code.md](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) · [Local copy](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0006--vertical-slices-for-agent-tickets.md](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Local copy](../sources/SRC-0006--vertical-slices-for-agent-tickets.md)
- [sources/SRC-0007--developer-collaboration-and-ai.md](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Local copy](../sources/SRC-0007--developer-collaboration-and-ai.md)
- [sources/SRC-0011--review-work-and-developer-time.md](../sources/SRC-0011--review-work-and-developer-time.md) · [Local copy](../sources/SRC-0011--review-work-and-developer-time.md)
- [sources/SRC-0015--work-intensification-and-task-expansion.md](../sources/SRC-0015--work-intensification-and-task-expansion.md) · [Local copy](../sources/SRC-0015--work-intensification-and-task-expansion.md)
- [sources/SRC-0018--accountability-for-ai-assisted-contributions.md](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Local copy](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md)
