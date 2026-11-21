# Designing Memory and State

## Scenario

You are building an agent system that needs to remember things: across steps within a task, across tasks within a session, or across sessions over time. You need to decide what to store, where to store it, who can access it, and how to manage its lifecycle.

## Quick Answer

1. **Distinguish the three timescales** — within-task (working memory), within-session (conversation state), and across-sessions (long-term memory). Each has different patterns and tradeoffs. See [L-memory-state](../../families/L-memory-state/).
2. **State should live outside the model** — the model is stateless between calls. All memory must be explicitly managed by the harness or external systems. See [external-durable-state.md](../../families/L-memory-state/patterns/external-durable-state.md).
3. **Scope access tightly** — not every agent or step needs to see all state. Shared mutable state is as dangerous in agent systems as it is in concurrent programming. See [scoped-memory.md](../../families/L-memory-state/patterns/scoped-memory.md).

## Decision Guide: What Kind of State Do You Need?

### Step 1: Classify by timescale

| Timescale | Survives... | Example | Primary patterns |
|-----------|-------------|---------|-----------------|
| Within-task | One agent loop iteration to the next | Tool results, intermediate reasoning | Context window, artifacts |
| Within-session | Multiple tasks in one conversation | User preferences, accumulated context | [session-isolation.md](../../families/L-memory-state/patterns/session-isolation.md) |
| Across-sessions | System restarts, days/weeks | User history, learned preferences | [external-durable-state.md](../../families/L-memory-state/patterns/external-durable-state.md) |

### Step 2: Classify by access pattern

| Access pattern | Description | Pattern |
|---------------|-------------|---------|
| Private to one agent | Only the owning agent reads/writes | [scoped-memory.md](../../families/L-memory-state/patterns/scoped-memory.md) |
| Shared read-only | Multiple agents read, one source of truth writes | [shared-memory-gateway.md](../../families/L-memory-state/patterns/shared-memory-gateway.md) |
| Shared mutable | Multiple agents read and write | Dangerous — use gateway pattern with locking |
| Append-only log | Events accumulate, nothing is deleted | [provenance-tagged-memory.md](../../families/L-memory-state/patterns/provenance-tagged-memory.md) |

### Step 3: Choose a storage mechanism

| Mechanism | Best for | Tradeoff |
|-----------|----------|----------|
| Context window | Current step's working data | Limited size, lost between calls |
| Scratchpad/artifact | Intermediate work products | Persists within session, must be explicitly loaded |
| File system | Structured data, code, documents | Durable, but requires tool to access |
| Database | Queryable state, relationships | Most flexible, most complex |
| Key-value store | Simple lookups, flags, counters | Fast, limited query capability |

## Pattern Map

| Need | Pattern | Link |
|------|---------|------|
| Track task progress through defined stages | State machine | [state-machine.md](../../families/L-memory-state/patterns/state-machine.md) |
| Save progress to resume after failure | Checkpoint state | [checkpoint-state.md](../../families/L-memory-state/patterns/checkpoint-state.md) |
| Compress old context to fit more in | Summarized memory | [summarized-memory.md](../../families/L-memory-state/patterns/summarized-memory.md) |
| Pass work products between agents | Artifact state | [artifact-state.md](../../families/L-memory-state/patterns/artifact-state.md) |
| Track where information came from | Provenance-tagged memory | [provenance-tagged-memory.md](../../families/L-memory-state/patterns/provenance-tagged-memory.md) |
| Persist beyond session lifetime | External durable state | [external-durable-state.md](../../families/L-memory-state/patterns/external-durable-state.md) |
| Prevent cross-session contamination | Session isolation | [session-isolation.md](../../families/L-memory-state/patterns/session-isolation.md) |
| Give each agent only what it needs | Scoped memory | [scoped-memory.md](../../families/L-memory-state/patterns/scoped-memory.md) |
| Mediate shared access with controls | Shared memory gateway | [shared-memory-gateway.md](../../families/L-memory-state/patterns/shared-memory-gateway.md) |

## Context Engineering for State

State management is deeply connected to context engineering — what the agent can see determines what it can remember and use:

| Challenge | Solution pattern |
|-----------|-----------------|
| Context fills up with old state | [context-compaction.md](../../families/E-context-engineering/patterns/context-compaction.md) |
| Agent needs info it does not have yet | [just-in-time-retrieval.md](../../families/E-context-engineering/patterns/just-in-time-retrieval.md) |
| Passing state between agents efficiently | [minimal-context-handoff.md](../../families/E-context-engineering/patterns/minimal-context-handoff.md) |
| Large state that does not fit in context | [context-offloading.md](../../families/E-context-engineering/patterns/context-offloading.md) |

## Design Checklist

- [ ] Identified what state the agent needs at each timescale
- [ ] Chosen storage mechanism for each state category
- [ ] Defined access control (who reads, who writes)
- [ ] Designed lifecycle (when is state created, updated, expired, deleted)
- [ ] Handled the "cold start" problem (what happens with no prior state?)
- [ ] Planned for state growth (what happens after 1000 sessions?)
- [ ] Addressed consistency (what if two agents update the same state?)
- [ ] Considered privacy (does state contain sensitive information? who can access it?)

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Relying on context window as memory | State lost on context overflow or new session | Externalize important state |
| No state expiration | Unbounded growth, stale information | Define TTLs and cleanup policies |
| Shared mutable state without coordination | Race conditions, inconsistent reads | Use gateway pattern or event sourcing |
| Storing raw conversation as "memory" | Noise accumulates, retrieval degrades | Summarize and structure before storing |
| No provenance tracking | Cannot debug where bad state came from | Tag state with source and timestamp |
| Mixing session state across users | Privacy violations, confused responses | Strict session isolation |

## Anti-Patterns to Watch For

- [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) — if state is not updated between retries, the agent is stuck in a loop with the same inputs
- [Infinite/Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md) — state accumulation without bounds leads to degraded performance

## Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
