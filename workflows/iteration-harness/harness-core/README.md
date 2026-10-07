# Multi-Agent Runner — Production Guide

Iteratively develop and test the `example-skill` skill using structured milestones, automated testing, and review cycles.

---

## Top Rule — All Agents

```
You are NOT allowed to modify ~/.claude/skills/example-skill/ or any .claude/ project files.
Only the skill-change-agent has this permission.
Put this rule at the TOP of every sub-agent you spawn.
```

---

## Hard Rule — Tests Are Immutable

```
After the Director approves test definitions (Step 1 of the iteration),
NO agent may modify test files (blueprint.md, asserts.md, input/).

Tests are LOCKED. If you believe a test is wrong — STOP and tell the Director.
She is the only one who can change tests after approval.
```

---

## Communication Rule — All Agents

```
Never pass task details in agent prompts.
Instead, point agents to their role file:

  "You are the <role> agent for <act>.
   Read <act-file-path> first, then read <role-file-path>."

Files are the interface between actors. Prompts are 1-2 sentences max.
Each actor loads: act file → role file. In that order.
```

---

## Theater Model

This project uses a theater metaphor for its multi-agent structure:

| Term | Meaning |
|------|---------|
| **Theater** | The entire multi_agent_runner repo |
| **Director** | the Director — approves gates, makes all final decisions |
| **Main Agent** | The session-level Claude agent that the Director interacts with. It spawns Lead actors as sub-agents and coordinates the iteration cycle. |
| **Act** | A group of actors collaborating on one job (e.g., running tests) |
| **Lead** | The main actor in an act — spawned by the Main Agent, orchestrates the work, spawns cast |
| **Cast** | Sub-actors spawned by the lead to do specific tasks |

### Main Agent Responsibilities

The Main Agent is the orchestrator between acts. It:

1. **Spawns Lead actors** — each Lead is a sub-agent spawned by the Main Agent
2. **Reads act outputs** — after a Lead completes, the Main Agent reads its output
3. **Decides which act runs next** — based on the iteration cycle (test → reason → fix → review)
4. **Stops at GATEs** — presents results to the Director and waits for approval
5. **Never does the work itself** — delegates ALL execution to Lead sub-agents

The Main Agent prompt for spawning a Lead is minimal:
```
"You are the <Lead role> agent for <act>.
 Read <act-file-path> first, then read <role-file-path>.
 <1 sentence context: what milestone, what run-ID, what inputs are ready>"
```

---

## Acts — Concept

An **act** is a self-contained unit of work performed by a group of agents. It has:

| Property | Description |
|----------|-------------|
| **Purpose** | One job (e.g., "run tests", "fix skill", "review skill") — an act does exactly one thing |
| **Lead** | The main actor — orchestrates the work, spawns cast, reports up to the Director |
| **Cast** | Sub-actors spawned by the lead for specific tasks (verifier, reporter, etc.) |
| **Act file** | `act-<name>.md` — shared rules ALL actors in the act load FIRST, before their own role file |
| **Role files** | Per-actor instructions — what it can/cannot do, inputs, outputs |
| **Boundaries** | An act produces output but does NOT decide what to do with it — the next act or the Director decides |

### Loading Order

Every actor loads files in this order:

```
1. Act file (act-<name>.md)    ← shared rules, flow diagram, actor table
2. Role file (<role>.md)       ← specific instructions for this actor
3. Reference files             ← test-rules.md, report-rules.md, etc.
```

### Spawning Rule

Agents never receive task details in their prompt. Instead, the spawner points them to files:

```
"You are the <role> agent for <act>.
 Read <act-file-path> first, then read <role-file-path>."
```

Files are the interface between actors. Prompts are 1-2 sentences max.

### Relationship to the Theater

```
Theater (multi_agent_runner)
└── Director: the Director — gates, decisions, test approval
    └── Main Agent (session Claude) — spawns Leads, coordinates iteration
        ├── act-test-runner    → Runner Agent (Lead) → spawns cast
        ├── act-reasoning      → Reasoner (Lead) → spawns cast
        ├── act-skill-change   → Skill-Change-Agent (Lead) → spawns cast
        └── act-review         → Review Skill Agent (Lead) → spawns cast
```

Acts run sequentially in the iteration cycle. The Main Agent spawns each Lead, reads its output, then spawns the next. the Director sits between acts at gates.

---

## Acts & Actors

All actors run with **Model: opus, Effort: high**.

| Act | Role | Actor | Spawned By | Can Do | Cannot Do |
|-----|------|-------|-----------|--------|-----------|
| — | — | **Main Agent** | (session) | Spawn Leads, read outputs, coordinate iteration, stop at GATEs | Do the work itself, edit skill/test files |
| **act-test-runner** | Lead | Runner Agent | Main Agent | Execute test suites, spawn cast, track results | Edit skill files, edit tests, run reviews |
| -- | Cast | Orchestrator | Runner Agent | Invoke `/example-skill` for one test | Edit skill files, edit tests, spawn sub-agents |
| -- | Cast | Verifier | Runner Agent | Read workspace + asserts.md, produce results.md | Edit skill/test files, edit workspace, spawn sub-agents |
| -- | Cast | Reporter | Runner Agent | Read all results, write report files | Edit anything else, spawn sub-agents |
| **act-skill-change** | Lead | Skill-Change-Agent | Main Agent | Modify `~/.claude/skills/example-skill/**`, create version backups | Run tests, run reviews, edit tests |
| -- | Cast | Backup Agent | Skill-Change-Agent | Copy skill folder to `backups/V<N>/` | Edit skill files, run tests, spawn sub-agents |
| **act-review** | Lead | Review Skill Agent | Main Agent | Orchestrate review, spawn dimension/protocol/synthesis cast | Edit skill files, edit tests |
| -- | Cast | Dimension Reviewer | Review Skill Agent | Score one dimension (D1-D8) per criteria | Edit files, spawn sub-agents, score other dimensions |
| -- | Cast | Protocol Verifier | Review Skill Agent | Check inter-actor protocol consistency | Edit files, spawn sub-agents |
| -- | Cast | Synthesis Agent | Review Skill Agent | Combine scores + findings → scorecard + verdict | Edit files, spawn sub-agents, override scores |
| **act-reasoning** | Lead | Reasoner | Main Agent | Analyze results, write decisions + fix instructions | Edit skill files, edit tests, run tests/reviews |
| -- | Cast | Comparator | Reasoner | Compare N versions → comparison matrix | Edit files, spawn sub-agents, make decisions |
| **Director** | — | the Director | — | Approve gates, change tests, override any decision | — |

### Role Files

Each act has an `act-<name>.md` file that defines shared rules for all actors in that act. Every actor MUST load their act file first. Each actor also has their own role file with specific instructions.

```text
roles/
├── act-test-runner/
│   ├── act-test-runner.md ← Act definition (all actors load this FIRST)
│   ├── runner.md          ← Lead
│   ├── orchestrator.md    ← Cast
│   ├── verifier.md        ← Cast
│   └── reporter.md        ← Cast
├── act-skill-change/
│   ├── act-skill-change.md ← Act definition
│   ├── skill-change.md     ← Lead
│   └── backup.md           ← Cast
├── act-review/
│   ├── act-review.md       ← Act definition
│   ├── review-skill.md     ← Lead
│   ├── dimension-reviewer.md ← Cast
│   ├── protocol-verifier.md  ← Cast
│   └── synthesis.md          ← Cast
└── act-reasoning/
    ├── act-reasoning.md   ← Act definition
    ├── reasoner.md        ← Lead
    └── comparator.md      ← Cast
```

---

## Priority Guide

When deciding what to fix, in this order:

1. **Correctness** — the skill must produce correct output
2. **Robustness** — make the skill scalable and reliable (keep it easy to change)
3. **Token savings** — reduce unnecessary token consumption

---

## Project Structure

```text
harness-core/
├── README.md                    ← this file (production guide)
├── iteration-guide.md           ← iteration lifecycle, versioning, review rules
├── iteration-status.md          ← mock: current iteration state, what's next, cycle diagram
├── roles/                       ← role files per act/actor
│   ├── act-test-runner/
│   ├── act-skill-change/
│   ├── act-review/
│   └── act-reasoning/
├── skill/                       ← fix instruction files (input for skill-change-agent)
├── decisions/                   ← decision files written by reasoner
├── implementation/
│   ├── README.md                ← milestone folder structure, required files per MT
│   ├── runner-guide.md          ← full test run procedure (5 phases)
│   ├── test-rules.md            ← assertion format, results format, categories
│   ├── report-rules.md          ← 3 report output files, reporter agent rules
│   ├── m1-mono-phase-skill/     ← milestone 1
└── skill-review/
    └── m1/                      ← review criteria, dimensions, checklists, results
```

---

## Key References

| File | What it covers |
|------|----------------|
| [`iteration-guide.md`](iteration-guide.md) | Full iteration lifecycle: test → fix → review → decide. Versioning system (V2, V2.1). Progression criteria. |
| [`roles/`](roles/) | Role files per actor — the full instructions each agent receives when spawned |
| [`implementation/README.md`](implementation/README.md) | Milestone folder structure, required files per MT, milestone list |
| [`implementation/runner-guide.md`](implementation/runner-guide.md) | How to run tests: 5-phase procedure, run-ID system, agent prompts, token tracking |
| [`implementation/test-rules.md`](implementation/test-rules.md) | Test structure, assertion layers (structural/functional/logs), results format, categories |
| [`implementation/report-rules.md`](implementation/report-rules.md) | Three report output files (report.md, results-X.md, results-summary.md), reporter agent prompt |
| [`skill-review/`](skill-review/) | Review criteria (8 dimensions, scoring rubric), checklists, review task definition (`tasks.md`) |

---

## The Skill Under Development

- **Skill:** `example-skill`
- **Location:** `~/.claude/skills/example-skill/`
- **What it does:** Multi-phase workflow executor — reads a blueprint, creates a workspace, runs phases sequentially via sub-agents
- **Current version:** See `~/.claude/skills/example-skill/backups/` for version history

---

## How an Iteration Works (Summary)

See [`iteration-guide.md`](iteration-guide.md) for full details.

```text
1. the Director verifies test definitions are correct ← TESTS LOCKED AFTER THIS
2. Main Agent spawns Runner Agent → runs tests → results
3. Tests fail? → Main Agent spawns Reasoner → analyzes, writes fix instructions to skill/
4. Main Agent spawns Skill-Change-Agent → fixes (with versioning)
5. Main Agent spawns Runner Agent again → re-runs tests
6. Tests pass? → Main Agent spawns Review Skill Agent → full skill review
7. Main Agent spawns Reasoner → evaluates findings (delta acceptance rules)
8. Critical findings? → Main Agent spawns Skill-Change-Agent → fixes (only important ones)
9. No critical findings? → [GATE] Main Agent presents results, the Director approves milestone progression
```

**Key rules:**
- The Main Agent spawns ALL Lead actors — Leads never spawn each other
- Tests are LOCKED after the Director approves them (Step 1) — no agent may modify tests
- If you think a test is wrong: STOP and tell the Director
- If something isn't working after 3 attempts: STOP and explain
- If you're unsure about a design decision: STOP and ask
- the Director is always here
