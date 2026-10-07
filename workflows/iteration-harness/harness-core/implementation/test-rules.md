# Test Rules — example-skill

---

## Test Structure

Every test folder must contain:

| File | Required | Description |
|------|----------|-------------|
| `blueprint.md` | yes | The input to the skill (same format as production usage) |
| `asserts.md` | yes | Assertions to verify after the run |
| `input/` | no | Pre-created shared files the blueprint references |

Source files (`blueprint.md`, `asserts.md`, `input/`) are **read-only** — never modified by the skill or runner.

```text
tests/
├── test-01-<description>/
│   ├── blueprint.md
│   ├── asserts.md
│   └── input/           ← optional
├── test-02-<description>/
│   ├── blueprint.md
│   └── asserts.md
└── ...
```

---

## Test Categories

### End-to-End

Full skill execution: `blueprint.md` → main planner → orchestrator → phase agents → output.

Invocation: `/example-skill <workspace>/blueprint.md`

Use when verifying that agents produce correct output and the full pipeline works.

### Workspace-only (dry-run)

Planner-only execution: creates workspace structure, planner.md, briefings, but spawns no phase agents.

Invocation: `/example-skill <workspace>/blueprint.md --dry-run`

Use when verifying workspace creation, planner behavior, and spec content without executing phases.

### Determining Category

The runner reads the category from the `asserts.md` header:

```md
# Asserts — Test NN — <Description>

Category: End-to-End
```

or:

```md
# Asserts — Test NN — <Description>

Category: Workspace-only (dry-run)
```

---

## Assertion Layers

Assertions in `asserts.md` are organized into three sections, in this order:

### 1. Structural (always required)

Verify the workspace filesystem was created correctly.

```md
## Structural

- `planner.md` exists
- `p1/` exists
- `p1/briefing.md` exists
- `p1/input/` exists
- `p1/output/` exists
```

### 2. Functional

Verify content inside spec files and output files.

```md
## Functional

### planner.md

- Phase order: P1
- P1 type = mono
- P1 model = haiku
- P1 effort = low

### p1/output/haiku.md

- File exists
- File is not empty
- Content is a haiku (3 lines)
```

### 3. Logs (Advisory — Yellow Severity)

Verify log files exist and contain expected entries.

**Log assertions are advisory (🟡), not critical (🔴).** They verify observability, not correctness. A missing or differently-named log action does NOT fail a test.

Rules for log assertion evaluation:
- **Same meaning = PASS.** If the log contains an action with the same semantic meaning as expected (e.g., `plan-ready` instead of `planner-spawned` — both mean "planner finished"), mark it 🟢.
- **Missing log = 🟡 (yellow).** A missing log entry is marked 🟡, not 🔴. It counts toward the advisory total, not the pass/fail total.
- **Log file missing entirely = 🔴.** If the log FILE doesn't exist at all, that's structural and is a real failure.
- **Pattern detection (Reporter).** If many tests show the same missing log action, the Reporter flags it as a potential issue. If only some tests miss it, it's LLM non-determinism and acceptable.

```md
## Logs

### logs/orchestrator.log

- File exists
- Contains action: `started`
- Contains action: `planner-spawned`
- Contains action: `workflow-end`
```

---

## Results File Format (`results.md`)

After verifying assertions, the verifier writes `results.md` inside the test's run folder. This is the **only output** of the verifier.

### Format

```md
🟢 PASS: X/Y

## Structural

- 🟢 `planner.md` exists
- 🟢 `p1/` exists
- 🔴 `p1/output/` exists — DIRECTORY MISSING

## Functional

- 🟢 Phase order: P1
- 🟢 P1 model = haiku
- 🔴 Content is a haiku (3 lines) — found 5 lines

## Logs

- 🟢 Contains action: `started`
- 🔴 Contains action: `workflow-end` — NOT FOUND

## Observations

- 1 structural failure: output directory missing
- Phase agent may not have executed
```

### Markers

| Marker | Meaning |
|--------|---------|
| `🟢` | Assertion passed |
| `🔴` | Assertion failed — include brief reason after ` — ` |
| `🟡` | Advisory miss (log assertions) — not counted as failure |

### Scoring

- **Pass/Fail count** uses only 🟢 and 🔴 markers. 🟡 markers are tracked separately.
- **Summary line** reports: `X/Y` where Y = structural + functional assertions only.
- **Advisory line** (optional): `Advisory: A/B log assertions passed` — shown after the summary line if any 🟡 exist.

### Summary Line

First line of the file, one of:
- `🟢 PASS: X/Y` — all structural + functional assertions passed
- `🔴 FAIL: X/Y passed` — at least one structural/functional assertion failed

Second line (if any log assertions were advisory):
- `🟡 Advisory: A/B log checks passed`

### Rules

- One assertion per line, as a markdown list item (`- 🟢 ...`, `- 🔴 ...`)
- Group by section headers (`## Structural`, `## Functional`, `## Logs`)
- Failed assertions MUST include a brief reason after ` — `
- End with `## Observations` section
- **Never use `[x]`/`[ ]` checkboxes** — always use colored markers
- **Every assertion line must start with `- `** (markdown list)

---

## Milestone Scoping

- Tests belong to a milestone (e.g., `m1-mono-phase-skill/tests/`)
- The runner targets one milestone at a time
- Run artifacts live under `<milestone>/tests/runs/run-NN/`
- After moving to the next milestone, previous milestone tests are historical — not re-run

---

## Milestone Promotion

When advancing from M<N> to M<N+1>:

1. **Identify reusable tests** — tests verifying foundational behavior (workspace structure, log format, planner mechanics) likely still apply
2. **Copy forward** — duplicate relevant test folders into the new milestone's `tests/` directory
3. **Adapt** — update assertions for any new/changed behavior in the new milestone (new log events, new file structures, new phase types)
4. **Add new tests** — write tests for the new milestone's unique capabilities
5. **Update test.md** — the new milestone's test index reflects all its tests (copied + new)
6. **Old runs stay** — `m1/tests/runs/` is never deleted; it's the historical record of M1 verification

### What to Copy Forward

| Always copy | Never copy |
|-------------|------------|
| Workspace structure tests | Tests for deprecated/removed features |
| Log format verification | Tests whose assertions reference M<N>-only behavior |
| Multi-phase ordering | — |
| Before/After copy mechanics | — |

---

## General Rules

- All tests use cheap models: phase agents = haiku/low, planner = haiku or sonnet
- Exception: tests specifically verifying model/effort override use their specified values
- Every test must have the Structural section — no exceptions
- Test numbering is sequential within a milestone: `test-01`, `test-02`, etc.
- Test folder naming: `test-NN-<short-description>/`
- Blueprints must be trivially simple — test the orchestration, not domain work

---

## Phase I/O Rules (CRITICAL)

Phase I/O assertions are **critical** — they represent the core contract of the skill. If I/O breaks, nothing works.

### Mandatory I/O Tests Per Milestone

Every milestone MUST include:

1. **At least one I/O output file test** — verifies that phase agents write the expected files to `output/`
2. **At least one I/O chaining test** — verifies that output from phase N correctly arrives as input to phase N+1
3. **At least one I/O arithmetic/content verification test** — verifies that downstream phases correctly USE input data (not just that files exist)

### I/O Assertion Subsections

When writing assertions for tests involving phase I/O, use these subsections under `## Functional`:

| Subsection | When to use | What to verify |
|-----------|-------------|----------------|
| `### Phase I/O — Output Files (CRITICAL)` | E2E tests | Each expected output file exists, is not empty, contains valid content |
| `### Phase I/O — Input Chain (CRITICAL)` | E2E tests with Before copy | Each input file exists, is not empty, matches the source output file |
| `### Phase I/O — Arithmetic/Content Verification (CRITICAL)` | E2E tests with cumulative data | Downstream output is mathematically/logically correct given inputs |
| `### Phase I/O Documentation (CRITICAL)` | Dry-run tests | planner.md documents outputs, briefings reference correct I/O files |
| `### Phase I/O Chain Documentation (CRITICAL)` | Dry-run tests with Before copy | planner.md documents all copy instructions, source/dest match |

### Rules

1. **Every phase with an Output section in the blueprint** → assert the output file exists and is not empty (E2E) or is documented in planner.md (dry-run)
2. **Every Before copy instruction** → assert the input file exists and matches the source (E2E) or is documented in planner.md (dry-run)
3. **Every chained phase** → verify the data flows correctly: input content matches the upstream output content
4. **Mark all I/O assertions with `(CRITICAL)`** in the section header
5. **I/O failures are never "acceptable"** — they indicate a broken core contract, not LLM non-determinism
6. **Dry-run tests verify documentation** — since phases don't execute, verify that planner.md and briefings correctly document what would happen
7. **E2E tests verify actual files** — verify the real files exist with correct content after execution
