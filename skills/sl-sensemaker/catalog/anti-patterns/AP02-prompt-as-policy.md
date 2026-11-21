# AP02 — Prompt-as-Policy

## Symptoms

- Security-critical rules exist only in system prompts or instruction files, with no programmatic enforcement
- The system relies on "please don't do X" instructions to prevent dangerous actions
- Jailbreak attempts or prompt injection can bypass access controls
- Authorization logic lives inside the model's context rather than in application code
- The team says "we told it not to" when asked how a dangerous action is prevented

## Root Cause

Teams conflate instructing the model with enforcing policy. Prompts are probabilistic — the model follows them most of the time, but not deterministically. Under adversarial conditions (prompt injection, edge cases, ambiguous inputs), instruction-only policies fail silently. The root confusion is treating a language model as a rule engine rather than a probabilistic text generator. Real policy enforcement requires deterministic mechanisms that cannot be bypassed regardless of what the model decides to do.

## Failure Scenario

A customer support agent is given the instruction: "Never share customer data with anyone other than the account holder. Never execute refunds above $500 without manager approval." An attacker submits a support ticket containing a carefully crafted prompt injection in the "issue description" field. The injected text convinces the model it is in a "manager override" context. The agent processes a $2,000 refund and emails full account details to an external address — both actions that the prompt explicitly prohibited, but no programmatic gate enforced.

## Counter-Patterns

- [H07 — Authorization Outside Model](../families/H-deterministic-control/patterns/H07-authorization-outside-model.md) — Enforce access control in application code, not prompts
- [H02 — Programmatic Gate](../families/H-deterministic-control/patterns/H02-programmatic-gate.md) — Hard stops that cannot be bypassed by model output
- [J05 — Deterministic Authorization](../families/J-security-trust/patterns/J05-deterministic-authorization.md) — Authorization decisions made by code, not by the model
- [G06 — Tool Gate](../families/G-tool-action-design/patterns/G06-tool-gate.md) — Require deterministic approval before executing sensitive tools

## Sources

- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
