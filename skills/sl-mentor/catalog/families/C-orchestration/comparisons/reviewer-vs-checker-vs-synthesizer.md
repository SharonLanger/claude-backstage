# Reviewer vs. Checker vs. Synthesizer

## Purpose

Three patterns handle the post-processing of agent outputs — but they serve fundamentally different purposes. Using the wrong one produces either an underperforming system (a checker used where critique is needed) or an over-engineered one (a synthesizer where a single checker would suffice). This file distinguishes them.

---

## The Three Roles at a Glance

| Dimension | Specialist Reviewer | Maker-Checker | Synthesizer / Aggregator |
|-----------|--------------------|-----------|-----------------------|
| Input | One output from one producer | One output from one maker | N outputs from N producers |
| Purpose | Qualitative critique on multiple dimensions | Binary verification against defined criteria | Unification of parallel outputs |
| Output | Structured critique with rationale and severity | Pass / Fail + reason | One coherent unified result |
| Verdict type | Qualitative (good / needs improvement / unacceptable) | Binary (correct / incorrect) | Not a verdict — a new artifact |
| Revision loop | Common — reviewer gives feedback; producer revises | Common — checker fails; maker retries | Uncommon — synthesizer produces final result directly |
| Produces content? | No — only evaluates | No — only verifies | Yes — synthesizer creates a new unified artifact |
| Criteria | Multi-dimensional; may be partially subjective | Precise, checkable, ideally objective | Not criteria — synthesis strategy |

---

## Decision Guide

**Use Specialist Reviewer when:**
- You need qualitative critique: "is this accurate, complete, safe, and well-structured?"
- The evaluation spans multiple named dimensions.
- The output needs improvement but not rejection — feedback-driven revision is the goal.
- Criteria include subjective or stylistic dimensions.

**Use Maker-Checker when:**
- You need binary verification: "is this correct or not?"
- The correctness criteria are precise and checkable.
- The output must pass a hard gate before being committed or exposed to downstream systems.
- The cost of an undetected error is high (irreversible actions, safety constraints).
- Speed matters — a binary check is faster than multi-dimensional critique.

**Use Synthesizer / Aggregator when:**
- Multiple producers have generated outputs in parallel.
- Those outputs must be unified, deduplicated, or conflict-resolved into one result.
- You are implementing a fan-out / fan-in pattern.
- The concern is convergence, not quality gate.

---

## Core Distinction

The reviewer and checker are **evaluators** — they receive one output and decide what to do with it. They do not produce content; they produce verdicts.

The synthesizer is a **producer** — it receives many outputs and creates a new, unified artifact. It is not an evaluator; it has no verdict to render.

```
Reviewer:     one output  →  verdict (qualitative)  →  revise or accept
Checker:      one output  →  verdict (binary)        →  commit or retry
Synthesizer:  N outputs   →  new artifact            →  return to caller
```

---

## When They Overlap

**Reviewer + Checker in sequence**: A reviewer provides qualitative feedback (revise); after revision, a checker provides a binary gate (commit or not). The reviewer improves quality; the checker provides the hard gate. This is a common combination for high-stakes outputs.

**Synthesizer + Reviewer**: After synthesis, a reviewer critiques the unified result before it is returned to the caller. The synthesizer converges; the reviewer validates the convergence.

**Synthesizer + Checker**: After synthesis, a checker verifies the unified result against a correctness constraint. Useful when the synthesis process itself might introduce errors.

**Voting Synthesizer as Checker**: When a synthesizer implements majority voting across N independent producers, it acts as a soft checker — the majority view is "verified" by consensus. This is not a true checker (no explicit criteria) but provides similar confidence at scale.

---

## Common Mistakes

**Mistake 1: Using a checker where a reviewer is needed.**
If the evaluation criteria include "is this well-reasoned?" or "is this comprehensive?", a binary checker cannot answer them. Use a reviewer.

**Mistake 2: Using a reviewer where a checker is needed.**
If the question is "does this SQL query modify only the rows it should?", qualitative critique is the wrong tool. Use a checker with explicit correctness criteria.

**Mistake 3: Using a synthesizer as a quality gate.**
A synthesizer unifies; it does not validate. If you need to ensure the unified output meets a quality bar, add a reviewer or checker after synthesis — do not ask the synthesizer to do both.

**Mistake 4: Giving the checker qualitative instructions.**
Checker prompts that say "evaluate the quality of this output" produce inconsistent binary verdicts. Checker prompts must specify precise, checkable conditions only.

---

## Sources

- **Anthropic Engineering** — AI safety company; authors of Claude. [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Google Cloud Architecture Center** — Google's cloud architecture team. [Choose a Design Pattern for Agentic AI](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- **AWS Prescriptive Guidance** — Amazon Web Services architecture team. [Agentic AI Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- **Stanford CS224G** — Stanford University course on LLM agents. [Agentic Design Patterns (lecture slides)](https://web.stanford.edu/class/cs224g/lectures/Agentic_Design_Patterns.pdf)
