# AI / Agent Design Patterns

A catalog of reusable guidance for people working with LLMs and coding agents, including practical session procedures and engineering patterns.

- **Working through a session problem?** Start with [practitioner entry points](catalog-lookup.md#working-with-an-assistant-in-a-session).
- **Looking up patterns?** Read [`catalog-lookup.md`](catalog-lookup.md)
- **Adding patterns from a new source?** Read [`contributing/catalog-intake.md`](contributing/catalog-intake.md)

---

## Practical coverage

The catalog contains 278 Markdown files, including 137 patterns and 13 guides. Session routes include diagnosis framing, API verification, repair-versus-fresh selection, clarification interviews, review overload, and intentional decision visibility. Start at the [session lookup](catalog-lookup.md#working-with-an-assistant-in-a-session) for canonical entries and limits.

## What's In This Catalog

```
research-ai-design-patterns/
├── README.md                          ← this file
├── catalog-lookup.md                  ← agent/user guide for finding patterns
│
├── contributing/                      ← guides for adding to the catalog
│   ├── README.md                      ← index for contributing guides
│   ├── catalog-intake.md              ← full pipeline: blog → catalog entries
│   ├── authoring-guide.md             ← writing spec, schemas, checklists
│   ├── classification-guide.md        ← how to classify and place patterns
│   └── source-registry.md             ← verified URLs and citation rules
│
├── families/                          ← 15 pattern families (A–O)
│   ├── A-workflow-topology/
│   ├── B-task-decomposition/
│   ├── C-orchestration/
│   ├── D-verification-evaluation/
│   ├── E-context-engineering/
│   ├── F-harness-environment/
│   ├── G-tool-action-design/
│   ├── H-deterministic-control/
│   ├── I-reliability-recovery/
│   ├── J-security-trust/
│   ├── K-human-control/
│   ├── L-memory-state/
│   ├── M-observability-debugging/
│   ├── N-efficiency-routing/
│   └── O-output-integration/
│
├── anti-patterns/                     ← 10 named failure modes (AP01–AP10)
├── principles/                        ← 8 cross-cutting principles (P1–P8)
├── use-cases/                         ← scenario-based cross-cutting indexes
└── input/                             ← raw discovery research
```

---

## Pattern Families (A–O)

| Family | Recurring problem | Patterns |
|---|---|---|
| **A — Workflow Topology** | Single model call too coarse; task needs structured progression | 10 |
| **B — Task Decomposition** | Large/ambiguous tasks overload one reasoning step | 6 |
| **C — Orchestration** | One agent has too many responsibilities | 9 |
| **D — Verification** | Generated work looks plausible but doesn't satisfy the real task | 12 |
| **E — Context Engineering** | Wrong, stale, or noisy context reduces performance | 10 |
| **F — Harness Engineering** | Model capability alone insufficient for reliable work | 11 |
| **G — Tool Design** | Model must translate ambiguous intent into safe actions | 10 |
| **H — Deterministic Control** | Must-hold rules encoded in prompts instead of enforced mechanically | 8 |
| **I — Reliability & Recovery** | Agents fail partially, loop, repeat mistakes, lose progress | 11 |
| **J — Security & Trust** | Model-controlled actions cross security boundaries | 11 |
| **K — Human Control** | Not every decision should be autonomous | 6 |
| **L — Memory & State** | Long-running work can't rely on ever-growing context | 9 |
| **M — Observability** | Can't reconstruct what happened when agent fails | 9 |
| **N — Efficiency & Routing** | Reliability improvements make inference too slow/expensive | 9 |
| **O — Output & Integration** | Natural-language output must safely enter deterministic software | 6 |

---

## Anti-Patterns (AP01–AP10)

| # | Name | Short description |
|---|---|---|
| AP01 | Self-Certified Completion | Agent says "done" with no independent evidence |
| AP02 | Prompt-as-Policy | Security rule exists only in natural language |
| AP03 | Giant Instruction Manual | All rules crammed into one huge system prompt |
| AP04 | Retry Without New Information | Failed attempt retried with no additional feedback |
| AP05 | Multi-Agent by Default | Agent teams used where a single workflow would suffice |
| AP06 | Model as Security Boundary | Model decides its own authorization |
| AP07 | Shared Context Everywhere | All agents receive all history and reference material |
| AP08 | Generic Evals Before Error Analysis | Generic metrics adopted before studying real failures |
| AP09 | Infinite / Weakly Bounded Loop | Loop runs until model informally believes it is complete |
| AP10 | Overpowered Coding Agent | Agent has private data + untrusted content + external comms |

---

## Principles (P1–P8)

1. Prefer Determinism Where the Problem Is Deterministic
2. Complexity Must Earn Its Keep
3. Give Agents Ground Truth
4. Separate Generation From Verification
5. Context Is a Designed Resource
6. Security Boundaries Belong Outside the Model
7. Measure Real Task Success
8. Failures Should Improve the Harness

---

## Discovery Research

`input/ai_agent_design_patterns_discovery.md` — the raw discovery output (2026-08-24) that this catalog is based on. Read it for evidence behind any family or pattern, original source citations, and the research-phase template.

---

Last updated: 2026-11-22
