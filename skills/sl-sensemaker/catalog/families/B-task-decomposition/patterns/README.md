# Family B — Task Decomposition: Patterns

Navigation hub for the 6 pattern files in this family.

---

## Practitioner entry points

- [Slice a change for review](B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review) — the AI change is too large to review.

## Directory Tree

```
patterns/
├── README.md                          ← this file
├── B1-plan-execute.md                 ← Plan-Execute pattern
├── B2-hierarchical-decomposition.md   ← Hierarchical Decomposition pattern
├── B3-dynamic-decomposition.md        ← Dynamic Decomposition pattern
├── B4-fixed-decomposition.md          ← Fixed Decomposition pattern
├── B5-milestone-checkpoint.md         ← Milestone-Checkpoint pattern
└── B6-reconnaissance-first.md         ← Reconnaissance-First pattern
```

---

## What Each File Contains

| File | Pattern | One-line Description |
|------|---------|----------------------|
| `B1-plan-execute.md` | Plan-Execute | Generate a structured plan before any execution begins; then execute the plan step by step |
| `B2-hierarchical-decomposition.md` | Hierarchical Decomposition | Recursively break a complex goal into a tree of sub-goals until each leaf is actionable |
| `B3-dynamic-decomposition.md` | Dynamic Decomposition | Determine the next sub-task at runtime based on results so far, rather than up front |
| `B4-fixed-decomposition.md` | Fixed Decomposition | Split a task into a predetermined, static set of parallel or sequential sub-tasks |
| `B5-milestone-checkpoint.md` | Milestone-Checkpoint | Decompose work into milestones with explicit checkpoints for validation before proceeding |
| `B6-reconnaissance-first.md` | Reconnaissance-First | Explore and gather information before committing to a decomposition strategy |

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

- **Choosing a decomposition strategy?** Start with B1 (Plan-Execute) as the baseline; then compare B3 (Dynamic) vs B4 (Fixed) based on how well-defined the problem is.
- **Dealing with uncertainty or unknown scope?** B6 (Reconnaissance-First) is the entry point.
- **Need checkpoints for long-running work?** B5 (Milestone-Checkpoint) addresses that directly.
- **Understanding hierarchy depth?** B2 (Hierarchical Decomposition) handles recursive nesting.
- **Cross-family connections?** Decomposition patterns in Family B frequently compose with workflow topologies from Family A — check "Related Patterns" in each file.
- **Going up?** The family overview is at `../` — it covers all families and explains how B-Task-Decomposition fits the broader catalog.

---

Last updated: 2026-08-24
