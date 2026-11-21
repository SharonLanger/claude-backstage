# Family N — Efficiency & Model Routing

**Recurring problem:** Once a system is correct, reliability improvements can make inference unnecessarily slow or expensive. This family covers how to reduce cost and latency without sacrificing correctness — through smarter routing, cheaper models, avoided work, and bounded execution.

> **Correctness before efficiency.**
> Never apply patterns from this family to a system that is not yet correct. Routing to a cheaper model, truncating context, or stopping early on an incorrect system produces cheap wrong answers faster. Establish correctness first (families D, I), then optimize.

---

## Directory Tree

```
N-efficiency-routing/
├── README.md                              ← this file (navigation, optimization sequence, routing guide)
│
├── patterns/
│   ├── complexity-based-model-routing.md  ← route easy inputs to small models, hard inputs to large
│   ├── confidence-based-routing.md        ← escalate only when the model's own confidence is low
│   ├── small-model-first-escalation.md    ← always start cheap; escalate on failure or low confidence
│   ├── parallel-execution.md             ← run independent subtasks concurrently to cut wall-clock time
│   ├── context-minimization.md           ← trim context to the minimum needed for the current step
│   ├── caching.md                        ← reuse previous outputs for identical or near-identical inputs
│   ├── tool-result-reuse.md              ← avoid re-invoking tools whose output is already known
│   ├── budgeted-agent-loop.md            ← cap total tokens/cost/steps before the loop starts
│   └── cost-aware-stopping.md           ← stop early when marginal improvement no longer justifies cost
│
└── anti-patterns/
    ├── premature-optimization.md         ← optimizing before correctness is established
    └── silent-quality-degradation.md     ← cost cuts that quietly lower output quality with no monitoring
```

---

## Per-Pattern File Schema

Each engineering entry in `patterns/` and `anti-patterns/` follows this structure:

```markdown
# <Pattern Name>

**Family:** N — Efficiency & Model Routing
**Type:** Pattern | Anti-Pattern

## Problem
One paragraph: what goes wrong (in cost, latency, or quality) without this pattern.

## Solution
One paragraph: the core mechanic of the pattern.

## Structure
Minimal pseudocode or component diagram showing the key steps.

## When to Use
Bullet list of conditions that call for this pattern.

## When Not to Use
Bullet list of conditions where this pattern is wrong or overkill.

## Trade-offs
| Pro | Con |
|-----|-----|
| ... | ... |

## Example
Concrete scenario showing the pattern applied.

## Related Patterns
Links to related patterns in this family and other families.

## Related Anti-Patterns
What you fall into if you misapply this pattern.
```

---

## Cost Optimization Sequence

Apply interventions in this order. Each step is cheaper to implement and lower-risk than those that follow. Stop as soon as the cost/latency target is met — do not keep optimizing.

| Step | Intervention | Pattern | Why first |
|---|---|---|---|
| 1 | Reuse work you already did | Caching; Tool/Result Reuse | Zero inference cost for a cache hit |
| 2 | Cut unnecessary input tokens | Context Minimization | Reduces cost and latency on every call |
| 3 | Run independent work in parallel | Parallel Execution | Cuts wall-clock time with no quality loss |
| 4 | Start with a small model; escalate only on failure | Small-Model-First Escalation | Most inputs are simple; pay large-model price only when needed |
| 5 | Route by predicted complexity before calling any model | Complexity-Based Model Routing | Avoids the small-model call cost when input is clearly complex |
| 6 | Route by model's own confidence score | Confidence-Based Routing | Fine-grained escalation when complexity is hard to predict upfront |
| 7 | Cap total budget before the loop starts | Budgeted Agent Loop | Hard ceiling on runaway cost |
| 8 | Stop early when returns diminish | Cost-Aware Stopping | Avoids paying for marginal iterations at the end of a run |

---

## Routing Decision Guide

Use this guide when deciding which routing pattern to apply to a given call or loop.

```
1. Do you have a cached result for this input (exact or semantic match)?
   YES → return it (Caching)
   NO  → continue

2. Does this step use tool outputs from an earlier step in the same run?
   YES → reuse stored results (Tool/Result Reuse)
   NO  → continue

3. Can the input be trimmed without losing necessary information?
   YES → trim first (Context Minimization), then continue routing
   NO  → continue

4. Does this step have multiple independent subtasks?
   YES → run them concurrently (Parallel Execution)
   NO  → continue

5. Can input complexity be reliably predicted BEFORE calling a model
   (e.g., via input length, query classifier, rule)?
   YES → route at intake (Complexity-Based Model Routing)
   NO  → continue

6. Is the failure mode "occasionally wrong" rather than "systematically wrong"?
   YES → start with small model and escalate on failure (Small-Model-First Escalation)
   NO  → continue

7. Does the model produce a reliable confidence or probability score?
   YES → escalate on low confidence (Confidence-Based Routing)
   NO  → use the larger model directly

8. Is this call inside an agent loop?
   YES → set a token/step/cost budget before entering (Budgeted Agent Loop)
        AND define a stopping criterion for diminishing returns (Cost-Aware Stopping)
   NO  → done
```

---

## Anti-Patterns Addressed

| Anti-Pattern | What it looks like | Primary cure |
|---|---|---|
| Premature Optimization | Routing or truncating before the system produces correct output | Establish correctness (families D, I) first; apply N patterns after |
| Silent Quality Degradation | Cost cuts ship without quality monitoring; accuracy quietly drops | Add quality metrics before optimizing; use Confidence-Based Routing to detect degradation |

---

## Related Families

| Family | Connection |
|---|---|
| A — Workflow Topology | Parallel Execution is also a topology pattern; N treats it as a latency optimization |
| C — Orchestration | Complexity-Based and Confidence-Based Routing overlap with routing between specialized agents |
| D — Verification & Evaluation | Correctness must be verified before applying efficiency patterns |
| E — Context Engineering | Context Minimization is also a context pattern; N treats it as a cost intervention |
| I — Reliability & Recovery | Budgeted Agent Loop bounds the same loop that Bounded Retry caps for correctness |

---

Last updated: 2026-08-24
