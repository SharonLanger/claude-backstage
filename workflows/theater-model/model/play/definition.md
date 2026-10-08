# What Is a Play

A Play is a complete workflow definition. It describes a goal, breaks it into sequential Acts, assigns agents to each Act, specifies verification criteria, and defines where the Director must intervene.

The Play definition lives in `play.md` at the root of the Play folder. It is the single document that captures the entire workflow structure.

## Play vs Run

A **Play** is the static definition — what should happen. A **Run** is one execution of that Play.

Each Run uses a fresh Play folder with the full folder structure, definition files, and input data. Setup is a separate step before execution — the Director (or a helper agent) prepares the folder with definitions, references, and props. Only after setup is complete does the Stage Manager begin running the Play.

The Play definition does not change during execution — it is locked once the Run begins. A resumed Run uses its existing folder and progress; it does not create a new copy.

## What a Play contains

A Play defines five things:

### 1. Goal

What the Play achieves. One to three sentences.

### 2. Acts

The sequential stages of work. Each Act has a clear goal, defined inputs and outputs, and one or more assigned agents. Acts execute one at a time, in strict forward order — there are no parallel Acts, and execution never goes backward. If a downstream Act discovers that an earlier Act produced wrong output, execution stops for Director intervention.

Each Act section in `play.md` includes the Act's name, Lead assignment, purpose, inputs, and outputs.

### 3. Checklists

Every Act has a bound Checklist — a list of verification criteria that the Checklist Agent checks after the Act completes. Checklists are defined inline in `play.md`, immediately after their Act section.

Checklist items are verification criteria, not checkboxes. The Checklist Agent produces verdicts in separate report files — see `management/checklist-agent.md` for how verification works.

### 4. Gates

A Gate is a mandatory hard stop between Acts where the Director must review evidence and make a decision. Gates are optional — not every Act pair needs one. They are defined inline in `play.md` between the checklist of one Act and the next Act.

Only explicit Director approval opens a Gate. No agent, no checklist result, and no prior approval can bypass it.

The Director is the human. The Director has full authority over the Play — they can modify checklists, change Act definitions, and override any rule. All other participants are agents.

### 5. Shared references

Static files in `reference/` that multiple Acts read. Listed at the top of `play.md` so every reader knows what shared context exists.

## How these connect

The structural pattern in `play.md` is:

```
Act 1 → Checklist 1 → [Gate] → Act 2 → Checklist 2 → [Gate] → Act 3 → Checklist 3
```

Gates are placed where the Director needs to make a decision before work continues. The simplest Play has Acts and Checklists with no Gates at all.

Each Act has a bounded number of retries (details in `management/stage-manager.md`). If retries are exhausted, execution stops for Director intervention.

## Play completion

A Play is complete when all required Acts are Done, every verification has a passing result (or has a qualifying documented Stage Manager exception), and every required Gate has explicit Director approval. If the Director has not run certain Acts, those must be accounted for in the Director's decision — a Play does not silently finish with unresolved work.

## What a Play does NOT contain

Play definitions are deliberately limited. These things live elsewhere:

| Content | Where it belongs |
|---------|-----------------|
| Execution procedures (retry logic, recovery) | `management/stage-manager.md` |
| Verification procedures | `management/checklist-agent.md` |
| General rules (access, authority, delegation) | `management/play-rules.md` |
| Runtime progress (statuses, timestamps, decisions) | `progress.md` |
| Runtime settings (model, effort) | `management/play-rules.md`, Act files, or role files |

This separation keeps `play.md` focused on *what* the workflow does, not *how* the machinery runs it.

## Relationship to other files

The Play definition references but does not duplicate:

- **Act files** (`acts/act-NN-slug/act-NN-slug.md`) — detailed Act definitions with internal flow, rules, and workspace layout.
- **Role files** (`acts/act-NN-slug/lead-slug.md`, `cast-slug.md`) — agent-specific responsibilities and instructions.
- **Management files** — shared rules and agent procedures that `play.md` does not repeat.

For the complete file format specification — sections, fields, heading syntax, and a copy-paste template — see [schemas/play-md.md](../schemas/play-md.md).
