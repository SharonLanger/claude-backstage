# designing/

Guides for key design decisions when building agent systems — from first principles to specific architectural choices.

```
designing/
├── README.md              ← this file
├── new-system.md          ← building from scratch; first design decisions
├── multi-agent.md         ← deciding whether and how to use multiple agents
├── tool-design.md         ← designing tools and actions an agent can take
├── memory-and-state.md    ← deciding how agents remember and share information
└── output-integration.md  ← connecting agent output to downstream systems
```

## File descriptions

- **new-system.md** — Building an agent system from scratch; first design decisions
- **multi-agent.md** — Deciding whether and how to use multiple agents; maps to anti-pattern Multi-Agent by Default
- **tool-design.md** — Designing tools and actions an agent can take; maps to families G, F
- **memory-and-state.md** — Deciding how agents remember and share information; maps to families L, E
- **output-integration.md** — Connecting agent output to downstream systems; maps to family O

## When to use this folder

Use this folder when making upfront architecture decisions for a new or evolving agent system. Each file corresponds to a distinct design axis — come to the specific file for the decision you are facing rather than reading sequentially.

## How to navigate

| Arrival scenario | Go to |
|---|---|
| "I'm starting from scratch — what do I decide first?" | `new-system.md` |
| "Should I use one agent or many?" | `multi-agent.md` |
| "How do I design the tools my agent can call?" | `tool-design.md` |
| "How should my agent store and recall information?" | `memory-and-state.md` |
| "How do I wire agent output into the rest of my system?" | `output-integration.md` |

Last updated: 2026-08-24
