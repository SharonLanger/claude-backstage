# Designing a New Agent System

## Scenario

You are starting from scratch. You have a problem that seems like it needs an agent (or at least an LLM-powered system), and you need to make foundational architecture decisions: topology, tool design, context strategy, and verification approach.

## Quick Answer

1. **Start with the simplest topology that could work** — prompt chain or single agent loop. Prove it works, then add complexity. See [A-workflow-topology](../../families/A-workflow-topology/).
2. **Design your tools and context strategy before writing agent code** — these constrain everything else. See [G-tool-action-design](../../families/G-tool-action-design/) and [E-context-engineering](../../families/E-context-engineering/).
3. **Build evaluation from day one** — you cannot iterate without measurement. See [D-verification-evaluation](../../families/D-verification-evaluation/).

## Design Checklist

Work through these decisions in order. Each builds on the previous.

### Step 1: Characterize the Task

| Question | If yes... | If no... |
|----------|-----------|----------|
| Are the steps known in advance? | Use a workflow/prompt chain | Consider an agent loop |
| Does it require external data? | Design read tools | Context may suffice |
| Does it modify external state? | Design write tools with guards | Output-only is simpler |
| Can a human verify the output? | Add human-in-the-loop checkpoints | Need automated verification |
| Does it need to handle failures? | Design retry/recovery strategy | Single-shot may work |

### Step 2: Choose a Topology

Start from the left. Move right only when you have evidence the simpler approach fails.

```
Single call → Prompt chain → Router/workflow → Single agent → Multi-agent
```

| Topology | When to use | Key pattern |
|----------|-------------|-------------|
| Single LLM call | Classification, extraction, simple generation | — |
| Prompt chain | Multi-step with fixed sequence | [prompt-chaining.md](../../families/A-workflow-topology/patterns/prompt-chaining.md) |
| Router | Input determines which path to take | [routing.md](../../families/A-workflow-topology/patterns/routing.md) |
| Agent loop | Dynamic number of steps, tool use required | [react.md](../../families/A-workflow-topology/patterns/react.md) |
| Multi-agent | Distinct specializations, context isolation needed | [orchestrator-workers.md](../../families/C-orchestration/patterns/orchestrator-workers.md) |

### Step 3: Design the Harness

The harness is everything around the model. Key decisions:

| Decision | Options | Pattern family |
|----------|---------|---------------|
| How does the loop run? | Fixed iterations, condition-based, budget-based | [F-harness-environment](../../families/F-harness-environment/) |
| What stops execution? | Max iterations, success signal, budget exhaustion | [stop-condition.md](../../families/I-reliability-recovery/patterns/stop-condition.md) |
| What happens on failure? | Retry, escalate, fallback | [I-reliability-recovery](../../families/I-reliability-recovery/) |
| What can the agent see? | Full context, progressive disclosure, scoped views | [E-context-engineering](../../families/E-context-engineering/) |

### Step 4: Design Tools

| Principle | Explanation | Pattern |
|-----------|-------------|---------|
| Least privilege | Only expose tools the agent needs | [J01-least-privilege.md](../../families/J-security-trust/patterns/J01-least-privilege.md) |
| Clear contracts | Tools have unambiguous inputs/outputs | [G-tool-action-design](../../families/G-tool-action-design/) |
| Separate read from write | Reading is safe; writing needs guards | [J11-read-write-separation.md](../../families/J-security-trust/patterns/J11-read-write-separation.md) |
| Return useful errors | The model needs actionable failure info | [retry-with-feedback.md](../../families/I-reliability-recovery/patterns/retry-with-feedback.md) |

### Step 5: Design Context Strategy

| Question | Pattern |
|----------|---------|
| What does the agent need to know upfront? | [role-scoped-context.md](../../families/E-context-engineering/patterns/role-scoped-context.md) |
| How does it get information it needs later? | [just-in-time-retrieval.md](../../families/E-context-engineering/patterns/just-in-time-retrieval.md) |
| What happens when context fills up? | [context-compaction.md](../../families/E-context-engineering/patterns/context-compaction.md) |
| How do sub-tasks share information? | [artifact-based-handoff.md](../../families/E-context-engineering/patterns/artifact-based-handoff.md) |

### Step 6: Design Verification

| What to verify | How | Pattern |
|----------------|-----|---------|
| Output structure | Schema validation | [schema-validation.md](../../families/O-output-integration/patterns/schema-validation.md) |
| Correctness | Deterministic checks, test execution | [D01-deterministic-validator.md](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) |
| Safety | Output filtering, permission checks | [sanitized-output-boundary.md](../../families/O-output-integration/patterns/sanitized-output-boundary.md) |
| Quality over time | Evaluation suites | [D-verification-evaluation](../../families/D-verification-evaluation/) |

### Step 7: Plan for Observability

| Need | Pattern |
|------|---------|
| Debug failing runs | [M-observability-debugging](../../families/M-observability-debugging/) |
| Understand costs | [budgeted-agent-loop.md](../../families/N-efficiency-routing/patterns/budgeted-agent-loop.md) |
| Track decisions | [state-machine.md](../../families/L-memory-state/patterns/state-machine.md) |

## Relevant Patterns by Phase

| Design phase | Key patterns |
|-------------|-------------|
| Topology | [prompt-chaining](../../families/A-workflow-topology/patterns/prompt-chaining.md), [routing](../../families/A-workflow-topology/patterns/routing.md), [react](../../families/A-workflow-topology/patterns/react.md), [bounded-loop](../../families/A-workflow-topology/patterns/bounded-loop.md) |
| Decomposition | [B1-plan-execute](../../families/B-task-decomposition/patterns/B1-plan-execute.md), [B6-reconnaissance-first](../../families/B-task-decomposition/patterns/B6-reconnaissance-first.md) |
| Orchestration | [orchestrator-workers](../../families/C-orchestration/patterns/orchestrator-workers.md), [agent-as-tool](../../families/C-orchestration/patterns/agent-as-tool.md) |
| Reliability | [bounded-retry](../../families/I-reliability-recovery/patterns/bounded-retry.md), [circuit-breaker](../../families/I-reliability-recovery/patterns/circuit-breaker.md) |
| Security | [J01-least-privilege](../../families/J-security-trust/patterns/J01-least-privilege.md), [J11-read-write-separation](../../families/J-security-trust/patterns/J11-read-write-separation.md) |

## Anti-Patterns to Watch For

- [Multi-Agent by Default](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md) — adding agents before proving one is insufficient
- [Infinite/Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md) — not defining clear termination
- [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md) — optimizing before you know what works
- [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) — retrying without changing what the model sees

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- https://openai.com/index/harness-engineering/
