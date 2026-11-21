# guides/

Decision guides for Family C: Orchestration & Role Separation.

Guides are opinionated, flow-based documents. They ask diagnostic questions and route you to a conclusion or to the right pattern file. They are not reference material — read them when you are deciding, not after.

## Files

```
guides/
├── README.md                      ← this file
└── do-you-need-multi-agent.md     ← step-by-step decision guide for whether multi-agent orchestration is warranted
```

## When to use this folder

Read `do-you-need-multi-agent.md` before committing to any orchestration pattern, especially when:

- The problem feels like it could be solved by one well-prompted agent
- You are adding agents to a design that already works but feels slow or complex
- A stakeholder is pushing for multi-agent because it sounds more sophisticated
- You want a defensible rationale for why orchestration is or is not the right call

If the guide concludes that multi-agent is warranted, it will point you to the relevant patterns in `../patterns/`. If it concludes otherwise, see `../anti-patterns/multi-agent-by-default.md` for the failure mode you are avoiding.

Last updated: 2026-08-24
