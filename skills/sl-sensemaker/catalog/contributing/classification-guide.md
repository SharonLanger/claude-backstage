# Classification Guide

How to classify extracted content and assign it to the right place in the catalog.

---

## Step 1: What type is it?

| If the source describes… | It's a… | File location |
|---|---|---|
| A recurring problem + a reusable structural solution + trade-offs | **Pattern** | `families/<family>/patterns/<name>.md` |
| A recurring structure that causes failure + observable symptoms | **Anti-Pattern** | `anti-patterns/AP<nn>-<name>.md` |
| A cross-cutting rule that explains WHY multiple patterns exist | **Principle** | `principles/P<n>-<name>.md` |
| A how-to procedure for a family's topic area | **Guide** | `families/<family>/guides/<name>.md` |
| A side-by-side comparison of approaches within a family | **Comparison** | `families/<family>/comparisons/<name>.md` |
| A checklist, lookup table, or quick-reference for a family | **Reference** | `families/<family>/reference/<name>.md` |
| A concrete scenario mapping problem → patterns | **Use-case** | `use-cases/<category>/<name>.md` |
| A technique, tip, or best practice without a recurring problem/solution structure | **Not a pattern** — skip or note for future reference | — |

### Decision signals

**It's a pattern when:**
- The source describes the same structural solution appearing in 2+ independent contexts
- There's a clear "when to use / when not to use" boundary
- It has real trade-offs (not "just do this")
- It can be diagrammed as a component wiring

**It's an anti-pattern when:**
- The source describes a failure mode that teams repeatedly fall into
- There are observable symptoms (not just "this is bad")
- Counter-patterns exist that address it

**It's a principle when:**
- It's more abstract than a single pattern — it explains why several patterns share a shape
- It applies across multiple families
- Removing it would make multiple patterns seem arbitrary

**Skip it when:**
- It's a one-off technique specific to one tool/framework
- It's advice without structure ("be careful with X")
- It's already covered by an existing pattern (see Step 3)

**It's a guide when:**
- The source walks through a procedure step-by-step
- It teaches "how to do X" within a specific family's topic area
- It doesn't define a new pattern — it helps you apply existing ones

**It's a comparison when:**
- The source puts two or more approaches side by side
- It has a trade-off table or "X vs Y" framing
- The approaches being compared are patterns within the same family

**It's a reference when:**
- The source provides a checklist, lookup table, or quick-reference card
- It's meant to be consulted during work, not read once
- It applies to a specific family's topic area

**It's a use-case when:**
- The source describes a concrete developer scenario ("if you're building a chatbot...")
- It maps the scenario to multiple patterns across families
- It doesn't define new patterns — it routes to existing ones

---

## Step 2: Which family?

Use the 4-layer model to narrow down, then match against family descriptions.

### Layer → Families

| Layer | What it covers | Families |
|---|---|---|
| **1 — Model Interaction** | What happens inside or immediately around one model call | A, G, O |
| **2 — Workflow / Composition** | How multiple calls, roles, or agents are combined | A, B, C, K |
| **3 — Harness / Runtime** | The environment that makes agent behavior reliable | E, F, H, I, J, L, M, N |
| **4 — Development / Governance** | How developers validate and improve the system | D, K, M |

### Family selection criteria

| Family | Assign here when the pattern is about… |
|---|---|
| **A — Workflow Topology** | Structuring sequences of model calls (chains, loops, routing, parallel) |
| **B — Task Decomposition** | Breaking large tasks into scoped subtasks before execution |
| **C — Orchestration** | Multiple agents dividing work, handing off, reviewing each other |
| **D — Verification** | Confirming output is correct, not just plausible |
| **E — Context Engineering** | Managing what information the model sees at each step |
| **F — Harness Engineering** | The environment/repo/tools that make the agent reliable |
| **G — Tool Design** | How tool interfaces are designed, constrained, and validated |
| **H — Deterministic Control** | Enforcing must-hold rules mechanically, not via prompts |
| **I — Reliability & Recovery** | Handling failures, retries, loops, partial progress |
| **J — Security & Trust** | Preventing unauthorized actions after injection or model error |
| **K — Human Control** | When and how humans intervene in agent decisions |
| **L — Memory & State** | Persisting information across turns, sessions, or agents |
| **M — Observability** | Reconstructing what happened and why |
| **N — Efficiency & Routing** | Making the system faster or cheaper without losing reliability |
| **O — Output & Integration** | Validating model output before it enters deterministic systems |

### When a pattern spans families

Some patterns legitimately belong in multiple families (e.g., Tool Gateway is both G and J). Rules:

1. **Primary home** — the family where the pattern's core problem lives. This is where the file goes.
2. **Cross-references** — other families reference it via relative links in their README and in related patterns' "Related Patterns" sections.
3. **Never duplicate the file.** One file, multiple cross-references.

---

## Step 3: Does it already exist?

Before writing a new file, check for duplicates.

### Search procedure

1. **Search by name:** grep pattern names across all family READMEs
   ```
   grep -ri "<candidate name>" families/*/README.md
   ```

2. **Search by problem:** read the Problem section of patterns in the candidate family — does any existing pattern address the same failure mode?

3. **Search by solution shape:** does any existing pattern describe the same structural wiring, even under a different name?

### If it already exists

| Situation | Action |
|---|---|
| Same pattern, same name | Skip — already cataloged. Add the new source to its Sources section if not already there. |
| Same pattern, different name | Skip — add the new source and note the alternative name in the existing file. |
| Similar but distinct (different problem or different solution shape) | Write a new pattern. Note the relationship in both files' "Related Patterns" sections. |
| Existing pattern is incomplete | Update the existing file with new information from the source. |

---

## Step 4: Assign pattern number

Pattern files are numbered sequentially within their family: `<family-letter><nn>`.

1. Check the highest existing number in `families/<family>/patterns/`
2. Assign the next number: if the highest is G10, the next is G11
3. File name format: `<family><nn>-<kebab-case-name>.md` (e.g., `G11-tool-versioning.md`)

---

## Step 5: Assign anti-pattern number

Anti-patterns are numbered sequentially: `AP<nn>`.

1. Check the highest existing number in `anti-patterns/`
2. Assign the next number: if the highest is AP10, the next is AP11
3. File name format: `AP<nn>-<kebab-case-name>.md`

---

Last updated: 2026-11-19
