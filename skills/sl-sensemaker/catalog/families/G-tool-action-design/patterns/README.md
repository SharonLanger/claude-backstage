# Family G — Tool & Action Design: Patterns

10 patterns covering how tool interfaces are designed for safe, deterministic model actions.

**Core insight (AWS):** Tool interfaces should be designed for the LLM, not simply expose every underlying API. The model's ability to use a tool correctly depends almost entirely on how that tool is defined — its scope, schema, error responses, and the semantics the name and description communicate.

---

## File Tree

```
patterns/
├── README.md                              ← this file
├── G01-typed-schema-constrained-tool.md   ← declare strict parameter schemas; reject invalid calls at the boundary
├── G02-narrow-tool-interface.md           ← give each tool one job; don't expose broad APIs directly
├── G03-tool-gateway.md                    ← route all tool calls through a single controlled dispatch layer
├── G04-agent-as-tool.md                   ← expose a sub-agent as a callable tool to a parent agent
├── G05-read-write-separation.md           ← separate read tools from write tools; different safety treatment
├── G06-tool-gate.md                       ← require explicit approval before irreversible tool actions execute
├── G07-deterministic-tool-execution.md    ← make tool results reproducible given the same inputs
├── G08-tool-result-validation.md          ← validate tool outputs before returning them to the model
├── G09-tool-discovery-progressive-exposure.md ← surface tools incrementally; don't overwhelm with a full catalog
└── G10-idempotent-action-wrapper.md       ← wrap actions so repeated calls produce the same result safely
```

---

## Schema

Each engineering pattern follows the same structure:

| Section | Contents |
|---|---|
| `# GNN — Title` | Pattern name with family-scoped number |
| `**Status:**` + `**Related families:**` + `**Also see:**` | Front-matter: stability, cross-family links, sibling patterns |
| `## Problem` | The failure mode this pattern addresses — concrete, specific |
| `## Context` | Conditions under which the pattern is most relevant |
| `## Solution` | What to do instead — the core intervention |
| `## Structure` | Mermaid diagram (collapsible) showing the execution or validation flow |
| `## Implementation Notes` | Concrete guidance on how to apply the pattern |
| `## Forces & Tradeoffs` | Two-column table: Force vs. Tension |
| `## Examples` | Pseudocode or concrete scenario illustrating the pattern |
| `## Verification` | Test cases to confirm the pattern is correctly implemented |
| `## Related Patterns` | Cross-links with one-line explanation of the relationship |
| `## Sources` | Attributed sources with organization, role, and URL |

---

## How to Navigate

**By problem type:**
- Model produces invalid or out-of-range parameter values → [G01](G01-typed-schema-constrained-tool.md)
- Tool exposes too much surface area; model uses it incorrectly → [G02](G02-narrow-tool-interface.md)
- No single point of control over what tools can be called → [G03](G03-tool-gateway.md)
- Orchestrator needs to delegate a complex sub-task to another agent → [G04](G04-agent-as-tool.md)
- Reads and destructive writes treated with equal permissiveness → [G05](G05-read-write-separation.md)
- Irreversible actions execute without any pause for confirmation → [G06](G06-tool-gate.md)
- Same tool call produces different results on retry → [G07](G07-deterministic-tool-execution.md)
- Tool returns malformed or unexpected output; model hallucinates around it → [G08](G08-tool-result-validation.md)
- Model paralyzed or confused by too many available tools → [G09](G09-tool-discovery-progressive-exposure.md)
- Retried or replayed actions cause duplicate side effects → [G10](G10-idempotent-action-wrapper.md)

**Patterns that commonly pair together:**
- G01 + G08 (schema validates inputs; result validation validates outputs — both needed for a safe boundary)
- G05 + G06 (read/write separation identifies which tools need a gate; G06 applies it)
- G02 + G09 (narrow tools produce a larger catalog; progressive exposure manages its size)
- G07 + G10 (deterministic execution + idempotent wrappers — both reduce unpredictable side effects)

Last updated: 2026-08-24
