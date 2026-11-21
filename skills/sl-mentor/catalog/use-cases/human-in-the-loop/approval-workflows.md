# Designing Review Gates and Approval Checkpoints

## Scenario

You need to implement approval workflows in an agent system — structured points where human reviewers must sign off before the agent proceeds. This applies to deployment pipelines, content publishing, financial operations, or any workflow where organizational policy requires human oversight.

## Quick Answer

1. **Design gates as explicit workflow nodes** — approval checkpoints should be first-class elements in your agent topology, not afterthoughts. Use [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md).
2. **Make approvals informative** — present reviewers with the relevant context, proposed action, and expected effects. Use [K04 Review Before Side Effect](../../families/K-human-control/patterns/K04-review-before-side-effect.md).
3. **Batch and queue** — when multiple actions need approval, queue them for efficient batch review rather than interrupting per-action. See [Batch Approval Queue](#batch-approval-queue).

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

- **Log the full approval lifecycle** — record the request, who made the decision, when it was made, what context the reviewer saw, and whether the action ran or was cancelled. See [J08 Human Approval Gate](../../families/J-security-trust/patterns/J08-human-approval-gate.md).
- **Record rejections with reasons** — helps improve future agent proposals.
- **Maintain approval chain** — for regulated environments, preserve the full sequence of reviews.
- **Protect approval records** — store decisions in an append-only log outside the agent’s reach. [J04 Tool Gateway](../../families/J-security-trust/patterns/J04-tool-gateway.md) describes this storage for tool calls. Independently detecting tampering requires a separate control.

## Relevant Patterns

| Pattern | Role in Approval Workflows |
|---------|----------------------------|
| [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) | Core mechanism — block execution until approved |
| [Batch Approval Queue](#batch-approval-queue) | Batch pending approvals for efficient review |
| [K04 Review Before Side Effect](../../families/K-human-control/patterns/K04-review-before-side-effect.md) | Present the proposed action and its effects before execution |
| [Tiered Approval](#tiered-approval) | Set reviewer authority and approval requirements by action risk |
| [Autonomy Calibration Guide](../../families/K-human-control/autonomy-calibration-guide.md) | Choose the autonomy level for each type of task |
| [J08-Human-Approval-Gate](../../families/J-security-trust/patterns/J08-human-approval-gate.md) | Security-motivated approval requirements |
| [Audit and Compliance](#audit-and-compliance) | Record approvals, rejections, and review context across the approval lifecycle |
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
