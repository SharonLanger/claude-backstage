# Manager vs. Orchestrator vs. Coordinator

## Purpose

These three patterns share surface structure — a central agent dispatches to other agents — but they differ in three critical dimensions: **authority** (who owns the goal), **state** (who holds intermediate results), and **domain knowledge** (who understands what the workers are doing). Choosing the wrong one creates either an over-burdened central agent or one that cannot make the decisions its role requires.

---

## The Three Patterns at a Glance

| Dimension | Manager | Orchestrator | Coordinator |
|-----------|---------|-------------|-------------|
| Goal ownership | Manager owns the goal end-to-end | Caller owns the goal; orchestrator does not | Caller owns the goal; coordinator does not |
| State | Manager accumulates and holds state | Stateless; passes state to caller | Stateless; passes state to caller |
| Domain knowledge | Manager needs enough domain knowledge to decompose and integrate | None required — routing is mechanical | None required — workers are the domain experts |
| Adaptation | Manager adapts the plan based on intermediate results | No adaptation — routing rules are fixed upfront | No adaptation — routing rules are fixed upfront |
| Replanning | Manager can replan mid-execution | Cannot replan | Cannot replan |
| Authority | Full authority; can abort, retry, escalate | Routing authority only | Routing authority only |
| Worker type | Any workers; manager decides | Typed workers matched to task types | Domain specialists |

---

## Decision Guide

**Use Manager when:**
- Someone must own the goal end-to-end and be accountable for the final result.
- The plan cannot be fully determined upfront — intermediate results must influence next steps.
- You need adaptive retry, rerouting, or early termination based on worker outputs.
- Workers are not domain specialists — the manager decides what to do with their outputs.

**Use Orchestrator when:**
- The routing logic is well-defined and mechanical (match task type to worker type).
- Goal state and planning belong with the caller; the orchestrator is just a dispatcher.
- You want the coordinator to be stateless, testable in isolation, and replaceable.
- Fan-out across many typed workers is the primary concern.

**Use Coordinator when:**
- Workers are domain experts and the coordinator has no domain knowledge.
- The caller provides a cross-domain request that must be routed to the right specialist.
- You want to add or replace specialists without changing the coordinator.
- Domain quality is the primary concern, not routing efficiency.

---

## Authority vs. Routing vs. Domain

```
Manager          Orchestrator         Coordinator
   │                  │                    │
   ▼                  ▼                    ▼
Owns goal         Routes tasks         Routes tasks
Holds state       Stateless            Stateless
Adapts plan       No adaptation        No adaptation
Domain-aware      Domain-agnostic      Domain-agnostic
  (enough to        (routing by          (routing by
   integrate)        task type)           domain)
```

The orchestrator and coordinator look identical in structure but differ in what their routing decisions are based on: task type (orchestrator) vs. domain expertise (coordinator). The manager is the only one of the three that can change its plan mid-execution.

---

## Common Mistakes

**Mistake 1: Using a manager when an orchestrator suffices.**
If the routing rules are fully known upfront and no replanning is needed, a stateless orchestrator is simpler and cheaper. The manager's adaptability is unused complexity.

**Mistake 2: Using an orchestrator when a manager is needed.**
If intermediate results must influence which workers run next, an orchestrator cannot do this — it has no goal state. The caller would need to implement replanning logic, effectively becoming the manager.

**Mistake 3: Giving the coordinator domain knowledge.**
If the coordinator's prompt includes domain instructions so it can "help out" when no specialist is available, it is no longer a coordinator — it is a degraded manager. Keep coordinators domain-agnostic; add a fallback specialist instead.

**Mistake 4: Conflating orchestrator and coordinator.**
Both are stateless routers, but the distinction matters for system design: orchestrators route by task type (easily enumerable, mechanical), coordinators route by domain (requires a domain classification step that itself may be non-trivial).

---

## Transitions

These patterns are not exclusive. A common real-world structure is:

```
Manager (owns the goal)
  └── Orchestrator (routes typed subtasks in parallel)
        ├── Worker A (typed worker)
        └── Coordinator (for domain-expert subtasks)
              ├── Legal Specialist
              └── Finance Specialist
```

The manager adapts the plan; the orchestrator routes efficiently; the coordinator ensures domain quality. Each does exactly what it is equipped for.

---

## Sources

- **Anthropic Engineering** — AI safety company; authors of Claude. [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Google Cloud Architecture Center** — Google's cloud architecture team. [Choose a Design Pattern for Agentic AI](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- **AWS Prescriptive Guidance** — Amazon Web Services architecture team. [Agentic AI Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- **Microsoft Azure Architecture Center** — Microsoft's cloud architecture team. [AI Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
