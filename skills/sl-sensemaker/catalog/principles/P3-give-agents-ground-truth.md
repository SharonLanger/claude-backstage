# Principle 3 — Give Agents Ground Truth

> Execution results, tests, compiler output, tool results, and runtime evidence are more useful than asking the agent to imagine whether something worked.

## Why This Matters

A language model generating code or plans has no built-in mechanism to distinguish between output that works and output that merely looks plausible. Without ground truth — the actual result of running the code, the actual error message from the compiler, the actual response from an API — the model can only estimate correctness based on pattern matching against its training data. This estimation fails precisely on edge cases and novel situations where agents are most needed.

This principle emerged from the coding-agent community because the difference between agents that work and agents that hallucinate is almost entirely explained by access to execution feedback. Anthropic's agent architecture feeds tool results (compiler output, test results, runtime errors) back into the conversation as evidence. OpenAI's Codex harness runs code in a sandbox and returns real execution traces, treating the execution environment as the source of truth rather than the model's self-assessment. The pattern generalizes: any system where the agent receives real-world feedback outperforms one where the agent is asked to reason about hypothetical outcomes.

## Which Sources Converge

| Organization | How They Express This Principle |
|---|---|
| **Anthropic** | Agent loops feed tool execution results back as conversation context — the model sees real output, not imagined output |
| **OpenAI** | Codex harness provides sandboxed execution with real compiler/test output; harness engineering treats execution feedback as the primary signal |
| **OpenAI** | Symphony orchestration provides each agent with concrete execution results from prior steps |
| **Google Cloud** | Patterns include observation steps where the agent receives actual environment state |
| **AWS** | Agent patterns include tool execution results as evidence for next-step decisions |

## Patterns That Implement This Principle

- [Evidence-Based Completion](../families/D-verification-evaluation/patterns/D03-evidence-based-completion.md) — task is complete only when execution evidence confirms it
- [Repository-Local System of Record](../families/F-harness-environment/patterns/F02-repository-local-system-of-record.md) — the repo's actual state (tests, types, lint) is truth, not the agent's memory of what it did
- [Retry With Feedback](../families/I-reliability-recovery/patterns/retry-with-feedback.md) — retry includes the actual error, not just "try again"
- [External Durable State](../families/L-memory-state/patterns/external-durable-state.md) — persist real results to external storage so future steps use facts, not recalled impressions

## Anti-Patterns This Prevents

- **Giant Instruction Manual** — attempting to describe reality exhaustively in instructions rather than letting the agent observe reality through tools
- **Shared Context Everywhere** — passing forward stale summaries of what happened rather than fresh execution results

## Practical Application

1. **Run tests after every code change:** Instead of asking the model "does this code work?", execute the test suite and feed the results back. A failing test is unambiguous ground truth; the model's confidence about correctness is not.

2. **Return actual error messages:** When a tool call fails, return the full error message (stderr, stack trace, HTTP status) to the model. Don't summarize or filter — the model needs the raw signal to diagnose the problem correctly.

3. **Verify file state rather than trusting memory:** After an agent writes a file, read the file back and confirm its contents match intent. Models can hallucinate having made a change, or make a change that a formatter then reverts.

4. **Use compiler/type-checker output:** In typed languages, run the type checker after changes and feed violations back to the agent. Type errors are ground truth about interface mismatches that no amount of reasoning can replace.

## Sources

- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- OpenAI — [Unrolling the Codex Agent Loop](https://openai.com/index/unrolling-the-codex-agent-loop/)
- OpenAI — [Open-Source Codex Orchestration: Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/)
- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
