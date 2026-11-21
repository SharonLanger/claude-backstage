# Principle 6 — Security Boundaries Belong Outside the Model

> Prompts are not authorization systems.

---

## Why This Matters

A language model that decides its own authorization can be manipulated by the content it processes. Prompt injection — where adversarial input in user-supplied data overrides system instructions — is not a bug that will be patched; it is a structural property of systems that interpret instructions and data in the same channel. Any security boundary enforced solely through prompt instructions is only as strong as the model's obedience under adversarial conditions, which is empirically unreliable.

This principle has the strongest cross-source convergence of any in this catalog. OWASP ranks prompt injection and insufficient access controls as top risks for agentic applications. Simon Willison identified the "lethal trifecta" — combining access to private data, exposure to untrusted content, and ability to communicate externally creates a direct exfiltration path. AWS mandates deterministic execution logic for security-critical decisions. OpenAI's harness engineering enforces architectural invariants mechanically rather than through instructions. The convergence is absolute because the attack surface is architectural: no amount of instruction-tuning eliminates the possibility that a sufficiently crafted input overrides a prompt-based rule.

---

## Which Sources Converge

| Organization | What They Say | Key Concept |
|---|---|---|
| OWASP | Ranks prompt injection (#1) and excessive agency as top agentic risks | Authorization must be enforced outside the model's reasoning |
| Simon Willison | Identified the "lethal trifecta" — data access + untrusted content + external communication | Never combine all three without deterministic controls |
| AWS | Use deterministic execution logic for security decisions; do not rely on AI for authorization | Deterministic enforcement over probabilistic obedience |
| OpenAI | Enforce architectural invariants mechanically with linters, tests, and structural constraints | Security properties are harness responsibilities, not model responsibilities |

---

## Patterns That Implement This Principle

- [Least-Privilege Tool Access](../families/G-tool-action-design/) — tools expose minimal capabilities; permissions are granted by the harness, not the model
- [Deterministic Validation Gate](../families/H-deterministic-control/) — security-relevant decisions use code-level checks, not prompt-level instructions
- [Human Approval Gate](../families/K-human-control/) — irreversible or high-privilege actions require explicit human authorization
- [Scoped Tool Permissions](../families/J-security-trust/) — tool access is narrowed to the minimum required for each task

---

## Anti-Patterns This Prevents

- **Prompt-as-Policy** — encoding access control rules in the system prompt and trusting the model to follow them under all inputs, including adversarial ones
- **Model as Security Boundary** — relying on the model to refuse unauthorized actions rather than making unauthorized actions structurally impossible
- **Overpowered Coding Agent** — giving an agent broad filesystem, network, and execution permissions and trusting prompt instructions to prevent misuse

---

## Practical Application

1. **Tool-level permission enforcement:** Instead of telling the model "only read files in the project directory," configure the tool wrapper to reject any path outside the allowed directory. The model never gets the choice — unauthorized actions fail at the tool layer regardless of what the model requests.

2. **Separation of data and control planes:** When processing user-submitted documents, run extraction in a sandboxed context where the model has no access to tools that send emails, make API calls, or write to databases. The trifecta is broken by architecture, not instructions.

3. **Allowlist over denylist for actions:** Define a positive list of permitted operations (read these specific files, call these specific APIs) rather than trying to enumerate what the model must not do. Anything not on the allowlist is structurally impossible.

4. **Human-in-the-loop for privilege escalation:** When an agent needs to perform a high-privilege action (deploy code, send external communications, modify permissions), the harness routes through a human approval step — the model cannot bypass this regardless of reasoning.

---

## Sources

- Simon Willison — [The Lethal Trifecta for AI Agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- OWASP — [Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Simon Willison — [Living Dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
