# 🔄 Workflows

Structured processes that bring agents, skills, and stages together.

Each workflow has its own folder describing its purpose, required inputs, agent responsibilities, execution steps, and expected outputs.

## Available workflows

| Workflow | Purpose | Format |
|---|---|---|
| [Iteration Harness](iteration-harness/README.md) | Develop and improve AI skills through milestones, tests, fixes, and quality reviews. | Markdown scaffold with mock examples |

## Iteration Harness

Bring a skill you want to develop and define its first milestone. The harness provides a process for testing the skill, analyzing failures, applying versioned fixes, and reviewing quality before advancing.

It includes:

- Agent roles for testing, reasoning, skill changes, and review.
- Milestone test structures, assertions, and reporting rules.
- Versioning guidance and human approval gates.
- Review criteria and checklists.
- Mock results, decisions, and fix instructions illustrating the expected artifacts.

The skill being developed is supplied separately. Files marked `-mock` are examples, not results from actual runs.

### Where to start

1. Read the [workflow overview and setup guide](iteration-harness/README.md).
2. Follow the [walkthrough](iteration-harness/harness-core/docs/walkthrough.md).
3. Use the [runner guide](iteration-harness/harness-core/implementation/runner-guide.md) when preparing a run.

[← Back to Claude Backstage](../README.md)
