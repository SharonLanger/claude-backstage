# Guide: Context vs. Memory vs. State

## Purpose

Use this guide when designing a new agent system and deciding where information should live. Context window, external memory, and state machines serve different purposes — conflating them leads to systems that are either brittle (over-reliance on context) or over-engineered (external memory for everything).

---

## Definitions

| Mechanism | What it is | Lifetime | Capacity | Access pattern |
|---|---|---|---|---|
| **Context Window** | Tokens visible to the model in a single call | One turn / one session | Fixed (model-dependent) | Full random access within the window |
| **External Memory** | Persistent store retrieved into context on demand | Cross-session, indefinite | Unbounded | Query-then-load (retrieval) |
| **State Machine** | Deterministic tracking of where the process is and what has happened | Session or workflow | Small (states + transitions) | Programmatic read/write |

---

## Decision Matrix

Use this table to determine where a piece of information belongs.

| Question | Context Window | External Memory | State Machine |
|---|---|---|---|
| Does the model need it for the CURRENT reasoning step? | Yes | No | No |
| Does it need to persist across sessions? | No | Yes | Yes (if tracking progress) |
| Is it a fact about the project that rarely changes? | Only if currently needed | Yes (retrieve when needed) | No |
| Is it the current step in a multi-step process? | No (don't rely on the model to track this) | No | Yes |
| Is it a rule/constraint the model must always follow? | Yes (system prompt) | No | No |
| Is it historical conversation context? | Only recent/relevant turns | Yes (long-term) | No |
| Is it the result of a previous agent's work? | Only if needed now | Yes (artifact store) | No |
| Can it be verified deterministically? | No (move to state/code) | No | Yes |

---

## When to Use Each

### Use Context Window When

- The information is needed for the current reasoning step
- The information fits within token limits without crowding out other needed context
- The information is ephemeral (not needed after this turn)
- The information is a rule or constraint that must always be followed (system prompt)
- Freshness matters — you need the model to see the latest version

### Use External Memory When

- The information persists across sessions
- The total knowledge exceeds what fits in a context window
- Only a subset is relevant at any given step (retrieval is selective)
- The information is shared across multiple agents
- You need an audit trail of what was known and when

### Use State Machine When

- You are tracking progress through a multi-step workflow
- The transitions between steps are deterministic (not model-decided)
- You need to resume a workflow after a failure
- Certain actions are only valid in certain states (e.g., "can only push after commit")
- You need to enforce ordering that the model might violate

---

## Common Mistakes

| Mistake | Why it fails | Fix |
|---|---|---|
| Putting workflow state in the context window | Model may "forget" which step it's on across long sessions; no recovery on crash | Use explicit state tracking outside the model |
| Storing everything in external memory and retrieving on every turn | Adds latency, retrieval errors, and can return irrelevant results | Keep always-needed rules in system prompt; retrieve only on-demand knowledge |
| Using context window as long-term memory | Context resets between sessions; long sessions cause drift | Persist important conclusions to external memory |
| Using external memory for real-time data | Retrieval adds latency; stale indexes miss recent changes | Read live data into context at the point of use |
| Tracking state in the prompt ("remember you are on step 3") | Model may misparse or lose track | Use programmatic state that the harness reads |

---

## Architecture Decision Record Template

When designing a new agent, fill in this table for each category of information the agent needs:

| Information | Where it lives | Why | Refresh strategy |
|---|---|---|---|
| Project conventions | System prompt (context) | Always needed, rarely changes | Update system prompt on convention changes |
| Codebase structure | External memory (retrieval) | Too large for context, subset needed per task | Re-index on significant changes |
| Current task progress | State machine | Must survive crashes, enforce ordering | Updated programmatically after each step |
| Previous conversation | External memory | Too long for context, selectively relevant | Summarize and store after each session |
| Tool results | Context window | Needed for current reasoning | Fresh per invocation |

---

## Related Patterns

- [Context Offloading](../patterns/context-offloading.md) — moving information from context to external storage
- [Just-in-Time Retrieval](../patterns/just-in-time-retrieval.md) — loading from external memory into context at the right moment
- [Context Compaction](../patterns/context-compaction.md) — reducing context when it grows too large
- [Repository-as-System-of-Record](../patterns/repository-as-system-of-record.md) — using the repo as the authoritative external memory

---

## Sources

- Anthropic — [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
