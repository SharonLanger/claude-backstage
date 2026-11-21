# Family N — Efficiency & Model Routing: Anti-Patterns

2 named failure modes that efficiency patterns must actively avoid.

These are not patterns to apply — they are failure modes to recognize and prevent. Every efficiency pattern in `../patterns/` references one or both of these as the risk it introduces if applied incorrectly.

---

## Files

```
anti-patterns/
├── README.md                        ← this file
├── premature-optimization.md        ← applying efficiency patterns before correctness is established
└── silent-quality-degradation.md    ← shipping efficiency optimizations without quality monitoring
```

---

## Schema

Both files follow the same structure:

| Section | What it contains |
|---|---|
| `# Name` | Canonical anti-pattern name |
| `**Family / Type**` | Family N, Type: Anti-Pattern |
| `## Problem` | How the failure mode arises and what it costs |
| `## Solution` | The corrective discipline that prevents or reverses the failure |
| `## Structure` | Diagram or gate sequence showing the correct order of operations |
| `## Consequences` | What happens when the anti-pattern is not addressed |
| `## Related Patterns` | Which Family N patterns are at risk, and cross-family dependencies |

---

## How to Navigate

**premature-optimization.md** — The sequencing failure. Teams apply routing, trimming, and caching before the system produces correct output. The fix is a hard gate: correctness first (Families D and I), efficiency second (Family N), in that order with no exceptions.

**silent-quality-degradation.md** — The monitoring failure. Efficiency patterns ship but quality metrics are never instrumented. Cost and latency look healthy while accuracy degrades invisibly. The fix is mandatory quality monitoring wired up before any efficiency pattern is deployed to production.

**Cross-family links:** The correctness gate in `premature-optimization` depends on eval infrastructure from Family D. Quality monitoring in `silent-quality-degradation` depends on observability from Family M. Patterns in `../patterns/` each note which anti-pattern they risk introducing.
