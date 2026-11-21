# Cutting Token Usage and API Spend

## Scenario

Your agent system works correctly but costs too much to operate. You need to reduce token consumption and API spend without sacrificing output quality — or you need to identify where the biggest cost savings are before committing to architectural changes.

## Quick Answer

1. **Minimize context per call** — most agents carry far more context than they need. Apply [E-Context-Compaction](../../families/E-context-engineering/patterns/context-compaction.md) and [N-Context-Minimization](../../families/N-efficiency-routing/patterns/context-minimization.md) to send only what's relevant.
2. **Route to cheaper models when possible** — not every task needs your most capable model. Use [N-Small-Model-First-Escalation](../../families/N-efficiency-routing/patterns/small-model-first-escalation.md) and [N-Complexity-Based-Model-Routing](../../families/N-efficiency-routing/patterns/complexity-based-model-routing.md).
3. **Cache and reuse** — avoid regenerating the same outputs. Apply [N-Caching](../../families/N-efficiency-routing/patterns/caching.md) and [N-Tool-Result-Reuse](../../families/N-efficiency-routing/patterns/tool-result-reuse.md).

## Cost Reduction Checklist

### High Impact (usually 30-70% savings)

- [ ] **Audit context size**: Measure actual tokens per call. Are you sending full documents when summaries would suffice?
- [ ] **Route simple tasks to smaller models**: Classification, extraction, and formatting tasks rarely need frontier models.
- [ ] **Cache repeated computations**: If multiple runs process the same documents/queries, cache results.
- [ ] **Stop loops early**: Use [N-Cost-Aware-Stopping](../../families/N-efficiency-routing/patterns/cost-aware-stopping.md) to terminate when output quality plateaus.
- [ ] **Reduce retry waste**: Fix root causes of failures rather than retrying expensive operations. See [I-Root-Cause-Before-Retry](../../families/I-reliability-recovery/patterns/root-cause-before-retry.md).

### Medium Impact (usually 10-30% savings)

- [ ] **Summarize long contexts**: Use [E-Context-Compaction](../../families/E-context-engineering/patterns/context-compaction.md) to compress conversation history and documents.
- [ ] **Scope memory**: Use [L-Scoped-Memory](../../families/L-memory-state/patterns/scoped-memory.md) so agents retrieve only task-relevant history.
- [ ] **Batch related calls**: Combine multiple small prompts into one structured call where possible.
- [ ] **Progressive disclosure**: Send context in stages — start minimal, add detail only if needed. Apply [E-Progressive-Disclosure](../../families/E-context-engineering/patterns/progressive-disclosure.md).
- [ ] **Reuse tool results**: Cache tool call outputs within a session. Apply [N-Tool-Result-Reuse](../../families/N-efficiency-routing/patterns/tool-result-reuse.md).

### Lower Impact (optimization polish)

- [ ] **Tighten output schemas**: Request structured output to reduce verbose free-text responses.
- [ ] **Use token budgets**: Set explicit max-token limits on responses where appropriate.
- [ ] **Parallelize for wall-clock savings** (doesn't reduce tokens but reduces time-cost of expensive runs).
- [ ] **Monitor and alert**: Use [M06-Token-Cost-Metrics](../../families/M-observability-debugging/patterns/M06-token-cost-metrics.md) to track spend by agent, task, and model.

## Decision Guide: Where to Cut First

```
What's your biggest cost driver?
│
├── Large context windows (lots of input tokens)
│   ├── Sending full documents → Summarize or chunk, use just-in-time retrieval
│   ├── Long conversation history → Compact with sliding window or summary
│   └── Redundant system prompts → Factor out common instructions, use caching
│
├── Many iterations per task (lots of API calls)
│   ├── Retrying failures → Fix root causes, use feedback-enriched retries
│   ├── Unnecessary verification loops → Tighten output constraints upfront
│   └── Overly cautious stopping → Set clearer done-criteria
│
├── Using expensive models for everything
│   ├── Simple routing/classification → Use small models
│   ├── Deterministic validation → Use code, not LLM
│   └── Boilerplate generation → Template + fill, not full generation
│
└── Redundant computation across runs
    ├── Same inputs, same outputs → Cache results
    ├── Multiple agents doing same retrieval → Share tool results
    └── Repeated embeddings/lookups → Pre-compute and store
```

## Relevant Patterns

| Pattern | Cost Reduction Mechanism |
|---------|--------------------------|
| [N-Context-Minimization](../../families/N-efficiency-routing/patterns/context-minimization.md) | Send less input → fewer input tokens |
| [N-Small-Model-First-Escalation](../../families/N-efficiency-routing/patterns/small-model-first-escalation.md) | Use cheap models for easy tasks |
| [N-Complexity-Based-Model-Routing](../../families/N-efficiency-routing/patterns/complexity-based-model-routing.md) | Match model capability to task difficulty |
| [N-Caching](../../families/N-efficiency-routing/patterns/caching.md) | Avoid repeating identical work |
| [N-Tool-Result-Reuse](../../families/N-efficiency-routing/patterns/tool-result-reuse.md) | Share results across agents/steps |
| [N-Cost-Aware-Stopping](../../families/N-efficiency-routing/patterns/cost-aware-stopping.md) | Stop iterations when value diminishes |
| [N-Budgeted-Agent-Loop](../../families/N-efficiency-routing/patterns/budgeted-agent-loop.md) | Hard caps on total spend per task |
| [E-Context-Compaction](../../families/E-context-engineering/patterns/context-compaction.md) | Compress history to reduce token count |
| [E-Progressive-Disclosure](../../families/E-context-engineering/patterns/progressive-disclosure.md) | Load context incrementally, not all at once |
| [L-Summarized-Memory](../../families/L-memory-state/patterns/summarized-memory.md) | Replace full history with compressed summaries |
| [H01-Deterministic-Override](../../families/H-deterministic-control/patterns/H01-deterministic-override.md) | Replace LLM calls with code where possible |
| [M06-Token-Cost-Metrics](../../families/M-observability-debugging/patterns/M06-token-cost-metrics.md) | Measure to find where spend concentrates |

## Anti-Patterns to Watch For

| Anti-Pattern | Problem |
|--------------|---------|
| [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md) | Optimizing costs before validating that the system works correctly |
| [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) | Cutting costs in ways that silently harm output quality |
| [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) | Expensive retries that are unlikely to succeed |
| Sending full context to every agent | Burning tokens on irrelevant information |

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/index/harness-engineering/
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
