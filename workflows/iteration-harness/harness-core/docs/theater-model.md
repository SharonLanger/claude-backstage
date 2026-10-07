# Theater Model

A multi-agent coordination pattern using a theater metaphor. Each agent has a defined role, clear boundaries, and communicates through files — not context.

---

## 1. The Hierarchy

```
Director (human)
└── Main Agent (orchestrator)
    ├── Act 1 → Lead → Cast members
    ├── Act 2 → Lead → Cast members
    └── Act N → Lead → Cast members
```

| Role | What it does |
|------|-------------|
| **Director** | Human. Approves gates, makes final decisions, owns test definitions. |
| **Main Agent** | Session-level agent. Spawns leads, reads outputs, decides what runs next. Never does the work itself. |
| **Lead** | One per act. Orchestrates the work, spawns cast, reports results upward. |
| **Cast** | Workers spawned by a lead for specific tasks (verify, report, compare, etc.). |

The Main Agent is the orchestrator between acts. It spawns Lead actors as sub-agents, reads their output when they complete, decides which act runs next based on the iteration cycle, and stops at gates for human approval. It never does the work itself — all execution is delegated to Leads and their Cast.

---

## 2. Acts

An **act** is one unit of work — a group of agents doing one job.

| Property | Rule |
|----------|------|
| **Purpose** | One job per act (test, reason, fix, review) |
| **Boundaries** | An act produces output but never decides what happens next |
| **Act file** | Shared rules all actors in the act load first (`act-<name>.md`) |
| **Role files** | Per-actor instructions — what the actor can and cannot do |

Every actor loads files in this order: act file, then role file, then any reference files.

### Acts in This Scaffold

| Act | Lead | Cast | Purpose | Folder |
|-----|------|------|---------|--------|
| **act-test-runner** | Orchestrator | Runner, Verifier, Reporter | Execute tests, report results | `roles/act-test-runner/` |
| **act-skill-change** | Skill-Change-Agent | Backup | Apply fixes with versioning | `roles/act-skill-change/` |
| **act-review** | Review-Skill | Dimension Reviewer, Protocol Verifier, Synthesis | Multi-dimensional quality review | `roles/act-review/` |
| **act-reasoning** | Reasoner | Comparator | Root-cause analysis, fix decisions | `roles/act-reasoning/` |

Acts run sequentially in the iteration cycle. The Main Agent spawns each Lead, reads its output, then spawns the next. The Director sits between acts at gates.

### Full Acts & Actors Table

All actors run with **Model: opus, Effort: high**.

| Act | Role | Actor | Spawned By | Can Do | Cannot Do |
|-----|------|-------|-----------|--------|-----------|
| — | — | **Main Agent** | (session) | Spawn Leads, read outputs, coordinate iteration, stop at GATEs | Do the work itself, edit skill/test files |
| **act-test-runner** | Lead | Runner Agent | Main Agent | Execute test suites, spawn cast, track results | Edit skill files, edit tests, run reviews |
| -- | Cast | Orchestrator | Runner Agent | Invoke the skill for one test | Edit skill files, edit tests, spawn sub-agents |
| -- | Cast | Verifier | Runner Agent | Read workspace + asserts.md, produce results.md | Edit skill/test files, edit workspace, spawn sub-agents |
| -- | Cast | Reporter | Runner Agent | Read all results, write report files | Edit anything else, spawn sub-agents |
| **act-skill-change** | Lead | Skill-Change-Agent | Main Agent | Modify skill files, create version backups | Run tests, run reviews, edit tests |
| -- | Cast | Backup Agent | Skill-Change-Agent | Copy skill folder to `backups/V<N>/` | Edit skill files, run tests, spawn sub-agents |
| **act-review** | Lead | Review Skill Agent | Main Agent | Orchestrate review, spawn dimension/protocol/synthesis cast | Edit skill files, edit tests |
| -- | Cast | Dimension Reviewer | Review Skill Agent | Score one dimension (D1-D8) per criteria | Edit files, spawn sub-agents, score other dimensions |
| -- | Cast | Protocol Verifier | Review Skill Agent | Check inter-actor protocol consistency | Edit files, spawn sub-agents |
| -- | Cast | Synthesis Agent | Review Skill Agent | Combine scores + findings → scorecard + verdict | Edit files, spawn sub-agents, override scores |
| **act-reasoning** | Lead | Reasoner | Main Agent | Analyze results, write decisions + fix instructions | Edit skill files, edit tests, run tests/reviews |
| -- | Cast | Comparator | Reasoner | Compare N versions → comparison matrix | Edit files, spawn sub-agents, make decisions |
| **Director** | — | The Director (human) | — | Approve gates, change tests, override any decision | — |

---

## 3. Core Rules

### Files are the interface

Agents communicate through files, not through context or long prompts. A spawner writes a file; the spawned agent reads it.

### Prompts are minimal

One to two sentences pointing to files:

```
"You are the <role> agent for <act>.
 Read <act-file> first, then <role-file>."
```

Context lives in files, not in the spawn prompt. This keeps agent launches cheap and deterministic — the same role file produces the same behavior regardless of who spawns it.

### Separation of concerns

Each agent has explicit can-do and cannot-do boundaries:

- The test-runner cannot edit the skill
- The skill-changer cannot run tests
- The reasoner cannot do either
- Only the Director can modify tests after approval

### Gates control flow

| Gate type | Who passes it | When |
|-----------|--------------|------|
| **Human gate** | Director only | Hard stop — the agent presents results and waits for explicit approval |
| **Checklist gate** | Agent (automated) | The agent self-validates a checklist before proceeding to the next phase |

---

## 4. Milestones

Development is split into milestones. Each milestone adds one new capability. They run in order — a milestone must fully pass before the next one starts.

### Two phases per milestone

1. **Make it work** — get all tests passing. The iteration cycle (test, reason, fix, re-test) runs until the full test suite is green. The focus is correctness.
2. **Make it better** — once tests pass, a full review runs. The review scores across multiple dimensions and the reasoner decides what is worth improving using delta acceptance rules.

Only after both phases complete — and the Director approves — does the next milestone begin.

### Why milestones

| Benefit | How |
|---------|-----|
| **Incremental complexity** | Each milestone adds one thing, so failures are easy to attribute |
| **Tests carry forward** | Earlier milestone tests are promoted to the next, so regressions are caught |
| **Clean baselines** | The skill is backed up at every milestone boundary, so you can always revert |

---

## 5. Review Dimensions and Delta Acceptance

### Dimensions

The review phase scores across eight dimensions:

| ID | Dimension | What it measures |
|----|-----------|-----------------|
| D1 | Structural clarity | Does the file layout map cleanly to the skill's concepts? |
| D2 | Single source of truth | Is every concept defined in exactly one place, or duplicated? |
| D3 | Token efficiency | How many tokens does a single run consume? Lines read, prompt sizes, redundant reads. |
| D4 | Flow coherence | Does the execution flow follow a logical, traceable path? |
| D5 | Scenario completeness | Are all expected scenarios covered, including edge cases? |
| D6 | Contract stability | Are interfaces between agents stable and well-defined? |
| D7 | Restriction consistency | Are agent permissions explicit and consistently enforced? |
| D8 | Extensibility | How easy is it to add a new capability in the next milestone? |

### Delta acceptance rules

Not every finding is worth fixing. The reasoner applies thresholds:

| Category | Threshold | Action |
|----------|-----------|--------|
| Correctness | Any delta | **Always fix** |
| Robustness | Hard failure on valid input | **Fix** |
| Token savings | >10% improvement possible | Fix |
| Token savings | <=10% | Skip — not worth the churn |
| Everything else | Critical only | Skip unless it blocks progression |

The principle: small improvements that are not correctness-related cost more risk than they save. Fix what matters, skip what does not.

---

## 6. How This Connects to the Scaffold

| Concept | Scaffold location |
|---------|-------------------|
| Role files (act files + actor files) | `roles/<act>/<role>.md` |
| Review infrastructure (dimensions, scoring, checklists) | `skill-review/` |
| Iteration lifecycle, versioning, review rules | `iteration-guide.md` |
| Report format rules | `implementation/report-rules.md` |
| Test structure and assertion rules | `implementation/test-rules.md` |
| Milestone folder structure | `implementation/README.md` |
| Fix instruction files (input for skill-change) | `skill/` |
| Decision files (output from reasoner) | `decisions/` |

All paths are relative to `harness-core/`.
