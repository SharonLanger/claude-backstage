# Results — run-01

> **This is a mock example** showing the format of a per-run results file. Written by the Reporter agent after test execution. Replace with real data from your own runs.

Milestone: M1 — Example Milestone
Date: YYYY-MM-DD
Status: 1/2 tests passed

## Failed Tests

### test-02-multi-phase (14/28 assertions)

- p2/output/result.md — file does not exist (orchestrator stopped after planning)
- p2/output/summary.md — file does not exist
- p3/input/result.md — file does not exist (no copy from p2)
- p3/output/final.md — file does not exist
- All 14 failures stem from orchestrator stopping at `plan-ready` without launching phase agents for phases 2-3

## Passed Tests

### test-01-single-phase (24/24 assertions)

- All structural assertions pass (workspace layout, planner.md exists, briefing content)
- All functional assertions pass (output file contains expected content, arithmetic correct)
- All log assertions pass (execution log exists with required entries)

## Observations

- **Planning works correctly in both tests:** Both test-01 and test-02 produce valid planner.md files with correct phase chains, I/O mappings, and briefing content. All planning-layer assertions pass.
- **Execution fails for multi-phase only:** test-01 (single phase) executes correctly — the orchestrator spawns the phase agent, produces output, and completes. test-02 (3 phases) stalls after planning — the orchestrator writes `plan-ready` but never transitions to execution.
- **Root cause hypothesis:** The orchestrator instructions use passive language ("phases should be executed sequentially") instead of imperative ("execute phases sequentially"). Single-phase tests succeed because the orchestrator treats a 1-phase plan as a single action, but multi-phase requires explicit loop dispatch.
- **Token usage is reasonable:** test-01 at 58k tokens (2m 30s), test-02 at 66k tokens (4m) despite the stall — the orchestrator consumed tokens trying to determine next steps.

## Token Usage — Summary

| # | Test | Skill Tokens | Verifier Tokens | Total Tokens |
|---|------|--------------|-----------------|--------------|
| 01 | single-phase | 58,412 | 51,233 | 109,645 |
| 02 | multi-phase | 65,889 | 62,502 | 128,391 |
| | **TOTAL** | **124,301** | **113,735** | **238,036** |

## Grand Total

| Metric | Value |
|--------|-------|
| Total Tokens | 238,036 |
| Skill Tokens | 124,301 |
| Verifier Tokens | 113,735 |
| Total Tool Calls | 87 |
| Total Duration | 12m 14s |
