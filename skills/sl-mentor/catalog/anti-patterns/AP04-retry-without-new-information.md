# AP04 — Retry Without New Information

## Symptoms

- The agent fails, then retries the exact same action hoping for a different result
- Retry loops burn tokens and time without making progress
- Error messages are not parsed or incorporated into the next attempt
- The same failure repeats 3-5 times before the agent gives up or hits a budget limit
- Logs show identical requests repeated in sequence with identical failures

## Root Cause

Teams implement retry logic without requiring that each retry incorporates new information about why the previous attempt failed. This mirrors naive exception handling in traditional software — catch and retry without diagnosis. The model, lacking explicit error-classification and feedback-incorporation logic, defaults to repeating what it already tried because it has no structured mechanism to analyze the failure and adjust its approach. The missing piece is always the same: diagnostic information that changes the next attempt.

## Failure Scenario

A deployment agent attempts to push a Docker image to a registry. The push fails with "403 Forbidden — authentication token expired." The agent retries the push command four more times, receiving the same 403 each time. After five attempts it reports "deployment failed — unable to push image" without ever attempting to refresh the authentication token or examining the error code. The team's retry budget is exhausted, the deployment window closes, and a human must intervene to run a single `docker login` command before the push succeeds on the first try.

## Counter-Patterns

- [I08 — Root Cause Before Retry](../families/I-reliability-recovery/patterns/root-cause-before-retry.md) — Diagnose the failure before attempting again
- [I07 — Retry with Feedback](../families/I-reliability-recovery/patterns/retry-with-feedback.md) — Each retry must incorporate the error signal
- [I10 — Structured Error Classification](../families/I-reliability-recovery/patterns/structured-error-classification.md) — Categorize errors to determine the right recovery action
- [I05 — Fresh Context Retry](../families/I-reliability-recovery/patterns/fresh-context-retry.md) — Reset polluted context before retrying

## Sources

- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
