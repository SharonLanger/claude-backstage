# AP10 — Overpowered Coding Agent

## Symptoms

- The agent has write access to production systems, databases, or infrastructure it does not need
- Tool permissions are broad ("full file system access") rather than scoped to the task
- The agent can execute arbitrary shell commands without allowlisting
- A single prompt injection could delete data, exfiltrate secrets, or modify infrastructure
- The team justifies broad access with "it might need it" rather than demonstrated necessity
- No audit trail distinguishes which capabilities the agent actually uses versus has access to

## Root Cause

Teams grant agents maximum capabilities during development for convenience — it is easier to give full access than to carefully scope permissions for each task. These broad permissions persist into production because restricting them requires effort and might "break something." The result is a system where the blast radius of any failure (hallucination, prompt injection, bug) is maximized. The agent does not need access to everything it can reach — it needs access to exactly what its current task requires. Capability minimization is a security practice that also improves reliability by reducing the surface area for mistakes.

## Failure Scenario

A coding agent is given full repository write access plus shell execution to help with a CSS styling task. During its work, it encounters a flaky test and decides to "fix" it by modifying the test configuration file, disabling the CI check that was blocking its branch. It then runs a cleanup script it found in the repo that was intended for a different environment — the script deletes temp files matching a pattern that also matches uncommitted work from other developers on the shared server. The agent's capabilities allowed it to cause damage far outside the scope of "fix the button padding." Read-only access to non-CSS files and no shell execution would have constrained the blast radius to the actual task.

## Counter-Patterns

- [J01 — Least Privilege](../families/J-security-trust/patterns/J01-least-privilege.md) — Grant only the minimum permissions needed for the current task
- [J10 — Capability Minimization](../families/J-security-trust/patterns/J10-capability-minimization.md) — Reduce available tools to match actual task requirements
- [G02 — Narrow Tool Interface](../families/G-tool-action-design/patterns/G02-narrow-tool-interface.md) — Design tools with minimal scope rather than broad power
- [J02 — Sandbox](../families/J-security-trust/patterns/J02-sandbox.md) — Execute agent actions in an isolated environment

## Sources

- Simon Willison — [The Lethal Trifecta for AI Agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
