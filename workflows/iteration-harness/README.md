# Multi-Agent Iteration Scaffold

A reusable framework for building AI skills using **milestone-based iteration** and the **theater model** (multi-agent coordination).

This scaffold contains **the process, not the product**. You bring your own skill — the scaffold provides the iteration system, agent roles, test infrastructure, review dimensions, and versioning rules to develop it systematically.

---

## What This Enables

1. **Define milestones** — incremental capability targets for your skill
2. **Write tests** — immutable after approval; the skill adapts to the tests, not the other way around
3. **Run the iteration loop** — test, reason, fix, re-test, review, decide
4. **Coordinate agents** — using the theater model (Director, Orchestrator, Leads, Cast)
5. **Track progress** — versions, decisions, and review findings over time

---

## Quick Start

1. **Create your skill** — write the skill files you want to iterate on (SKILL.md, actors, phase-types, etc.)
2. **Define M1** — edit `harness-core/implementation/m1-example/` with your first milestone's tests
3. **Lock the tests** — review and approve them (they become immutable)
4. **Run the iteration** — use `harness-core/implementation/runner-guide.md` to execute the loop
5. **Review** — after tests pass, run a multi-dimensional review using `harness-core/skill-review/`
6. **Advance** — when the Director approves, define M2 and repeat

---

## What You Bring

| You provide | Where it goes |
|-------------|---------------|
| Your skill spec files | Your own `skill/` directory (outside this scaffold) |
| Milestone test definitions | `harness-core/implementation/m1-*/tests/` |
| Approval decisions (gates) | You are the Director — you approve milestones and tests |

---

## What's Included

| Component | Purpose |
|-----------|---------|
| **Iteration Harness** (`harness-core/`) | The iteration engine — guides, rules, and format specs |
| **Roles** (`harness-core/roles/`) | 16 agent role definitions across 4 acts |
| **Implementation** (`harness-core/implementation/`) | Milestone structure, test rules, runner guide, report rules |
| **Skill Review** (`harness-core/skill-review/`) | Review checklists, criteria, and scoring dimensions |
| **Example Milestone** (`harness-core/implementation/m1-example/`) | 2 mock tests showing the expected test structure |
| **Mock Examples** (`*-mock.md` files) | Sample outputs showing what each stage of the iteration produces |
| **Docs** (`harness-core/docs/`) | Methodology documentation — algorithm, theater model, patterns, walkthrough |

> All files with a `-mock` suffix are example templates showing the format and content generated during the iteration process. They demonstrate what the Reasoner, Reviewer, and other agents write at each stage. Replace them with real data from your own runs.

---

## The Theater Model

Agents are organized into **Acts**, each with a Lead and Cast members:

| Act | Lead | Cast | Purpose |
|-----|------|------|---------|
| **act-test-runner** | Orchestrator | Runner, Verifier, Reporter | Execute tests and report results |
| **act-skill-change** | Skill-Change-Agent | Backup | Apply fixes with versioning |
| **act-review** | Review-Skill | Dimension Reviewer, Protocol Verifier, Synthesis | Multi-dimensional quality review |
| **act-reasoning** | Reasoner | Comparator | Root-cause analysis and fix decisions |

The **Director** (you) approves milestone gates. The **Main Agent** orchestrates the full iteration loop.

---

## File Tree

```
example/
├── README.md                                          ← you are here
└── harness-core/                                 ← the iteration engine
    ├── README.md                                      ← harness overview, acts & actors
    ├── iteration-guide.md                             ← iteration flow, versioning, delta rules
    ├── iteration-status.md                            ← mock: current state, what's next, cycle diagram
    ├── format.md                                      ← formatting rules for all outputs
    ├── docs/                                          ← methodology documentation
    │   ├── README.md                                  ← reading order + index
    │   ├── iteration-algorithm.md                     ← 9-step iteration loop + Mermaid flow diagram
    │   ├── theater-model.md                           ← agent hierarchy, acts, roles, milestones
    │   ├── walkthrough.md                             ← end-to-end guided tour connecting mock files
    │   ├── version-evolution.md                       ← how versions evolve, typical progression
    │   └── design-patterns.md                         ← 35 patterns, 8 principles, 9 anti-patterns
    ├── decisions/                                     ← decision files (written by Reasoner at runtime)
    │   ├── README.md
    │   ├── decision-m1-test-failure-mock.md           ← mock: Reasoner analyzes test failures
    │   └── decision-m1-review-findings-mock.md        ← mock: Reasoner analyzes review findings
    ├── skill/                                         ← fix instructions (written by Reasoner at runtime)
    │   ├── README.md
    │   └── fix-01-restore-execution-loop-mock.md      ← mock: fix instruction with root cause + change
    ├── roles/                                         ← 16 agent role definitions
    │   ├── act-test-runner/                            ← test execution act (5 roles)
    │   │   ├── act-test-runner.md                     ← act overview + dispatch
    │   │   ├── orchestrator.md                        ← coordinates test execution
    │   │   ├── runner.md                              ← executes individual tests
    │   │   ├── verifier.md                            ← validates test results
    │   │   └── reporter.md                            ← formats test reports
    │   ├── act-skill-change/                          ← skill modification act (3 roles)
    │   │   ├── act-skill-change.md                    ← act overview + dispatch
    │   │   ├── skill-change.md                        ← applies fixes to skill files
    │   │   └── backup.md                              ← manages version backups
    │   ├── act-review/                                ← quality review act (5 roles)
    │   │   ├── act-review.md                          ← act overview + dispatch
    │   │   ├── review-skill.md                        ← review lead
    │   │   ├── dimension-reviewer.md                  ← scores one dimension
    │   │   ├── protocol-verifier.md                   ← checks inter-agent contracts
    │   │   └── synthesis.md                           ← combines findings into scorecard
    │   └── act-reasoning/                             ← analysis act (3 roles)
    │       ├── act-reasoning.md                       ← act overview + dispatch
    │       ├── reasoner.md                            ← root-cause analysis + fix instructions
    │       └── comparator.md                          ← compares version variations
    ├── implementation/                                ← milestone structure + execution rules
    │   ├── README.md                                  ← milestone index
    │   ├── runner-guide.md                            ← 5-phase run procedure
    │   ├── test-rules.md                              ← test structure, assertion layers, scoring
    │   ├── report-rules.md                            ← reporter output format
    │   └── m1-example/                                ← example milestone with 2 mock tests
    │       ├── README.md                              ← milestone description
    │       ├── test.md                                ← test index
    │       ├── results/
    │       │   ├── results-summary.md                 ← mock: run summary table with progression
    │       │   ├── results-run-01-mock.md             ← mock: run-01 (1/2 tests, execution failure)
    │       │   └── results-run-02-mock.md             ← mock: run-02 (2/2 tests, all green after fix)
    │       └── tests/
    │           ├── test-01-single-phase/
    │           │   ├── blueprint.md                   ← test scenario
    │           │   └── asserts.md                     ← 3-layer assertions
    │           └── test-02-multi-phase/
    │               ├── blueprint.md                   ← test scenario
    │               └── asserts.md                     ← 3-layer assertions
    └── skill-review/                                  ← review infrastructure
        ├── tasks.md                                   ← review task definitions
        ├── m1/                                        ← mock review outputs for M1
        │   ├── review-results-mock.md                 ← mock: scorecard (52/80), priority fixes, verdict
        │   ├── d2-ssot-review-mock.md                 ← mock: D2 dimension review (5/10)
        │   ├── d7-restrictions-review-mock.md         ← mock: D7 dimension review (6/10)
        │   └── checklist-m1-mock.md                   ← mock: review checklist across all 8 dimensions
        └── resources/
            ├── checklist-universal.md                 ← universal review checklist
            ├── checklist-template.md                  ← milestone checklist template
            ├── criteria.md                            ← scoring criteria per dimension
            └── anti-patterns.md                       ← mock: anti-pattern catalog with 5 example entries
```

---

## What Is NOT Included

| Category | Why | Mock example provided? |
|----------|-----|------------------------|
| **Skill files** | The skill is the *product* of the process. You create your own. | No |
| **Skill backups** | Created by the iteration process. Backup rules are in `iteration-guide.md`. | No |
| **Run outputs** | Generated by running the iteration loop. | Yes — results summary + 2 run results in `harness-core/implementation/m1-example/results/` |
| **Decision files** | Written by the Reasoner during runs. | Yes — 2 mock decisions in `harness-core/decisions/` |
| **Fix instructions** | Written by the Reasoner, consumed by Skill-Change-Agent. | Yes — 1 mock fix in `harness-core/skill/` |
| **Review findings** | Output of actual review runs. | Yes — scorecard, 2 dimension reviews, checklist in `harness-core/skill-review/m1/` |

---

## Key Concepts

- **Immutable tests** — once approved, tests cannot be modified. The skill adapts to the tests.
- **Versioned fixes** — every change is backed up. Multiple variations can be tried in parallel.
- **Delta acceptance** — not every finding is worth fixing. Explicit thresholds prevent unnecessary churn.
- **8 review dimensions** — structural clarity, SSOT, token efficiency, flow coherence, scenario completeness, contract stability, restriction consistency, extensibility.
- **Files as interfaces** — agents communicate through files, not prompts. Every agent reads and writes structured artifacts.
- **Separation of concerns** — the test-runner can't edit skills; the skill-changer can't run tests.

---

## Customization Guide

| What to customize | How |
|-------------------|-----|
| Milestone tests | Replace `m1-example/` tests with your own scenarios |
| Review dimensions | Adjust weights in `skill-review/resources/criteria.md` |
| Anti-patterns | Add entries to `skill-review/resources/anti-patterns.md` as you discover them |
| Additional milestones | Create `m2-*/`, `m3-*/` folders following the M1 structure |
| Role behavior | Role files are the source of truth — edit boundaries and rules as needed |
