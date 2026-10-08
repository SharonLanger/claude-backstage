# Locations

The Play folder has four categories of content locations. Each serves a different purpose and has different access rules.

## Static input locations

### `reference/`

Shared input data available to all Acts. Populated during setup, locked during execution.

**What goes here:** Files that multiple Acts need to read — source code being reviewed, requirements documents, security criteria, API specifications. Anything that is shared context rather than Act-specific input.

**Who reads it:** Every Act actor (Lead and Cast) in the Play.

**Key rule:** `reference/` is read-only during execution. If an Act produces new shared data, it goes to `handoffs/`, not `reference/`.

### `props/`

Act-specific static input data. Each Act has its own `props/` folder inside its Act directory (`acts/act-NN-slug/props/`).

**What goes here:** Files that only one Act needs — review dimension definitions, specific configuration for that Act's task, supplementary criteria. Props are the Act-level equivalent of `reference/`.

**Who reads it:** That Act's Lead and Cast only.

**Key rule:** `props/` is read-only during execution. Props are prepared during setup alongside the Act definition. If the Director needs to provide additional input mid-execution, that is a deliberate override.

### How to choose: `reference/` vs `props/`

| Question | If yes → |
|----------|----------|
| Will multiple Acts read this file? | `reference/` |
| Is it specific to one Act's task? | `props/` |
| Does it come from outside the Play? | `reference/` |
| Is it a decomposition of the Act's goal? | `props/` |

When uncertain, prefer `reference/`. Shared availability does no harm; hidden data causes missing dependencies.

## Mutable working locations

### `stage/`

Act-internal mutable workspace. Each Act has its own `stage/` folder inside its Act directory (`acts/act-NN-slug/stage/`).

**What goes here:** Intermediate files that actors produce during work — partial findings, draft outputs, coordination artifacts between Lead and Cast. Stage files are working material, not final outputs.

**Who reads it:** That Act's Lead and Cast. The Checklist Agent may also read the target Act's `stage/` when needed for verification evidence. No other Act or management agent reads `stage/`.

**Who writes it:** That Act's Lead and Cast. Both may create, modify, and read files in `stage/`.

**Key rules:**
- Stage content is internal to the Act. Other Acts cannot see it.
- The Act file defines `stage/` organization (which files go where, naming conventions for Cast outputs). There is no universal internal layout — each Act designs its own.
- Final outputs move from `stage/` to `handoffs/` when the Act completes.

### `handoffs/`

Shared output location. Each Act gets a subfolder in `handoffs/` matching its name (`handoffs/act-NN-slug/`).

**What goes here:** Final, published outputs from an Act. Review reports, fixed files, test results — anything downstream Acts or the Director needs. Handoff files are the Act's contribution to the Play.

**Who reads it:** Everyone in the Play. All Act actors, the Stage Manager, the Checklist Agent, and the Director can read any Act's handoff folder.

**Who writes it:** That Act's actors (Lead and Cast). No one outside the Act writes to its handoff folder.

**Key rules:**
- Handoff files are the primary channel between Acts. An Act's inputs typically include `reference/` plus handoffs from earlier Acts.
- Once published, handoff files are not modified by later Acts. A later Act that transforms earlier output writes its own version to its own `handoffs/` folder.
- The distinction matters: `stage/` is scratch paper visible only inside the Act; `handoffs/` is the published result visible to everyone.

## Verification location

### `verifications/`

Verification reports organized by Act. Each Act gets a subfolder (`verifications/act-NN-slug/`).

**What goes here:** Reports written by the Checklist Agent after verifying an Act's outputs. One report per verification execution, named `<act-folder>-attempt-NN.md`.

**Who reads it:** Everyone in the Play.

**Who writes it:** Only the Checklist Agent. One new report per verification. Earlier reports are preserved — never edited or deleted.

**Key rules:**
- Report naming counts verification executions, not Lead retries. A Lead retry followed by re-verification produces the next attempt number.
- The Stage Manager reads verification reports to make recovery decisions but never modifies them.
- Exceptions are recorded in `progress.md`, not in verification reports. A FAIL verdict stays FAIL.

## Summary table

| Location | Scope | Static/Mutable | Read by | Written by |
|----------|-------|----------------|---------|------------|
| `reference/` | Play-wide | Static | All Act actors | Setup only |
| `props/` | Per Act | Static | That Act's actors | Setup only |
| `stage/` | Per Act | Mutable | That Act's actors + Checklist Agent | That Act's actors |
| `handoffs/` | Per Act, shared reads | Mutable | Everyone | That Act's actors |
| `verifications/` | Per Act, shared reads | Mutable (append-only) | Everyone | Checklist Agent only |

---

For the full folder tree with access annotations, see [folder-structure.md](folder-structure.md). For the complete read/write matrix, see [permissions.md](permissions.md).
