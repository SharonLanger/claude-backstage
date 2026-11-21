# Key Architecture Forks and Tradeoffs

## Scenario

You're designing an agent system and face fundamental architecture decisions: single vs. multi-agent, autonomous vs. supervised, simple chain vs. dynamic planning. This guide maps the key decision points, what each choice trades off, and which patterns support each path.

## Quick Answer

1. **Start with the simplest topology that could work** — single agent, prompt chain, no dynamic planning. Add complexity only when you hit a wall. See [Prompt Chaining](../../families/A-workflow-topology/patterns/prompt-chaining.md).
2. **The biggest fork is autonomy level** — how much does the agent decide vs. follow a fixed path? This determines your entire reliability and safety posture.
3. **Multi-agent adds coordination overhead** — only use it when single-agent genuinely cannot handle the breadth. See [Multi-Agent by Default](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md) anti-pattern.

## Architecture Decision Points

### Fork 1: Fixed Workflow vs. Dynamic Planning

| | Fixed Workflow | Dynamic Planning |
|---|---|---|
| **What it means** | Steps are predetermined at design time | Agent decides what steps to take at runtime |
| **Patterns** | [Prompt Chaining](../../families/A-workflow-topology/patterns/prompt-chaining.md), [Sequential Workflow](../../families/A-workflow-topology/patterns/sequential-workflow.md), [Fixed Decomposition](../../families/B-task-decomposition/patterns/B4-fixed-decomposition.md) | [Plan-Execute](../../families/B-task-decomposition/patterns/B1-plan-execute.md), [Dynamic Decomposition](../../families/B-task-decomposition/patterns/B3-dynamic-decomposition.md), [ReAct](../../families/A-workflow-topology/patterns/react.md) |
| **Pro** | Predictable, debuggable, cheap | Handles novel tasks, adapts to input |
| **Con** | Brittle to unexpected inputs | Harder to debug, higher cost, can go off-track |
| **Choose when** | Task structure is known; reliability > flexibility | Task varies significantly across inputs |
| **Safety patterns needed** | Minimal — [Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) at outputs | Heavy — [Bounded Loop](../../families/A-workflow-topology/patterns/bounded-loop.md), [Stop Condition](../../families/I-reliability-recovery/patterns/stop-condition.md), [Human Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) |

### Fork 2: Single Agent vs. Multi-Agent

| | Single Agent | Multi-Agent |
|---|---|---|
| **What it means** | One LLM handles everything (possibly with tools) | Multiple specialized LLMs coordinate |
| **Patterns** | [Prompt Chaining](../../families/A-workflow-topology/patterns/prompt-chaining.md), [Bounded Loop](../../families/A-workflow-topology/patterns/bounded-loop.md) | [Coordinator-Specialists](../../families/C-orchestration/patterns/coordinator-specialists.md), [Orchestrator-Workers](../../families/C-orchestration/patterns/orchestrator-workers.md), [Decentralized Handoff](../../families/C-orchestration/patterns/decentralized-handoff.md) |
| **Pro** | Simple, no coordination overhead, full context | Separation of concerns, specialized prompts, parallelism |
| **Con** | Context window limits, single point of failure | Coordination complexity, context loss at handoffs, harder to debug |
| **Choose when** | Task fits in one context window; domain is cohesive | Genuinely distinct specializations; context would overflow |
| **Required supporting patterns** | [Context Engineering](../../families/E-context-engineering/) for window management | [Context Isolation](../../families/E-context-engineering/patterns/context-isolation.md), [Minimal Context Handoff](../../families/E-context-engineering/patterns/minimal-context-handoff.md), [Instrumented Handoff](../../families/M-observability-debugging/patterns/M04-instrumented-handoff.md) |

### Fork 3: Autonomous vs. Human-in-the-Loop

| | High Autonomy | Human-in-the-Loop |
|---|---|---|
| **What it means** | Agent acts without human approval | Humans approve key decisions |
| **Patterns** | [Bounded Loop](../../families/A-workflow-topology/patterns/bounded-loop.md) + [Stop Condition](../../families/I-reliability-recovery/patterns/stop-condition.md) | [Human-in-the-Loop Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md), [Escalation](../../families/I-reliability-recovery/patterns/human-escalation.md) |
| **Pro** | Fast, scales without human bottleneck | Safe, catches errors before they propagate |
| **Con** | Risk of cascading errors; security surface | Slow, doesn't scale, human becomes bottleneck |
| **Choose when** | Actions are reversible AND low-cost AND well-validated | Actions are irreversible OR high-cost OR novel |
| **Safety patterns needed** | [Least Privilege](../../families/J-security-trust/patterns/J01-least-privilege.md), [Circuit Breaker](../../families/I-reliability-recovery/patterns/circuit-breaker.md), [Maker-Checker](../../families/C-orchestration/patterns/maker-checker.md) | [Approval Levels](../../families/K-human-control/patterns/K02-tiered-approval-levels.md), [Read-Write Separation](../../families/J-security-trust/patterns/J11-read-write-separation.md) |

### Fork 4: Deterministic Steps vs. AI-Decided Everything

| | Deterministic Where Possible | AI-Decided Everything |
|---|---|---|
| **What it means** | Use code/rules for what you can; LLM only for what requires judgment | LLM makes all decisions including routine ones |
| **Patterns** | [Deterministic Override](../../families/H-deterministic-control/patterns/H01-deterministic-override.md), [Non-AI Fallback](../../families/H-deterministic-control/patterns/H08-non-ai-fallback-path.md) | [ReAct](../../families/A-workflow-topology/patterns/react.md), [Dynamic Decomposition](../../families/B-task-decomposition/patterns/B3-dynamic-decomposition.md) |
| **Pro** | Reliable for known cases, cheaper, faster, auditable | Maximum flexibility, handles edge cases |
| **Con** | Brittle if rules don't cover the case | Expensive, non-deterministic, harder to guarantee |
| **Choose when** | You can enumerate the rules; correctness > flexibility | Rules are too complex to enumerate; flexibility > cost |

### Fork 5: Eager Execution vs. Reconnaissance-First

| | Eager Execution | Reconnaissance-First |
|---|---|---|
| **What it means** | Start executing immediately | Gather information before acting |
| **Patterns** | [Sequential Workflow](../../families/A-workflow-topology/patterns/sequential-workflow.md) | [Reconnaissance-First](../../families/B-task-decomposition/patterns/B6-reconnaissance-first.md), [Plan-Execute](../../families/B-task-decomposition/patterns/B1-plan-execute.md) |
| **Pro** | Fast for straightforward tasks | Avoids expensive mistakes; better plans |
| **Con** | May go wrong direction with insufficient info | Slower; reconnaissance itself costs tokens |
| **Choose when** | Task is well-understood; quick feedback loops exist | Task is ambiguous; mistakes are expensive to undo |

## Decision Flowchart

```
START: What are you building?
│
├─ "A pipeline that processes documents the same way every time"
│   → Fixed workflow (Fork 1: Fixed)
│   → Single agent (Fork 2: Single)
│   → High autonomy OK (Fork 3: Autonomous)
│   → Maximum determinism (Fork 4: Deterministic)
│
├─ "A coding assistant that handles varied requests"
│   → Dynamic planning (Fork 1: Dynamic)
│   → Single agent with tools (Fork 2: Single)
│   → Human approves destructive actions (Fork 3: Mixed)
│   → AI decides approach, deterministic validation (Fork 4: Hybrid)
│
├─ "A customer service system with routing"
│   → Routing + fixed sub-workflows (Fork 1: Hybrid)
│   → Multi-agent by specialization (Fork 2: Multi)
│   → Escalation to human for edge cases (Fork 3: HITL)
│   → Deterministic routing, AI for responses (Fork 4: Hybrid)
│
└─ "A research agent that explores open-ended questions"
    → Dynamic planning (Fork 1: Dynamic)
    → Possibly multi-agent for parallelism (Fork 2: Depends on scale)
    → Human reviews conclusions (Fork 3: HITL)
    → Reconnaissance-first (Fork 5: Recon)
```

## Anti-Patterns to Watch For

- **Multi-Agent by Default** — Reaching for multiple agents before proving a single agent can't handle it. The coordination overhead is real. See [Multi-Agent by Default](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md).
- **Premature Optimization** — Routing to cheaper models before you've established quality baselines on the capable model. See [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md).
- **Infinite Weakly-Bounded Loop** — Choosing dynamic planning without adequate stop conditions. See [Infinite Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md).

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
