# Schema: play.md

## File name

`play.md` — one per Play folder, at the root.

## Required sections

| Section | Required | HARD / CONFIGURABLE | Content |
|---------|----------|---------------------|---------|
| `# Play: <title>` | Required | Title is CONFIGURABLE | Top-level heading. Short descriptive title. |
| `## Goal` | Required | Body is CONFIGURABLE | What this Play achieves. 1-3 sentences. |
| `## Shared references` | Required | Body is CONFIGURABLE | Bullet list of `reference/` paths and descriptions used across Acts. |
| `## Acts and Actors` | Required | Body is CONFIGURABLE | Summary table of all Acts with Lead and Cast. Actor file paths listed below the table. |
| `## act` (per act) | Required | Heading is HARD; body is CONFIGURABLE | One section per Act in sequence order. See Act fields below. |
| `## checklist` (per act) | Required | Heading is HARD; body is CONFIGURABLE | One section per Act, immediately after its `## act`. See Checklist schema below. |
| `## gate` | Optional | Heading is HARD; body is CONFIGURABLE | Placed between Acts where a Director decision is needed. See Gate schema below. |
| Companion-definition notes | Optional | CONFIGURABLE | Package-specific notes about role files, context loading, conventions. |
| V3 execution context | Optional | CONFIGURABLE | Execution-context rules relevant to this Play. |
| Director interaction | Optional | CONFIGURABLE | Play-specific Director interaction rules. |

**HARD structural rules:**
- `play.md` is static and locked during execution.
- Section order follows the Act sequence: `## act` / `## checklist` / `## gate` / `## act` / `## checklist` / ...
- `## act`, `## gate`, and `## checklist` headings are exactly lowercase — no capitalization variants.

## Act section fields

Each `## act` section contains:

| Field | Required | Description |
|-------|----------|-------------|
| `Name:` | Required | Act folder name: `act-<NN>-<slug>` |
| `Lead:` | Required | Relative path to lead file: `acts/<act-folder>/lead-<slug>.md` |
| Workspace | Optional | `acts/<act-folder>/stage/` — where actors do mutable work |
| Purpose | Optional | Short description of the Act's goal |
| Prose | Required | What this Act does. Can mention Cast coordination and stage usage. |
| `Inputs:` | Required | Bullet list of files/folders this Act reads. |
| `Outputs:` | Required | Bullet list of files this Act produces in `handoffs/<act-folder>/`. |

## Gate schema

Gates live inline in `play.md`, placed between the checklist of one Act and the `## act` of the next.

```
## gate

Name: gate-<slug>

<presentation-instructions>

<decision-hints>

Decision needed: <what the Director must decide>
```

| Field | Required | HARD / CONFIGURABLE | Description |
|-------|----------|---------------------|-------------|
| `## gate` | Required | HARD | Exact heading, lowercase. |
| `Name:` | Required | Slug is CONFIGURABLE | Format: `gate-<slug>`. Slug uses hyphen-separated words; agents use max 3 words, Play authors may use more when clarity requires it. |
| Presentation instructions | Required | CONFIGURABLE | What to show the Director: evidence, summaries, risks, open questions. |
| Decision hints | Optional | CONFIGURABLE | What the Director should inspect or consider. |
| `Decision needed:` | Required | CONFIGURABLE | The specific decision the Director must make. |

**HARD gate rules:**
- A Gate is a mandatory hard stop. Only explicit Director approval opens it.
- Checklist success, retries, or earlier approvals cannot bypass a Gate.
- On resume, a Gate without recorded explicit approval remains closed.

## Checklist schema

Checklists live inline in `play.md`, placed immediately after their bound Act's `## act` section.

```
## checklist

For: <act-name>

- <check item 1>
- <check item 2>
- ...
```

| Field | Required | HARD / CONFIGURABLE | Description |
|-------|----------|---------------------|-------------|
| `## checklist` | Required | HARD | Exact heading, lowercase. |
| `For:` | Required | CONFIGURABLE | Binds to an act name, e.g. `act-01-review-quality`. |
| Check items | Required | CONFIGURABLE | Bullet list of verification criteria. No checkboxes — these are criteria, not a runtime form. |

**HARD checklist rules:**
- Only the Checklist Agent performs verification against these items.
- The Director may change a checklist; agents cannot silently weaken them.
- Each verification runs the entire checklist, not a subset.
- Generic verification procedures belong in `management/checklist-agent.md`, not here.

## Template

```markdown
# Play: {{title}}

> {{optional-note-about-this-play}}

## Goal

{{1-3 sentences describing what this Play achieves}}

## Shared references

- `reference/{{path}}/` -- {{description}}.
- `reference/{{file}}.md` -- {{description}}.

## Acts and Actors

| Act | Lead | Cast |
|---|---|---|
| {{act-01-slug}} | {{Lead Name}} | {{Cast Name 1}}; {{Cast Name 2}} |
| {{act-02-slug}} | {{Lead Name}} | None |
| {{act-03-slug}} | {{Lead Name}} | {{Cast Name}} |

Actor files inside each Act folder:
- {{act-01-slug}}: `lead-{{slug}}.md`, `cast-{{slug}}.md`, `cast-{{slug}}.md`.
- {{act-02-slug}}: `lead-{{slug}}.md`.
- {{act-03-slug}}: `lead-{{slug}}.md`, `cast-{{slug}}.md`.

Each Act has its matching static Act file, static role files, read-only `props/`, and mutable `stage/`. Shared outputs use `handoffs/<act-folder>/`; verification attempts use `verifications/<act-folder>/<act-folder>-attempt-NN.md`.

## act

Name: `{{act-01-folder-name}}`
Lead: `acts/{{act-01-folder-name}}/lead-{{slug}}.md`

{{What this Act does. Mention Cast coordination and stage/ usage if applicable.}}

Inputs:
- {{reference or prop paths}}
- {{earlier handoff paths if not Act 01}}

Outputs:
- `handoffs/{{act-01-folder-name}}/{{output-file}}.md` -- {{description}}.

## checklist

For: `{{act-01-folder-name}}`

- {{Verification criterion 1}}.
- {{Verification criterion 2}}.

## gate

Name: `gate-{{slug}}`

{{What to present to the Director: evidence, summaries, risks, open questions.}}

{{What the Director should inspect or decide.}}

Decision needed: {{the specific decision required}}.

## act

Name: `{{act-02-folder-name}}`
Lead: `acts/{{act-02-folder-name}}/lead-{{slug}}.md`

{{What this Act does.}}

Inputs:
- {{paths including approved scope from progress.md}}

Outputs:
- `handoffs/{{act-02-folder-name}}/{{output}}/` -- {{description}}.
- `handoffs/{{act-02-folder-name}}/{{output-file}}.md` -- {{description}}.

## checklist

For: `{{act-02-folder-name}}`

- {{Verification criterion 1}}.
- {{Verification criterion 2}}.

{{Repeat ## act / ## checklist / ## gate pattern for remaining Acts.}}
```

## Constraints — what must NOT appear in play.md

- **No execution procedures.** Generic retry logic, recovery steps, verification procedures, and Stage Manager coordination belong in `management/` files.
- **No runtime progress.** Act statuses, timestamps, Director decisions, and checklist verdicts go in `progress.md`.
- **No general rules.** Rules that apply to all Plays belong in `management/play-rules.md`.
- **No checkboxes in checklists.** These are verification criteria, not a runtime form. The Checklist Agent produces verdicts in separate report files.
- **No runtime settings.** Model, effort, and other runtime defaults go in `management/play-rules.md`, Act files, or role files — not in `play.md`.
