# Agent Produces Incorrect or Unexpected Results

## Scenario

Your agent completes its task but the output is wrong — incorrect facts, malformed data, missed requirements, hallucinated content, or results that don't match what was asked for. The agent doesn't loop or crash; it confidently produces the wrong answer.

## Quick Answer

1. **Add verification layers** — Never trust a single generation pass. Use deterministic validators or a separate evaluator to check outputs before they reach the user. See [Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) and [Maker-Checker](../../families/C-orchestration/patterns/maker-checker.md).
2. **Constrain the output format** — Wrong outputs often stem from ambiguous output expectations. Use schemas and typed results. See [Schema Validation](../../families/O-output-integration/patterns/schema-validation.md) and [Typed Result Object](../../families/O-output-integration/patterns/typed-result-object.md).
3. **Evaluate systematically** — Build evals that catch regressions. Wrong outputs are a signal to add a test case. See [Trace-Linked Eval](../../families/M-observability-debugging/patterns/M08-trace-linked-eval.md).

## Decision Guide

```
Wrong output produced
│
├─ Is the format wrong (structure, schema, types)?
│   ├─ Missing fields or wrong types → No schema enforcement
│   │   → Apply: Schema Validation + Typed Result Object
│   ├─ Extra content or preamble → No output boundary
│   │   → Apply: Structured Output Boundary + Parse and Reject
│   └─ Partially correct structure → Ambiguous format spec
│       → Apply: Typed Schema-Constrained Tool
│
├─ Is the content wrong (facts, logic, reasoning)?
│   ├─ Hallucinated information → Missing grounding
│   │   → Apply: Just-in-Time Retrieval + Deterministic Validator
│   ├─ Missed requirements → Context not provided or lost
│   │   → See: context-problems.md
│   ├─ Wrong reasoning steps → No intermediate verification
│   │   → Apply: Generator-Critic + Step-Level Diagnostic
│   └─ Correct reasoning, wrong conclusion → Accumulation error
│       → Apply: Iterative Refinement + Checkpoint State
│
├─ Is the output inconsistent with instructions?
│   ├─ Ignoring constraints → Prompt not effective
│   │   → Apply: Role-Scoped Context + Deterministic Override
│   ├─ Doing something not asked → Scope creep in generation
│   │   → Apply: Fixed Decomposition + Programmatic Postcondition
│   └─ Partial compliance → Underspecified success criteria
│       → Apply: Deterministic Validator + Evaluator-Optimizer
│
└─ Is the output dangerous or harmful?
    ├─ Injected content from input → Prompt injection
    │   → Apply: Sanitized Output Boundary + Context Isolation
    └─ Executing unintended actions → Missing guardrails
        → Apply: Least Privilege + Human-in-the-Loop Checkpoint
```

## Relevant Patterns

| Pattern | Family | Role in This Scenario |
|---------|--------|----------------------|
| [Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) | Verification | Check outputs against deterministic rules (regex, schema, business logic) |
| [Maker-Checker](../../families/C-orchestration/patterns/maker-checker.md) | Orchestration | Use a separate agent/model to verify the first agent's output |
| [Generator-Critic](../../families/A-workflow-topology/patterns/generator-critic.md) | Workflow | Pair generation with criticism to catch errors before output |
| [Schema Validation](../../families/O-output-integration/patterns/schema-validation.md) | Output | Enforce structural correctness via JSON Schema or similar |
| [Typed Result Object](../../families/O-output-integration/patterns/typed-result-object.md) | Output | Return well-typed objects instead of freeform text |
| [Parse and Reject](../../families/O-output-integration/patterns/parse-and-reject.md) | Output | Reject malformed outputs and re-request with feedback |
| [Structured Output Boundary](../../families/O-output-integration/patterns/structured-output-boundary.md) | Output | Cleanly separate agent reasoning from user-facing output |
| [Programmatic Postcondition](../../families/O-output-integration/patterns/programmatic-postcondition.md) | Output | Run deterministic checks on the final result |
| [Evaluator-Optimizer](../../families/A-workflow-topology/patterns/evaluator-optimizer.md) | Workflow | Iteratively improve output quality with evaluation feedback |
| [Step-Level Diagnostic](../../families/D-verification-evaluation/patterns/D12-step-level-diagnostic.md) | Verification | Identify which specific step introduced the error |
| [Just-in-Time Retrieval](../../families/E-context-engineering/patterns/just-in-time-retrieval.md) | Context | Ground the agent in real data at decision time, not upfront |
| [Deterministic Override](../../families/H-deterministic-control/patterns/H01-deterministic-override.md) | Control | For known-correct answers, bypass the LLM entirely |
| [Trace-Linked Eval](../../families/M-observability-debugging/patterns/M08-trace-linked-eval.md) | Observability | Connect wrong outputs back to the trace that produced them for debugging |

## Anti-Patterns to Watch For

| Anti-Pattern | Why It Causes This Problem |
|--------------|---------------------------|
| [Multi-Agent by Default](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md) | Adding more agents without clear verification roles creates more points of failure, not fewer. A single agent with good validation often beats an unverified multi-agent chain. |
| [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) | Routing to cheaper/faster models without eval coverage means you only discover wrong outputs in production. |

## Diagnostic Checklist

- [ ] Can you reproduce the wrong output with the same input? (If not, see non-determinism.md)
- [ ] Is the output format enforced by schema validation or just by prompt instructions?
- [ ] Does the agent have access to the ground truth it needs (retrieved docs, tool results)?
- [ ] Is there a second pass (critic, validator, checker) that verifies correctness?
- [ ] Are you evaluating against specific test cases, or only checking ad hoc?
- [ ] Does the prompt clearly define what "correct" looks like (examples, constraints)?
- [ ] Is the wrong output a pattern (same category of mistake) or random?
- [ ] Could the error come from a tool returning wrong data (garbage in, garbage out)?

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://hamel.dev/blog/posts/evals-skills/
- https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
