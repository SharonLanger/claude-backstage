# Designing Tools and Actions

## Scenario

You are building or extending an agent system and need to design the tools (functions, APIs, actions) that the agent can call. You want tools that are effective for the LLM to use, safe to execute, and maintainable over time.

## Quick Answer

1. **Design tools for the LLM, not for humans** — tool names, descriptions, and parameter schemas are the LLM's API documentation. Clarity here directly impacts agent performance. See [G-tool-action-design](../../families/G-tool-action-design/).
2. **Separate reads from writes** — reading is safe and reversible; writing has consequences. Different trust levels apply. See [J11-read-write-separation.md](../../families/J-security-trust/patterns/J11-read-write-separation.md).
3. **Return actionable information** — tool results should tell the agent what happened and what to do next, especially on failure. See [retry-with-feedback.md](../../families/I-reliability-recovery/patterns/retry-with-feedback.md).

## Tool Design Principles

### Naming and Description

| Principle | Why it matters |
|-----------|---------------|
| Verb-noun names (`search_files`, `create_issue`) | LLM can infer behavior from the name |
| One action per tool | Reduces ambiguity about what will happen |
| Description explains when to use, not just what it does | Helps the model choose the right tool |
| Parameters have clear types and descriptions | Reduces malformed calls |
| Required vs. optional is explicit | Prevents missing critical inputs |

### Granularity Decisions

| Approach | When to use | Tradeoff |
|----------|------------|----------|
| Fine-grained (many small tools) | Agent needs flexibility, task is exploratory | More tool calls, higher token cost |
| Coarse-grained (few powerful tools) | Task is well-understood, efficiency matters | Less flexibility, harder to debug |
| Composite (one tool does multi-step) | Common sequences that always go together | Hides complexity, less observable |

**Rule of thumb:** Start with fine-grained tools. Combine into coarse-grained only when you observe the agent repeatedly executing the same sequence.

### Safety Levels

Categorize every tool by its risk level:

| Level | Description | Example | Safeguard |
|-------|-------------|---------|-----------|
| Read-only | No state change | `search_files`, `get_status` | None required |
| Reversible write | Can be undone | `create_branch`, `write_draft` | Confirmation optional |
| Irreversible write | Cannot be undone | `delete_file`, `send_email` | Require confirmation |
| Destructive | Affects other systems/users | `deploy`, `push_to_prod` | Human approval gate |

Related pattern: [J01-least-privilege.md](../../families/J-security-trust/patterns/J01-least-privilege.md)

## Decision Guide: What Tools Does Your Agent Need?

### Step 1: Map the task to capabilities

| Task requires... | Tool category |
|-----------------|---------------|
| Finding information | Search, query, read tools |
| Creating content | Write, generate tools |
| Modifying state | Update, edit tools |
| Verifying results | Test, validate, check tools |
| Communicating | Send, notify tools |

### Step 2: Apply least privilege

For each tool, ask:
- Does the agent need this for its core task? (If no, remove it)
- Can this tool be scoped narrower? (e.g., `read_file` limited to a directory)
- What is the worst thing that could happen if the agent misuses this tool?

### Step 3: Design the return format

| Return style | When to use |
|--------------|-------------|
| Structured data (JSON) | Agent needs to process the result programmatically |
| Natural language summary | Agent needs to reason about the result |
| Status + data | Agent needs to know if it worked AND what happened |
| Error with guidance | On failure, tell the agent what went wrong and suggest fixes |

## Relevant Patterns

| Pattern | What it covers | Link |
|---------|---------------|------|
| G-tool-action-design (family) | All tool design patterns | [G-tool-action-design](../../families/G-tool-action-design/) |
| Least privilege | Expose minimum necessary tools | [J01-least-privilege.md](../../families/J-security-trust/patterns/J01-least-privilege.md) |
| Read-write separation | Different trust for read vs. write | [J11-read-write-separation.md](../../families/J-security-trust/patterns/J11-read-write-separation.md) |
| Retry with feedback | Return errors that help the agent recover | [retry-with-feedback.md](../../families/I-reliability-recovery/patterns/retry-with-feedback.md) |
| Schema validation | Validate tool inputs/outputs | [schema-validation.md](../../families/O-output-integration/patterns/schema-validation.md) |
| Structured output boundary | Clean interface between agent and tools | [structured-output-boundary.md](../../families/O-output-integration/patterns/structured-output-boundary.md) |
| Human-in-the-loop checkpoint | Gates for dangerous actions | [K01-human-in-the-loop-checkpoint.md](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) |
| Tool result reuse | Cache expensive tool results | [tool-result-reuse.md](../../families/N-efficiency-routing/patterns/tool-result-reuse.md) |

## Common Tool Design Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Ambiguous tool descriptions | Agent picks the wrong tool | Write descriptions that explain WHEN to use each tool |
| Too many tools at once | Agent confused, picks poorly | Start small, add tools only when needed |
| No error information in returns | Agent retries blindly | Return structured errors with actionable guidance |
| All-or-nothing permissions | Either too dangerous or too restrictive | Scope tools narrowly, use tiered permissions |
| Tools that require multi-step setup | Agent forgets intermediate state | Combine setup steps or manage state in the harness |
| String-typed everything | Model generates invalid inputs | Use enums, numbers, booleans where possible |

## Anti-Patterns to Watch For

- [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) — if tools do not return useful error info, the agent cannot improve on retry
- [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md) — combining tools for efficiency before understanding usage patterns

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
