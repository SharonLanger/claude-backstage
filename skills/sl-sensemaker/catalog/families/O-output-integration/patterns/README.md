# Family O — Output & Integration Boundaries: Patterns

6 patterns covering how model output safely enters deterministic software.

**Key insight:** Model output is untrusted input to downstream code. The output boundary is the last line of defense before unvalidated text reaches business logic, databases, APIs, or rendered surfaces. Sources: Anthropic, OpenAI, AWS, OWASP.

---

## Files

```
patterns/
├── README.md                       ← this file
├── structured-output-boundary.md   ← force the model to produce a declared machine-readable format at generation time
├── parse-and-reject.md             ← parse atomically; reject the entire output and invoke a fallback on any parse failure
├── schema-validation.md            ← validate parsed output against a declared schema before it reaches any downstream consumer
├── programmatic-postcondition.md   ← assert domain-level invariants on schema-valid output before business logic consumes it
├── sanitized-output-boundary.md    ← strip or escape output before it reaches any injection-capable sink
└── typed-result-object.md          ← wrap validated output in a typed domain object so downstream code never branches on raw text
```

---

## Schema

Every file in this folder follows the same structure:

| Section | What it contains |
|---|---|
| `# Name` | Canonical pattern name |
| `**Family / Intent / Also known as**` | Family O, one-sentence intent, alternate names |
| `## Problem` | The specific failure mode at the output boundary, including injection and partial-processing hazards |
| `## Solution` | The mechanism that makes output safe to consume downstream |
| `## Structure` | Mermaid diagram (in a `<details>` block) showing the boundary and control flow |
| `## Consequences` | What the pattern prevents, what it costs, and failure modes if misapplied |
| `## Known Uses` | Provider features, frameworks, or standards (Anthropic, OpenAI, OWASP) that apply the pattern |
| `## Related Patterns` | Cross-references within Family O and to other families |

---

## How to Navigate

**The patterns form a layered defense, applied in sequence:**

1. **Generation layer:** `structured-output-boundary` — constrain what the model can produce
2. **Parsing layer:** `parse-and-reject` — fail fast on malformed output, never partially process
3. **Structural layer:** `schema-validation` — enforce declared field types and shapes
4. **Semantic layer:** `programmatic-postcondition` — assert domain invariants schema alone cannot express
5. **Injection layer:** `sanitized-output-boundary` — escape before any injection-capable sink
6. **Consumption layer:** `typed-result-object` — wrap in a typed object so no downstream code touches raw text

**Each layer catches failures the previous layer cannot.** Schema validation catches structurally valid but semantically wrong output that parse-and-reject accepts. Sanitization applies even after schema validation passes, because a well-formed string can still contain injection payloads.

**Cross-family links:** Output failures that reach production generate traces in Family M. Eval infrastructure in Family D asserts output quality. Prompt design patterns that reduce malformed output probability live in Family B.
