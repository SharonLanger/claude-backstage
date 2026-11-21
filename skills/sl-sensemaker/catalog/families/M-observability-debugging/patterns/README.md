# Family M — Observability & Debugging: Patterns

9 patterns covering instrumentation so agent failures can be reconstructed and analyzed.

**Key insight (Hamel Husain):** Inspect real traces first. Discover actual failure modes. Build a failure taxonomy. Only then define success criteria. Generic evals before error analysis is the named anti-pattern this family addresses.

---

## Files

```
patterns/
├── README.md                    ← this file
├── M01-structured-trace.md      ← emit a structured event at every decision boundary for full run reconstruction
├── M02-tool-call-event-log.md   ← record every tool invocation and result verbatim for audit without re-running
├── M03-execution-tree.md        ← build a hierarchical tree of agent spawns so failures isolate to a single branch
├── M04-instrumented-handoff.md  ← attach trace context at agent boundaries so parent/child events can be joined
├── M05-artifact-lineage.md      ← track provenance of every artifact so downstream failures trace back to origin
├── M06-token-cost-metrics.md    ← capture token usage and cost per node so budget overruns are detectable early
├── M07-replayable-run.md        ← snapshot full input state at run start for deterministic replay of failures
├── M08-trace-linked-eval.md     ← anchor eval results to specific trace entries, not just final output
└── M09-failure-categorization.md ← classify failures into a taxonomy derived from real traces before attempting fixes
```

---

## Schema

Each engineering entry in this folder follows the same structure:

| Section | What it contains |
|---|---|
| `# MXX — Name` | Pattern ID, canonical name |
| `## Intent` | One-sentence statement of what the pattern achieves |
| `## Context` | When and where the pattern applies |
| `## Problem` | The specific failure mode it solves, with a concrete "without this pattern" example |
| `## Solution` | The mechanism, often including a field-level schema or pseudocode |
| `## Structure` | Diagram (Mermaid) or annotated pseudocode illustrating the solution |
| `## Consequences` | Trade-offs: what you gain, what it costs |
| `## Known Uses` | Real systems, frameworks, or sources that apply the pattern |
| `## Related Patterns` | Cross-references within and across families |

---

## How to Navigate

**Start here if you're debugging a live failure:** M09 (categorize first) → M01/M02 (find the trace events) → M03 (isolate the branch) → M08 (link to eval).

**Start here if you're instrumenting a new system:** M01 (foundation event schema) → M04 (handoff context) → M03 (tree) → M05 (artifacts) → M06 (cost) → M07 (replay).

**Patterns build on each other:** M01 defines the event schema that M02, M03, M04, M05, and M06 all emit into. M07 depends on M01–M06 being in place. M08 requires M01 and M04. M09 is the analytical endpoint that consumes everything upstream.

**Cross-family links:** Token/cost data from M06 feeds directly into the efficiency patterns in Family N. Failure taxonomy from M09 is the prerequisite for defining evals in Family D.
