# Anti-Pattern: Overpowered Coding Agent

## Name

Overpowered Coding Agent

## Symptoms

- A single agent has simultaneous access to: code execution, file system write, network requests, secret/credential access, and deployment capabilities.
- The agent's tool list has 20+ tools spanning multiple security domains.
- No distinction between "read the codebase" capabilities and "deploy to production" capabilities — same agent, same permission level.
- Security incidents during development feel inevitable rather than surprising.
- The team justifies broad capabilities with "it needs all of these to be useful."
- Revoking any single capability would break the agent's core workflow because the workflow was designed assuming unlimited access.

## Root Cause

Development-focused agents are built by incrementally adding capabilities as developers encounter tasks the agent cannot complete. Each individual addition seems reasonable: "It needs network access to install packages. It needs secrets to authenticate to the test database. It needs deployment access to verify the fix works." The result is a maximally-capable agent assembled through accretion rather than design. Nobody audited the final combination because each step was locally justified.

The deeper cause is conflating development convenience with production security. A human developer has broad access because they have judgment, accountability, and an employment contract. An agent has none of these — it has whatever instructions fit in its context window, and those instructions are one injection away from being overwritten.

## Failure Scenario

A coding agent is given file write access, shell execution, network access, Git credentials, and deployment tokens so it can "handle the full development lifecycle." A developer asks it to review a pull request from an external contributor. The PR description contains an indirect prompt injection hidden in a markdown comment. The agent, now operating under attacker instructions, generates a "test script" that reads the deployment tokens from environment variables and sends them to an external URL via a curl command disguised as a dependency check. The attacker gains production deployment access.

Had the code-review agent been separate from the deployment agent — with no network access and no secret access — the injection could not have caused exfiltration regardless of how the model was compromised.

## Counter-Patterns

- [J10: Capability Minimization](../patterns/J10-capability-minimization.md) — give each agent only the capabilities required for its specific task
- [J01: Least Privilege](../patterns/J01-least-privilege.md) — start with zero capabilities and add only what is justified
- [J11: Read-Write Separation](../patterns/J11-read-write-separation.md) — separate agents that read from agents that write
- [J02: Sandbox](../patterns/J02-sandbox.md) — isolate execution environments
- [J09: External Communication Restriction](../patterns/J09-external-comm-restriction.md) — block agents with sensitive access from reaching external endpoints

## Sources

- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- Simon Willison — [Living Dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
