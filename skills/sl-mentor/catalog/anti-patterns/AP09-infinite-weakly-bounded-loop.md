# AP09 — Infinite / Weakly Bounded Agent Loop

## Symptoms

- The agent runs for hours or consumes thousands of dollars in tokens before anyone notices
- Loop termination depends on the model deciding it is "done" with no hard deadline
- Token or time budgets exist on paper but are set so high they never trigger in practice
- The agent gets stuck in a cycle — trying the same approach, failing, and trying again — without escalating
- There is no maximum iteration count, or it is set to an absurdly high number "just in case"
- Runaway costs appear in billing before the system halts itself

## Root Cause

Teams trust the model to know when to stop. They implement loops (ReAct, tool-calling cycles, iterative refinement) without hard bounds because they fear that a tight limit might cut off a productive agent mid-task. The result is the opposite problem: an unproductive agent that burns resources indefinitely. The model lacks a reliable internal sense of diminishing returns — it will continue trying approaches, generating plausible but unhelpful output, as long as the loop allows. Hard bounds with escalation paths (timeout → human review, budget cap → checkpoint and ask) are the engineering discipline that agent loops require.

## Failure Scenario

A data analysis agent is asked to "find anomalies in the sales data and explain their root causes." The agent queries the database, identifies some patterns, generates hypotheses, queries again to test them, finds the results inconclusive, generates new hypotheses, and repeats. There is no iteration limit because the developer thought "it should stop when it has a good answer." After 847 iterations over 6 hours, the agent has spent $340 in API costs and produced a 200-page "analysis" that is mostly circular reasoning. It never stopped because each iteration produced slightly different output, so the model believed it was making progress. A 20-iteration cap with a "present best findings and escalate" fallback would have produced a useful 2-page report in 10 minutes.

## Counter-Patterns

- [I09 — Stop Condition](../families/I-reliability-recovery/patterns/stop-condition.md) — Define explicit termination criteria for every loop
- [A01 — Bounded Loop](../families/A-workflow-topology/patterns/bounded-loop.md) — Hard iteration limits with escalation on breach
- [N06 — Cost-Aware Stopping](../families/N-efficiency-routing/patterns/cost-aware-stopping.md) — Stop when marginal cost exceeds expected value
- [K03 — Failure Threshold Escalation](../families/K-human-control/patterns/K03-failure-threshold-escalation.md) — Escalate to humans when the agent is stuck

## Sources

- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
