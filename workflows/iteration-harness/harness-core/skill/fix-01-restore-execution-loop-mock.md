> **Mock example** — this file demonstrates the format and content generated during the iteration process. Replace with real data from your own runs.

# Fix: Restore execution loop imperative in skill entry point

## Problem

The skill entry point's Execution Flow section uses passive description instead of imperative instruction. The executing agent treats this as documentation and stops after planning completes, never entering the phase execution loop.

Evidence: decision-m1-test-failure-mock.md

## Root Cause

A deduplication pass removed the explicit loop instruction ("Loop: prepare phase, spawn agent, receive result, next") because it appeared to duplicate the orchestrator's algorithm. However, the entry point instruction was behavioral (tells the agent what to DO), while the orchestrator algorithm is procedural (tells the agent HOW to do it). Both are needed.

## Suggested Change

In the skill entry point file, Execution Flow section:

Replace:
```
The skill plans work into phases, then executes each phase sequentially
with a dedicated agent. The orchestrator follows the execution algorithm
defined in the orchestrator spec.
```

With:
```
After receiving "Plan ready" from the planner:
1. Enter the phase execution loop — request each phase, spawn an agent, collect the result
2. Continue until the planner reports all phases complete
3. Follow the detailed algorithm in the orchestrator spec

Do NOT stop after planning. The planner completing is the START of execution, not the end.
```

## Acceptance Criteria

- The entry point contains an imperative instruction to loop through phases
- The instruction does NOT restate the full orchestrator algorithm
- Both tests pass (test-01 single-phase + test-02 multi-phase)

## Priority

Correctness

## Delta

Test-02 would go from FAIL to PASS. No impact on test-01 (already passing).
