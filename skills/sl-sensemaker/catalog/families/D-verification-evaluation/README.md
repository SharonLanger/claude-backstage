# Family D — Verification & Evaluation

**Recurring problem:** Generated work looks plausible without satisfying the real task.  
**Family answer:** Apply the right type of check — deterministic, structural, LLM-judge, or human — at the right cost.

Related families: A (Generator-Critic is also a topology), H (prefer deterministic checks over LLM checks), K (human calibration = human control), M (observability: trace-linked eval).

---

## Practitioner entry points

- [Review AI changes](patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them) — tests pass after the agent changed assertions; I cannot explain the diff.

## Directory Tree

```
D-verification-evaluation/
├── README.md                              ← this file — navigation hub
│
├── patterns/
│   ├── D01-deterministic-validator.md     ← rule/schema/regex checks; zero LLM cost
│   ├── D02-test-before-done.md            ← tests pass = done; blocks premature completion
│   ├── D03-evidence-based-completion.md   ← completion requires citing concrete evidence
│   ├── D04-independent-verifier.md        ← separate agent re-checks without shared context
│   ├── D05-review-pass.md                 ← structured post-generation review checklist
│   ├── D06-generator-critic.md            ← paired generate/critique loop (see also A family)
│   ├── D07-evaluator-optimizer.md         ← eval score drives the next generation attempt
│   ├── D08-multi-review-ensemble.md       ← N independent reviews; aggregate verdict
│   ├── D09-llm-as-judge.md               ← LLM scores output against rubric
│   ├── D10-human-calibration.md          ← human spot-checks anchor LLM-judge scores
│   ├── D11-end-to-end-task-success.md    ← full task replay; pass/fail on real outcome
│   └── D12-step-level-diagnostic.md      ← per-step scoring to isolate which step failed
│
└── guides/
    ├── verification-ladder.md             ← when to escalate check type (see table below)
    └── eval-type-selector.md              ← "what eval do I need?" decision tree
```

---

For tests that change during a bug fix, see [D02](patterns/D02-test-before-done.md) when the acceptance checks can be protected and [AP10](../../anti-patterns/AP10-overpowered-coding-agent.md) when write access exceeds the task.

## Per-Pattern File Schema

Each engineering entry in `patterns/` follows this structure:

```markdown
# D##: <Pattern Name>

**Intent** — one sentence: what problem it solves.
**Also known as** — alternate names used in literature.

## Problem
What goes wrong without this pattern.

## Solution
Core mechanism in 2–4 sentences.

## Structure
Diagram or prose describing the components and their relationships.

## When to Use
- Conditions that favour this pattern
- Minimum viable trigger (when is it worth the cost?)

## When NOT to Use
- Cases where a cheaper check suffices
- Cases where it gives false confidence

## Implementation Notes
Concrete guidance: schema format, prompt shape, scoring rubric, etc.

## Cost Profile
| Dimension       | Rating (Low / Med / High) |
|-----------------|---------------------------|
| Latency added   |                           |
| Token cost      |                           |
| Implementation  |                           |
| False-positive risk |                       |

## Related Patterns
- Links to patterns in this family and others

## Anti-Patterns Addressed
- Named anti-patterns this pattern prevents
```

---

## Verification Ladder

Use the cheapest check that catches the failure. Escalate only when lower rungs cannot cover the requirement.

| Rung | Type | Patterns | Latency | Token Cost | Catches |
|------|------|----------|---------|------------|---------|
| 1 | **Deterministic** | D01, D02 | ~0 ms | 0 | Schema errors, test failures, constraint violations, exact matches |
| 2 | **Structural / Evidence** | D03, D05 | Low | Low | Missing required artefacts, unsupported claims, checklist gaps |
| 3 | **Independent Agent** | D04, D06, D08 | Med | Med | Logic errors, hallucinations, reasoning gaps a single agent misses |
| 4 | **LLM-as-Judge** | D07, D09, D12 | Med–High | High | Subjective quality, rubric conformance, step-level diagnosis |
| 5 | **Human** | D10, D11 | Hours | N/A | Ground truth, calibration, high-stakes correctness |

**Rule of thumb (from Family H):** if a deterministic check can answer the question, use it. LLM-judge is only justified when the correctness criterion is inherently qualitative.

---

## What Type of Eval Do I Need?

| Question to ask | If yes → use | Pattern |
|-----------------|-------------|---------|
| Is the output schema-valid or rule-compliant? | Deterministic validator | D01 |
| Does passing a test suite define "done"? | Test-Before-Done | D02 |
| Must completion be backed by cited evidence? | Evidence-Based Completion | D03 |
| Would the generating agent's context bias the check? | Independent Verifier | D04 |
| Is there a checklist of required properties to scan? | Review Pass | D05 |
| Should low-quality output trigger another generation attempt? | Generator-Critic or Evaluator-Optimizer | D06, D07 |
| Do you need high-confidence verdict via redundancy? | Multi-Review / Ensemble | D08 |
| Is the quality criterion qualitative (style, tone, reasoning)? | LLM-as-Judge | D09 |
| Is your LLM judge drifting from human standards? | Human Calibration | D10 |
| Does the whole task need a pass/fail on the real outcome? | End-to-End Task-Success Eval | D11 |
| Do you need to find which step in a pipeline broke? | Step-Level Diagnostic Eval | D12 |

---

## Anti-Patterns Addressed by This Family

| Anti-Pattern | Description | Patterns that counter it |
|---|---|---|
| **Self-Certified Completion** | Agent declares done without independent check | D02, D03, D04 |
| **Generic Evals Before Error Analysis** | Applying broad evals before understanding the failure mode | D12 (diagnose first), D01 (cheapest check first) |

---

Last updated: 2026-08-24
