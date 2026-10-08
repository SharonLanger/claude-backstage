# Schema: Lead File

Defines the primary agent in an Act. Exactly one per Act. Located at `acts/act-NN-slug/lead-slug.md`.

## File naming

`lead-<slug>.md` where slug is 1-3 hyphen-separated descriptive words.

Bare `lead.md` does not satisfy naming conventions. The slug describes what this Lead does, not the Act it belongs to.

## Required @ references

Every Lead file must begin with exactly these two lines, before any heading:

```
@../../management/play-rules.md
@./act-NN-slug.md
```

Use the actual Act filename. From `acts/act-NN-slug/`, `../../` reaches the Play root, then into `management/`. These are the Lead's context-loading directives.

HARD: Both references are mandatory. No other content may precede them.

## Sections

| Section | Required | HARD / CONFIGURABLE | Purpose |
|---|---|---|---|
| `# Lead: <Name>` | Yes | HARD (heading format) | Identifies the role. Name is CONFIGURABLE. |
| `## Responsibilities` | Yes | CONFIGURABLE (content) | What this Lead does, what it produces, coordination summary. |
| `## Access` | Yes | CONFIGURABLE (content) | Explicit read/write paths. Reads and Writes listed separately. |
| `## Cast coordination` | Yes | CONFIGURABLE (content) | How Cast are assigned, or "No Cast in this Act. Lead works alone." |
| `## Runtime overrides` | Yes | CONFIGURABLE (content) | Per-role settings overriding Act/Play defaults, or "None. Inherits Act defaults." |

HARD: All four sections must be present. Section headings are fixed. Content within each section is authored per-Act.

## Template

```markdown
@../../management/play-rules.md
@./act-NN-slug.md

# Lead: <Name>

## Responsibilities

<What this Lead does. What outputs it produces. If it coordinates Cast, summarize the coordination strategy. 2-5 sentences.>

## Access

- Reads: <comma-separated paths — reference/, handoffs from prior Acts, this Act's props/, other files needed>
- Writes: <this Act's stage/ and handoff folder>

## Cast coordination

<One of:>
<Option A — no Cast:>
No Cast in this Act. Lead works alone.

<Option B — with Cast:>
- Assign <Cast name> the <dimension/task> (fresh context).
- <Repeat for each Cast member.>
- Consolidate Cast outputs from `stage/` and `handoffs/<act>/` into final handoff summary.

## Runtime overrides

None. Inherits Act defaults.
<Or: specific overrides, e.g., model, reasoning effort.>
```

## Constraints

**Static and locked.** The Lead file is a definition. It does not change during execution, including retries. Only the Director may modify it (via Director authority).

**Exactly one per Act.** An Act folder contains one `lead-*.md` file and zero or more `cast-*.md` files.

**Fresh context.** The Lead starts with fresh context — not forked from the Stage Manager. Its context is loaded from: play-rules.md, the Act file, this Lead file, and the Stage Manager's short assignment prompt.

**Corrective retries resume the same instance.** When the Stage Manager sends corrections, the same Lead instance continues with its retained context. This is not a fresh launch.

**Only Leads call Cast.** Cast never call other Cast. The Stage Manager does not call Cast directly.

**Access boundaries.** Writes are limited to this Act's `stage/` and `handoffs/<act>/`. Reads must be listed explicitly — they may include `reference/`, prior Acts' handoffs, and this Act's `props/`.

**Runtime override precedence.** Play defaults < Act defaults < Role overrides. Overrides cannot weaken mandatory rules, expand permissions, or bypass Gates.
