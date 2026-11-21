# Family F — Harness/Environment Engineering: Patterns

11 patterns covering the repository, tools, instructions, feedback loops, tests, and execution environment that make coding agents reliable.

**Core insight (OpenAI):** When agents fail repeatedly on real tasks, the issue is often the environment, not the model. The "harness" — everything surrounding the model — determines whether it can perform. Improving the harness yields more reliable gains than switching models.

**Term coined by:** OpenAI Engineering.

---

## File Tree

```
patterns/
├── README.md                              ← this file
├── F01-agent-legible-repository.md        ← organize the repo so agents navigate correctly on first contact
├── F02-repository-local-system-of-record.md ← keep authoritative knowledge in versioned repo files
├── F03-executable-feedback-loop.md        ← wire tests/linters so agents can self-correct in seconds
├── F04-mechanical-architecture-constraints.md ← enforce structure via tooling, not instruction
├── F05-agent-accessible-tools.md          ← make every needed tool discoverable and invocable by agents
├── F06-structured-repository-instructions.md ← write machine-readable instructions (CLAUDE.md/AGENTS.md)
├── F07-agent-skills-procedures.md         ← package reusable multi-step procedures as callable skills
├── F08-sandboxed-execution.md             ← run agent-generated code in isolated environments
├── F09-persistent-task-artifacts.md       ← commit progress to durable artifacts, not conversation memory
├── F10-agent-to-agent-review.md           ← have a second agent review the first agent's output
└── F11-capability-gap-feedback.md         ← surface gaps between what agents need and what the harness provides
```

---

## Schema

Each engineering pattern follows the same structure:

| Section | Contents |
|---|---|
| `# FNN — Title` | Pattern name with family-scoped number |
| `## Problem` | The failure mode this pattern addresses — concrete, specific |
| `## Solution` | What to do instead — the core intervention |
| `## Structure` | Mermaid diagram (collapsible) + key components list |
| `## Implementation` | Numbered steps for putting the pattern in place |
| `## Signals` | Observable indicators that the pattern is working |
| `## Anti-Patterns` | Named failure modes this pattern directly counters |
| `## Related Patterns` | Cross-links with one-line explanation of the relationship |
| `## Examples` | Concrete scenarios or code illustrating the pattern |
| `## Sources` | Attributed sources with organization, role, and URL |

---

## How to Navigate

**By problem type:**
- Agent gets lost in the codebase → [F01](F01-agent-legible-repository.md), [F06](F06-structured-repository-instructions.md)
- Knowledge lives in prompts, not the repo → [F02](F02-repository-local-system-of-record.md)
- Agent cannot verify its own output → [F03](F03-executable-feedback-loop.md)
- Agent violates architectural rules despite instructions → [F04](F04-mechanical-architecture-constraints.md)
- Agent cannot find or call the right tools → [F05](F05-agent-accessible-tools.md)
- Repeated multi-step procedures require re-explanation → [F07](F07-agent-skills-procedures.md)
- Agent-generated code runs in the live environment → [F08](F08-sandboxed-execution.md)
- Progress is lost when a session ends → [F09](F09-persistent-task-artifacts.md)
- No review step before agent output is accepted → [F10](F10-agent-to-agent-review.md)
- Agents fail because they lack capabilities the task needs → [F11](F11-capability-gap-feedback.md)

**Patterns that commonly pair together:**
- F01 + F06 (legible repo structure + machine-readable instructions — same CLAUDE.md serves both)
- F03 + F08 (executable feedback requires sandboxed execution to be safe)
- F07 + F09 (skills encode procedures; artifacts persist their outputs)
- F02 + F09 (system of record + persistent artifacts — both use the repo as the durable store)

Last updated: 2026-08-24
