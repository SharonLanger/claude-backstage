# Family F — Harness / Environment Engineering

**Core insight:** When an agent fails repeatedly on real tasks, the issue is often the environment, not the model. Model capability alone is insufficient for reliable long-horizon software work. The harness is the repository, tools, instructions, feedback loops, tests, and execution environment that make agents work reliably.

**Term coined by:** OpenAI — "harness engineering" as a discipline distinct from prompt engineering.

**Related families:**
- E (Context Engineering) — what the harness makes visible to the agent
- G (Tool Design) — what tools the harness provides
- J (Security) — sandboxing constraints the harness enforces
- M (Observability) — what the harness records and surfaces

---

## Directory Tree

```
F-harness-environment/
├── README.md                              ← this file (navigation, checklists, diagnostics)
│
├── patterns/
│   ├── F01-agent-legible-repository.md    ← repo structure optimized for agent navigation
│   ├── F02-repository-local-system-of-record.md  ← plans, tasks, state persisted in-repo
│   ├── F03-executable-feedback-loop.md    ← tests/linters/type-checkers give signal immediately
│   ├── F04-mechanical-architecture-constraints.md ← hard rules the environment enforces (not asks)
│   ├── F05-agent-accessible-tools.md      ← tools callable by agents without human mediation
│   ├── F06-structured-repository-instructions.md  ← CLAUDE.md / agent instructions in repo
│   ├── F07-agent-skills-procedures.md     ← packaged, reusable, callable skill definitions
│   ├── F08-sandboxed-execution.md         ← isolated execution prevents blast radius
│   ├── F09-persistent-task-artifacts.md   ← outputs survive session ends; agents pick up mid-task
│   ├── F10-agent-to-agent-review.md       ← one agent reviews another's output
│   └── F11-capability-gap-feedback.md     ← harness signals when task exceeds agent capability
│
├── harness-assessment-checklist.md        ← evaluate an existing harness against all 11 patterns
└── harness-vs-prompt-decision-guide.md    ← decide: is this a harness fix or a prompt fix?
```

---

## Per-Pattern File Schema

Every pattern file (`F01` through `F11`) uses this structure:

```markdown
# F<N> — <Pattern Name>

## Problem
One paragraph: what breaks when this pattern is absent.

## Solution
One paragraph: what the pattern prescribes.

## Structure
Diagram or component list showing how the pattern is wired up.

## Implementation
Concrete steps to add this pattern to an existing repo.
Ordered list, each step actionable.

## Signals (how to know it's working)
- Observable indicators the pattern is active and effective.

## Anti-Patterns
- Common wrong implementations and why they fail.

## Related Patterns
- Cross-references to other F-family patterns and cross-family references.

## Examples
Real or representative examples (system prompts, directory layouts, config snippets).

## References
Links to source material, research, or prior art.
```

---

## Is Your Problem the Harness or the Model?

Use this diagnostic before blaming the model or writing more prompt text.

### Step 1 — Characterize the failure

| Failure type | Likely location |
|---|---|
| Agent completes task incorrectly in a consistent, reproducible way | Harness (missing constraint or bad instructions) |
| Agent completes task incorrectly in a random, non-reproducible way | Could be model — check Step 2 |
| Agent takes a wrong action it was never told not to take | Harness — missing F04 (Mechanical Constraints) or F06 (Instructions) |
| Agent cannot find the right file or function | Harness — F01 (Agent-Legible Repository) |
| Agent repeats a mistake it made before, even in a new session | Harness — F09 (Persistent Artifacts) or F06 (Instructions) |
| Agent produces output that passes its own check but fails yours | Harness — F03 (Executable Feedback Loop) — the feedback loop is checking the wrong thing |
| Agent loses track of what it was doing mid-task | Harness — F02 (System of Record) or F09 (Persistent Artifacts) |
| Agent calls a tool incorrectly or not at all | Harness — F05 (Agent-Accessible Tools) |
| Agent's sub-steps are correct but they compose badly | Harness — F07 (Skills/Procedures) — needs structured procedures |
| Agent gets stuck at the same step across models/versions | Harness — the step requires a missing harness capability |

### Step 2 — The substitution test

> Replace the agent with a skilled human developer who can only see what the agent sees (the same files, tools, and instructions). Would the human succeed?

- **Yes, human succeeds** → the environment is adequate; the problem is the model.
- **No, human also struggles** → the environment is the problem. Fix the harness.
- **Human needs to ask clarifying questions** → F06 (Instructions) or F02 (System of Record) is incomplete.
- **Human needs a tool that doesn't exist** → F05 (Agent-Accessible Tools) is missing a capability.

### Step 3 — Prompt vs. harness decision

| You want to… | Fix in… |
|---|---|
| Tell the agent what to do once | Prompt / task description |
| Enforce a rule every time, automatically | Harness (F04 or F06) |
| Prevent a class of mistakes at the tooling level | Harness (F03 or F08) |
| Give the agent a reusable procedure | Harness (F07) |
| Make a file easier to navigate | Harness (F01) |
| Persist state across sessions | Harness (F02, F09) |
| Detect when the agent is failing silently | Harness (F03, F11) |

**Rule of thumb:** If you find yourself adding the same instruction to multiple prompts, it belongs in the harness (F06). If the instruction is task-specific and one-time, it belongs in the prompt.

---

## Harness Assessment Checklist

Score your harness: check each item that is fully implemented. Partial counts as unchecked.

### F01 — Agent-Legible Repository
- [ ] Directory structure follows a predictable, documented convention
- [ ] Key entry points are named consistently (index, main, mod, etc.)
- [ ] A machine-readable map (CLAUDE.md or equivalent) describes where things live
- [ ] Folder names are self-describing — agent can infer purpose without reading contents

### F02 — Repository-Local System of Record
- [ ] Active tasks/plans are committed files in the repo (not only in memory or chat)
- [ ] Completed tasks leave an artifact (commit, plan file, decision log)
- [ ] A new agent session can resume a task from the repo state alone

### F03 — Executable Feedback Loop
- [ ] Tests exist and run in under 60 seconds for unit-level work
- [ ] Type-checking runs on every modified file
- [ ] Linting / formatting runs and produces actionable output
- [ ] Agent can invoke all checks without human mediation
- [ ] Failure output is structured (file, line, message) — not wall-of-text

### F04 — Mechanical Architecture Constraints
- [ ] Hard rules are enforced by tooling (pre-commit hooks, CI, type system) not only instructions
- [ ] Violations fail with an error, not a warning
- [ ] Constraints are narrow enough not to block legitimate work

### F05 — Agent-Accessible Tools
- [ ] Tools are callable via CLI or MCP without interactive prompts
- [ ] Tool outputs are machine-readable (structured JSON or parseable text)
- [ ] No tool requires out-of-band auth the agent cannot obtain
- [ ] Tool error messages are specific enough to act on

### F06 — Structured Repository Instructions
- [ ] CLAUDE.md (or equivalent) exists at repo root
- [ ] Instructions are organized by concern (code style, testing, commit, deploy)
- [ ] Instructions are specific to this repo — not generic advice
- [ ] Instructions are kept current (no stale rules that cause agent confusion)

### F07 — Agent Skills / Procedures
- [ ] Repeated multi-step workflows are packaged as named skills
- [ ] Skills are invocable by name from the agent
- [ ] Skills are versioned alongside the code they operate on
- [ ] Skills document their inputs, outputs, and failure modes

### F08 — Sandboxed Execution
- [ ] Agent cannot modify production state during development work
- [ ] Test runs are isolated (no cross-test pollution)
- [ ] Destructive operations require an explicit confirmation gate
- [ ] Blast radius of a runaway agent is bounded

### F09 — Persistent Task Artifacts
- [ ] Intermediate outputs are written to disk, not held only in context
- [ ] Artifacts are discoverable by path convention (not only by memory)
- [ ] Artifacts survive session end / context reset
- [ ] Stale artifacts are cleaned up or versioned to avoid confusion

### F10 — Agent-to-Agent Review
- [ ] High-stakes outputs are reviewed by a second agent before acceptance
- [ ] Reviewer agents are given a different context than the author agent (to avoid rubber-stamping)
- [ ] Review failures block progress (not just annotate)

### F11 — Capability-Gap Feedback
- [ ] The harness detects when the agent has failed N times on the same step
- [ ] On repeated failure, the agent surfaces the gap rather than silently retrying
- [ ] Capability gaps are logged as actionable items (new tool needed, instruction gap, etc.)

### Scoring

| Score | Interpretation |
|---|---|
| 0–10 / 34 | Minimal harness — agent success is mostly luck; high variance on real tasks |
| 11–20 / 34 | Partial harness — works for simple tasks; fails on multi-session or multi-step work |
| 21–28 / 34 | Solid harness — reliable for most coding tasks; gaps mainly in edge cases |
| 29–34 / 34 | Strong harness — ready for long-horizon autonomous work |

---

Last updated: 2026-08-24
