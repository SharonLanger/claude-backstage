# What Is the Theater Model

The Theater Model is a structured workflow model for multi-agent AI systems that require human oversight. It uses theater metaphors to organize how agents collaborate, how work flows between stages, and where a human must intervene.

## The metaphor

| Theater | Model |
|---|---|
| Play | A complete workflow definition — goal, stages, participants, verification, and decision points |
| Act | A focused stage of work with a clear goal and defined inputs/outputs |
| Lead | The primary agent in an Act — coordinates work, may delegate to Cast |
| Cast | Supporting agents assigned by the Lead for specialized subtasks |
| Director | The human — makes decisions at Gates, holds highest authority |
| Stage Manager | Coordinator agent — runs the sequence, tracks progress, enforces Gates |
| Checklist Agent | Independent verifier — checks Act outputs before the workflow advances |

## When to use it

Use the Theater Model when a workflow has:

- **Multiple stages** that must execute in order, with outputs feeding into later stages.
- **Human decision points** where a person must review evidence and approve before work continues.
- **Independent verification** — you need proof that each stage's output meets criteria before moving on.
- **Multiple agents** that need clear boundaries on what they can read, write, and delegate.

## When not to use it

- Single-agent tasks with no human checkpoints.
- Simple pipelines where output validation is unnecessary.
- Real-time or latency-sensitive workflows — the model prioritizes correctness and oversight over speed.

## Key principles

1. **Sequential execution** — Acts run one at a time, in order. No parallel Acts.
2. **Gates are hard stops** — only the Director can open them. No agent can bypass a Gate.
3. **Independent verification** — the Checklist Agent is a fresh instance every time, with no memory of prior checks.
4. **File-based communication** — agents exchange work through files in designated folders, not through shared memory.
5. **Honest reporting** — agents must report failures truthfully. False passes and false failures are both unacceptable.
