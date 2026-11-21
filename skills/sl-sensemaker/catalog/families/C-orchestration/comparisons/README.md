# comparisons/

Side-by-side comparison files for Family C: Orchestration & Role Separation.

Each file places two or three similar-sounding patterns next to each other and maps out the precise distinctions — where they overlap, where they diverge, and which signals point to each one.

## Files

```
comparisons/
├── README.md                                  ← this file
├── manager-vs-orchestrator-vs-coordinator.md  ← distinguishes the three top-level control patterns
└── reviewer-vs-checker-vs-synthesizer.md      ← distinguishes the three output-handling role patterns
```

## When to use this folder

Come here when you have narrowed down to a small set of candidates and need to make a final choice. Typical triggers:

- "Should this be a manager or an orchestrator?" — read `manager-vs-orchestrator-vs-coordinator.md`
- "Is maker-checker the same as specialist-reviewer?" — read `reviewer-vs-checker-vs-synthesizer.md`
- A pattern name is ambiguous and you want a precise definition relative to its neighbors

If you have not yet narrowed down to candidates, start in `../patterns/` and read the When to Use / When Not to Use sections of the patterns you are considering.

Last updated: 2026-08-24
