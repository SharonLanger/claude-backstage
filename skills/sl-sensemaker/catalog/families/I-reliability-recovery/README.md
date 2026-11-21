# Family I — Reliability & Recovery

**Recurring problem:** Agents fail partially, loop, repeat mistakes, or lose progress. This family covers how agent systems detect failure, decide whether to retry, and recover state.

---

## Practical session guidance

- [Choose between a repair and a fresh bounded implementation](guides/repair-or-fresh-attempt.md).

## Practitioner entry points

- [Recover a drifting session](patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work) — the session returns to an abandoned approach or forgets a decision.
- [Turn feedback into a check](patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check) — the agent agrees with feedback but the fix is still wrong.

## Directory Tree

```
I-reliability-recovery/
├── guides/
│   ├── README.md — practical guide navigation
│   ├── repair-or-fresh-attempt.md — Choose between a repair and a fresh bounded implementation
├── README.md                          ← this file (navigation, lookup tables, decision guide)
│
├── patterns/
│   ├── validation-retry-loop.md       ← retry gated on output passing a validator
│   ├── retry-with-feedback.md         ← retry with the error message injected into context
│   ├── structured-error-classification.md  ← classify errors before acting on them
│   ├── bounded-retry.md               ← hard cap on retry count
│   ├── stop-condition.md              ← explicit exit criteria that halt the loop
│   ├── human-escalation.md            ← route to a human when automation cannot proceed
│   ├── checkpoint-and-resume.md       ← persist progress so a restart skips done work
│   ├── fresh-context-retry.md         ← discard accumulated context; start a clean run
│   ├── fallback-model-workflow.md     ← degrade to a simpler model or alternative path
│   ├── circuit-breaker.md             ← stop attempting after repeated failure; wait then reset
│   └── root-cause-before-retry.md     ← diagnose why before retrying
│
└── anti-patterns/
    ├── retry-without-new-information.md   ← retrying the same prompt with no change
    └── infinite-weakly-bounded-loop.md    ← loop with no hard exit condition
```

---

## Per-Pattern File Schema

Each engineering entry in `patterns/` and `anti-patterns/` follows this structure:

```markdown
# <Pattern Name>

**Family:** I — Reliability & Recovery
**Type:** Pattern | Anti-Pattern

## Problem
One paragraph: what goes wrong without this pattern.

## Solution
One paragraph: the core mechanic of the pattern.

## Structure
Minimal pseudocode or component diagram showing the key steps.

## When to Use
Bullet list of conditions that call for this pattern.

## When Not to Use
Bullet list of conditions where this pattern is wrong or overkill.

## Trade-offs
| Pro | Con |
|-----|-----|
| ... | ... |

## Example
Concrete scenario showing the pattern applied.

## Related Patterns
Links to related patterns in this family and other families.

## Related Anti-Patterns
What you fall into if you misapply this pattern.
```

---

If an agent reintroduces a rejected approach and accumulated attempts may be influencing the next try, see [Fresh-Context Retry](patterns/fresh-context-retry.md). If the failure is still unexplained, see [Root-Cause-Before-Retry](patterns/root-cause-before-retry.md). For a person in a chat or CLI, start with the session-recovery subsection above. It preserves rejected alternatives and useful work; a guarantee of permanent compliance and code-local enforcement remain outside its scope.

## Failure Mode → Recovery Pattern

Quick-reference: given the failure type, which pattern(s) to reach for first.

| Failure Mode | Primary Pattern | Secondary / Fallback |
|---|---|---|
| Output fails a quality/format check | Validation-Retry Loop | Retry-With-Feedback |
| Output is wrong but agent doesn't know why | Root-Cause-Before-Retry | Structured Error Classification |
| Same error repeats across retries | Fresh-Context Retry | Human Escalation |
| Error type is ambiguous (transient vs. logic vs. resource) | Structured Error Classification | Circuit Breaker |
| Retry count keeps growing with no success | Bounded Retry + Stop Condition | Circuit Breaker |
| Progress is lost when the run crashes | Checkpoint and Resume | — |
| Task is beyond automation capability | Human Escalation | Fallback Model / Workflow |
| Downstream service is degraded or rate-limiting | Circuit Breaker | Fallback Model / Workflow |
| Accumulated context is corrupting future steps | Fresh-Context Retry | — |
| Loop never terminates | Stop Condition | Bounded Retry |
| Primary model unavailable or too expensive for retry | Fallback Model / Workflow | — |
| Error is recoverable but agent retried without change | Retry-With-Feedback | Root-Cause-Before-Retry |

---

## Retry or Escalate? — Decision Guide

Use this guide when an agent has just failed and must decide what to do next.

```
1. Is this the first failure?
   YES → classify the error (Structured Error Classification)
   NO  → continue below

2. Is the error transient (network, rate limit, timeout)?
   YES → wait and retry (Bounded Retry with backoff)
   NO  → continue below

3. Has the same error occurred N times already?  (N = your retry cap)
   YES → stop retrying; go to step 6
   NO  → continue below

4. Does the agent have new information to act on
   (error message, validator output, diagnostic result)?
   YES → inject feedback and retry (Retry-With-Feedback or Validation-Retry Loop)
   NO  → diagnose first (Root-Cause-Before-Retry), then retry with findings

5. Is accumulated context likely polluting the reasoning?
   YES → discard context and retry clean (Fresh-Context Retry)
   NO  → continue retrying with feedback (step 4 path)

6. Retry cap reached or no recovery path visible.
   Is a simpler model / alternative workflow available?
   YES → degrade gracefully (Fallback Model / Workflow)
   NO  → escalate to a human (Human Escalation)

ALWAYS: ensure a Stop Condition is defined before entering any retry loop.
ALWAYS: use Checkpoint and Resume for long multi-step tasks so recovery
         does not restart from zero.
```

---

## Anti-Patterns Addressed

| Anti-Pattern | What it looks like | Primary cure |
|---|---|---|
| Retry Without New Information | Agent retries the same prompt unchanged after failure | Retry-With-Feedback; Root-Cause-Before-Retry |
| Infinite / Weakly Bounded Agent Loop | No hard exit; loop runs until context limit or budget exhaustion | Bounded Retry + Stop Condition |

---

## Related Families

| Family | Connection |
|---|---|
| A — Topologies | Bounded loop is a topology concern; reliability patterns constrain it |
| D — Verification | Failure must be detected before recovery can begin |
| K — Human Control | Human Escalation is the handoff point between automation and oversight |
| L — Memory & State | Checkpoint and Resume is a state-persistence pattern |
| M — Observability | You cannot recover what you cannot see; monitoring surfaces failure signals |

---

Last updated: 2026-11-22
