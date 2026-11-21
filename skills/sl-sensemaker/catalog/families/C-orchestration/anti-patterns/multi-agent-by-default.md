# Anti-Pattern: Multi-Agent by Default

## Name

Multi-Agent by Default

## Also Known As

- Agent Sprawl
- Orchestration Theater
- Premature Decomposition

## Intent (Misapplied)

Decompose every task into multiple agents because multi-agent architectures seem more capable, more production-ready, or more impressive — regardless of whether the task actually requires it.

## Symptoms

- The system has more coordination logic than task logic.
- Adding another agent is the default response to any quality or reliability problem.
- The team cannot explain why each agent boundary exists — they "just felt right."
- Debugging requires tracing across 5+ agents to find the source of a simple error.
- Latency is dominated by inter-agent handoffs, not actual task execution.
- The system works, but a prototype with a single well-prompted agent produces equivalent results.
- Agents are created to "specialize" in tasks that a generalist handles equally well.
- The context passed between agents is nearly identical to what a single agent would hold.

## Motivation for the Anti-Pattern

The anti-pattern is seductive for several reasons:

- **Parallelism feels like progress.** Running five agents concurrently looks faster and more sophisticated than one agent running sequentially — even when the total computation is the same.
- **Specialization feels like quality.** A "legal specialist agent" sounds more reliable than a generalist with a legal-focused prompt — even when the underlying model and training are identical.
- **Complexity signals effort.** A diagram with ten agents and arrows impresses stakeholders in ways that a single well-designed prompt does not.
- **It postpones hard thinking.** Decomposing a problem into agents is easier than writing a clear, focused single-agent prompt that handles the problem correctly.

## Consequences

| Consequence | Description |
|-------------|-------------|
| Latency inflation | Every inter-agent call adds network round-trip, serialization, and LLM inference time |
| Cost amplification | N agents × M turns = N×M LLM calls; costs scale super-linearly with agent count |
| Coordination bugs | Context translation between agents introduces errors that would not exist in a single agent |
| Debugging complexity | Stack traces span multiple agents; correlating a wrong output to its root cause requires full trace infrastructure |
| Fragile failure modes | One slow or failing agent cascades to the entire system; single-agent failures are self-contained |
| Stale context | Each agent receives a summarized or truncated version of prior context; information loss accumulates |
| Maintenance burden | Each agent is a separate system prompt, tool configuration, and test surface to maintain |

## Root Cause

The anti-pattern stems from applying multi-agent as a default architectural choice rather than as a solution to a specific, demonstrated constraint. The constraints that justify multi-agent are:

1. Genuine context overflow that cannot be resolved by retrieval or summarization
2. Subtasks that are provably independent and where parallelism meaningfully reduces wall-clock time
3. Specialization that produces measurable quality improvement over a generalist
4. Independent verification that requires structural isolation (the same agent cannot unbiasedly verify its own output)

When none of these constraints is present, multi-agent adds complexity without benefit.

## Refactored Solution

Before reaching for multi-agent, apply these in order:

1. **Write a better single-agent prompt.** Most "complex tasks that need multiple agents" are complex because the prompt is vague or poorly structured.
2. **Use retrieval to extend effective context.** If context overflow is the concern, retrieval-augmented generation (RAG) often solves it without spawning agents.
3. **Use tools, not agents, for external calls.** Web search, code execution, and database queries are tools — they do not need to be wrapped in separate agents unless their internal complexity genuinely requires an agentic loop.
4. **Use a single agent with a longer model.** If the task requires more reasoning, upgrade the model — don't split the task.
5. **Add agents only when a specific, demonstrated constraint requires it.** Use the [Do You Actually Need Multi-Agent?](../guides/do-you-need-multi-agent.md) guide before adding each new agent.

## Detection Checklist

Use this checklist to audit an existing multi-agent system for this anti-pattern:

- [ ] Can you state, in one sentence, why each agent boundary exists?
- [ ] Would removing any agent (and folding its logic into the caller) break correctness or violate a real constraint?
- [ ] Is the context each agent receives meaningfully different from what the calling agent already holds?
- [ ] Is coordination logic (routing, error handling, retries) a minority of the codebase?
- [ ] Has a single-agent baseline been tested and found insufficient?

If any checkbox cannot be marked done, the system likely has unnecessary agents.

## Related Patterns

- [Do You Actually Need Multi-Agent?](../guides/do-you-need-multi-agent.md) — decision guide to apply before building
- [Manager → Workers](../patterns/manager-workers.md) — the correct pattern when multi-agent is genuinely justified and a single owner is needed
- [Agent-as-Tool](../patterns/agent-as-tool.md) — wrapping a complex sub-process as a tool delays the agent boundary until it is actually needed
- [Family N — Efficiency](../../N-efficiency-routing/README.md) — patterns for reducing agent count and cost

## Sources

- **Anthropic Engineering** — AI safety company; authors of Claude. [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **OpenAI Engineering** — AI research company; authors of GPT and Codex. [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- **Google Cloud Architecture Center** — Google's cloud architecture team. [Choose a Design Pattern for Agentic AI](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- **Stanford CS224G** — Stanford University course on LLM agents. [Agentic Design Patterns (lecture slides)](https://web.stanford.edu/class/cs224g/2025/lectures/Agentic_Design_Patterns.pdf)
