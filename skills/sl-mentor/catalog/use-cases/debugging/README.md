# debugging/

Symptom-first guides for diagnosing common agent failures. Each file maps symptoms to relevant pattern families and anti-patterns.

```
debugging/
├── README.md                  ← this file
├── agent-not-completing.md    ← loops, stalls, never finishes
├── wrong-outputs.md           ← incorrect or unexpected results
├── tool-failures.md           ← tool calls failing, misused, or erroring
├── context-problems.md        ← context window, lost state, prompt degradation
└── non-determinism.md         ← flaky behavior, inconsistent results across runs
```

## File descriptions

- **agent-not-completing.md** — Agent loops, stalls, or never finishes; maps to families I, H, A; anti-patterns: Infinite/Weakly Bounded Loop, Retry Without New Information
- **wrong-outputs.md** — Agent produces incorrect or unexpected results; maps to families D, E, L; anti-pattern: Self-Certified Completion
- **tool-failures.md** — Tool calls failing, misused, or producing errors; maps to families G, D, F
- **context-problems.md** — Context window issues, lost state, prompt degradation; maps to families E, L; anti-patterns: Shared Context Everywhere, Giant Instruction Manual
- **non-determinism.md** — Flaky behavior, inconsistent results across runs; maps to families H, D, M

## When to use this folder

Use this folder when an agent system is misbehaving and you need to diagnose the cause. Pick the file whose symptom description matches what you are observing — each one traces the symptom back to pattern families and specific anti-patterns to investigate.

## How to navigate

| Arrival scenario | Go to |
|---|---|
| "My agent is stuck in a loop or never returns" | `agent-not-completing.md` |
| "The agent finishes but the output is wrong" | `wrong-outputs.md` |
| "Tool calls are failing or behaving unexpectedly" | `tool-failures.md` |
| "The agent seems to forget things or the prompt is degrading" | `context-problems.md` |
| "Results change randomly between identical runs" | `non-determinism.md` |

Last updated: 2026-08-24
