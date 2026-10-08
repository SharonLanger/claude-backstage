# Schema: play-rules.md

## File name

`management/play-rules.md` -- one per Play, inside the `management/` folder. Static and locked during execution.

## Purpose

Short shared rules file that every agent reads before work. Contains mandatory constraints, a folder/access map, and runtime defaults. Does NOT contain detailed procedures (those belong in `stage-manager.md` and `checklist-agent.md`).

## Required sections

| Section | Required | HARD / CONFIGURABLE | Content |
|---------|----------|---------------------|---------|
| `# Play Rules` | Required | Title wording is CONFIGURABLE | Top-level heading. May include the Play title. |
| `## Rules` | Required | HARD | Mandatory constraints. Cannot be overridden by runtime settings or agent instructions. |
| `## Folder map` | Required | Structure is HARD; Act names are CONFIGURABLE | Canonical folder tree with read/write access annotations. |
| `## Runtime defaults` | Required | CONFIGURABLE | Play-level defaults for model, effort, and other runtime settings. |

**HARD structural rules:**
- `play-rules.md` is static and locked during execution, including retries.
- Every agent in the Play reads this file before work.
- The `## Rules` section cannot be overridden by runtime settings, Act defaults, role overrides, or ordinary agent task instructions.
- Permissions, Gates, and locked-file restrictions cannot be weakened by more-specific definitions.
- More-specific instructions (Act or role) may add detail or stricter limits but never expand permission.

## Rules section

The `## Rules` section contains mandatory constraints as a bullet list. All items are HARD -- not overridable.

| Rule | Required | Content |
|------|----------|---------|
| Authority | Required | Director > model rules > agent instructions. Explicit Director override applies only within its stated scope. |
| Delegation | Required | Stage Manager calls Leads; Leads call Cast. Cast do not call other Cast. Stage Manager calls Checklist Agent (exception to Lead-only delegation). |
| Locked locations | Required | List all static locations: `play.md`, `management/`, Act definitions, role files, `reference/`, `props/`. All locked during execution, including retries. |
| Write permissions | Required | Who may write where. Act actors write own `stage/` and `handoffs/<act>/`. Stage Manager writes `progress.md` only. Checklist Agent writes own new report in `verifications/<act>/`. |
| Read permissions | Required | Who may read what. All actors read all `handoffs/` and `verifications/`. Act actors read `reference/`, own `props/`, own `stage/`. Stage Manager reads Play, progress, all handoffs, all verifications. |
| Gates | Required | Mandatory hard stop. Present evidence, wait for Director. Record decision. Skip = Skipped (not Done). |
| Recovery | Required | Retry limits and forward-only direction. Ask Director when unclear or exhausted. |
| Truthfulness | Required | No invented evidence, false passes, or hidden failures. Pause and report conflicts. |

**What stays OUT of the Rules section:**
- Detailed retry procedures and recovery logic (belong in `stage-manager.md`).
- Verification procedures and golden rules (belong in `checklist-agent.md`).
- Act-specific stage layout and navigation (belong in Act files).
- Actor-specific instructions (belong in role files).
- Exception authority details (belong in `stage-manager.md`).

## Folder map section

A tree or table showing every folder in the Play with access annotations. Structure is HARD; specific Act folder names are CONFIGURABLE per Play.

Each entry must show: folder/file path, whether it is static or writable, and which agents have read and write access.

The folder map is the canonical reference for access control. Role files and Act files may add specificity (which files within `stage/` an actor produces) but cannot contradict the map.

## Runtime defaults section

Play-level default settings. CONFIGURABLE -- each Play sets its own values.

Required elements:
- Settings values (model, effort, and other approved runtime settings).
- Inheritance note: "More-specific definitions may override these. Omitted settings are inherited."

Precedence: Play defaults (here) < Act defaults < Role overrides.

Runtime defaults cannot override Rules. Permissions, Gates, and locked-file restrictions are not runtime settings.

## Template

```markdown
# Play Rules — {{play-title}}

## Rules

- **Authority:** Director > model rules > agent instructions. An explicit Director override applies only within its stated scope.
- **Delegation:** Stage Manager calls Leads; Leads call Cast. Cast do not call other Cast. Stage Manager calls Checklist Agent (exception to Lead-only delegation).
- **Locked locations:** `play.md`, `management/`, Act definitions, role files, `reference/`, `props/` — all static during execution, including retries.
- **Write permissions:** Act actors write own `stage/` and `handoffs/<act>/`. Stage Manager writes `progress.md` only. Checklist Agent writes own new report in `verifications/<act>/`.
- **Read permissions:** All actors read all `handoffs/` and `verifications/`. Act actors read `reference/`, own `props/`, own `stage/`. Stage Manager reads Play, progress, all handoffs, all verifications.
- **Gates:** Mandatory hard stop. Present evidence, wait for Director. Record decision. Skip = Skipped (not Done).
- **Recovery:** Two retries per Act per Run. Resume same Lead. Forward-only. Ask Director when unclear or exhausted.
- **Truthfulness:** Mandatory for all agents. No invented evidence, false passes, or hidden failures. Pause and report conflicts.

## Folder map

```
play/
├── play.md                          [static]
├── progress.md                      [writable by: Stage Manager]
├── management/                      [static]
├── reference/                       [static, read: all]
├── verifications/<act>/             [writable by: Checklist Agent (new reports only)]
├── handoffs/<act>/                  [writable by: that Act's actors]
└── acts/<act>/
    ├── act-NN-slug.md               [static]
    ├── lead-slug.md                 [static]
    ├── cast-slug.md                 [static]
    ├── props/                       [static]
    └── stage/                       [writable by: that Act's actors]
```

## Runtime defaults

- model: {{model-choice or "(unspecified — implementation choice)"}}
- effort: {{effort-level or "(unspecified — implementation choice)"}}

More-specific definitions may override these. Omitted settings are inherited.
```

## Constraints -- what must NOT appear in play-rules.md

- **No detailed procedures.** Retry logic, recovery sequences, verification steps, progress table format, and exception criteria belong in `stage-manager.md` or `checklist-agent.md`.
- **No Act-specific content.** Stage layout, actor coordination, and workspace instructions belong in Act files.
- **No role-specific instructions.** Actor responsibilities, tool usage, and Cast assignments belong in role files.
- **No Play-specific flow.** The Act sequence, checklists, and Gates belong in `play.md`.
- **No runtime progress.** Statuses, timestamps, and decisions belong in `progress.md`.
- **No checklist authoring guidance.** That is a design-time concern, not a runtime file.

## Size target

~30-40 lines of content. Every line costs tokens across all agents in the Play (Stage Manager, every Lead, every Cast, every Checklist Agent invocation). Brevity is a structural requirement, not a style preference.
