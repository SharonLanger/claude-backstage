# human-in-the-loop/

Guides for designing agent systems that involve humans at decision points — when to pause, how to structure approvals, and how to avoid over- or under-interrupting.

```
human-in-the-loop/
├── README.md               ← this file
├── when-to-interrupt.md    ← deciding when agents should pause for human input
└── approval-workflows.md   ← designing review gates and approval checkpoints
```

## Practical session routes

- [Clarify an idea](../../families/K-human-control/guides/clarify-an-idea.md)
- [Manage review overload](../../families/K-human-control/guides/manage-review-overload.md)

## File descriptions

- **when-to-interrupt.md** — Deciding when agents should pause for human input; maps to families K, H
- **approval-workflows.md** — Designing review gates and approval checkpoints; maps to families K, H, D

## When to use this folder

Use this folder when designing or tuning the boundary between autonomous agent action and human oversight. Both files are closely related — `when-to-interrupt.md` covers the policy decision, `approval-workflows.md` covers the mechanical implementation.

## How to navigate

| Arrival scenario | Go to |
|---|---|
| "How do I decide which actions require human approval?" | `when-to-interrupt.md` |
| "How do I implement a review gate in my workflow?" | `approval-workflows.md` |
| "My agent is interrupting too often (or not enough)" | `when-to-interrupt.md` |
| "I need to design a multi-step approval process" | `approval-workflows.md` |

Last updated: 2026-11-22
