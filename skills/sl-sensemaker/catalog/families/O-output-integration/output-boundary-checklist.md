# Guide: Output Boundary Checklist

## Purpose

Use this checklist at every point where model-generated output enters deterministic code — API responses, function calls, database writes, UI rendering, file writes, or downstream system inputs. Each boundary is an opportunity for malformed, unexpected, or adversarial content to break your system.

## The Core Principle

Model output is untrusted input. Treat it with the same rigor you would treat user input in a web application: validate, sanitize, constrain, and handle failures gracefully.

---

## Checklist: For Every Output Boundary

### 1. Schema Validation

- [ ] Output is validated against a strict schema (JSON Schema, Zod, Pydantic, etc.) before use
- [ ] The schema defines: required fields, field types, allowed values, string lengths, numeric ranges
- [ ] Unknown/extra fields are rejected (not silently ignored)
- [ ] Nested structures are validated recursively
- [ ] Validation errors produce structured error messages (not just "invalid")

### 2. Type Coercion and Parsing

- [ ] String-to-number conversions handle NaN, Infinity, and extremely large values
- [ ] Date parsing handles invalid formats, impossible dates, and timezone ambiguity
- [ ] Boolean parsing handles the model's tendency to say "yes"/"no"/"true"/"True"/1/0
- [ ] Enum values are checked against the allowed set (not just type-checked)
- [ ] Arrays have maximum length limits enforced

### 3. Content Safety

- [ ] String outputs are sanitized for the target context (HTML-escaped for web, SQL-parameterized for queries)
- [ ] Code outputs are never executed directly without sandboxing
- [ ] File paths are validated against an allowlist (no path traversal: `../`)
- [ ] URLs are validated against allowed domains (no SSRF via model-generated URLs)
- [ ] Command-line arguments are escaped or validated against allowlists

### 4. Size and Resource Limits

- [ ] Maximum output length is enforced BEFORE downstream processing
- [ ] Output that exceeds limits is truncated or rejected (not buffered indefinitely)
- [ ] Nested structures have maximum depth limits
- [ ] Arrays and repeated elements have maximum count limits
- [ ] Total response size cannot exhaust memory

### 5. Failure Handling

- [ ] Schema validation failure triggers a retry with feedback (not a hard crash)
- [ ] Maximum retry count is defined (no infinite retry loops)
- [ ] After max retries, a sensible default or human escalation occurs
- [ ] Partial output is handled explicitly (what if the model stops mid-JSON?)
- [ ] Timeout is defined for output generation (what if the model hangs?)

### 6. Downstream Protection

- [ ] The consuming system has its own input validation (defense in depth)
- [ ] Database writes use parameterized queries regardless of output validation
- [ ] UI rendering escapes model output regardless of prior sanitization
- [ ] File writes go to a restricted directory with size limits
- [ ] API calls constructed from model output use allowlisted endpoints only

---

## Boundary Inventory Template

For each agent system, document every output boundary:

| # | Boundary | Output Type | Consuming System | Validation Method | Failure Action |
|---|----------|-------------|-----------------|-------------------|----------------|
| 1 | Agent → API response | JSON | Client application | JSON Schema + Zod | Return error + retry |
| 2 | Agent → Database | SQL params | PostgreSQL | Parameterized query | Log + skip record |
| 3 | Agent → File system | Code file | Build system | Path allowlist + size limit | Reject + escalate |
| 4 | Agent → External API | HTTP request | Third-party service | URL allowlist + payload schema | Block + log |
| 5 | Agent → UI | Text/HTML | Browser | HTML escape + CSP | Render escaped |

---

## Common Boundary Types and Their Specific Risks

### JSON Output → Application Code

| Risk | Example | Mitigation |
|------|---------|-----------|
| Missing required field | Model omits `id` field | Schema validation with `required` |
| Wrong type | `"count": "five"` instead of `"count": 5` | Strict type checking |
| Injection via string value | `"name": "<script>alert(1)</script>"` | Context-appropriate escaping |
| Extremely long string | 100KB in a field expected to be 50 chars | `maxLength` in schema |
| Unexpected null | `"result": null` when code assumes non-null | Explicit null handling |

### Function/Tool Call Arguments → Execution

| Risk | Example | Mitigation |
|------|---------|-----------|
| Invalid argument type | String where number expected | Type validation before execution |
| Out-of-range value | `delete_records(limit=999999)` | Range validation, conservative defaults |
| Injection in arguments | `filename: "; rm -rf /"` | Argument sanitization, no shell interpolation |
| Non-existent function | Model invents a tool name | Validate against registered tool list |
| Extra arguments | Model adds arguments the tool does not accept | Strict argument matching |

### Natural Language → Structured Decision

| Risk | Example | Mitigation |
|------|---------|-----------|
| Ambiguous response | "Maybe" when yes/no is required | Constrain output format; retry on ambiguity |
| Explanation instead of answer | Model explains rather than deciding | Parse structure; extract decision token |
| Multiple answers | Model gives three options when one is needed | Take first; or reject and retry |
| Refusal disguised as answer | "I can't do that" treated as content | Detect refusal patterns |

---

## Quick Decision: Do I Need a Boundary Check Here?

```
Does model output flow into this component?
│
├── YES: Is the component deterministic code (not another model)?
│   │
│   ├── YES → You need a boundary check. Use this checklist.
│   │
│   └── NO (another model) → You need format validation but not security sanitization.
│
└── NO → Not an output boundary (this is internal model reasoning).
```

## Related Patterns

- [Common Output Parsing Failures](common-output-parsing-failures.md) — reference for what goes wrong at these boundaries
- [O patterns](patterns/) — specific patterns for output validation and integration

## Sources

- OpenAI — [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
