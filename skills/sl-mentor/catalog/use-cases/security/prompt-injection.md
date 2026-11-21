# Protecting Against Prompt Injection and Hijacking

## Scenario

You are building an agent that processes untrusted input — user messages, retrieved documents, tool outputs, or data from external APIs — and you need to prevent adversarial content from hijacking the agent's behavior.

## Quick Answer

1. **Separate trust levels architecturally** — never concatenate untrusted input directly into system-level instructions. Use [J03-Input-Validation-Boundary](../../families/J-security-trust/patterns/J03-input-validation-boundary.md) to define clear boundaries.
2. **Layer defenses** — combine input validation, output filtering, sandboxed execution, and human approval. No single defense is sufficient. Apply [J09-Defense-In-Depth](../../families/J-security-trust/patterns/J09-defense-in-depth.md).
3. **Validate outputs deterministically** — use [D01-Deterministic-Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) and [O-Schema-Validation](../../families/O-output-integration/patterns/schema-validation.md) to catch anomalous agent behavior regardless of how it was induced.

## The Lethal Trifecta

An agent is maximally vulnerable to prompt injection when three conditions combine:

1. **Access to untrusted content** — RAG retrieval, web browsing, email processing, tool outputs
2. **Consequential tool access** — ability to send messages, modify files, execute code, make purchases
3. **Implicit trust in context** — the LLM treats all text in its context window as instructions

When all three are present, an attacker can embed instructions in content the agent reads, causing it to take harmful actions. Break any one leg of the trifecta to reduce risk dramatically.

## Decision Guide

```
Does the agent process untrusted text?
├── NO → Low injection risk (still apply basic input validation)
└── YES → Does it have write/action permissions?
    ├── NO → Medium risk: output can be manipulated but no side effects
    │   └── Apply: input sanitization + output validation
    └── YES → HIGH RISK: full lethal trifecta
        └── Apply ALL defenses below
```

## Defense Layers

### Layer 1: Input Boundary Controls

- **Structural separation**: Place untrusted content in clearly demarcated sections (e.g., XML tags, role separators) that the model is instructed to treat as data, not instructions.
- **Sanitization**: Strip or escape known injection patterns before including in context.
- **Length limits**: Cap input size to reduce the surface area for hidden instructions.
- **Content-type validation**: Reject inputs that don't match expected formats.

### Layer 2: Architectural Isolation

- **Privilege separation**: The agent that reads untrusted content should NOT be the same agent that executes actions. Use [C-Maker-Checker](../../families/C-orchestration/patterns/maker-checker.md) to split planning from execution.
- **Context isolation**: Use [E-Context-Isolation](../../families/E-context-engineering/patterns/context-isolation.md) to prevent untrusted content from contaminating decision-making context.
- **Read-write separation**: Agents that browse or retrieve operate in read-only mode; a separate privileged agent handles writes after validation. Apply [J11-Read-Write-Separation](../../families/J-security-trust/patterns/J11-read-write-separation.md).

### Layer 3: Output Validation

- **Deterministic checks**: Validate every action the agent wants to take against allowlists, schemas, and business rules — not against LLM judgment.
- **Anomaly detection**: Flag actions that don't match the user's original intent (e.g., user asked to summarize an email, agent tries to forward it).
- **Rejection on parse failure**: Use [O-Parse-and-Reject](../../families/O-output-integration/patterns/parse-and-reject.md) to refuse malformed or unexpected outputs.

### Layer 4: Human Oversight

- **Confirmation gates**: For high-risk actions (sending data externally, deleting resources, financial transactions), always require human confirmation.
- **Monitoring**: Use [K06-Human-on-the-Loop-Monitoring](../../families/K-human-control/patterns/K06-human-on-the-loop-monitoring.md) to flag suspicious behavioral patterns.

## Relevant Patterns

| Pattern | Role in Injection Defense |
|---------|---------------------------|
| [J03-Input-Validation-Boundary](../../families/J-security-trust/patterns/J03-input-validation-boundary.md) | Define and enforce trust boundaries on all inputs |
| [J09-Defense-In-Depth](../../families/J-security-trust/patterns/J09-defense-in-depth.md) | Layer multiple independent defenses |
| [J04-Sandboxed-Execution](../../families/J-security-trust/patterns/J04-sandboxed-execution.md) | Isolate execution so injection cannot escape |
| [J06-Output-Filtering](../../families/J-security-trust/patterns/J06-output-filtering.md) | Strip sensitive data from agent outputs |
| [J11-Read-Write-Separation](../../families/J-security-trust/patterns/J11-read-write-separation.md) | Separate reading untrusted content from acting |
| [E-Context-Isolation](../../families/E-context-engineering/patterns/context-isolation.md) | Prevent context contamination across trust levels |
| [C-Maker-Checker](../../families/C-orchestration/patterns/maker-checker.md) | Separate planning from execution for independent review |
| [D01-Deterministic-Validator](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) | Validate actions with non-bypassable code checks |
| [O-Parse-and-Reject](../../families/O-output-integration/patterns/parse-and-reject.md) | Reject outputs that don't match expected structure |
| [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) | Require human approval for destructive actions |
| [O-Schema-Validation](../../families/O-output-integration/patterns/schema-validation.md) | Enforce strict output schemas |

## Anti-Patterns to Watch For

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| Prompt-only defense ("ignore all previous instructions") | Attackers craft inputs that bypass or override textual instructions |
| Single-layer validation | Any individual defense can be circumvented; only layering provides robust protection |
| Trusting LLM-generated security judgments | An injected prompt can also compromise the LLM's security reasoning |
| Allowing tools that exceed task requirements | Broader permissions mean broader attack surface when injection succeeds |

## Sources

- https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
