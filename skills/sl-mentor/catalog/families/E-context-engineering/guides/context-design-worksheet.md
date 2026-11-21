# Guide: Context Design Worksheet

## Purpose

Use this worksheet when designing the context strategy for a new agent or when refactoring an existing agent whose performance has degraded. Work through each section sequentially — the outputs of earlier sections feed into later ones.

---

## Step 1: Inventory the Information

List every category of information your agent needs access to. Do not filter yet — capture everything.

| # | Information Category | Example | Approximate Size | Change Frequency |
|---|---|---|---|---|
| 1 | _e.g., Project coding conventions_ | _Naming rules, file structure_ | _~2K tokens_ | _Monthly_ |
| 2 | _e.g., Current task description_ | _Issue/ticket content_ | _~500 tokens_ | _Per task_ |
| 3 | _e.g., Codebase structure_ | _File tree, module boundaries_ | _~10K tokens_ | _Weekly_ |
| 4 | ... | | | |

**Completeness check:** For each category, ask "If the agent lacked this, what would go wrong?" If nothing would go wrong, remove it.

---

## Step 2: Classify by Placement

For each item from Step 1, determine where it should live using the classification criteria below.

### Classification Criteria

| Criterion | System Prompt | Retrieval (on-demand) | State Machine | Not Needed |
|---|---|---|---|---|
| Needed every turn? | Yes | No | No | — |
| Size vs. budget? | Fits in budget | Too large | Tiny | — |
| Changes mid-session? | No (or rarely) | Yes | Yes (deterministic) | — |
| Model must reason over it? | Yes | Yes (after retrieval) | No (harness reads it) | No |

Fill in this table:

| # | Information Category | Placement | Justification |
|---|---|---|---|
| 1 | | System Prompt / Retrieval / State / Drop | |
| 2 | | | |
| 3 | | | |

---

## Step 3: Budget the Context Window

Your context window has a fixed token limit. Allocate it deliberately.

| Slot | Token Budget | Contents |
|---|---|---|
| System prompt (fixed) | _____ tokens | Always-present instructions, role definition, rules |
| Task description | _____ tokens | Current task/issue being worked on |
| Retrieved context | _____ tokens | Dynamically loaded knowledge per step |
| Conversation history | _____ tokens | Recent turns, summaries of older turns |
| Tool results | _____ tokens | Outputs from tool calls in current turn |
| Output space | _____ tokens | Reserved for the model's response |
| **Total** | _____ tokens | Must not exceed model's context limit |

**Rules of thumb:**
- System prompt should be < 20% of total context for most tasks
- Reserve at least 25% for the model's output on generation tasks
- Retrieved context should be the most elastic slot — scales with task complexity
- If conversation history is consuming > 30% of budget, trigger compaction

---

## Step 4: Design the Retrieval Strategy

For each item classified as "Retrieval" in Step 2, define how and when it gets loaded.

| # | What to Retrieve | Trigger | Retrieval Method | Freshness Requirement |
|---|---|---|---|---|
| 1 | _e.g., File contents_ | _Agent decides to read a file_ | _Tool call: read_file_ | _Always live_ |
| 2 | _e.g., Related docs_ | _Task mentions a concept_ | _Semantic search over docs_ | _Index updated daily_ |
| 3 | ... | | | |

**Quality checks:**
- Is the trigger reliable? (Will the agent know when to retrieve?)
- Is the retrieval method fast enough? (< 2s for interactive use)
- Can retrieval fail? What happens then? (Fallback strategy)

---

## Step 5: Design Context Lifecycle

How does context change during the agent's session?

### Session Start

What gets loaded when the agent starts?

- [ ] System prompt (static instructions)
- [ ] Task description from external source
- [ ] Initial state from state machine
- [ ] Pre-fetched context (predicted needs)

### Mid-Session Updates

What changes during the session?

| Event | Context Action |
|---|---|
| _Agent completes a step_ | _Update state machine, optionally compact history_ |
| _Agent calls a tool_ | _Tool result added to context_ |
| _Context budget approaching limit_ | _Trigger compaction or offloading_ |
| _Agent spawns sub-agent_ | _Prepare minimal-context handoff_ |

### Session End

What gets persisted?

- [ ] Updated state machine
- [ ] Key conclusions to external memory
- [ ] Session summary for future retrieval
- [ ] Artifacts produced (code, plans, documents)

---

## Step 6: Validate Against Failure Modes

Review your design against the five context failure modes. For each, confirm your design prevents it.

| Failure Mode | Prevention in This Design | Confidence |
|---|---|---|
| Overload (too much) | _e.g., Budget enforced, progressive disclosure_ | High / Medium / Low |
| Starvation (too little) | _e.g., Retrieval covers all needed knowledge_ | High / Medium / Low |
| Stale context | _e.g., Live retrieval, short sessions_ | High / Medium / Low |
| Conflicting context | _e.g., Single source of truth per topic, priority hierarchy_ | High / Medium / Low |
| Leaked context | _e.g., Role-scoped, no shared context bus_ | High / Medium / Low |

If any row has "Low" confidence, revisit the design before building.

---

## Step 7: Document the Design

Record the final decisions in a format your team can review and maintain.

```
Agent: [name]
Model: [model and context limit]
Context Budget: [total tokens allocated]

System Prompt: [size, what it contains, where it lives in the repo]
Retrieval Sources: [list with trigger conditions]
State Machine: [what it tracks, where it persists]
Compaction Strategy: [when triggered, what method]
Handoff Strategy: [what goes to sub-agents, what stays]
```

---

## Related Patterns

- [Context Failure Modes](./context-failure-modes.md) — the failures this worksheet helps prevent
- [Context vs. Memory vs. State](./context-vs-memory-vs-state.md) — detailed comparison of storage mechanisms
- [Progressive Disclosure](../patterns/progressive-disclosure.md) — layered context loading
- [Map-Not-Manual](../patterns/map-not-manual.md) — keeping system prompts lean
- [Context Compaction](../patterns/context-compaction.md) — managing context growth mid-session

---

## Sources

- Anthropic — [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
