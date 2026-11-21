# Retry-With-Feedback

**Family:** I — Reliability & Recovery
**Type:** Pattern

## Problem

When an agent fails, the simplest recovery is to try again with the same input. Repeating an identical prompt may produce another failure without resolving what went wrong. Without new information, retries waste tokens and time.

## Solution

Before retrying, inject the failure signal — the error message, the validator report, the tool exception, or the evaluator's critique — directly into the conversation context. The model then has explicit evidence of what went wrong and can correct its approach. Each retry carries forward everything learned from prior failures.

## In a session: turn feedback into a check

Use this after the agent has produced work you can inspect. You control the conversation and need a known expected outcome. Code claims require relevant execution or inspection; a prose revision can be checked directly against its content requirements. Agreement with a review comment does not show that a revision is correct.

Ivett Ördög's ROSE feedback names the risk, observation, requested solution, and expected outcome. Use only the elements needed; they need not appear in that order. Our adaptation from PAT-0005 makes the outcome checkable and adds a neighboring case that a shortcut might break.

1. Describe what you observed, with an input or location, separately from the suspected cause and possible consequence.
2. State the agreed behavior. If the cause is unknown, ask for investigation rather than prescribing an unverified fix. If the requirement itself is unresolved, get that decision before editing.
3. Ask for the failed example and a nearby existing case to be checked after the change. Request observable results; read changes to assertions and expected outputs yourself.
4. Close the feedback when the revision matches the requirement, not when the agent says it agrees. If the same premise returns despite useful feedback, consult [Fresh-Context Retry](fresh-context-retry.md).

**Original illustration:** “With an explicit retry count of zero, this parser returns three. That could repeat work the caller disabled. Preserve explicit counts; the configuration contract still defaults to three when absent. Show results for zero, absent, and two, and the relevant diff.”

Expected results are 0, 3, and 2. Replacing the default with zero passes only the first case. An agent's verbal prediction still needs a check on the revised work.

**Limits:** A wrong expected result can steer a correct implementation into a bug. A one-line correction is sufficient when its context and check are already clear. This practice helps structure feedback; it does not permanently train the model or demonstrate general effectiveness.

## Solution Structure

<details>
<summary><b>Retry-With-Feedback — Context Injection Flow</b></summary>

```mermaid
flowchart TD
    A([Attempt N fails]) --> B[Capture failure signal\nerror / validator / critique]
    B --> C[Append failure signal\nto context as user message]
    C --> D{Retry cap\nreached?}
    D -->|No| E[Generate next attempt\nwith enriched context]
    E --> F{Succeeded?}
    F -->|Yes| G([Accept output])
    F -->|No| A
    D -->|Yes| H([Escalate / Fallback])

    style A fill:#5c1a1a,color:#fff
    style G fill:#1a5c2a,color:#fff
    style H fill:#5c1a1a,color:#fff
    style B fill:#1a3a6b,color:#fff
    style C fill:#1a3a6b,color:#fff
    style D fill:#1a3a6b,color:#fff
    style E fill:#3a1a6b,color:#fff
    style F fill:#1a3a6b,color:#fff
```

</details>

## Structure

```
function retryWithFeedback(prompt, executor, maxRetries):
    context = [systemMessage(prompt)]
    attempt = 0

    while attempt < maxRetries:
        output = executor(context)

        if succeeded(output):
            return output

        failureSignal = extractFailureReason(output)
        context.append(assistantMessage(output.rawContent))
        context.append(userMessage(
            "The previous attempt failed. Reason: " + failureSignal +
            "\nPlease correct the issue and try again."
        ))
        attempt += 1

    raise RetryCapExceeded(context)
```

## When to Use

- The failure signal is informative enough that the model can act on it (error messages, schema violations, tool exceptions with descriptions).
- Errors are model-caused rather than infrastructure-caused (transient network errors don't benefit from this; just wait and retry).
- The accumulated context from prior attempts does not yet crowd out the working space.
- You need more than one corrective attempt before escalating.

## When Not to Use

- The error message is opaque or uninformative — injecting noise does not help.
- Failures stem from a fundamentally wrong approach that context accumulation will not fix; use [Fresh-Context Retry](fresh-context-retry.md) instead.
- The task is simple enough that a single retry without feedback is sufficient.
- Context length is already near its limit — appending feedback may overflow the window.

## Trade-offs

| Pro | Con |
|-----|-----|
| Each retry is better informed than the last | Conversation context grows with every failure |
| Directly addresses the OpenAI principle: failures are evidence, not just cues to try harder | If the failure signal is misleading, feedback can steer the model in the wrong direction |
| Composable — works inside Validation-Retry Loop or as a standalone wrapper | Requires parsing or extracting a useful failure signal from raw exceptions |
| Minimal overhead; no architectural change to the agent | Does not help when the model lacks the capability to fix the identified problem |

## Example

An agent uses a code-execution tool to run generated Python. The first attempt raises `AttributeError: 'NoneType' object has no attribute 'split'`. The feedback injector appends the full traceback as a user message. On attempt 2 the model adds a null check. The execution succeeds.

## Related Patterns

- [Validation-Retry Loop](validation-retry-loop.md) — a structured loop that uses this pattern as its feedback step
- [Bounded Retry](bounded-retry.md) — caps the number of feedback-enriched retries
- [Root-Cause-Before-Retry](root-cause-before-retry.md) — a deeper diagnostic step before injecting feedback
- [Fresh-Context Retry](fresh-context-retry.md) — alternative when accumulated context becomes the problem
- [Structured Error Classification](structured-error-classification.md) — determines what kind of feedback to inject

## Related Anti-Patterns

- [Retry Without New Information](../anti-patterns/retry-without-new-information.md) — the failure mode this pattern directly prevents

## Sources

- **Anthropic Engineering** — AI safety company; authors of Claude. [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **OpenAI Engineering** — AI research company; authors of GPT and Codex. [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- **AWS Prescriptive Guidance** — Amazon Web Services architecture team; defines Validation-Retry Loop and Structured Error Classification. [Agentic AI Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)

- Ivett Ördög / Samman Coaching — [ROSE Feedback](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html): feedback structure, optional elements, and scope to already produced work; consulted 2026-11-21. The ROSE-based session subsection above adapts this lesson with new wording, a new illustration, and a verification step; that subsection is shared under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
