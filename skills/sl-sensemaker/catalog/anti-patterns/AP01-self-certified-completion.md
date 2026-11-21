# AP01 — Self-Certified Completion

## Symptoms

- The agent declares "done" without running tests, linters, or validators
- Output quality degrades silently over time because nobody checks
- Human reviewers discover obvious errors that automated checks would have caught
- The system has no mechanism to distinguish "agent thinks it's done" from "output meets acceptance criteria"
- Confidence in agent output erodes, leading to manual re-checking of everything

## Root Cause

Teams treat the model's assertion that a task is complete as sufficient evidence of completion. This happens because early prototypes work well on simple tasks where the model's self-assessment is accurate, creating a false sense that self-certification scales. In reality, as tasks grow in complexity, the model's ability to judge its own output degrades — it cannot reliably detect its own hallucinations, missed edge cases, or subtle regressions.

## Failure Scenario

A coding agent is tasked with fixing a bug in a payment processing service. The agent reads the error, modifies two files, and responds "Fixed the null pointer exception in the payment handler." The team's pipeline accepts this at face value and merges. In production, the fix introduced a race condition that only manifests under load — the agent never ran the test suite, never checked for concurrent access patterns, and had no mechanism to verify the fix beyond its own assessment. The bug reaches production and causes duplicate charges for 2% of transactions over a weekend.

## Counter-Patterns

- [D02 — Test Before Done](../families/D-verification-evaluation/patterns/D02-test-before-done.md) — Require passing automated checks before marking a task complete
- [D03 — Evidence-Based Completion](../families/D-verification-evaluation/patterns/D03-evidence-based-completion.md) — Completion requires observable evidence, not self-declaration
- [D01 — Deterministic Validator](../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) — Use compilers, tests, and schemas as objective completion gates
- [F03 — Executable Feedback Loop](../families/F-harness-environment/patterns/F03-executable-feedback-loop.md) — Give the agent access to execution results that confirm correctness

## Sources

- Anthropic — [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Hamel Husain & Shreya Shankar — [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/)
