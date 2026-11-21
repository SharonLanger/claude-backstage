# Start Here: New to AI Agents

## Scenario

You are a developer who has used LLMs for chat or code completion but has never built an agentic system. You want to understand what "agents" actually are, what the simplest useful architecture looks like, and where to go from there.

## Quick Answer

1. **Start with the simplest topology that works** — a single LLM call with tools, or a prompt chain. Do not begin with multi-agent systems. See [A-workflow-topology](../../families/A-workflow-topology/) for the foundational patterns.
2. **Understand the harness** — an agent is not just a model. It is a model running inside a loop with tool access, managed by a harness that controls execution. See [F-harness-environment](../../families/F-harness-environment/) for how the surrounding infrastructure works.
3. **Add verification early** — the difference between a demo and production is whether you can tell if the agent did the right thing. See [D-verification-evaluation](../../families/D-verification-evaluation/) for evaluation patterns.

## Learning Path

### Level 1: Single-Agent Basics

Before building anything complex, understand these core building blocks:

| Concept | What it means | Pattern to study |
|---------|--------------|-----------------|
| Prompt chaining | Break a task into sequential LLM calls | [prompt-chaining.md](../../families/A-workflow-topology/patterns/prompt-chaining.md) |
| Tool use | Let the model call functions | [G-tool-action-design](../../families/G-tool-action-design/) |
| The agent loop | Model calls tools, observes results, decides next step | [react.md](../../families/A-workflow-topology/patterns/react.md) |
| Bounded execution | Prevent runaway loops | [bounded-loop.md](../../families/A-workflow-topology/patterns/bounded-loop.md) |

### Level 2: Making It Reliable

Once you have a working single agent, the next challenge is making it consistently good:

| Concept | What it means | Pattern to study |
|---------|--------------|-----------------|
| Output validation | Check that results match expected structure | [schema-validation.md](../../families/O-output-integration/patterns/schema-validation.md) |
| Retry with feedback | When something fails, give the model the error | [retry-with-feedback.md](../../families/I-reliability-recovery/patterns/retry-with-feedback.md) |
| Stop conditions | Know when to stop trying | [stop-condition.md](../../families/I-reliability-recovery/patterns/stop-condition.md) |
| Evals | Measure whether your agent actually works | [D01-deterministic-validator.md](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) |

### Level 3: Scaling Up

Only after Level 2 is solid should you consider:

| Concept | What it means | Pattern to study |
|---------|--------------|-----------------|
| Task decomposition | Breaking complex work into subtasks | [B1-plan-execute.md](../../families/B-task-decomposition/patterns/B1-plan-execute.md) |
| Multiple agents | Specialists that coordinate | [multi-agent.md](../designing/multi-agent.md) |
| Context management | Keeping agents focused | [context-isolation.md](../../families/E-context-engineering/patterns/context-isolation.md) |
| Security boundaries | Preventing harm at scale | [J01-least-privilege.md](../../families/J-security-trust/patterns/J01-least-privilege.md) |

## Common First Mistakes

| Mistake | Why it happens | What to do instead |
|---------|---------------|-------------------|
| Starting with multi-agent | "Agents" sounds like it needs multiple | Start with one agent, add more only when you hit limits |
| No evaluation | Hard to measure LLM output | Add deterministic checks from day one |
| Unbounded loops | Assuming the model will "figure it out" | Always set iteration limits and stop conditions |
| Too much context | Dumping everything into the prompt | Give the agent only what it needs for the current step |

## Anti-Patterns to Watch For

- [Multi-Agent by Default](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md) — reaching for multiple agents before proving a single agent is insufficient
- [Infinite/Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md) — letting an agent run without clear termination criteria
- [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md) — optimizing for cost before you know what works

## Next Steps

- Read [Mental Models](mental-models.md) for the conceptual foundation
- When ready to build, go to [Designing a New System](../designing/new-system.md)

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html
- https://web.stanford.edu/class/cs224g/2025/lectures/Agentic_Design_Patterns.pdf
