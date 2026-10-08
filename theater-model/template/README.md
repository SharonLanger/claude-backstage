# Play Template

Copy this folder, rename it for your Play, and fill in the placeholders.

## How to use

1. Copy the entire `template/` folder. Rename the copy to your Play name (e.g., `my-code-review-play/`).
2. Start with `play.md` — define your goal, Acts, checklists, and Gates.
3. Fill in `progress.md` — update the Act rows to match your Play's Acts and Gates.
4. Review `management/play-rules.md` — the Rules section has substantive defaults. Add Play-specific runtime defaults.
5. Review `management/stage-manager.md` — update the Gate names in Responsibilities to match your Play's Gates.
6. Leave `management/checklist-agent.md` as-is — it has no Play-specific content.
7. For each Act, copy the `acts/act-01-SLUG/` folder. Rename the folder and files to match your Act (e.g., `acts/act-01-review-api/`).
8. Fill in Act definitions, Lead files, and Cast files (if any). Update the `@` references in Lead/Cast files to point to the actual Act file name.
9. Add shared input files to `reference/`. Add Act-specific input files to each Act's `props/`.
10. Hand off to the Stage Manager to begin execution.

## What each file is

| File | Purpose |
|------|---------|
| `play.md` | Play definition — goal, Acts, checklists, Gates |
| `progress.md` | Execution tracking — Stage Manager writes this |
| `management/play-rules.md` | Shared rules, folder/access map, runtime defaults |
| `management/stage-manager.md` | Stage Manager role definition |
| `management/checklist-agent.md` | Checklist Agent role definition + golden rules |
| `acts/act-01-SLUG/act-01-SLUG.md` | Act definition — goal, inputs, outputs, flow |
| `acts/act-01-SLUG/lead-SLUG.md` | Lead role — responsibilities, access, Cast coordination |
| `acts/act-01-SLUG/cast-SLUG.md` | Cast role (optional) — focused task, access |
| `verification-report.md` | Report format reference — used by Checklist Agent at runtime |

## Empty directories

| Directory | Purpose |
|-----------|---------|
| `reference/` | Shared input files read by multiple Acts |
| `verifications/` | Checklist Agent writes verification reports here |
| `handoffs/` | Act agents write shared outputs here |
| `acts/act-01-SLUG/props/` | Act-specific input files |
| `acts/act-01-SLUG/stage/` | Mutable workspace for Act agents |

## Key rules

- **play.md**, **management/**, Act definitions, and role files are **locked during execution**. Only the Director can change them.
- **progress.md** is written only by the Stage Manager.
- **verification reports** are written only by the Checklist Agent.
- **stage/** and **handoffs/** are written by the Act's actors (Lead and Cast).
- All `@` references in role files use paths relative to the file's location.
