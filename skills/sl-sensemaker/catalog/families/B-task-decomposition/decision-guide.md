# Guide: How Should I Decompose This Task?

## Purpose

Use this decision guide when you have a complex task that a single LLM call cannot handle reliably, and you need to choose the right decomposition strategy: fixed, dynamic, or hierarchical.

## Decision Tree

```
Is the task structure known before execution begins?
│
├── YES: Are steps independent (can execute in parallel)?
│   │
│   ├── YES → Fixed Decomposition (B4) with parallel execution
│   │
│   └── NO: Is the step count small and stable (<10 steps)?
│       │
│       ├── YES → Fixed Decomposition (B4) with sequential execution
│       │
│       └── NO → Hierarchical Decomposition (B2) with fixed sub-plans
│
└── NO: Does earlier output determine later steps?
    │
    ├── YES: Is the task exploratory (unknown scope)?
    │   │
    │   ├── YES → Reconnaissance-First (B6) then Dynamic Decomposition (B3)
    │   │
    │   └── NO → Plan-Execute (B1) with replanning checkpoints
    │
    └── NO: Are there naturally recursive sub-problems?
        │
        ├── YES → Hierarchical Decomposition (B2) with dynamic sub-plans
        │
        └── NO → Dynamic Decomposition (B3) with milestone checkpoints (B5)
```

## Key Decision Factors

| Factor | Fixed (B4) | Dynamic (B3) | Hierarchical (B2) |
|--------|------------|--------------|-------------------|
| Task structure knowable upfront | Required | Not required | Partially required |
| Step count | Small, fixed | Unknown | Large, recursive |
| Parallelism potential | High (steps independent) | Low (steps depend on prior) | Medium (sub-trees parallel) |
| Cost (LLM calls) | Lowest | Medium | Highest |
| Latency | Lowest | Highest (serial) | Medium |
| Error recovery | Replace single step | Replan from checkpoint | Retry sub-tree |
| Best for | Code formatting, batch transforms | Research, debugging, exploration | Multi-file refactors, project planning |

## Choosing by Task Type

**Use Fixed Decomposition when:**
- Processing a batch of items with the same operation
- Following a known checklist or procedure
- The output structure matches an existing template

**Use Dynamic Decomposition when:**
- You don't know what you'll find until you start looking
- Each step's output determines what to do next
- The task involves investigation or search

**Use Hierarchical Decomposition when:**
- The task has natural recursive structure (e.g., a project breaks into modules, modules into files, files into functions)
- The task is too large for a single plan but too structured for purely reactive execution
- Sub-problems are semi-independent and can be delegated

**Use Reconnaissance-First, then decide:**
- You cannot even choose a decomposition strategy without understanding the problem space first
- The codebase, dataset, or domain is unfamiliar

## Common Mistakes

1. **Over-decomposing simple tasks.** If a single well-prompted agent can handle it in one pass, decomposition adds cost without benefit.
2. **Fixed decomposition on dynamic tasks.** If earlier outputs change the plan, a fixed plan will produce irrelevant steps.
3. **Skipping milestones in dynamic decomposition.** Without checkpoints, a dynamically decomposing agent can drift arbitrarily far before anyone notices.
4. **Hierarchical decomposition without clear delegation boundaries.** If sub-tasks share too much context, you lose the isolation benefit and gain coordination overhead.

## Related Patterns

- [B1: Plan-Execute](patterns/B1-plan-execute.md) — the foundational two-phase pattern
- [B2: Hierarchical Decomposition](patterns/B2-hierarchical-decomposition.md) — recursive sub-problem delegation
- [B3: Dynamic Decomposition](patterns/B3-dynamic-decomposition.md) — plan emerges during execution
- [B4: Fixed Decomposition](patterns/B4-fixed-decomposition.md) — pre-determined step list
- [B5: Milestone Checkpoint](patterns/B5-milestone-checkpoint.md) — progress gates within decomposition
- [B6: Reconnaissance-First](patterns/B6-reconnaissance-first.md) — understand before planning

## Sources

- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- Stanford — [CS224G: Agentic Design Patterns](https://web.stanford.edu/class/cs224g/2025/lectures/Agentic_Design_Patterns.pdf)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
