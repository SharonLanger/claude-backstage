# Anti-Pattern Detector: Symptoms to Diagnosis

## Scenario

Your agent system has a problem but you're not sure what's causing it. You observe symptoms — loops, wrong outputs, high costs, unreliable behavior — and want to identify which named anti-pattern you may have stumbled into, so you can apply the correct fix.

## Quick Answer

1. **Match your symptoms** in the table below to identify the likely anti-pattern.
2. **Confirm with the diagnostic questions** for that anti-pattern.
3. **Apply the recommended fix patterns** to address the root cause.

## Symptom → Anti-Pattern Lookup

| Symptom You Observe | Likely Anti-Pattern | Fix Direction |
|--------------------|--------------------|---------------|
| Agent runs for a very long time, uses many tokens, and eventually times out or hits a limit | [Infinite Weakly-Bounded Loop](#infinite-weakly-bounded-loop) | Add real stop conditions |
| Agent retries the same action repeatedly with the same result | [Retry Without New Information](#retry-without-new-information) | Change strategy on retry |
| System uses 5+ agents but a single agent could do the job | [Multi-Agent by Default](#multi-agent-by-default) | Simplify to fewer agents |
| You optimized for cost/speed but output quality dropped without anyone noticing | [Silent Quality Degradation](#silent-quality-degradation) | Add quality monitoring |
| You spent weeks on caching/routing/optimization before validating core quality | [Premature Optimization](#premature-optimization) | Get quality right first |

---

## Detailed Anti-Pattern Profiles

### Infinite Weakly-Bounded Loop

**File**: [../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md)

**Symptoms**:
- Agent execution time is unpredictable — sometimes 10 seconds, sometimes 10 minutes
- Token costs spike unexpectedly on certain inputs
- Agent "spins" doing similar actions without converging
- You set a high iteration limit (e.g., 100) "just to be safe" and it actually hits it

**Diagnostic Questions**:
- Does your loop have a maximum iteration count? What is it? (If > 10 for most tasks, suspect this)
- Does the loop have a *meaningful* exit condition beyond "max iterations reached"?
- Can you articulate what "done" means in concrete terms the agent can check?
- Does the agent's strategy change after repeated failures, or does it keep trying the same approach?

**Root Cause**: The loop's termination condition is either missing, too permissive, or not based on actual progress metrics.

**Fix Patterns**:
- [Bounded Loop](../../families/A-workflow-topology/patterns/bounded-loop.md) — Set tight, realistic iteration limits
- [Stop Condition](../../families/I-reliability-recovery/patterns/stop-condition.md) — Define explicit "done" criteria
- [Cost-Aware Stopping](../../families/N-efficiency-routing/patterns/cost-aware-stopping.md) — Stop when cost exceeds value
- [Circuit Breaker](../../families/I-reliability-recovery/patterns/circuit-breaker.md) — Cut off after repeated failures

---

### Retry Without New Information

**File**: [../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md)

**Symptoms**:
- Agent fails, retries with identical or near-identical input, fails again
- Retry logs show the same error message repeating
- "Maybe it'll work this time" logic (pure retry with no mutation)
- Agent exhausts all retries and still produces the same wrong answer

**Diagnostic Questions**:
- When the agent retries, what specifically changes between attempts?
- Does the retry include the error message from the previous attempt?
- Is there a mechanism to try a *different approach* on failure, not just the same approach again?
- Would a human looking at the first failure know that retrying identically is pointless?

**Root Cause**: The retry mechanism doesn't incorporate new information (error feedback, different strategy, modified context) between attempts.

**Fix Patterns**:
- [Retry with Feedback](../../families/I-reliability-recovery/patterns/retry-with-feedback.md) — Include error info in next attempt
- [Root Cause Before Retry](../../families/I-reliability-recovery/patterns/root-cause-before-retry.md) — Diagnose before retrying
- [Fresh Context Retry](../../families/I-reliability-recovery/patterns/fresh-context-retry.md) — Start from clean state
- [Fallback Model Workflow](../../families/I-reliability-recovery/patterns/fallback-model-workflow.md) — Try a different model/approach
- [Structured Error Classification](../../families/I-reliability-recovery/patterns/structured-error-classification.md) — Categorize error to choose strategy

---

### Multi-Agent by Default

**File**: [../../families/C-orchestration/anti-patterns/multi-agent-by-default.md](../../families/C-orchestration/anti-patterns/multi-agent-by-default.md)

**Symptoms**:
- System has many agents but most are thin wrappers around a single prompt
- Debugging requires tracing through 4+ handoffs to find where things went wrong
- Agents frequently pass large contexts to each other (information loss at each hop)
- Adding a feature requires updating 3+ agent prompts
- "Coordinator" agent spends most of its time reformatting outputs for the next agent

**Diagnostic Questions**:
- Could you collapse 2-3 of these agents into one with a better prompt?
- Are agents genuinely specialized (different tools, different expertise) or just segmented by step?
- How much context is lost at each handoff?
- Is the coordination logic more complex than the actual task logic?

**Root Cause**: Defaulting to multi-agent architecture out of organizational habit or premature separation of concerns, rather than genuine need for specialization.

**Fix Patterns**:
- [Prompt Chaining](../../families/A-workflow-topology/patterns/prompt-chaining.md) — Single agent, multiple steps
- [Sequential Workflow](../../families/A-workflow-topology/patterns/sequential-workflow.md) — One agent with structured flow
- [Context Isolation](../../families/E-context-engineering/patterns/context-isolation.md) — If you DO need multi-agent, minimize handoff cost
- [Minimal Context Handoff](../../families/E-context-engineering/patterns/minimal-context-handoff.md) — Pass only what the next step needs

---

### Silent Quality Degradation

**File**: [../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md)

**Symptoms**:
- You switched to a cheaper/faster model and metrics "look fine" but users complain
- Output passes all format checks but is subtly less helpful, less accurate, or less complete
- You added caching and stopped noticing that cached responses don't fit new contexts
- Eval scores stayed flat but user satisfaction dropped

**Diagnostic Questions**:
- Do your evals measure quality at the level users care about, or just format/schema compliance?
- Did you A/B test the optimization against the baseline on *quality* metrics (not just cost)?
- Are users reporting dissatisfaction that doesn't show up in your automated metrics?
- Could your evals be "gamed" by an output that's technically valid but unhelpful?

**Root Cause**: Optimization (cost, speed, simplicity) was applied without adequate quality monitoring, so degradation goes undetected by automated systems.

**Fix Patterns**:
- [LLM-as-Judge](../../families/D-verification-evaluation/patterns/D04-LLM-as-judge.md) — Add quality-sensitive evaluation
- [Regression Suite](../../families/D-verification-evaluation/patterns/D08-regression-suite.md) — Catch quality drops on known cases
- [Complexity-Based Model Routing](../../families/N-efficiency-routing/patterns/complexity-based-model-routing.md) — Route by difficulty, not uniformly cheap
- [Confidence-Based Routing](../../families/N-efficiency-routing/patterns/confidence-based-routing.md) — Escalate uncertain cases to better models

---

### Premature Optimization

**File**: [../../families/N-efficiency-routing/anti-patterns/premature-optimization.md](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md)

**Symptoms**:
- You built caching, routing, and cost optimization before knowing if the agent produces correct output
- System is complex but basic quality is poor
- You're debugging cache invalidation issues on a feature that doesn't reliably work yet
- Team discusses model routing strategies but hasn't established quality baselines

**Diagnostic Questions**:
- Do you have a working, validated version using the most capable model before optimizing?
- Can you articulate your quality bar numerically (what score on what metric)?
- Are you optimizing for cost/speed BEFORE or AFTER establishing that quality is acceptable?
- Would removing all optimizations and just using the best model solve the core problem?

**Root Cause**: Optimizing secondary concerns (cost, speed, architecture elegance) before the primary concern (correct, useful output) is solved.

**Fix Patterns**:
- Start with [Prompt Chaining](../../families/A-workflow-topology/patterns/prompt-chaining.md) on the best model
- Establish quality with [Regression Suite](../../families/D-verification-evaluation/patterns/D08-regression-suite.md)
- THEN optimize with [Small Model First Escalation](../../families/N-efficiency-routing/patterns/small-model-first-escalation.md)
- Use [Caching](../../families/N-efficiency-routing/patterns/caching.md) only after quality is stable

---

## Compound Anti-Patterns

Sometimes multiple anti-patterns combine. Common toxic combinations:

| Combination | Result | How to Tell |
|-------------|--------|-------------|
| Infinite Loop + Retry Without Info | Agent loops forever retrying the same failed action | Same error in logs 50+ times |
| Multi-Agent + Silent Degradation | Each handoff loses a little quality; end result is much worse | Final output worse than any single agent would produce |
| Premature Optimization + Silent Degradation | You optimized away quality you hadn't measured | Users hate it but your metrics say it's fine |

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- https://hamel.dev/blog/posts/evals-faq/
