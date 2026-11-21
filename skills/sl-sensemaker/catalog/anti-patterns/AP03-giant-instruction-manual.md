# AP03 — Giant Instruction Manual

## Symptoms

- The system prompt or instruction file exceeds thousands of tokens and keeps growing
- New edge cases are "fixed" by appending more instructions rather than restructuring
- The agent ignores rules that are buried deep in the context
- Contradictory instructions appear in different sections because nobody can track them all
- Performance degrades as the instruction payload grows — the model starts missing directives it used to follow
- The team's first response to any agent failure is "add a rule about that"

## Root Cause

Teams treat the system prompt as a growing specification document rather than a navigation map. Every failure gets patched with another instruction, creating a monotonically growing blob. The model's attention is finite — as the instruction surface grows, each individual directive gets less reliable attention. The underlying problem is that knowledge belongs in the repository, in tool descriptions, in structured documentation — not crammed into a single context window. The prompt should be a map that points to knowledge, not the knowledge itself.

## Failure Scenario

A code review agent starts with a 200-token system prompt and works well. Over six months, the team adds rules for every edge case: "Don't flag unused imports in test files," "Always suggest TypeScript strict mode," "Ignore line length in generated files," and 300 more directives. The prompt reaches 8,000 tokens. The agent now routinely violates rules from the middle of the document while reliably following the first and last sections. The team adds yet more instructions to compensate — "Remember to check rule #47 about generated files" — making the problem worse. Eventually the agent's behavior becomes unpredictable and the team considers replacing it entirely.

## Counter-Patterns

- [E06 — Map-Not-Manual](../families/E-context-engineering/patterns/map-not-manual.md) — Keep instructions short; point to structured documentation
- [E08 — Progressive Disclosure](../families/E-context-engineering/patterns/progressive-disclosure.md) — Load information only when needed for the current step
- [F06 — Structured Repository Instructions](../families/F-harness-environment/patterns/F06-structured-repository-instructions.md) — Organize instructions in the repository rather than the prompt
- [E05 — Just-in-Time Retrieval](../families/E-context-engineering/patterns/just-in-time-retrieval.md) — Retrieve relevant rules at the point of use

## Sources

- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Anthropic — [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
