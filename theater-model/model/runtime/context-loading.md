# Context Loading

Every agent in the Theater Model starts with a defined set of information. Context is not a shared pool that agents dip into -- each agent loads its own context independently, from specific files, in a specific order. What an agent knows is determined by what it loads, and nothing more.

This matters because the Theater Model uses fresh agent instances rather than forked copies of a parent's state. A Lead does not inherit the Stage Manager's accumulated reasoning. A Checklist Agent does not remember last time it verified the same Act. Each agent builds its understanding from the files it reads and the prompt it receives.

## What each agent type loads

| Agent | Context loaded |
|-------|---------------|
| **Stage Manager** | `play.md`, `management/play-rules.md` (via @), `management/stage-manager.md` (own identity), `progress.md`; also reads `handoffs/` and `verifications/` during execution (runtime reads, not pre-loaded) |
| **Lead** | `management/play-rules.md` (via @), Act file (via @), own role file (loaded as identity), assignment prompt from SM, permitted files |
| **Cast** | `management/play-rules.md` (via @), Act file (via @), own role file (loaded as identity), assignment prompt from Lead, permitted files |
| **Checklist Agent** | `management/play-rules.md`, `management/checklist-agent.md` (loaded as identity), current Act checklist and relevant file references (from SM invocation), report destination |

The Stage Manager does not load Act-level files by default. Whether it should have read access to Act definitions and role files is tracked as open question 2.6 -- see [permissions.md](../workspace/permissions.md) for the current state.

## Per-agent detail

### Stage Manager

The Stage Manager reads Play-level governance and execution state. Its context is narrow by design -- it coordinates, it does not do Act work.

- `play.md` -- the full Play definition (Acts, order, Gates, runtime defaults).
- `management/play-rules.md` -- shared rules that all agents follow (loaded via @ reference).
- `management/stage-manager.md` -- the Stage Manager's own role definition.
- `progress.md` -- execution state, updated as Acts complete.

The Stage Manager also reads `handoffs/` and `verifications/` outputs during execution, but these are runtime reads driven by the flow, not pre-loaded context.

### Lead

The Lead builds its context from four sources, loaded in this order:

1. **Shared rules** -- `management/play-rules.md`, loaded via @ reference at the top of the role file.
2. **Act definition** -- the Act file (e.g., `act-01-review-quality.md`), loaded via @ reference at the top of the role file.
3. **Role file** -- the Lead's own file (e.g., `lead-quality-reviewer.md`), loaded as identity.
4. **Assignment prompt** -- a short prompt from the Stage Manager pointing to relevant inputs and the task at hand.

After loading, the Lead may read additional files within its permitted access -- `reference/`, `props/`, prior Acts' `handoffs/` -- as the work requires.

### Cast

Cast context follows the same four-source pattern as the Lead:

1. **Shared rules** -- `management/play-rules.md` (via @).
2. **Act definition** -- the Act file (via @).
3. **Role file** -- the Cast member's own file (loaded as identity).
4. **Assignment prompt** -- a short prompt from the Lead describing the specific subtask.

The Lead decides whether each Cast member gets fresh context or is forked from the Lead's own state, unless the governing instructions (Play definition, Act file, Lead file, or play-rules.md) prescribe the choice. Fresh is the default assumption.

### Checklist Agent

The Checklist Agent receives its context through a combination of its definition file and the Stage Manager's invocation. The `@./play-rules.md` reference in the CA's definition file specifies what shared rules to load; the Stage Manager's invocation triggers the loading and provides the Act-specific context.

- `management/play-rules.md` -- shared rules.
- `management/checklist-agent.md` -- loaded as identity (includes golden rules).
- Current Act checklist and relevant file references -- provided in the SM's invocation prompt.
- Report destination path -- where to write the verification report.

Every Checklist Agent instance is fresh. No verification result, reasoning, or accumulated context carries over from a previous invocation.

## The @ reference convention

Role files (Lead and Cast) use explicit @ references to load shared context. These appear as the first two lines of the file, before any headings or content:

```
@../../management/play-rules.md
@./act-01-review-quality.md
```

Paths are relative to the role file's location. From `acts/act-01-review-quality/`:
- `@../../management/play-rules.md` -- up two levels to the Play root, then into `management/`.
- `@./act-01-review-quality.md` -- the Act file in the same folder.

Both @ references are mandatory for every Lead and Cast file. No other content may precede them.

The @ convention is a model-level directive -- it tells the runtime what to load into the agent's context. Runtime resolution and reliable loading remain implementation tasks. The @ reference is a contract between the Play author and the runtime: "this file must be in context." It is not a guarantee that every runtime environment will handle it identically.

## Fresh context principle

Agents do not inherit context from their callers:

- **Lead** -- starts fresh. Not forked from the Stage Manager. The SM's assignment prompt is deliberately short, pointing to files rather than duplicating their content.
- **Checklist Agent** -- always a fresh instance. No memory of prior verifications, even of the same Act. This is by design -- honest re-verification requires examining current evidence without anchoring to previous judgments.
- **Cast** -- fresh by default. The Lead may fork Cast from its own context if the work benefits from shared state, but fresh is the baseline. Governing instructions may prescribe the choice.
- **Stage Manager** -- the one persistent agent. It retains context across Acts within a single Run. When it retries a Lead, it resumes the same Lead instance (retained context), but it does not share its own context with that instance.

## Assignment prompts

Assignment prompts are the glue between coordination and execution. They connect the delegating agent (SM or Lead) to the receiving agent (Lead or Cast).

**Stage Manager to Lead:**
Short. Points to the Act definition, relevant inputs (handoffs from prior Acts, reference files), and the specific task. Does not duplicate file contents. Does not contain permissions or definitions -- those come from the files the Lead loads.

**Lead to Cast:**
Short. Describes the specific subtask, points to relevant files in `stage/` or `props/`, and sets any instance-specific parameters. Like the SM's prompt, it does not redefine rules or expand permissions.

Task information in assignment prompts cannot change permissions, override locked definitions, or bypass Gates. The prompt adds work context; it does not alter governance.

## Override precedence

When context sources conflict, later (more specific) sources take precedence:

```
Play (play-rules.md) --> Act definition --> Role file --> Assignment prompt
```

This is the loading order, and later entries override earlier ones for configurable settings. But the override rule from the governance hierarchy matters more than the loading sequence: Play-level rules override Act-level rules override Role-level rules for anything marked HARD. A role file cannot weaken a rule from `play-rules.md`. An assignment prompt cannot expand permissions defined in a role file. For runtime settings precedence, see [settings-and-defaults.md](settings-and-defaults.md).

The practical effect: shared rules set the floor. Act definitions customize within that floor. Role files specialize further. Assignment prompts add task-specific context but cannot lower the floor.

---

Related: [schemas/lead-file.md](../schemas/lead-file.md) and [schemas/cast-file.md](../schemas/cast-file.md) for the @ reference format and required sections. [workspace/permissions.md](../workspace/permissions.md) for the full read/write matrix. [agents/stage-manager.md](../agents/stage-manager.md) and [agents/checklist-agent.md](../agents/checklist-agent.md) for agent role definitions. [execution/flow.md](../execution/flow.md) for the sequence in which agents are invoked.
