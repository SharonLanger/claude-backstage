# Anti-Pattern: Generic Evals Before Analysis

## Name

Generic Evals Before Analysis

## Symptoms

- The team has an eval suite that runs broad benchmarks (e.g., "accuracy on 1000 diverse questions") but cannot explain why specific production failures occur.
- Eval scores are "good enough" but users report quality problems regularly.
- When a failure is reported, the response is "let's add it to the eval set" without first understanding the root cause.
- The eval suite grows by accumulation — new test cases added without categorization or prioritization.
- Eval scores improve on paper while user-perceived quality stagnates or declines.
- The team optimizes for aggregate metrics (accuracy, F1) rather than eliminating specific, understood failure categories.
- Nobody can list the top 5 failure modes by frequency or severity.

## Root Cause

Teams reach for evaluation frameworks before investing in understanding their system's actual failure modes. This happens because evals feel productive — you get a number, the number goes up, progress is made. Error analysis is harder: it requires reading individual failures, categorizing them manually, and building a taxonomy specific to your system. Generic evals provide the comfort of measurement without the insight of understanding.

The underlying mistake is measuring before diagnosing. A doctor who runs every available blood test before asking "where does it hurt?" is wasting resources and may optimize for the wrong biomarker. Similarly, a broad eval suite may push the team to optimize for cases that do not matter while ignoring the failures that users actually experience.

## Failure Scenario

A team builds a code review agent. They create an eval suite with 500 diverse code snippets and grade the agent's review quality on a 1–5 scale. The average score is 3.8 — "acceptable." They invest two months optimizing prompt structure and few-shot examples, pushing the score to 4.1.

Meanwhile, users report: "The agent keeps suggesting changes to code it didn't fully read — it hallucinates that functions exist that don't." This specific failure mode (context window overflow causing hallucinated references) accounts for 40% of user complaints but only 3% of the eval suite (because most eval snippets are short enough to fit in context). The eval improvement from 3.8 to 4.1 was driven by making the agent better at short snippets — which were never the problem.

Had the team started with error analysis — reading 50 real user complaints, categorizing them, and finding that "hallucinated references due to incomplete context" was the dominant failure — they could have fixed the actual problem (context management) instead of optimizing the wrong metric.

## Counter-Patterns

- [M09: Failure Categorization](../patterns/M09-failure-categorization.md) — classify real failures first, then build targeted evals
- [M08: Trace-Linked Eval](../patterns/M08-trace-linked-eval.md) — connect eval cases to specific traced failures
- [M01: Structured Trace](../patterns/M01-structured-trace.md) — the foundation for observing real failures

## Sources

- Hamel Husain & Shreya Shankar — [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/)
- Hamel Husain & Shreya Shankar — [Why Is Error Analysis Important](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html)
- Anthropic — [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
