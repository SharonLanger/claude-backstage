# Core Design Patterns

## Patterns

Three patterns define how this system works. Remove any one of them and the iteration loop breaks. Each pattern addresses a different failure mode of multi-agent systems — context drift, confirmation bias, and goal drift. Together, they create a system where agents operate deterministically, evaluate independently, and iterate toward a fixed human-defined target.

1. **Files as Interfaces** — Agents communicate through files, not prompts. Spawn prompts are 1-2 sentences pointing to files. This makes agent behavior deterministic, sessions recoverable, and debugging possible.
2. **Separation of Concerns (Act Boundaries)** — The agent that changes the code never judges whether the change is correct. Each agent has explicit can-do and cannot-do boundaries enforced through role files.
3. **Immutable Test Contracts** — Tests lock after human approval. No agent may modify test files. The skill adapts to the tests, never the reverse.

---

## Sources

### Building Effective Agents — Anthropic

https://www.anthropic.com/engineering/building-effective-agents

A practical guide to building LLM-powered agent systems. The key argument: start simple, add complexity only when it measurably improves outcomes. Introduces workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) and draws a clear line between deterministic workflows and autonomous agents. The main takeaway for this scaffold: **agent systems work best when most of the orchestration is deterministic** — the LLM handles the hard parts (reasoning, generation), while the structure around it controls flow, gates, and evaluation.

> "The most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."

> "For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."

> "During execution, it's crucial for the agents to gain 'ground truth' from the environment at each step."

### Effective Context Engineering for AI Agents — Anthropic

https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

Reframes the problem from "write a better prompt" to "design the information environment." Context engineering is about curating the smallest set of high-signal tokens for each step — not dumping everything into one prompt. The main takeaway for this scaffold: **every agent should see exactly what it needs and nothing more.** File-based communication, 1-2 sentence spawn prompts, and role-scoped context loading are direct implementations of this principle.

> "Good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."

> "Agents built with the 'just in time' approach maintain lightweight identifiers and use these references to dynamically load data into context at runtime."

### Harness Engineering — OpenAI

https://openai.com/index/harness-engineering/

Describes how OpenAI built the execution environment around Codex — not the model itself, but everything surrounding it: file access, tool invocation, test execution, structured feedback. The central insight: **the harness matters more than the model.** A well-engineered environment (files, tests, gates, structured outputs) makes an average model effective, while a poorly-engineered one makes a great model unreliable. This scaffold is a direct application of that principle — the 54 files in `harness-core/` are the harness.

Key findings from the Codex project:

- **The main bottleneck was often not model capability but an underspecified environment.** Failures are diagnostic evidence about what the harness is missing — a missing tool, an unclear instruction, an absent validator.
- **Keep AGENTS.md short as a map, not a giant manual.** Put deeper knowledge in structured repository-local documentation.
- **Enforce architectural invariants mechanically** — use linters, structural tests, and CI hooks rather than relying on instructions for must-hold rules.

---

## Principles Behind the Patterns

These three patterns didn't emerge in isolation. They implement principles that appeared independently across every major source — Anthropic, OpenAI, Google, AWS, and Microsoft all arrived at the same conclusions through different engineering paths.

| Principle | What it says | Who converged | Which pattern |
|-----------|-------------|---------------|---------------|
| **Prefer Determinism** | Don't spend model reasoning on conditions a program can reliably decide. | AWS, OpenAI, Anthropic, Google, OWASP | All three — files make behavior deterministic, act boundaries are structural, test immutability is enforced by role permissions |
| **Separate Generation from Verification** | The system that produced output should not be the only source establishing correctness. | Anthropic, Google, AWS, OpenAI, Hamel Husain | Pattern 2 — the agent that changes code never judges the change |
| **Context Is a Designed Resource** | More context is not better. Context must be selected, scoped, and isolated. | Anthropic, OpenAI, Microsoft, Google | Pattern 1 — each agent loads exactly one role file, not the full history |

The scaffold's contribution is making these principles **structural** rather than advisory. They're not guidelines an agent might follow — they're boundaries the system enforces.

---

## 1. Files as Interfaces

### The Pattern

Agents communicate through files, not through prompts or shared context. A spawner writes a file; the spawned agent reads it. Agent spawn prompts are 1-2 sentences pointing to files — never inlined task details.

```
"You are the runner agent for act-test-runner.
 Read act-test-runner.md first, then read runner.md."
```

That is the entire prompt. Everything else lives in files.

### Why It's Critical

Multi-agent systems have a fundamental problem: how do agents share state without context windows bleeding into each other? Most approaches inline context into prompts, which creates three failures:

1. **Prompt bloat** — each agent receives everything, reads most of it, uses little of it
2. **Non-determinism** — rephrasing the same information in a prompt produces different agent behavior
3. **Session fragility** — if a session dies, all context dies with it

Files solve all three. An agent reads exactly the file it needs. The same file produces the same behavior across sessions. And files survive session crashes — a new session reconstructs the full state from the file tree.

### What the Sources Say

> "Good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."
> — Anthropic, *Effective Context Engineering*

The scaffold implements this literally: a spawn prompt is 1-2 sentences pointing to files. The agent loads its role file. That's the context — nothing else.

> "Agents built with the 'just in time' approach maintain lightweight identifiers and use these references to dynamically load data into context at runtime."
> — Anthropic, *Effective Context Engineering*

This is exactly what role files are — lightweight identifiers that load structured knowledge on demand.

OpenAI's Harness Engineering recommends keeping AGENTS.md short as a **map, not a giant manual**, and putting deeper knowledge in structured repository-local documentation. The scaffold's 16 role files across 4 acts are that structured documentation. The spawn prompt is the map.

### How It's Used Here

| Communication | File | Writer | Reader |
|---------------|------|--------|--------|
| Test results | `results/results-run-NN.md` | Reporter | Reasoner |
| Failure analysis | `decisions/decision-*.md` | Reasoner | Main Agent, Skill-Change-Agent |
| Fix instructions | `skill/fix-NN-*.md` | Reasoner | Skill-Change-Agent |
| Review findings | `skill-review/m1/review-results.md` | Synthesis Agent | Reasoner |
| Role instructions | `roles/<act>/<role>.md` | Human (setup) | Every agent in that role |

No agent ever receives task content in its spawn prompt. The prompt says *where to look*. The files say *what to do*.

### What Breaks Without It

- Agents receive inconsistent context depending on how the spawner phrases the prompt
- Session crashes lose all state — the iteration cannot resume
- Debugging becomes impossible — you cannot inspect what an agent "knew" because it was in a transient prompt
- Token costs explode as every agent loads the full context of every preceding agent

### Scaffold locations

- Role files: `roles/<act>/<role>.md`
- Decision files: `decisions/`
- Fix instruction files: `skill/`
- Result files: `implementation/m1-example/results/`
- Review outputs: `skill-review/m1/`

---

## 2. Separation of Concerns (Act Boundaries)

### The Pattern

Each agent has explicit **can-do** and **cannot-do** boundaries. These are not suggestions — they are structural rules loaded at the top of every agent's instructions.

| Agent | Can Do | Cannot Do |
|-------|--------|-----------|
| Test-Runner | Execute tests, report results | Edit the skill, edit tests |
| Skill-Change-Agent | Modify skill files, create backups | Run tests, run reviews |
| Reasoner | Analyze results, write fix instructions | Edit the skill, run tests |
| Reviewer | Score dimensions, produce findings | Edit the skill, edit tests |
| Director (human) | Approve gates, change tests | — |

The critical invariant: **the agent that changes the code never judges whether the change is correct.** Generation and verification are structurally independent.

### Why It's Critical

A single agent that writes code and then evaluates its own code exhibits **confirmation bias**. It knows what it intended, so it reads its output charitably. This is not a theoretical concern — it is the primary failure mode of single-agent iteration loops.

The separation also prevents **shortcut-taking**. If the test-runner could edit the skill, a failing test could be "fixed" by adjusting the skill mid-run. If the skill-changer could run tests, it could run them privately, see failures, and adjust before the official test run. Both undermine the integrity of the results.

### What the Sources Say

> "The system that produced uncertain output should not be the only source establishing correctness."
> — Cross-source principle (Anthropic, Google, AWS, OpenAI, Hamel Husain)

This is the single most validated principle in the research. A model that generates code and then evaluates its own code exhibits **confirmation bias** — the same reasoning that produced the output will tend to confirm it. Every major source names this independently: Google calls it evaluator-optimizer. AWS calls it maker-checker. Anthropic separates orchestrators from workers. The scaffold enforces it structurally — the skill-change agent literally cannot run tests.

> "For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect."
> — Anthropic, *Building Effective Agents*

Each act in the scaffold handles exactly one consideration: testing, reasoning, fixing, or reviewing. No act handles two.

OpenAI's Harness Engineering recommends that agents review other agents, and that evidence should come from execution — not self-assessment. The scaffold's test-runner produces ground truth (actual test results), the reasoner diagnoses from that evidence, and the review act scores independently. No agent evaluates its own output.

### How It's Used Here

```
act-test-runner  →  act-reasoning  →  act-skill-change  →  act-test-runner  →  act-review
     (test)          (diagnose)         (fix)                  (re-test)        (review)
```

Between acts, only files transfer. The Reasoner reads test results but never sees the skill-change agent's internal reasoning. The Reviewer reads the skill files but never sees what the Reasoner recommended. Each act operates on artifacts, not on another agent's thought process.

### What Breaks Without It

- The skill-change agent evaluates its own work → confirmation bias → false "all tests pass" reports
- The test-runner edits failing tests instead of reporting failures → the acceptance criteria drift
- The reasoner applies fixes directly → no versioning, no backup, no audit trail
- Review findings are biased by knowledge of what the fix intended → real issues get rationalized away

### Scaffold locations

- Act boundaries defined in: `roles/<act>/act-<name>.md`
- Per-actor permissions in: `roles/<act>/<role>.md`
- Full actor table in: `README.md` (Acts & Actors section)

---

## 3. Immutable Test Contracts

### The Pattern

Tests lock after human approval. Once locked, **no agent may modify test files** — not the blueprints, not the assertions, not the input data. If an agent believes a test is wrong, it must stop and escalate to the human Director. The skill adapts to the tests, never the reverse.

```
After the Director approves test definitions,
NO agent may modify test files (blueprint.md, asserts.md, input/).

Tests are LOCKED. If you believe a test is wrong — STOP and tell the Director.
```

This rule appears at the top of every agent's instructions.

### Why It's Critical

Tests define what "correct" means. If agents can modify tests, they can **redefine correctness to match their output** — the iteration loop converges on whatever the agent happens to produce, not on what the human intended.

This is the difference between iteration and oscillation. With immutable tests, each iteration either moves toward the fixed target (passing the locked tests) or reveals that the approach is wrong (escalation). Without them, the target moves with every attempt.

### What the Sources Say

> "During execution, it's crucial for the agents to gain 'ground truth' from the environment at each step."
> — Anthropic, *Building Effective Agents*

Locked tests ARE the ground truth. They define exactly what "correct" means — immutable, human-approved, deterministic. Without them, each iteration could redefine its own success criteria.

OpenAI's Harness Engineering found that **the main bottleneck was often not model capability but an underspecified environment.** Immutable tests are the specification. They convert a vague goal ("make the skill work") into a concrete, verifiable contract ("pass these 5 assertions across 3 layers"). When a test fails, the failure points at the skill — never at drifting acceptance criteria.

OpenAI also recommends enforcing architectural invariants mechanically — using linters, structural tests, and hooks rather than relying on instructions for must-hold rules. The "no agent may modify tests" rule follows this exactly: it's enforced by role-file permissions (each agent's `cannot-do` list), not by a prompt instruction that could be ignored.

> "When an agent repeatedly fails, inspect what capability, documentation, feedback, boundary, or validator is missing."
> — Cross-source principle (OpenAI, Hamel Husain, Anthropic, AWS)

Immutable tests make this possible. When the target doesn't move, each failure narrows the search space. When the target moves, failures teach nothing.

### How It's Used Here

1. The Director writes test definitions (blueprints + assertions) for a milestone
2. The Director reviews and approves them — **tests are now locked**
3. The iteration loop runs: test → reason → fix → re-test → review
4. At no point can any agent modify the test files
5. If a test seems wrong, the system stops and asks the Director
6. Only the Director can unlock, modify, and re-lock tests

The assertions have three layers — structural (filesystem), functional (content), and logs (observability) — each verified independently by the Verifier agent, which has read-only access to the workspace.

### What Breaks Without It

- Agents "fix" failing tests instead of fixing the skill → the iteration loop produces skills that pass weakened tests
- Test definitions drift across iterations → you cannot compare run-01 results to run-05 results because the criteria changed
- The human Director loses control of what "done" means → milestone approval becomes meaningless
- Regression detection breaks → a test that previously passed may have been silently modified to be easier

### Scaffold locations

- Test definitions: `implementation/m1-example/tests/test-NN-*/`
- Test rules and assertion format: `implementation/test-rules.md`
- Immutability rule: `README.md` (Hard Rule section), every act file

---

## Full Pattern Catalog

<details>
<summary><b>All 35 patterns mapped to the scaffold (reference appendix)</b></summary>

| Pattern | Family | Where in the Scaffold | Why |
|---------|--------|----------------------|-----|
| Sequential Workflow | Workflow Topology | The iteration cycle follows a fixed sequence: test → reason → fix → re-test → review → decide | Prevents concurrent modification; each stage consumes the previous stage's output |
| Iterative Refinement | Workflow Topology | The outer loop repeats the test-fix cycle until all tests pass, then repeats through review findings | Incremental improvement; each pass targets specific failures from the previous run |
| Evaluator-Optimizer | Workflow Topology | The reasoner evaluates; the skill-change agent optimizes. The evaluator gates whether the optimizer acts. | Separates judgment from execution, preventing churn on marginal improvements |
| Generator-Critic | Workflow Topology | Skill-change agent generates; test-runner and review agents critique. The generator never evaluates its own output. | Eliminates self-assessment bias through structural separation |
| Bounded Loop | Workflow Topology | Sub-version exploration capped at 3 attempts. Reverts to baseline on failure. | Hard caps prevent unbounded exploration |
| Fixed Decomposition | Task Decomposition | Milestones defined before execution, each with a locked test suite | Immutable acceptance criteria make iteration deterministic and auditable |
| Milestone/Checkpoint Planning | Task Decomposition | Each milestone is an explicit checkpoint with progression criteria | Natural recovery points; failures reset within the milestone, not to the beginning |
| Reconnaissance-Before-Implementation | Task Decomposition | The reasoner analyzes failures before writing fix instructions | Prevents blind fixing; evidence gathered before committing to a direction |
| Manager → Workers | Orchestration | Main agent spawns leads; leads spawn cast. Two-level hierarchy. | Matches the natural decomposition: acts vs tasks within acts |
| Specialist Reviewer | Orchestration | Dimension reviewers each score one dimension independently | Specialized reviewers catch issues generalist review misses |
| Synthesizer/Aggregator | Orchestration | Synthesis agent combines all dimension scores into one scorecard | Resolves fragmented parallel findings into a single actionable assessment |
| Maker-Checker | Orchestration | Skill-change agent makes; test-runner and reviewers check. Maker never self-verifies. | Independence is the invariant |
| Test-Before-Done | Verification | Tests must pass before milestone progression. The test suite is the gate. | Prevents self-certified completion |
| Independent Verifier | Verification | Verifier has no access to the skill-change agent's reasoning or intent | Eliminates confirmation bias in result assessment |
| Multi-Review / Ensemble | Verification | Multiple dimension reviewers assess independently; findings aggregated by synthesis | Redundant evaluation catches what single review misses |
| End-to-End Task-Success Eval | Verification | Tests run the full skill end-to-end against real inputs | Actual execution results replace proxy metrics |
| Step-Level Diagnostic | Verification | Reasoner maps failures to root causes across assertion layers | Targeted diagnosis prevents shotgun fixes |
| Role-Scoped Context | Context Engineering | Each agent loads only its act file and role file | Prevents context contamination |
| Artifact-Based Handoff | Context Engineering | All inter-agent communication flows through files | Files are reproducible, auditable, and token-efficient |
| Minimal-Context Handoff | Context Engineering | Spawn prompts are 1-2 sentences pointing to files | Eliminates prompt bloat |
| Context Isolation | Context Engineering | Each agent has its own context window; cross-act reasoning is not visible | Prevents cross-act contamination |
| Repository-as-System-of-Record | Harness | The file tree is the source of truth; any session can resume from file state | Sessions are disposable; the file system is durable |
| Executable Feedback Loop | Harness | Test-runner feeds actual execution results through the verification chain | Ground truth from execution replaces self-assessment |
| Agent Skills/Procedures | Harness | The skill under development is a packaged, versioned, callable procedure | Enables automated testing and version comparison |
| Persistent Task Artifacts | Harness | All outputs written to disk with predictable paths | Multi-session iteration requires durable state |
| Agent-to-Agent Review | Harness | The review act reviews the skill-change agent's output with blocking authority | Structural review is required, not optional |
| Structured Repository Instructions | Harness | Actors load instruction files in defined order: act → role → reference | Progressive loading by concern, not a single prompt |
| Read/Write Separation | Tool Design | Most agents are read-only. Only specific agents may write to specific directories. | Structural enforcement of who can write what |
| Programmatic Gate | Deterministic Control | Milestone progression requires: tests pass + no critical findings + human approval | Conditions checked deterministically; no agent can override through reasoning |
| Bounded Retry | Reliability | Sub-version exploration capped at 3; global retry capped at 3 before escalation | Prevents infinite exploration |
| Root-Cause-Before-Retry | Reliability | Reasoner diagnoses before skill-change agent retries | Every retry incorporates new information; no blind retries |
| Checkpoint and Resume | Reliability | Version backups serve as checkpoints; failed explorations revert cleanly | State is never lost; full audit trail via version log |
| Human Escalation | Reliability | Five explicit escalation triggers with defined stop conditions | Prevents spinning indefinitely on unsolvable problems |
| Human-in-the-Loop Checkpoint | Human Control | Milestone progression is a hard gate requiring human approval | No agent can autonomously advance to the next milestone |
| High-Risk Action Gate | Human Control | Only the human can modify tests after approval | Prevents the system from redefining its own acceptance criteria |

</details>
