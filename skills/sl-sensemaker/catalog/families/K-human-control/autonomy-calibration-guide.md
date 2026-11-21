# Guide: Autonomy Calibration

## Purpose

Use this guide when deciding how much autonomy to grant an agent for a given task, user, or domain. Autonomy is not binary — it exists on a spectrum, and the right level depends on risk, trust evidence, and reversibility.

## The Autonomy Spectrum

```
Full Human Control ←――――――――――――――――――――――――――――→ Full Autonomy

[1]          [2]            [3]            [4]           [5]
Human does   Agent drafts   Agent acts     Agent acts    Agent acts
everything   Human approves Human monitors on exception  fully alone
```

| Level | Agent Behavior | Human Role | Example |
|-------|---------------|------------|---------|
| 1 — Manual | Agent provides information only | Human makes all decisions and takes all actions | "Show me the options" |
| 2 — Suggest | Agent proposes actions, waits for approval | Human approves every action | "Here's my plan — approve?" |
| 3 — Act & Report | Agent acts, reports what it did | Human monitors output stream, can intervene | "I did X, Y, Z — here's the summary" |
| 4 — Act on Exception | Agent acts silently on routine tasks, escalates exceptions | Human handles escalations only | "Everything normal except this — what should I do?" |
| 5 — Full Autonomy | Agent acts without reporting | Human reviews periodically or not at all | Scheduled batch processing |

## Calibration Factors

Use these factors to determine the appropriate level for a specific agent-task pair:

### Factor 1: Reversibility

| Reversibility | Appropriate Level |
|--------------|-------------------|
| Fully reversible (can undo with no cost) | 3–5 |
| Partially reversible (some cost to undo) | 2–3 |
| Irreversible (cannot undo) | 1–2 |

### Factor 2: Blast Radius

| Blast Radius | Appropriate Level |
|-------------|-------------------|
| Affects only the requesting user | 3–5 |
| Affects a team or shared resource | 2–3 |
| Affects customers or production | 1–2 |

### Factor 3: Task Familiarity

| Familiarity | Appropriate Level |
|-------------|-------------------|
| Agent has succeeded at this exact task type 100+ times | 4–5 |
| Agent has succeeded at similar tasks | 3–4 |
| Novel task type for this agent | 1–2 |

### Factor 4: Failure Detectability

| Detectability | Appropriate Level |
|--------------|-------------------|
| Failures are immediately obvious (build breaks, test fails) | 3–5 |
| Failures are detectable but delayed (wrong output noticed later) | 2–3 |
| Failures are subtle (logical errors, data corruption) | 1–2 |

### Factor 5: Domain Sensitivity

| Sensitivity | Appropriate Level |
|-------------|-------------------|
| Non-sensitive (documentation, formatting) | 4–5 |
| Moderate (internal code, test data) | 3–4 |
| High (customer data, financial, security) | 1–2 |

## Calibration Formula

Take the minimum across all factors. The most restrictive factor determines the ceiling.

```
Autonomy Level = min(Reversibility, Blast Radius, Familiarity, Detectability, Sensitivity)
```

Example: An agent that formats code (reversible=5, blast=4, familiar=5, detectable=5, sensitive=5) → Level 4–5.

Example: An agent that deploys to production (reversible=2, blast=1, familiar=3, detectable=3, sensitive=2) → Level 1–2.

## Increasing Autonomy Over Time

Autonomy should increase based on demonstrated performance, not on schedule:

1. **Start at Level 2** for any new agent-task combination.
2. **Promote to Level 3** after N successful completions with no interventions (N depends on blast radius — higher blast radius = higher N).
3. **Promote to Level 4** after the agent has handled exceptions correctly without human input.
4. **Promote to Level 5** only if: the domain is low-sensitivity, failures are auto-detectable, and there is an automated rollback mechanism.

**Demotion triggers** — drop one level immediately when:
- The agent makes an error that a human at the current level would have caught
- The task environment changes (new tools, new constraints, new data)
- A security-relevant incident occurs
- The agent's success rate drops below threshold

## Implementation Checklist

- [ ] Defined the autonomy level for each agent-task pair (not per agent globally)
- [ ] The level is enforced architecturally (approval gates, not just instructions)
- [ ] Promotion criteria are explicit and measurable
- [ ] Demotion triggers are defined and automated where possible
- [ ] High-autonomy agents have automated failure detection (tests, assertions, monitors)
- [ ] Level 5 agents have automated rollback mechanisms

## Related Patterns

- [Trust Ladder](trust-ladder.md) — the progression framework for building trust over time
- [J08: Human Approval Gate](../J-security-trust/patterns/J08-human-approval-gate.md) — mechanism for Level 2 enforcement
- [K patterns](patterns/) — full set of human-in-the-loop patterns

## Sources

- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- OpenAI — [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
