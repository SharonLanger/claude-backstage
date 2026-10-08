# Runtime Settings and Defaults

## What runtime settings are

Runtime settings are configurable values that affect how an agent operates — model choice, reasoning effort, and potentially other execution parameters. They tune agent behavior without changing what the agent is allowed to do.

Runtime settings are NOT permissions, Gates, or locked-file restrictions. Those are hard constraints defined in the Rules section and the folder map of `play-rules.md`. Runtime settings cannot weaken or override them.

## The precedence chain

Settings resolve from broad to specific. More-specific definitions win.

```
Play defaults  →  Act defaults  →  Role overrides
(play-rules.md)   (act-NN-slug.md)  (lead-*.md / cast-*.md)
```

Each level can override values set by the level above. When a setting is omitted at a given level, the value from the level above carries through unchanged.

**Where each level is defined:**

| Level | File | Section |
|-------|------|---------|
| Play defaults | `management/play-rules.md` | `## Runtime defaults` |
| Act defaults | `acts/act-NN-slug/act-NN-slug.md` | `## Runtime defaults` |
| Role overrides | `acts/act-NN-slug/lead-*.md` or `cast-*.md` | `## Runtime overrides` |

## Inheritance

Omitted settings are inherited from the level above. Only explicitly stated values override.

**Example:**

1. Play sets: model A, effort medium.
2. Act overrides: effort high. (Model is omitted — inherits model A.)
3. Role overrides: model B. (Effort is omitted — inherits high from Act.)
4. Effective settings for that role: model B, effort high.

An Act or role file that states "Inherit from `play-rules.md`." or "None. Inherits Act defaults." takes all values from the level above without change.

## What cannot be overridden

The following are hard constraints. They live in `## Rules` sections, the folder map, and Gate definitions — never in runtime settings sections. No Act default or role override can weaken them.

- **Permissions** — read/write access boundaries from the folder map and role Access sections.
- **Gates** — mandatory Director-approval stops.
- **Locked-file restrictions** — static files (`play.md`, `management/`, Act definitions, role files, `reference/`, `props/`) remain locked during execution.
- **Mandatory rules** — every item in a `## Rules` section (Play-level or Act-level).

More-specific instructions may add detail or impose stricter limits, but they cannot expand permission or relax mandatory rules. For the general specificity rule on non-runtime instructions, see [rules/authority.md](../rules/authority.md).

## The separation: Rules vs Runtime

Each file that carries both constraints and settings keeps them in separate, clearly labeled sections:

| Section | Nature | Overridable? |
|---------|--------|--------------|
| `## Rules` | HARD constraints | No. Not by settings, not by agent instructions. |
| `## Runtime defaults` / `## Runtime overrides` | CONFIGURABLE values | Yes, by more-specific levels in the precedence chain. |

This separation is structural. A Play author puts mandatory constraints in Rules and tuning knobs in Runtime defaults. Agents reading the file know which parts they must obey unconditionally and which parts may be superseded by their own role file.

## Management agents

The Stage Manager and Checklist Agent are Play-level agents defined in `management/`. They operate outside the Act structure, so they have no Act layer in the precedence chain.

Their settings resolve as:

```
Play defaults  →  Management agent's own Runtime defaults
(play-rules.md)   (stage-manager.md / checklist-agent.md)
```

The Stage Manager schema includes a `## Runtime defaults` section that can override Play defaults or state "Inherit from `play-rules.md` unless overridden here."

The Checklist Agent definition is entirely HARD — identical across all Plays — and does not include a runtime settings section. Its behavior is fixed by design.

**Open question (2.5):** Three aspects of management-agent settings remain open: (a) no concrete model choice or complete setting schema is approved yet, (b) whether a management-level override should be treated as equivalent to an Act-level override or as a separate tier, and (c) how a caller resolves the effective settings before launching another agent. See open question 2.5 in the definition log for the full scope.

## Current state

No concrete model choice or complete setting schema is approved yet. The precedence chain and inheritance rules are defined, but the full list of configurable settings — beyond model and effort — remains open. See open question 2.5 in the definition log for the outstanding items.

---

**Related files:**

- [schemas/play-rules-md.md](../schemas/play-rules-md.md) — file format for `play-rules.md`, including the Runtime defaults section spec
- [schemas/act-file.md](../schemas/act-file.md) — Act definition schema with Runtime defaults section
- [schemas/lead-file.md](../schemas/lead-file.md) — Lead role schema with Runtime overrides section
- [schemas/cast-file.md](../schemas/cast-file.md) — Cast role schema with Runtime overrides section
- [schemas/stage-manager-md.md](../schemas/stage-manager-md.md) — Stage Manager schema with Runtime defaults section
- [agents/stage-manager.md](../agents/stage-manager.md) — Stage Manager conceptual description
- [agents/checklist-agent.md](../agents/checklist-agent.md) — Checklist Agent conceptual description
