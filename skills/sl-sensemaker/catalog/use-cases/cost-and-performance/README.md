# cost-and-performance/

Guides for reducing token cost, lowering latency, and scaling agent systems efficiently.

```
cost-and-performance/
├── README.md               ← this file
├── reducing-cost.md        ← cutting token usage and API spend
├── latency.md              ← reducing end-to-end latency
└── routing-and-scaling.md  ← routing requests to right model/tier, scaling patterns
```

## File descriptions

- **reducing-cost.md** — Cutting token usage and API spend; maps to families N, E, B
- **latency.md** — Reducing end-to-end latency; maps to families N, A, C
- **routing-and-scaling.md** — Routing requests to right model/tier, scaling patterns; maps to families N, A

## When to use this folder

Use this folder when operational costs or response times are a concern. The three files cover distinct levers — cost, speed, and routing/scaling — and can be consulted independently based on which constraint you are hitting.

## How to navigate

| Arrival scenario | Go to |
|---|---|
| "My API bill is too high — how do I cut costs?" | `reducing-cost.md` |
| "End-to-end latency is too slow for users" | `latency.md` |
| "I need to route different requests to different models" | `routing-and-scaling.md` |
| "I want to scale my agent system under load" | `routing-and-scaling.md` |

Last updated: 2026-08-24
