# Routing Requests to the Right Model/Tier and Scaling Patterns

## Scenario

You have an agent system handling diverse requests and need to route each request to the appropriate model, capability tier, or processing path. You want to avoid using expensive frontier models for simple tasks, while ensuring complex tasks get the capability they need.

## Quick Answer

1. **Classify complexity upfront** — use a fast, cheap model (or code heuristics) to classify incoming requests before routing them. Apply [N-Complexity-Based-Model-Routing](../../families/N-efficiency-routing/patterns/complexity-based-model-routing.md).
2. **Start small, escalate on failure** — attempt with a smaller model first; if it fails validation, retry with a more capable one. Use [N-Small-Model-First-Escalation](../../families/N-efficiency-routing/patterns/small-model-first-escalation.md).
3. **Use deterministic routing where possible** — many routing decisions can be made with code (keyword matching, regex, structured metadata) rather than an LLM call. Apply [A-Routing](../../families/A-workflow-topology/patterns/routing.md).

## Routing Decision Framework

### When to Route with Code (Deterministic)

Use deterministic routing when the classification signal is clear:

- **Keyword/pattern matching**: Request contains specific keywords, file types, or structured commands
- **Metadata-based**: User tier, request source, content length, language
- **Historical**: Same user/query pattern has been seen before (cached classification)
- **Schema-driven**: Input matches a specific tool schema or format

Pattern: [A-Routing](../../families/A-workflow-topology/patterns/routing.md), [H01-Deterministic-Override](../../families/H-deterministic-control/patterns/H01-deterministic-override.md)

### When to Route with an LLM (Semantic)

Use LLM-based routing when the decision requires understanding intent:

- **Ambiguous requests**: "Help me with this" — needs intent classification
- **Multi-domain**: Could belong to multiple specialist agents
- **Complexity estimation**: Requires understanding the reasoning depth needed

Pattern: [N-Confidence-Based-Routing](../../families/N-efficiency-routing/patterns/confidence-based-routing.md)

### When to Use Escalation (Try-and-Fallback)

Use escalation when you cannot predict difficulty upfront:

- **Variable complexity**: Same category of request spans easy to hard
- **Cost sensitivity**: Worth attempting cheap first even with some failures
- **Quality validation available**: You can detect when the small model fails

Pattern: [N-Small-Model-First-Escalation](../../families/N-efficiency-routing/patterns/small-model-first-escalation.md)

## Routing Architecture Patterns

### Pattern A: Classification Router

```
Request → [Classifier (fast/cheap)] → Route to appropriate model/agent
                                      ├── Simple → Small model
                                      ├── Medium → Standard model
                                      └── Complex → Frontier model
```

### Pattern B: Escalation Ladder

```
Request → [Small model] → [Validate output]
                          ├── PASS → Return result
                          └── FAIL → [Larger model] → [Validate]
                                                      ├── PASS → Return
                                                      └── FAIL → [Frontier model]
```

### Pattern C: Specialist Routing

```
Request → [Router] → Route to specialist agent
                     ├── Code task → Coding agent (with code tools)
                     ├── Research → Research agent (with search tools)
                     ├── Data analysis → Analysis agent (with data tools)
                     └── Conversation → Chat agent (minimal tools)
```

### Pattern D: Fan-Out with Budget

```
Request → [Fan out to N workers in parallel]
          Each worker has a token budget
          [Aggregator] selects best result
```

## Scaling Considerations

| Challenge | Pattern | Mechanism |
|-----------|---------|-----------|
| High request volume | [N-Parallel-Execution](../../families/N-efficiency-routing/patterns/parallel-execution.md) | Process requests concurrently |
| Variable load | [N-Budgeted-Agent-Loop](../../families/N-efficiency-routing/patterns/budgeted-agent-loop.md) | Cap spend per request, queue excess |
| Mixed difficulty | [N-Complexity-Based-Model-Routing](../../families/N-efficiency-routing/patterns/complexity-based-model-routing.md) | Right-size model per request |
| Peak demand | [N-Caching](../../families/N-efficiency-routing/patterns/caching.md) | Serve repeated queries from cache |
| Degraded service | [I-Fallback-Model-Workflow](../../families/I-reliability-recovery/patterns/fallback-model-workflow.md) | Fall back to available models when primary is down |
| Cost explosion | [N-Cost-Aware-Stopping](../../families/N-efficiency-routing/patterns/cost-aware-stopping.md) | Hard budget caps prevent runaway spend |

## Decision Guide

```
How should I route this request?
│
├── Can routing be decided by rules/code?
│   ├── YES → Use deterministic routing (fastest, cheapest)
│   └── NO → Need semantic understanding
│       ├── Can a small model classify it?
│       │   ├── YES → Use classifier router (Pattern A)
│       │   └── NO → Use confidence-based routing
│       └── Is complexity unpredictable?
│           └── YES → Use escalation ladder (Pattern B)
│
├── How many model tiers do I need?
│   ├── 2 tiers (small + large) → Simple escalation
│   ├── 3+ tiers → Classification with fallback
│   └── Specialist agents → Domain-based routing (Pattern C)
│
└── What about failures/overload?
    ├── Primary model unavailable → Fallback model workflow
    ├── Budget exceeded → Cost-aware stopping + queue
    └── Quality degraded → Escalate tier, alert operators
```

## Relevant Patterns

| Pattern | Role in Routing & Scaling |
|---------|---------------------------|
| [N-Complexity-Based-Model-Routing](../../families/N-efficiency-routing/patterns/complexity-based-model-routing.md) | Route based on estimated task difficulty |
| [N-Small-Model-First-Escalation](../../families/N-efficiency-routing/patterns/small-model-first-escalation.md) | Try cheap model first, escalate on failure |
| [N-Confidence-Based-Routing](../../families/N-efficiency-routing/patterns/confidence-based-routing.md) | Route based on model confidence in its classification |
| [A-Routing](../../families/A-workflow-topology/patterns/routing.md) | General routing topology for workflow branching |
| [N-Budgeted-Agent-Loop](../../families/N-efficiency-routing/patterns/budgeted-agent-loop.md) | Hard budget limits per request/session |
| [N-Parallel-Execution](../../families/N-efficiency-routing/patterns/parallel-execution.md) | Scale throughput with parallel processing |
| [N-Caching](../../families/N-efficiency-routing/patterns/caching.md) | Reduce load by serving cached results |
| [I-Fallback-Model-Workflow](../../families/I-reliability-recovery/patterns/fallback-model-workflow.md) | Graceful degradation when models are unavailable |
| [I-Circuit-Breaker](../../families/I-reliability-recovery/patterns/circuit-breaker.md) | Stop routing to failing endpoints |
| [H01-Deterministic-Override](../../families/H-deterministic-control/patterns/H01-deterministic-override.md) | Code-based routing decisions |
| [C-Coordinator-Specialists](../../families/C-orchestration/patterns/coordinator-specialists.md) | Coordinator routes to domain specialists |

## Anti-Patterns to Watch For

| Anti-Pattern | Problem |
|--------------|---------|
| [Premature Optimization](../../families/N-efficiency-routing/anti-patterns/premature-optimization.md) | Building complex routing before knowing what's needed |
| [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) | Routing to cheaper models without measuring quality impact |
| Single model for everything | Overpaying for simple tasks, or under-serving complex ones |
| Over-engineered routing | Router that costs more than the savings it produces |
| No fallback path | System fails entirely when preferred model is unavailable |

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/index/harness-engineering/
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
