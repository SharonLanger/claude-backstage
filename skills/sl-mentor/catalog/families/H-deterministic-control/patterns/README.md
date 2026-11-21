# Family H — Deterministic Control Boundaries: Patterns

8 patterns covering how to enforce must-hold rules in code rather than prompts. The core principle: if a property can be checked deterministically, do not rely solely on probabilistic model obedience. These patterns directly address the **Prompt-as-Policy** anti-pattern.

---

## File Tree

```
patterns/
├── README.md                        ← this file
├── H01-deterministic-override.md    ← replace model output when a rule is violated
├── H02-programmatic-gate.md         ← block execution when output fails a hard check
├── H03-structural-test.md           ← assert invariants with automated tests, not prompts
├── H04-policy-hook.md               ← inject policy enforcement at a defined hook point
├── H05-typed-boundary.md            ← use type systems to reject ill-formed model output
├── H06-schema-validator.md          ← validate model output against a schema before use
├── H07-authorization-outside-model.md ← enforce authz in code, never inside the model
└── H08-non-ai-fallback-path.md      ← maintain a deterministic fallback when AI is absent
```

---

## File Descriptions

| File | What it covers |
|------|----------------|
| H01-deterministic-override.md | Post-inference step that unconditionally replaces model output when a rule applies — treats model output as a suggestion, the override as the final decision |
| H02-programmatic-gate.md | Hard check that blocks downstream execution when output fails; use when there is no safe substitute value (complement to H01) |
| H03-structural-test.md | Automated tests that assert invariants on model output; moves rule enforcement out of the prompt and into the test suite |
| H04-policy-hook.md | Named hook point in the pipeline where policy rules are injected; separates policy logic from inference logic |
| H05-typed-boundary.md | Use of static types or typed data structures to make ill-formed model output a compile-time or parse-time error |
| H06-schema-validator.md | Runtime schema validation (JSON Schema, Pydantic, etc.) applied to model output before it reaches any consumer |
| H07-authorization-outside-model.md | Authorization decisions made in code, not prompted; the model never decides what a user is allowed to do |
| H08-non-ai-fallback-path.md | A fully deterministic path that handles the case when AI is unavailable, misconfigured, or returns unusable output |

---

## Schema

Every pattern file follows this structure:

| Section | Contents |
|---------|----------|
| Title + one-line summary | `# HXX — Name` followed by a bold one-liner |
| Problem | What goes wrong without this pattern; why the prompt-only approach fails |
| Solution | The deterministic mechanism that fixes it |
| Solution Structure | Mermaid control-flow diagram in a `<details>` block |
| When to Use | Conditions under which this pattern applies |
| When NOT to Use | Conditions where it would be wrong or harmful |
| Implementation Notes | Concrete guidance: logging, side effects, ordering, edge cases |
| Related Patterns | Cross-links to other H-family patterns with brief contrast |
| Related Families | Cross-links to patterns in other families that operate in the same layer |
| Example | Before/after showing the Prompt-as-Policy failure and the deterministic fix |
| Sources | AWS, OpenAI, and/or Anthropic citations with URLs |

---

## How to Navigate

**"What is the difference between H01 and H02?"** — H01 replaces bad output silently; H02 blocks execution entirely. Use H01 when a safe substitute exists, H02 when there is none.

**"Where does authorization belong?"** — H07. It is the only pattern in this family solely about access control.

**"I want to catch bad output before it reaches any consumer."** — H05 (type boundary) and H06 (schema validator) act at the parse/validation layer. H02 (gate) acts at the execution layer.

**"I need a safety net if the whole AI path is broken."** — H08.

**Finding related work outside this family:** Every file's "Related Families" section links outward. Family D (Verification) detects invalid output; Family O (Output) shapes output in the same post-inference layer.

---

Last updated: 2026-08-24
