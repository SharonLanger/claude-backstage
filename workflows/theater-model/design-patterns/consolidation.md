# Consolidation — One Folder Is the System of Record

Everything about a Play lives in one folder: the plan (`play.md`), the checkpoint (`progress.md`), the rules, the role definitions, the reference material, the outputs. No external state. No conversation history to reconstruct. No separate database.

## Why this matters

Any agent — fresh or continuing — can reconstruct the full task state by reading the folder. Recovery time after a crash, timeout, or context limit is under 2 minutes. The human can inspect exactly where things stand by opening one directory.

When an agent session ends mid-task, nothing is lost. The folder IS the state. A replacement agent reads `progress.md`, sees what's done and what's next, and picks up without re-briefing from the human.

## How the model achieves this

The play folder is the single source of truth for all task state. Decisions are persisted in files, not in ephemeral conversation history. `progress.md` doubles as both the deliverable progress report and the state tracker — the folder's file listing itself indicates what work has been done. Between Acts, partial results are persisted so that GATEs become natural audit points where the full state is knowable and inspectable.

## Patterns implemented

| Pattern | Family | How the Theater Model applies it |
|---------|--------|----------------------------------|
| [Repository-as-System-of-Record](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | The play folder is the authoritative source of truth. When an agent needs state, it reads a file — not its conversation history. |
| [Repository-Local System of Record](https://openai.com/index/harness-engineering/) | F — Harness & Environment | Any agent can identify exactly where a task left off by reading `progress.md`, with no re-briefing from the human. |
| [Persistent Task Artifacts](https://openai.com/index/harness-engineering/) | F — Harness & Environment | All outputs are written to the play folder during execution — not just at task end. Artifacts survive session end and agent replacement. |
| [Checkpoint and Resume](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | I — Reliability & Recovery | `progress.md` is the checkpoint file. After each Act completes, the Stage Manager updates it. No full-restart cost after partial failures. |
| [Artifact State](https://www.anthropic.com/engineering/building-effective-agents) | L — Memory & State | `progress.md` doubles as both the deliverable progress report and the state tracker. |
| [Human Escalation](https://www.anthropic.com/engineering/building-effective-agents) | I — Reliability & Recovery | When retries are exhausted, the human is presented with the consolidated folder — everything needed for review is in one place. |
| [Map-Not-Manual](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | `play.md` is the index. Deep knowledge lives in referenced files. The Play stays concise; the folder holds the depth. |
| [Milestone Checkpoint](https://www.anthropic.com/engineering/building-effective-agents) | B — Task Decomposition | Acts are milestones. Between Acts, partial results are persisted. GATEs are audit points where the full state is inspectable. |
