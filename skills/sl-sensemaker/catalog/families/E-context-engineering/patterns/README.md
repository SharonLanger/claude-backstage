# Family E — Context Engineering: Patterns

10 patterns covering how to design what information is visible to the model at each step.

**Core insight (Anthropic):** Context engineering is broader than prompt engineering — it encompasses everything that enters the model's context window: instructions, memory, retrieved data, tool results, conversation history, and the order and format of all of it.

**Anti-patterns addressed:** Giant Instruction Manual, Shared Context Everywhere.

---

## File Tree

```
patterns/
├── README.md                        ← this file
├── artifact-based-handoff.md        ← pass structured artifacts between agents, not raw context
├── context-compaction.md            ← compress long histories before they overflow the window
├── context-isolation.md             ← enforce explicit context boundaries per task/user/agent
├── context-offloading.md            ← move stable reference data out of the prompt into retrievable storage
├── just-in-time-retrieval.md        ← fetch knowledge only when the current step requires it
├── map-not-manual.md                ← replace monolithic instructions with a short navigable index
├── minimal-context-handoff.md       ← pass only what the next agent needs, nothing extra
├── progressive-disclosure.md        ← reveal deeper context incrementally as task complexity increases
├── repository-as-system-of-record.md ← keep authoritative knowledge in the repo, not in prompts
└── role-scoped-context.md           ← build context from what the agent's current role requires
```

---

## Schema

Each engineering pattern follows the same structure:

| Section | Contents |
|---|---|
| `# Title` + `**Family:** E` | Pattern name and family tag |
| `## Problem` | The failure mode this pattern addresses — concrete, specific |
| `## Solution` | What to do instead — the core intervention |
| `## Structure` | Mermaid diagram (collapsible) + numbered implementation steps |
| `## When to Use` | Conditions that signal this pattern applies |
| `## When NOT to Use` | Conditions where the pattern is inappropriate or counterproductive |
| `## Tradeoffs` | Two-column table: Benefit vs. Cost |
| `## Related Patterns` | Cross-links with one-line explanation of the relationship |
| `## Anti-Patterns Addressed` | Named anti-patterns this pattern directly counters |
| `## Example` | Concrete scenario illustrating the pattern in action |
| `## Sources` | Attributed sources with organization, role, and URL |

---

## How to Navigate

**By problem type:**
- Too much in the prompt → [map-not-manual.md](map-not-manual.md), [context-offloading.md](context-offloading.md), [progressive-disclosure.md](progressive-disclosure.md)
- Context leaking between tasks or users → [context-isolation.md](context-isolation.md), [role-scoped-context.md](role-scoped-context.md)
- Multi-agent handoffs losing or leaking state → [artifact-based-handoff.md](artifact-based-handoff.md), [minimal-context-handoff.md](minimal-context-handoff.md)
- Context window filling up over long sessions → [context-compaction.md](context-compaction.md)
- Fetching knowledge too early or too late → [just-in-time-retrieval.md](just-in-time-retrieval.md)
- Knowledge lives in prompts instead of the repo → [repository-as-system-of-record.md](repository-as-system-of-record.md)

**Patterns that commonly pair together:**
- Map-Not-Manual + Just-in-Time Retrieval (map tells what to fetch; retrieval is how)
- Context Isolation + Artifact-Based Handoff (boundaries enforced; crossing them requires an explicit artifact)
- Repository-as-System-of-Record + Map-Not-Manual (repo holds the docs; map is the index into them)

Last updated: 2026-08-24
