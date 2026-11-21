# Family E — Context Engineering

**Recurring problem:** too little, too much, stale, conflicting, or irrelevant context reduces model performance. Context is not free — every token shapes what the model attends to.

**Principle 5** (from `principles/`): *Context Is a Designed Resource.* Information that reaches the model at each step is a deliberate engineering choice, not an accident of conversation history.

---

## Directory Structure

```
E-context-engineering/
├── README.md                            ← this file — navigation hub
│
├── patterns/
│   ├── map-not-manual.md                ← replace giant instructions with a navigable index
│   ├── progressive-disclosure.md        ← reveal information only when the step needs it
│   ├── context-isolation.md             ← prevent context leakage between tasks or agents
│   ├── minimal-context-handoff.md       ← pass only what the next agent needs to continue
│   ├── just-in-time-retrieval.md        ← fetch relevant content at the moment it is needed
│   ├── context-compaction.md            ← summarize or compress history to recover window space
│   ├── context-offloading.md            ← move stable reference material out of the prompt
│   ├── role-scoped-context.md           ← give each role only the context relevant to its job
│   ├── artifact-based-handoff.md        ← hand off a structured artifact instead of raw history
│   └── repository-as-system-of-record.md ← the repo is the source of truth; prompt is transient
│
├── guides/
│   ├── context-failure-modes.md         ← quick-reference: 7 failure modes + diagnostic signals
│   ├── context-vs-memory-vs-state.md    ← when to use context, memory (L), or state (L/F)
│   └── context-design-worksheet.md      ← step-by-step worksheet for designing a context strategy
│
└── anti-patterns/
    ├── giant-instruction-manual.md      ← all rules in one huge prompt; cross-ref to catalog
    └── shared-context-everywhere.md     ← all agents get full history; cross-ref to catalog
```

---

## Per-Pattern File Schema

Every file under `patterns/` follows this schema exactly. Use it when writing new pattern files.

```markdown
# <Pattern Name>

**Family:** E — Context Engineering
**Also appears in:** <other families if cross-listed, else omit>

## Problem
One paragraph. What goes wrong without this pattern.
Be concrete: name the failure mode (e.g., "model ignores the relevant instruction because 
it is buried in 8000 tokens of unrelated rules").

## Solution
One paragraph. The core idea in plain terms.

## Structure
How the pattern is implemented. Use a diagram if the structure is non-trivial.
For simple patterns, a numbered list of steps is enough.

## When to Use
Bullet list. 2–5 conditions that indicate this pattern applies.

## When NOT to Use
Bullet list. 1–3 conditions where the overhead isn't justified.

## Tradeoffs
| Benefit | Cost |
|---------|------|
| ...     | ...  |

## Related Patterns
- **<Pattern>** (Family X) — one sentence on the relationship
- ...

## Anti-Patterns Addressed
- **<Anti-Pattern>** — one sentence

## Example
Short concrete scenario. Code or pseudocode optional; prefer prose.

## Sources / Evidence
- Source name + one-line summary of what it says about this pattern
```

---

## Context Failure Modes — Quick Reference

Use this table to diagnose a context problem before choosing a pattern.

| Failure Mode | Symptom | Root Cause | Primary Counter-Pattern |
|---|---|---|---|
| **Context Starvation** | Model makes decisions without the information it needs | Relevant content was never put in the prompt | Just-in-Time Retrieval, Progressive Disclosure |
| **Context Overload** | Model ignores relevant instructions; attention dilutes | Too many tokens compete for attention | Map-Not-Manual, Context Compaction, Context Offloading |
| **Stale Context** | Model acts on outdated facts or decisions | Prompt not refreshed after state changed | Repository-as-System-of-Record, Artifact-Based Handoff |
| **Context Leakage** | Task B is influenced by context from Task A | Shared context window or shared memory not isolated | Context Isolation, Role-Scoped Context |
| **Context Conflict** | Model hedges or ignores instructions due to contradictions | Multiple sources provide conflicting facts or rules | Artifact-Based Handoff, Minimal-Context Handoff, Role-Scoped Context |
| **Context Sprawl** | Window fills with history before the task completes | Unbounded accumulation across turns | Context Compaction, Context Offloading, Minimal-Context Handoff |
| **Irrelevant Context** | Model hallucinates or drifts; output doesn't match role | Unrelated material is present and distracts | Role-Scoped Context, Context Isolation, Progressive Disclosure |

**Diagnostic flow:** symptom → failure mode → counter-pattern. If multiple failure modes apply, start with the one that is structurally cheapest to fix (isolation before retrieval before compaction).

---

## Context vs Memory vs State — Distinction Guide

These three mechanisms often address the same underlying problem (the model needs information). Choosing the wrong one creates the failure mode you were trying to prevent.

| Dimension | Context (Family E) | Memory (Family L) | State (Family L / F) |
|---|---|---|---|
| **Where it lives** | Inside the current prompt/window | External store (file, DB, vector store) | External store, structured format |
| **Lifetime** | One model call or turn | Across calls and sessions | Across tasks and agents |
| **Who controls access** | The code that builds the prompt | Retrieval or lookup logic | State machine / harness |
| **Token cost** | Always paid per call | Paid only when retrieved | Not in prompt unless explicitly loaded |
| **Best for** | What the model needs right now | Facts that accumulate over time | Phase transitions, checkpoints, locks |
| **Failure if misused** | Overload, leakage, stale content | Stale retrieval, unbounded growth | Lost progress, race conditions |
| **Counter-patterns** | This family (E) | Scoped Memory, Summarized Memory, External Durable State | Checkpoint State, State Machine |

**Rule of thumb:**
- If the information is needed *for this call and will not be needed again* → put it in context.
- If the information accumulates *across calls or sessions* → use memory (Family L).
- If the information represents *a checkpoint or transition* that other agents or future sessions must see → use structured state (Family L / F).
- If information is *too large for the prompt* and only parts are needed → retrieve just-in-time into context (Just-in-Time Retrieval) or offload entirely (Context Offloading).

---

## Related Families

| Family | Relationship to E |
|---|---|
| **B — Task Decomposition** | Each subtask should receive minimal relevant context. Decomposition decisions determine what context each step needs. |
| **F — Harness / Environment** | The harness controls what files and tools are available; this shapes what can be retrieved into context. Context Engineering decides what to load; F decides what exists to load. |
| **L — Memory & State** | External memory is the primary alternative to growing context. When context can't hold it, L stores it. These two families are complements, not substitutes. |
| **N — Efficiency & Routing** | Context minimization (N) and context engineering (E) overlap: both reduce token cost. N focuses on routing decisions; E focuses on content design. |

---

## Anti-Patterns This Family Addresses

Both anti-patterns below are cataloged in `anti-patterns/` at the top-level catalog. The files here are cross-references with E-specific counter-pattern mappings.

| Anti-Pattern | Core Error | Primary Counter-Patterns in E |
|---|---|---|
| **Giant Instruction Manual** | All rules, background, and procedures in one massive system prompt | Map-Not-Manual, Progressive Disclosure, Context Offloading |
| **Shared Context Everywhere** | Every agent receives full conversation history and all reference material | Context Isolation, Role-Scoped Context, Minimal-Context Handoff |

---

## Where to Start

| You are trying to… | Read first |
|---|---|
| Diagnose why the model is ignoring instructions | Context failure modes (above) → Map-Not-Manual or Context Compaction |
| Design context for a new multi-step workflow | `guides/context-design-worksheet.md` |
| Understand when to use memory instead of context | `guides/context-vs-memory-vs-state.md` |
| Pass results between agents cleanly | `patterns/artifact-based-handoff.md`, `patterns/minimal-context-handoff.md` |
| Prevent one task's context polluting another | `patterns/context-isolation.md`, `patterns/role-scoped-context.md` |
| Handle a long-running task that fills the window | `patterns/context-compaction.md`, `patterns/context-offloading.md` |
| Make retrieval precise rather than noisy | `patterns/just-in-time-retrieval.md` |
| Treat the repo as the source of truth | `patterns/repository-as-system-of-record.md` |

---

Last updated: 2026-08-24
