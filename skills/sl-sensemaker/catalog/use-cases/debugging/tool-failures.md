# Tool Calls Failing, Misused, or Producing Errors

## Practitioner routes

- [Verify an unfamiliar API](../../families/D-verification-evaluation/guides/verify-unfamiliar-api.md)

## Scenario

Your agent's tool calls are failing (errors, timeouts, permission denied), the agent is calling tools incorrectly (wrong parameters, wrong tool for the task), or tool results are unexpected. The agent may be retrying fruitlessly, hallucinating tool names, or misinterpreting tool outputs.

## Quick Answer

1. **Enforce tool schemas strictly** — Tools must have typed, constrained parameters so the agent cannot pass malformed input. See [Typed Schema-Constrained Tool](../../families/G-tool-action-design/patterns/G01-typed-schema-constrained-tool.md).
2. **Make tools idempotent and observable** — Retrying a failed tool call should be safe, and every call should be logged. See [Idempotent Action Wrapper](../../families/G-tool-action-design/patterns/G10-idempotent-action-wrapper.md) and [Tool Call Event Log](../../families/M-observability-debugging/patterns/M02-tool-call-event-log.md).
3. **Provide feedback on failure** — When a tool fails, the agent needs structured error information to adapt its approach. See [Retry with Feedback](../../families/I-reliability-recovery/patterns/retry-with-feedback.md) and [Structured Error Classification](../../families/I-reliability-recovery/patterns/structured-error-classification.md).

## Decision Guide

```
Tool failure observed
│
├─ Tool call returns an error
│   ├─ Permission / auth error → Privilege configuration wrong
│   │   → Apply: Least Privilege (audit scope) + Structured Error Classification
│   ├─ Timeout → Tool too slow or hanging
│   │   → Apply: Circuit Breaker + Bounded Retry
│   ├─ Rate limit → Too many calls too fast
│   │   → Apply: Tool Result Reuse + Caching
│   └─ Invalid input error → Agent passed wrong parameters
│       → Apply: Typed Schema-Constrained Tool + Parse and Reject
│
├─ Agent calls wrong tool or invents tools
│   ├─ Hallucinated tool name → Too many tools or poor descriptions
│   │   → Apply: Context Minimization (reduce tool count) + Role-Scoped Context
│   ├─ Right intent, wrong tool → Tool descriptions ambiguous
│   │   → Apply: Typed Schema-Constrained Tool (improve descriptions)
│   └─ Uses tool for unintended purpose → Tool boundary unclear
│       → Apply: Read-Write Separation + Deterministic Override
│
├─ Tool succeeds but agent misinterprets result
│   ├─ Ignores error in result body → No structured error format
│   │   → Apply: Structured Error Classification + Typed Result Object
│   ├─ Treats partial result as complete → No pagination/continuation signal
│   │   → Apply: Typed Schema-Constrained Tool (result schema)
│   └─ Hallucinates data not in result → Context confusion
│       → See: context-problems.md
│
└─ Agent retries the same failed call
    ├─ Same parameters each time → No feedback loop
    │   → Apply: Retry with Feedback + Root Cause Before Retry
    ├─ Infinite retries → No retry bound
    │   → Apply: Bounded Retry + Circuit Breaker
    └─ Changes parameters randomly → No error analysis
        → Apply: Structured Error Classification + Fresh Context Retry
```

## Relevant Patterns

| Pattern | Family | Role in This Scenario |
|---------|--------|----------------------|
| [Typed Schema-Constrained Tool](../../families/G-tool-action-design/patterns/G01-typed-schema-constrained-tool.md) | Tool Design | Enforce parameter types and constraints so invalid calls are rejected before execution |
| [Idempotent Action Wrapper](../../families/G-tool-action-design/patterns/G10-idempotent-action-wrapper.md) | Tool Design | Make retries safe by ensuring repeated calls produce the same result |
| [Tool Call Event Log](../../families/M-observability-debugging/patterns/M02-tool-call-event-log.md) | Observability | Log every tool call with inputs, outputs, and timing for debugging |
| [Bounded Retry](../../families/I-reliability-recovery/patterns/bounded-retry.md) | Reliability | Limit retry attempts with exponential backoff |
| [Circuit Breaker](../../families/I-reliability-recovery/patterns/circuit-breaker.md) | Reliability | Stop calling a failing tool after N failures |
| [Retry with Feedback](../../families/I-reliability-recovery/patterns/retry-with-feedback.md) | Reliability | Include the error message in the next attempt so the agent can adapt |
| [Root Cause Before Retry](../../families/I-reliability-recovery/patterns/root-cause-before-retry.md) | Reliability | Diagnose why the tool failed before retrying |
| [Structured Error Classification](../../families/I-reliability-recovery/patterns/structured-error-classification.md) | Reliability | Categorize errors (transient vs permanent) to choose the right recovery strategy |
| [Fresh Context Retry](../../families/I-reliability-recovery/patterns/fresh-context-retry.md) | Reliability | When the agent's context is poisoned by failures, restart with clean state |
| [Tool Result Reuse](../../families/N-efficiency-routing/patterns/tool-result-reuse.md) | Efficiency | Cache tool results to avoid redundant calls and rate limits |
| [Caching](../../families/N-efficiency-routing/patterns/caching.md) | Efficiency | Cache expensive or slow tool responses |
| [Least Privilege](../../families/J-security-trust/patterns/J01-least-privilege.md) | Security | Ensure tools have exactly the permissions needed — no more, no less |
| [Read-Write Separation](../../families/J-security-trust/patterns/J11-read-write-separation.md) | Security | Separate read tools from write tools to limit blast radius |
| [Human Escalation](../../families/I-reliability-recovery/patterns/human-escalation.md) | Reliability | When tools are permanently failing, escalate to a human |

## Anti-Patterns to Watch For

| Anti-Pattern | Why It Causes This Problem |
|--------------|---------------------------|
| [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) | Calling the same tool with the same parameters after a failure guarantees the same failure. The agent must change something — parameters, approach, or tool choice. |
| [Infinite / Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md) | High retry limits on tool calls (e.g., retry 50 times) waste tokens and time when the failure is permanent. |

## Diagnostic Checklist

- [ ] Are tool schemas well-documented with parameter descriptions and constraints?
- [ ] Does the agent receive the actual error message when a tool fails (not just "tool failed")?
- [ ] Are retries bounded (max 2-3 for transient errors, 0 for permanent errors)?
- [ ] Is each tool call logged with full request/response for post-hoc debugging?
- [ ] Are tools idempotent (safe to retry)?
- [ ] Does the agent have too many tools available (>15-20 causes selection confusion)?
- [ ] Is there a distinction between transient errors (retry) and permanent errors (stop or escalate)?
- [ ] Are tool results cached where appropriate to avoid redundant calls?
- [ ] Does the tool response schema clearly indicate success vs failure?
- [ ] Are permissions/auth tokens valid and not expired?

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
