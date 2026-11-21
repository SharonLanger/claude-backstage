# Family O — Output & Integration Boundaries

**Recurring problem:** Natural-language model output must safely enter deterministic software systems.

**Core insight:** Model output is untrusted input to downstream code. The output boundary is the last line of defense before probabilistic output enters deterministic systems. Every pattern in this family is a different strategy for enforcing that boundary.

---

## Directory Tree

```
O-output-integration/
├── README.md                              ← this file (navigation + checklists)
├── patterns/
│   ├── structured-output-boundary.md     ← force structured format at generation time
│   ├── schema-validation.md              ← validate generated output against a schema
│   ├── typed-result-object.md            ← wrap parsed output in a typed domain object
│   ├── parse-and-reject.md               ← parse output; reject and retry on failure
│   ├── programmatic-postcondition.md     ← assert invariants on the result after parsing
│   └── sanitized-output-boundary.md      ← strip/escape model output before use in sinks
├── output-boundary-checklist.md          ← (referenced inline below)
└── common-output-parsing-failures.md     ← (referenced inline below)
```

---

## Per-Pattern File Schema

Every file under `patterns/` follows this structure:

```markdown
# Pattern Name

**Family:** O — Output & Integration Boundaries
**Intent:** One-sentence statement of what the pattern does.
**Also known as:** Alternate names, if any.

## Problem
The forces at play — what goes wrong without this pattern.

## Solution
The structural solution: what you build and where it sits.

## Structure
Diagram or pseudo-code showing the pattern shape.

## Participants
The roles involved (model, output boundary, validator, downstream consumer, etc.).

## Implementation Notes
Concrete guidance — language-agnostic where possible, with examples.

## Consequences
What you gain and what you give up.

## Related Patterns
Cross-references within O and to other families (H, G, J, D).

## When to Use / When Not to Use
Decision criteria.
```

---

## Output Boundary Checklist

Use before any code path that receives model output and passes it to a deterministic system.

| # | Check | Why |
|---|-------|-----|
| 1 | Output format is declared in the prompt (JSON, XML, enumerated value, etc.) | Structured Output Boundary — don't parse what was never requested in a defined shape |
| 2 | Output is parsed into an explicit intermediate representation before use | Typed Result Object — never pass raw strings into business logic |
| 3 | Schema or type constraints are validated immediately after parsing | Schema Validation — catch structural failures at the boundary, not deep inside |
| 4 | The parser rejects and does not partially process malformed output | Parse-and-Reject — partial processing of malformed output is a common bug class |
| 5 | Retry / fallback behavior is defined for rejection | Parse-and-Reject — the caller must know what happens on failure |
| 6 | Post-parse invariants are asserted programmatically | Programmatic Postcondition — schema-valid does not mean semantically correct |
| 7 | Output is sanitized before use in injection-capable sinks (SQL, HTML, shell, filesystem) | Sanitized Output Boundary — schema-valid output can still contain injection payloads |
| 8 | Downstream code does not branch on raw model text; it branches on typed values | Typed Result Object — raw-string branching couples logic to model phrasing |
| 9 | Output boundary errors are logged with the raw model response preserved | Debugging — parsed-only logs make root-cause analysis impossible |
| 10 | The boundary is unit-testable with injected model responses | Any of the O patterns — verify the boundary in isolation, without a live model |

---

## Common Output Parsing Failures

| Failure Mode | Description | Pattern That Addresses It |
|---|---|---|
| Free-form prose instead of structured output | Model ignores format instruction and returns natural language | Structured Output Boundary |
| Partial JSON / truncated output | Output cut off mid-structure due to token limits | Parse-and-Reject + caller checks finish reason |
| Extra wrapper text around JSON | Model outputs "Here is the result: `{...}`" instead of bare JSON | Structured Output Boundary (strict mode), Parse-and-Reject |
| Field name hallucination | Model invents field names not in the requested schema | Schema Validation |
| Type coercion errors | Number fields returned as strings; boolean returned as "yes"/"no" | Schema Validation, Typed Result Object |
| Missing required fields | Model omits fields it judges irrelevant | Schema Validation (required field enforcement) |
| Semantic constraint violation | Output is schema-valid but violates a business rule (e.g. end < start) | Programmatic Postcondition |
| Injection payload in structured field | SQL/HTML/shell metacharacters in a "safe" output field | Sanitized Output Boundary |
| Nested structure depth mismatch | Model flattens or over-nests arrays/objects | Schema Validation |
| Enum value not in allowed set | Model returns a plausible but unlisted enumeration value | Schema Validation, Parse-and-Reject |
| Numeric range overflow | Model outputs values outside expected domain (e.g. probability > 1) | Programmatic Postcondition |
| Silent partial match | Parser extracts a substring and succeeds; the rest is silently dropped | Parse-and-Reject (total parse, no substring extraction) |

---

## Related Families

| Family | Relationship to O |
|--------|------------------|
| **H — Deterministic Control** | Schema validator is both an H pattern (hard gate in control flow) and an O pattern (output boundary enforcement) |
| **G — Tool Design** | Tool result validation is an O pattern applied to tool outputs; typed tool results mirror Typed Result Object |
| **J — Security** | Sanitized Output Boundary is the O-side enforcement of injection prevention; J covers the broader threat model |
| **D — Verification** | The deterministic validator (first rung of D's verification ladder) is instantiated as Schema Validation or Programmatic Postcondition in O |

---

Last updated: 2026-08-24
