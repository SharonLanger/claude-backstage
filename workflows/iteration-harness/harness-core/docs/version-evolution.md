# Version Evolution: From Broken to Polished

The iteration algorithm produces measurable improvement over time. Each version represents a concrete step from a rough first draft to a tested, reviewed, and polished skill. This document shows the typical evolution pattern across milestones, using generalized examples.

---

## Two Acts

The evolution follows a natural two-act structure. The first milestone answers "does it work?" The second answers "is it good?"

### Act 1: Make It Work (Milestone 1)

The skill begins with a handful of spec files and an initial implementation. First test execution typically scores roughly half the tests passing — the structure is partially right but several behaviors are wrong or missing. Most structural assertions pass, but behavioral ones fail.

The algorithm runs fix-and-retest cycles. Each cycle identifies the failing tests, generates targeted fixes, applies them, and re-runs the full suite. Over several versions and a few test runs, the pattern looks like this:

- **Run 1:** Roughly half the tests pass. Multiple spec gaps surface: execution flow is unclear, dispatch logic is hardcoded, error handling is missing.
- **Run 2:** Most tests pass (e.g., 70-80%). The algorithm has consolidated the execution flow, tightened contracts, and added missing error states. One or two stubborn failures remain.
- **Run 3:** All tests green. The test suite itself has expanded — the algorithm added coverage for edge cases it discovered during fixing.

**Key observation:** The test count grew. The algorithm did not just fix code to pass existing tests — it identified untested behaviors and added assertions, raising the bar as it cleared it.

### Act 2: Make It Better (Milestone 2)

All tests pass. A lesser process would stop here. The iteration algorithm does not.

Milestone 2 introduces multi-dimensional review — multiple independent scoring dimensions evaluate the skill beyond pass/fail. The algorithm then uses delta acceptance rules to decide which review findings are worth fixing, rejecting changes that risk regression or add unnecessary complexity.

Over several runs and a few review rounds, the skill goes from "correct" to "well-engineered":

- **Early review runs:** The first review round applies several fixes (e.g., dispatch logic, contracts, deduplication, structural clarity). One test may regress from the changes — the algorithm identifies the root cause (typically an accidentally removed directive) and restores it.
- **Middle review runs:** All tests green again. Subsequent review rounds find subtler issues — briefing quality gaps, missing documentation entries, bare descriptions that need annotation.
- **Late review runs:** Targeted single-fix changes. The algorithm replaces duplicated content with cross-references, following patterns it established in earlier rounds.

**Key observation:** Assertion counts may fluctuate even as tests stay green. This reflects the review process tightening and relaxing assertion granularity — not regressions. The final assertion count is often lower because redundant checks were consolidated.

---

## Typical Progression Pattern

| Phase | Version | Tests | What Typically Changes | Category |
|-------|---------|-------|------------------------|----------|
| Initial | v1 | ~50% pass | Baseline implementation | — |
| Fix cycle 1 | v2-v3 | ~70-80% pass | Core execution flow, contracts | Correctness |
| Fix cycle 2 | v4-v5 | ~90% pass | Edge cases, error handling | Correctness |
| All green | v6 | 100% pass | Last stubborn failures resolved | Correctness |
| Review round 1 | v7-v8 | 100% pass | Structural clarity, deduplication | Spec clarity |
| Review round 2 | v9 | 100% pass | Token efficiency, single source of truth | Optimization |
| Final | v10+ | 100% pass | Documentation, cross-references | Polish |

The exact version numbers vary by skill complexity. Simple skills may reach all-green in 2-3 versions; complex multi-file skills may take 5-6. Review rounds typically converge in 2-3 passes.

---

## What to Expect

### Early iterations are cheap

Correctness fixes in the first few versions are usually obvious — a missing error state, a hardcoded value that should be dynamic, an incomplete contract. The algorithm identifies the gap, applies the fix, and moves on. These cycles are fast and low-risk.

### Mid iterations are expensive

Once the easy failures are resolved, the remaining ones require root-cause analysis. A test failure in the middle iterations often traces back to an interaction between two specs, or a directive that was correct in isolation but contradictory in context. These cycles take longer and may require multi-file changes.

### Late iterations are surgical

Review-driven changes are highly targeted. The delta acceptance rules filter aggressively — most review findings are rejected as style preferences or low-signal suggestions. The fixes that survive are precise: replace this duplicated paragraph with a cross-reference, add this missing annotation, remove this redundant constraint.

### Assertion counts fluctuate

Even when all tests stay green, the total assertion count may rise or fall between versions. This is normal. Review rounds may add granular assertions to test newly-precise contracts, or consolidate redundant assertions that were testing the same behavior in different ways. Track test pass/fail status, not raw assertion counts.

### The test suite grows

The algorithm may add new tests during fix cycles. When it fixes a bug, it sometimes discovers adjacent untested behavior and adds coverage proactively. Budget for a test suite that is 20-50% larger at the end than at the start.

### Budget guidance

- **3-5 runs per milestone** is typical. Simple milestones may need only 2; complex ones rarely need more than 5.
- **2-3 review rounds maximum.** If review findings are still substantial after 3 rounds, the spec likely has a structural issue that incremental fixes will not solve — consider a redesign pass instead.
- Each run costs one agent invocation (test execution + fix generation). Review rounds additionally invoke the review scoring agent.

---

## Before/After: Structural Comparison Template

A before/after comparison at each milestone boundary shows whether the skill grew, shrank, or stayed flat. Here is the typical format:

### Milestone 1: Make It Work (v1 to vN)

| Aspect | Start | End | Change |
|--------|-------|-----|--------|
| Total files | e.g., 6 | e.g., 6 | Typically unchanged — correctness fixes modify existing files |
| Total lines | e.g., ~1,000 | e.g., ~1,050-1,100 | Modest growth (5-10%) from added contracts and error handling |
| Entry point | e.g., 150 lines | e.g., 140 lines | Often shrinks — redundant explanation removed |
| Most-changed spec | e.g., 100 lines | e.g., 130 lines | 20-30% growth — the spec that needed the most work |
| Least-changed spec | e.g., 90 lines | e.g., 90 lines | Unchanged — already correct |

**Typical pattern:** M1 changes are surgical. The overall structure stays stable — same files, same directory layout. Growth concentrates in the specs that needed the most work, while other files stay flat or shrink.

### Milestone 2: Make It Better (vN to vFinal)

| Aspect | Start | End | Change |
|--------|-------|-----|--------|
| Total files | e.g., 6-7 | e.g., 6-7 | May add one file (scripts, utilities) |
| Total lines | e.g., ~1,100 | e.g., ~1,100 | Net zero — additions offset by deduplication |
| Entry point | e.g., 150 lines | e.g., 140 lines | Shrinks — flow sections replaced with pointers |
| Deduplicated spec | e.g., 90 lines | e.g., 75 lines | Shrinks 10-15% — inline text replaced with cross-references |
| Annotated spec | e.g., 230 lines | e.g., 255 lines | Grows 5-10% — precision added where review found ambiguity |

**Typical pattern:** M2 net content stays flat while quality improves. The consistent pattern is: remove duplicated text, replace with cross-references, add precision where reviews found ambiguity.

See `implementation/m1-example/results/` for a concrete example with mock run data.

---

## How This Connects to the Scaffold

| Concept | Where It Lives | Purpose |
|---------|----------------|---------|
| Version backups | `iteration-guide.md` (backup rules) | Ensures every version is recoverable before fixes are applied |
| Run results | `implementation/m1-example/results/` | Stores test output from each iteration for comparison |
| Decision trail | `decisions/` | Records why specific fixes were chosen over alternatives |
| Review scorecards | `skill-review/m1/` | Captures multi-dimensional review scores that drive M2 improvements |
| Progression tracking | `implementation/m1-example/results/results-summary.md` | Aggregates pass/fail progression across runs |
| Test definitions | `implementation/m1-example/tests/` | The assertions that drive the fix-and-retest loop |
