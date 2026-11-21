# Designing Multi-Agent Systems

## Scenario

You have a working single-agent system (or are considering building one) and are evaluating whether multiple agents would solve your problem better. You need to decide: should I use multiple agents, how should they be organized, and how should they communicate?

## Quick Answer

1. **Default to single-agent** — multi-agent adds communication overhead, failure modes, and debugging complexity. Only split when you have a concrete reason. See the decision criteria below.
2. **If you split, choose an orchestration pattern** — the relationship between agents (hierarchy, peer, handoff) determines everything about communication and failure handling. See [C-orchestration](../../families/C-orchestration/).
3. **Isolate context per agent** — the primary benefit of multi-agent is that each agent has a focused context window. If agents share everything, you have a single agent with extra steps. See [context-isolation.md](../../families/E-context-engineering/patterns/context-isolation.md).

## Decision Guide: Do You Need Multiple Agents?

Answer these questions honestly. You need multiple agents only if at least one "Yes" applies:

| Question | If yes → multi-agent reason |
|----------|----------------------------|
| Does the task require distinct expertise that would conflict in a single prompt? | Specialization |
| Is the context window too small for all relevant information? | Context isolation |
| Do sub-tasks have different security requirements? | Trust boundaries |
| Do sub-tasks need to run in parallel for performance? | Parallelism |
| Does the task require adversarial checking (one agent verifies another)? | Verification |

**If none apply, stay with a single agent.** A longer system prompt or better tool design usually solves the problem more simply.

## Orchestration Patterns

Once you decide on multi-agent, choose how agents relate to each other:

### Hierarchical (one controls many)

| Pattern | When to use | Link |
|---------|------------|------|
| Orchestrator-Workers | Central coordinator delegates tasks, workers report back | [orchestrator-workers.md](../../families/C-orchestration/patterns/orchestrator-workers.md) |
| Manager-Workers | Like orchestrator, but manager also decides task decomposition | [manager-workers.md](../../families/C-orchestration/patterns/manager-workers.md) |
| Hierarchical Coordinator | Multiple levels of coordination | [hierarchical-coordinator.md](../../families/C-orchestration/patterns/hierarchical-coordinator.md) |
| Agent-as-Tool | Sub-agent exposed as a tool to the parent | [agent-as-tool.md](../../families/C-orchestration/patterns/agent-as-tool.md) |

### Peer-based (agents collaborate)

| Pattern | When to use | Link |
|---------|------------|------|
| Coordinator-Specialists | Peers with different expertise, light coordination | [coordinator-specialists.md](../../families/C-orchestration/patterns/coordinator-specialists.md) |
| Decentralized Handoff | Agents pass control to each other | [decentralized-handoff.md](../../families/C-orchestration/patterns/decentralized-handoff.md) |

### Verification-oriented (one checks another)

| Pattern | When to use | Link |
|---------|------------|------|
| Maker-Checker | One agent produces, another validates | [maker-checker.md](../../families/C-orchestration/patterns/maker-checker.md) |
| Specialist-Reviewer | Domain expert reviews another's work | [specialist-reviewer.md](../../families/C-orchestration/patterns/specialist-reviewer.md) |
| Generator-Critic | Iterative improvement through critique | [generator-critic.md](../../families/A-workflow-topology/patterns/generator-critic.md) |

### Aggregation (combining outputs)

| Pattern | When to use | Link |
|---------|------------|------|
| Synthesizer-Aggregator | Multiple agents produce partial results, one combines | [synthesizer-aggregator.md](../../families/C-orchestration/patterns/synthesizer-aggregator.md) |
| Parallel Voting | Multiple agents independently solve, majority wins | [parallel-voting.md](../../families/A-workflow-topology/patterns/parallel-voting.md) |

## Communication Design

How agents share information is as important as how they are organized:

| Approach | Best for | Pattern |
|----------|----------|---------|
| Structured handoff (artifact) | Clear boundaries, async work | [artifact-based-handoff.md](../../families/E-context-engineering/patterns/artifact-based-handoff.md) |
| Minimal context handoff | Reducing token waste | [minimal-context-handoff.md](../../families/E-context-engineering/patterns/minimal-context-handoff.md) |
| Shared state store | Agents need common ground truth | [shared-memory-gateway.md](../../families/L-memory-state/patterns/shared-memory-gateway.md) |
| Scoped memory | Agents have private + shared views | [scoped-memory.md](../../families/L-memory-state/patterns/scoped-memory.md) |

## Checklist Before Going Multi-Agent

- [ ] Single-agent approach tested and found insufficient (document why)
- [ ] Clear reason for splitting (specialization, context, security, parallelism, or verification)
- [ ] Each agent has a well-defined role with minimal overlap
- [ ] Communication protocol defined (what is passed, in what format)
- [ ] Failure handling designed (what happens when one agent fails?)
- [ ] Context isolation strategy in place (each agent sees only what it needs)
- [ ] Orchestration pattern chosen and documented
- [ ] Human escalation path defined for multi-agent disagreements

## Common Multi-Agent Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Chatty agents | High token cost, slow execution | Reduce handoff data, use artifacts |
| Unclear ownership | Tasks fall through cracks or are duplicated | Explicit role definitions |
| Circular delegation | Agents delegate back and forth | Hierarchical structure, bounded handoffs |
| Shared context bloat | All agents see everything | Isolate contexts, use scoped memory |
| Cascade failures | One agent failure kills the system | Circuit breakers, fallback paths |

## Anti-Patterns to Watch For

- [Multi-Agent by Default](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md) — the most common mistake. Multi-agent is a solution to specific problems, not a default architecture.
- [Infinite/Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md) — agents delegating indefinitely without termination criteria
- [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) — splitting work across agents reduces quality but you do not measure it

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- https://web.stanford.edu/class/cs224g/2025/lectures/Agentic_Design_Patterns.pdf
