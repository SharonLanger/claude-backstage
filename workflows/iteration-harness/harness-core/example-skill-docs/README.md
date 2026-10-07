# Skill Reference Docs

Place your skill's **read-only reference documentation** here — the context that agents need to understand the skill they're iterating on.

This folder is **not modified during iteration**. Agents read from it but never write to it.

---

## What to Put Here

| Content | Example |
|---------|---------|
| Skill specification | The full spec your skill implements |
| Domain knowledge | Background context agents need to reason about failures |
| API or format references | Schemas, expected inputs/outputs, contract definitions |
| Architecture notes | How the skill's components relate to each other |
| Constraints | Hard rules the skill must follow (regulatory, performance, compatibility) |
| Reusable knowledge | Patterns, conventions, lessons learned, or best practices that agents should apply across iterations — anything that prevents re-discovering the same insight twice |
| Style guides | Coding conventions, naming rules, tone/voice guidelines the skill must follow |
| Edge cases catalog | Known tricky scenarios, boundary conditions, or failure modes agents should be aware of |

---

## How Agents Use This

- **Reasoner** reads these docs when analyzing test failures — understanding the skill's intent helps produce better root-cause analysis
- **Skill-Change-Agent** reads these docs to understand boundaries before applying fixes
- **Dimension Reviewers** read these docs to score the skill against its own spec
- **Reporter** may reference these docs when describing what a test was checking

---

## Guidelines

- Keep files **focused and concise** — agents have limited context windows
- Use **clear headings** so agents can find relevant sections quickly
- **Don't duplicate** content that's already in the iteration harness (test rules, role definitions, etc.)
- Rename this folder to match your skill (e.g., `my-skill-docs/`) and update references in `format.md`
