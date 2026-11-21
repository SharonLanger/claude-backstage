# Family A — Workflow Topology: Patterns

Navigation hub for the 10 pattern files in this family.

---

## Directory Tree

```
patterns/
├── README.md                    ← this file
├── bounded-loop.md              ← Bounded Loop pattern
├── evaluator-optimizer.md       ← Evaluator-Optimizer pattern
├── generator-critic.md          ← Generator-Critic pattern
├── iterative-refinement.md      ← Iterative Refinement pattern
├── parallel-sectioning.md       ← Parallel Sectioning pattern
├── parallel-voting.md           ← Parallel Voting pattern
├── prompt-chaining.md           ← Prompt Chaining pattern
├── react.md                     ← ReAct (Reason + Act) pattern
├── routing.md                   ← Routing pattern
└── sequential-workflow.md       ← Sequential Workflow pattern
```

---

## What Each File Contains

| File | Pattern | One-line Description |
|------|---------|----------------------|
| `prompt-chaining.md` | Prompt Chaining | Pass the output of one LLM call as the input to the next in a fixed chain |
| `sequential-workflow.md` | Sequential Workflow | Execute a fixed, ordered series of steps where each step depends on the previous |
| `routing.md` | Routing | Classify an input and dispatch it to the appropriate specialist handler |
| `parallel-sectioning.md` | Parallel Sectioning | Split a task into independent sections and process them concurrently |
| `parallel-voting.md` | Parallel Voting | Run the same prompt multiple times and aggregate results by consensus |
| `iterative-refinement.md` | Iterative Refinement | Repeatedly improve an output through successive passes until a quality bar is met |
| `generator-critic.md` | Generator-Critic | Separate generation and critique into two roles that collaborate over multiple turns |
| `evaluator-optimizer.md` | Evaluator-Optimizer | An evaluator scores output and drives an optimizer loop until the score is acceptable |
| `react.md` | ReAct | Interleave reasoning traces with tool actions in a tight think-act-observe loop |
| `bounded-loop.md` | Bounded Loop | Run an agentic loop with explicit iteration or cost caps to prevent runaway execution |

---

## Schema

Each engineering pattern in this folder follows the same 8-section structure:

1. **Problem** — the specific challenge this pattern addresses
2. **Solution Structure** — how the pattern works, including a Mermaid diagram of the flow
3. **When to Use** — conditions that make this pattern a good fit
4. **When Not to Use** — conditions where this pattern adds cost without benefit
5. **Trade-offs** — latency, cost, complexity, reliability considerations
6. **Implementation Sketch** — minimal pseudocode or structural outline
7. **Related Patterns** — links to other patterns in this catalog
8. **Anti-Patterns Addressed** — failure modes this pattern prevents

All files end with a **Sources** section linking to primary references from Anthropic, OpenAI, Google, AWS, and Microsoft.

---

## How to Navigate

- **Looking for a specific topology?** Go directly to the file by pattern name.
- **Choosing between similar patterns?** Compare the "When to Use" and "Trade-offs" sections side by side.
- **Understanding how patterns compose?** Check "Related Patterns" in any file — it cross-references within and across families.
- **Going up?** The family overview is at `../` — it covers all families and explains how A-Workflow-Topology fits the broader catalog.

---

Last updated: 2026-08-24
