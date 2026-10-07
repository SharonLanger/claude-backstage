# Implementation

> **Project overview:** See [`../README.md`](../README.md) for the full project guide, actors, and iteration lifecycle.
> **Iteration rules:** See [`../iteration-guide.md`](../iteration-guide.md) for versioning, review integration, and progression criteria.

All files in this project must follow the rules in [`../format.md`](../format.md).

---

## What is a Milestone?

A milestone is a self-contained deliverable that moves the skill from one capability level to the next. Each milestone produces a working state — when it's done, the skill can do something it couldn't do before.

---

## Milestone Folder Structure

Every milestone folder follows this layout:

```text
m<N>-<name>/
├── README.md          ← goal, scope, out-of-scope for this milestone
├── test.md            ← test index: lists all tests with category and description
├── results/
│   ├── results-run-01.md    ← compact failure summary per run
│   ├── results-run-02.md
│   └── results-summary.md   ← running overview table (updated each run)
└── tests/
    ├── test-01-<desc>/
    │   ├── blueprint.md   ← input to the skill (read-only)
    │   ├── asserts.md     ← assertions to verify (read-only)
    │   └── input/         ← optional pre-created files the blueprint references
    ├── test-02-<desc>/
    │   └── ...
    └── runs/
        ├── run-01/
        │   ├── test-01/   ← workspace for test-01
        │   ├── test-02/   ← workspace for test-02
        │   └── report.md  ← detailed report (see report-rules.md)
        └── run-02/
            └── ...
```

### Required Files Per Milestone

| File | Purpose |
|------|---------|
| `README.md` | Goal, scope, and out-of-scope boundaries |
| `test.md` | Index of all tests — category, number, short description |
| `tests/test-NN-<desc>/blueprint.md` | Input blueprint for the test |
| `tests/test-NN-<desc>/asserts.md` | Assertions to verify after the run |
| `results/results-summary.md` | Running overview table across all runs |

### Per-Run Output Files

| File | Purpose |
|------|---------|
| `tests/runs/<run-ID>/report.md` | Detailed report for this run |
| `results/results-<run-ID>.md` | Compact failure summary + observations |

### Optional Files

| File | Purpose |
|------|---------|
| `tests/test-NN-<desc>/input/` | Pre-created shared files referenced by the blueprint |

---

## Key Reference Files

| File | What it covers |
|------|----------------|
| [`test-rules.md`](test-rules.md) | Test structure, assertion layers, results format, categories, milestone promotion |
| [`runner-guide.md`](runner-guide.md) | Full run procedure, run-ID system, agent prompts, token tracking |
| [`report-rules.md`](report-rules.md) | Report creation rules — must be done by a sub-agent |

See section "Assertion Layers" in [`test-rules.md`](test-rules.md) for the required format of `asserts.md` files.

See section "Milestone Promotion" in [`test-rules.md`](test-rules.md) for rules on copying tests between milestones.

See section "Full Run Procedure" in [`runner-guide.md`](runner-guide.md) for how to execute a test suite.

See [`report-rules.md`](report-rules.md) for how test reports must be generated (always by a sub-agent).

---

## Milestones

### M1 — Mono Phase Skill

Create the skill with only the mono phase type. One phase, one agent, end-to-end: blueprint → main planner → orchestrator → mono agent → output. Includes logging from day one.

**Folder:** `m1-mono-phase-skill/`

---

### M2 — Your Next Milestone

Define your next milestone here. Each milestone adds a capability the skill could not do before.

**Folder:** `m2-your-next-milestone/`