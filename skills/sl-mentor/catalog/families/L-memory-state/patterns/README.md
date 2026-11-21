# Family L — Memory & State: Patterns

9 patterns covering how long-running agent work persists information across steps, sessions, and agent handoffs.

**Central insight (Microsoft):** Persist long-running state externally. Do not pass accumulated context to the next agent if that agent does not need it — context dumps are expensive, noisy, and often carry stale or irrelevant information.

**Sources:** Anthropic Engineering, Microsoft Azure Architecture Center, OpenAI Engineering.

---

## Files

```
patterns/
├── README.md                     ← this file
├── artifact-state.md             ← treat produced files/documents as the primary state carrier; skip a separate state store
├── checkpoint-state.md           ← snapshot progress at safe points so a failed task can resume without reprocessing completed work
├── external-durable-state.md     ← persist task state outside the context window so it survives session ends and restarts
├── provenance-tagged-memory.md   ← tag every memory entry with source, author, timestamp, and confidence so it can be audited and invalidated
├── scoped-memory.md              ← partition memory by agent/role/sub-task scope; do not expose all memory to all agents
├── session-isolation.md          ← prevent memory leakage between concurrent users, tenants, or sessions on shared infrastructure
├── shared-memory-gateway.md      ← route all multi-agent reads and writes through a controlled access layer with conflict resolution
├── state-machine.md              ← model agent task progress as explicit states with defined transitions and invariants
└── summarized-memory.md          ← compact growing history into summaries that preserve meaning while reducing context size
```

---

## Pattern Schema

Every file in this folder follows the same structure:

| Section | Contents |
|---|---|
| **Title + metadata** | Pattern name, Family, aliases, related patterns |
| **Problem** | The failure mode this pattern prevents |
| **Forces** | Competing concerns that make the problem non-trivial |
| **Solution** | The architectural response in plain language |
| **Structure** | Mermaid diagram in a collapsible `<details>` block |
| **Implementation Notes** | Concrete guidance, format recommendations, failure modes |
| **Examples** | 2–3 worked scenarios showing the pattern in context |
| **Consequences** | Benefits and liabilities in plain terms |
| **Related Families** | Cross-family connections with explanation |
| **Sources** | Citations with relevance summary and URL |

---

## How to Navigate

**Entry by persistence concern:**
- State must survive a crash or restart → `checkpoint-state.md`, `external-durable-state.md`
- State lives in the output artifact itself → `artifact-state.md`
- State grows too large for context → `summarized-memory.md`, `external-durable-state.md`

**Entry by multi-agent concern:**
- Multiple agents sharing one memory store → `shared-memory-gateway.md`
- Agents receiving irrelevant context dumps → `scoped-memory.md`
- Cannot tell who wrote a memory entry or when → `provenance-tagged-memory.md`

**Entry by isolation concern:**
- Different users/tenants on shared infrastructure → `session-isolation.md`
- Agent taking wrong action for current task stage → `state-machine.md`

**Typical composition paths:**
- Long-running batch task: `external-durable-state.md` + `checkpoint-state.md` + `artifact-state.md`
- Multi-agent pipeline: `shared-memory-gateway.md` + `scoped-memory.md` + `provenance-tagged-memory.md`
- Conversational agent over many sessions: `summarized-memory.md` + `session-isolation.md`
- Complex stateful workflow: `state-machine.md` + `checkpoint-state.md`

**Cross-family links:** L patterns sit on the substrate managed by Family F (Harness). Large memory stores interact with Family E (Context Engineering) — E governs what gets loaded into context from the L store. Audit trails for memory writes connect to Family M (Observability). Recovery from bad state connects to Family I (Reliability).

---

Last updated: 2026-08-24
