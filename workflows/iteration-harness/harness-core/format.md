# Format Rules

All files in this project must follow these formatting conventions (derived from the docs folder).

---

## Headings

- `#` for the document title (one per file)
- `##` for major sections
- `###` for subsections
- One blank line before and after headings

## Lists

- Use `-` (hyphen) for unordered lists
- Three spaces indent for list items: `-   item` (pandoc style)
- Continuation lines aligned with the text above them
- Use numbered lists (`1.`, `2.`) only for ordered sequences

## Code blocks

- Always fenced with triple backticks
- Always include a language tag: `text`, `md`, `yaml`
- Use `text` for diagrams, flows, and filesystem trees
- Use `md` for markdown examples
- Use `yaml` for configuration examples

## Emphasis

- `**bold**` for key terms, rules, and names on first mention
- `` `backticks` `` for file names, paths, commands, and identifiers
- `---` (triple dash) as separator between logical sections (not em-dashes in prose)
- Use `---` (three hyphens) in prose as em-dash between words (e.g. "Otor --- top-level orchestrator")

## Prose

- Short sentences. One idea per sentence.
- No filler words.
- Present tense.
- Active voice.
- Paragraphs separated by one blank line.

## File structure

```text
# Title

Opening statement (1–2 sentences explaining what this file is).

## Section

Content.

## Section

Content.
```

## Diagrams / flows

Use arrow notation inside ```` ``` text ```` blocks:

```text
A
  ↓
B
  ↓
C
```

Use `→` for inline file references (e.g. `p1/output/a.md → p2/input/a.md`).

## Tables

- Use markdown pipe tables
- Align header separator with content width
- Keep tables compact

## File naming

- Lowercase kebab-case: `phase-types.md`, `planner-output.md`
- Folders: lowercase, hyphen-separated when multi-word

---

## Parameters

When documenting function parameters, arguments, or configuration options use a one-liner per param with a dash separator:

```text
- name — short description
- type — mono | gate | group
- model — which model to use (default: claude-sonnet)
- effort — low | medium | high
```

When a parameter needs more detail, indent below it:

```text
- custom — phase-specific open-ended properties
    passed to the phase type for interpretation
    not validated by the core runner
```

## Property definitions

One line per property. Keep it human-readable --- scannable at a glance.

Format: `property` followed by `---` followed by what it is.

```text
id --- unique phase identifier (e.g. P4)
name --- human-readable phase name
type --- mono | gate | group
definition --- optional reference to a phase definition file
goal --- short statement of what the phase must accomplish
model --- model used for execution
effort --- requested execution effort (low | medium | high)
custom --- open-ended phase-specific configuration
input --- logical files required by the phase
output --- files the phase is expected to produce
before --- preparation operations run before the phase
validation --- success checklist the phase must pass
after --- post-phase workflow operations
```

## Type hierarchies / inheritance

Use tree notation with box-drawing characters:

```text
IPhaseType
├── Mono
├── Gate
└── Group
```

Nested:

```text
Runner
├── Otor
│   └── runs agents only
├── Main Planner
│   ├── reads blueprint
│   ├── creates workspace
│   └── manages transitions
└── Phase Agent
    └── performs phase work
```

## Folder structures

Always use tree notation inside ```` ``` text ```` blocks.

Rules:
- `├──` for items with siblings below
- `└──` for last item in a group
- `│` for continuation lines
- Indent 4 spaces per nesting level
- Add `←` annotations for explanations

```text
workspace/
├── blueprint.md          ← source of truth
├── planner.md            ← execution map
├── format.md             ← formatting rules
├── shorts.md             ← abbreviations
├── skill/                ← the mock skill
├── implementation/
│   ├── README.md         ← milestones & steps
│   ├── m1-mono-phase-skill/
│   │   ├── README.md
│   │   └── test.md
│   └── m2-phase-type-logs/
└── example-skill-docs/       ← READ-ONLY reference docs for your skill
```
