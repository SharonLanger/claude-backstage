# Family A — Workflow Topology

Structural shapes for composing multiple LLM calls: sequences, branches, parallel execution, loops, and iterative refinement.

**Recurring problem:** A single model call is too coarse, or a task requires structured progression through distinct stages.

---

## Directory Tree

```
A-workflow-topology/
├── README.md                      ← this file — navigation, schema, decision guide
└── patterns/
    ├── prompt-chaining.md             ← serial pipeline; output of step N feeds step N+1
    ├── sequential-workflow.md         ← named stages with distinct roles; stricter than chaining
    ├── routing.md                     ← classifier → dispatches to one of N specialist branches
    ├── parallel-sectioning.md         ← split work into independent chunks; merge results
    ├── parallel-voting.md             ← N independent answers → majority / consensus pick
    ├── iterative-refinement.md        ← repeated improvement passes on a single artifact
    ├── generator-critic.md            ← separate generate and evaluate roles in a loop
    ├── evaluator-optimizer.md         ← optimizer drives edits; evaluator gates acceptance
    ├── react.md                       ← interleaved reasoning + action + observation cycles
    └── bounded-loop.md                ← loop with an explicit exit condition and iteration cap
```

---

## Per-Pattern File Schema

Each engineering pattern follows this structure (in order):

| Section | Content |
|---|---|
| **Problem** | The recurring situation that makes this pattern relevant. One paragraph. |
| **Solution Structure** | How the calls are wired together. Include a Mermaid diagram. |
| **When to Use** | Concrete triggering conditions (bullet list). |
| **When Not to Use** | Anti-cases where this pattern adds cost without benefit (bullet list). |
| **Trade-offs** | A two-column table: Benefit vs. Cost/Risk. |
| **Implementation Sketch** | Pseudocode or minimal real code showing the wiring, not business logic. |
| **Related Patterns** | Patterns that pair well, extend, or constrain this one (with links). |
| **Anti-Patterns Addressed** | Named failure modes this pattern prevents. |

---

## Quick-Reference Table

| Pattern | Problem it solves | Key trade-off |
|---|---|---|
| Prompt Chaining | Task too complex for one prompt; has natural sub-steps | Latency adds up; error propagates downstream |
| Sequential Workflow | Multiple roles (write, review, format) must not overlap | Rigid ordering; no parallelism |
| Routing | Different inputs need different specialist prompts | Classifier errors misroute; adds one extra call |
| Parallel Sectioning | Large input can be divided; sub-tasks are independent | Merge step needed; inter-section coherence may suffer |
| Parallel Voting | Single answer unreliable; want consensus or diversity check | N× cost; tie-breaking logic required |
| Iterative Refinement | First draft is good enough to improve but not to ship | Convergence not guaranteed; may spin on minor changes |
| Generator-Critic | Generator is creative but uncritical; need external check | Critic prompt engineering is non-trivial; adds latency |
| Evaluator-Optimizer | Need measurable acceptance criterion before moving on | Evaluator must be precise; vague criteria cause loops |
| ReAct | Task requires interleaved reasoning and external actions | Observation quality determines success; harder to trace |
| Bounded Loop | Loop logic is needed but infinite loops must be prevented | Cap choice is heuristic; premature exit loses quality |

---

## Which Topology Should I Pick?

Work through these questions top to bottom. Stop at the first match.

```
1. Is the task a single, self-contained question with no external state?
   → Use a single LLM call (no family A pattern needed).

2. Does the task split into ordered stages where stage N feeds stage N+1?
   → Are stages role-differentiated (writer → reviewer → formatter)?
      YES → Sequential Workflow
      NO  → Prompt Chaining

3. Does the input determine which of several very different paths to follow?
   → Routing

4. Can the task be divided into truly independent sub-tasks?
   → Do you want N answers and then pick the best?
      YES → Parallel Voting
      NO  → Parallel Sectioning

5. Is the goal to improve an artifact over multiple passes?
   → Do you need a separate evaluator that gates progress?
      YES, with measurable criterion → Evaluator-Optimizer
      YES, with qualitative critique → Generator-Critic
      NO, same model refines itself  → Iterative Refinement

6. Does the task require calling external tools or APIs mid-reasoning?
   → ReAct

7. Any of the above, but you need an explicit exit condition and safety cap?
   → Wrap with Bounded Loop
```

---

## Cross-Family Overlaps

| This pattern | Overlaps with |
|---|---|
| Routing | Family B (task decomposition determines dispatch targets) |
| Parallel Sectioning | Family B (decomposition), Family N (efficiency: parallel execution) |
| Parallel Voting | Family N (efficiency: parallel execution) |
| Sequential Workflow | Family C (orchestration layer drives stage transitions) |
| ReAct | Family C (orchestrator manages tool calls and observations) |
| Bounded Loop | Family I (reliability: prevents infinite loops) |
| Evaluator-Optimizer | Family B (optimizer may decompose tasks), Family C (orchestrator drives the loop) |
| Generator-Critic | Family C (orchestrator coordinates roles) |
| Iterative Refinement | Family I (reliability: refinement loops need a termination condition) |

---

Last updated: 2026-08-24
