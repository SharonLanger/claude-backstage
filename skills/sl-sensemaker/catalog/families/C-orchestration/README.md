# Family C — Orchestration & Role Separation

Recurring problem: one agent has too many responsibilities, or a task requires dynamic specialization that a single agent cannot provide cleanly.

This family covers how multiple agents divide work, hand off results, and check each other — and when NOT to reach for multi-agent at all.

Related families: A (topology primitives), B (task decomposition feeds the orchestrator), K (human control at handoff points), N (efficiency: is multi-agent actually worth it?).

---

## Directory Tree

```
C-orchestration/
├── README.md                          ← this file
│
├── patterns/
│   ├── manager-workers.md             ← hierarchical delegation; manager owns the goal
│   ├── orchestrator-workers.md        ← stateless coordination; orchestrator routes, not owns
│   ├── coordinator-specialists.md     ← domain experts called by a neutral coordinator
│   ├── agent-as-tool.md              ← agent wrapped as a callable tool in another agent's loop
│   ├── decentralized-handoff.md      ← peer-to-peer passing without a central controller
│   ├── hierarchical-coordinator.md   ← nested coordinators for deep decomposition trees
│   ├── specialist-reviewer.md        ← separate agent whose only job is critique/validation
│   ├── synthesizer-aggregator.md     ← collects parallel outputs and produces a unified result
│   └── maker-checker.md              ← producer + independent verifier; catches errors before commit
│
├── comparisons/
│   ├── manager-vs-orchestrator-vs-coordinator.md  ← when to use each; authority vs routing vs domain
│   └── reviewer-vs-checker-vs-synthesizer.md      ← post-processing roles distinguished
│
├── guides/
│   └── do-you-need-multi-agent.md    ← decision guide; anti-pattern: Multi-Agent by Default
│
└── anti-patterns/
    └── multi-agent-by-default.md     ← full anti-pattern entry
```

---

## Per-Pattern File Schema

Each engineering entry under `patterns/` follows this structure:

```
# <Pattern Name>

## Intent
One sentence: what problem does this pattern solve?

## Motivation
The concrete pain that triggers this pattern. What goes wrong without it?

## Structure
Mermaid diagram showing roles and message/control flow.

## Participants
| Role | Responsibility |
|------|---------------|
| ...  | ...           |

## How It Works
Numbered steps describing the runtime sequence.

## When to Use
Bulleted conditions that indicate this pattern fits.

## When NOT to Use
Conditions where a simpler alternative is better.

## Variants
Named sub-forms or common adaptations.

## Implementation Notes
Concrete guidance: context passing, failure handling, token budget, latency.

## Trade-offs
| Pro | Con |
|-----|-----|

## Related Patterns
Links to other files in this family and other families.

## Example Sketch
Minimal pseudocode or scenario walkthrough (no production code).
```

---

## Quick-Reference Table

| Pattern | Controller | Workers | Key Differentiator |
|---------|-----------|---------|-------------------|
| Manager → Workers | Manager owns goal and state | Parallel or sequential | Manager accountable end-to-end |
| Orchestrator → Workers | Stateless router | Parallel | Orchestrator routes only; no ownership |
| Coordinator → Specialists | Neutral coordinator | Domain experts | Coordinator has no domain knowledge |
| Agent-as-Tool | Any caller | Single wrapped agent | Worker invisible to outer loop as an agent |
| Decentralized Handoff | None (peer-to-peer) | All peers | No single point of control |
| Hierarchical Coordinator | Root + nested coords | Leaf workers | Multi-level decomposition |
| Specialist Reviewer | None (post-hoc) | Reviewer only | Critique without production responsibility |
| Synthesizer / Aggregator | Synthesizer | Parallel producers | Convergence after fan-out |
| Maker-Checker | Maker produces | Checker verifies | Independence is the invariant |

---

## Do You Actually Need Multi-Agent?

Before choosing any pattern in this family, consult `guides/do-you-need-multi-agent.md`.

The anti-pattern **Multi-Agent by Default** is addressed in `anti-patterns/multi-agent-by-default.md`.

Quick filter — if you answer YES to any of these, stop and reconsider:

- Can one agent with a longer context window do this sequentially?
- Is the "parallelism" mostly to feel faster, not because subtasks are genuinely independent?
- Does coordination overhead (context passing, error routing, retries) exceed the work itself?
- Are you adding agents because the prompt is too complex — and simplifying the prompt would fix it?

Multi-agent is justified when subtasks are genuinely parallel and independent, when specialization brings measurable quality gain, or when a single agent's context window is a real constraint — not a perceived one.

---

## Comparison Files

`comparisons/manager-vs-orchestrator-vs-coordinator.md` — The three top-level patterns share surface structure but differ in authority, state ownership, and domain knowledge. Read this before picking between them.

`comparisons/reviewer-vs-checker-vs-synthesizer.md` — Three post-processing roles that look similar but serve different purposes: critique, binary verification, and unification.

---

Last updated: 2026-08-24
