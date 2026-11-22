# evaluation/

Guides for measuring, testing, and improving agent system quality — from baseline evals to regression detection and production-driven test creation.

```
evaluation/
├── README.md               ← this file
├── evaluating-agents.md    ← how to measure if an agent system is working
├── regression-testing.md   ← detecting regressions after changes
└── evals-from-errors.md    ← building evals from production failures
```

## Practical session routes

- [Make intentional decisions visible](../../families/E-context-engineering/guides/clarify-domain-terms.md#make-an-intentional-decision-visible-at-the-edit)

## File descriptions

- **evaluating-agents.md** — How to measure if an agent system is working; maps to families D, M; source: Hamel Husain & Shreya Shankar methodology
- **regression-testing.md** — Detecting regressions after changes; maps to families D, M, F
- **evals-from-errors.md** — Building evals from production failures (not generically); maps to families D, M; anti-pattern: Generic Evals Before Error Analysis

## When to use this folder

Use this folder when you need to assess, test, or improve the quality of an agent system. Read `evaluating-agents.md` first if you are starting from scratch; go to `evals-from-errors.md` if you already have production failures to learn from.

## How to navigate

| Arrival scenario | Go to |
|---|---|
| "I have no evals yet — where do I start?" | `evaluating-agents.md` |
| "I changed something and want to catch regressions" | `regression-testing.md` |
| "I have real production failures — how do I turn them into tests?" | `evals-from-errors.md` |
| "My evals feel generic and not catching real issues" | `evals-from-errors.md` |

Last updated: 2026-11-22
