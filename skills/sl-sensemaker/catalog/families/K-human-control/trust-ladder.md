# Guide: The Trust Ladder

## Purpose

Use this guide to understand and implement the progression from full human control to full agent autonomy. The ladder defines discrete levels with explicit criteria for moving up or down — preventing both premature trust and unnecessary bottlenecks.

## The Ladder

```
    ┌─────────────────────────────────────────────────────────┐
    │  Level 5: AUTONOMOUS                                    │
    │  Agent operates independently; human reviews periodic   │
    │  summaries only                                         │
    ├─────────────────────────────────────────────────────────┤
    │  Level 4: SUPERVISED                                    │
    │  Agent acts on routine tasks; escalates exceptions      │
    │  to human                                               │
    ├─────────────────────────────────────────────────────────┤
    │  Level 3: DELEGATED                                     │
    │  Agent executes approved plans; human monitors          │
    │  output stream                                          │
    ├─────────────────────────────────────────────────────────┤
    │  Level 2: COLLABORATIVE                                 │
    │  Agent proposes; human approves each action             │
    │                                                         │
    ├─────────────────────────────────────────────────────────┤
    │  Level 1: ADVISORY                                      │
    │  Agent provides information; human decides and acts     │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
```

## Level Definitions

### Level 1: Advisory

**Agent behavior:** Answers questions, surfaces information, generates options. Never takes action.

**Human role:** Makes all decisions. Executes all actions. The agent is a search/analysis tool.

**Appropriate when:**
- First deployment of a new agent capability
- High-sensitivity domains (security, finance, legal)
- The team has no track record with the agent
- The task is novel and the failure mode is unknown

**Example:** "What are the three most likely root causes of this error?" — human investigates and fixes.

**Promotion criteria to Level 2:**
- Agent's suggestions have been correct >90% of the time over 20+ interactions
- The team understands what the agent can and cannot do
- Failure modes at this level are well-characterized

---

### Level 2: Collaborative

**Agent behavior:** Proposes specific actions (diffs, commands, messages). Waits for explicit approval before executing any of them.

**Human role:** Reviews every proposed action. Approves, modifies, or rejects. The agent is a junior colleague who checks everything.

**Appropriate when:**
- The agent has demonstrated good judgment at Level 1
- Actions are reversible but could cause confusion if wrong
- The human wants to build calibration on agent quality

**Example:** "I propose this code change: [diff]. Approve?" — human reviews and approves.

**Promotion criteria to Level 3:**
- Human approval rate >95% over 50+ proposals (i.e., rarely rejects or modifies)
- No safety-relevant errors in the last N proposals
- The human finds the approval step adds latency without catching errors

---

### Level 3: Delegated

**Agent behavior:** Executes an approved plan end-to-end. Reports results after completion. Pauses on unexpected situations.

**Human role:** Approves the plan upfront. Monitors the output log. Can interrupt. Reviews the final result.

**Appropriate when:**
- The plan is reviewable (human can understand what will happen before it starts)
- Each step is reversible or the overall result is verifiable
- The agent has a consistent track record at Level 2

**Example:** "Here's my plan to refactor this module [5 steps]. Approved? ... Done. Here's what changed." — human reviews the summary.

**Promotion criteria to Level 4:**
- Agent handles unexpected situations appropriately (pauses or resolves correctly)
- Human monitoring adds no value — they never catch something the agent missed
- Completion rate without intervention >98% over 30+ delegated tasks

---

### Level 4: Supervised

**Agent behavior:** Handles routine tasks silently. Escalates to human only when it encounters something outside its confidence threshold or outside its authorized scope.

**Human role:** Available for escalation. Reviews periodic summaries. Sets the boundary of "routine."

**Appropriate when:**
- The task is repetitive and well-understood
- The agent has demonstrated reliable exception detection
- There is automated verification (tests pass, linting clean, etc.)
- Failures are detectable within a reasonable timeframe

**Example:** Agent processes incoming bug reports: triages, labels, assigns. Escalates unclear reports or security issues. Human reviews the escalation queue daily.

**Promotion criteria to Level 5:**
- Escalation rate has stabilized at a low percentage
- Escalated items are genuinely ambiguous (not things the agent should have handled)
- Automated rollback exists for agent errors
- No human intervention has been required for >100 consecutive tasks

---

### Level 5: Autonomous

**Agent behavior:** Operates independently on its defined domain. Produces periodic reports. No real-time human involvement.

**Human role:** Sets goals and boundaries. Reviews periodic reports. Adjusts parameters. Conducts occasional audits.

**Appropriate when:**
- The domain is fully characterized — no novel situations expected
- Automated verification catches all known failure modes
- Automated rollback exists for all reversible errors
- The blast radius of any single failure is bounded and acceptable
- There is a comprehensive eval suite measuring ongoing quality

**Example:** Automated code formatting on every commit. Automated dependency update PRs with auto-merge when tests pass.

**No promotion beyond Level 5.** Periodic audits can reveal the need for demotion.

---

## Demotion Rules

Moving DOWN the ladder is as important as moving up. Demotion is not failure — it is correct calibration.

| Trigger | Action |
|---------|--------|
| Agent makes an error a human at current level would have caught | Drop one level |
| Environment changes significantly (new tools, new data, new constraints) | Drop to Level 2 until recalibrated |
| Security incident involving the agent | Drop to Level 1 pending investigation |
| Agent's success rate drops below level threshold | Drop one level |
| New capability added to agent | Drop to Level 2 for the new capability |
| Agent produces output the team cannot explain | Drop one level pending understanding |

## Key Principle: Level Per Task, Not Per Agent

An agent can be at different levels for different tasks simultaneously:

- Level 4 for code formatting (well-understood, reversible, auto-verifiable)
- Level 2 for database migrations (high blast radius, partially irreversible)
- Level 1 for security-related changes (high sensitivity, novel situations)

## Implementation Notes

- **Enforce levels architecturally, not just culturally.** Level 2 means there IS an approval gate in the code — not just an agreement to check.
- **Track metrics per agent-task pair.** Success rate, intervention rate, escalation quality.
- **Make promotion explicit.** Someone decides "this agent is now Level 3 for task X" — it does not drift upward silently.
- **Audit Level 5 periodically.** Autonomous agents degrade without anyone noticing. Schedule quarterly reviews.

## Related Patterns

- [Autonomy Calibration Guide](autonomy-calibration-guide.md) — the factors that determine appropriate level
- [K patterns](patterns/) — specific patterns implementing each level
- [J08: Human Approval Gate](../J-security-trust/patterns/J08-human-approval-gate.md) — the mechanism for Level 2

## Sources

- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- OpenAI — [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
