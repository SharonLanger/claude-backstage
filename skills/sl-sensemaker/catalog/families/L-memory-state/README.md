# Family L — Memory & State

**Recurring problem:** Long-running agent work cannot rely solely on an ever-growing conversational context. As tasks extend across steps, sessions, and agent handoffs, the context window becomes a bottleneck — expensive, lossy at the boundary, and unavailable across process restarts.

**Family L answer:** Externalize, compress, or scope what the agent needs to remember. Trade context space for durable, queryable, structured memory.

---

## Directory Tree

```
L-memory-state/
├── README.md                          ← this file (navigation + taxonomy + decision guide)
└── patterns/
    ├── external-durable-state.md          ← persist structured state to an external store (DB, KV, file)
    ├── artifact-state.md                  ← use produced artifacts (files, documents) as implicit state
    ├── checkpoint-state.md                ← snapshot progress at safe points; resume after failure
    ├── shared-memory-gateway.md           ← single controlled interface for multi-agent shared memory
    ├── session-isolation.md               ← scope memory strictly to one session; no cross-contamination
    ├── scoped-memory.md                   ← partition memory by role, task, or agent to limit blast radius
    ├── summarized-memory.md               ← compress old context into summaries before it is evicted
    ├── state-machine.md                   ← make agent state explicit; transitions are the only writes
    └── provenance-tagged-memory.md        ← tag every memory entry with source, time, and confidence
```

---

## Per-Pattern File Schema

Every pattern file follows this structure:

```
# <Pattern Name>

**Family:** L — Memory & State
**Also known as:** <aliases if any>
**Related patterns:** <pattern names in this or other families>

## Problem
One paragraph: what breaks without this pattern.

## Forces
Bullet list of competing concerns the pattern resolves.

## Solution
How the pattern works. Implementation-focused. No fluff.

## Structure
Mermaid diagram (flowchart or sequence) showing the key components and data flow.

## Implementation Notes
- Language/framework-specific notes
- Common failure modes
- Cost / latency tradeoffs

## Examples
Concrete scenarios (2–3) showing the pattern applied.

## Consequences
### Benefits
### Liabilities

## Related Families
Cross-references to patterns in E (context engineering), F (harness), I (reliability), M (observability).
```

---

## Memory Type Taxonomy

Four types of memory arise in agent systems, drawn from cognitive science:

| Type | What it holds | Lifetime | Typical implementation |
|---|---|---|---|
| **Working memory** | The current task's active reasoning — what the agent is thinking about right now | Single step or turn | Context window, scratchpad variable |
| **Episodic memory** | Specific past events — "what happened in run #42", session logs, interaction history | Session to long-term | Append-only log, vector store with timestamps |
| **Semantic memory** | General facts and domain knowledge — stable, not tied to a specific event | Long-term, rarely mutated | Knowledge base, embeddings index, config files |
| **Procedural memory** | How to do things — skills, workflows, tool-use patterns | Long-term, versioned | Skill files, prompt templates, runbooks |

**Where each pattern fits:**

| Pattern | Memory type(s) targeted |
|---|---|
| External Durable State | Working → Episodic (persisted) |
| Artifact State | Episodic, Semantic |
| Checkpoint State | Working (snapshotted) |
| Shared-Memory Gateway | All types (controlled access layer) |
| Session Isolation | Working, Episodic (scoped) |
| Scoped Memory | All types (partitioned) |
| Summarized Memory | Episodic → Semantic (compressed) |
| State Machine | Working (structured) |
| Provenance-Tagged Memory | Episodic, Semantic (annotated) |

---

## When to Use Context vs Memory vs External State

Use this guide when deciding where information should live.

### Use the context window when:
- The information is needed **right now**, in this turn or step
- The total size fits comfortably (well under the model's limit)
- The task is short-lived and won't be resumed
- You need the model to reason over the full content (not a retrieval summary)

### Use in-session memory (summarized or scoped) when:
- The task spans multiple turns but **ends in the same session**
- Context is growing too large; older content can be compressed without losing fidelity
- Multiple sub-agents share a workspace but shouldn't share raw context

### Use external durable state when:
- The task **spans sessions** or may be interrupted and resumed
- Multiple agents (possibly concurrent) need to read and write shared state
- Auditability, rollback, or history replay is required
- The state is too large or structured for the context window (tables, trees, blobs)

### Decision flowchart

```
Is the information needed beyond this session?
├── Yes → External Durable State (+ Provenance-Tagged if auditability matters)
└── No → Is the context window under pressure?
           ├── Yes → Summarized Memory or Scoped Memory
           └── No → Context window is fine; no pattern needed

Is the task resumable after failure?
└── Yes → Checkpoint State (regardless of above)

Do multiple agents share this state?
└── Yes → Shared-Memory Gateway (wraps whichever storage you chose)

Is the agent's progress a sequence of discrete stages?
└── Yes → State Machine (structures transitions; combine with durable state for persistence)
```

---

## Related Families

| Family | Relationship to L |
|---|---|
| **E — Context Engineering** | Memory is the alternative when context is insufficient; E patterns shrink what must go in context |
| **F — Harness** | Persistent task artifacts (F) are a substrate for Artifact State (L) |
| **I — Reliability** | Checkpoint/resume (I) is the reliability application of Checkpoint State (L) |
| **M — Observability** | Provenance tracking (M) extends Provenance-Tagged Memory (L) to the full audit trail |

---

Last updated: 2026-08-24
