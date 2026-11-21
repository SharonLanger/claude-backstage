# Detecting Regressions After Changes

## Scenario

You changed your agent's prompts, tools, model version, or orchestration logic and need to verify you didn't break something that was previously working. You want a systematic approach to regression detection — not just "run it again and see if it looks okay."

## Quick Answer

1. **Maintain a regression suite** of known input-output pairs that must always pass. See [D08 Regression Suite](../../families/D-verification-evaluation/patterns/D08-regression-suite.md).
2. **Diff behavior, not just outputs** — trace-level comparison catches regressions in intermediate steps that may not surface in final output yet. See [M01 Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md).
3. **Run evals before AND after** every change, compare scores, and flag degradation beyond a threshold.

## Checklist: Setting Up Regression Detection

- [ ] **Baseline established** — You have eval scores from before the change
- [ ] **Test cases cover known failure modes** — Each past bug has a corresponding test case
- [ ] **Deterministic checks run first** — Format/schema validation catches obvious breaks cheaply
- [ ] **Multi-dimensional scoring** — You track multiple metrics (correctness, latency, cost, format compliance) not just one
- [ ] **Threshold defined** — You know what "regression" means numerically (e.g., >5% drop in any metric)
- [ ] **Trace comparison available** — You can diff execution paths between runs, not just final output

## What Changes Cause Regressions

| Change Type | Common Regression | Detection Strategy |
|-------------|-------------------|-------------------|
| Prompt edit | Fixes one case, breaks another | Regression suite with diverse cases |
| Model version upgrade | Subtle behavioral shifts | A/B eval comparison on fixed test set |
| Tool schema change | Agent calls tools incorrectly | Tool-call validation + schema checks |
| Context window adjustment | Information loss | Assertion checks on output completeness |
| Temperature/sampling change | Non-deterministic output shifts | Statistical eval over N runs per case |
| Orchestration logic change | Step ordering or handoff breaks | Trace-level comparison |

## Practical Regression Workflow

```
1. Before change:
   Run eval suite → record baseline scores + traces

2. Make change

3. After change:
   Run same eval suite → record new scores + traces

4. Compare:
   - Any metric dropped > threshold? → REGRESSION
   - Any previously-passing case now fails? → REGRESSION
   - New trace diverges at unexpected step? → INVESTIGATE

5. If regression found:
   - Classify: is the old behavior actually correct? (sometimes the "regression" reveals the old output was wrong)
   - If real regression: revert or fix before shipping
   - Add the regression case to the permanent suite
```

## Relevant Patterns

| Pattern | Family | Role in Regression Detection |
|---------|--------|------------------------------|
| [Regression Suite](../../families/D-verification-evaluation/patterns/D08-regression-suite.md) | D | Core pattern — maintains known-good test cases |
| [Deterministic Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) | D | Catches format/schema breaks instantly |
| [Assertion-Based Validator](../../families/D-verification-evaluation/patterns/D02-assertion-based-validator.md) | D | Encodes invariants that must hold across versions |
| [Structured Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md) | M | Enables trace-level diffing between runs |
| [Replayable Run](../../families/M-observability-debugging/patterns/M07-replayable-run.md) | M | Allows re-running past inputs deterministically |
| [Trace-Linked Eval](../../families/M-observability-debugging/patterns/M08-trace-linked-eval.md) | M | Connects eval scores to specific execution paths |
| [Checkpoint State](../../families/L-memory-state/patterns/checkpoint-state.md) | L | Preserves intermediate state for comparison |
| [Bounded Loop](../../families/A-workflow-topology/patterns/bounded-loop.md) | A | Prevents infinite loops from new changes |

## Anti-Patterns to Watch For

- **"Run it 3 times and it seems fine"** — Without a structured regression suite, you're relying on luck. Non-deterministic outputs require statistical comparison, not spot-checking.
- **Testing only the case you just fixed** — The classic regression trap: you verify your fix works but don't check everything else still works.
- **Infinite/weakly-bounded loops after orchestration changes** — A change to loop logic can create unbounded execution. See [Infinite Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md).
- **Silent quality degradation** — Output looks valid (passes schema) but is subtly worse. Requires quality-sensitive evals, not just format checks. See [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md).

## Sources

- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://hamel.dev/blog/posts/evals-skills/
- https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html
- https://openai.com/index/harness-engineering/
