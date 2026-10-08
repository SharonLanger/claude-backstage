# Schema: Act Definition File

Reference card and template for `act-NN-slug.md` files.

## File naming

- Pattern: `act-NN-slug.md` where NN is a two-digit order starting at 01.
- Slug: 1-3 hyphen-separated descriptive words.
- File name matches folder name: `acts/act-01-review-api/act-01-review-api.md`.

## Required sections

| Section | Req? | Type | Description |
|---|---|---|---|
| `# Act NN -- <Title>` | Required | HARD | H1 heading. NN matches the file's two-digit order number. |
| `## Goal` | Required | CONFIGURABLE | One or two sentences: what this Act achieves. |
| `## Workspace` | Required | HARD (path) | Points to `acts/<act-folder>/stage/`. One-line description of how actors use it. |
| `## Inputs` | Required | CONFIGURABLE | Bulleted list of file paths the Act reads. Paths are relative to the Play root. |
| `## Outputs` | Required | CONFIGURABLE | Bulleted list of file paths the Act produces. Must land in `handoffs/<act-folder>/`. |
| `## Flow` | Required | CONFIGURABLE | Numbered steps describing internal coordination: who does what, in what order, and where intermediate files land in `stage/`. |
| `## Rules` | Required | HARD | Mandatory constraints for this Act. Not overridable by actors or runtime settings. Use "No Act-specific rules beyond the shared Play rules." when empty. |
| `## Runtime defaults` | Required | CONFIGURABLE | Inheritable settings (model, reasoning effort, etc.). Use "Inherit from `play-rules.md`." when no Act-level overrides exist. More-specific role files may override these. |

**HARD** -- structure and constraints baked into the model; not Play-specific.
**CONFIGURABLE** -- filled in per Play; content varies.

## HARD rules

1. The Act file is **static and locked** during execution, including retries. Only the Director may change it.
2. `## Workspace` must point to `acts/<act-folder>/stage/`. No other writable location.
3. `## Inputs` reference paths within the Play folder (reference/, handoffs/, props/, or other readable locations).
4. `## Outputs` reference paths under `handoffs/<act-folder>/` only.
5. `## Rules` contains mandatory constraints that actors cannot weaken or override.
6. `## Runtime defaults` is separate from `## Rules`. Defaults are inheritable and overridable by role files; rules are not.
7. The Act file does not contain actor definitions, checklist items, Gate definitions, or progress tracking. Those live elsewhere (role files, play.md, progress.md).

## Precedence

Runtime settings resolve as: Play defaults -> Act defaults -> Role overrides.
Permissions, Gates, and locked-file restrictions cannot be overridden at any level.

## Template

```markdown
# Act {{NN}} -- {{Title}}

## Goal

{{One or two sentences describing what this Act achieves.}}

## Workspace

`acts/act-{{NN}}-{{slug}}/stage/`

{{One sentence describing how actors use the workspace.}}

## Inputs

- `{{path/to/input-1}}` -- {{short description}}.
- `{{path/to/input-2}}` -- {{short description}}.
- `acts/act-{{NN}}-{{slug}}/props/{{file}}` -- {{short description}}.

## Outputs

- `handoffs/act-{{NN}}-{{slug}}/{{output-file-or-dir}}` -- {{short description}}.
- `handoffs/act-{{NN}}-{{slug}}/{{output-file-or-dir}}` -- {{short description}}.

## Flow

1. {{Lead does X.}}
2. {{Cast-A writes `stage/intermediate-a.md`; Cast-B writes `stage/intermediate-b.md`.}}
3. {{Lead consolidates and produces final outputs in `handoffs/`.}}

## Rules

{{Act-specific mandatory constraints, or:}}
No Act-specific rules beyond the shared Play rules.

## Runtime defaults

{{Act-level settings such as model or reasoning effort, or:}}
Inherit from `play-rules.md`.
```

## Constraints -- what must NOT appear

- Actor definitions (Lead/Cast files are separate: `lead-slug.md`, `cast-slug.md`).
- Checklist items (belong in `play.md` under the Act's checklist section).
- Gate definitions (belong in `play.md` as separate flow elements).
- Progress tracking or status (belongs in `progress.md`).
- Generic execution procedures (belong in `play-rules.md` or `stage-manager.md`).
- Runtime override syntax (belongs in role files under `## Runtime overrides`).
- Absolute file paths. All paths are relative to the Play root.
