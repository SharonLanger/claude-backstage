# Principle 5 — Context Is a Designed Resource

> More context is not monotonically better. Context must be selected, scoped, compressed, isolated, and made navigable.

---

## Why This Matters

Language models degrade silently when overloaded with context. Unlike traditional software where more data simply slows processing, excess or poorly organized context causes models to miss instructions, hallucinate connections between unrelated information, and lose track of their current objective. The failure mode is insidious: the system still produces fluent output, making degradation hard to detect without task-level evaluation.

This principle recurs across independent sources because every team building production agent systems discovers the same counterintuitive truth — giving a model "everything it might need" performs worse than giving it precisely what it needs for the current step. Anthropic formalized this as "context engineering," OpenAI operationalized it as the "map not manual" principle, Microsoft applied it to multi-agent handoffs, and Google embedded it in their pattern selection criteria. The convergence is strong because the underlying cause is architectural: finite attention windows and positional degradation are properties of the technology itself.

---

## Which Sources Converge

| Organization | What They Say | Key Concept |
|---|---|---|
| Anthropic | Named and defined "context engineering" as a discipline distinct from prompt engineering | Context is the entire evolving token state — must be designed, not accumulated |
| OpenAI | Keep AGENTS.md short as a map, not a giant manual; make the repository the system of record | Map-not-manual; progressive lookup over upfront loading |
| Microsoft | Minimal-context handoff between agents in orchestration patterns | Each agent receives only what it needs for its specific sub-task |
| Google | Context persistence and scoping as explicit design decisions in agentic patterns | Context isolation between workflow stages |

---

## Patterns That Implement This Principle

- [Progressive Disclosure / Map-Not-Manual](../families/E-context-engineering/patterns/map-not-manual.md) — short top-level file points to deeper knowledge on demand
- [Context Isolation](../families/E-context-engineering/patterns/context-isolation.md) — each agent or step sees only its relevant subset
- [Repository-Local System of Record](../families/F-harness-environment/patterns/F02-repository-local-system-of-record.md) — ground truth lives in structured files, not in the prompt
- [External Durable State](../families/L-memory-state/patterns/external-durable-state.md) — state persists outside the conversation window
- [Minimal-Context Handoff](../families/E-context-engineering/patterns/minimal-context-handoff.md) — orchestrators pass only task-relevant information to workers

---

## Anti-Patterns This Prevents

- **Giant Instruction Manual** — cramming all possible instructions into a single system prompt, causing the model to lose track of which subset applies to the current task
- **Shared Context Everywhere** — giving every agent in a multi-agent system access to the full shared state, causing cross-contamination and irrelevant information competing for attention

---

## Practical Application

1. **Tiered instruction files:** Keep a 20-line top-level instruction file that acts as a navigation map. Deep rules live in separate files loaded only when relevant — the model reads the map, then fetches what it needs.

2. **Per-step context scoping in workflows:** When a coding agent moves from "understand the bug" to "write the fix" to "verify the fix," each phase gets a different context window — bug reports and stack traces for phase one, relevant source files for phase two, test output for phase three.

3. **Agent handoff compression:** When an orchestrator delegates to a worker agent, pass a structured summary of the task and constraints — not the entire conversation history. The worker doesn't need to know how the user arrived at the request.

4. **Context window budgeting:** Allocate portions of the context window deliberately — system instructions get X tokens, retrieved documents get Y tokens, conversation history gets Z tokens — with explicit compression or eviction when a section exceeds its budget.

---

## Sources

- Anthropic — [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
