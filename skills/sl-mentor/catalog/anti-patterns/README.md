# Anti-Patterns

10 named failure modes in LLM/agent systems — recurring structures that cause real-world failures. Each file documents the failure mode, its root cause, detection signals, and the counter-patterns from families A–O that address it.

```
anti-patterns/
├── README.md                                    ← this file — navigation hub
├── AP01-self-certified-completion.md            ← agent claims done with no external evidence
├── AP02-prompt-as-policy.md                     ← security/correctness rule lives only in natural language
├── AP03-giant-instruction-manual.md             ← all rules crammed into one huge system prompt
├── AP04-retry-without-new-information.md        ← failed attempt retried with no additional feedback
├── AP05-multi-agent-by-default.md               ← team of agents used where a single workflow suffices
├── AP06-model-as-security-boundary.md           ← model decides its own authorization
├── AP07-shared-context-everywhere.md            ← all agents receive all history and reference material
├── AP08-generic-evals-before-error-analysis.md  ← generic metrics adopted before studying real failures
├── AP09-infinite-weakly-bounded-loop.md         ← loop runs until model informally believes it is done
└── AP10-overpowered-coding-agent.md             ← agent holds private data + untrusted content + external comms simultaneously
```

---

## What Each Anti-Pattern File Contains

Every file is structured identically:

| Section | Contents |
|---------|----------|
| **Summary** | One-sentence definition of the failure mode |
| **How It Happens** | Root cause — why teams fall into this pattern |
| **Failure Modes** | Concrete ways it manifests at runtime |
| **Detection Signals** | Observable indicators that you are already in it |
| **Counter-Patterns** | Families and specific patterns that resolve it (with links) |
| **Migration Path** | Minimal steps to move from the anti-pattern to a safer structure |
| **Examples** | Short concrete scenarios: one naive implementation, one corrected |

---

## Quick Reference: Anti-Pattern → Counter-Pattern Families

| # | Anti-Pattern | Primary Families | Supporting Families |
|---|---|---|---|
| AP01 | Self-Certified Completion | D (Verification & Evaluation), H (Deterministic Control) | A (Bounded Loop), K (Human Control) |
| AP02 | Prompt-as-Policy | H (Deterministic Control), J (Security & Trust) | G (Tool & Action Design), O (Output Boundaries) |
| AP03 | Giant Instruction Manual | E (Context Engineering), F (Harness/Environment) | B (Task Decomposition), C (Orchestration) |
| AP04 | Retry Without New Information | I (Reliability & Recovery), M (Observability) | D (Verification), H (Deterministic Control) |
| AP05 | Multi-Agent by Default | A (Workflow Topology), N (Efficiency & Routing) | B (Task Decomposition), C (Orchestration) |
| AP06 | Model as Security Boundary | J (Security & Trust), H (Deterministic Control) | G (Tool & Action Design), K (Human Control) |
| AP07 | Shared Context Everywhere | E (Context Engineering), L (Memory & State) | C (Orchestration), N (Efficiency & Routing) |
| AP08 | Generic Evals Before Error Analysis | D (Verification & Evaluation), M (Observability) | F (Harness/Environment), I (Reliability & Recovery) |
| AP09 | Infinite / Weakly Bounded Loop | H (Deterministic Control), A (Workflow Topology) | I (Reliability & Recovery), K (Human Control) |
| AP10 | Overpowered Coding Agent | J (Security & Trust), G (Tool & Action Design) | H (Deterministic Control), F (Harness/Environment) |

---

## Detection at a Glance

Use this column to decide quickly whether an anti-pattern applies to your system.

| Anti-Pattern | You might be here if… |
|---|---|
| AP01 Self-Certified Completion | The agent's success signal is its own output text ("Task complete.") with no external check |
| AP02 Prompt-as-Policy | A must-hold rule (auth, safety, format) is enforced only by words in the system prompt |
| AP03 Giant Instruction Manual | Your AGENTS.md / system prompt exceeds ~500 tokens or mixes unrelated domains in one file |
| AP04 Retry Without New Information | Agent retries on failure with an identical or near-identical prompt and no new error context |
| AP05 Multi-Agent by Default | You added agents to increase quality, but latency/cost rose and quality did not improve |
| AP06 Model as Security Boundary | Authorization logic runs inside the model (prompt says "only do X if user is admin") |
| AP07 Shared Context Everywhere | Every subagent receives the full conversation history and all reference docs regardless of role |
| AP08 Generic Evals Before Error Analysis | You are tracking ROUGE/BLEU/pass@1 but cannot explain the last three production failures |
| AP09 Infinite / Weakly Bounded Loop | The loop exit condition is "the model decides it is done" with no hard iteration cap |
| AP10 Overpowered Coding Agent | The agent can read private data, process untrusted user input, AND call external APIs — all at once |

---

## Relationship to Principles

Each anti-pattern violates one or more of the 8 cross-cutting principles in `../principles/`.

| Anti-Pattern | Violated Principle(s) |
|---|---|
| AP01 | P4 — Separate Generation From Verification |
| AP02 | P1 — Prefer Determinism Where the Problem Is Deterministic |
| AP03 | P5 — Context Is a Designed Resource |
| AP04 | P8 — Failures Should Improve the Harness; P3 — Give Agents Ground Truth |
| AP05 | P2 — Complexity Must Earn Its Keep |
| AP06 | P6 — Security Boundaries Belong Outside the Model |
| AP07 | P5 — Context Is a Designed Resource |
| AP08 | P7 — Measure Real Task Success |
| AP09 | P1 — Prefer Determinism Where the Problem Is Deterministic |
| AP10 | P6 — Security Boundaries Belong Outside the Model |

---

## How to Use This Folder

**Diagnosing a live system:** Start with the Detection at a Glance table. Match a symptom, open the file, check the Detection Signals section for confirmation.

**Reviewing a design:** Read AP05 (Multi-Agent by Default) and AP10 (Overpowered Coding Agent) before finalizing any multi-agent architecture. They are the most common early-design mistakes.

**Fixing a specific failure:** Find the anti-pattern file, go directly to Counter-Patterns and Migration Path.

**Understanding the full picture:** Anti-patterns are the inverse of the pattern families. If a family describes what to do, the anti-pattern describes the structure you end up with when you ignore that family. Reading both together is faster than reading either alone.

---

Last updated: 2026-08-24
