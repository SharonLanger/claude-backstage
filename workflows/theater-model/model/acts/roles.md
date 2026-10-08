# Roles: Lead and Cast

Every Act has exactly one Lead and zero or more Cast. These are the two role types in the Theater Model. This page defines their responsibilities, behavioral differences, and how they relate.

## Lead

The Lead is the primary agent in an Act. It coordinates all work, produces the Act's outputs, and is the only role the Stage Manager interacts with directly.

**Key properties:**

- Exactly one per Act — every Act has a Lead.
- Coordinates Cast (if any) by assigning focused subtasks.
- Produces the Act's final outputs in `handoffs/act-NN-slug/`.
- Only Leads call Cast. The Stage Manager does not call Cast directly.
- Can report failure directly to the Stage Manager without waiting for checklist verification, explaining the failure, evidence, and missing dependencies.

**Context:** The Lead starts with fresh context — not forked from the Stage Manager. It loads: shared rules (`play-rules.md`), the Act file, its own Lead file, and the Stage Manager's short assignment prompt.

**On retry:** When the Stage Manager sends corrections after a failed checklist, the same Lead instance continues with its retained context. This is a correction, not a fresh start.

## Cast

Cast are supporting agents within an Act. Each Cast member handles one focused subtask delegated by the Lead.

**Key properties:**

- Zero or more per Act — Cast are optional.
- Each Cast has a single, narrow responsibility.
- Cast report to their Lead only — never to the Stage Manager, never to other Cast.
- Cast do not call other Cast.
- Cast can write to their Act's `stage/` and `handoffs/act-NN-slug/`.
- Cast do not write to `verifications/`, `progress.md`, or another Act's folders.

**Context:** The Lead chooses fresh or forked context for Cast, unless governing instructions prescribe the choice. Cast context loads: shared rules, Act file, Cast file, and the Lead's assignment prompt.

**Multiple instances:** The same Cast definition can be instantiated multiple times with different assignments from the Lead. The definition is the template; the assignment prompt differentiates instances.

## Lead vs Cast comparison

| Property | Lead | Cast |
|----------|------|------|
| Count per Act | Exactly 1 | 0 or more |
| Called by | Stage Manager | Lead |
| Reports to | Stage Manager | Lead |
| Calls others | Can call Cast | Cannot call anyone |
| Context start | Always fresh | Fresh or forked (Lead decides) |
| On retry | Same instance continues | Lead decides (new or reuse) |
| Writes to | `stage/`, `handoffs/act-NN-slug/` | `stage/`, `handoffs/act-NN-slug/` |
| Can report failure early | Yes (to Stage Manager) | No (reports to Lead) |

## Context decisions

The Lead makes context decisions for Cast:

- **Fresh context** — Cast starts clean, loading only rules + Act + Cast file + assignment prompt. Good for independent subtasks where the Lead's prior work isn't needed.
- **Forked context** — Cast starts with the Lead's context at the point of delegation. Good when the Cast needs everything the Lead has already discovered.

Unless the Play definition, Act file, Lead file, or play-rules.md prescribes the choice, the Lead decides per invocation.

## Delegation chain

The Theater Model has a strict delegation chain:

```
Stage Manager → Lead → Cast
```

The Stage Manager assigns the Lead. The Lead assigns Cast. No shortcuts: the Stage Manager never calls Cast directly, and Cast never call other Cast. This keeps coordination centralized in the Lead, who owns the Act's output.

## When to use Lead-only vs Lead + Cast

**Lead-only** works when:
- The Act's work is straightforward and focused.
- One agent can handle the full scope without decomposition.
- The outputs don't benefit from multiple perspectives.

**Lead + Cast** works when:
- The Act's work has natural subtasks that benefit from focused agents.
- Different parts of the work need different expertise or scope constraints.
- The Lead's job is primarily coordination and synthesis, not direct production.

Not every Act needs Cast. A simple Act with a single focused goal is fine with a Lead alone.

## Roles are not reusable across Acts

Each role definition is specific to one Act. The same role name may appear in multiple Acts (e.g., two Acts could each have a `cast-test-writer.md`), but each is an independent definition — there is no shared role abstraction. Reusable cross-Act roles are a possible future extension, not a current feature.

For the Lead file format specification, see [schemas/lead-file.md](../schemas/lead-file.md).
For the Cast file format specification, see [schemas/cast-file.md](../schemas/cast-file.md).
