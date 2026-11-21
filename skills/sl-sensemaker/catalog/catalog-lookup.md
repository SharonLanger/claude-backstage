# Catalog Lookup — Finding Patterns, Anti-Patterns, Principles & More

How to find what you need in this catalog. Read this file when you're searching for information.

---

## What's In This Catalog

| Content type | Location | Count | What it is |
|---|---|---|---|
| **Pattern families** | `families/A-*` through `families/O-*/` | 15 families | Reusable solutions to recurring problems |
| **Anti-patterns** | `anti-patterns/` | 10 (AP01–AP10) | Named failure modes with counter-patterns |
| **Principles** | `principles/` | 8 (P1–P8) | Cross-cutting rules that explain WHY patterns work |
| **Use-case indexes** | `use-cases/` | 8 scenario categories | Problem-first navigation across families |
| **Discovery research** | `input/` | 1 file | Raw source material the catalog was built from |

---

## How to Search

Choose your entry point based on what you have:

### "I have a problem to solve"

1. Check the **Quick Lookup by Problem** table below — it maps common problems to families and anti-patterns
2. If no match, go to `use-cases/README.md` — its scenario table maps problems to families
3. Still no match — check `use-cases/decision-trees/which-family.md` for a guided decision tree

### "I'm diagnosing a failure"

1. Go to `anti-patterns/README.md` — check the **Detection at a Glance** table to match symptoms
2. Open the matching anti-pattern file and read its Counter-Patterns section
3. Follow the counter-pattern links to the pattern files that fix it

### "I want to understand WHY a pattern works"

1. Go to `principles/README.md` — 8 principles with one-line summaries
2. For cross-referencing: `principles/index.md` maps principles × families × anti-patterns in one table
3. Each principle file links to the families and anti-patterns it governs

### "I'm designing a new system"

1. Start with `use-cases/onboarding/new-to-agents.md` — curated reading path
2. Then `use-cases/designing/new-system.md` — first design decisions
3. Check `use-cases/decision-trees/architecture-choices.md` for key architecture forks

### "I'm doing a security review"

1. Go to `use-cases/security/security-review.md` — full checklist
2. Also check `anti-patterns/AP06-model-as-security-boundary.md` and `AP10-overpowered-coding-agent.md`
3. Family J (`families/J-security-trust/`) has all security patterns

### "I'm setting up evals"

1. Go to `use-cases/evaluation/` — three files covering agent eval, regression testing, and building evals from errors
2. Family D (`families/D-verification-evaluation/`) has all verification patterns
3. Check `anti-patterns/AP08-generic-evals-before-error-analysis.md` — the most common eval mistake

---

## Quick Lookup by Problem

| You're dealing with… | Start here |
|---|---|
| Agent changes or deletes the regression test | [AP10 — scope write access](anti-patterns/AP10-overpowered-coding-agent.md), [D02 — verify against protected tests](families/D-verification-evaluation/patterns/D02-test-before-done.md) |
| Long session loses decisions or requirements | [Context Compaction](families/E-context-engineering/patterns/context-compaction.md), [Repository-as-System-of-Record](families/E-context-engineering/patterns/repository-as-system-of-record.md) |
| Agent keeps proposing a rejected approach | [Fresh-Context Retry for accumulated failed attempts](families/I-reliability-recovery/patterns/fresh-context-retry.md), [Root-Cause-Before-Retry when the failure is unclear](families/I-reliability-recovery/patterns/root-cause-before-retry.md) |
| Diff is too large to review | [B5 — verifiable milestones](families/B-task-decomposition/patterns/B5-milestone-checkpoint.md), [K01 — human checkpoints](families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md), [K05 — preview before writing](families/K-human-control/patterns/K05-draft-preview-before-apply.md) |
| Project instruction file has grown too large | [Map-Not-Manual](families/E-context-engineering/patterns/map-not-manual.md), [AP03 — Giant Instruction Manual](anti-patterns/AP03-giant-instruction-manual.md) |
| Routine task needs the same instructions every time | [F07 — Agent Skills / Procedures](families/F-harness-environment/patterns/F07-agent-skills-procedures.md) |
| Agent loops or repeats mistakes | [I — Reliability](families/I-reliability-recovery/), [H — Deterministic Control](families/H-deterministic-control/), [AP04](anti-patterns/AP04-retry-without-new-information.md), [AP09](anti-patterns/AP09-infinite-weakly-bounded-loop.md) |
| Need to verify the agent actually finished | [D — Verification](families/D-verification-evaluation/), [AP01](anti-patterns/AP01-self-certified-completion.md) |
| Agent has wrong or noisy context | [E — Context Engineering](families/E-context-engineering/), [AP03](anti-patterns/AP03-giant-instruction-manual.md), [AP07](anti-patterns/AP07-shared-context-everywhere.md) |
| Agent took a dangerous/irreversible action | [J — Security](families/J-security-trust/), [K — Human Control](families/K-human-control/), [G — Tool Design](families/G-tool-action-design/) |
| Multi-agent system is expensive or unreliable | [C — Orchestration](families/C-orchestration/), [N — Efficiency](families/N-efficiency-routing/), [AP05](anti-patterns/AP05-multi-agent-by-default.md) |
| Can't debug what the agent did | [M — Observability](families/M-observability-debugging/), [D — Verification](families/D-verification-evaluation/) |
| Model output needs to feed downstream code | [O — Output Boundaries](families/O-output-integration/), [H — Deterministic Control](families/H-deterministic-control/) |
| Agent works in tests but fails on real repo | [F — Harness Engineering](families/F-harness-environment/), [E — Context Engineering](families/E-context-engineering/) |
| Security / prompt injection risk | [J — Security](families/J-security-trust/), [AP10](anti-patterns/AP10-overpowered-coding-agent.md), [AP06](anti-patterns/AP06-model-as-security-boundary.md) |
| Long-running task loses state | [L — Memory & State](families/L-memory-state/), [F — Harness](families/F-harness-environment/) |
| Task is too large for one prompt | [B — Task Decomposition](families/B-task-decomposition/), [A — Workflow Topology](families/A-workflow-topology/) |
| Need to structure a sequence of model calls | [A — Workflow Topology](families/A-workflow-topology/) |
| Designing or debugging tool interfaces | [G — Tool Design](families/G-tool-action-design/) |
| Reducing cost or latency | [N — Efficiency](families/N-efficiency-routing/), [E — Context](families/E-context-engineering/), also `use-cases/cost-and-performance/` |
| When to pause for human input | [K — Human Control](families/K-human-control/), also `use-cases/human-in-the-loop/` |
| New to AI agents | [Principles](principles/), then `use-cases/onboarding/` |

---

## Navigation by Layer

Every pattern belongs to one of four layers.

| Layer | What it covers | Families |
|---|---|---|
| **1 — Model Interaction** | What happens inside or immediately around one model call | [A](families/A-workflow-topology/), [G](families/G-tool-action-design/), [O](families/O-output-integration/) |
| **2 — Workflow / Composition** | How multiple calls, roles, or agents are combined | [A](families/A-workflow-topology/), [B](families/B-task-decomposition/), [C](families/C-orchestration/), [K](families/K-human-control/) |
| **3 — Harness / Runtime** | The environment that makes agent behavior reliable | [E](families/E-context-engineering/), [F](families/F-harness-environment/), [H](families/H-deterministic-control/), [I](families/I-reliability-recovery/), [J](families/J-security-trust/), [L](families/L-memory-state/), [M](families/M-observability-debugging/), [N](families/N-efficiency-routing/) |
| **4 — Development / Governance** | How developers validate and improve the system | [D](families/D-verification-evaluation/), [K](families/K-human-control/), [M](families/M-observability-debugging/) |

---

## Inside a Family Directory

Each family directory follows this structure (not all subdirectories present in every family):

| Subdirectory | What it contains | Families that have it |
|---|---|---|
| `patterns/` | Individual engineering and practical patterns | All families |
| `guides/` | How-to guides and decision aids for the family's topic | C, D, E, M |
| `comparisons/` | Side-by-side comparisons of similar patterns | C |
| `reference/` | Checklists, quick-reference tables | G |
| `anti-patterns/` | Family-specific anti-pattern details (supplements root `anti-patterns/`) | C, E, I, J, M, N |

Each family has a `README.md` with:
- Pattern list with one-line descriptions
- "Start here when" routing guide
- Family relationships table (which other families overlap)

---

## Cross-Family Search

Some problems span multiple families. When one family's patterns don't fully solve your problem:

1. Check the **Related Patterns** section at the bottom of the pattern you found — it links to patterns in other families
2. Check the family README's **Family Relationships** table — it shows which families overlap
3. Check `use-cases/` for composite scenarios that combine patterns across families
4. Check `principles/index.md` — it maps principles to families, so you can find all families that share a principle

---

## Anti-Pattern → Counter-Pattern Quick Reference

| Anti-Pattern | Primary Counter-Families | Key Patterns |
|---|---|---|
| AP01 Self-Certified Completion | D, H, K | Independent Verifier, Test-Before-Done, Human Approval Gate |
| AP02 Prompt-as-Policy | H, J, G | Deterministic Override, Programmatic Gate, Schema Validator |
| AP03 Giant Instruction Manual | E, F, B | Map-Not-Manual, Progressive Disclosure, Repository-Local System of Record |
| AP04 Retry Without New Information | I, M, H | Retry-With-Feedback, Root-Cause-Before-Retry, Structured Error Classification |
| AP05 Multi-Agent by Default | A, N, B | Prompt Chaining, Complexity-Based Routing, Fixed Decomposition |
| AP06 Model as Security Boundary | J, H, G | Deterministic Authorization, Tool Gateway, Authorization Outside the Model |
| AP07 Shared Context Everywhere | E, L, C | Context Isolation, Session Isolation, Role-Scoped Context |
| AP08 Generic Evals Before Error Analysis | D, M, F | End-to-End Task-Success Eval, Failure Categorization, Capability-Gap Feedback |
| AP09 Infinite / Weakly Bounded Loop | H, A, I | Bounded Loop, Stop Condition, Circuit Breaker |
| AP10 Overpowered Coding Agent | J, G, K | Least Privilege, Capability Minimization, Read/Write Separation |

---

## Principle → Family Quick Reference

| Principle | Governs families | Violated by anti-patterns |
|---|---|---|
| P1 Prefer Determinism | H, G, O | AP02, AP06, AP09 |
| P2 Complexity Earns Its Keep | C, B, N | AP05 |
| P3 Give Agents Ground Truth | E, F, L | AP03, AP07 |
| P4 Separate Generation From Verification | D, C, A | AP01 |
| P5 Context Is a Designed Resource | E, L, F | AP03, AP07 |
| P6 Security Boundaries Outside the Model | J, H, G | AP02, AP06, AP10 |
| P7 Measure Real Task Success | D, M, F | AP08, AP01 |
| P8 Failures Improve the Harness | F, I, M | AP04, AP08 |

---

Last updated: 2026-11-19
