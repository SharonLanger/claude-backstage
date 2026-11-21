# Principle 8 — Failures Should Improve the Harness

> When an agent repeatedly fails, inspect what capability, documentation, feedback, boundary, or validator is missing.

---

## Why This Matters

When agent failures are treated as isolated incidents — retried, worked around, or attributed to model limitations — the same failure mode recurs across tasks because the system that produced it remains unchanged. The insight that drives this principle is that the main bottleneck is often not model capability but an underspecified environment. A failure is diagnostic evidence about what the harness is missing: a missing tool, an unclear instruction, an absent validator, a gap in the feedback loop.

This principle appears across sources because production agent teams universally discover that improving the model is not the primary lever. OpenAI's harness engineering framework explicitly names this: failures are evidence of missing capabilities in the harness, not in the model. Hamel Husain's failure-taxonomy-first methodology operationalizes this — categorize failures, identify the systemic cause, and fix the environment rather than re-prompting. The pattern is consistent: teams that invest in harness improvement see compound returns, while teams that retry or re-prompt see the same failures recur indefinitely.

---

## Which Sources Converge

| Organization | What They Say | Key Concept |
|---|---|---|
| OpenAI | The main bottleneck is not model capability but an underspecified environment; failures are evidence of missing harness capabilities | Harness engineering as the primary improvement vector |
| Hamel Husain & Shreya Shankar | Build a failure taxonomy first, then address systemic causes; error analysis precedes solutions | Failure-taxonomy-first methodology |
| Anthropic | Agent evaluation should drive iterative system improvement, not just score reporting | Evals as a feedback loop into system design |
| AWS | Validation and recovery patterns should evolve based on observed failure modes | Error classification drives pattern selection |

---

## Patterns That Implement This Principle

- [Debugging Runbook](../families/M-observability-debugging/guides/debugging-runbook.md) — use execution traces to identify systemic failure causes
- [Retry With Feedback](../families/I-reliability-recovery/patterns/retry-with-feedback.md) — failed attempts produce diagnostic information that changes the next attempt
- [Repository-Local System of Record](../families/F-harness-environment/patterns/F02-repository-local-system-of-record.md) — harness improvements persist as code, documentation, and configuration
- [Bounded Agent Loop](../families/A-workflow-topology/patterns/bounded-loop.md) — loops terminate and surface failures rather than retrying indefinitely

---

## Anti-Patterns This Prevents

- **Retry Without New Information** — re-running the same prompt after a failure without changing anything about the context, tools, or constraints available to the model
- **Generic Evals Before Error Analysis** — measuring aggregate scores without understanding the specific failure modes those scores obscure, preventing targeted harness improvements

---

## Practical Application

1. **Failure log to harness change pipeline:** When an agent fails a task, log the failure category (missing context, wrong tool selected, ambiguous instruction, hallucinated fact). Weekly, review the failure log and make one harness change per top failure category — add a tool, clarify an instruction, add a validator.

2. **Post-mortem as harness ticket:** After a production failure, don't just fix the immediate issue. Ask: "What could the harness have provided that would have prevented this class of failure?" Turn the answer into a concrete improvement — a new lint rule, a pre-flight check, better error messages from tools.

3. **Evaluation-driven iteration:** Run evals, categorize failures into a taxonomy, then prioritize harness changes by failure frequency. A category that accounts for 40% of failures gets a harness fix before a category that accounts for 5% — regardless of which is more interesting technically.

4. **Documentation as failure response:** When an agent repeatedly misuses an API or makes the same incorrect assumption, the fix is not a longer prompt — it's better tool documentation, a worked example in the repository, or a validator that catches the mistake before it propagates.

---

## Sources

- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Hamel Husain & Shreya Shankar — [Why Is Error Analysis Important](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html)
- Anthropic — [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Hamel Husain & Shreya Shankar — [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/)
- AWS — [Agentic AI Patterns and Workflows](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
