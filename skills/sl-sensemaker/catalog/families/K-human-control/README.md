# Family K — Human Control

Patterns for deciding when an agent should pause, check in, or hand off to a human rather than proceeding autonomously.

**Recurring problem:** Not every decision should be autonomous. Agents that never pause erode trust and cause harm at speed; agents that always pause defeat the purpose of automation. This family calibrates the boundary.

**Core tension:** Autonomy increases throughput but reduces oversight. These patterns exist to match the level of human involvement to the current trust level, risk profile, and reversibility of the action.

---

## Practical session guidance

- [Develop a rough request through a focused interview](guides/clarify-an-idea.md).
- [Manage incoming decisions and reviews across tasks](guides/manage-review-overload.md).

## Directory Tree

```
K-human-control/
├── guides/
│   ├── README.md — practical guide navigation
│   ├── clarify-an-idea.md — Develop a rough request through a focused interview
│   ├── manage-review-overload.md — Manage incoming decisions and reviews across tasks
├── README.md                          ← this file (navigation hub)
├── autonomy-calibration-guide.md      ← when to use which level of human control
├── trust-ladder.md                    ← supervised → autonomous progression model
└── patterns/
    ├── K01-human-in-the-loop-checkpoint.md    ← pause at defined points and wait for human approval
    ├── K02-high-risk-action-gate.md           ← block irreversible/high-blast-radius actions until approved
    ├── K03-failure-threshold-escalation.md    ← escalate to human when retry/error budget is exhausted
    ├── K04-review-before-side-effect.md       ← require review of any action that changes external state
    ├── K05-draft-preview-before-apply.md      ← show a diff/preview and require confirmation before writing
    └── K06-human-on-the-loop-monitoring.md    ← human observes async; can intervene but is not in the critical path
```

---

## Per-Pattern File Schema

Each engineering pattern (`K0N-*.md`) follows this structure:

```
# K0N — Pattern Name

## Intent
One-sentence statement of what the pattern achieves.

## Problem
The recurring situation that makes this pattern necessary. What goes wrong without it.

## Solution
How the pattern works mechanically. What the agent does, what the human does, and how control transfers.

## Structure
Sequence or flow diagram (Mermaid) showing the decision path and actors.

## When to Use
Conditions, signals, or heuristics that indicate this pattern is appropriate.

## When NOT to Use
Counter-indications. What autonomy level or trust level makes this pattern wasteful or harmful.

## Implementation Notes
Concrete guidance: trigger conditions, timeout handling, what to show the human, how to resume.

## Tradeoffs
| Force | Impact |
|-------|--------|
| Latency | ... |
| Throughput | ... |
| Oversight | ... |
| Trust erosion | ... |

## Related Patterns
Links to other K-family patterns and cross-family overlaps.

## Example
A short concrete scenario showing the pattern in action.
```

---

If a generated diff outpaces review, start with [K01](patterns/K01-human-in-the-loop-checkpoint.md) for phase boundaries and [K05](patterns/K05-draft-preview-before-apply.md) when the tool can wait before a write. For independently verifiable chunks, see [B5](../B-task-decomposition/patterns/B5-milestone-checkpoint.md).

## Autonomy Calibration Guide

**Question to ask first:** How bad is the worst-case outcome if the agent proceeds without checking?

| Risk Level | Reversible? | Trust Level | Recommended Pattern |
|------------|-------------|-------------|---------------------|
| Low — cosmetic, sandboxed, or easily undone | Yes | Any | No gate needed; log for audit |
| Medium — touches external state, affects one user | Partially | Established | K05 Draft/Preview, K06 Monitoring |
| High — data loss, financial, multi-user impact | No | New or uncertain | K04 Review-Before-Side-Effect, K02 Gate |
| Critical — irreversible, regulatory, or security-affecting | No | Any | K02 High-Risk Gate always; K01 Checkpoint upstream |
| Degraded — agent has already failed N times | N/A | Any | K03 Failure-Threshold Escalation |

**Secondary question:** Is the human in the critical path or watching from the side?

- Human must approve before the agent proceeds → K01, K02, K04, K05 (blocking patterns)
- Human watches and can intervene but does not block → K06 (non-blocking monitoring)
- Human is called only when the agent gives up → K03 (escalation-only)

**Calibration heuristic — "BRIDE":**

- **B**last radius: how many systems/users are affected?
- **R**eversibility: can the action be undone in under 5 minutes?
- **I**nformation: does the agent have all the context a human would use?
- **D**elegation level: has the human explicitly granted autonomy for this action class?
- **E**xperience: has the agent completed this exact action class successfully N times before?

Score 0–1 for each. Sum ≥ 4 → proceed autonomously. Sum ≤ 2 → require human approval. Middle band → apply the lightest applicable K pattern.

---

## Trust Ladder

From least autonomous (most supervised) to fully autonomous. Agents should climb this ladder gradually — trust is earned through demonstrated reliability on a specific action class, not granted wholesale.

```
Level 0 — Supervised
  Every action requires explicit human approval before execution.
  Use when: new agent, new environment, first-time action class, critical domain.
  K patterns: K01 at every step, K04 on all side effects.

Level 1 — Gated
  Agent plans and previews freely; execution requires approval.
  Use when: agent is trusted for analysis but not yet for action.
  K patterns: K05 Draft/Preview before every write, K02 for high-risk classes.

Level 2 — Monitored
  Agent executes low-risk actions autonomously; human watches async.
  High-risk actions still blocked until approved.
  Use when: agent has a track record on routine tasks.
  K patterns: K06 Monitoring always-on, K02 for defined high-risk classes.

Level 3 — Escalating
  Agent proceeds autonomously for known action classes.
  Escalates only on failure, ambiguity, or out-of-scope situations.
  Use when: well-scoped domain, established error budget.
  K patterns: K03 Failure-Threshold Escalation, K02 for irreversible actions.

Level 4 — Audited
  Fully autonomous execution. Human reviews logs after the fact.
  Anomaly detection triggers re-review or temporary downgrade.
  Use when: high confidence, bounded scope, reversible outcomes.
  K patterns: none active; K06 in passive audit mode only.

Level 5 — Autonomous (rarely appropriate)
  No human review unless the agent itself flags an issue.
  Reserved for fully deterministic, trivially reversible, low-stakes tasks.
  K patterns: none.
```

**Important:** Trust level is per-action-class, not per-agent. An agent can be Level 4 for reading files and Level 1 for sending emails.

**Downgrade triggers:** Any of the following should reset an action class to Level 1:
- Unexpected failure in production
- Human overrides the agent's decision
- Scope of the action class expands
- Regulatory or security context changes

---

## Cross-Family Relationships

| Family | Overlap |
|--------|---------|
| J — Security | K02 High-Risk Gate and J's human-approval-gate are near-identical; K02 is the general form, J's variant adds security-specific trigger conditions |
| I — Reliability | K03 Failure-Threshold Escalation is the human-facing exit from I's retry chain |
| D — Verification | K01 Checkpoints can be inserted at D's verification points to add human calibration |
| B — Task Decomposition | K01 maps naturally to plan-approval gates between B's phases |

---

Last updated: 2026-11-22
