# Reference: Never in a Prompt

## Purpose

This is a reference list of things that should NEVER be enforced only via prompting. Each item on this list must have a deterministic enforcement mechanism (code, validator, gate, hook, or infrastructure) regardless of whether it also appears in the prompt.

The prompt can remind the model of these rules. But the prompt must never be the ONLY thing preventing violation.

---

## The Principle

> A rule that matters when violated must be enforced by something that cannot be probabilistically ignored.

Prompts are probabilistic instructions. Given enough inputs, enough context variation, and enough turns, any prompt-only rule will eventually be violated. For items on this list, that violation has unacceptable consequences.

---

## Category 1: Security and Authorization

These items concern who can do what. Violations lead to unauthorized access, data breach, or privilege escalation.

| Never Enforce Only via Prompt | Why | Enforce With |
|---|---|---|
| Authentication checks | Model may skip checks under prompt injection or complex context | Auth middleware, token validation |
| Authorization / RBAC | Model cannot reliably evaluate permissions across all edge cases | Permission check in code before action |
| Secret/credential handling | Model may echo, log, or include secrets in output | Secret manager, environment variables never in context |
| Input sanitization | Model cannot catch all injection vectors | Input validation library, parameterized queries |
| Rate limiting | Model has no concept of request frequency | Server-side rate limiter |
| Tenant isolation | Model may confuse tenant boundaries in multi-tenant context | Database-level row isolation, query scoping |
| PII redaction in output | Model may include PII when instructed not to | Output filter/redactor |

---

## Category 2: Data Integrity

These items concern correctness of data operations. Violations lead to corruption, loss, or inconsistency.

| Never Enforce Only via Prompt | Why | Enforce With |
|---|---|---|
| Schema compliance of writes | Model may produce invalid data structures | Schema validator before write |
| Foreign key / referential integrity | Model cannot track all relationships | Database constraints |
| Idempotency of operations | Model may re-execute side-effecting operations | Idempotency keys, deduplication |
| Transaction boundaries | Model has no concept of atomicity | Database transactions in code |
| Backup before destructive operations | Model may forget or skip | Automated pre-operation backup |
| Data type validation | Model may pass string where number is expected | Type checking at system boundaries |

---

## Category 3: Process and Workflow

These items concern ordering and gating of steps. Violations lead to skipped steps, invalid states, or irreversible actions without checkpoints.

| Never Enforce Only via Prompt | Why | Enforce With |
|---|---|---|
| Required approval before deployment | Model may rationalize skipping approval | Programmatic gate that blocks deploy without approval token |
| Test execution before commit | Model may "forget" to run tests when confident | Pre-commit hook that blocks without passing tests |
| Step ordering in critical workflows | Model may reorder steps for "efficiency" | State machine that only allows valid transitions |
| Confirmation before destructive actions | Model may execute destructive actions without pausing | Tool gating that requires explicit confirmation parameter |
| Cooldown periods between retries | Model may retry immediately and repeatedly | Retry logic with programmatic backoff |

---

## Category 4: Output Constraints

These items concern the format or content of what the system produces. Violations lead to broken integrations, security issues, or compliance failures.

| Never Enforce Only via Prompt | Why | Enforce With |
|---|---|---|
| Output format (JSON, XML, etc.) | Model may produce malformed output | Output parser with retry on failure |
| Maximum output length | Model may exceed token budget | Hard truncation or length validation |
| No executable code in user-facing output | Model may produce code when tricked | Output sanitizer / code block stripper |
| Required fields in structured output | Model may omit fields | Schema validation on output |
| Language/encoding of output | Model may switch languages or encodings | Output validator |
| No internal system details in user-facing output | Model may leak tool names, prompts, or system architecture | Output filter |

---

## Category 5: Resource and Cost

These items concern consumption of finite resources. Violations lead to cost overruns, outages, or denial of service.

| Never Enforce Only via Prompt | Why | Enforce With |
|---|---|---|
| Maximum number of tool calls per turn | Model may enter infinite loops | Hard loop counter in harness |
| Maximum tokens consumed per request | Model may consume entire budget on one task | Token budget enforcement in orchestrator |
| Maximum concurrent operations | Model may spawn unlimited parallel work | Concurrency limiter |
| API call budget | Model has no cost awareness | Budget tracking with hard cutoff |
| Timeout on long-running operations | Model may wait indefinitely | Timeout enforcement in harness |

---

## How to Use This List

1. **For new systems:** Review each category. For every item that applies, confirm a deterministic enforcement mechanism exists BEFORE going to production.

2. **For existing systems:** Audit your prompt/instructions for rules on this list. For each one found only in the prompt, add deterministic enforcement.

3. **For security reviews:** This list serves as a minimum checklist of what must be mechanically enforced.

---

## The Prompt's Role

The prompt still has a role for items on this list:
- It explains WHY the rule exists (so the model cooperates rather than resists)
- It provides the model's "first line of defense" (reducing how often the deterministic enforcement is triggered)
- It helps the model produce outputs that pass validation on the first try (reducing retries)

But the prompt is the belt. The deterministic enforcement is the suspenders. Wear both.

---

## Related Patterns

- [H01 — Deterministic Override](patterns/H01-deterministic-override.md) — code always wins over model for these decisions
- [H02 — Programmatic Gate](patterns/H02-programmatic-gate.md) — blocking invalid workflow transitions
- [H04 — Policy Hook](patterns/H04-policy-hook.md) — running policy checks before/after actions
- [H06 — Schema Validator](patterns/H06-schema-validator.md) — validating structured output
- [H07 — Authorization Outside Model](patterns/H07-authorization-outside-model.md) — auth must never be model-only

---

## Sources

- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
