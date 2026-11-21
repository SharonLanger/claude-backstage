# AP08 — Generic Evals Before Error Analysis

## Symptoms

- The team runs benchmark suites (MMLU, HumanEval, etc.) but cannot explain why their specific system fails on specific inputs
- Eval dashboards show aggregate scores improving while user complaints increase
- Nobody has manually reviewed a sample of failures to categorize them
- The team optimizes for a metric (accuracy, F1, pass@k) without knowing what errors compose the failures
- "Our eval score went up 3%" is celebrated without understanding whether the remaining failures are critical or trivial
- Prompt changes are evaluated by re-running the full benchmark rather than by examining failure cases

## Root Cause

Teams apply the standard ML evaluation playbook (train, eval, iterate on metrics) to LLM systems without first understanding their failure modes. Generic benchmarks measure average capability, not task-specific reliability. A system can score 95% on a generic eval while systematically failing on the 5% of cases that matter most to users — edge cases, ambiguous inputs, multi-step reasoning. The fix starts with error analysis: look at actual failures, categorize them, understand their root causes, then build evals that target those specific failure categories. Generic evals are useful later as regression guards, not as the primary optimization target.

## Failure Scenario

A legal document summarization team achieves 92% on their eval suite and ships to production. Users immediately report that the system mishandles limitation-of-liability clauses — it summarizes them as favorable when they contain carve-outs that reverse the apparent meaning. This failure category affects only 8% of documents but represents the highest-stakes use case. The generic eval never tested for semantic inversion in nested clauses because nobody analyzed real failures first. The team spent three months optimizing a metric that did not capture their most dangerous failure mode.

## Counter-Patterns

- [D12 — Step-Level Diagnostic](../families/D-verification-evaluation/patterns/D12-step-level-diagnostic.md) — Evaluate at the step level to find where failures originate
- [M09 — Failure Categorization](../families/M-observability-debugging/patterns/M09-failure-categorization.md) — Classify failures before choosing metrics
- [D11 — End-to-End Task Success](../families/D-verification-evaluation/patterns/D11-end-to-end-task-success.md) — Measure actual task success, not proxy metrics
- [D10 — Human Calibration](../families/D-verification-evaluation/patterns/D10-human-calibration.md) — Calibrate automated evals against human judgment

## Sources

- Hamel Husain & Shreya Shankar — [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/)
- Hamel Husain & Shreya Shankar — [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- Hamel Husain & Shreya Shankar — [Why Is Error Analysis Important](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html)
- Anthropic — [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
