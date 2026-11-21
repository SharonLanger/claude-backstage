# Reducing End-to-End Latency

## Scenario

Your agent system produces correct results but takes too long. Users experience unacceptable wait times, or downstream systems time out. You need to reduce end-to-end latency while preserving output quality.

## Quick Answer

1. **Parallelize independent work** — if subtasks don't depend on each other, run them simultaneously. Use [A-Parallel-Sectioning](../../families/A-workflow-topology/patterns/parallel-sectioning.md) and [N-Parallel-Execution](../../families/N-efficiency-routing/patterns/parallel-execution.md).
2. **Eliminate unnecessary sequential steps** — every LLM call adds latency. Remove verification steps that don't catch real errors, flatten chains where possible.
3. **Route to faster models for simple tasks** — smaller models respond faster. Use [N-Small-Model-First-Escalation](../../families/N-efficiency-routing/patterns/small-model-first-escalation.md) for the speed benefit, not just cost.

## Latency Reduction Strategies

### Strategy 1: Parallelization

The highest-impact latency reduction comes from running independent operations concurrently rather than sequentially.

**Identify parallelizable work:**
- Multiple documents to process independently
- Several tool calls that don't depend on each other's results
- Validation checks that can run simultaneously
- Multiple specialists that can work on different aspects of a problem at once

**Patterns:**
- [A-Parallel-Sectioning](../../families/A-workflow-topology/patterns/parallel-sectioning.md) — split work across parallel branches, aggregate results
- [A-Parallel-Voting](../../families/A-workflow-topology/patterns/parallel-voting.md) — run multiple approaches in parallel, pick best result
- [N-Parallel-Execution](../../families/N-efficiency-routing/patterns/parallel-execution.md) — execute independent operations concurrently

### Strategy 2: Reduce Sequential Depth

Every step in a chain adds its full latency. Flatten where possible.

| Instead of... | Consider... |
|---------------|-------------|
| 5-step sequential chain | 2 steps with richer prompts that do more per call |
| Plan → Validate plan → Execute → Validate result | Plan+Execute → Validate result (combine planning into execution) |
| Retrieve → Summarize → Analyze | Retrieve → Analyze directly (skip summarization if model can handle full context) |
| Generate → Check → Regenerate | Generate with constraints that reduce need for checking |

### Strategy 3: Smarter Model Selection

| Task Type | Model Choice | Latency Impact |
|-----------|--------------|----------------|
| Classification/routing | Small, fast model | 100-300ms vs 1-3s |
| Extraction from structured data | Small model or code | Near-instant |
| Complex reasoning | Frontier model | Accept the latency here |
| Deterministic validation | Code (no LLM) | Eliminates LLM latency entirely |

### Strategy 4: Caching and Pre-computation

- **Cache frequent queries**: If users ask similar questions, cache responses. Apply [N-Caching](../../families/N-efficiency-routing/patterns/caching.md).
- **Pre-compute embeddings**: Don't compute at query time what you can compute at index time.
- **Warm tool results**: For predictable tool calls, pre-fetch results before the agent requests them.
- **Reuse within sessions**: Apply [N-Tool-Result-Reuse](../../families/N-efficiency-routing/patterns/tool-result-reuse.md) to avoid redundant tool calls.

### Strategy 5: Early Termination

- **Stop when good enough**: Use [N-Cost-Aware-Stopping](../../families/N-efficiency-routing/patterns/cost-aware-stopping.md) — if an iterative loop produces acceptable quality early, stop.
- **Confidence-based shortcuts**: If a routing step is highly confident, skip verification. Apply [N-Confidence-Based-Routing](../../families/N-efficiency-routing/patterns/confidence-based-routing.md).
- **Bounded loops**: Use [A-Bounded-Loop](../../families/A-workflow-topology/patterns/bounded-loop.md) with tight iteration limits.

## Decision Guide

```
Where is latency accumulating?
│
├── Sequential LLM calls (most common)
│   ├── Steps are independent → Parallelize them
│   ├── Steps could be merged → Combine into fewer, richer prompts
│   └── Steps are truly sequential → Optimize each step individually
│
├── Long model response times
│   ├── Using large model for simple tasks → Route to smaller/faster model
│   ├── Generating very long outputs → Constrain output length
│   └── Complex reasoning required → Accept latency, optimize elsewhere
│
├── Tool/API call latency
│   ├── Repeated identical calls → Cache results
│   ├── Multiple independent calls → Run in parallel
│   └── Slow external APIs → Add timeouts and fallbacks
│
└── Unnecessary work
    ├── Validation that rarely catches errors → Remove or make async
    ├── Redundant verification steps → Consolidate
    └── Over-cautious retry loops → Tighten stop conditions
```

## Relevant Patterns

| Pattern | Latency Reduction Mechanism |
|---------|------------------------------|
| [A-Parallel-Sectioning](../../families/A-workflow-topology/patterns/parallel-sectioning.md) | Run independent subtasks concurrently |
| [A-Parallel-Voting](../../families/A-workflow-topology/patterns/parallel-voting.md) | Parallel generation with fast selection |
| [N-Parallel-Execution](../../families/N-efficiency-routing/patterns/parallel-execution.md) | Concurrent tool calls and operations |
| [N-Small-Model-First-Escalation](../../families/N-efficiency-routing/patterns/small-model-first-escalation.md) | Fast model for simple tasks, escalate only when needed |
| [N-Confidence-Based-Routing](../../families/N-efficiency-routing/patterns/confidence-based-routing.md) | Skip steps when confidence is high |
| [N-Caching](../../families/N-efficiency-routing/patterns/caching.md) | Eliminate redundant computation |
| [N-Tool-Result-Reuse](../../families/N-efficiency-routing/patterns/tool-result-reuse.md) | Avoid repeating tool calls |
| [N-Cost-Aware-Stopping](../../families/N-efficiency-routing/patterns/cost-aware-stopping.md) | Terminate early when quality is sufficient |
| [A-Bounded-Loop](../../families/A-workflow-topology/patterns/bounded-loop.md) | Cap iterations to prevent runaway latency |
| [H01-Deterministic-Override](../../families/H-deterministic-control/patterns/H01-deterministic-override.md) | Replace LLM calls with instant code checks |
| [A-Prompt-Chaining](../../families/A-workflow-topology/patterns/prompt-chaining.md) | Design efficient chains with minimal steps |
| [I-Circuit-Breaker](../../families/I-reliability-recovery/patterns/circuit-breaker.md) | Fail fast on slow/failing dependencies |

## Anti-Patterns to Watch For

| Anti-Pattern | Problem |
|--------------|---------|
| [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md) | Optimizing latency before the system works correctly |
| [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) | Cutting steps that silently reduce quality to save time |
| Sequential by default | Running steps serially without checking if they can be parallel |
| Over-verification | Adding safety checks that rarely trigger but always add latency |

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/index/harness-engineering/
- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
