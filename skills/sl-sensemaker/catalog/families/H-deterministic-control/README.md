# Family H — Deterministic Control Boundaries

**Recurring problem:** Must-hold rules are encoded in prompts even though they can be enforced mechanically.

**Core rule:** If a property can be checked deterministically, do not rely solely on probabilistic obedience.

**Anti-pattern addressed:** Prompt-as-Policy — using a prompt instruction as the sole enforcement mechanism for a rule that must always hold.

---

## Directory Tree

```
H-deterministic-control/
├── README.md                          ← this file (navigation hub)
├── decision-guide.md                  ← "Should this be code or a prompt?" flowchart + rules
├── never-in-a-prompt.md               ← reference: properties that must never be prompt-only
└── patterns/
    ├── H01-deterministic-override.md  ← model output overridden by code rule, unconditionally
    ├── H02-programmatic-gate.md       ← hard code check before action is allowed to proceed
    ├── H03-structural-test.md         ← automated test asserts a must-hold invariant
    ├── H04-policy-hook.md             ← pluggable enforcement hook evaluated outside the model
    ├── H05-typed-boundary.md          ← static types eliminate an entire class of invalid states
    ├── H06-schema-validator.md        ← runtime schema check at the input or output boundary
    ├── H07-authorization-outside-model.md  ← authz decisions made by code, never by model
    └── H08-non-ai-fallback-path.md    ← deterministic fallback when AI path cannot be trusted
```

---

## Per-Pattern File Schema

Each engineering entry in `patterns/` follows this structure exactly:

```
# H<nn> — <Pattern Name>

**One-line summary:** <what it does in ≤ 15 words>

## Problem
<2–4 sentences: what breaks when this pattern is absent>

## Solution
<The mechanical enforcement mechanism. What code/schema/test does the checking.>

## Structure
<Minimal pseudo-code or diagram showing the enforcement point>

## When to Use
- <condition>
- <condition>

## When NOT to Use
- <condition>

## Implementation Notes
<Pitfalls, edge cases, language/framework-specific notes>

## Related Patterns
- <pattern id + name>: <one-line relationship>

## Related Families
- <family letter + name>: <why this pattern overlaps>

## Example
<Concrete before/after or code snippet showing the pattern in action>
```

---

## Should This Be Code or a Prompt?

Full flowchart and decision rules: [`decision-guide.md`](decision-guide.md)

**Quick heuristic:**

| Ask yourself | Code if… | Prompt if… |
|---|---|---|
| Can a test assert this? | Yes — write the test | No observable output to assert |
| Does it need to hold 100% of the time? | Yes — code/schema/gate | Acceptable to hold ~95% |
| Is the rule structural (type, range, format)? | Yes — type or schema | No — it's nuanced/contextual |
| Is it a security or authz decision? | Always code | Never |
| Would a bug here be a security incident? | Always code | Never |
| Does it require business logic judgment? | Probably prompt | Possibly code |

---

## Never Trust the Model to Enforce These

Full reference: [`never-in-a-prompt.md`](never-in-a-prompt.md)

**Summary list:**

- **Authorization** — who may call what, what a user may see or modify
- **Data isolation** — tenant separation, PII scope, row-level access
- **Rate limiting and quotas** — always enforce in middleware, never by asking the model to refuse
- **Idempotency** — deduplication keys, exactly-once semantics
- **Schema conformance** — required fields, value ranges, enum membership, foreign key validity
- **Immutable audit records** — append-only logs must be protected by code, not intent
- **Cryptographic operations** — signing, verification, key handling
- **Irreversible side effects** — delete, publish, charge; gate must be code
- **Regulatory / legal constraints** — GDPR erasure, export controls, retention limits
- **Safety shutoffs** — hard stop on resource consumption, loop limits, recursion depth

---

## Related Families

| Family | Relationship |
|---|---|
| **J — Security** | `H07-authorization-outside-model` belongs to both; see J for the full security threat model |
| **O — Output** | `H06-schema-validator` applied at the output boundary is an O-family concern; both families claim it |
| **D — Verification** | A deterministic validator (H02, H03) is the cheapest verification step; D covers richer verification strategies |
| **G — Tool Gate** | A tool gate is a deterministic control point at the tool interface — H02 in the tool-use context |

---

Last updated: 2026-08-24
