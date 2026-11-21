# Guide: Threat Model Primer for Agent Systems

## Purpose

Use this guide when designing or reviewing the security posture of an agent system. It provides a structured approach to identifying threats specific to LLM-powered agents — beyond traditional application security.

## What Makes Agent Threat Modeling Different

Traditional threat models assume deterministic components. Agent systems introduce:

1. **Probabilistic execution** — the agent may interpret instructions differently each run
2. **Untrusted content in the execution path** — web pages, documents, user messages can contain adversarial instructions
3. **Capability amplification** — tools give the model power beyond text generation
4. **Emergent behavior** — multi-step tool chains create attack surfaces not visible in any single step

## The Five-Question Framework

For every agent system, answer these questions:

### 1. What can the agent access?

List all capabilities: file system paths, APIs, databases, network endpoints, secrets, external services.

| Capability | Read | Write | Delete | Scope |
|-----------|------|-------|--------|-------|
| File system | ? | ? | ? | Which paths? |
| Database | ? | ? | ? | Which tables? |
| External APIs | ? | ? | ? | Which endpoints? |
| Secrets/tokens | ? | ? | ? | Which scopes? |
| Network | ? | ? | ? | Which hosts? |

### 2. What content does the agent process that you do not control?

Any content from outside your trust boundary:
- User messages (direct prompt injection vector)
- Retrieved documents, web pages, emails (indirect injection)
- API responses from third parties
- File contents uploaded by users
- Database records written by other systems

### 3. Can the agent communicate externally?

If the agent can send data outward (email, HTTP requests, file writes to shared locations, Slack messages), it can exfiltrate. Check:
- Can it send HTTP requests to arbitrary URLs?
- Can it compose and send messages?
- Can it write to locations readable by external parties?
- Can it modify shared resources (repos, wikis, databases)?

### 4. Does the combination create the Lethal Trifecta?

If you answered YES to all three — private data access + untrusted content processing + external communication — you have a high-severity exfiltration path. Any successful prompt injection can steal private data.

```
Private Data Access  +  Untrusted Content  +  External Comms  =  Exfiltration Path
```

### 5. What is the blast radius of a compromised agent?

If the agent is fully compromised (treats attacker instructions as its own), what is the worst-case outcome?
- Data exfiltration scope (what secrets are reachable?)
- Destructive potential (can it delete, corrupt, or overwrite?)
- Lateral movement (can it access other systems or spawn other agents?)
- Persistence (can it modify its own tools, prompts, or scheduled jobs?)

## Threat Catalog for Agent Systems

| Threat | Attack Vector | Impact | Primary Mitigation |
|--------|--------------|--------|-------------------|
| Direct prompt injection | User input | Full agent compromise | Input validation, instruction hierarchy |
| Indirect prompt injection | Retrieved documents, web pages | Covert agent compromise | Untrusted context isolation (J06) |
| Tool misuse | Manipulated agent reasoning | Unauthorized actions | Least-privilege tools (J01), deterministic auth (J05) |
| Data exfiltration | Prompt injection + external comms | Data breach | External comm restriction (J09), capability minimization (J10) |
| Privilege escalation | Tool chaining | Expanded blast radius | Sandbox (J02), tool gateway (J04) |
| Secret leakage | Secrets in prompt context | Credential theft | Secret isolation (J03) |
| Session hijacking | Cross-session state pollution | Wrong-user data access | Session isolation (J07) |

## Minimum Viable Threat Model (30-Minute Version)

For teams that need to start somewhere:

1. **Draw the trust boundary.** What is inside your control vs. outside?
2. **List all capabilities.** Every tool, every API, every file path.
3. **Check the Lethal Trifecta.** If present, you have a critical finding — stop and mitigate.
4. **Apply least privilege.** For each capability, ask: "Does the agent need this for its core task?" Remove everything else.
5. **Identify untrusted inputs.** For each, ask: "If this contained malicious instructions, what could happen?"
6. **Document the blast radius.** Write one paragraph describing worst-case compromise.

## Related Patterns

- [J01: Least Privilege](patterns/J01-least-privilege.md)
- [J02: Sandbox](patterns/J02-sandbox.md)
- [J06: Untrusted Context Isolation](patterns/J06-untrusted-context-isolation.md)
- [J09: External Communication Restriction](patterns/J09-external-comm-restriction.md)
- [J10: Capability Minimization](patterns/J10-capability-minimization.md)
- [High-Risk Combinations](high-risk-combinations.md) — detailed reference on dangerous capability sets

## Sources

- Simon Willison — [The Lethal Trifecta for AI Agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- Simon Willison — [Living Dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- OWASP — [Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
