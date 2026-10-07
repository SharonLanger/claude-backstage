> **Mock example** — this file demonstrates the format and content generated during the iteration process. Replace with real data from your own runs.

# Decision — M1 Test Failure Analysis

## Evidence Reviewed

- Test results: `implementation/m1-example/results/results-summary.md` — 1/2 tests passed, FAIL
- Test-02 logs: orchestrator stopped after planning, no phase execution
- Current skill version: v2
- Previous skill version: v1 (baseline — 0/2 tests passed)

## Analysis

### Failure Characterization

Test-02 (multi-phase execution) fails because the orchestrator does not transition from planning to phase execution. The planner completes successfully — workspace is created, briefings are written, phases are planned. But the orchestrator treats the planner's "Plan ready" response as task completion instead of continuing into the phase execution loop.

Test-01 (single-phase) passes because its workload completes within the planning phase.

### Root Cause

The skill's entry point file describes the execution flow in passive language: "The skill plans work into phases, then executes each phase sequentially." This is a description, not an instruction. The executing agent reads it as documentation rather than a directive.

The previous version (v1) had an explicit imperative: "Loop: prepare phase, spawn agent, receive result, report, next." This was removed during a deduplication pass that treated it as redundant with the orchestrator's algorithm.

**Critical distinction:** LLM agents follow imperatives. They read descriptions as documentation. Removing the imperative instruction broke the execution loop.

### Delta Assessment

| Category | Threshold | Applies? |
|----------|-----------|----------|
| Correctness | Any delta | YES — complete execution failure on multi-phase tasks |

This is a hard correctness regression. The fix must restore an imperative execution instruction without reintroducing the full duplicated algorithm.

## Decision

- **Action:** Fix — restore imperative execution loop instruction in the skill entry point
- **Reason:** Correctness regression from over-aggressive deduplication. The loop instruction was behavioral, not documentary.
- **Next step:** act-skill-change applies fix, then act-test-runner re-runs both tests.

## Goal for Next Step

Restore 2-3 imperative sentences in the entry point's Execution Flow section. The fix must:
1. Give the agent an explicit imperative to loop through phases after planning
2. NOT reintroduce the full step-by-step algorithm (keep cross-reference to orchestrator spec)
3. Be short enough to avoid the duplication problem the original change was solving
