# Mental Models for Agent Systems

## Scenario

You want to understand the fundamental concepts behind agent design before diving into specific patterns. You have heard terms like "harness," "orchestrator," "context window," and "tool use" but need a coherent mental model of how these pieces fit together.

## Quick Answer

1. **An agent is a model in a loop** — the model proposes actions, the harness executes them, the results feed back into the model. Everything else is detail.
2. **The harness is the real system** — the LLM is a component. The harness controls execution, enforces constraints, manages state, and provides tools. See [F-harness-environment](../../families/F-harness-environment/).
3. **Context is the bottleneck** — every design decision ultimately trades off what the model can see (context) against what it needs to decide. See [E-context-engineering](../../families/E-context-engineering/).

## Core Mental Models

### Model 1: The Agent Loop

Every agent system follows this loop:

```
[Observe] → [Think] → [Act] → [Observe result] → [Think] → ...
```

The model receives observations (tool results, user input, system state), reasons about what to do, selects an action (tool call, response, delegation), and then observes the result. The harness manages this loop — it is NOT the model managing itself.

**Key insight:** The harness decides when the loop starts, when it ends, what tools are available, and what the model can see. The model only decides what to do within those constraints.

Related patterns: [react.md](../../families/A-workflow-topology/patterns/react.md), [bounded-loop.md](../../families/A-workflow-topology/patterns/bounded-loop.md)

### Model 2: Workflow vs. Agent

There is a spectrum from fully deterministic to fully autonomous:

| Approach | Who decides the steps? | Example |
|----------|----------------------|---------|
| Pipeline | Developer (hardcoded) | ETL pipeline |
| Prompt chain | Developer (fixed sequence, LLM fills slots) | Summarize → Translate → Format |
| Workflow | Developer (structure) + LLM (content) | Router picks a path, each path is fixed |
| Agent | LLM (decides next step each iteration) | ReAct loop with tools |
| Multi-agent | Multiple LLMs (negotiate, delegate) | Coordinator assigns to specialists |

**Key insight:** Move right on this spectrum only when the task requires it. Most production systems sit in the "workflow" zone, not the "agent" zone.

Related patterns: [prompt-chaining.md](../../families/A-workflow-topology/patterns/prompt-chaining.md), [routing.md](../../families/A-workflow-topology/patterns/routing.md), [sequential-workflow.md](../../families/A-workflow-topology/patterns/sequential-workflow.md)

### Model 3: Context as Working Memory

The context window is the model's entire working memory. It cannot remember anything not in the current context. This has deep implications:

- **Context is finite** — you must choose what goes in and what stays out
- **Context degrades** — as it fills up, the model's attention becomes less precise
- **Context is per-call** — between API calls, everything outside the context is forgotten unless explicitly managed

**Key insight:** Context engineering (what to include, when, in what format) is the highest-leverage design activity in agent systems.

Related patterns: [progressive-disclosure.md](../../families/E-context-engineering/patterns/progressive-disclosure.md), [context-compaction.md](../../families/E-context-engineering/patterns/context-compaction.md), [minimal-context-handoff.md](../../families/E-context-engineering/patterns/minimal-context-handoff.md)

### Model 4: Tools as the Agent's Hands

Without tools, a model can only produce text. Tools give it the ability to:

- **Read** — fetch files, query databases, search the web
- **Write** — create files, call APIs, modify state
- **Verify** — run tests, check outputs, validate results

**Key insight:** Tool design is API design for an LLM consumer. The tools you provide define what the agent can do and strongly influence what it will try to do.

Related patterns: [G01 through G10](../../families/G-tool-action-design/)

### Model 5: Verification is Not Optional

LLMs produce probabilistic output. Without verification, you cannot know if the agent did the right thing. Verification operates at multiple levels:

| Level | What it checks | Example |
|-------|---------------|---------|
| Output format | Does it match the schema? | JSON validation |
| Semantic correctness | Is the content right? | Unit tests, assertions |
| Task completion | Did it achieve the goal? | End-to-end evaluation |
| Safety | Did it stay within bounds? | Permission checks, output filters |

**Key insight:** The less deterministic the task, the more important verification becomes. Build verification into the loop, not just at the end.

Related patterns: [D-verification-evaluation](../../families/D-verification-evaluation/), [maker-checker.md](../../families/C-orchestration/patterns/maker-checker.md)

### Model 6: State Lives Outside the Model

The model itself is stateless between calls. All persistence must be managed externally:

- **Short-term:** Context window (current conversation)
- **Medium-term:** Scratchpads, artifacts, working files
- **Long-term:** Databases, file systems, external memory

**Key insight:** Deciding where state lives and who can access it is an architectural decision, not an implementation detail.

Related patterns: [L-memory-state](../../families/L-memory-state/), [checkpoint-state.md](../../families/L-memory-state/patterns/checkpoint-state.md), [external-durable-state.md](../../families/L-memory-state/patterns/external-durable-state.md)

## Decision Framework: Complexity Budget

Before choosing patterns, assess your complexity budget:

```
Task complexity → determines minimum architecture
Team capability → determines maximum architecture
Gap between them → your design space
```

- If the task is simple (classification, extraction, formatting): use a single LLM call with validation
- If the task requires multiple steps with dependencies: use prompt chaining or a workflow
- If the task requires dynamic decision-making: use an agent loop
- If the task requires specialized knowledge across domains: consider multi-agent

## Anti-Patterns to Watch For

- [Multi-Agent by Default](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md) — architectural complexity without a forcing function
- [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) — hoping the model will get it right if you just ask again
- [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) — optimizing cost at the expense of quality without measurement

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://web.stanford.edu/class/cs224g/lectures/Agentic_Design_Patterns.pdf
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html
