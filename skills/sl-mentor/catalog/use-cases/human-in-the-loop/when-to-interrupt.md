# Deciding When Agents Should Pause for Human Input

## Scenario

You are designing an agent system and need to determine where to insert human checkpoints — points where the agent stops and waits for human review, approval, or guidance. Too few checkpoints risk dangerous autonomous actions; too many create bottlenecks that negate the value of automation.

## Quick Answer

1. **Interrupt on irreversibility** — any action that cannot be undone (sending an email, deleting data, making a purchase, deploying to production) should require human confirmation. Use [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md).
2. **Interrupt on uncertainty** — when the agent's confidence drops below a threshold or it encounters ambiguous instructions, it should ask rather than guess. Use [I-Human-Escalation](../../families/I-reliability-recovery/patterns/human-escalation.md).
3. **Don't interrupt on routine work** — if the agent is executing well-defined, reversible, low-risk operations, let it run autonomously with [K06-Human-on-the-Loop-Monitoring](../../families/K-human-control/patterns/K06-human-on-the-loop-monitoring.md).

## Decision Matrix: When to Interrupt

| Factor | Autonomous (no interrupt) | Monitor (async review) | Checkpoint (stop and wait) |
|--------|---------------------------|------------------------|----------------------------|
| **Reversibility** | Fully reversible | Partially reversible | Irreversible |
| **Impact scope** | Single file/record | Multiple records/users | Organization-wide |
| **Confidence** | High confidence, clear intent | Moderate confidence | Low confidence or ambiguous |
| **Risk** | No harm possible | Limited harm, recoverable | Significant harm potential |
| **Precedent** | Done this many times before | Similar to past actions | Novel situation |
| **Cost** | Low cost if wrong | Medium cost if wrong | High cost if wrong |

## Decision Flowchart

```
Agent wants to take an action:
│
├── Is the action reversible?
│   ├── YES → Is the agent confident it's correct?
│   │   ├── YES → Execute autonomously
│   │   └── NO → Pause and ask for clarification
│   └── NO → Is there a clear, unambiguous instruction from the user?
│       ├── YES → Is it a routine action the user has approved before?
│       │   ├── YES → Execute with logging (monitor mode)
│       │   └── NO → Pause for explicit confirmation
│       └── NO → Always pause for confirmation
│
├── Does the action affect other people/systems?
│   ├── NO → Lower threshold for autonomous execution
│   └── YES → Higher threshold, favor checkpoints
│
└── Has the agent failed or been uncertain recently in this session?
    ├── YES → Lower confidence threshold, interrupt more
    └── NO → Maintain current threshold
```

## Types of Human Interruption

### 1. Confirmation Gate (Synchronous Block)

The agent stops completely and waits for explicit "go/no-go."

**Use for:**
- Irreversible actions (delete, send, publish, deploy)
- Actions with significant cost (API calls, purchases)
- First time performing a new action type
- Actions the user's organization policy requires approval for

**Pattern:** [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md)

### 2. Clarification Request (Synchronous Block)

The agent pauses because it cannot proceed without more information.

**Use for:**
- Ambiguous instructions with multiple valid interpretations
- Missing information required for the next step
- Conflicting requirements detected
- Agent confidence below threshold

**Pattern:** [I-Human-Escalation](../../families/I-reliability-recovery/patterns/human-escalation.md)

### 3. Progress Report (Async Notification)

The agent continues working but notifies the human of status.

**Use for:**
- Long-running tasks (show milestones)
- Intermediate results that may inform future direction
- Decisions the agent made autonomously (for audit)

**Pattern:** [K06-Human-on-the-Loop-Monitoring](../../families/K-human-control/patterns/K06-human-on-the-loop-monitoring.md)

### 4. Escalation (Synchronous Block)

The agent encounters something beyond its capability or authority.

**Use for:**
- Repeated failures after retries
- Security-sensitive decisions
- Edge cases not covered by instructions
- Actions that exceed the agent's authorized scope

**Pattern:** [I-Human-Escalation](../../families/I-reliability-recovery/patterns/human-escalation.md), K05-Tiered-Autonomy (catalog entry unavailable)

## Calibrating Interrupt Frequency

**Too many interrupts** (signs):
- Users ignore or rubber-stamp approvals
- Automation provides no speed benefit over manual work
- The same type of action is approved every time without exception

**Too few interrupts** (signs):
- Agents take actions users didn't intend
- Costly mistakes happen before anyone notices
- Users feel loss of control or trust

**Right balance** (characteristics):
- Interrupts happen only when human judgment adds value
- Users trust the system enough to leave it running
- Mistakes are caught before they become costly
- Users can adjust autonomy level based on context

## Relevant Patterns

| Pattern | When to Apply |
|---------|---------------|
| [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) | Hard stop before irreversible actions |
| K02-Configurable-Autonomy (catalog entry unavailable) | Let users adjust how often agents interrupt |
| K03-Approval-Queue (catalog entry unavailable) | Batch pending approvals for efficient review |
| K04-Graceful-Handoff (catalog entry unavailable) | Transfer control smoothly when agent escalates |
| K05-Tiered-Autonomy (catalog entry unavailable) | Different autonomy levels for different action types |
| [K06-Human-on-the-Loop-Monitoring](../../families/K-human-control/patterns/K06-human-on-the-loop-monitoring.md) | Async oversight without blocking execution |
| [I-Human-Escalation](../../families/I-reliability-recovery/patterns/human-escalation.md) | Escalate on failure or uncertainty |
| [I-Stop-Condition](../../families/I-reliability-recovery/patterns/stop-condition.md) | Define when to stop autonomous iteration |
| [J08-Human-Approval-Gate](../../families/J-security-trust/patterns/J08-human-approval-gate.md) | Security-motivated approval requirements |
| [B5-Milestone-Checkpoint](../../families/B-task-decomposition/patterns/B5-milestone-checkpoint.md) | Review at natural task milestones |

## Anti-Patterns to Watch For

| Anti-Pattern | Problem |
|--------------|---------|
| Interrupt on every action | Negates the value of automation; users learn to approve blindly |
| Never interrupt | Agents make irreversible mistakes before anyone notices |
| Vague escalation criteria | Agent doesn't know when to ask, so it guesses wrong |
| No way to adjust autonomy | One-size-fits-all doesn't match different users' risk tolerance |
| Blocking on offline humans | Agent waits indefinitely because no reviewer is available |

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
