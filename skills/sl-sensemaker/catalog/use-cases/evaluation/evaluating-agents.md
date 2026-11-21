# How to Measure If an Agent System Is Working

## Scenario

You have deployed (or are about to deploy) an agent system and need to know whether it produces correct, reliable results. You want a practical evaluation strategy — what to measure, how to measure it, and which patterns support measurability.

## Quick Answer

1. **Start with deterministic validators** on every output before measuring anything fuzzy — wrong format or violated constraints is a clear "not working" signal. See [D01 Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md).
2. **Build evals from real failures**, not imagined ones — production errors are your best eval source. See [evals-from-errors.md](./evals-from-errors.md).
3. **Instrument everything** so you can trace failures back to their origin step. See [M01 Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md).

## Decision Guide: What to Evaluate

| Question | If Yes | If No |
|----------|--------|-------|
| Can you define a correct answer for most inputs? | Use deterministic evals (exact match, schema validation, assertion-based) | Use LLM-as-judge or human eval on a sample |
| Is the task multi-step? | Evaluate intermediate steps, not just final output | End-to-end output eval is sufficient |
| Do failures have high cost? | Add maker-checker patterns + human spot-checks | Automated evals with periodic human review |
| Is the system already in production? | Prioritize error-driven evals from real logs | Use synthetic benchmarks + adversarial inputs |

## Evaluation Layers (from cheapest to most expensive)

1. **Schema & format validation** — Does the output parse? Does it match the expected type?
   - Pattern: [D01 Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md)
   - Pattern: [Schema Validation (output)](../../families/O-output-integration/patterns/schema-validation.md)

2. **Programmatic correctness checks** — Does the output satisfy known invariants?
   - Pattern: [D01 Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md)
   - Pattern: [Programmatic Postcondition](../../families/O-output-integration/patterns/programmatic-postcondition.md)

3. **Behavioral benchmarks** — Given known inputs, does the system produce known-good outputs?
   - Guide: [Practical Regression Workflow](./regression-testing.md#practical-regression-workflow)

4. **LLM-as-judge** — For subjective quality where no ground truth exists
   - Pattern: [D09 LLM-as-Judge](../../families/D-verification-evaluation/patterns/D09-llm-as-judge.md)
   - Caution: calibrate judges against human labels; uncalibrated judges are unreliable

5. **Human evaluation** — Gold standard for ambiguous tasks; expensive but necessary for calibration
   - Pattern: [D08 Multi-Evaluator Consensus](../../families/D-verification-evaluation/patterns/D08-multi-review-ensemble.md)

## Relevant Patterns

| Pattern | Family | Role in Evaluation |
|---------|--------|-------------------|
| [D01 Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) | D | Start with low-cost pass/fail checks for schemas and known invariants |
| [Practical Regression Workflow](./regression-testing.md#practical-regression-workflow) | — | Catch previously passing cases that now fail |
| [LLM-as-Judge](../../families/D-verification-evaluation/patterns/D09-llm-as-judge.md) | D | Evaluates subjective quality at scale |
| [Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md) | M | Makes failures diagnosable |
| [Trace-Linked Eval](../../families/M-observability-debugging/patterns/M08-trace-linked-eval.md) | M | Connects eval results to execution traces |
| [Failure Categorization](../../families/M-observability-debugging/patterns/M09-failure-categorization.md) | M | Classifies errors for targeted improvement |
| [Step-Level Diagnostic](../../families/D-verification-evaluation/patterns/D12-step-level-diagnostic.md) | D | Evaluates intermediate steps, not just final output |

## Anti-Patterns to Watch For

- **Evaluating only the final output of multi-step agents** — You lose the ability to identify which step failed. Use step-level diagnostics.
- **Using uncalibrated LLM judges** — An LLM judge that hasn't been validated against human labels can systematically miss failure modes.
- **Premature optimization of eval metrics** — Optimizing for a proxy metric (e.g., "LLM judge says 4/5") without validating the proxy correlates with real quality. See [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md).
- **No eval at all** — "It seems to work" is not evaluation. Even 20 hand-picked test cases is better than nothing.

## Sources

- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://hamel.dev/blog/posts/evals-skills/
- https://hamel.dev/blog/posts/evals-faq/
- https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html
