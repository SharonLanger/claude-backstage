# Anti-Pattern: Giant Instruction Manual

## Name

Giant Instruction Manual

## Symptoms

- System prompt or instruction file exceeds 10,000 tokens and continues growing
- Agent selectively ignores rules — follows some, contradicts others, seemingly at random
- Adding new instructions causes previously-working behaviors to degrade
- Team's response to any agent failure is "add another rule to the prompt"
- Instruction file has become a changelog of accumulated fixes rather than a coherent document
- Agent performance varies between runs on identical tasks (non-determinism from attention dilution)
- No one on the team can explain the full contents of the instruction file from memory

## Root Cause

Teams treat the system prompt as an append-only log of lessons learned. Every time the agent makes a mistake, the fix is another instruction: "Never do X," "Always check Y," "Remember to Z." Over months, the prompt becomes a sprawling manual that no human would read cover-to-cover — and the model cannot effectively attend to all of it either.

The underlying belief is that more instructions equal better compliance. In practice, past a certain density, instructions compete for the model's attention. The model attends strongly to instructions near the beginning and end of the prompt, and weakly to those buried in the middle. Adding instruction N+1 can degrade compliance with instructions 1 through N.

## Failure Scenario

A team builds a coding agent with a 200-line AGENTS.md file containing: coding conventions, git workflow rules, security requirements, testing patterns, deployment procedures, team communication norms, and troubleshooting guides — all in one flat document.

The agent works well initially. Over three months, the team adds 50 more rules (one per bug encountered). By month four:
- The agent sometimes commits without running tests (rule added in month 2, buried at line 147)
- The agent occasionally uses deprecated APIs (rule added in month 3, line 189)
- The agent consistently follows the most recent rules (near the bottom) while ignoring older ones (middle)
- The team adds "IMPORTANT: Always run tests before committing" at the top — which helps for a week until the context around it grows further

The system is now in a state where the prompt is too large to maintain, too dense to follow, and adding more instructions makes it worse.

## Counter-Patterns

- [Map-Not-Manual](../patterns/map-not-manual.md) — keep the top-level instruction file short as a navigation map; put details in retrievable locations
- [Progressive Disclosure](../patterns/progressive-disclosure.md) — load detailed instructions only when the agent reaches a step that needs them
- [Just-in-Time Retrieval](../patterns/just-in-time-retrieval.md) — retrieve specific knowledge at the moment of need rather than preloading everything
- [Repository-as-System-of-Record](../patterns/repository-as-system-of-record.md) — let the repository structure itself communicate conventions

## Sources

- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Anthropic — [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
