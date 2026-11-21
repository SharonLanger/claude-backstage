# Flaky Behavior, Inconsistent Results Across Runs

## Scenario

Your agent produces different outputs for the same input, passes evals intermittently, behaves differently in production versus development, or exhibits "works on my machine" syndrome. You need to identify whether the non-determinism is inherent (LLM sampling), environmental (different context), or systemic (race conditions, ordering effects).

## Quick Answer

1. **Separate deterministic from non-deterministic components** — Push decisions with known-correct answers into deterministic code paths. See [Deterministic Override](../../families/H-deterministic-control/patterns/H01-deterministic-override.md) and [Non-AI Fallback Path](../../families/H-deterministic-control/patterns/H08-non-ai-fallback-path.md).
2. **Make runs replayable** — Log enough state to reproduce any run exactly. See [Replayable Run](../../families/M-observability-debugging/patterns/M07-replayable-run.md).
3. **Design evals that account for variance** — Use deterministic assertions where possible; use statistical methods for inherently variable outputs. See [Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md).

## Decision Guide

```
Non-deterministic behavior observed
│
├─ Same input, different output (single agent)
│   ├─ Output format varies → No schema enforcement
│   │   → Apply: Schema Validation + Structured Output Boundary
│   ├─ Content varies but all acceptable → Normal LLM variance
│   │   → Accept if eval passes; add Deterministic Validator for critical fields
│   ├─ Content varies and sometimes wrong → Quality variance
│   │   → Apply: Parallel Voting + Generator-Critic
│   └─ Only varies in production → Different context/tools in prod
│       → Apply: Replayable Run + Structured Trace (compare environments)
│
├─ Same input, different execution path
│   ├─ Tool call order varies → No fixed execution plan
│   │   → Apply: Sequential Workflow or Fixed Decomposition
│   ├─ Different tools selected → Routing instability
│   │   → Apply: Deterministic Override + Confidence-Based Routing
│   └─ Sometimes skips steps → Unreliable instruction following
│       → Apply: State Machine + Milestone Checkpoint
│
├─ Multi-agent: different agents give conflicting results
│   ├─ Race condition → Ordering dependency
│   │   → Apply: Session Isolation + State Machine
│   ├─ Different context per agent → Context inconsistency
│   │   → Apply: Shared Memory Gateway + Artifact-Based Handoff
│   └─ Legitimate disagreement → No consensus mechanism
│       → Apply: Parallel Voting + Synthesizer-Aggregator
│
└─ Evals pass intermittently
    ├─ Flaky by small margins → Eval threshold too tight for LLM variance
    │   → Widen threshold or use statistical pass criteria
    ├─ Flaky on specific cases → Edge cases triggering different paths
    │   → Apply: Step-Level Diagnostic + Trace-Linked Eval
    └─ Flaky on timing → External dependencies non-deterministic
        → Apply: Idempotent Action Wrapper + Tool Result Reuse (mock in eval)
```

## Relevant Patterns

| Pattern | Family | Role in This Scenario |
|---------|--------|----------------------|
| [Deterministic Override](../../families/H-deterministic-control/patterns/H01-deterministic-override.md) | Control | Remove LLM from decisions that have deterministic correct answers |
| [Non-AI Fallback Path](../../families/H-deterministic-control/patterns/H08-non-ai-fallback-path.md) | Control | Use rule-based logic for components where consistency matters more than flexibility |
| [Replayable Run](../../families/M-observability-debugging/patterns/M07-replayable-run.md) | Observability | Capture all inputs and state so any run can be reproduced exactly |
| [Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md) | Observability | Compare traces between "good" and "bad" runs to find divergence points |
| [Parallel Voting](../../families/A-workflow-topology/patterns/parallel-voting.md) | Workflow | Run multiple instances and take majority/consensus to reduce variance |
| [Sequential Workflow](../../families/A-workflow-topology/patterns/sequential-workflow.md) | Workflow | Force a fixed execution order to eliminate path variance |
| [State Machine](../../families/L-memory-state/patterns/state-machine.md) | Memory/State | Make execution states explicit so the agent cannot skip or reorder steps |
| [Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) | Verification | Check outputs with deterministic rules regardless of how they were generated |
| [Schema Validation](../../families/O-output-integration/patterns/schema-validation.md) | Output | Eliminate format variance by enforcing schema on outputs |
| [Structured Output Boundary](../../families/O-output-integration/patterns/structured-output-boundary.md) | Output | Clean boundary between LLM output and system consumption |
| [Confidence-Based Routing](../../families/N-efficiency-routing/patterns/confidence-based-routing.md) | Efficiency | Route based on confidence scores to reduce unstable routing decisions |
| [Generator-Critic](../../families/A-workflow-topology/patterns/generator-critic.md) | Workflow | Add a critic pass to catch quality variance before output |
| [Session Isolation](../../families/L-memory-state/patterns/session-isolation.md) | Memory/State | Prevent state from one run bleeding into another |
| [Synthesizer-Aggregator](../../families/C-orchestration/patterns/synthesizer-aggregator.md) | Orchestration | Combine multiple agent outputs into a stable consensus |
| [Fixed Decomposition](../../families/B-task-decomposition/patterns/B4-fixed-decomposition.md) | Decomposition | Use a predetermined task breakdown to eliminate planning variance |
| [Step-Level Diagnostic](../../families/D-verification-evaluation/patterns/D12-step-level-diagnostic.md) | Verification | Identify which specific step introduces the variance |
| [Trace-Linked Eval](../../families/M-observability-debugging/patterns/M08-trace-linked-eval.md) | Observability | Link eval results to execution traces to debug flaky cases |
| [Tool Result Reuse](../../families/N-efficiency-routing/patterns/tool-result-reuse.md) | Efficiency | Cache tool results to eliminate external non-determinism in evals |
| [Shared Memory Gateway](../../families/L-memory-state/patterns/shared-memory-gateway.md) | Memory/State | Ensure all agents see the same state to prevent conflicts |

## Anti-Patterns to Watch For

| Anti-Pattern | Why It Causes This Problem |
|--------------|---------------------------|
| [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) | Routing to different models per run without eval coverage means different quality levels manifest as flakiness. |
| [Multi-Agent by Default](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md) | More agents = more variance. Each LLM call is a source of non-determinism; unnecessary agents multiply the problem. |

## Diagnostic Checklist

- [ ] Is the non-determinism in the output format, content, or execution path?
- [ ] Are you using temperature > 0? (Temperature 0 reduces but doesn't eliminate variance)
- [ ] Can you replay a failing run with the exact same inputs and context?
- [ ] Are external tools/APIs returning different results between runs?
- [ ] Is the context window content identical between runs? (Different retrieval = different output)
- [ ] Are you comparing traces between "good" and "bad" runs to find the divergence point?
- [ ] For flaky evals: is the eval criterion binary when it should be statistical?
- [ ] Are multiple agents racing or sharing state without synchronization?
- [ ] Could prompt ordering effects (position of examples, instructions) explain the variance?
- [ ] Have you identified which component is the variance source (LLM, tools, context, routing)?

## Sources

- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://hamel.dev/blog/posts/evals-faq/
- https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html
- https://web.stanford.edu/class/cs224g/lectures/Agentic_Design_Patterns.pdf
