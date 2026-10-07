# Universal Checklist

> **Usage:** Use as-is. Do not modify per milestone. These checks apply identically regardless of which milestone is being reviewed.

---

## D1 — Structural Clarity

| # | Check | Hard/Soft |
|---|-------|-----------|
| 1.1 | Every file has a single, stated purpose in its first 3 lines | Soft |
| 1.2 | No file exceeds 300 lines (role files) or 500 lines (reference files) | Soft |
| 1.3 | File tree matches the layout documented in SKILL.md | Hard |
| 1.4 | No orphan files (every file referenced by at least one other file) | Hard |
| 1.5 | Actor files follow the standard template (Top Rules, Identity, Can/Cannot, Procedure, Output) | Soft |
| 1.6 | Phase-type files follow the standard template (Summary, Actors, Flow, Restrictions, Format) | Soft |
| 1.7 | No file combines multiple concerns (e.g., actor definition + scoring rubric in same file) | Hard |

---

## D2 — Single Source of Truth

| # | Check | Hard/Soft |
|---|-------|-----------|
| 2.1 | Execution flow defined in exactly one place (no conflicting flow descriptions) | Hard |
| 2.2 | Log format defined in exactly one place | Hard |
| 2.3 | Workspace/folder structure defined in exactly one place | Hard |
| 2.4 | Error handling strategy defined in exactly one place | Hard |
| 2.5 | Phase-type behavior defined only in its phase-type file (not duplicated in actor files) | Hard |
| 2.6 | Scoring/verdict rules defined only in criteria files (not re-stated in actor files) | Soft |
| 2.7 | Restriction rules stated in actor AND phase-type files must be identical (cross-reference, not duplication) | Hard |
| 2.8 | No concept explained in two different ways in two different files | Hard |

---

## D3 — Token Efficiency

| # | Check | Hard/Soft |
|---|-------|-----------|
| 3.1 | No repeated blocks of text across files (>5 lines identical) | Hard |
| 3.2 | Actor prompts contain only what that actor needs (no "just in case" context) | Soft |
| 3.3 | Briefings do not duplicate information available in the phase-type file | Hard |
| 3.4 | Reference files use cross-references (file paths) rather than inline copies | Soft |
| 3.5 | No boilerplate paragraphs that could be replaced by a one-line pointer | Soft |

---

## D4 — Flow Coherence

| # | Check | Hard/Soft |
|---|-------|-----------|
| 4.1 | Step numbers in actor files match the execution sequence in SKILL.md | Hard |
| 4.2 | Request format (what actor A sends) matches response expectation (what actor B parses) | Hard |
| 4.3 | No circular dependencies between actors (A waits for B which waits for A) | Hard |
| 4.4 | Every actor's "Input Contract" has an identified producer | Hard |
| 4.5 | Every actor's "Output Contract" has an identified consumer | Hard |
| 4.6 | Spawn ordering is unambiguous (parallel vs sequential clearly stated) | Soft |
| 4.7 | Completion signals are defined (how does the spawner know the cast member finished) | Hard |

---

## D6 — Contract Stability

| # | Check | Hard/Soft |
|---|-------|-----------|
| 6.1 | Output file naming patterns are locked (defined once, used consistently) | Hard |
| 6.2 | Output format templates include ALL required fields (no implicit fields) | Hard |
| 6.3 | Success/failure report format is identical across all actors that produce it | Hard |
| 6.4 | Briefing format is stable (same structure regardless of phase type) | Hard |
| 6.5 | Version/iteration numbering scheme is defined and unambiguous | Soft |
| 6.6 | All enum-like values (verdicts, severities, statuses) have closed sets | Soft |
| 6.7 | Format definitions are parseable by downstream consumers without guessing | Hard |

---

## D7 — Restriction Consistency (meta-rule)

| # | Check | Hard/Soft |
|---|-------|-----------|
| 7.1 | Every restriction stated in an actor file appears identically in the corresponding phase-type file | Hard |
| 7.2 | No actor file contains restrictions that contradict another actor file | Hard |
| 7.3 | "Cannot do" lists are exhaustive (no implied restrictions missing from the list) | Soft |
| 7.4 | Spawn permissions are consistent (if actor A can spawn B, B's file acknowledges being spawned by A) | Hard |

---

## D8 — Extensibility

| # | Check | Hard/Soft |
|---|-------|-----------|
| 8.1 | Adding a new phase type does NOT require modifying SKILL.md core sections | Hard |
| 8.2 | Adding a new phase type does NOT require modifying actor role files | Hard |
| 8.3 | Phase-type files are self-contained (all type-specific logic lives there) | Hard |
| 8.4 | Generic protocols work for any phase type without modification | Hard |

---

## Totals

- **D1:** 7 items (3 Hard, 4 Soft)
- **D2:** 8 items (6 Hard, 2 Soft)
- **D3:** 5 items (2 Hard, 3 Soft)
- **D4:** 7 items (6 Hard, 1 Soft)
- **D6:** 7 items (5 Hard, 2 Soft)
- **D7:** 4 items (3 Hard, 1 Soft)
- **D8:** 4 items (4 Hard, 0 Soft)

**Grand total: 42 universal checks** (D5 checks are milestone-specific, not listed here)

---

## Scoring Impact

- **Hard fail:** Caps the dimension score at 6/10 maximum (per failed hard item)
- **Soft fail:** Reduces dimension score by 0.5-1 point per item
