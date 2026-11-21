# Principle 1 — Prefer Determinism Where the Problem Is Deterministic

> Do not spend model reasoning on conditions a program can reliably decide.

## Why This Matters

Every instruction in a prompt is probabilistic — the model may follow it or may not, depending on context length, competing instructions, and adversarial input. When a correctness rule (file format validation, permission check, schema conformance) is encoded only as a prompt instruction, it becomes a suggestion rather than an invariant. The system appears to work during testing, then fails unpredictably in production when context conditions shift.

This principle recurs across independent sources because every organization that ships agents at scale discovers the same failure: rules that seemed reliable in demos become unreliable under load, longer contexts, or adversarial inputs. The fix is always the same — move the check from the probabilistic layer (prompt) to the deterministic layer (code, schema validator, linter, type system, permission system). AWS calls this "use deterministic execution logic unless AI reasoning is specifically needed." OpenAI calls it "enforce architectural invariants mechanically." Anthropic builds gate patterns that wrap model output in validator code. The convergence is total.

## Which Sources Converge

| Organization | How They Express This Principle |
|---|---|
| **AWS** | "Use deterministic execution logic unless AI reasoning is specifically needed" — system design recommendations |
| **OpenAI** | "Enforce architectural invariants mechanically" via linters, structural tests, and CI hooks rather than relying on instructions |
| **Anthropic** | Gate patterns that wrap model output in programmatic validators before it reaches downstream systems |
| **OWASP** | Prompt injection risk exists precisely because prompt-level rules can be overridden; deterministic boundaries cannot |
| **Google Cloud** | Pattern selection criteria include whether the task requires AI reasoning or can be handled by conventional code |

## Patterns That Implement This Principle

- [Deterministic Validation Gate](../families/H-deterministic-control/) — wraps model output in schema/type/format validators
- [Least-Privilege Tool Access](../families/G-tool-design/) — tool permissions enforced by code, not by asking the model to self-limit
- [Structured Output Enforcement](../families/O-output-integration/) — output schemas enforced by parsing, not by instruction
- [Bounded Agent Loop](../families/I-reliability-recovery/) — loop termination via counter/timer, not model self-awareness

## Anti-Patterns This Prevents

- **Prompt-as-Policy** — encoding authorization, validation, or business rules solely in system prompts where they can be overridden or ignored
- **Model as Security Boundary** — trusting the model to refuse unauthorized actions rather than enforcing permissions in code

## Practical Application

1. **Output format enforcement:** Instead of instructing "always return valid JSON," use a structured output mode or parse the response through a JSON schema validator. Reject and retry on parse failure.

2. **Permission checks:** Instead of telling the model "never access files outside /workspace," implement a filesystem sandbox that physically prevents access. The model's compliance is irrelevant when the boundary is enforced by the runtime.

3. **Loop termination:** Instead of instructing "stop after you've completed the task," implement a hard iteration cap (e.g., max 25 tool calls) and a wall-clock timeout. The model can still decide to stop early, but the system guarantees termination.

4. **Content filtering:** Instead of instructing "never output harmful content," run model output through a deterministic content classifier before returning it to the user. The classifier catches what the instruction misses.

## Sources

- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
