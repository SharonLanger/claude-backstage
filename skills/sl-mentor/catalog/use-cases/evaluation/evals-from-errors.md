# Building Evals from Production Failures

## Scenario

Your agent failed in production — wrong output, tool call error, infinite loop, or user complaint. You want to turn that specific failure into a permanent eval so the same class of bug never ships again. This is not about building evals generically; it's about the concrete workflow of going from "this broke" to "this is now tested."

## Quick Answer

1. **Capture the full trace** of the failed execution — inputs, intermediate steps, tool calls, and final output. See [M01 Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md).
2. **Classify the failure** before writing the eval — is it a format error, correctness error, safety violation, or performance issue? Different failure types need different eval approaches. See [M09 Failure Categorization](../../families/M-observability-debugging/patterns/M09-failure-categorization.md).
3. **Write the minimal reproduction** as a test case and add it to your regression suite. See [Practical Regression Workflow](./regression-testing.md#practical-regression-workflow) for comparing runs and adding confirmed failures.

## The Error-to-Eval Pipeline

```
Production failure occurs
        │
        ▼
┌─────────────────────┐
│ 1. Capture evidence │ ← Full trace, input, output, context
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 2. Classify failure │ ← What category? What went wrong?
└─────────┬───────────┘
          │
          ▼
┌─────────────────────────┐
│ 3. Identify root step   │ ← Which step in the trace actually failed?
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────────┐
│ 4. Write minimal repro case │ ← Strip to smallest input that triggers the bug
└─────────┬───────────────────┘
          │
          ▼
┌──────────────────────────────┐
│ 5. Define expected behavior  │ ← What SHOULD the output/behavior be?
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│ 6. Choose eval type          │ ← Deterministic assert? LLM judge? Human label?
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────┐
│ 7. Add to regression suite   │ ← Permanent, runs on every change
└──────────────────────────────┘
```

## Failure Type → Eval Type Mapping

| Failure Category | Example | Eval Approach | Pattern |
|-----------------|---------|---------------|---------|
| Format/schema violation | JSON output has wrong field names | Deterministic schema validator | [D01](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) |
| Factual incorrectness | Agent stated wrong API endpoint | Assertion against known-good answer | [D01 Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) |
| Tool misuse | Called delete instead of update | Tool-call sequence assertion | [M02](../../families/M-observability-debugging/patterns/M02-tool-call-event-log.md) |
| Infinite/excessive looping | Retried 47 times without progress | Loop count assertion + cost check | [Bounded Loop](../../families/A-workflow-topology/patterns/bounded-loop.md) |
| Safety/security violation | Leaked PII in output | Pattern-match + sanitization check | [Sanitized Output Boundary](../../families/O-output-integration/patterns/sanitized-output-boundary.md) |
| Subtle quality regression | Answer technically correct but unhelpful | LLM-as-judge with rubric | [D09](../../families/D-verification-evaluation/patterns/D09-llm-as-judge.md) |
| Wrong routing/delegation | Sent math question to writing specialist | Routing decision assertion | [Routing](../../families/A-workflow-topology/patterns/routing.md) |

## Practical Steps: From Error Log to Eval Case

### Step 1: Capture evidence

Minimum data to save from a production failure:
- The exact user input / trigger
- The full agent trace (every LLM call, tool call, intermediate output)
- The final output that was wrong
- Any error messages or exceptions
- The model version and configuration at time of failure

### Step 2: Find the root step

Use the trace to identify WHERE things went wrong — not just THAT they went wrong. In a 5-step chain, the error might originate at step 2 but only become visible at step 5. Write your eval at the root cause level.

### Step 3: Write the eval case

A good eval case from a production failure has:
- **Input**: The minimal input that triggers the bug (strip irrelevant context)
- **Expected behavior**: What the correct output/action is (not just "not this wrong thing")
- **Assertion**: A check that passes for correct behavior and fails for the specific bug
- **Metadata**: Link to the original incident, failure category, date added

### Step 4: Generalize (optional but high-value)

After writing the specific case, ask: "What class of input would trigger similar failures?" Generate 2-3 variations that test the same vulnerability with different specifics.

## Relevant Patterns

| Pattern | Family | Role in Error-to-Eval |
|---------|--------|----------------------|
| [Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md) | M | Captures the raw evidence |
| [Failure Categorization](../../families/M-observability-debugging/patterns/M09-failure-categorization.md) | M | Classifies the error type |
| [Step-Level Diagnostic](../../families/D-verification-evaluation/patterns/D12-step-level-diagnostic.md) | D | Pinpoints which step failed |
| [Practical Regression Workflow](./regression-testing.md#practical-regression-workflow) | — | Add the repro to the permanent regression suite |
| [Replayable Run](../../families/M-observability-debugging/patterns/M07-replayable-run.md) | M | Allows re-running the exact failure scenario |
| [Tool Call Event Log](../../families/M-observability-debugging/patterns/M02-tool-call-event-log.md) | M | Captures tool-call-level detail for tool misuse bugs |
| [Artifact Lineage](../../families/M-observability-debugging/patterns/M05-artifact-lineage.md) | M | Tracks how outputs were derived (provenance) |

## Anti-Patterns to Watch For

- **Writing evals for the symptom, not the cause** — If the root cause is bad routing at step 2, writing an eval that only checks the final output may not catch the same bug in a different form.
- **Retry without new information** — If your "fix" is just to retry and hope for different output, you haven't actually fixed the failure class. See [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md).
- **Over-fitting evals to one exact input** — Your eval should catch the *class* of failure, not just the one specific input. Generalize slightly.
- **Never reviewing old evals** — Evals accumulate. Periodically review whether old evals are still testing relevant behavior or just adding noise.

## Sources

- https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html
- https://hamel.dev/blog/posts/evals-skills/
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html
