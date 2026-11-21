# AP05 — Multi-Agent by Default

## Symptoms

- The system has multiple agents where a single agent with better tools would suffice
- Debugging requires tracing messages across agent boundaries for simple tasks
- Inter-agent communication introduces latency and failure modes that dwarf the task complexity
- The team cannot explain what specific problem multi-agent architecture solves that a workflow could not
- Coordination bugs (lost context, conflicting actions, deadlocks) outnumber domain bugs
- Token costs are multiplied because each agent carries its own system prompt and context

## Root Cause

Teams reach for multi-agent architectures because they sound sophisticated or because a demo looked impressive, rather than because the task requires autonomous sub-problems that cannot share a single context window. The allure of "agents talking to each other" obscures the engineering cost: every agent boundary is a serialization point where context is lost, coordination must be explicit, and failure modes multiply. Most tasks that seem to need multiple agents actually need a single agent with well-designed tools, or a deterministic workflow with LLM calls at specific points.

## Failure Scenario

A team builds a "research agent," "writing agent," and "editing agent" to produce blog posts. The research agent gathers facts and passes them to the writing agent, which drafts the post and passes it to the editing agent. In practice, the writing agent loses nuance from the research because the handoff is a compressed summary. The editing agent rewrites sections in ways that contradict the research because it never saw the original sources. Debugging why a factual error appeared requires tracing through three agent logs. The team eventually discovers that a single agent with a web-search tool and a self-revision loop produces better posts in one-third the time at one-quarter the cost.

## Counter-Patterns

- [A07 — Prompt Chaining](../families/A-workflow-topology/patterns/prompt-chaining.md) — Use deterministic workflows before reaching for agents
- [A01 — Sequential Workflow](../families/A-workflow-topology/patterns/sequential-workflow.md) — Chain simple steps rather than autonomous agents
- [C01 — Orchestrator-Workers](../families/C-orchestration/patterns/orchestrator-workers.md) — When multi-agent is justified, use clear hierarchy
- [E07 — Minimal-Context Handoff](../families/E-context-engineering/patterns/minimal-context-handoff.md) — If you must split, minimize what crosses boundaries

## Sources

- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- OpenAI — [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
