# Act: act-test-runner

Every actor in this act MUST load this file first.

---

## Purpose

Run the milestone's test suite and produce structured results. This act does NOT fix anything — it observes and reports.

---

## Shared Rules (all actors in this act)

1. You are NOT allowed to modify `~/.claude/skills/example-skill/` or any `.claude/` project files.
2. You are NOT allowed to modify test files (`blueprint.md`, `asserts.md`, `input/`). Tests are locked after the Director approves them.
3. You are NOT allowed to modify the workspace output of other actors in this act.
4. Never pass task details in sub-agent prompts — point actors to their role file.
5. All actors: Model = opus, Effort = high.

---

## Actors

| Role | Actor | File | Spawned By |
|------|-------|------|-----------|
| Lead | Runner Agent | `runner.md` | Main Agent |
| Cast | Orchestrator | `orchestrator.md` | Runner Agent |
| Cast | Verifier | `verifier.md` | Runner Agent |
| Cast | Reporter | `reporter.md` | Runner Agent |

---

## Flow

```text
Runner (Lead)
  ├── spawns Orchestrator (one per test, ALL IN PARALLEL) → runs skill, produces workspace
  ├── spawns Verifier (one per test, IMMEDIATELY after ITS orchestrator completes) → checks workspace against asserts.md
  └── spawns Reporter (once, after ALL verifiers complete) → writes summary reports
```

**Parallelism rules:**
- All Orchestrators run concurrently.
- Verifier-X starts as soon as Orchestrator-X finishes. It does NOT wait for other Orchestrators.
- The Reporter waits for all Verifiers to complete.
- The Runner (Lead) does NOT need to read full sub-agent output. It only needs: done + status (PASS/FAIL + score).

---

## Inputs

| Input | Source |
|-------|--------|
| Test definitions | `implementation/<milestone>/tests/test-NN-*/blueprint.md` |
| Assertion specs | `implementation/<milestone>/tests/test-NN-*/asserts.md` |
| Run procedure | `implementation/runner-guide.md` |
| Result format | `implementation/test-rules.md` |
| Report format | `implementation/report-rules.md` |

---

## Outputs

| Output | Location |
|--------|----------|
| Per-test results | `implementation/<milestone>/tests/test-NN-*/results.md` |
| Summary report | Per `implementation/report-rules.md` |

---

## Reference Files

These files define HOW this act works. The Lead (Runner) must read them before spawning cast.

| File | What it covers | Who reads it |
|------|----------------|--------------|
| `implementation/runner-guide.md` | Full 5-phase run procedure, run-ID system, token tracking | Runner (Lead) |
| `implementation/test-rules.md` | Test structure, assertion layers (structural/functional/logs), results.md format, categories | Runner + Verifier |
| `implementation/report-rules.md` | Three report output files, format rules | Reporter |
| `implementation/<milestone>/tests/test-NN-*/blueprint.md` | Per-test input definition | Orchestrator |
| `implementation/<milestone>/tests/test-NN-*/asserts.md` | Per-test expected output | Verifier |

---

## Boundaries

- This act produces results. It does NOT decide what to do with them.
- After this act completes, `act-reasoning` reads the results and decides next steps.
- If a test looks wrong (impossible to satisfy), STOP and tell the Runner, who escalates to the Director.
