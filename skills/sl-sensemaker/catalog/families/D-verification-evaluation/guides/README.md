# Family D — Verification & Evaluation: Guides

Navigation hub for the 3 practical and decision guides in this folder.

---

## Practical guide schema

The API guide gives purpose, applicability, a quick tip, steps, an illustration, limits, related patterns, and sources. Cross-family routes include [retrieval](../../E-context-engineering/patterns/just-in-time-retrieval.md) and [executable feedback](../../F-harness-environment/patterns/F03-executable-feedback-loop.md).

## File Tree

```
guides/
├── README.md                  ← this file
├── verify-unfamiliar-api.md   ← verify the actual dependency contract
├── eval-type-selector.md      ← "what eval do I need?" — decision tree mapping symptoms to patterns
└── verification-ladder.md     ← cost escalation ladder — cheapest check first, escalate only as needed
```

---

## What Each File Contains

**eval-type-selector.md** — A structured decision process for choosing which D-family pattern to use. Works through a sequence of yes/no questions (does a test suite define done? is output schema-constrained? would generator context bias the check? etc.). Includes a full Mermaid decision tree, a quick-reference table, common stacking recipes per pipeline type, and the Hamel Husain sequencing rule: collect real failing traces, read them manually, run D11 before designing any targeted evals.

**verification-ladder.md** — A 5-rung escalation table mapping check types to patterns by cost and capability. Rung 1 is deterministic (zero token cost), Rung 5 is human review. Each rung lists which patterns live there, approximate cost per check, and what category of failure it catches. Includes an escalation decision tree, a "when to escalate" prose section, a cost-benefit reference, and a common-mistakes table.

---

## How to Navigate

**If you don't know which pattern to use** — start with `eval-type-selector.md`. Answer the questions top to bottom; the first branch that matches your situation names the right pattern.

**If you're constrained by cost or latency** — start with `verification-ladder.md`. Find the cheapest rung that can catch your failure type, then follow its pattern links into `../patterns/`.

**If you're debugging a live failure** — both guides converge on the same entry point: run D11 (end-to-end task success) first to confirm the failure exists, then D12 (step-level diagnostic) to locate it.

For a questionable generated dependency call, start with [Verify an unfamiliar API](verify-unfamiliar-api.md). The evaluation guides above address broader system checks.

---

Last updated: 2026-11-22
