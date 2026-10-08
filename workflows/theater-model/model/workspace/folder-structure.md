# Folder Structure

The canonical layout of a Play folder. Every Play follows this structure; the specific Act names and actor files vary per Play. There is no required parent folder or enclosing container — a Play folder can live anywhere.

## The tree

```
play/
├── play.md                              [static]
├── progress.md                          [writable by: Stage Manager]
├── management/                          [static]
│   ├── stage-manager.md
│   ├── checklist-agent.md
│   └── play-rules.md
├── reference/                           [static, read: all]
├── verifications/
│   └── <act-NN-slug>/                   [writable by: Checklist Agent (new reports only)]
│       ├── <act-NN-slug>-attempt-01.md
│       └── <act-NN-slug>-attempt-02.md
├── handoffs/
│   └── <act-NN-slug>/                   [writable by: that Act's actors]
└── acts/
    └── <act-NN-slug>/
        ├── <act-NN-slug>.md             [static]
        ├── lead-<slug>.md               [static]
        ├── cast-<slug>.md               [static] (zero or more)
        ├── props/                       [static]
        └── stage/                       [writable by: that Act's actors]
```

## Two phases: setup and execution

The folder exists in two distinct phases.

**Setup** happens before execution. The Director (or a helper agent) prepares the Play folder: creates the directory structure, writes all definition files (`play.md`, management files, Act files, role files), populates `reference/` and `props/` with input data, and initializes empty `handoffs/`, `verifications/`, and `stage/` folders. Setup is complete when every definition file is in place and all input data is available.

**Execution** begins when the Stage Manager starts the first Act. From this point, all definition files are locked — `play.md`, `management/`, Act files, role files, `reference/`, and `props/` cannot be modified. Only the Director can change locked files during execution, and any such change is a deliberate override recorded in `progress.md`.

## Root-level files

Two files live at the Play root:

- **`play.md`** — the Play definition. Contains the goal, Act sequence, checklists, and Gates. Static during execution.
- **`progress.md`** — the execution record. Contains status table, timestamps, verification results, recovery decisions, and exceptions. The only file the Stage Manager writes.

## Top-level folders

### `management/`

Three definition files for the Play's management agents and shared rules:

- `stage-manager.md` — Stage Manager role definition and behavioral constraints.
- `checklist-agent.md` — Checklist Agent role definition, golden rules, and report instructions.
- `play-rules.md` — shared rules, folder/access map, and runtime defaults. Every agent reads this before work.

All three are static during execution.

### `reference/`

Shared input data that multiple Acts read. Populated during setup, static during execution. Examples: API source files, requirements documents, security criteria. Every Act actor can read `reference/`.

### `verifications/`

Verification reports organized by Act. Each Act gets a subfolder matching its name (`verifications/act-01-review-quality/`). The Checklist Agent writes one report per verification execution, named `<act-folder>-attempt-NN.md` starting at 01. Earlier reports are preserved — the Checklist Agent never edits or deletes a previous report.

Only the Checklist Agent writes to `verifications/`. All other agents have read-only access.

### `handoffs/`

Shared outputs organized by Act. Each Act gets a subfolder matching its name (`handoffs/act-01-review-quality/`). When an Act completes its work, its actors publish final outputs here. Downstream Acts read these as inputs.

All Act actors (Lead and Cast) may write to their own Act's handoff folder. All agents in the Play may read all handoff folders.

### `acts/`

Act definitions and working space, organized by Act. Each Act gets a subfolder containing:

- The **Act file** (`act-NN-slug.md`) — goal, inputs, outputs, flow, workspace, rules.
- **Role files** — one Lead file (required) and zero or more Cast files.
- **`props/`** — Act-specific static input data (distinct from shared `reference/`).
- **`stage/`** — mutable working directory for intermediate files during execution.

Act files, role files, and `props/` are static during execution. Only `stage/` is writable.

## Naming conventions

- **Act folders and files:** `act-NN-slug` where NN is a two-digit number starting at 01 and slug is 1-3 descriptive words. Example: `act-01-review-quality`.
- **Lead files:** `lead-slug.md` — one per Act. Example: `lead-review-coordinator.md`.
- **Cast files:** `cast-slug.md` — zero or more per Act. Example: `cast-security-reviewer.md`.
- **Verification reports:** `<act-folder>-attempt-NN.md` — numbering counts verification executions, not Lead retries.

---

For access control details — who reads what, who writes where — see [permissions.md](permissions.md). For the distinction between `reference/`, `props/`, `stage/`, and `handoffs/` — see [locations.md](locations.md).
