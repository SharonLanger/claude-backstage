# Designing Review Gates and Approval Checkpoints

## Scenario

You need to implement approval workflows in an agent system — structured points where human reviewers must sign off before the agent proceeds. This applies to deployment pipelines, content publishing, financial operations, or any workflow where organizational policy requires human oversight.

## Quick Answer

1. **Design gates as explicit workflow nodes** — approval checkpoints should be first-class elements in your agent topology, not afterthoughts. Use [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md).
2. **Make approvals informative** — present reviewers with a clear summary of what the agent did, what it wants to do next, and what the risks are. Use K04-Graceful-Handoff (catalog entry unavailable).
3. **Batch and queue** — when multiple actions need approval, queue them for efficient batch review rather than interrupting per-action. Apply K03-Approval-Queue (catalog entry unavailable).

## Approval Workflow Design

### Core Components of an Approval Gate

Every approval checkpoint should include:

1. **Context**: What led to this point (summary of agent's work so far)
2. **Proposal**: What the agent wants to do (specific actions, not vague intentions)
3. **Risk assessment**: What could go wrong, what's irreversible
4. **Options**: Approve, reject, modify, or defer
5. **Timeout handling**: What happens if no reviewer responds within SLA

### Gate Placement Principles

| Place a gate... | Because... |
|-----------------|------------|
| Before irreversible actions | Cannot undo — must be right the first time |
| After planning, before execution | Plan review is cheaper than rollback |
| At phase boundaries | Natural review points in multi-step work |
| Before external communication | Messages to customers/partners cannot be unsent |
| When cost exceeds threshold | Prevent runaway spend on incorrect paths |
| Before privilege escalation | Principle of least authority requires explicit grant |

### Gate Types

#### Simple Approve/Reject

```
Agent work → [GATE: Approve?] → YES → Execute
                               → NO → Stop or revise
```

Best for: single clear action, binary decision, low complexity.

#### Approve with Modifications

```
Agent work → [GATE: Review proposal] → APPROVE → Execute as proposed
                                      → MODIFY → Agent adjusts, re-submits
                                      → REJECT → Agent stops or tries new approach
```

Best for: plans, drafts, code changes where the reviewer may want tweaks.

#### Tiered Approval

```
Agent work → [GATE 1: Low-risk reviewer] → Approved
             [GATE 2: High-risk reviewer] → Approved (only if action crosses threshold)
```

Best for: organizations with role-based authority levels.

#### Batch Approval Queue

```
Agent produces items → [Queue: 5 items pending]
                       → Reviewer batch-approves/rejects
                       → Agent proceeds with approved items
```

Best for: high-volume workflows (content moderation, PR reviews, data corrections).

## Implementation Considerations

### Reviewer Experience

- **Show diffs, not full state**: Reviewers should see what changed, not everything.
- **Highlight risks**: Explicitly flag irreversible actions, external communications, cost implications.
- **Provide one-click actions**: Approve/reject should be one action, not a multi-step form.
- **Include undo information**: Tell the reviewer how to reverse the action if it goes wrong.

### Timeout and Availability

| Scenario | Strategy |
|----------|----------|
| Reviewer available within minutes | Block and wait |
| Reviewer delayed (hours) | Queue, notify, continue other work |
| Reviewer unavailable (days) | Escalate to alternate reviewer |
| No reviewer available | Fail safe — do not proceed |
| Urgent action, slow approval | Define pre-approved emergency paths |

### State Management During Approval

While waiting for approval, the system must:

- **Preserve the agent's state** — so it can resume seamlessly after approval. Use [L-Checkpoint-State](../../families/L-memory-state/patterns/checkpoint-state.md).
- **Prevent stale approvals** — if the world changed since the proposal was made, flag the approval as potentially stale.
- **Handle concurrent work** — other agents or processes may modify shared state while awaiting approval.

### Audit and Compliance

- **Log every approval decision** — who approved, when, what context they saw.
- **Record rejections with reasons** — helps improve future agent proposals.
- **Maintain approval chain** — for regulated environments, preserve the full sequence of reviews.
- **Make approvals non-repudiable** — reviewer cannot deny having approved.

## Relevant Patterns

| Pattern | Role in Approval Workflows |
|---------|----------------------------|
| [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) | Core mechanism — block execution until approved |
| K03-Approval-Queue (catalog entry unavailable) | Batch pending approvals for efficient review |
| K04-Graceful-Handoff (catalog entry unavailable) | Present clear context when handing to reviewer |
| K05-Tiered-Autonomy (catalog entry unavailable) | Different approval requirements by action tier |
| K02-Configurable-Autonomy (catalog entry unavailable) | Allow organizations to adjust gate placement |
| [J08-Human-Approval-Gate](../../families/J-security-trust/patterns/J08-human-approval-gate.md) | Security-motivated approval requirements |
| J07-Audit-Trail (catalog entry unavailable) | Log all approval decisions for compliance |
| [B5-Milestone-Checkpoint](../../families/B-task-decomposition/patterns/B5-milestone-checkpoint.md) | Natural checkpoint at task milestones |
| [L-Checkpoint-State](../../families/L-memory-state/patterns/checkpoint-state.md) | Preserve agent state while awaiting approval |
| [C-Maker-Checker](../../families/C-orchestration/patterns/maker-checker.md) | Separate proposer from approver |
| [I-Human-Escalation](../../families/I-reliability-recovery/patterns/human-escalation.md) | Escalate when agent cannot self-resolve |
| [M01-Structured-Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md) | Provide audit-quality trace for reviewers |

## Anti-Patterns to Watch For

| Anti-Pattern | Problem |
|--------------|---------|
| Approval fatigue (too many gates) | Reviewers rubber-stamp without reading, defeating the purpose |
| Insufficient context at gate | Reviewer cannot make an informed decision, approves blindly or rejects conservatively |
| No timeout handling | Agent blocks forever waiting for an unavailable reviewer |
| Stale approval execution | World changed between proposal and approval, action is no longer safe |
| No escalation path | If primary reviewer is unavailable, system deadlocks |
| All-or-nothing gates | Reviewer must approve everything or reject everything; no partial approval |

## Example: Code Deployment Approval Workflow

```
Agent: Code changes ready for deployment

[GATE 1: Code Review]
├── Show: diff, test results, coverage delta, affected services
├── Reviewer: approve / request changes / reject
└── Timeout: 4 hours → notify backup reviewer

[GATE 2: Deployment Approval] (only after Gate 1 passes)
├── Show: deployment plan, rollback procedure, affected users
├── Reviewer: approve / schedule for later / reject
└── Timeout: 2 hours → escalate to on-call lead

[Execution]
├── Deploy with canary (10% traffic)
├── Monitor for 15 minutes
└── [GATE 3: Full Rollout] — auto-approve if metrics are green, else block
```

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
