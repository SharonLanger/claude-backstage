# Guide: Debugging Runbook — "My Agent Failed, Now What?"

## Purpose

Use this runbook when an agent produces a wrong result, fails to complete, or behaves unexpectedly. It provides a systematic path from "something went wrong" to "here's the root cause and fix."

## Prerequisites

Before starting, you need:
- Access to the agent's trace/execution log for the failed run
- The expected output (or at least "not this")
- The actual output or error

If you do not have traces, stop and instrument first (see [Observability Stack](observability-stack.md)).

---

## Step 1: Classify the Failure Type

Before investigating, classify. The failure type determines where to look.

| Failure Type | Symptoms | Start Investigation At |
|-------------|----------|----------------------|
| **Hard failure** | Error thrown, run did not complete | Step 2: Error trace |
| **Wrong output** | Run completed, result is incorrect | Step 3: Output comparison |
| **Degraded quality** | Output is acceptable but worse than before | Step 4: Regression detection |
| **Timeout/loop** | Run did not terminate or took too long | Step 5: Loop detection |
| **Partial completion** | Some steps succeeded, others failed or were skipped | Step 6: Step-by-step audit |

---

## Step 2: Hard Failure — Error Trace

**Goal:** Find the exact point of failure and its immediate cause.

1. Open the execution trace for the failed run.
2. Find the span with `status: error`.
3. Read the error message and stack trace.
4. Categorize:

| Error Category | Common Causes | Fix Direction |
|---------------|---------------|---------------|
| Tool execution error | Bad arguments, tool unavailable, permission denied | Validate args before call; handle tool errors |
| Rate limit / quota | Too many calls, too many tokens | Add backoff; reduce token usage |
| Context overflow | Prompt + conversation exceeded window | Summarize; truncate; use retrieval |
| Parse failure | Model output did not match expected format | Add output validation + retry; improve format instructions |
| External dependency | API down, network timeout | Add retry with backoff; circuit breaker |

5. If the error is in a tool call: check the tool arguments in the log. Was the model's generated call valid?
6. If the error is in model output parsing: check the raw model response. Did the model follow the format instructions?

---

## Step 3: Wrong Output — Comparison Analysis

**Goal:** Find where the reasoning chain diverged from correct.

1. Get the full trace: every LLM call's input and output.
2. Walk the chain forward from the beginning.
3. At each step, ask: "Is this step's output reasonable given its input?"
4. Find the FIRST step where the output is wrong or misleading.
5. For that step, investigate:

| Divergence Cause | Diagnostic Question | Fix Direction |
|-----------------|--------------------|----|
| Wrong information in context | Was the context accurate and relevant? | Fix retrieval; fix context construction |
| Instruction not followed | Was the instruction clear? Was it buried? | Improve prompt structure; move instruction to more prominent position |
| Reasoning error | Did the model draw a wrong conclusion from correct premises? | Add verification step; chain-of-thought; or use a stronger model |
| Missing information | Did the model lack something it needed? | Add to context; add a tool that provides it |
| Stale context | Was the context outdated? | Refresh strategy; expiration |

---

## Step 4: Degraded Quality — Regression Detection

**Goal:** Identify what changed that caused quality to drop.

1. Find a recent "good" run of the same task type.
2. Diff the two runs:
   - Same model version?
   - Same system prompt?
   - Same tools available?
   - Same context construction logic?
   - Same input data characteristics?
3. The diff tells you what changed. Common culprits:

| Change | Why It Degrades Quality |
|--------|------------------------|
| Longer system prompt | Dilutes attention on task-specific instructions |
| New tool added | Model sometimes chooses wrong tool; more choices = more errors |
| Model version update | New model may interpret instructions differently |
| Context construction change | Different or less relevant information in prompt |
| Data drift | Input characteristics shifted beyond training distribution |

4. Write a regression eval that catches this specific degradation. Add it to the suite.

---

## Step 5: Timeout/Loop — Loop Detection

**Goal:** Find what the agent is doing repeatedly and why it cannot exit.

1. Open the trace. Look for repeated patterns:
   - Same tool called with same/similar arguments
   - Same reasoning structure repeated
   - Growing context without progress
2. Identify the loop type:

| Loop Type | Pattern | Fix |
|-----------|---------|-----|
| Retry without change | Same call, same args, same failure | Add failure handling; change strategy after N retries |
| Exploration without convergence | Different calls but no progress toward goal | Add a "step back" prompt; limit exploration budget |
| Context accumulation | Each iteration adds context, making the next iteration worse | Summarize before continuing; truncate irrelevant history |
| Oscillation | Alternates between two actions | Add memory of what was tried; conflict detection |

3. Check: does the agent have a loop budget (max iterations)? If not, add one.
4. Check: does the agent have an exit condition beyond "task complete"? If not, add timeout + graceful exit.

---

## Step 6: Partial Completion — Step-by-Step Audit

**Goal:** Find which step failed and why subsequent steps did not compensate.

1. List all steps in the plan/trace.
2. For each step, mark: completed successfully / failed / skipped.
3. For the first failed step: apply Step 2 (hard failure) or Step 3 (wrong output) analysis.
4. For skipped steps: ask why. Was it because:
   - The failed step's output was needed as input? (dependency failure)
   - The agent decided to skip based on wrong reasoning? (reasoning error)
   - The error handler aborted too eagerly? (error handling too strict)
5. Determine if the agent SHOULD have recovered:
   - Is there an alternative path that does not depend on the failed step?
   - Should the agent have retried with a different approach?
   - Should the agent have escalated to a human?

---

## Step 7: Root Cause Summary

After completing the relevant diagnostic steps, document:

```
## Root Cause Analysis

**Run ID:** [trace ID]
**Failure type:** [classification from Step 1]
**Root cause:** [one sentence]
**Evidence:** [link to specific span/log entry]
**Fix:** [what to change]
**Eval:** [test case to add that would have caught this]
```

---

## Quick Reference: "Where Do I Look?"

| Symptom | First Check |
|---------|-------------|
| Agent returned an error | Error span in trace → Step 2 |
| Agent returned wrong answer | First divergent reasoning step → Step 3 |
| Agent used to work but now doesn't | Diff against last working run → Step 4 |
| Agent is spinning/hanging | Repeated spans in trace → Step 5 |
| Agent did half the job | Step sequence in trace → Step 6 |
| Agent works sometimes | Compare successful vs. failed traces → find the variable input |

## Related Patterns

- [M01: Structured Trace](../patterns/M01-structured-trace.md) — the trace format needed for this runbook
- [M03: Execution Tree](../patterns/M03-execution-tree.md) — visualizing the execution path
- [M07: Replayable Run](../patterns/M07-replayable-run.md) — reproducing failures
- [M09: Failure Categorization](../patterns/M09-failure-categorization.md) — systematic classification
- [Observability Stack](observability-stack.md) — prerequisite instrumentation

## Sources

- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- Hamel Husain & Shreya Shankar — [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/)
- Hamel Husain & Shreya Shankar — [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
