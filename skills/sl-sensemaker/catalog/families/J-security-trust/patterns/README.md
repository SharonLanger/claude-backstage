# Family J — Security & Trust Boundaries: Patterns

11 patterns (J01–J11) covering architectural controls that prevent model-controlled actions from crossing security boundaries.

**Central insight:** Simon Willison's "lethal trifecta" — private data + untrusted content + external communication present simultaneously — creates an exfiltration path after a single prompt injection. The patterns in this family dismantle the trifecta by attacking each leg independently.

**Sources:** Simon Willison, OWASP GenAI Top 10 2026, AWS Prescriptive Guidance, Anthropic Engineering.

---

## Files

```
patterns/
├── README.md                          ← this file
├── J01-least-privilege.md             ← grant only the minimum permissions required per task; short-lived scoped credentials
├── J02-sandbox.md                     ← isolate code/command execution so model errors cannot reach the host system
├── J03-secret-isolation.md            ← keep secrets out of the context window; deliver them out-of-band to the tool layer
├── J04-tool-gateway.md                ← centralize tool dispatch behind a policy enforcement point with audit logging
├── J05-deterministic-authorization.md ← never delegate authorization decisions to the model; use rule-based checks
├── J06-untrusted-context-isolation.md ← process untrusted content in a separate context, away from credentials and instructions
├── J07-session-isolation.md           ← prevent state leakage between sessions in multi-tenant or multi-session systems
├── J08-human-approval-gate.md         ← require human approval before irreversible or high-impact actions execute
├── J09-external-comm-restriction.md   ← restrict outbound network access to remove the exfiltration leg of the trifecta
├── J10-capability-minimization.md     ← prune tools and permissions down to what the current task actually requires
└── J11-read-write-separation.md       ← grant read-only access by default; require explicit justification for write access
```

---

## Pattern Schema

Each engineering entry in this folder follows the same structure:

| Section | Contents |
|---|---|
| **Title + metadata** | Pattern name, Family, ID, cross-family appearances |
| **Problem** | The concrete failure mode this pattern prevents |
| **Solution** | The architectural response in plain language |
| **Structure** | Mermaid diagram in a collapsible `<details>` block |
| **Implementation Notes** | Concrete guidance, pseudocode, configuration examples |
| **Failure Modes** | How this pattern can be violated or circumvented |
| **Evidence** | Source citations with relevance summary and URL |
| **Related Patterns** | Intra- and inter-family links with relationship description |

---

## How to Navigate

**Entry by threat type:**
- Credential abuse → J01, J03, J11
- Code/command execution risk → J02, J10
- Prompt injection → J06, J09 (remove the exfiltration channel), J04 (enforce at dispatch)
- Authorization bypass → J05, J08
- Multi-tenant leakage → J07
- Attack surface growth → J10, J01

**Entry by the lethal trifecta leg you are addressing:**
- Private data in context → J03, J11
- Untrusted content processing → J06
- External communication → J09

**Entry by architectural layer:**
- Credential/permission layer → J01, J03, J05, J11
- Execution layer → J02, J10
- Tool dispatch layer → J04
- Context/input layer → J06, J07
- Human oversight → J08
- Network layer → J09

**Cross-family links:** J08 (human approval) overlaps with Family K. J02 (sandbox) and J07 (session isolation) overlap with Family F (Harness). J06 (untrusted context) connects to Family E (Context Engineering).

---

Last updated: 2026-08-24
