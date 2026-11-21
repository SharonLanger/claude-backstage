# Agent Loops, Stalls, or Never Finishes

## Scenario

Your agent enters infinite loops, gets stuck retrying the same action, runs indefinitely without converging on a result, or silently stalls without producing output. You need to diagnose whether the issue is architectural (missing stop conditions), environmental (tool timeouts), or prompt-related (unclear success criteria).

## Quick Answer

1. **Add explicit stop conditions** — Every loop needs a bounded iteration limit and a clear exit criterion. See [Stop Condition](../../families/I-reliability-recovery/patterns/stop-condition.md) and [Bounded Loop](../../families/A-workflow-topology/patterns/bounded-loop.md).
2. **Define deterministic checkpoints** — Use milestones to detect lack of progress and trigger escalation. See [Milestone Checkpoint](../../families/B-task-decomposition/patterns/B5-milestone-checkpoint.md).
3. **Instrument the loop** — You cannot fix what you cannot see. Add structured traces to identify where the agent stalls. See [Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md).

## Decision Guide

```
Agent not completing
│
├─ Is the agent looping (repeating actions)?
│   ├─ Same action, same result → Missing stop condition
│   │   → Apply: Stop Condition + Bounded Loop
│   ├─ Same action, different result → Non-determinism issue
│   │   → See: non-determinism.md
│   └─ Different actions, no progress → Unclear success criteria
│       → Apply: Deterministic Validator + Evaluator-Optimizer
│
├─ Is the agent stalled (no actions)?
│   ├─ Waiting for tool response → Tool timeout / hanging
│   │   → See: tool-failures.md
│   ├─ Context window exhausted → Cannot generate next token
│   │   → See: context-problems.md
│   └─ Ambiguous next step → Underspecified prompt
│       → Apply: Plan-Execute + Progressive Disclosure
│
└─ Is the agent running but never converging?
    ├─ Oscillating between states → Missing state machine
    │   → Apply: State Machine + Circuit Breaker
    ├─ Perfection-seeking refinement → No "good enough" threshold
    │   → Apply: Evaluator-Optimizer + Cost-Aware Stopping
    └─ Expanding scope each iteration → Unbounded decomposition
        → Apply: Fixed Decomposition + Budgeted Agent Loop
```

## Relevant Patterns

| Pattern | Family | Role in This Scenario |
|---------|--------|----------------------|
| [Stop Condition](../../families/I-reliability-recovery/patterns/stop-condition.md) | Reliability | Define when an agent should halt — timeouts, iteration caps, quality thresholds |
| [Bounded Loop](../../families/A-workflow-topology/patterns/bounded-loop.md) | Workflow | Enforce hard iteration limits on any repeating structure |
| [Circuit Breaker](../../families/I-reliability-recovery/patterns/circuit-breaker.md) | Reliability | Halt execution after repeated failures rather than retrying endlessly |
| [State Machine](../../families/L-memory-state/patterns/state-machine.md) | Memory/State | Prevent oscillation by making transitions explicit and irreversible where needed |
| [Milestone Checkpoint](../../families/B-task-decomposition/patterns/B5-milestone-checkpoint.md) | Decomposition | Break long tasks into verifiable milestones so stalls are detected early |
| [Cost-Aware Stopping](../../families/N-efficiency-routing/patterns/cost-aware-stopping.md) | Efficiency | Stop when marginal improvement no longer justifies cost |
| [Budgeted Agent Loop](../../families/N-efficiency-routing/patterns/budgeted-agent-loop.md) | Efficiency | Set token/time/cost budgets that force termination |
| [Evaluator-Optimizer](../../families/A-workflow-topology/patterns/evaluator-optimizer.md) | Workflow | Pair generation with evaluation to define convergence criteria |
| [Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md) | Observability | Emit structured events to pinpoint where the loop or stall occurs |
| [Plan-Execute](../../families/B-task-decomposition/patterns/B1-plan-execute.md) | Decomposition | Create an explicit plan upfront so the agent has a clear finish line |
| [Human Escalation](../../families/I-reliability-recovery/patterns/human-escalation.md) | Reliability | Escalate to a human when the agent cannot make progress |

## Anti-Patterns to Watch For

| Anti-Pattern | Why It Causes This Problem |
|--------------|---------------------------|
| [Infinite / Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md) | Setting max_iterations=100 when the task should complete in 5 is effectively unbounded. Bounds must be tight relative to expected completion. |
| [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) | Retrying the same prompt with the same context guarantees the same failure. Each retry must change something. |

## Diagnostic Checklist

- [ ] Does the agent loop have a hard iteration cap (not just a soft "try to stop" instruction)?
- [ ] Is there a time-based or cost-based budget that forces termination?
- [ ] Does the agent have a clear, machine-verifiable definition of "done"?
- [ ] Are you logging each iteration so you can see the repetition pattern?
- [ ] If the agent retries on failure, does each retry include new information (feedback, different approach)?
- [ ] Is the agent's context growing unboundedly across iterations?
- [ ] Does the orchestrator monitor for lack-of-progress (same state after N steps)?

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- https://web.stanford.edu/class/cs224g/lectures/Agentic_Design_Patterns.pdf
