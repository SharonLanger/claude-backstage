# Manage the attention needed by delegated tasks

## Purpose

Recognize when easy task starts create more incoming decisions than you can review, and try a manageable work rhythm.

## When to use this guide

- Several agent results or questions arrive while you are still reviewing another.
- More tasks are started, but finished and verified work is accumulating slowly.

You need control over your own task starts and review periods. Team scheduling changes require agreement. No multi-agent framework or notification implementation is required.

## Quick tip

Identify what is waiting: execution, a decision, or review. If review is the bottleneck, try completing one review before starting another optional task and group nonurgent updates into planned review periods. Keep urgent or safety-critical decisions on their existing escalation path.

## Guide content

1. Make a brief list of active tasks and their next human action. Check whether a few large diffs or many competing tasks create the queue.
2. Choose a short focus period. Defer optional new starts while completing a review; agree when routine results will be checked. Do not defer a time-critical decision just to preserve the schedule.
3. Before accepting another task, identify who will review it and when. If one result is too large to inspect, use reviewable milestones rather than merely postponing it.
4. Reassess after the trial: did the pending-review queue shrink, were important decisions delayed, and did useful work finish? Adjust the rhythm rather than declaring a fixed concurrency limit.

**Original illustration:** Five assistant tasks are awaiting answers. Two are routine drafts, one needs a decision today, and two can wait. Deal with the time-critical decision, reserve a review period for the drafts, and defer optional starts until review capacity is available. This is a local adaptation, not a scheduling rule established by the study.

## Evidence and limits

The AP-04 research note describes an obstacle and attributed advice; it contains no approved work-in-progress method. This guide makes that advice usable without promoting it to a measured remedy. It does not establish an optimal number of agents, prove that parallel work caused the backlog, or replace team priorities. A small queue may be healthy overlap. Broader team isolation and arbitrary cross-project prioritization remain open.

## Related patterns

- [Reviewable milestones](../../B-task-decomposition/patterns/B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review) — reduce an individual review unit.
- [Review Pass](../../D-verification-evaluation/patterns/D05-review-pass.md) — inspect the actual changes.
- [Human-on-the-Loop Monitoring](../patterns/K06-human-on-the-loop-monitoring.md) — monitoring where the tool supports it.

## Sources

- Laura Counts, interviewing researcher Xingqi Maggie Ye — [AI promised to free up workers’ time. UC Berkeley Haas researchers found the opposite.](https://newsroom.haas.berkeley.edu/ai-promised-to-free-up-workers-time-uc-berkeley-haas-researchers-found-the-opposite/), February 18, 2026, methodology and final answer on an “AI practice”; consulted 2026-11-22. The account describes expanded work in one workplace. Ye recommends deliberate pauses, batching nonurgent updates, focus periods, and human dialogue. No intervention trial or concurrency cap is reported. Queue inspection, review-before-start, and the trial questions above are catalog adaptations.
