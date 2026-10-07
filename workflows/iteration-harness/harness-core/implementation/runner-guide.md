# Runner Guide — example-skill Tests

Everything a fresh agent needs to run the test suite, collect results, and produce a report.

---

## Overview

- **Skill under test:** `example-skill` (at `~/.claude/skills/example-skill/`)
- **Test rules:** [`test-rules.md`](test-rules.md) — assertion format, results format, categories
- **Report rules:** [`report-rules.md`](report-rules.md) — report format, reporter agent prompt
- **Milestone-scoped:** runner targets one milestone at a time
- **Parallelism:** ALL tests in a milestone run simultaneously — no tier ordering, no sequential gating between tiers

---

## Milestone Resolution

The runner is given a milestone name (e.g., "M1"). It resolves the test directory from the milestone folder:

```text
implementation/<milestone-folder>/tests/
```

The test index is at `<milestone-folder>/test.md`. It lists all tests and their categories.

---

## Run-ID System

Runs are stored per-milestone under a `runs/` folder:

```text
<milestone>/tests/
├── test-01-<desc>/
├── test-02-<desc>/
└── runs/
    ├── run-01/
    │   ├── test-01/    ← workspace for test-01
    │   ├── test-02/    ← workspace for test-02
    │   └── report.md   ← suite report (written by reporter sub-agent)
    ├── run-02/
    └── ...
```

**To determine the next run ID:**

```bash
BASE=<MILESTONE_TESTS>/runs
last=$(ls -d "$BASE"/run-* 2>/dev/null | sort -V | tail -1 | grep -o '[0-9]*$')
next=$(printf "%02d" $(( ${last:-0} + 1 )))
echo "run-$next"
```

---

## Full Run Procedure

```text
1. Determine milestone and test directory
2. Compute next run ID
3. Setup: create run folder, copy test files into workspaces
4. Determine category for each test (read asserts.md header)
5. Run: spawn ALL orchestrator agents in parallel (all tests simultaneously, no tier ordering)
6. Wait for all orchestrators to complete
7. Assert: spawn ALL verifier agents in parallel
8. Wait for all verifiers to complete
9. Report: spawn reporter sub-agent (see report-rules.md)
```

**No sequential gating:** Tier 1, 2, 3, and 4 tests all run at the same time. There is no requirement for lower tiers to pass before higher tiers execute.

---

## Phase 1: Setup

For each test in the milestone:

```bash
MILESTONE_TESTS=<path-to-milestone>/tests
RUN_ID="run-XX"  # from run-ID logic above

# For each test-NN-<name>:
TEST="test-01-single-mono-haiku"
WORKSPACE="$MILESTONE_TESTS/runs/$RUN_ID/test-01"

mkdir -p "$WORKSPACE"
cp "$MILESTONE_TESTS/$TEST/blueprint.md" "$WORKSPACE/"

# If test has input/ folder, copy it too
if [ -d "$MILESTONE_TESTS/$TEST/input" ]; then
  cp -r "$MILESTONE_TESTS/$TEST/input" "$WORKSPACE/"
fi
```

Repeat for all tests. This is fast — run sequentially in bash.

---

## Phase 2: Determine Category

For each test, read the `Category:` line from `asserts.md`:

```bash
grep "^Category:" "$MILESTONE_TESTS/$TEST/asserts.md"
```

- `Category: End-to-End` → full run
- `Category: Workspace-only (dry-run)` → dry-run

---

## Phase 3.1: Pre-Run Snapshot

Before spawning any orchestrator agents, create `results.md` in each test's run folder with a pre-run snapshot:

```bash
WORKSPACE="$MILESTONE_TESTS/runs/$RUN_ID/test-NN"

# Write pre-run snapshot
cat > "$WORKSPACE/results.md" << EOF
# Results — test-NN

Run: $RUN_ID
Start: $(date -u +"%Y-%m-%dT%H:%M:%SZ")

## Pre-Run Folder Contents

$(find "$WORKSPACE" -type f | sort | sed "s|$WORKSPACE/||")

---

EOF
```

This captures the exact state of the workspace before the orchestrator touches it. The verifier will later append to this file.

---

## Phase 3.2: Run (Orchestrator Agents)

Spawn one agent per test, **all in parallel** (`run_in_background: true`).

### End-to-End Prompt

```text
Agent(
  description: "test-NN orchestrator (run-XX)",
  prompt: """
You are running example-skill for a test.

Invoke the skill:
/example-skill <WORKSPACE>/blueprint.md

Where <WORKSPACE> = <MILESTONE_TESTS>/runs/<RUN_ID>/test-NN

Follow the skill exactly. All output goes into the workspace.
When the skill completes (success or failure), report done.
""",
  run_in_background: true
)
```

### Workspace-only (Dry-Run) Prompt

```text
Agent(
  description: "test-NN orchestrator dry-run (run-XX)",
  prompt: """
You are running example-skill in dry-run mode for a test.

Invoke the skill:
/example-skill <WORKSPACE>/blueprint.md --dry-run

Where <WORKSPACE> = <MILESTONE_TESTS>/runs/<RUN_ID>/test-NN

Follow the skill exactly. All output goes into the workspace.
When the skill completes (success or failure), report done.
""",
  run_in_background: true
)
```

---

## Phase 4: Assert (Verifier Agents)

After ALL orchestrators complete, spawn one verifier per test, **all in parallel**.

### Verifier Prompt

```text
Agent(
  description: "test-NN verifier (run-XX)",
  prompt: """
You are verifying the results of a example-skill test.

Workspace: <MILESTONE_TESTS>/runs/<RUN_ID>/test-NN
Asserts file: <MILESTONE_TESTS>/test-NN-<name>/asserts.md

1. Read asserts.md — it defines what to check.
2. Check every assertion against the actual files in the workspace.
3. Write your results to: <MILESTONE_TESTS>/runs/<RUN_ID>/test-NN/results.md

Format of results.md (see test-rules.md for full spec):
- First line: `🟢 PASS: X/Y` or `🔴 FAIL: X/Y passed`
- Sections: ## Structural, ## Functional, ## Logs
- Each assertion: `- 🟢` pass, `- 🔴` fail (with reason after ` — `), `- 🟡` skipped
- End with: ## Observations

IMPORTANT: results.md is your ONLY output. Do not modify any other files.
""",
  run_in_background: true
)
```

---

## Phase 5: Report (Reporter Sub-Agent)

After ALL verifiers complete, spawn a reporter sub-agent.

**The reporter must receive `report-rules.md` as input.** See [`report-rules.md`](report-rules.md) for the exact prompt template, format, and rules.

The runner never writes the report directly.

---

## Copying Tests Between Milestones

When a new milestone builds on a previous one (e.g., M2 builds on M1), tests from the prior milestone should be copied forward and adapted.

### Procedure

1. **Identify which tests to carry forward** — foundational behavior tests (workspace structure, log format, planner mechanics) almost always apply to the next milestone
2. **Copy the test folder** into the new milestone's `tests/` directory:
   ```bash
   cp -r <old-milestone>/tests/test-NN-<name> <new-milestone>/tests/test-NN-<name>
   ```
3. **Adapt assertions** — update `asserts.md` for any behavioral changes in the new milestone (new log events, new file structures, new phase types, changed defaults)
4. **Renumber if needed** — tests in the new milestone should be sequentially numbered starting from `test-01`
5. **Update `test.md`** — the new milestone's test index must list all its tests (copied + new)
6. **Leave the old milestone untouched** — runs and test definitions in the source milestone are historical record

### What to Copy Forward

| Always copy | Never copy |
|-------------|------------|
| Workspace structure tests | Tests for deprecated/removed features |
| Log format verification | Tests whose assertions reference M<N>-only behavior |
| Multi-phase ordering | Tests that are fully superseded by new tests |
| Before/After copy mechanics | — |

### What to Adapt

After copying, review each `asserts.md` for:
- Log action names that may have changed
- New required files/folders that didn't exist before
- Changed defaults (model, effort)
- New phase types that affect orchestrator behavior

---

## Re-Running a Single Test

To re-run one test without running the full suite:

1. Use the same run-NN folder (or create a new run if preferred)
2. Re-run setup + orchestrator + verifier for just that test
3. Spawn a reporter sub-agent to update the report (or append a note)

---

## Token Usage Tracking

The runner captures usage stats from each agent's task-notification.

Token data is passed to the reporter sub-agent, which includes it in the report. See [`report-rules.md`](report-rules.md) for the exact format.

Collected from task-notification `<usage>` blocks:
- `subagent_tokens` — total tokens (includes nested agents)
- `tool_uses` — number of tool calls
- `duration_ms` — agent execution time

---

## Checklist Before Running

- [ ] Skill files exist at `~/.claude/skills/example-skill/`
- [ ] All test folders have `blueprint.md` and `asserts.md`
- [ ] `runs/` directory exists (create if not)
- [ ] No leftover state from a crashed run (check for incomplete `run-NN/` folders missing `report.md`)

---

## Cleaning Up

Delete all runs for a milestone:
```bash
rm -rf <MILESTONE_TESTS>/runs/run-*
```

Delete a specific run:
```bash
rm -rf <MILESTONE_TESTS>/runs/run-03
```
