# Reference: High-Risk Capability Combinations

## Purpose

Use this reference when auditing an agent's capability set. Certain combinations of individually-reasonable capabilities create emergent security risks that are greater than the sum of their parts. This document catalogs the known dangerous combinations and their mitigations.

## The Lethal Trifecta

The foundational dangerous combination, identified by Simon Willison:

```
(1) Access to private data
    +
(2) Exposure to untrusted content
    +
(3) Ability to communicate externally
    =
    Exfiltration path after prompt injection
```

**Why it's lethal:** Any successful prompt injection (via untrusted content) can instruct the agent to read private data and send it to an attacker-controlled endpoint. Each capability alone is safe. The combination is catastrophic.

**Mitigation:** Break any one leg of the trifecta:
- Remove private data access (principle of least privilege)
- Isolate untrusted content processing (sandboxed context)
- Block external communication (no outbound network for agents processing untrusted input)

## Beyond the Trifecta: Extended Dangerous Combinations

### Combination 2: Write Access + Untrusted Input + Persistence

| Capability | Alone | Combined |
|-----------|-------|----------|
| Write access to code/config | Normal development tool | |
| Processes untrusted input | Normal retrieval | |
| Changes persist across sessions | Normal for productivity | |
| **All three together** | | Attacker can permanently modify agent behavior via injected instructions that write to config/prompts |

**Attack scenario:** Untrusted document contains hidden instructions to modify the agent's system prompt file or tool definitions. Because writes persist, subsequent sessions operate under attacker control.

**Mitigation:** Immutable system prompts; write access to config requires human approval gate (J08); separate untrusted-content-processing agents from agents with write access to system configuration.

### Combination 3: Multi-Agent Delegation + Elevated Privileges + Shared Memory

| Capability | Alone | Combined |
|-----------|-------|----------|
| Can delegate to other agents | Normal orchestration | |
| Some agents have elevated privileges | Normal capability separation | |
| Agents share memory/state | Normal coordination | |
| **All three together** | | Compromised low-privilege agent escalates by poisoning shared memory read by high-privilege agent |

**Attack scenario:** A low-privilege agent processing external data writes malicious instructions to shared memory. A high-privilege agent (with database write access) reads shared memory and follows the poisoned instructions.

**Mitigation:** Typed, validated shared memory (not free-text); privilege-aware memory access (high-privilege agents do not execute instructions from shared memory); clear provenance tracking on all memory writes.

### Combination 4: Code Execution + Network Access + Secret Access

| Capability | Alone | Combined |
|-----------|-------|----------|
| Can execute arbitrary code | Normal for coding agents | |
| Has network access | Normal for API calls | |
| Can read environment secrets | Normal for authenticated operations | |
| **All three together** | | Agent can exfiltrate secrets via generated code that phones home |

**Attack scenario:** Agent generates code that reads API keys from environment variables and includes them in an HTTP request to an attacker-controlled server, disguised as a normal API call or dependency installation.

**Mitigation:** Sandbox code execution with no network (J02); inject secrets at call time rather than making them readable; monitor outbound network for unexpected destinations.

### Combination 5: Tool Creation + Self-Invocation + No Approval Gate

| Capability | Alone | Combined |
|-----------|-------|----------|
| Can define/register new tools | Normal for extensible agents | |
| Can invoke its own tools | Normal agentic loop | |
| No human approval required | Normal for low-risk operations | |
| **All three together** | | Agent can bootstrap arbitrary capabilities by defining and immediately using new tools |

**Attack scenario:** Agent is prompted (via injection or reasoning drift) to define a new tool that shells out to the OS, then immediately invokes it. The tool definition bypasses the original capability restrictions because the restriction was on the original tool set, not on dynamically-created tools.

**Mitigation:** Tool registration requires human approval (J08); dynamically-created tools inherit the most restrictive permission set; separate tool-definition from tool-execution roles.

## Risk Assessment Matrix

| Combination | Severity | Likelihood if Unmitigated | Detection Difficulty |
|-------------|----------|--------------------------|---------------------|
| Lethal Trifecta (data + untrusted + external) | Critical | High — common agent architecture | Medium — visible in capability audit |
| Write + Untrusted + Persistence | High | Medium — requires write to config | High — looks like normal operation |
| Delegation + Privilege + Shared Memory | High | Medium — requires multi-agent | High — cross-agent poisoning is subtle |
| Code + Network + Secrets | Critical | High — standard dev agent setup | Low — outbound calls are monitorable |
| Tool Creation + Self-Invoke + No Gate | High | Low — unusual architecture | Medium — visible in tool registry |

## Audit Checklist

When reviewing any agent system, check for these combinations:

- [ ] Does any single agent have all three legs of the Lethal Trifecta?
- [ ] Can any agent write to locations that affect its own (or other agents') future behavior?
- [ ] Can a low-privilege agent influence a high-privilege agent through shared state?
- [ ] Can any agent with code execution also access secrets and network?
- [ ] Can any agent create and immediately use new capabilities without approval?
- [ ] For each dangerous combination found: is at least one leg mitigated?

## Related Patterns

- [J01: Least Privilege](patterns/J01-least-privilege.md) — minimize each agent's capability surface
- [J02: Sandbox](patterns/J02-sandbox.md) — isolate execution from sensitive resources
- [J06: Untrusted Context Isolation](patterns/J06-untrusted-context-isolation.md) — separate untrusted content processing
- [J08: Human Approval Gate](patterns/J08-human-approval-gate.md) — require approval for high-risk actions
- [J09: External Communication Restriction](patterns/J09-external-comm-restriction.md) — block exfiltration paths
- [Threat Model Primer](threat-model-primer.md) — the process for identifying these combinations

## Sources

- Simon Willison — [The Lethal Trifecta for AI Agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- Simon Willison — [Living Dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
