# Least-Privilege Design, Trust Boundaries, and Sandboxing

## Scenario

You are designing the permission model for an agent system — deciding what each agent can access, how to isolate untrusted operations, and where to draw trust boundaries between components.

## Quick Answer

1. **Start with zero permissions and add incrementally** — each agent gets only the tools and data access required for its specific task. Use [J01-Least-Privilege](../../families/J-security-trust/patterns/J01-least-privilege.md).
2. **Separate read from write** — agents that gather information should not be the same agents that take action. Apply [J11-Read-Write-Separation](../../families/J-security-trust/patterns/J11-read-write-separation.md).
3. **Sandbox execution environments** — code execution, file access, and network calls should run in isolated environments with explicit resource limits. Use [J02-Sandboxed-Execution](../../families/J-security-trust/patterns/J02-sandbox.md).

## Design Principles

### Principle 1: Minimum Viable Permissions

Every agent component should be scoped to the narrowest set of capabilities:

- **Tool-level scoping**: An agent that needs to read a database should not have write access. An agent that writes to one table should not have access to others.
- **Temporal scoping**: Elevated permissions should be granted only for the duration of a specific operation, then revoked.
- **Data scoping**: Agents should see only the data relevant to their current task, not all available data.

### Principle 2: Trust Boundary Identification

Map every point where data or control crosses a trust level:

| Boundary | Example | Control |
|----------|---------|---------|
| User → Agent | User prompt | Input validation, sanitization |
| External data → Agent | RAG retrieval, API responses | Treat as untrusted, validate before use |
| Agent → Agent | Multi-agent message passing | Schema validation, scoped context handoff |
| Agent → Tool | Tool invocation | Schema-constrained parameters, approval gates |
| Agent → External system | API calls, database writes | Credential isolation, sandboxing |

### Principle 3: Defense Through Architecture

Security comes from system structure, not from asking the LLM to be careful:

- **Deterministic enforcement**: Use code-level guards (allowlists, schema validation, rate limits) that cannot be bypassed by prompt manipulation.
- **Separation of duties**: Split high-risk operations across multiple agents so no single compromised agent can complete a harmful action alone.
- **Fail closed**: When validation is uncertain, deny the action rather than allowing it.

## Decision Guide: Setting Permission Boundaries

```
For each agent in the system, ask:
│
├── What tools does it NEED? (not "might use" — NEEDS)
│   └── Grant only those tools, with narrowest scope
│
├── Does it need to READ external/untrusted data?
│   ├── YES → Isolate it from write operations
│   │         Use context isolation for retrieved content
│   └── NO → Standard input validation is sufficient
│
├── Does it need to WRITE or EXECUTE?
│   ├── YES → Add confirmation gates for irreversible actions
│   │         Sandbox the execution environment
│   │         Log all actions for audit
│   └── NO → Read-only agent, lower risk profile
│
└── Does it handle credentials or secrets?
    ├── YES → Use credential isolation (vault, env vars, never in context)
    │         Rotate credentials on schedule
    └── NO → Ensure no credential leakage from upstream
```

## Sandboxing Strategies

| Strategy | Use When | Implementation |
|----------|----------|----------------|
| Process isolation | Agent executes arbitrary code | Container or VM with resource limits |
| Filesystem isolation | Agent reads/writes files | Scoped to specific directories, no path traversal |
| Network isolation | Agent makes external calls | Allowlisted domains/ports, egress filtering |
| Memory isolation | Multi-tenant agents | Separate state per user/session, no cross-contamination |
| Temporal isolation | One-shot operations | Fresh environment per execution, no persistent state |

## Relevant Patterns

| Pattern | Role in Privilege Design |
|---------|--------------------------|
| [J01-Least-Privilege](../../families/J-security-trust/patterns/J01-least-privilege.md) | Core principle — minimum permissions per component |
| J02-Scoped-Tool-Access (catalog entry unavailable) | Restrict tool availability per agent role |
| [J02-Sandboxed-Execution](../../families/J-security-trust/patterns/J02-sandbox.md) | Isolated environments for untrusted operations |
| [J03-Credential-Isolation](../../families/J-security-trust/patterns/J03-secret-isolation.md) | Separate secrets from agent context |
| J10-Rate-Limit-Budget (catalog entry unavailable) | Cap resource consumption per agent |
| [J11-Read-Write-Separation](../../families/J-security-trust/patterns/J11-read-write-separation.md) | Architectural split between readers and writers |
| [J08-Human-Approval-Gate](../../families/J-security-trust/patterns/J08-human-approval-gate.md) | Human confirmation for privilege escalation |
| [E-Context-Isolation](../../families/E-context-engineering/patterns/context-isolation.md) | Prevent data leakage across context boundaries |
| [L-Session-Isolation](../../families/L-memory-state/patterns/session-isolation.md) | Isolate state between sessions/users |
| [L-Scoped-Memory](../../families/L-memory-state/patterns/scoped-memory.md) | Restrict memory access by scope |
| [G01-Typed-Schema-Constrained-Tool](../../families/G-tool-action-design/patterns/G01-typed-schema-constrained-tool.md) | Tools that only accept valid, typed parameters |

## Anti-Patterns to Watch For

| Anti-Pattern | Risk |
|--------------|------|
| Granting all tools to all agents "for convenience" | One compromised agent can do anything |
| Shared credentials across agents | Credential compromise affects entire system |
| Relying on the LLM to self-restrict | Injection can override self-imposed limits |
| No separation between reading and acting | Agent that browses untrusted content can also take destructive actions |
| Persistent elevated permissions | Time-unlimited access outlives the task that needed it |

## Sources

- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html
- https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
