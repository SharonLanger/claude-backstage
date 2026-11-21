# G — Tool & Action Design

**Recurring problem:** The model must translate ambiguous natural-language intent into safe, deterministic, side-effectful actions. Poorly designed tool interfaces amplify ambiguity, leak capability, and produce non-deterministic or unsafe behavior.

**Family scope:** How tool interfaces are designed, constrained, discovered, and validated so the model can act reliably on behalf of the user.

---

## Directory Tree

```
G-tool-action-design/
├── README.md                              ← this file (navigation hub)
│
├── patterns/
│   ├── G01-typed-schema-constrained-tool.md   ← enforce input types via schema; reject at boundary
│   ├── G02-narrow-tool-interface.md           ← one tool, one job; minimal parameters
│   ├── G03-tool-gateway.md                    ← single entry point that audits/routes all tool calls
│   ├── G04-agent-as-tool.md                   ← wrap a sub-agent behind a tool interface
│   ├── G05-read-write-separation.md           ← split read and mutating tools; never conflate
│   ├── G06-tool-gate.md                       ← require explicit approval before destructive execution
│   ├── G07-deterministic-tool-execution.md    ← eliminate randomness and side effects from tool logic
│   ├── G08-tool-result-validation.md          ← validate tool output before it re-enters the model
│   ├── G09-tool-discovery-progressive-exposure.md  ← reveal tools incrementally to match capability to context
│   └── G10-idempotent-action-wrapper.md       ← safe-to-retry wrapper; duplicate calls produce no extra effect
│
├── reference/
│   ├── tool-design-checklist.md          ← gate checklist before shipping a tool interface
│   └── tool-interface-antipatterns.md    ← common mistakes and their failure modes
```

---

## Per-Pattern File Schema

Every file under `patterns/` follows this structure:

```markdown
# G<nn> — <Pattern Name>

**Status:** draft | review | stable
**Related families:** <comma-separated family codes>
**Also see:** <links to other patterns in this family>

---

## Problem

<One paragraph: the specific failure mode this pattern addresses.>

## Context

<When does this pattern apply? What preconditions must hold?>

## Solution

<The core design decision. What structure or constraint solves the problem.>

## Structure

<Diagram (Mermaid) or numbered description of the components and their relationships.>

## Implementation Notes

<Concrete guidance: what to do, what to avoid, language/framework specifics where relevant.>

## Forces & Tradeoffs

| Force | Tension |
|-------|---------|
| <force> | <what you give up> |

## Examples

<Short concrete example: a tool schema snippet, a pseudocode interface, or a real-world analogy.>

## Verification

<How to confirm the pattern is correctly applied. Testable criteria.>

## Related Patterns

- **<Pattern>** — <one-line relationship>
```

Fields that must always be present: Problem, Solution, Forces & Tradeoffs, Related Patterns.
Fields that may be omitted if empty: Context, Structure, Examples, Verification.

---

## Tool Design Checklist

Use this before shipping any new tool interface. All items must pass.

### Interface Shape
- [ ] The tool has exactly one responsibility — no multi-purpose catch-all tools
- [ ] Every parameter has a declared type and schema constraint (enum, pattern, range, or object shape)
- [ ] Optional parameters have explicit defaults; no implicit fallback behavior
- [ ] Parameter names are unambiguous — no `data`, `input`, `payload` without qualification
- [ ] Read operations and write operations are in separate tools

### Safety
- [ ] Destructive or irreversible actions require a Tool Gate (explicit confirmation step)
- [ ] The tool is idempotent OR the caller is documented as responsible for deduplication
- [ ] The tool cannot be invoked with parameters that produce unbounded side effects (e.g., no `limit: null`)
- [ ] Sensitive parameters (credentials, PII) are never echoed back in tool results

### Determinism
- [ ] Given the same inputs, the tool produces the same outputs (or a documented narrow range)
- [ ] No hidden state or ambient globals affect tool behavior
- [ ] Errors are typed and structured — no free-text error strings the model must parse

### Validation
- [ ] Tool results are validated before re-entering the model context (see G08)
- [ ] Schema violations at input boundary are rejected with a structured error, not silently coerced
- [ ] Tool result size is bounded — large payloads are paginated or summarized

### Discovery
- [ ] The tool description is written for the model, not the developer
- [ ] The tool is only exposed when it is relevant to the current context (see G09)
- [ ] Tool names follow a consistent verb-noun convention across the interface set

---

## Common Tool Interface Mistakes

| Mistake | Why It Fails | Correct Pattern |
|---------|-------------|-----------------|
| One god-tool with a `mode` or `action` parameter | Forces the model to reason about internal routing; schema provides no guidance | G02 Narrow Tool Interface — split by responsibility |
| Free-text `query` parameter with no schema | Any string is valid; model cannot know what is safe or expected | G01 Typed/Schema-Constrained Tool — use enums or structured fields |
| Read and write in the same tool call | Model cannot express intent without side effects; hard to audit | G05 Read/Write Separation |
| No confirmation before destructive action | One hallucinated parameter causes irreversible damage | G06 Tool Gate |
| Tool result returned as unstructured prose | Model must re-parse its own tool output; introduces hallucination risk | G08 Tool Result Validation + structured return type |
| All tools always visible | Overwhelms context window; model picks wrong tool by proximity | G09 Tool Discovery / Progressive Exposure |
| Tool not idempotent + retry on failure | Retries double-charge, double-send, or double-write | G10 Idempotent Action Wrapper |
| Sub-agent invoked inline as a function | No interface contract; model cannot reason about latency or failure modes | G04 Agent-as-Tool |
| Exposing the full API surface through one gateway | Gateway becomes a pass-through with no enforcement | G03 Tool Gateway — gateway must enforce policy, not just route |
| Silent coercion of invalid input | Model receives success signal for malformed input; errors propagate silently | Reject at boundary with a typed error (G01) |

---

## Family Relationships

| Family | Relationship to G |
|--------|------------------|
| **F — Harness** | The harness provides the execution environment in which tools are registered and invoked |
| **H — Deterministic Control** | Tool outputs feed into deterministic checks; G07 and H patterns are complementary |
| **J — Security** | Tool Gateway (G03) and Read/Write Separation (G05) are also security boundary patterns |
| **O — Output** | Tool results are model outputs; G08 (Tool Result Validation) mirrors O-family output validation |

---

Last updated: 2026-08-24
