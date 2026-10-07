# Milestone Checklist Template

> **Usage:** Copy to `skill-review/<milestone>/checklist-milestone.md` and fill in the bracketed sections based on the milestone's phase types and scope. Do not modify the universal checklist — this template generates ADDITIONAL milestone-specific checks only.

---

## How to Generate

1. Read SKILL.md to identify the phase types in scope for the milestone
2. Read each phase-type file (`phase-types/<name>.md`) to extract actors, restrictions, and protocols
3. Fill in each section below, replacing `[bracketed]` placeholders
4. Delete any section that has zero items (e.g., if no new phase types were added)

---

## D5 — Scenario Completeness

> These checks verify that every scenario for the milestone's phase types is fully specified.

### Per Phase Type: [phase-type-name]

| # | Check | Hard/Soft |
|---|-------|-----------|
| 5.[N].1 | Happy-path execution is fully specified (all steps, inputs, outputs) | Hard |
| 5.[N].2 | Error handling is specified (what happens on failure at each step) | Hard |
| 5.[N].3 | Dry-run behavior is specified (if applicable to this phase type) | Soft |
| 5.[N].4 | Multi-actor interactions are specified (timing, ordering, handoffs) | Hard |
| 5.[N].5 | Edge cases are addressed (empty input, missing files, partial completion) | Soft |
| 5.[N].6 | Retry/recovery behavior is specified (what happens after a failure) | Soft |

> Repeat this table for each phase type in the milestone. Replace `[N]` with an incrementing number per phase type (1, 2, 3...).

### Cross-Phase-Type Scenarios

| # | Check | Hard/Soft |
|---|-------|-----------|
| 5.X.1 | Transition between phase types is specified (how one phase's output feeds the next) | Hard |
| 5.X.2 | Phase ordering constraints are documented (which phases can run in parallel, which are sequential) | Hard |

---

## D7 — Restriction Cross-Checks (Milestone-Specific)

> These verify restrictions that are specific to this milestone's phase types.

### Phase Type: [phase-type-name]

| # | Restriction | Stated In (actor file) | Stated In (phase-type file) | Check |
|---|-------------|------------------------|-----------------------------|-------|
| 7.M.[N] | [specific restriction, e.g., "cannot spawn sub-agents"] | [actor-file.md:section] | [phase-type.md:section] | MATCH / MISMATCH / MISSING |

> Fill one row per restriction per phase type. Both the actor file and phase-type file must state the same restriction identically.

---

## Protocol Checks (Milestone-Specific)

> These verify protocols introduced by this milestone's phase types.

### Protocol: [protocol-name]

| Direction | Message/Artifact | Sender Spec Location | Receiver Spec Location | Check |
|-----------|------------------|----------------------|------------------------|-------|
| [A -> B] | [what is sent] | [file:section] | [file:section] | MATCH / MISMATCH / UNDEFINED |

> Fill one table per protocol. Include both message-based protocols and filesystem-based protocols (briefings, output files).

---

## D8 — Extensibility Checks (Milestone-Specific)

> These verify that newly added phase types did not require core file modifications.

| # | Check | Hard/Soft |
|---|-------|-----------|
| 8.M.1 | [phase-type-name] was added without modifying SKILL.md core sections | Hard |
| 8.M.2 | [phase-type-name] was added without modifying actor role files | Hard |
| 8.M.3 | [phase-type-name]'s phase-type file is self-contained | Hard |
| 8.M.4 | Generic protocols work for [phase-type-name] without modification | Hard |

> Only include this section if the milestone ADDED new phase types. If it only refined existing ones, delete this section.

---

## Generation Checklist (for the Review Skill Agent)

Before using the generated milestone checklist, verify:

- [ ] All phase types in scope are covered in D5
- [ ] All restrictions per phase type are listed in D7
- [ ] All new protocols are listed in the Protocol section
- [ ] D8 section exists only if new phase types were added
- [ ] No universal-checklist items are duplicated here
- [ ] All `[bracketed]` placeholders have been replaced with actual values
