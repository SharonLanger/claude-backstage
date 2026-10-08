# Play: {{play-title}}

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
<!-- Purpose: {{short Act goal}} (optional — use if the prose is long) -->
<!-- Workspace: acts/{{act-01-folder-name}}/stage/ (optional — include if Cast uses stage/) -->

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
<!-- Purpose: {{short Act goal}} (optional) -->
<!-- Workspace: acts/{{act-02-folder-name}}/stage/ (optional) -->

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
