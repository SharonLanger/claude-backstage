# Workflows

Structured processes for coordinating agents, managing context, and improving skills through repeatable stages. Each workflow includes its own setup guide, roles, and examples.

### [Theater Model](theater-model/README.md)

Define a Play, split it into Acts, and coordinate agents through a Stage Manager. Focused contexts, file-based handoffs, independent checks, and human approval gates make progress easier to inspect and resume.

Start with the [Play template](theater-model/template/README.md), then adapt the roles and stages to your task. The [design-pattern catalog](theater-model/design-patterns/README.md) explains the model's foundations.

### [Iteration Harness](iteration-harness/README.md)

Bring a skill and improve it through milestones: approve tests, run them, diagnose failures, apply versioned fixes, and review quality before advancing. Separate agent roles handle testing, reasoning, changes, and review.

Start with the [walkthrough](iteration-harness/harness-core/docs/walkthrough.md) and use the [runner guide](iteration-harness/harness-core/implementation/runner-guide.md) to prepare a run. The scaffold supplies the process; you supply the skill, and files marked `-mock` illustrate artifacts rather than actual results.

[← Claude Backstage](../README.md)
