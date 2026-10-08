# Examples: Acts and Roles

Annotated snippets from two Acts in the same Play. Act 01 uses a Lead + Cast; Act 02 is Lead-only. Both demonstrate the standard file structure.

---

## Example 1: Act file — Goal and Workspace

```markdown
# Act 01 — Review Metering API

## Goal

Review the metering API baseline for correctness, security, and maintainability issues across all defined review dimensions.

## Workspace

`acts/act-01-review-api/stage/`

Actors exchange dimension findings and synthesis files here before publishing the final outputs.
```

**What makes this good:**
- The goal is one sentence, describing the outcome (a review across dimensions), not the process.
- The workspace points to `stage/` with a one-line description of how it's used.
- The Act title uses the naming pattern: two-digit number, descriptive slug.

---

## Example 2: Act file — Inputs and Outputs

```markdown
## Inputs

- `reference/api-baseline/` — current API source files.
- `reference/requirements.md` — endpoint specs, tenant isolation, rate limits.
- `reference/security-criteria.md` — OWASP-adapted security checklist.
- `acts/act-01-review-api/props/review-dimensions.md` — the three review dimensions to cover.

## Outputs

- `handoffs/act-01-review-api/review-report.md` — findings with evidence, severity, and affected files.
- `handoffs/act-01-review-api/action-items.md` — proposed fixes with unique IDs (F01–F0N).
```

**What makes this good:**
- Every input is a specific path with a short description.
- Inputs come from three source types: `reference/` (shared), `props/` (Act-specific), and prior handoffs would be listed here for later Acts.
- Outputs are specific files in `handoffs/act-01-review-api/`, not vague descriptions.
- Each output describes what the file contains.

---

## Example 3: Act file — Flow (multi-Cast)

```markdown
## Flow

1. Lead assigns each Cast a review dimension from `props/review-dimensions.md`.
2. Security Reviewer writes `stage/security-findings.md`; Code Analyst writes `stage/correctness-findings.md`.
3. Lead reviews both, resolves overlaps, writes `stage/consolidated-findings.md`.
4. Lead produces the final `review-report.md` and `action-items.md` in `handoffs/`.
```

**What makes this good:**
- Each step names the actor (Lead, Security Reviewer, Code Analyst).
- Intermediate files land in `stage/` with specific names.
- The Lead consolidates before producing final outputs — coordination is explicit.
- Final outputs go to `handoffs/`, not `stage/`.

---

## Example 4: Act file — Flow (Lead-only)

```markdown
## Flow

Single Lead, no Cast. The Lead:
1. Reads the approved fix IDs from `progress.md`.
2. Applies each fix to the baseline, working in `stage/`.
3. Validates syntax and consistency.
4. Publishes updated files to `handoffs/act-02-apply-fixes/api/` and the change report.
```

**What makes this good:**
- Explicitly notes "Single Lead, no Cast" — no ambiguity about who's doing the work.
- The first step reads a Gate decision (`progress.md` has the Director's approved fix IDs) — this Act depends on the prior Gate.
- Working in `stage/`, publishing to `handoffs/` — the boundary is clear.

> **Note:** The Lead reading `progress.md` directly is one approach. Alternatively, the Stage Manager's assignment prompt could convey the approved fix IDs, avoiding a direct Lead dependency on `progress.md`. Both patterns are valid; the Play author decides.

---

## Example 5: Lead file (multi-Cast Act)

```markdown
@../../management/play-rules.md
@./act-01-review-api.md

# Lead: Review Coordinator

## Responsibilities

Coordinate the API review across all dimensions. Assign dimensions to Cast, consolidate their findings, resolve overlaps and conflicts, and produce the final review report and action items.

## Access

- Reads: `reference/api-baseline/`, `reference/requirements.md`, `reference/security-criteria.md`, `acts/act-01-review-api/props/`.
- Writes: `acts/act-01-review-api/stage/`, `handoffs/act-01-review-api/`.

## Cast coordination

- Assign Security Reviewer the security dimension (fresh context).
- Assign Code Analyst the correctness and maintainability dimensions (fresh context).
- Consolidate Cast outputs from `stage/` into final handoff files.

## Runtime overrides

None. Inherits Act defaults.
```

**What makes this good:**
- Starts with the two mandatory `@` references — rules first, then Act definition.
- Responsibilities describe coordination, not implementation details.
- Access lists specific read and write paths.
- Cast coordination names each Cast member, their assignment, and the context choice (fresh).
- The consolidation step is explicit — the Lead owns the final output.

---

## Example 6: Lead file (Lead-only Act)

```markdown
@../../management/play-rules.md
@./act-02-apply-fixes.md

# Lead: API Fixer

## Responsibilities

Implement all Director-approved fixes from the action items list. Produce an updated copy of the metering API and a change report mapping each fix ID to the affected files and changes made.

## Access

- Reads: `reference/api-baseline/`, `reference/requirements.md`, `handoffs/act-01-review-api/`, `acts/act-02-apply-fixes/props/`, `progress.md` (for approved fix IDs).
- Writes: `acts/act-02-apply-fixes/stage/`, `handoffs/act-02-apply-fixes/`.

## Cast coordination

No Cast in this Act. Lead works alone.

## Runtime overrides

None. Inherits Act defaults.
```

**What makes this good:**
- Same structure as the multi-Cast Lead — all four sections present.
- Cast coordination explicitly says "No Cast in this Act. Lead works alone." — the section is required even when empty.
- Access reads include `progress.md` for the Director's Gate decision — this traces the dependency on the prior Gate.
- Reads include prior Act's handoffs (`handoffs/act-01-review-api/`) — the Act chain is visible.

---

## Example 7: Cast file

```markdown
@../../management/play-rules.md
@./act-01-review-api.md

# Cast: Security Reviewer

## Responsibilities

Review the metering API baseline against all criteria in `reference/security-criteria.md` (SEC-01 through SEC-07). For each criterion, report compliance or non-compliance with specific code locations and evidence.

## Access

- Reads: `reference/api-baseline/`, `reference/security-criteria.md`, `acts/act-01-review-api/props/review-dimensions.md`.
- Writes: `acts/act-01-review-api/stage/security-findings.md`.

## Runtime overrides

None.
```

**What makes this good:**
- Narrow, focused responsibility: review against one specific criteria set.
- Writes to exactly one file in `stage/` — the Cast's output is well-scoped.
- No Cast coordination section — Cast files don't have one (only Leads do).
- The criteria are named (`SEC-01 through SEC-07`) — the Cast knows exactly what to check.

---

## Example 8: Multi-Cast Act vs Lead-only Act — structural comparison

| Property | Act 01 (Review) | Act 02 (Apply Fixes) |
|----------|-----------------|----------------------|
| Lead | Review Coordinator | API Fixer |
| Cast | Security Reviewer, Code Analyst | None |
| Flow pattern | Lead assigns → Cast work → Lead consolidates | Lead does all work sequentially |
| Intermediate files | Cast write to `stage/`, Lead consolidates | Lead works in `stage/` |
| Final outputs | Lead publishes to `handoffs/` | Lead publishes to `handoffs/` |
| Gate dependency | None (first Act) | Reads Director's approved fixes from `progress.md` |

**When each pattern fits:**
- Act 01 decomposes naturally: security and correctness are independent review dimensions that benefit from focused agents.
- Act 02 is a single sequential task (apply approved fixes) — decomposition would add overhead without benefit.
