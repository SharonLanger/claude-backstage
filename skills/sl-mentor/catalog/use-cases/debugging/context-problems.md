# Context Window Issues, Lost State, Prompt Degradation

## Scenario

Your agent loses track of earlier information, ignores instructions that were provided, produces degraded output as conversations grow longer, forgets completed sub-tasks, or fails because critical context was not available when needed. These problems stem from context window limits, poor context management, or state that is not properly persisted.

## Quick Answer

1. **Offload state to external storage** — Don't rely on the context window as your database. Persist important state outside the prompt. See [External Durable State](../../families/L-memory-state/patterns/external-durable-state.md) and [Checkpoint State](../../families/L-memory-state/patterns/checkpoint-state.md).
2. **Compact and scope context deliberately** — Include only what the current step needs. See [Context Compaction](../../families/E-context-engineering/patterns/context-compaction.md) and [Minimal Context Handoff](../../families/E-context-engineering/patterns/minimal-context-handoff.md).
3. **Retrieve just-in-time instead of loading upfront** — Fetch relevant information at the moment of decision, not at the start. See [Just-in-Time Retrieval](../../families/E-context-engineering/patterns/just-in-time-retrieval.md).

## Decision Guide

```
Context problem observed
│
├─ Agent forgets earlier instructions/information
│   ├─ Long conversation (>50K tokens) → Context window saturation
│   │   → Apply: Context Compaction + Summarized Memory
│   ├─ Instructions at start, action much later → Positional decay
│   │   → Apply: Progressive Disclosure + Role-Scoped Context
│   └─ Multi-agent: downstream agent missing info → Handoff loss
│       → Apply: Minimal Context Handoff + Artifact-Based Handoff
│
├─ Agent cannot access information it needs
│   ├─ Information exists but not in prompt → Missing retrieval
│   │   → Apply: Just-in-Time Retrieval + Repository as System of Record
│   ├─ Information was in prompt but removed → Overly aggressive compaction
│   │   → Apply: Scoped Memory + Provenance-Tagged Memory
│   └─ Information spread across sub-agents → No shared state
│       → Apply: Shared Memory Gateway + External Durable State
│
├─ Agent's output quality degrades over time
│   ├─ First outputs good, later outputs sloppy → Context noise accumulation
│   │   → Apply: Context Compaction + Fresh Context Retry
│   ├─ Repeating itself or contradicting earlier work → State confusion
│   │   → Apply: State Machine + Checkpoint State
│   └─ Following stale instructions → State not updated after changes
│       → Apply: External Durable State + Session Isolation
│
└─ State lost between steps or sessions
    ├─ Multi-step task: earlier results lost → No persistence
    │   → Apply: Checkpoint State + Artifact State
    ├─ Session restart: all progress gone → Memory not externalized
    │   → Apply: External Durable State + Summarized Memory
    └─ Parallel agents: conflicting state → No isolation
        → Apply: Session Isolation + Shared Memory Gateway
```

## Relevant Patterns

| Pattern | Family | Role in This Scenario |
|---------|--------|----------------------|
| [Context Compaction](../../families/E-context-engineering/patterns/context-compaction.md) | Context | Summarize or prune older context to stay within window limits |
| [Minimal Context Handoff](../../families/E-context-engineering/patterns/minimal-context-handoff.md) | Context | Pass only essential information between agents/steps |
| [Just-in-Time Retrieval](../../families/E-context-engineering/patterns/just-in-time-retrieval.md) | Context | Fetch information when needed rather than loading everything upfront |
| [Progressive Disclosure](../../families/E-context-engineering/patterns/progressive-disclosure.md) | Context | Reveal instructions/data progressively as the agent reaches relevant steps |
| [Role-Scoped Context](../../families/E-context-engineering/patterns/role-scoped-context.md) | Context | Each agent role sees only the context relevant to its function |
| [Context Isolation](../../families/E-context-engineering/patterns/context-isolation.md) | Context | Prevent context contamination between unrelated tasks |
| [Artifact-Based Handoff](../../families/E-context-engineering/patterns/artifact-based-handoff.md) | Context | Pass structured artifacts (not raw conversation) between agents |
| [External Durable State](../../families/L-memory-state/patterns/external-durable-state.md) | Memory/State | Store state in files, databases, or external systems — not in the prompt |
| [Checkpoint State](../../families/L-memory-state/patterns/checkpoint-state.md) | Memory/State | Save progress at milestones so work survives context loss |
| [Summarized Memory](../../families/L-memory-state/patterns/summarized-memory.md) | Memory/State | Maintain running summaries of past work rather than full transcripts |
| [Scoped Memory](../../families/L-memory-state/patterns/scoped-memory.md) | Memory/State | Different memory scopes for different purposes (task, session, global) |
| [Shared Memory Gateway](../../families/L-memory-state/patterns/shared-memory-gateway.md) | Memory/State | Central state accessible to multiple agents with controlled access |
| [Session Isolation](../../families/L-memory-state/patterns/session-isolation.md) | Memory/State | Prevent state leakage between independent sessions |
| [Provenance-Tagged Memory](../../families/L-memory-state/patterns/provenance-tagged-memory.md) | Memory/State | Track where each piece of remembered information came from |
| [State Machine](../../families/L-memory-state/patterns/state-machine.md) | Memory/State | Track agent progress through explicit states to prevent confusion |
| [Artifact State](../../families/L-memory-state/patterns/artifact-state.md) | Memory/State | Use artifacts (files, documents) as the source of truth for state |
| [Fresh Context Retry](../../families/I-reliability-recovery/patterns/fresh-context-retry.md) | Reliability | When context is poisoned, restart with a clean prompt |
| [Repository as System of Record](../../families/F-harness-environment/patterns/F01-agent-legible-repository.md) | Harness | Use the repository/filesystem as persistent ground truth |

## Anti-Patterns to Watch For

| Anti-Pattern | Why It Causes This Problem |
|--------------|---------------------------|
| [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) | Failed attempts accumulate in context, pushing useful information out of the window and adding noise. |
| [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md) | Aggressively compacting context before understanding what the agent actually needs leads to information loss. |

## Diagnostic Checklist

- [ ] How full is the context window? (Check token count vs model limit)
- [ ] Is critical information at the beginning of a very long context? (Positional decay risk)
- [ ] Are you relying on the conversation history as the sole source of state?
- [ ] When handing off between agents, are you passing structured summaries or raw transcripts?
- [ ] Does the agent have access to retrieval (search, file read) for information it needs?
- [ ] Are completed sub-task results being preserved externally or only in context?
- [ ] Is the prompt growing with each iteration (tool results, error messages accumulating)?
- [ ] Are multiple agents sharing state through a controlled mechanism?
- [ ] Does the agent know its current position in a multi-step task?
- [ ] Can the agent recover if the session is interrupted (checkpointed state)?

## Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/index/harness-engineering/
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
