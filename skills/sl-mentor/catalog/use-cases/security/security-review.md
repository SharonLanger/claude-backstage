# Security Review Checklist for Agent Systems

## Scenario

You are preparing an agent system for production deployment and need a systematic security review. This applies whether you are auditing an existing system or building security controls into a new one.

## Quick Answer

1. **Map trust boundaries** — identify every point where untrusted input enters the system (user prompts, tool outputs, retrieved documents, other agents' messages). Apply patterns from [J-Security-Trust](../../families/J-security-trust/patterns/).
2. **Enforce least privilege** — every agent should have only the permissions it needs. Use [J01-Least-Privilege](../../families/J-security-trust/patterns/J01-least-privilege.md) and [J11-Read-Write-Separation](../../families/J-security-trust/patterns/J11-read-write-separation.md).
3. **Add human gates on destructive actions** — use [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) for irreversible operations.

## Security Review Checklist

### 1. Input Boundaries

- [ ] All user inputs are treated as untrusted
- [ ] Retrieved documents (RAG) are treated as potential injection vectors
- [ ] Tool outputs are validated before being consumed by the agent
- [ ] Inter-agent messages are scoped and validated
- [ ] System prompts are separated from user-controllable content

### 2. Permission Model

- [ ] Each agent/tool operates with minimum required permissions
- [ ] Read-only operations are separated from write operations
- [ ] Destructive actions (delete, overwrite, send) require explicit confirmation
- [ ] Token/credential scope is narrowed to specific resources
- [ ] No agent can escalate its own privileges

### 3. Prompt Injection Defense

- [ ] Input sanitization applied at trust boundaries
- [ ] System prompts are hardened against extraction attempts
- [ ] Multi-step flows validate intermediate outputs before passing downstream
- [ ] Output parsers reject malformed or suspicious results
- [ ] See [prompt-injection.md](./prompt-injection.md) for detailed defenses

### 4. Tool and Action Safety

- [ ] All tool calls are schema-validated before execution
- [ ] Side-effecting tools have confirmation gates
- [ ] Tool execution is sandboxed (filesystem, network, process isolation)
- [ ] Rate limits and budget caps prevent runaway execution
- [ ] Idempotent wrappers protect against retry-induced duplication

### 5. Data Protection

- [ ] Sensitive data (PII, credentials, keys) is never included in prompts
- [ ] Agent memory/state is scoped per-session or per-user
- [ ] Logs are scrubbed of sensitive content before storage
- [ ] Context windows are cleared between unrelated tasks
- [ ] Output is sanitized before display to users

### 6. Observability and Auditability

- [ ] All tool calls and their results are logged
- [ ] Agent decisions are traceable (structured traces)
- [ ] Anomalous behavior triggers alerts (unusual tool patterns, repeated failures)
- [ ] Human reviewers can replay agent runs for audit

### 7. Failure Modes

- [ ] Agents fail closed (deny by default on uncertainty)
- [ ] Circuit breakers prevent cascading failures
- [ ] Error messages do not leak system internals
- [ ] Graceful degradation paths exist for every critical operation

## Relevant Patterns

| Pattern | Role in Security Review |
|---------|------------------------|
| [J01-Least-Privilege](../../families/J-security-trust/patterns/J01-least-privilege.md) | Foundation — minimum permissions per agent |
| J02-Scoped-Tool-Access (catalog entry unavailable) | Restrict which tools each agent can call |
| J03-Input-Validation-Boundary (catalog entry unavailable) | Sanitize at every trust boundary |
| [J02-Sandboxed-Execution](../../families/J-security-trust/patterns/J02-sandbox.md) | Isolate agent execution environments |
| [J08-Human-Approval-Gate](../../families/J-security-trust/patterns/J08-human-approval-gate.md) | Require approval for high-risk actions |
| J06-Output-Filtering (catalog entry unavailable) | Filter sensitive data from outputs |
| J07-Audit-Trail (catalog entry unavailable) | Maintain tamper-evident action logs |
| [J03-Credential-Isolation](../../families/J-security-trust/patterns/J03-secret-isolation.md) | Separate credential storage from agent context |
| J09-Defense-In-Depth (catalog entry unavailable) | Layer multiple security controls |
| J10-Rate-Limit-Budget (catalog entry unavailable) | Cap resource consumption |
| [J11-Read-Write-Separation](../../families/J-security-trust/patterns/J11-read-write-separation.md) | Separate read and write permissions |
| [K01-Human-in-the-Loop-Checkpoint](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) | Human gates on critical decisions |
| [M01-Structured-Trace](../../families/M-observability-debugging/patterns/M01-structured-trace.md) | Audit-quality execution traces |
| [O-Sanitized-Output-Boundary](../../families/O-output-integration/patterns/sanitized-output-boundary.md) | Clean outputs before external delivery |

## Anti-Patterns to Watch For

| Anti-Pattern | Risk |
|--------------|------|
| Overly broad tool permissions | A single compromised prompt can trigger destructive actions across the entire system |
| Trusting retrieved content | RAG documents can contain injected instructions that alter agent behavior |
| Relying solely on prompt engineering for security | LLM-based guards are probabilistic — combine with deterministic validation |
| No human oversight on irreversible actions | Autonomous agents making permanent changes without review |

## Sources

- https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- https://genai.owasp.org/llm-top-10/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html
- https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
