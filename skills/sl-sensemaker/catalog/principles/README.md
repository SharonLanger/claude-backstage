# Principles

8 high-confidence cross-source principles that explain *why* the patterns in this catalog are shaped the way they are. Each principle appeared independently across Anthropic, OpenAI, Google, AWS, Microsoft, and OWASP.

Principles are not patterns. They don't tell you what to build — they explain the reasoning that makes certain patterns consistently effective and others consistently fragile.

```
principles/
├── README.md                              ← this file — navigation hub
├── index.md                               ← one-page cross-reference: principles × families × anti-patterns
├── P1-prefer-determinism.md               ← Prefer Determinism Where the Problem Is Deterministic
├── P2-complexity-earns-its-keep.md        ← Complexity Must Earn Its Keep
├── P3-give-agents-ground-truth.md         ← Give Agents Ground Truth
├── P4-separate-generation-verification.md ← Separate Generation From Verification
├── P5-context-is-designed-resource.md     ← Context Is a Designed Resource
├── P6-security-boundaries-outside-model.md← Security Boundaries Belong Outside the Model
├── P7-measure-real-task-success.md        ← Measure Real Task Success
└── P8-failures-improve-the-harness.md     ← Failures Should Improve the Harness
```

---

## How to Use This Folder

**If you're designing a new system:** read `index.md` first. It maps each principle to the families it governs, so you can jump directly to relevant patterns.

**If you're debugging a recurring failure:** find the principle that names the failure mode, then follow its counter-pattern links.

**If you're writing a pattern file** in `families/`: link back to the principle(s) that motivate the pattern's core rule. One or two links per pattern is enough.

**If you're reading a principle file:** each one is self-contained. You don't need to read them in order.

---

## Principle Files — What Each Contains

Every principle file (`P1`–`P8`) uses the same structure:

| Field | What it captures |
|---|---|
| **Statement** | One sentence — the principle itself, exactly as named |
| **Problem it addresses** | The failure mode that appears when this principle is violated |
| **Why it holds** | The underlying reason this constraint matters for probabilistic systems |
| **Evidence** | Which sources named this principle independently (Anthropic / OpenAI / Google / AWS / Microsoft / OWASP) |
| **Related families** | Links to the pattern families that operationalize this principle |
| **Counter-patterns** | The anti-patterns that arise when this principle is ignored (links to `anti-patterns/`) |
| **Tension with** | Other principles this one trades off against, and when to resolve the tension |
| **Smell** | One-line diagnostic: if you see X in your system, this principle is probably being violated |

---

## The 8 Principles at a Glance

### P1 — Prefer Determinism Where the Problem Is Deterministic
`P1-prefer-determinism.md`

Problem: correctness rules encoded in prompts can be obeyed or disobeyed probabilistically — the same as any other instruction.

Related families: H (Deterministic Control), G (Tool Design), O (Output Boundaries)
Counter-patterns: Prompt-as-Policy, Model as Security Boundary

---

### P2 — Complexity Must Earn Its Keep
`P2-complexity-earns-its-keep.md`

Problem: multi-agent systems and elaborate orchestration are added for their own sake, multiplying failure surfaces without proportional capability gain.

Related families: C (Orchestration), B (Task Decomposition), N (Efficiency)
Counter-patterns: Multi-Agent by Default

---

### P3 — Give Agents Ground Truth
`P3-give-agents-ground-truth.md`

Problem: agents working from stale, ambiguous, or incomplete information produce plausible-looking wrong output, and there is no way to detect the error without external evidence.

Related families: E (Context Engineering), F (Harness), L (Memory & State)
Counter-patterns: Giant Instruction Manual, Shared Context Everywhere

---

### P4 — Separate Generation From Verification
`P4-separate-generation-verification.md`

Problem: the component that produces output is structurally biased toward validating its own output — self-review catches far fewer errors than independent review.

Related families: D (Verification & Evaluation), C (Orchestration), A (Workflow Topology)
Counter-patterns: Self-Certified Completion

---

### P5 — Context Is a Designed Resource
`P5-context-is-designed-resource.md`

Problem: context that grows unbounded, contains noise, or is shared indiscriminately degrades performance in ways that are hard to diagnose because the model still produces output.

Related families: E (Context Engineering), L (Memory & State), F (Harness)
Counter-patterns: Giant Instruction Manual, Shared Context Everywhere

---

### P6 — Security Boundaries Belong Outside the Model
`P6-security-boundaries-outside-model.md`

Problem: a model that decides its own authorization can be manipulated by the content it processes — authorization logic that lives in a prompt is only as safe as the model's obedience under adversarial input.

Related families: J (Security & Trust), H (Deterministic Control), G (Tool Design)
Counter-patterns: Prompt-as-Policy, Model as Security Boundary, Overpowered Coding Agent

---

### P7 — Measure Real Task Success
`P7-measure-real-task-success.md`

Problem: proxy metrics (fluency, format compliance, step completion) diverge from real task outcomes; systems optimized against proxies produce output that looks correct but isn't.

Related families: D (Verification & Evaluation), M (Observability), F (Harness)
Counter-patterns: Generic Evals Before Error Analysis, Self-Certified Completion

---

### P8 — Failures Should Improve the Harness
`P8-failures-improve-the-harness.md`

Problem: when failures are treated as isolated incidents rather than diagnostic signals, the same failure mode recurs across tasks because the system that produced it remains unchanged.

Related families: F (Harness), I (Reliability & Recovery), M (Observability)
Counter-patterns: Retry Without New Information, Generic Evals Before Error Analysis

---

## Index File

`index.md` is the single cross-reference table for this folder. It shows:

- Which families each principle governs (rows = principles, columns = families A–O)
- Which anti-patterns each principle predicts
- Which principles tension each other (the tradeoff matrix)

Use it when you know the principle but not the family, or when you want to understand which principles a given family is built on.

---

Last updated: 2026-08-24
