# Catalog Intake — Adding New Sources

Pipeline for turning accessible sources into practical or engineering catalog guidance.

Read this file first. It routes you to the detailed guides for each step.

---

## Before You Start

1. Read the full relevant source material before extracting recommendations. Use inventories to locate sources and dossiers, then check the original material. One accessible, relevant source is sufficient. Include additional sources when they corroborate, qualify, contradict, or extend the guidance.
2. Have the catalog root `README.md` open for reference (family list, layer model)
3. Know where the detailed guides are:
   - **Writing practical and engineering entries:** [authoring-guide.md](authoring-guide.md)
   - **Classifying and placing:** [classification-guide.md](classification-guide.md)
   - **Sources and citations:** [source-registry.md](source-registry.md)
   - **Finding existing content (to check for duplicates):** [../catalog-lookup.md](../catalog-lookup.md)

---

## The Pipeline

### Phase 1: Read & Extract Candidates

Read the source and identify each candidate contribution, including useful observations that may belong in the research inventory.

For each candidate, note:
- **Source and location** — author, title, URL, revision/date where available, and the section or passage used
- **User situation** — recognizable problem or opportunity, including what the user controls
- **Contribution** — useful advice or explanation, with the source's term where useful
- **Evidence type and limits** — documented advice, measured finding, or catalog inference/adaptation, with scope, trade-offs, and reuse terms
- **Existing overlap and proposed destination** — actual entries read and the family or index that fits
- **Disposition** — enrich, write, cross-link, or record a gap, with a reason. Confirm this in Phase 2.

**What to look for:**

| Signal in the source | Likely type |
|---|---|
| A reusable response to a recurring engineering or practitioner situation | **Pattern** |
| "Don't do X — here's what goes wrong" with symptoms | **Anti-pattern** |
| A general rule that applies across many situations | **Principle** |
| A concrete scenario ("if you're building a chatbot...") with relevant patterns | **Use-case material** |
| A how-to guide for a specific topic (e.g., "how to design tools") | **Guide** (goes in a family's `guides/` subfolder) |
| A comparison of approaches ("X vs Y for orchestration") | **Comparison** (goes in a family's `comparisons/` subfolder) |
| A checklist or reference table | **Reference** (goes in a family's `reference/` subfolder) |

Output: a candidate list. Don't write any files yet.

### Phase 2: Classify & Deduplicate

For each candidate, apply the classification procedure in [classification-guide.md](classification-guide.md):

1. **Confirm the type** — is it really a pattern, anti-pattern, principle, or something else? Use the decision signals.
2. **Assign to a family** (for patterns, guides, comparisons, references) — use the 4-layer model and family selection criteria.
3. **Check for duplicates** — search existing catalog by name, problem, and solution shape. Use [../catalog-lookup.md](../catalog-lookup.md) to navigate.

Output: a filtered list with type, family/location assignment, and duplicate status for each candidate.

### Phase 3: Write or Enrich

Use the [authoring guide](authoring-guide.md) for confirmed contributions. Use its practical format for conversation, manual review, file-based, and settings guidance. The table gives the usual locations and engineering schemas.

| Content type | Schema | Where the file goes |
|---|---|---|
| **Pattern** | Practical format or engineering schema | `families/<family>/patterns/<family><nn>-<name>.md` |
| **Anti-pattern** | Practical format or anti-pattern schema | `anti-patterns/AP<nn>-<name>.md` |
| **Principle** | Principle schema | `principles/P<n>-<name>.md` |
| **Guide** | Guide schema | `families/<family>/guides/<name>.md` |
| **Comparison** | Free-form with trade-off table | `families/<family>/comparisons/<name>.md` |
| **Reference** | Free-form (checklist or table) | `families/<family>/reference/<name>.md` |
| **Use-case material** | Use-case schema | `use-cases/<category>/<name>.md` |

Key rules while writing:
- The **Problem** section comes from the source's description of the failure/limitation — not from the solution
- Use diagrams and implementation sketches when they explain engineering structure. A practical entry can explain the action in prose.
- Attribute each contribution. Preserve applicability and limitations. Distinguish source advice, measured findings, catalog adaptations, and composed examples.
- Verify each new source URL and register the source. One source can support multiple entries, and an entry can draw on multiple sources. See [source-registry.md](source-registry.md).
- **Related guidance** — link to existing catalog entries that pair with, extend, or constrain this one
- **Anti-Patterns Addressed** — link to existing anti-patterns this pattern counters
- **Principles** — link to the principle(s) that motivate this pattern

### Phase 4: Integrate

After writing the files:

- [ ] Update the [symptom bridge](../../bridge-file.md), [catalog lookup](../catalog-lookup.md), and [inventory](../../catalog-inventory.md) where the change affects retrieval. Link to the canonical entry and state important applicability limits.
- [ ] Update the owning family and subfolder READMEs, plus the relevant anti-pattern or principle indexes.
- [ ] Update relevant use-case routes and their indexes. Link symptom-first and family-first routes to the same entry.
- [ ] Update related entries where a cross-reference changes the reader's choices.
- [ ] Update the [source registry](source-registry.md) and family–source mapping for new citations.
- [ ] Reconcile changed counts and file lists in the inventory and affected READMEs, including the catalog root.
- [ ] Record uncovered scenarios in repository research. Add runtime routes when there is an applicable entry.

### Phase 5: Verify

Run the verification checklist from [authoring-guide.md](authoring-guide.md) on every new or modified file:

Check the entry and evidence against the applicable format. Walk both routes through to the actual entry with the user’s constraints in mind. From the repository root, run `python3 skills/sl-sensemaker/tests/check-links.py` (requires Pandoc) and `sh skills/sl-sensemaker/tests/test-install.sh` (uses a disposable home).

---

## Handling Edge Cases

| Situation | What to do |
|---|---|
| Source documents a scoped practice or describes an obstacle | Classify actionable guidance by its shape. Record an obstacle without supported guidance in the research inventory. |
| Source overlaps existing entries | Add the supported contribution to each applicable entry. Use a distinct linked guide when the action differs. |
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

Last updated: 2026-11-21
