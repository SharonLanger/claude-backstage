# Recoverability — Bounded Failure, Structured Recovery, Zero Re-Work

Every failure mode has a defined exit: retry with feedback, retry with fresh context, or escalate to the human. No infinite loops. No silent failures. No full restarts. The checkpoint file (`progress.md`) means recovery never re-does completed work.

## Why this matters

Long multi-agent tasks are inherently fragile. A 5-Act Play where Act 4 fails should not re-run Acts 1–3. Bounded retries prevent runaway cost. Structured escalation gives the human only the failures the system couldn't resolve — high signal, no noise. Every retry gets a fresh context, breaking the failure cycle when accumulated errors are the root cause.

The human's trust in the system depends on predictable failure behavior. "It tried twice, then asked me" is trustworthy. "It looped for 20 minutes and produced garbage" is not.

## How the model achieves this

Each Act has a hard cap of 2 retries. `progress.md` persists state at each Act boundary so resume never re-does completed work. Each retry spawns a fresh agent — no accumulated errors polluting the new attempt. When budget is exhausted, the human gets a structured handoff: what was tried, what failed, what's needed.

GATEs are hard stops requiring human approval. The Checklist Agent re-checks work in a separate context with no confirmation bias. Each Act defines exit criteria that must be met with evidence before completion is claimed.

## Patterns implemented

| Pattern | Family | How the Theater Model applies it |
|---------|--------|----------------------------------|
| [Bounded Retry](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html) | I — Reliability & Recovery | Hard cap of 2 retries per Act per Run. Guarantees loop termination. Forces explicit escalation at cap. |
| [Checkpoint and Resume](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | I — Reliability & Recovery | `progress.md` persists state at each Act boundary. On failure, resume from last completed Act. Works across session boundaries. |
| [Fresh-Context Retry](https://www.anthropic.com/engineering/building-effective-agents) | I — Reliability & Recovery | Each retry spawns a fresh agent — no accumulated errors or failure history. Paired with checkpoint to preserve completed work. |
| [Human Escalation](https://www.anthropic.com/engineering/building-effective-agents) | I — Reliability & Recovery | Structured handoff: what was tried, what failed, what's needed. The consolidated folder makes the human's job tractable. |
| [Human-in-the-Loop Checkpoint](https://www.anthropic.com/engineering/building-effective-agents) | K — Human Control | GATEs are hard stops. The agent carries no implicit authority to proceed. Every checkpoint creates an audit record. |
| [High-Risk Action Gate](https://www.anthropic.com/engineering/building-effective-agents) | K — Human Control | Certain Acts can be marked as high-risk. The Director enforces a gate before they proceed. |
| [Failure-Threshold Escalation](https://www.anthropic.com/engineering/building-effective-agents) | K — Human Control | When budget is exhausted, escalation surfaces only failures the system couldn't resolve. |
| [Independent Verifier](https://www.anthropic.com/engineering/building-effective-agents) | D — Verification & Evaluation | The Checklist Agent re-checks work in a separate context — no confirmation bias. Sees only the output and criteria. |
| [Evidence-Based Completion](https://www.anthropic.com/engineering/building-effective-agents) | D — Verification & Evaluation | Each Act defines exit criteria. The Checklist Agent checks that required artifacts exist. No completion claim without evidence. |
| [State Machine](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | L — Memory & State | The Play defines a fixed state machine with legal transitions. Invalid transitions are structurally prevented. |
| [Maker-Checker](https://www.anthropic.com/engineering/building-effective-agents) | C — Orchestration | Cast member = maker. Checklist Agent = checker. No output is committed unless the checker has passed it. |
| [Programmatic Gate](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html) | H — Deterministic Control | Checklist gates run deterministic checks that cannot be bypassed by model output. GATEs are hard stops enforced by the Director. |
| [P4 — Separate Generation From Verification](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) | Principle | Cast members generate. Checklist Agent verifies. Director reviews at GATEs. Three structurally independent verification layers. |
| [Minimal-Context Handoff](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Between Acts, only the result is passed — not the journey. The next agent's context starts clean. |
| [Artifact-Based Handoff](https://www.anthropic.com/engineering/building-effective-agents) | E — Context Engineering | `progress.md` is the typed artifact between Acts. The Checklist Agent validates artifacts before the next Act begins. |
