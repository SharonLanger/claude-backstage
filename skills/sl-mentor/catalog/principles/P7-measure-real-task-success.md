# Principle 7 — Measure Real Task Success

> A beautiful reasoning trace or fluent answer is irrelevant if the requested outcome did not happen.

---

## Why This Matters

Proxy metrics — fluency, format compliance, step completion, reasoning quality — diverge from real task outcomes in ways that are difficult to detect. A coding agent that produces well-structured code that doesn't compile, a summarization system that writes fluent summaries that omit key facts, or a research agent that follows its plan perfectly but answers the wrong question all score well on proxies while failing the actual task. Systems optimized against proxies produce output that looks correct but isn't.

This principle recurs because evaluation is where the gap between "impressive demo" and "reliable production system" becomes measurable. Hamel Husain and Shreya Shankar demonstrated that error analysis must precede generic eval metrics — you cannot measure what you don't understand. Anthropic's evaluation guidance emphasizes measuring whether the actual task outcome occurred, not whether the model's behavior appeared reasonable. The convergence reflects hard-won production experience: teams that measure proxy metrics ship systems that degrade in ways invisible to their monitoring.

---

## Which Sources Converge

| Organization | What They Say | Key Concept |
|---|---|---|
| Hamel Husain & Shreya Shankar | Error analysis must precede metric selection; measure task outcomes, not model behavior | Failure-taxonomy-first evaluation methodology |
| Anthropic | Evals must measure whether YOUR system performs YOUR task on YOUR data | Task-specific evaluation over generic benchmarks |
| OpenAI | Harness feedback loops must detect real failures and feed them back into improvement | Ground-truth signal over behavioral proxy |
| Google Cloud | Pattern selection criteria include measurable task completion, not just step execution | End-to-end task success as the primary metric |

---

## Patterns That Implement This Principle

- [Task-Success Evaluation](../families/D-verification-evaluation/) — define success as the real-world outcome, not intermediate process quality
- [Trace-Driven Error Analysis](../families/M-observability-debugging/) — use execution traces to identify where task outcomes diverge from expectations
- [Evidence-Based Completion](../families/D-verification-evaluation/) — require observable evidence that the task succeeded before marking it complete
- [Explicit Definition of Done](../families/F-harness-environment/) — specify measurable completion criteria before execution begins

---

## Anti-Patterns This Prevents

- **Generic Evals Before Error Analysis** — applying off-the-shelf evaluation metrics without first understanding what failure modes exist in your specific system and task
- **Self-Certified Completion** — allowing the agent that performed the task to also judge whether it succeeded, without external verification of the actual outcome

---

## Practical Application

1. **Test execution as eval signal:** For a coding agent, the evaluation is not "does the code look correct?" but "do the tests pass?" Run the code, observe the result, and use that binary signal. A beautiful implementation that fails its tests is a failure; an ugly one that passes is a success.

2. **Error taxonomy before metrics:** Before building an evaluation suite, manually review 50–100 failures. Categorize them into a taxonomy (wrong tool selected, incomplete context, hallucinated API, correct approach but syntax error). Then build metrics that detect each failure category — not generic scores that average across them.

3. **End-to-end task assertions:** For a document-processing agent, don't measure "did it extract fields correctly?" in isolation. Measure "did the downstream system accept the output and produce the expected business outcome?" The extraction is a means, not an end.

4. **Regression detection on real tasks:** Maintain a set of real tasks (not synthetic benchmarks) that the system has previously completed successfully. Re-run them after changes. A regression is a task that previously succeeded and now fails — not a score that dropped by 2%.

---

## Sources

- Hamel Husain & Shreya Shankar — [Why Is Error Analysis Important](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html)
- Hamel Husain & Shreya Shankar — [Evaluating Agentic Workflows](https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html)
- Anthropic — [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Hamel Husain & Shreya Shankar — [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
