# Schema: Cast File

Defines a supporting agent within an Act. Zero or more Cast per Act. Located at `acts/act-NN-slug/cast-slug.md`.

---

## File naming

`cast-<slug>.md` where slug is 1-3 descriptive hyphen-separated words.

Valid: `cast-security-reviewer.md`, `cast-test-runner.md`, `cast-coverage-checker.md`
Invalid: `cast.md`, `cast-1.md`, `security-reviewer.md`

---

## Required @ references

Every cast file must begin with these two lines, before any headings or content:

```
@../../management/play-rules.md
@./act-NN-slug.md
```

Use the actual Act filename. From `acts/act-NN-slug/`, `../../` reaches the Play root, then into `management/`.

| Rule | Type |
|------|------|
| First line is `@../../management/play-rules.md` | HARD |
| Second line is `@./act-NN-slug.md` (actual Act filename) | HARD |
| No other @ references unless the Play explicitly requires them | HARD |

---

## Required sections

| Section | Type | Purpose |
|---------|------|---------|
| `# Cast: <Display Name>` | HARD | Title. Must match the slug's meaning. |
| `## Responsibilities` | HARD | What this Cast does. Narrow, specific scope. |
| `## Access` | HARD | Explicit reads and writes. |
| `## Runtime overrides` | CONFIGURABLE | Override Play/Act runtime defaults (model, reasoning effort). `None.` if no overrides. |

---

## Template

```markdown
@../../management/play-rules.md
@./act-NN-slug.md

# Cast: <Display Name>

## Responsibilities

<What this Cast does. One focused task. Specific deliverable.>

## Access

- Reads: <list of readable paths — reference/, props/, handoffs/, stage/ files>.
- Writes: <list of writable paths — this Act's stage/ and handoffs/<act>/>.

## Runtime overrides

None.
```

---

## Constraints

| Constraint | Type |
|------------|------|
| Cast file is static and locked during execution (including retries) | HARD |
| Cast writes to its Act's `stage/` and `handoffs/<act>/` | HARD |
| Cast does not call other Cast | HARD |
| Cast reports to its Lead only | HARD |
| Cast does not write to `verifications/`, `progress.md`, or another Act's folders | HARD |
| Zero or more Cast per Act (Cast are optional) | HARD |
| Lead chooses fresh or forked context for Cast, unless governing instructions prescribe the choice | HARD |
| Responsibilities describe a single focused task, not coordination | CONFIGURABLE |
| Access section lists every readable and writable path explicitly | CONFIGURABLE |

---

## Notes

- Multiple instances of the same Cast definition may receive different assignments from the Lead. The definition is the template; the assignment prompt differentiates instances.
- Cast receives context in this order: shared rules (play-rules.md) -> Act definition -> Cast file -> Lead's assignment prompt -> permitted files.
- Runtime override precedence: Play defaults -> Act defaults -> Cast overrides.
- Permissions, Gates, and locked-file restrictions cannot be weakened by runtime overrides.
