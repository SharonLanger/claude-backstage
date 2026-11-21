# anti-patterns/

Anti-pattern files for Family C: Orchestration & Role Separation.

Each file documents a recurring failure mode — a design choice that feels reasonable but causes harm in practice. Files follow the same structure as pattern files where applicable, with emphasis on the failure mechanism and how to recognize and escape it.

## Files

```
anti-patterns/
├── README.md                      ← this file
└── multi-agent-by-default.md      ← using multi-agent orchestration when a single agent would suffice
```

## When to use this folder

Come here when you need to:

- Recognize a failure mode before or after it appears in a design
- Understand what goes wrong when orchestration is applied where it is not needed
- Find the corrective pattern that replaces the anti-pattern

For the decision of whether multi-agent orchestration is warranted at all, see `../guides/do-you-need-multi-agent.md`. For the patterns that replace these anti-patterns, see `../patterns/`.

Last updated: 2026-08-24
