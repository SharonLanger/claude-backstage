# Review Act — General Tasks

How every skill review runs, regardless of milestone. This file defines the Review Skill Agent's procedure, what it spawns, what inputs it needs, what outputs it produces, and how findings are classified.

---

## Purpose

The review evaluates **specification quality** — not implementation correctness. Tests validate behavior; the review validates that the specification is clear, consistent, and complete enough to reliably produce correct implementations.

---

## Actors

| Actor | Role |
|-------|------|
| **Review Skill Agent** | Lead. Orchestrates the review, spawns cast members, writes final output. |
| **Dimension Reviewer** (x8) | Cast. Evaluates one dimension, scores 0-10, reports findings. |
| **Protocol Verifier** (x1) | Cast. Discovers and verifies all inter-actor protocols. |
| **Synthesis Agent** (x1) | Cast. Aggregates all findings, applies delta rules, produces verdict. |

---

## Dimensions (8 total)

| ID | Name | Core Question |
|----|------|---------------|
| D1 | Structural Clarity | Does each file have one clear purpose? |
| D2 | Single Source of Truth | Is every concept defined in exactly one place? |
| D3 | Token Efficiency | Do agents read only what they need? |
| D4 | Flow Coherence | Can agents follow the flow without ambiguity? |
| D5 | Scenario Completeness | Are all scenarios for the current scope fully specified? |
| D6 | Contract Stability | Are outputs defined precisely enough for testing? |
| D7 | Restriction Consistency | Do boundary rules agree across files? |
| D8 | Extensibility | Can new phase types be added without modifying core files? |

D1-D4, D6-D8 are universal (same definition every milestone).
D5 is milestone-parameterized (the scenario list changes per milestone).

---

## Inputs (per milestone)

The Review Skill Agent reads these before spawning cast:

| Input | Location | Purpose |
|-------|----------|---------|
| Skill source files | `~/.claude/skills/example-skill/` | What is being reviewed |
| Universal checklist | `skill-review/checklist-universal.md` | Fixed structural/quality checks |
| Milestone checklist | `skill-review/<milestone>/checklist-milestone.md` | Scope-specific completeness + restriction checks |
| Scoring criteria | `skill-review/criteria.md` | Universal rubric (0-10 per dimension) with calibration anchors |
| Anti-patterns catalog | `harness-core/skill-review/resources/anti-patterns.md` (sections 5-7) | Pattern IDs for findings |
| Delta acceptance rules | `iteration-guide.md` section "Delta Acceptance Rules" | Thresholds for fix classification |
| Previous review results (if any) | `skill-review/<milestone>/review-<N-1>/results.md` | For delta/regression detection |

### If `checklist-milestone.md` does not exist

Generate it from the template (`skill-review/checklist-template.md`) using:
- The phase types listed in SKILL.md Phase Types table
- The actor files currently in the skill
- The milestone's scope definition

---

## Outputs

```
skill-review/<milestone>/review-<N>/
  results.md              <- Final scorecard + verdict (Synthesis output)
  d1-structural.md        <- Dimension Reviewer output
  d2-ssot.md
  d3-tokens.md
  d4-flow.md
  d5-completeness.md
  d6-contracts.md
  d7-restrictions.md
  d8-extensibility.md
  protocols.md            <- Protocol Verifier output
```

`<N>` increments per review within a milestone (review-1, review-2, review-3).

---

## Task Sequence

### Phase 1: Preparation

**Owner:** Review Skill Agent (no spawn)

1. Read SKILL.md to enumerate actors, phase types, and format files
2. Read the milestone-specific checklist (or generate it from template)
3. Determine which dimensions need milestone-specific input:
   - D5 needs the scenario list from the milestone checklist
   - D8 needs the list of phase types currently supported
4. Determine review round number (N) by counting existing `review-*/` folders

---

### Phase 2: Dimension Scoring (parallel)

**Owner:** Review Skill Agent spawns 8 Dimension Reviewers in parallel.

Each Dimension Reviewer:
1. Reads its dimension definition from `criteria.md`
2. Reads the universal checklist items for its dimension
3. Reads the milestone checklist items (if applicable to its dimension)
4. Reads ALL skill source files
5. Evaluates each check: PASS / FAIL / PARTIAL with evidence
6. Scores 0-10 using calibration anchors
7. Tags findings with delta category + magnitude estimate
8. Writes output to `d<N>-<slug>.md`

**D5 receives:** The milestone's scenario list (from checklist-milestone.md).
**D8 receives:** The current phase-types list + instruction to evaluate pluggability.

---

### Phase 3: Protocol Verification (after Phase 2 or parallel)

**Owner:** Review Skill Agent spawns 1 Protocol Verifier.

The Protocol Verifier:
1. Discovers protocols by scanning `actors/` and `phase-types/` directories
2. Identifies generic protocols (orchestrator-planner loop, phase-agent spawn/report, filesystem handoffs)
3. Identifies phase-type-specific protocols (only for types that exist in the current milestone)
4. For each protocol, reads BOTH sides (sender spec + receiver spec)
5. Compares: exact wording, format parseability, timing
6. Classifies: MATCH / MATCH-SUBSTANCE / MISMATCH / UNDEFINED
7. Writes output to `protocols.md`

**Protocol discovery method:**
- Every actor's Input Contract must have an identified source
- Every actor's Output Contract must have an identified consumer
- Unmatched contracts = incomplete protocol documentation
- Filesystem conventions (briefings, output folders) ARE protocols — verify writer/reader agreement

---

### Phase 4: Synthesis

**Owner:** Review Skill Agent spawns 1 Synthesis Agent after all Phase 2 + Phase 3 agents complete.

The Synthesis Agent:
1. Reads all dimension review files (d1 through d8)
2. Reads the protocol verification file
3. Reads previous review results (if this is review-2 or later)
4. Builds scorecard table
5. Computes aggregate percentage: `(sum of scores) / (num_dimensions * 10) * 100`
6. Applies delta acceptance rules to classify each finding:
   - **Must fix** — meets threshold, correctness or hard robustness failure
   - **Should fix** — meets threshold, above 10% token savings or significant quality improvement
   - **Skip** — below threshold, not worth the churn
7. Ranks must-fix findings: correctness > robustness > token savings > other
8. Detects regressions (if previous review exists): any dimension score decrease
9. Determines verdict using three independent paths (most conservative wins)
10. Identifies test coverage gaps (for D5 findings) — writes to "Test Coverage Gaps" table
11. Writes `results.md`

---

### Phase 5: Output

**Owner:** Review Skill Agent (no spawn)

1. Verify all output files exist in `review-<N>/`
2. Report to the orchestrator: verdict + total score + critical finding count

---

## Scoring Method

### Per-Dimension Scoring

Each dimension is scored 0-10 by an independent reviewer using calibration anchors:

| Score | Anchor |
|-------|--------|
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

### Aggregate Scoring

```
aggregate_pct = (sum of all dimension scores) / (num_dimensions * 10) * 100
```

Scale-independent. Adding or removing dimensions does not invalidate thresholds.

### Verdict Determination (three paths, most conservative wins)

**Path 1 — Aggregate percentage:**
- >= 78% = Ready for implementation
- >= 57% = Ready with caveats
- < 57% = Needs revision

**Path 2 — Critical dimension override:**
- ANY dimension <= 3 = "Needs revision"
- 2+ dimensions <= 5 = cap at "Ready with caveats"

**Path 3 — Critical findings override:**
- > 3 critical findings = "Needs revision"
- Any critical findings = cap at "Ready with caveats"

Final verdict = the most conservative of all three paths.

### Delta Scoring Between Review Rounds

- Each review scores FRESH (absolute, not relative to previous)
- The Synthesis Agent computes deltas and flags regressions
- A dimension score DECREASE between reviews is flagged as a must-investigate item

---

## Delta Acceptance Rules

Reference: `iteration-guide.md` section "Delta Acceptance Rules" (single source of truth).

Summary for review context:

| Category | Threshold | Fix? |
|----------|-----------|------|
| Correctness | Any delta | Always fix |
| Token savings | >10% of per-agent-read overhead | Fix. Below 10% = skip |
| Robustness | Hard failure on valid input | Fix. Soft/cosmetic = skip |
| All other | Blocks progression or causes confusion at next milestone | Fix. Otherwise skip |

### Who applies what:

1. **Dimension Reviewer** — tags each finding with delta category + magnitude estimate. Does NOT classify as must-fix/skip.
2. **Synthesis Agent** — applies thresholds mechanically to produce must-fix / should-fix / skip.
3. **Reasoner** (downstream, not part of act-review) — accepts or overrides using iteration context.

### Scores and fix decisions are independent

A "skip" finding still affects the dimension score (accurate assessment) but does not generate a fix instruction. A dimension can score 7/10 with zero recommended fixes if all deductions are below threshold.

---

## Checklist Structure

### Universal checklist (`checklist-universal.md`)

Fixed items that apply regardless of milestone. Organized by dimension:

- **Structure** (7 items): file sizes, single purpose, tree matches layout, no orphans
- **Single Source of Truth** (8 items): execution flow once, log format once, workspace once, error handling once
- **Token Efficiency** (5 items): no repetition, short prompts, no boilerplate in briefings
- **Flow Coherence** (7 items): step numbers match, request/response formats match, no circular deps
- **Contract Stability** (7 items): locked naming patterns, single format definitions
- **Restriction Consistency** (meta-rule): every restriction stated in an actor file must appear identically in the corresponding phase-type file

Total: ~34 stable items.

### Milestone checklist (`checklist-milestone.md`)

Generated per milestone from template. Contains:

- **D5 Scenario Completeness** items: per-phase-type happy path, error handling, dry-run, interactions
- **D7 Restriction cross-checks**: specific restrictions per phase type (e.g., mono: cannot spawn sub-agents)
- **Protocol checks**: specific protocols introduced by this milestone's phase types
- **D8 Extensibility checks**: how core files handle the new phase types

### Hard vs Soft classification

- **Hard** (cap dimension at 6/10 max if failed): protocol mismatches, missing report formats, execution flow contradictions
- **Soft** (reduce by 0.5-1 point): line count targets, cosmetic markers, minor wording variations

---

## Protocol Verification — Discovery-Based

The Protocol Verifier does NOT use a hard-coded protocol list. It discovers protocols from the skill structure.

### Generic protocols (always present)

- Orchestrator <-> Planner: spawn, plan-ready, fetch-phase, phase-info, status-done, completion-report
- Orchestrator <-> Phase Agent: spawn prompt, success/failure report
- Planner -> Phase Agent (filesystem): briefing, input, output folders

### Phase-type-specific protocols (conditional)

Only checked when the corresponding `phase-types/<name>.md` exists. Discovered by:
1. Reading the phase-type file's "Actors Involved" and "Execution Flow" sections
2. Extracting all actor-to-actor interactions
3. Cross-referencing with actor files

### Completeness test

Every actor's Input Contract must have an identified source. Every Output Contract must have an identified consumer. Unmatched = incomplete protocol documentation = UNDEFINED finding.

---

## Adapting for New Phase Types

When a new phase type is added (e.g., `phase-types/gate.md`):

1. **Dimension reviews adapt automatically:**
   - D1 checks if the new file has a clear single purpose
   - D2 checks if concepts are duplicated with existing files
   - D5 checks the milestone-specific scenarios (provided via checklist-milestone.md)
   - D7 checks restrictions specific to the new type
   - D8 checks whether the new type required core file modifications

2. **Protocol verification adapts automatically:**
   - Verifier discovers new actor interactions from the phase-type file
   - Checks both sides for agreement

3. **Checklists adapt via the template:**
   - Generate new `checklist-milestone.md` from template + new phase type
   - Universal checklist unchanged

4. **Scoring unchanged:**
   - Same 8 dimensions, same 0-10 scale, same percentage thresholds
   - New phase type just adds more surface area to evaluate (more checks per dimension)

**No changes needed to this tasks.md file or to role definitions when phase types are added.**

---

## Review Triggers

### When to run a FULL review

| Trigger | Condition |
|---------|-----------|
| Post-green | All milestone tests pass AND no clean review exists for current skill version |
| Post-review-fix | Skill-Change-Agent applied fixes from review findings AND tests pass again |

### When to SKIP review

- All tests pass AND a clean review already exists for THIS skill version (no changes since)

### When to run PARTIAL review

Only when ALL of:
1. Fix addressed D1, D3, or D5 specifically (the independent dimensions)
2. Fix touched <= 2 files
3. Previous full review scored all other dimensions >= 7/10

Otherwise, run full review.

### Limits

- Maximum 3 full reviews per milestone
- After 3rd: stop and escalate to the Director (structural problem)

---

## Findings Classification (for downstream Reasoner)

Each finding in the review output includes:

```markdown
### Finding N: <title>
- **Severity:** Critical / Major / Minor
- **Location:** <file:section>
- **Issue:** <what's wrong>
- **Suggestion:** <what to change — a recommendation, not a directive>
- **Delta category:** Correctness / Token savings / Robustness / Other
- **Delta magnitude:** <estimated size, e.g., "~45 lines removable from ~270 read = ~17%">
```

The Synthesis Agent classifies into:
- **Must fix** — correctness (any), robustness (hard failure), tokens (>10%)
- **Should fix** — tokens (5-10%), maintainability issues blocking next milestone
- **Skip** — below all thresholds

The Reasoner receives results.md and can:
- Accept the classification and write fix instructions
- Override (e.g., skip a "must fix" that has failed 3 fix attempts)
- Add context (e.g., "this will be resolved by M3 architecture change")

---

## Test Coverage Gaps (review contribution to test suggestions)

The Synthesis Agent identifies gaps where D5 findings indicate uncovered scenarios:

```markdown
## Test Coverage Gaps

| Gap | Existing coverage | Suggested test category |
|-----|-------------------|-----------------------|
| <scenario not tested> | None / Partial | E2E / Workspace-only |
```

These feed into the pre-GATE test suggestion collection. The review does NOT write full test assertions — it identifies WHAT is missing. The Reasoner formalizes suggestions in asserts.md format during fix instructions.

---

## What This File Does NOT Cover

These are responsibilities of OTHER acts, not the review:

| Responsibility | Owner |
|----------------|-------|
| Running tests | act-test-runner |
| Deciding which findings to fix | act-reasoning (Reasoner) |
| Applying fixes to skill files | act-skill-change |
| Progressing to next milestone | the Director (GATE) |
| Writing fix instructions | act-reasoning (Reasoner) |
| Generating full test suggestions | act-reasoning (Reasoner, in fix instructions) |

The review EVALUATES and REPORTS. It never modifies skill files, test files, or makes progression decisions.
