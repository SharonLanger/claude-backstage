# Guide: Tool Design Checklist

## Purpose

Use this checklist when designing a new tool interface that an agent will call. A well-designed tool reduces agent errors, eliminates ambiguity, and makes the agent's job easier. A poorly-designed tool becomes a source of persistent failures that no amount of prompt engineering can fix.

---

## Pre-Design Questions

Answer these before writing any tool specification.

| # | Question | Your Answer |
|---|---|---|
| 1 | What is the single responsibility of this tool? (one sentence) | |
| 2 | What would an agent need to know to decide WHEN to call this tool? | |
| 3 | What would an agent need to know to decide WHAT to pass as parameters? | |
| 4 | What does success look like? (What does the tool return on success?) | |
| 5 | What does failure look like? (What errors can occur and how are they reported?) | |
| 6 | Is this tool read-only or does it mutate state? | |
| 7 | Is this tool idempotent? (Can it be safely retried?) | |
| 8 | What is the blast radius if the agent calls this tool incorrectly? | |

---

## Design Checklist

### Naming and Description

- [ ] **Name is a verb-noun pair** that describes the action (e.g., `read_file`, `search_code`, `create_branch` — not `file`, `code`, `branch`)
- [ ] **Description explains WHEN to use it**, not just what it does ("Use this to read file contents when you need to understand existing code" — not just "Reads a file")
- [ ] **Description states what it does NOT do** if there are common confusions ("This reads files, not directories. Use list_directory for directories.")
- [ ] **Name is distinguishable** from other tools in the set (no two tools with overlapping names or purposes)

### Parameters

- [ ] **Every parameter has a description** that explains what value to pass and in what format
- [ ] **Required vs. optional is explicit** — required parameters are clearly marked
- [ ] **Types are as constrained as possible** — use enums for fixed choices, not free-text strings
- [ ] **Defaults are documented** — if a parameter has a default, say what it is
- [ ] **No parameter does double duty** — each parameter controls one thing
- [ ] **File paths are absolute** — if the tool takes paths, specify whether relative or absolute is expected
- [ ] **No implicit coupling** — parameter A's valid values don't depend on parameter B's value (or if they do, document it)

### Output

- [ ] **Success output is structured** — JSON or clearly parseable, not free-text prose
- [ ] **Error output is actionable** — says what went wrong AND what to do about it
- [ ] **Partial success is distinguishable from full success** — if the tool can partially complete, the output makes this clear
- [ ] **Output size is bounded** — the tool does not return unbounded data that could overflow the context window
- [ ] **Empty results are explicit** — returning nothing is distinguishable from returning "no matches found"

### Safety

- [ ] **Read vs. write is declared** — the agent (and user) knows if this tool mutates state
- [ ] **Destructive actions require confirmation** — or are gated behind a separate approval mechanism
- [ ] **Scope is minimal** — the tool does not have access to more resources than it needs
- [ ] **Inputs are validated** — malformed inputs return clear errors, not undefined behavior
- [ ] **Rate limiting or quota** — if the tool calls an external API, it handles rate limits gracefully

### Discoverability

- [ ] **The tool is useful without reading source code** — description + parameter docs are sufficient
- [ ] **Examples are provided** for non-obvious usage ("Example: search_code({query: 'function handleAuth', language: 'typescript'})")
- [ ] **Edge cases are documented** — what happens with empty input, very large input, special characters

---

## Tool Specification Template

```
Name: [verb_noun]
Description: [1-2 sentences: when to use this tool and what it does]

Parameters:
  - name: [parameter_name]
    type: [string | number | boolean | enum | array | object]
    required: [true | false]
    description: [what to pass and in what format]
    default: [value, if any]
    constraints: [min/max, allowed values, format rules]

Returns:
  - On success: [structure and fields]
  - On error: [error format and common error codes]
  - On partial success: [how to identify]

Side effects: [none | list of mutations]
Idempotent: [yes | no]
Rate limits: [if applicable]

Example:
  Input: { ... }
  Output: { ... }
```

---

## Related Patterns

- [G01 — Typed Schema-Constrained Tool](../patterns/G01-typed-schema-constrained-tool.md) — enforcing types on tool interfaces
- [G02 — Narrow Tool Interface](../patterns/G02-narrow-tool-interface.md) — keeping tools focused on one responsibility
- [G05 — Read-Write Separation](../patterns/G05-read-write-separation.md) — separating observation from mutation
- [G06 — Tool Gate](../patterns/G06-tool-gate.md) — gating dangerous tool calls
- [G09 — Tool Discovery / Progressive Exposure](../patterns/G09-tool-discovery-progressive-exposure.md) — revealing tools as needed

---

## Sources

- AWS — [MCP Tool Scope Strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html)
- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- OpenAI — [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
