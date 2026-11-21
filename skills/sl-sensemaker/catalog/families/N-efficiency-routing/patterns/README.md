# Family N — Efficiency & Model Routing: Patterns

9 patterns covering cost and latency reduction across agent systems.

**Critical constraint:** Efficiency patterns apply AFTER correctness is established. Never sacrifice correctness for efficiency. See the `anti-patterns/` folder for the two named failure modes — premature-optimization and silent-quality-degradation — that this family must avoid.

---

## Files

```
patterns/
├── README.md                          ← this file
├── budgeted-agent-loop.md             ← set a hard cost/step ceiling before loop entry; return partial result on exhaust
├── caching.md                         ← skip inference for identical or near-identical inputs by reusing prior results
├── complexity-based-model-routing.md  ← classify input difficulty pre-inference and route to the appropriate model tier
├── confidence-based-routing.md        ← route based on the small model's own confidence score after an initial inference pass
├── context-minimization.md            ← strip accumulated context to only what the current step requires
├── cost-aware-stopping.md             ← stop iterative refinement when marginal quality gain no longer justifies step cost
├── parallel-execution.md              ← run independent subtasks concurrently to reduce wall-clock latency
├── small-model-first-escalation.md    ← attempt with small model first; escalate to large model only on failure
└── tool-result-reuse.md               ← cache tool call results within a run so identical calls skip re-execution
```

---

## Schema

Every file in this folder follows the same structure:

| Section | What it contains |
|---|---|
| `# Name` | Canonical pattern name |
| `**Family / Type**` | Family N, Type: Pattern |
| `## Problem` | The inefficiency being addressed, with concrete cost/latency impact |
| `## Solution` | The mechanism for reducing cost or latency while preserving correctness |
| `## Solution Structure` | Diagram (Mermaid, in a `<details>` block) or annotated pseudocode |
| `## Consequences` | What you gain, what you risk, how to detect quality regression |
| `## Known Uses` | Real systems, frameworks, or provider features that apply the pattern |
| `## Related Patterns` | Cross-references within Family N and to other families |

---

## How to Navigate

**Recommended sequence when optimizing a system:**

1. Reuse before computing: `tool-result-reuse.md`, `caching.md`
2. Trim before sending: `context-minimization.md`
3. Parallelize where independent: `parallel-execution.md`
4. Route to cheaper models: `complexity-based-model-routing.md`, `confidence-based-routing.md`, `small-model-first-escalation.md`
5. Cap runaway loops: `budgeted-agent-loop.md`, `cost-aware-stopping.md`

**The two routing patterns differ in when routing happens:** `complexity-based-model-routing` routes before any inference using input features; `confidence-based-routing` and `small-model-first-escalation` route after an initial cheap inference pass.

**Cross-family links:** Cost metrics feeding these decisions come from Family M (M06). Correctness baselines that must hold through optimization come from Family D (evals) and Family I (correctness patterns). Anti-patterns for this family live in `../anti-patterns/`.
