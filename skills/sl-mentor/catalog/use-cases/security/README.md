# security/

Security guides for agent systems — from full review checklists to targeted threat-specific mitigations.

```
security/
├── README.md                ← this file
├── security-review.md       ← full security review checklist for agent systems
├── prompt-injection.md      ← protecting against prompt injection and hijacking
└── privilege-and-trust.md   ← least-privilege design, trust boundaries, sandboxing
```

## File descriptions

- **security-review.md** — Full security review checklist for agent systems; maps to families J, G, K
- **prompt-injection.md** — Protecting against prompt injection and hijacking; maps to family J; source: Simon Willison's "lethal trifecta", OWASP
- **privilege-and-trust.md** — Least-privilege design, trust boundaries, sandboxing; maps to families J, K, G

## When to use this folder

Use this folder when reviewing the security posture of an agent system or designing defenses against specific threats. Start with `security-review.md` for a comprehensive pass; go directly to the threat-specific files if you already know what you are investigating.

## How to navigate

| Arrival scenario | Go to |
|---|---|
| "I need a full security review of my agent system" | `security-review.md` |
| "I'm worried about prompt injection attacks" | `prompt-injection.md` |
| "How do I limit what my agent can access and do?" | `privilege-and-trust.md` |
| "What trust boundaries should exist between agents?" | `privilege-and-trust.md` |

Last updated: 2026-08-24
