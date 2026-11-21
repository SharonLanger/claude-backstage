# Catalog Intake — Adding New Sources

End-to-end pipeline for extracting patterns, anti-patterns, principles, and use-case material from a new blog post, article, or documentation page.

Read this file first. It routes you to the detailed guides for each step.

---

## Before You Start

1. Read the source material fully before extracting anything
2. Have the catalog root `README.md` open for reference (family list, layer model)
3. Know where the detailed guides are:
   - **Writing patterns/anti-patterns/principles:** [authoring-guide.md](authoring-guide.md)
   - **Classifying and placing:** [classification-guide.md](classification-guide.md)
   - **Sources and citations:** [source-registry.md](source-registry.md)
   - **Finding existing content (to check for duplicates):** [../catalog-lookup.md](../catalog-lookup.md)

---

## The Pipeline

### Phase 1: Read & Tag

Read the source and identify every candidate — anything that looks like it could be a pattern, anti-pattern, principle, or use-case material.

For each candidate, note:
- **Name** (use the source's name if it has one, or invent a working name)
- **Type guess** — pattern / anti-pattern / principle / use-case material / skip
- **One-sentence summary** — what problem does it solve or what failure does it describe?
- **Where in the source** — quote or section reference

**What to look for:**

| Signal in the source | Likely type |
|---|---|
| "When building X, do Y because Z" with trade-offs | **Pattern** |
| "Don't do X — here's what goes wrong" with symptoms | **Anti-pattern** |
| A general rule that applies across many situations | **Principle** |
| A concrete scenario ("if you're building a chatbot...") with relevant patterns | **Use-case material** |
| A how-to guide for a specific topic (e.g., "how to design tools") | **Guide** (goes in a family's `guides/` subfolder) |
| A comparison of approaches ("X vs Y for orchestration") | **Comparison** (goes in a family's `comparisons/` subfolder) |
| A checklist or reference table | **Reference** (goes in a family's `reference/` subfolder) |

Output: a candidate list. Don't write any files yet.

### Phase 2: Classify

For each candidate, apply the classification procedure in [classification-guide.md](classification-guide.md):

1. **Confirm the type** — is it really a pattern, anti-pattern, principle, or something else? Use the decision signals.
2. **Assign to a family** (for patterns, guides, comparisons, references) — use the 4-layer model and family selection criteria.
3. **Check for duplicates** — search existing catalog by name, problem, and solution shape. Use [../catalog-lookup.md](../catalog-lookup.md) to navigate.

Output: a filtered list with type, family/location assignment, and duplicate status for each candidate.

### Phase 3: Extract & Write

For each confirmed new candidate, write the file following the schema in [authoring-guide.md](authoring-guide.md):

| Content type | Schema | Where the file goes |
|---|---|---|
| **Pattern** | 8-section schema | `families/<family>/patterns/<family><nn>-<name>.md` |
| **Anti-pattern** | 6-section schema | `anti-patterns/AP<nn>-<name>.md` |
| **Principle** | Principle schema | `principles/P<n>-<name>.md` |
| **Guide** | Guide schema | `families/<family>/guides/<name>.md` |
| **Comparison** | Free-form with trade-off table | `families/<family>/comparisons/<name>.md` |
| **Reference** | Free-form (checklist or table) | `families/<family>/reference/<name>.md` |
| **Use-case material** | Use-case schema | `use-cases/<category>/<name>.md` |

Key rules while writing:
- The **Problem** section comes from the source's description of the failure/limitation — not from the solution
- **Patterns** must include a Mermaid diagram in Solution Structure
- **Sources** must include the new blog/article. Check [source-registry.md](source-registry.md) — if the URL isn't in the registry, verify it exists and add it
- **Related Patterns** — link to existing catalog patterns that pair with, extend, or constrain this one
- **Anti-Patterns Addressed** — link to existing anti-patterns this pattern counters
- **Principles** — link to the principle(s) that motivate this pattern

### Phase 4: Integrate

After writing the files:

1. **Update the family README** — add the new file to the directory tree with a one-line description
2. **Update cross-references** — if existing patterns in other families should link to the new one, update their "Related Patterns" sections
3. **Update the source registry** — if the blog/article is new, add it to [source-registry.md](source-registry.md)
4. **Update the anti-patterns README** — if a new anti-pattern was added, update the tables in `anti-patterns/README.md`
5. **Update the principles README** — if a new principle was added, update `principles/README.md` and `principles/index.md`
6. **Update the use-cases README** — if new use-case material was added, update `use-cases/README.md` master lookup table
7. **Update the root README** — only if counts changed significantly or new families/categories were created

### Phase 5: Verify

Run the verification checklist from [authoring-guide.md](authoring-guide.md) on every new or modified file:

- Pattern files: all 8 sections, Mermaid diagram, 2–6 source links, working relative links
- Anti-pattern files: all 6 sections, working counter-pattern links
- Principle files: all sections per schema, working family and anti-pattern links
- README files: directory tree matches disk, every file has a description
- Use-case files: scenarios link to correct families, anti-patterns exist

---

## Handling Edge Cases

| Situation | What to do |
|---|---|
| Blog describes a technique but not a recurring problem | Skip it — no problem means no pattern |
| Blog describes something that overlaps 2+ existing patterns | Don't create a new file. Add the source to the existing patterns' Sources sections and note any new nuance |
| Blog introduces a concept that doesn't fit any existing family | Flag it. Consider whether it warrants a new family or belongs as a principle. Don't force it into an ill-fitting family. |
| Blog contradicts an existing pattern's claims | Note the contradiction in the existing pattern file as a "Counterpoint" under Trade-offs. Add the source. |
| Blog is behind a paywall or requires login | Do not add it to the source registry. Only publicly accessible sources qualify. |
| Blog describes both patterns and anti-patterns | Extract them separately — patterns go to families, anti-patterns go to `anti-patterns/` |
| Blog has a useful how-to guide for a family topic | Write it as a guide file in the family's `guides/` subfolder |
| Blog compares approaches within a family | Write it as a comparison in the family's `comparisons/` subfolder |
| Blog has a useful checklist or reference table | Write it as reference material in the family's `reference/` subfolder |
| Blog describes a new cross-cutting scenario | Add it to the appropriate `use-cases/` category, or create a new category if none fits |

---

## Quick Reference: File Locations

| What you're creating | Where it goes |
|---|---|
| New pattern | `families/<family>/patterns/<family><nn>-<name>.md` |
| New anti-pattern | `anti-patterns/AP<nn>-<name>.md` |
| New principle | `principles/P<n>-<name>.md` |
| New guide | `families/<family>/guides/<name>.md` |
| New comparison | `families/<family>/comparisons/<name>.md` |
| New reference material | `families/<family>/reference/<name>.md` |
| New use-case index | `use-cases/<category>/<name>.md` |
| New source URL | `contributing/source-registry.md` |

---

Last updated: 2026-11-19
