# Authoring Guide

How to write pattern files, anti-pattern files, and README files for this catalog.

For source citation rules and verified URLs, see [source-registry.md](source-registry.md).
For classifying a pattern into a family, see [classification-guide.md](classification-guide.md).
For the full intake pipeline (source → catalog), see [catalog-intake.md](catalog-intake.md).

---

## Key Definitions

Every term below has a verified source. Do not use these terms loosely.

### Pattern

> A reusable response to a recurring situation when working with LLMs or building with probabilistic models and agents.

A pattern describes the situation, the reusable response, who does what, and when the response helps or adds cost. One relevant source can establish a documented practice. Report how much evidence there is for its applicability.

### Principle

> A cross-cutting rule that explains WHY multiple patterns are shaped the way they are.

Principles are higher than patterns. A principle generates many patterns; a pattern implements one or more principles.

### Anti-Pattern

> A recurring structure that causes failure — the opposite of a pattern. Named so developers can recognize and avoid it.

Link any applicable counter-patterns. Record an explanation without actionable guidance as a research gap during intake.

### Workflow vs. Agent

> **Workflow:** Code predetermines the control flow; the model is called at specific points.
> **Agent:** The model dynamically controls its process and tool usage.

### Harness Engineering

> Engineering the repository, tools, instructions, feedback loops, tests, observability, architectural invariants, and execution environment that allow coding agents to work reliably.

### Context Engineering

> Designing which subset of all available information should be visible to the model at each exact step. Broader than "prompt engineering."

### The Lethal Trifecta

> Combining (1) access to private data, (2) exposure to untrusted content, and (3) ability to communicate externally creates a powerful exfiltration path after prompt injection.

### Deterministic Control Boundary

> If a property can be checked or enforced deterministically, do not rely solely on probabilistic obedience.

### Evaluation (Evals)

> Measuring whether YOUR system performs YOUR task on YOUR data. Error analysis must precede generic eval metrics.

### Orchestration

> Coordinating multiple agents: who directs whom, how work is handed off, how results are merged.

### Map-Not-Manual

> Keep a short top-level instruction file as a map. Put deeper knowledge in structured repository-local documentation.

---

## Practical Entry Format

Use this format when the action is primarily a conversation, manual review, file-based practice, or a tool setting. It applies across families and content types. Family-local engineering schemas describe implementation entries. Practical entries can use prose, a sample exchange, or a worked review or file example without code, pseudocode, or diagrams.

Include the recognizable situation, when it applies, a practical action, a concrete example, limitations or trade-offs, attribution, and relevant catalog links. State what the reader must control (conversation, project files, settings, or implementation). Preserve attribution for source examples and label examples written for the catalog as illustrations. Keep practitioner advice, measured findings, and catalog adaptations visibly distinct.

For authored guidance in any format, cite at least one accessible and relevant source. Add relevant supporting, qualifying, or contradictory sources wherever they improve the entry. Navigation-only indexes point to the entries that carry the evidence. See the [citation rules](source-registry.md#citation-rules).

## Engineering Pattern File Schema

Engineering patterns use this structure or their family-local engineering schema.

| # | Section | Content | Mandatory |
|---|---|---|---|
| 1 | **Problem** | The recurring situation. One paragraph. | Yes |
| 2 | **Solution Structure** | How calls are wired. Must include a Mermaid diagram. | Yes |
| 3 | **When to Use** | Concrete triggering conditions (bullet list). | Yes |
| 4 | **When Not to Use** | Conditions where this pattern adds cost without benefit (bullet list). | Yes |
| 5 | **Trade-offs** | Two-column table: Benefit vs. Cost/Risk. | Yes |
| 6 | **Implementation Sketch** | Pseudocode showing wiring, not business logic. | Yes |
| 7 | **Related Patterns** | Patterns that pair well, extend, or constrain this one (with relative links). | Yes |
| 8 | **Anti-Patterns Addressed** | Named failure modes this pattern prevents. | Yes |
| — | **Sources** | Links to verified blogs/docs where this pattern is described. | Yes |

### Section rules

- **Problem** must describe the failure mode or limitation, not the solution.
- **Solution Structure** must include a Mermaid diagram showing the structural shape (see Mermaid rules below).
- **When to Use / When Not to Use** must be bullet lists of concrete conditions — not restatements of the Problem section.
- **Trade-offs** table must have real costs (latency, tokens, complexity, debugging difficulty) — not just "it's harder."
- **Implementation Sketch** uses pseudocode, not a specific language. Shows the structural wiring, not domain logic.
- **Related Patterns** uses relative markdown links (`[Name](path.md)`).
- **Anti-Patterns Addressed** references named anti-patterns from the `anti-patterns/` folder.
- **Sources** links to one or more relevant sources and makes clear which claims they support. See [source-registry.md](source-registry.md) for citation format and approved sources.

---

## Anti-Pattern File Schema

Anti-pattern files follow a different structure:

| # | Section | Content |
|---|---|---|
| 1 | **Name** | The anti-pattern's canonical name |
| 2 | **Symptoms** | Observable signs that this anti-pattern is present (bullet list) |
| 3 | **Root Cause** | Supported explanation and any relevant uncertainty |
| 4 | **Failure Scenario** | Concrete example of what goes wrong |
| 5 | **Counter-Patterns** | Named patterns that fix this, with relative links |
| 6 | **Sources** | One or more relevant sources |

### Rules

- Symptoms must be observable (things you can see), not judgments.
- Counter-Patterns use working relative links to pattern files.

---

## Principle File Schema

Principle files follow this structure:

| # | Section | Content |
|---|---|---|
| 1 | **Statement** | One sentence — the principle itself |
| 2 | **Problem it addresses** | The failure mode when this principle is violated |
| 3 | **Why it holds** | The underlying reason this constraint matters for probabilistic systems |
| 4 | **Evidence** | Which sources support this principle and under what conditions |
| 5 | **Related families** | Links to families that operationalize this principle |
| 6 | **Counter-patterns** | Anti-patterns that arise when this principle is ignored |
| 7 | **Tension with** | Other principles this one trades off against |
| 8 | **Smell** | One-line diagnostic: "if you see X, this principle is probably being violated" |

### Rules

- Statement must be a single imperative sentence.
- Related families use relative links.
- Counter-patterns link to files in `anti-patterns/`.
- After creating a new principle, update `principles/README.md` and `principles/index.md`.

---

## Use-Case File Schema

Use-case files map a scenario to relevant catalog content:

| # | Section | Content |
|---|---|---|
| 1 | **Scenario** | One paragraph: the situation the developer is in |
| 2 | **Key Families** | Families to consult, with brief explanation of why each is relevant |
| 3 | **Key Patterns** | Specific patterns within those families, with one-line descriptions |
| 4 | **Watch for Anti-Patterns** | Anti-patterns that commonly appear in this scenario |
| 5 | **Recommended Reading Order** | Ordered list of files to read for this scenario |
| 6 | **Related Use-Cases** | Links to other use-case files that overlap |

### Rules

- Use-case files are navigation aids — they point to patterns, not duplicate them.
- Every family and pattern referenced must exist and link correctly.
- After creating a new use-case, update `use-cases/README.md` master lookup table.

---

## Guide File Schema

Guides live inside family directories (`families/<family>/guides/`) and provide how-to content for the family's topic area.

| # | Section | Content |
|---|---|---|
| 1 | **Purpose** | What this guide helps you do (one sentence) |
| 2 | **When to use this guide** | Concrete triggers (bullet list) |
| 3 | **Guide content** | The how-to material — steps, decision trees, worked examples |
| 4 | **Related patterns** | Links to patterns this guide references |
| 5 | **Sources** | Verified URLs |

### Rules

- Guides are procedural — they tell you how to do something, not what a pattern is.
- Keep them in the family they belong to — don't create cross-family guides (use use-cases for that).

---

## Comparison and Reference Files

**Comparison files** (`families/<family>/comparisons/`) compare similar patterns side by side:
- Must include a trade-off table
- Must link to each pattern being compared
- Free-form structure otherwise

**Reference files** (`families/<family>/reference/`) provide checklists, lookup tables, or quick-reference material:
- Must be actionable — checklists have checkboxes, tables have clear columns
- Must link to the patterns they reference
- Free-form structure otherwise

---

## README File Rules

Every folder in this catalog has a `README.md` that serves as a **navigation hub** — not a content file.

### Required Sections

| Section | Purpose |
|---|---|
| **Title line** | `# Family X — Name` or `# Folder Purpose` |
| **Opening paragraph** | 1–3 sentences: what this folder contains and the recurring problem it addresses |
| **Directory Tree** | Code-fenced tree showing every file with a one-line description |
| **Schema Table** | Describes the section structure of content files in this folder |
| **Navigation / Decision Guide** | Helps readers find the right file (decision tree, lookup table, or "How to Navigate") |
| **Cross-Family Links** | Where this family overlaps with others |
| **Last updated** | `Last updated: YYYY-MM-DD` at the bottom |

### Rules

1. A README describes what IS in the folder — never what is NOT there.
2. Every file in the folder must appear in the Directory Tree.
3. One-line descriptions must be concrete (what the file solves), not vague ("useful information").
4. READMEs never contain pattern content — they point to it.
5. The navigation section must answer: "I have problem X — which file do I read?"

---

## Mermaid Diagram Rules

Use Mermaid for engineering patterns where the schema calls for a structural diagram.

### Format

```
<details>
<summary><b>Pattern Name — Diagram Title</b></summary>

` ``mermaid
flowchart TD
    ...
` ``

</details>
```

### Style rules

| Rule | Example |
|---|---|
| Dark node backgrounds | `fill:#1a3a6b` (blue), `fill:#1a5c2a` (green), `fill:#5c1a1a` (red) |
| White text on dark nodes | `color:#fff` |
| Dark strokes | `stroke:#0d2040` |
| Subgraph backgrounds darker than nodes | `fill:#0d1f3c` |
| Direction matches the flow | `LR` for chains, `TD` for hierarchies |

### What to diagram

- The structural wiring between components (prompts, tools, agents, validators)
- NOT the business logic
- NOT sequence diagrams with timing — use flowcharts

---

## Verification Checklist

Before any file is considered complete, verify:

### For all authored guidance

- [ ] The situation, action, applicability, example, and limits are clear
- [ ] At least one accessible, relevant source supports the guidance
- [ ] Substantive claims are supported or clearly identified as adaptations or inferences
- [ ] Source examples, measured results, and catalog illustrations are distinguishable

### For engineering pattern files

- [ ] The engineering schema fits the entry and any required structural diagram is present
- [ ] Problem section describes the failure/limitation, not the solution
- [ ] Trade-offs table has real costs, not platitudes
- [ ] Related Patterns uses working relative links
- [ ] Anti-Patterns Addressed names anti-patterns from the `anti-patterns/` folder

### For README files

- [ ] Directory Tree shows every file in the folder
- [ ] Every file has a one-line description
- [ ] Navigation section exists (decision tree, lookup table, or "How to Navigate")
- [ ] `Last updated: YYYY-MM-DD` line at bottom
- [ ] No pattern content in the README — only navigation

### For anti-pattern files

- [ ] The anti-pattern gives observable symptoms, a supported explanation, and applicable counter-patterns
- [ ] Counter-Patterns use working relative links
- [ ] Symptoms are observable (things you can see), not judgments

### Link verification

Check that repository links resolve and that entry citations match the [source registry](source-registry.md). Verify new source URLs and read the cited material to confirm that it supports the associated claims.

---

Last updated: 2026-11-21
