# Family J — Security & Trust Boundaries

**Recurring problem:** Model-controlled actions can cross security boundaries after prompt injection or model error.

**Primary evidence source:** OWASP GenAI Security Project

**Related families:** F (sandboxed execution), G (tool gateway), H (deterministic authorization), K (human approval gate)

---

## Directory Tree

```
J-security-trust/
├── README.md                          ← this file (navigation hub)
├── threat-model-primer.md             ← agent threat model: attack surfaces, trust zones, adversary goals
├── high-risk-combinations.md          ← capability combination danger table
│
├── patterns/
│   ├── J01-least-privilege.md             ← grant only the minimum permissions needed for the task
│   ├── J02-sandbox.md                     ← isolate execution environment; constrain OS/network/filesystem access
│   ├── J03-secret-isolation.md            ← secrets never enter the context window or tool outputs
│   ├── J04-tool-gateway.md                ← all tool calls route through a policy-enforcement layer
│   ├── J05-deterministic-authorization.md ← authorization decisions made outside the model, never delegated to it
│   ├── J06-untrusted-context-isolation.md ← untrusted inputs (web, files, user data) handled in separate context
│   ├── J07-session-isolation.md           ← no shared state between sessions; blast radius is one session
│   ├── J08-human-approval-gate.md         ← irreversible or high-risk actions require explicit human sign-off
│   ├── J09-external-comm-restriction.md   ← outbound network calls require explicit allow-list approval
│   ├── J10-capability-minimization.md     ← remove capabilities not required; shrink attack surface structurally
│   └── J11-read-write-separation.md       ← read and write permissions granted separately; default read-only
│
└── anti-patterns/
    ├── AP-model-as-security-boundary.md   ← why the model must never be the last line of defense
    └── AP-overpowered-coding-agent.md     ← the lethal triad: private data + untrusted content + external comms
```

---

## Per-Pattern File Schema

Each engineering pattern (`J01` – `J11`) follows this structure:

```
# <Pattern Name>
**Family:** J — Security & Trust Boundaries
**ID:** J0N
**Also appears in:** <other families if cross-listed>

## Problem
One paragraph: the specific failure mode this pattern prevents.

## Solution
One paragraph: the architectural control.

## Structure
Diagram or bullet list of components and their relationships.

## Implementation Notes
Concrete guidance — language/framework-agnostic where possible.
Flag HANA/SAP-specific considerations if relevant.

## Failure Modes
What breaks if this pattern is applied incorrectly or incompletely.

## Evidence
OWASP GenAI references, CVEs, incident reports, or research citations.

## Related Patterns
Cross-links to other J patterns and to other families (F, G, H, K).
```

---

## High-Risk Agent Capability Combinations

Full table with mitigations: see [`high-risk-combinations.md`](high-risk-combinations.md)

**Summary — the lethal triads:**

| Capabilities present simultaneously | Risk | Triggered anti-pattern |
|--------------------------------------|------|------------------------|
| Private data + untrusted content + external comms | Critical | Overpowered Coding Agent (AP-overpowered-coding-agent) |
| Tool execution + no authorization layer + prompt injection surface | Critical | Model as Security Boundary (AP-model-as-security-boundary) |
| File write + shell access + internet access | Critical | Overpowered Coding Agent |
| Secret access + untrusted input channel | High | Secret Isolation violation |
| Cross-session state + multi-tenant workload | High | Session Isolation violation |
| Broad tool set + no least-privilege scoping | High | Capability Minimization gap |

**Rule of thumb:** any agent that can simultaneously read sensitive data AND receive untrusted content AND communicate externally is in the critical risk tier regardless of model safety measures.

---

## Threat Model Primer

See [`threat-model-primer.md`](threat-model-primer.md) for:

- Trust zones in agent systems (user, orchestrator, model, tools, external)
- Primary attack surfaces (prompt injection, tool poisoning, context hijacking)
- Adversary goals (data exfiltration, privilege escalation, lateral movement)
- Mapping of OWASP GenAI Top 10 to this family's patterns

---

## Anti-Patterns

| File | What it explains |
|------|-----------------|
| `anti-patterns/AP-model-as-security-boundary.md` | Why a safety-trained model is not a substitute for architectural controls |
| `anti-patterns/AP-overpowered-coding-agent.md` | How accumulating capabilities creates emergent critical risk; the lethal triad |

---

## Cross-Family Map

| Pattern | Also in |
|---------|---------|
| J02 Sandbox | F (execution isolation) |
| J04 Tool Gateway | G (tool design) |
| J05 Deterministic Authorization | H (deterministic control) |
| J08 Human Approval Gate | K (human oversight) |

---

Last updated: 2026-08-24
