# Family B: Task Decomposition & Planning

**Recurring problem:** Large or ambiguous tasks overload a single reasoning step — the model loses track of constraints, misses subtasks, or produces shallow output when asked to do too much at once.

**Core insight:** Decompose before executing. Break the problem into scoped, sequenced subtasks with clear boundaries, then hand those subtasks to an execution layer (Family C).

---

## Practitioner entry points

- [Slice a change for review](patterns/B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review) — the AI change is too large to review.

## Directory Tree

```
B-task-decomposition/
├── README.md                          ← this file — navigation and decision guides
├── decision-guide.md                  ← when to use fixed vs dynamic; when to recon first
├── patterns/
│   ├── B1-plan-execute.md             ← produce a plan, then execute against it
│   ├── B2-hierarchical-decomposition.md ← recursive breakdown: epics → tasks → subtasks
│   ├── B3-dynamic-decomposition.md    ← decompose at runtime, adapt as results arrive
│   ├── B4-fixed-decomposition.md      ← decompose once upfront; locked before execution
│   ├── B5-milestone-checkpoint.md     ← decompose into milestones with explicit validation gates
│   └── B6-reconnaissance-first.md     ← gather information before committing to a plan
```

---

## Per-Pattern File Schema

Every file in `patterns/` follows this structure:

```
# <ID>: <Pattern Name>

## Intent
One-sentence statement of what the pattern does.

## Problem
What goes wrong without this pattern.

## Solution
How the pattern addresses the problem. Core mechanism in 3–5 sentences.

## Structure
Diagram or numbered steps showing the flow.

## When to Use
Bulleted list of conditions that make this pattern a good fit.

## When NOT to Use
Conditions where this pattern adds overhead without benefit.

## Implementation Notes
Key decisions, pitfalls, and design details.

## Related Patterns
Cross-references to other families (with family code: A, C, K, I, etc.).

## Example
Concrete scenario (one paragraph) showing the pattern in action.
```

---

## Quick-Reference Table

| Pattern | ID | Use when… |
|---|---|---|
| Plan → Execute | B1 | Task is complex enough to need a plan but stable enough that the plan won't change mid-flight |
| Hierarchical Decomposition | B2 | Task has natural levels of granularity (project → feature → step); depth helps parallelism |
| Dynamic Decomposition | B3 | Subtasks depend on earlier results; full plan cannot be known upfront |
| Fixed Decomposition | B4 | Task is well-understood; determinism and auditability matter more than flexibility |
| Milestone / Checkpoint Planning | B5 | Long tasks where partial failure is likely; you need recovery points or human gates |
| Reconnaissance-First | B6 | Domain is unfamiliar, inputs are ambiguous, or a wrong decomposition would be costly to redo |

---

## Fixed vs Dynamic Decomposition

| Dimension | Fixed (B4) | Dynamic (B3) |
|---|---|---|
| **When plan is built** | Before any execution begins | Incrementally, as results arrive |
| **Plan mutability** | Locked — no changes after decomposition | Adapts based on intermediate outputs |
| **Best for** | Well-defined tasks, known inputs, repeatable workflows | Exploratory tasks, unknown scope, tasks where step N informs step N+1 |
| **Cost model** | One planning LLM call; predictable token use | Multiple planning calls; higher total cost |
| **Auditability** | High — full plan visible before execution | Lower — plan emerges during execution |
| **Failure behavior** | Failure is often caught at planning time | Failure may require re-planning mid-execution |
| **Parallelism** | Easier — all subtasks known upfront | Harder — dependencies only known at runtime |
| **Risk** | Plan may be wrong if domain was misread | Plan may never converge if termination condition is weak |

**Heuristic:** Default to Fixed (B4) when you can. Use Dynamic (B3) only when the task structure genuinely cannot be determined without executing earlier steps.

---

## When to Do Reconnaissance First (B6)

Add a reconnaissance phase before decomposition when **any** of these are true:

- The task involves an unfamiliar codebase, dataset, or domain
- The prompt is ambiguous and a wrong decomposition would waste significant compute
- The task involves locating something (files, APIs, patterns) whose existence is uncertain
- A previous decomposition attempt failed due to incorrect assumptions about scope or structure

Reconnaissance is a cheap information-gathering pass — read, search, sample — that de-risks the planning step. See `patterns/B6-reconnaissance-first.md` for implementation detail.

---

## Related Families

| Family | Relationship |
|---|---|
| **A — Topology** | Shapes how decomposed subtasks are wired together (chain, fan-out, DAG) |
| **C — Orchestration** | Assigns subtasks to workers; consumes the output of B |
| **K — Human Control** | Checkpoints (B5) align with human gates in K |
| **I — Reliability** | Checkpoints (B5) double as recovery points for retry and resume patterns |

---

Last updated: 2026-08-24

