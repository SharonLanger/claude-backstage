# Director Interaction Guidelines

Recommendations for how the model presents information to the Director and how agents should handle Director decisions. These are guidance, not mandatory rules — the mandatory authority rules live in [rules/authority.md](../rules/authority.md) and [agents/director.md](../agents/director.md).

## Make Gate prompts useful

At a Gate, the Stage Manager stops and addresses the Director. The quality of this interaction matters — a useful Gate prompt helps the Director make an informed decision quickly; a poor one forces the Director to dig through files to understand what happened.

**A useful Gate prompt includes:**

1. The Gate name and where it falls in the Play.
2. A summary of completed work since the last Gate or Play start.
3. Links to relevant outputs — handoff files, verification reports.
4. The Play's hints for this Gate — what the Director should inspect or decide.

**Keep the summary honest.** Report what was done and what the verification found, including any exceptions the Stage Manager exercised. Do not editorialize or advocate for a particular decision.

**Link, don't duplicate.** Point the Director to the verification reports and handoff files. Do not paste their contents into the Gate prompt. The Director can read the source files; the prompt should help them navigate, not replace, the evidence.

## Distinguish explicit overrides from inferred intent

The Director's authority is activated by explicit instruction, not by implication.

**Explicit override:** "Skip the security review Gate — I've already reviewed the changes externally."
**Not an override:** The Director edited a configuration file. (File edits do not constitute permission to bypass a Gate or change rules.)

When the Director gives a clear, explicit instruction, act on it without redundant confirmation. Asking "Are you sure?" for an unambiguous instruction wastes the Director's time and implies distrust.

When the instruction is ambiguous — unclear scope, contradicts a model rule without acknowledging it, or could be interpreted multiple ways — clarify before acting. The cost of asking is low; the cost of misinterpreting an override is high.

## Scope overrides narrowly

A Director override applies only within its stated scope. Once the stated scope is fulfilled, the override expires.

**Example:** "For Act 3, the Lead may also read Act 1's `stage/` files." This override applies to Act 3 only. It does not grant Act 4's Lead the same access, and it does not expand the Lead's general permissions for future Plays.

When recording an override in `progress.md`, note both the instruction and its scope. This protects against scope creep and helps crash recovery understand what was authorized.

## Preserve normal boundaries outside overrides

An override for one situation does not relax rules everywhere. If the Director says "Skip the security Gate," the remaining Gates are still enforced. If the Director says "The Lead may write to `reference/`," that does not mean `reference/` is now generally writable.

Agents should return to normal behavior as soon as the override's scope is fulfilled.

## Handle checklist modifications cleanly

The Director may change checklists at any time — between verification rounds, before an Act begins, or pre-emptively for a future Act that has not yet started. When a checklist change happens:

- Use the current Director-authorized checklist for the next verification — not a cached version.
- The Stage Manager records the change in `progress.md`.
- Previous verification reports (run against the old checklist) are preserved as-is. They reflect what was true at the time.

Do not retroactively re-evaluate old reports against new criteria. The audit trail shows the evolution of both the checklist and the verification results.

## Skip semantics

When the Director explicitly instructs skipping a Gate:

- Mark the Gate as **Skipped** — not Done, not Passed.
- Record the Director's instruction verbatim.
- Acts whose verification was skipped are not falsely represented as verified.

A skip is an explicit, recorded decision. It is not a quiet omission. The distinction matters for the audit trail and for crash recovery.

---

**Related files:**

- [agents/director.md](../agents/director.md) — Director role definition, authority, and limits
- [rules/authority.md](../rules/authority.md) — authority hierarchy, Gate enforcement, override scope
- [agents/stage-manager.md](../agents/stage-manager.md) — Gate presentation responsibilities
- [execution/flow.md](../execution/flow.md) — Gate mechanics within the execution sequence
