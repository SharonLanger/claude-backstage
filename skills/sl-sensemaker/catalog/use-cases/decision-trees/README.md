# decision-trees/

Structured decision aids — trees and maps that route you from a symptom, problem, or question to the right pattern family, architecture choice, or anti-pattern.

```
decision-trees/
├── README.md                  ← this file
├── which-family.md            ← "I have X problem — which family?" covering all 15 families A–O
├── architecture-choices.md    ← key architecture forks with tradeoffs
└── anti-pattern-detector.md   ← symptoms → which anti-pattern you may have
```

## File descriptions

- **which-family.md** — "I have X problem — which family?" decision tree covering all 15 families A–O
- **architecture-choices.md** — Key architecture forks with tradeoffs (single vs multi-agent, fixed vs dynamic workflow, etc.)
- **anti-pattern-detector.md** — Symptoms → which anti-pattern you may have; all 10 anti-patterns

## When to use this folder

Use this folder when you know what problem you have but don't know which part of the catalog addresses it. These files are navigation accelerators — they shorten the path from "I have this problem" to "here is the relevant pattern."

## How to navigate

| Arrival scenario | Go to |
|---|---|
| "I have a specific problem — which pattern family covers it?" | `which-family.md` |
| "I'm at a design fork and need to understand the tradeoffs" | `architecture-choices.md` |
| "Something feels wrong — could I be hitting an anti-pattern?" | `anti-pattern-detector.md` |
| "I want to check all 10 anti-patterns against my system" | `anti-pattern-detector.md` |

Last updated: 2026-08-24
