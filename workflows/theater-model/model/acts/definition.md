# What Is an Act

An Act is a focused stage of work within a Play. Each Act has a single goal, defined inputs and outputs, and one or more assigned agents. Acts execute strictly in order — one at a time, always forward, never backward.

An Act definition lives in its own folder under `acts/`. The folder contains the Act file, role files, props, and the mutable workspace.

## One-Act-one-goal principle

Each Act achieves exactly one goal. If a stage has two separable goals, it should be two Acts. If two stages need each other's output, they are one Act with internal coordination.

This keeps checklists specific and failures easy to diagnose. A single Act with a vague goal produces a vague checklist.

## Parts of an Act

An Act folder contains:

### Act file

`act-NN-slug.md` — the Act definition. Describes the goal, workspace, inputs, outputs, internal flow, rules, and runtime defaults.

The Act file is static and locked during execution. Only the Director can change it.

### Role files

- **Lead file** (`lead-slug.md`) — exactly one per Act. The primary agent that coordinates work and produces outputs.
- **Cast files** (`cast-slug.md`) — zero or more per Act. Supporting agents the Lead delegates focused subtasks to.

Role files are also static and locked during execution.

### Props

`props/` — static supporting files for this Act. Read-only during execution. Props are Act-specific input data that doesn't belong in shared `reference/`.

### Stage

`stage/` — the mutable workspace. All intermediate files, actor-to-actor communication, and work-in-progress live here. Only this Act's agents can write to it.

## Naming

Act folders and files use the pattern `act-NN-slug`:

- **NN** — two-digit order number starting at 01
- **slug** — 1-3 hyphen-separated descriptive words describing what the Act *does*

The file name matches the folder name: `acts/act-01-review-api/act-01-review-api.md`.

Good: `act-01-run-tests`, `act-02-apply-fixes`, `act-03-review-quality`
Bad: `act-01-testing` (too vague), `act-1-review` (missing leading zero)

## How an Act executes

The Stage Manager starts each Act by assigning the Lead with a short prompt. The Lead starts with fresh context — not forked from the Stage Manager. It loads shared rules, the Act file, its Lead file, and the Stage Manager's assignment prompt, then either does the work alone or delegates to Cast.

When the Act's work is complete, the Act's outputs land in `handoffs/act-NN-slug/`. Any of the Act's agents (Lead or Cast) may write there, subject to their role-level access rules. The Checklist Agent (an independent verification agent — see [agents/](../agents/)) then verifies the outputs against the Act's bound checklist.

A Lead can also report failure directly to the Stage Manager without waiting for checklist verification, explaining the failure, evidence, and what is missing.

If verification fails, the Stage Manager may retry the Act (up to 2 corrective retries, giving 3 total attempts). On retry, the same Lead instance continues with its retained context — it is not a fresh start. If retries are exhausted, execution stops for Director intervention.

Acts never go backward. If a downstream Act discovers that an earlier Act produced wrong output, execution stops for the Director.

## What an Act file contains vs what lives elsewhere

| Content | Where it belongs |
|---------|-----------------|
| Goal, inputs, outputs, flow, rules, runtime defaults | Act file (`act-NN-slug.md`) |
| Agent responsibilities, access, coordination | Role files (`lead-slug.md`, `cast-slug.md`) |
| Verification criteria | `play.md` (inline checklist after the Act section) |
| Verification results | `verifications/act-NN-slug/` |
| Gate definitions | `play.md` (between Acts) |
| Progress and status | `progress.md` |
| Execution procedures, retry logic | `management/stage-manager.md` |

For the complete file format specification — sections, fields, heading syntax, and a copy-paste template — see [schemas/act-file.md](../schemas/act-file.md).
