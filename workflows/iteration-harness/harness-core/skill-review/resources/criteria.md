# Universal Scoring Criteria

> **Usage:** Use as-is. Universal scoring rubric — same every milestone. This file defines how to assign scores 0-10 per dimension with calibration anchors.

---

## Calibration Anchors (all dimensions)

| Score | Anchor Description |
|-------|-------------------|
| 10 | Zero defects. Would serve as a reference implementation. |
| 9 | Zero defects, 1-2 purely cosmetic observations. |
| 8 | 1 minor finding, no functional impact. |
| 7 | 1-2 minor findings, one PARTIAL checklist item. |
| 6 | 1 moderate finding OR 3+ minor. Agent would likely succeed. |
| 5 | 1 significant finding introducing real ambiguity. Edge-case failures possible. |
| 4 | Multiple significant findings. Agent would need to guess. |
| 3 | Critical finding: protocol mismatch or missing spec causing runtime failure. |
| 2 | Multiple critical findings. Dimension fundamentally inadequate. |
| 0-1 | Dimension essentially unaddressed. |

**Key rule:** A score of 9+ requires ZERO functional findings.

---

## Hard vs Soft Impact on Scoring

- **Hard checklist failure:** Caps the dimension score at 6/10 maximum, regardless of other factors
- **Soft checklist failure:** Reduces score by 0.5-1 point per item
- Multiple hard failures do NOT stack below 6 — one hard fail already caps at 6

---

## Per-Dimension Scoring Guidance

### D1 — Structural Clarity

| Score Range | Condition |
|-------------|-----------|
| 9-10 | All files single-purpose, correct size, no orphans, tree matches SKILL.md |
| 7-8 | Minor size violations or one file slightly overloaded |
| 5-6 | One file combining multiple concerns, or orphan file found |
| 3-4 | Multiple files lack clear purpose, tree diverges from documentation |
| 0-2 | No discernible file organization |

### D2 — Single Source of Truth

| Score Range | Condition |
|-------------|-----------|
| 9-10 | Every concept defined exactly once, all cross-references correct |
| 7-8 | One minor case of near-duplication (same intent, slightly different wording) |
| 5-6 | One concept defined in two places with risk of drift |
| 3-4 | Multiple concepts duplicated, active contradictions between copies |
| 0-2 | Pervasive duplication, no clear authoritative source for key concepts |

### D3 — Token Efficiency

| Score Range | Condition |
|-------------|-----------|
| 9-10 | Zero unnecessary reads, all briefings minimal, no repeated blocks |
| 7-8 | One instance of mild over-inclusion (< 10% overhead) |
| 5-6 | Noticeable token waste (10-20% of reads unnecessary) |
| 3-4 | Significant waste (>20% overhead), repeated blocks across files |
| 0-2 | Massive duplication, agents reading entire files when needing one section |

### D4 — Flow Coherence

| Score Range | Condition |
|-------------|-----------|
| 9-10 | All steps match, all contracts connected, no circular deps, no ambiguity |
| 7-8 | One minor ordering ambiguity that wouldn't cause failure |
| 5-6 | One significant gap in flow (agent might stall or guess) |
| 3-4 | Multiple flow gaps, circular dependency, or broken contract chain |
| 0-2 | Execution flow is contradictory or unspecified |

### D5 — Scenario Completeness

| Score Range | Condition |
|-------------|-----------|
| 9-10 | All scenarios for current milestone fully specified (happy path + errors + edges) |
| 7-8 | One scenario partially specified (missing one edge case) |
| 5-6 | One scenario largely unspecified or multiple partial specifications |
| 3-4 | Multiple scenarios missing, agent would need to improvise |
| 0-2 | Scenarios essentially not documented |

> Note: D5 is milestone-parameterized. The scenario list comes from `checklist-milestone.md`.

### D6 — Contract Stability

| Score Range | Condition |
|-------------|-----------|
| 9-10 | All outputs precisely defined, naming locked, formats parseable, enums closed |
| 7-8 | One format with an implicit field or minor ambiguity |
| 5-6 | One output format underspecified (consumer would need to guess fields) |
| 3-4 | Multiple outputs underspecified, naming inconsistent |
| 0-2 | Outputs not defined or contradictory across files |

### D7 — Restriction Consistency

| Score Range | Condition |
|-------------|-----------|
| 9-10 | All restrictions identical across all relevant files, no contradictions |
| 7-8 | One minor wording difference (same substance, different phrasing) |
| 5-6 | One restriction missing from one side (actor vs phase-type) |
| 3-4 | Active contradiction between files on what's allowed/forbidden |
| 0-2 | Restrictions poorly documented or pervasively inconsistent |

### D8 — Extensibility

| Score Range | Condition |
|-------------|-----------|
| 9-10 | New phase types can be added by creating one file only, zero core modifications |
| 7-8 | New phase types require one minor mention in a core file (e.g., a list update) |
| 5-6 | New phase types require modifying one core file's logic |
| 3-4 | New phase types require modifying multiple core files |
| 0-2 | Architecture is monolithic — adding anything requires rewriting |

---

## Aggregate Scoring

```
aggregate_pct = (sum of all 8 dimension scores) / (8 * 10) * 100
```

Scale-independent. Adding or removing dimensions does not invalidate thresholds.

---

## Verdict Determination (three paths, most conservative wins)

### Path 1 — Aggregate percentage

| Threshold | Verdict |
|-----------|---------|
| >= 78% | Ready for implementation |
| >= 57% | Ready with caveats |
| < 57% | Needs revision |

### Path 2 — Critical dimension override

| Condition | Effect |
|-----------|--------|
| ANY dimension <= 3 | Forces "Needs revision" |
| 2+ dimensions <= 5 | Caps at "Ready with caveats" |

### Path 3 — Critical findings override

| Condition | Effect |
|-----------|--------|
| > 3 critical findings | Forces "Needs revision" |
| Any critical findings | Caps at "Ready with caveats" |

**Final verdict = the most conservative of all three paths.**

---

## Delta Acceptance Rules (for finding classification)

| Category | Threshold | Classification |
|----------|-----------|----------------|
| Correctness | Any delta | Must fix |
| Token savings | >10% of per-agent-read overhead | Must fix. Below 10% = skip |
| Robustness | Hard failure on valid input | Must fix. Soft/cosmetic = skip |
| All other | Blocks progression or causes confusion at next milestone | Must fix. Otherwise skip |

### Classification tiers

- **Must fix** — meets threshold, correctness or hard robustness failure
- **Should fix** — meets threshold, above 10% token savings or significant quality improvement
- **Skip** — below threshold, not worth the churn

### Important rules

1. Scores are ABSOLUTE (fresh each review), not relative to previous reviews
2. A "skip" finding still affects the dimension score but does not generate a fix instruction
3. A dimension can score 7/10 with zero recommended fixes if all deductions are below threshold
4. Dimension Reviewers TAG findings with delta category + magnitude — they do NOT classify
5. The Synthesis Agent applies thresholds mechanically to produce the classification

---

## Finding Format (required for all dimension reviewers)

```markdown
### Finding N: <title>
- **Severity:** Critical / Major / Minor
- **Location:** <file:section>
- **Issue:** <what's wrong>
- **Suggestion:** <what to change — a recommendation, not a directive>
- **Delta category:** Correctness / Token savings / Robustness / Other
- **Delta magnitude:** <estimated size, e.g., "~45 lines removable from ~270 read = ~17%">
```
