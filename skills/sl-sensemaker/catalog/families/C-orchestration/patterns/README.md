# patterns/

Pattern files for Family C: Orchestration & Role Separation.

Each file documents one design pattern using a consistent schema: Problem, Solution Structure, When to Use, When Not to Use, Trade-offs, Implementation Sketch, Related Patterns, Anti-Patterns Addressed, Sources.

## Files

```
patterns/
├── README.md                      ← this file
├── agent-as-tool.md               ← wrapping an agent as a callable tool for a parent orchestrator
├── coordinator-specialists.md     ← a coordinator routes tasks to domain-specialist agents
├── decentralized-handoff.md       ← agents pass control peer-to-peer without a central orchestrator
├── hierarchical-coordinator.md    ← nested coordinators forming a tree of orchestration layers
├── maker-checker.md               ← one agent produces output; a second independently verifies it
├── manager-workers.md             ← a manager agent breaks work into tasks and assigns them to workers
├── orchestrator-workers.md        ← a stateful orchestrator drives a fixed pipeline of worker agents
├── specialist-reviewer.md         ← a domain specialist reviews output produced by a generalist agent
└── synthesizer-aggregator.md      ← an aggregator collects outputs from parallel agents and synthesizes them
```

## Schema

Each engineering pattern follows the same nine-section structure:

| Section | Purpose |
|---|---|
| Problem | The specific coordination or role failure the pattern addresses |
| Solution Structure | The roles involved and how they interact |
| When to Use | Conditions that make this pattern a good fit |
| When Not to Use | Signals that a simpler approach is better |
| Trade-offs | Costs and benefits to weigh |
| Implementation Sketch | Concrete pseudocode or structural outline |
| Related Patterns | Cross-references to other patterns in this family or others |
| Anti-Patterns Addressed | Which anti-patterns this pattern prevents |
| Sources | References and prior art |

## When to use this folder

Come here when you need to:

- Choose which orchestration pattern fits a specific coordination problem
- Understand the structural difference between similar-sounding roles (manager vs. orchestrator vs. coordinator — see `../comparisons/`)
- Find the implementation sketch for a pattern you already know by name
- Check which anti-patterns a pattern defends against

If you are unsure whether multi-agent orchestration is warranted at all, read `../guides/do-you-need-multi-agent.md` first.

Last updated: 2026-08-24
