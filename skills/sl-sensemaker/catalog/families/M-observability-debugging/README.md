# Family M — Observability & Debugging

**Core problem:** When an agent fails, developers cannot reconstruct what actually happened.

**What this family solves:** Instrumentation patterns that make agent systems inspectable — so failures can be reconstructed, root-caused, and used to improve the harness.

---

## Directory Tree

```
M-observability-debugging/
├── README.md                          ← this file (navigation, stack, runbook)
│
├── patterns/
│   ├── M01-structured-trace.md        ← emit structured events at every decision boundary
│   ├── M02-tool-call-event-log.md     ← record every tool invocation and result verbatim
│   ├── M03-execution-tree.md          ← hierarchical tree of agent/subagent spawns and completions
│   ├── M04-instrumented-handoff.md    ← attach trace context when crossing agent boundaries
│   ├── M05-artifact-lineage.md        ← track provenance of every artifact produced
│   ├── M06-token-cost-metrics.md      ← capture token usage and cost per node in the tree
│   ├── M07-replayable-run.md          ← snapshot inputs so a run can be replayed deterministically
│   ├── M08-trace-linked-eval.md       ← attach eval results back to the specific trace that produced them
│   └── M09-failure-categorization.md ← classify failures at collection time, not after the fact
│
├── guides/
│   ├── observability-stack.md         ← what to instrument first, second, third (sequenced guide)
│   └── debugging-runbook.md           ← step-by-step runbook for diagnosing a failed run
│
└── anti-patterns/
    └── AP-generic-evals-before-analysis.md  ← why designing evals before you have traces wastes effort
```

---

## Per-Pattern File Schema

Each engineering entry under `patterns/` follows this structure:

```markdown
# M0N — Pattern Name

## Intent
One sentence: what problem does this pattern solve?

## Context
When does this pattern apply? What does the system look like before this pattern is added?

## Problem
The specific failure mode this pattern prevents (with a concrete example of what goes wrong without it).

## Solution
What to instrument, where, and in what format. Include the minimal schema for the emitted data.

## Structure
Diagram or table showing what is captured, at what granularity, and where it is stored.

## Implementation Notes
- Key decisions (sync vs async emission, storage backend, sampling)
- Edge cases and gotchas
- Minimal viable vs full implementation

## Consequences
### Benefits
- ...
### Liabilities
- ...

## Related Patterns
- Links to other M-family patterns it composes with
- Links to cross-family dependencies (D, F, I, L)

## Example
A concrete snippet or schema sample showing the pattern in use.
```

---

## Observability Stack

Instrument in this order. Each layer depends on the one before it.

### Layer 1 — Run Identity (instrument first)
Before anything else, every run needs a stable, unique identity.

- Assign a `run_id` at harness entry.
- Propagate `run_id` to every spawned subagent via context injection (see M04 Instrumented Handoff).
- Emit a `run.start` and `run.end` event with wall-clock timestamps.

**Why first:** Without a run ID you cannot join any other signal. All other layers are useless without it.

### Layer 2 — Tool-Call Log (instrument second)
Record every tool invocation and its result before doing anything more sophisticated.

- Log: tool name, arguments (redact secrets), response summary, latency, success/error.
- Use verbatim capture where possible (see M02 Tool-Call Event Log).
- Store append-only; never mutate.

**Why second:** Tool calls are the highest-signal events. They are cheap to log, and they answer "what did the agent actually do?" — the first question in any debug session.

### Layer 3 — Execution Tree (instrument third)
Once you have tool logs per agent, link agents into a tree.

- Record every `agent.spawn` and `agent.complete` event with parent `run_id` and child `agent_id`.
- Attach the prompt and final output to each node (see M03 Execution Tree).
- This turns a flat log into a reconstructable call graph.

**Why third:** Tree structure lets you isolate which subagent branch failed without replaying the whole run.

### Layer 4 — Artifact Lineage
Once the tree exists, annotate artifacts with provenance.

- Every file, memory entry, or structured output written by an agent carries: `agent_id`, `run_id`, `step`, `timestamp` (see M05 Artifact Lineage).
- Store lineage metadata alongside the artifact, not inside it.

**Why fourth:** Lineage answers "where did this output come from?" — critical when downstream evals fail on an artifact you cannot trace.

### Layer 5 — Token / Cost Metrics
Add cost telemetry once the structure is stable.

- Capture input tokens, output tokens, and model ID per agent node (see M06 Token/Cost Metrics).
- Roll up to run level for budgeting; keep per-node for bottleneck analysis.

**Why fifth:** Cost data is useful but not diagnostic. Add it after structural observability is solid.

### Layer 6 — Replayability
After cost instrumentation, add replay support.

- Snapshot the full input state at `run.start`: prompt, tool definitions, any injected context (see M07 Replayable Run).
- Deterministic replay requires frozen tool responses — decide whether you replay live or from mocked responses.

**Why sixth:** Replayability is expensive to add correctly. You need the full execution tree first to know what "the same run" means.

### Layer 7 — Trace-Linked Evals
Only add evals once layers 1–6 are in place.

- Attach eval results to the specific `run_id` and `agent_id` that produced the evaluated output (see M08 Trace-Linked Eval).
- This is the bridge to Family D (verification).

**Why last:** Evals designed without traces measure the wrong things. The anti-pattern (AP-generic-evals-before-analysis) documents this failure mode.

---

## Debugging Runbook

Use this outline when a run has failed and you need to diagnose it.

### Step 1 — Locate the Run
- Find the `run_id` from the failure report or job log.
- Pull the `run.start` / `run.end` events to confirm the run completed vs. was interrupted.

### Step 2 — Identify the Failing Agent Node
- Load the execution tree (M03).
- Find the deepest node with `status: failed` or no `agent.complete` event.
- If the tree is missing, fall back to the tool-call log (M02) and look for the last successful event.

### Step 3 — Reconstruct the Tool-Call Sequence
- For the failing node, extract the ordered tool-call log (M02).
- Look for: error responses, unexpected empty results, tool calls that never returned.
- Check latency outliers — a stuck tool call often precedes a timeout cascade.

### Step 4 — Inspect Inputs and Context
- Pull the prompt and injected context for the failing node from the execution tree (M03).
- Compare against a passing run of the same task if one exists.
- Check for: stale memory, missing artifacts from a prior step (M05 lineage), truncated context.

### Step 5 — Check Handoff Points
- If the failure is in a subagent, inspect the handoff event that spawned it (M04 Instrumented Handoff).
- Verify the parent passed the correct `run_id`, prompt parameters, and artifact references.

### Step 6 — Categorize the Failure
- Assign a failure category (M09 Failure Categorization): tool error, model refusal, context overflow, harness bug, infra fault, prompt defect, or non-determinism.
- Record the category in the run metadata for trend analysis.

### Step 7 — Check Cost and Token Budget
- Pull token metrics for the failing node (M06).
- If input tokens are near the model's context limit, context overflow is the likely root cause.
- If cost spiked in a prior sibling node, check whether a runaway loop preceded the failure.

### Step 8 — Attempt Replay
- If the failure is deterministic (not flaky), replay the run from the snapshot (M07).
- Replay with additional logging or breakpoints to confirm the root cause before fixing.

### Step 9 — Link to Eval
- Once root cause is confirmed, check whether an existing eval would have caught it (M08).
- If not, add a trace-linked eval covering this failure mode before closing the issue.

---

## Cross-Family Dependencies

| Family | Relationship |
|--------|--------------|
| D — Verification | M08 Trace-Linked Eval is the direct bridge; evals reference trace IDs |
| F — Harness | The harness produces the traces; without F, M has nothing to instrument |
| I — Reliability | Recovery patterns (I) require knowing what failed; M provides that signal |
| L — Memory | Provenance-tagged memory (L) is an instance of artifact lineage (M05) |

---

Last updated: 2026-08-24
