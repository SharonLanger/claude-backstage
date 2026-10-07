# Report Rules — example-skill Tests

---

## Who Creates the Report

Reports **must** be created by a dedicated **sub-agent** (the "reporter"). The runner never writes reports directly — it spawns a reporter agent and provides this file as input.

The reporter agent receives:
1. This file (`report-rules.md`) — the format rules
2. The run path — where to find per-test `results.md` files
3. The milestone results path — where to write output files
4. The milestone name and test index — for context

---

## Output Files

The report system produces three files:

| File | Location | Purpose |
|------|----------|---------|
| `report.md` | `<milestone>/tests/runs/<run-ID>/report.md` | Detailed report for this run |
| `results-<run-ID>.md` | `<milestone>/results/results-<run-ID>.md` | Compact failure summary + observations |
| `results-summary.md` | `<milestone>/results/results-summary.md` | Running table across all runs (updated each run) |

The `results/` folder lives at the milestone root (sibling to `tests/`):

```text
<milestone>/
├── README.md
├── test.md
├── tests/
│   └── runs/
│       └── run-02/
│           ├── test-01/results.md
│           ├── test-02/results.md
│           └── report.md          ← detailed report
└── results/
    ├── results-run-01.md          ← compact per-run
    ├── results-run-02.md          ← compact per-run
    └── results-summary.md         ← running overview table
```

---

## Reporter Agent Prompt Template

```text
Agent(
  description: "report writer (run-XX)",
  prompt: """
You are writing the test suite reports for a completed example-skill test run.

Rules file: harness-core/implementation/report-rules.md
Run path: <MILESTONE>/tests/runs/<RUN_ID>/
Results path: <MILESTONE>/results/
Milestone: M<N> — <milestone name>
Test count: <total tests>

1. Read report-rules.md for the exact format of all three output files.
2. Read each test-NN/results.md in the run folder.
3. Write three files:
   a. <run-path>/report.md — detailed report
   b. <results-path>/results-<RUN_ID>.md — compact failure summary
   c. <results-path>/results-summary.md — update the running table (append a row)

These are your ONLY outputs. Do not modify any other file.
""",
  run_in_background: true
)
```

---

## File 1: `report.md` — Detailed Run Report

Location: `<milestone>/tests/runs/<run-ID>/report.md`

This is the full report for a single run. Shows everything.

### Format

```markdown
# Test Suite Report — <RUN_ID>

Milestone: M<N> — <Milestone Name>
Date: <YYYY-MM-DD HH:MM>
Skill: example-skill

## Summary

| Status | Count |
|--------|-------|
| 🟢 PASS | X |
| 🔴 FAIL | Y |
| TOTAL | Z |

## Results

| # | Test | Category | Status | Pass/Total | Advisory |
|---|------|----------|--------|------------|----------|
| 01 | single-mono-haiku | E2E | 🟢 | 18/18 | 6/6 |
| 02 | four-mono-cumulative | E2E | 🔴 | 14/16 | 10/12 |
| 03 | default-model-effort | Dry-run | 🟢 | 12/12 | 4/5 |
| ... | ... | ... | ... | ... | ... |

## Failed Tests

### test-02 — four-mono-cumulative (14/16)

**What was tested:** <brief description of what this test verifies>

**Failures:**

- 🔴 Contains action: `phase-completed` with description containing "P3" — NOT FOUND
  - **Expected:** Orchestrator log contains a phase-completed entry for P3
  - **Got:** Log has phase-completed for P1, P2, P4 but not P3
- 🔴 p3/output/number.md is not empty — FILE MISSING
  - **Expected:** P3 phase agent writes output
  - **Got:** File does not exist in workspace

### test-06 — custom-properties (17/18)

**What was tested:** <brief description>

**Failures:**

- 🔴 P1 entry includes custom properties section — planner.md has Model/Effort but no dedicated section
  - **Expected:** planner.md contains a visible custom properties block
  - **Got:** Custom props forwarded to briefing only, not surfaced in planner

## Token Usage — Per Test Detail

### test-01 — single-mono-haiku

| Agent | Role | Model | Effort | Tokens | Tools | Duration |
|-------|------|-------|--------|--------|-------|----------|
| otor-01 | orchestrator | sonnet | medium | 28,400 | 12 | 1m 30s |
| planner-01 | main-planner | sonnet | medium | 18,200 | 8 | 0m 55s |
| p1-agent | phase-agent (P1) | haiku | low | 13,806 | 5 | 0m 40s |
| **Skill Total** | | | | **60,406** | **25** | **3m 05s** |

### test-02 — four-mono-cumulative

| Agent | Role | Model | Effort | Tokens | Tools | Duration |
|-------|------|-------|--------|--------|-------|----------|
| otor-02 | orchestrator | sonnet | medium | 30,100 | 15 | 2m 10s |
| planner-02 | main-planner | sonnet | medium | 12,500 | 6 | 0m 45s |
| p1-agent | phase-agent (P1) | haiku | low | 5,800 | 4 | 0m 30s |
| p2-agent | phase-agent (P2) | haiku | low | 6,100 | 5 | 0m 35s |
| p3-agent | phase-agent (P3) | haiku | low | 5,900 | 5 | 0m 32s |
| p4-agent | phase-agent (P4) | haiku | low | 5,858 | 4 | 0m 28s |
| **Skill Total** | | | | **66,258** | **39** | **5m 00s** |

(repeat for all tests)

```

### Rules for report.md

1. **Summary counts must match** — count PASS/FAIL by reading first line of each `results.md`
2. **Failed Tests section** — only tests with failures appear; passing tests are omitted
3. **Per-failure detail** — each `🔴` gets an "Expected/Got" breakdown explaining what the test tried to verify vs what actually happened
4. **Per-Test Token Detail table** — only skill-related agents (orchestrator, main-planner, phase-agents). NOT the verifier or reporter agents themselves
5. **Date format** — `YYYY-MM-DD HH:MM` (24h)
6. **Missing data** — if a results.md is missing, mark that test as `🟡 INCOMPLETE`

---

## File 2: `results-<run-ID>.md` — Compact Per-Run Results

Location: `<milestone>/results/results-<run-ID>.md`

This is a compact file: just the failures and observations. No token tables, no passing test details.

### Format

```markdown
# Results — <RUN_ID>

Milestone: M<N> — <Milestone Name>
Date: <YYYY-MM-DD HH:MM>
Status: X/Y tests passed

## Failed Tests

### test-NN — <name> (X/Y assertions)

- 🔴 <assertion> — <reason>
- 🔴 <assertion> — <reason>

### test-NN — <name> (X/Y assertions)

- 🔴 <assertion> — <reason>

## Observations

<Patterns, common failures, comparison to prior runs, non-determinism notes, suggestions>

## Token Usage — Summary

| # | Test | Skill Agents | Skill Tokens | Verifier Tokens | Other Tokens | Total Tokens |
|---|------|-------------|--------------|-----------------|--------------|--------------|
| 01 | single-mono-haiku | 3 | 60,406 | 50,408 | — | 110,814 |
| 02 | four-mono-cumulative | 6 | 66,258 | 55,041 | — | 121,299 |
| 03 | default-model-effort | 2 | 57,936 | 48,559 | — | 106,495 |
| ... | ... | ... | ... | ... | ... | ... |
| | **TOTAL** | **X** | **Y** | **Z** | **W** | **GRAND** |

## Grand Total

| Metric | Value |
|--------|-------|
| Total Tokens | X |
| Skill Tokens | Y |
| Verifier Tokens | Z |
| Total Tool Calls | W |
| Total Duration | Xm Ys |
| Avg per Test (E2E) | ~Xk tokens / Ym |
| Avg per Test (Dry-run) | ~Xk tokens / Ym |
```

### Rules for results-<run-ID>.md

1. **Only failed tests listed** — if all pass, the Failed Tests section says "All tests passed."
2. **Observations collected from per-test results.md** — merge the `## Observations` sections from each test's results.md into a unified analysis
3. **Keep it brief** — this is the quick-reference file. Detailed breakdowns are in report.md

---

## File 3: `results-summary.md` — Running Overview

Location: `<milestone>/results/results-summary.md`

This file is **updated** (not overwritten) with each new run. It maintains a single table with one row per run, giving a bird's-eye view of the milestone's testing history.

### Format

```markdown
# Results Summary — M<N> <Milestone Name>

| Run | Date | Status | Assertions | Skill Tokens | Total Tokens | Duration | Skill Version | Runner | Links |
|-----|------|--------|------------|--------------|--------------|----------|---------------|--------|-------|
| run-01 | YYYY-MM-DD | 🔴 5/7 | 156/179 | 412k | 769k | 29m | v6 | the Director | [results](results-run-01.md) \| [report](../tests/runs/run-01/report.md) |
| run-02 | YYYY-MM-DD | 🔴 5/7 | 176/179 | 412k | 769k | 29m | v6 | the Director | [results](results-run-02.md) \| [report](../tests/runs/run-02/report.md) |
```

### Column Definitions

| Column | What it shows |
|--------|---------------|
| Run | Run ID (e.g., `run-02`) |
| Date | Run date (`YYYY-MM-DD`) |
| Status | 🟢/🔴 + pass/total tests (e.g., `🔴 5/7`) |
| Assertions | Total passed/total assertions across all tests (e.g., `176/179`) |
| Skill Tokens | Total tokens consumed by skill agents (orchestrator + planner + phase agents) — use `k` suffix |
| Total Tokens | Grand total including verifiers and reporter — use `k` suffix |
| Duration | Wall-clock time for the full run |
| Skill Version | Skill backup version at time of run (e.g., `v6`) |
| Runner | Who triggered the run |
| Links | Relative links to both `results-<run-ID>.md` and `report.md` |

### Rules for results-summary.md

1. **Append-only** — never remove previous rows. Each run adds one row
2. **If file doesn't exist** — create it with the header and first row
3. **If file exists** — read it, append the new row, write it back
4. **Tokens use `k` suffix** — round to nearest thousand (e.g., `412k`, `769k`)
5. **Links are relative** — `results-<run-ID>.md` is in the same folder; `report.md` is at `../tests/runs/run-XX/report.md`
6. **Links column format** — `[results](results-run-XX.md) \| [report](../tests/runs/run-XX/report.md)`

---

## Token Collection Details

The reporter reads token info from agent task-notifications. These contain:

```xml
<usage>
  <subagent_tokens>60406</subagent_tokens>
  <tool_uses>25</tool_uses>
  <duration_ms>185000</duration_ms>
</usage>
```

Convert:
- `subagent_tokens` → comma-separated number for tables, `k` suffix for summary
- `duration_ms` → `Xm YYs` format
- If usage data is unavailable, write `—` in the cell

### Agent Classification

| Agent type | Counts as |
|-----------|-----------|
| Orchestrator (runs the skill) | Skill |
| Main-planner (spawned by skill) | Skill |
| Phase-agent (spawned by skill) | Skill |
| Verifier (checks assertions) | Verifier |
| Reporter (writes reports) | Other |
| Any nested sub-agent of phase-agent | Skill |
