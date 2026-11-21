# Family K — Human Control: Patterns

6 patterns (K01–K06) covering when agents should pause, check in, or hand off to a human.

**Central tension:** Autonomy increases throughput but reduces oversight. Each pattern in this family stakes out a different point on that tradeoff — from hard blocking gates (K01, K02) to non-blocking monitoring (K06).

**Sources:** Anthropic Engineering, Google Cloud Architecture Center, OpenAI Engineering, Microsoft Azure Architecture Center.

---

## Files

```
patterns/
├── README.md                            ← this file
├── K01-human-in-the-loop-checkpoint.md  ← pause between plan phases; require explicit approval before the next phase begins
├── K02-high-risk-action-gate.md         ← block any single action whose blast radius or irreversibility exceeds a threshold
├── K03-failure-threshold-escalation.md  ← escalate to a human when retry budget is exhausted, rather than looping or failing silently
├── K04-review-before-side-effect.md     ← require human review before any action that changes external state
├── K05-draft-preview-before-apply.md    ← show a diff or preview of a proposed file/data change and require confirmation before writing
└── K06-human-on-the-loop-monitoring.md  ← let the agent run autonomously while a human observes and can intervene without blocking
```

---

## Pattern Schema

Each engineering entry in this folder follows the same structure:

| Section | Contents |
|---|---|
| **Title + ID** | Pattern name and identifier |
| **Intent** | One-sentence statement of what the pattern achieves |
| **Problem** | The failure mode or risk this pattern addresses |
| **Solution** | The architectural response in plain language |
| **Structure** | Mermaid diagram (sequence or flowchart) in a collapsible `<details>` block |
| **When to Use** | Conditions that favor applying this pattern |
| **When NOT to Use** | Conditions where this pattern adds friction without benefit |
| **Implementation Notes** | Concrete guidance, pseudocode, format templates |
| **Tradeoffs** | Table of forces: latency, throughput, oversight, auditability |
| **Related Patterns** | Intra- and inter-family links with relationship description |
| **Example** | A worked scenario showing the pattern in action |
| **Sources** | Citations with relevance summary and URL |

---

## How to Navigate

**Entry by blocking behavior:**
- Hard blocking (agent cannot proceed without human) → K01, K02, K04, K05
- Threshold-triggered blocking → K03
- Non-blocking (human observes but does not block) → K06

**Entry by granularity:**
- Phase-level control (coarse) → K01
- Action-level control (fine-grained) → K02, K04, K05
- Failure-triggered control → K03
- Continuous ambient oversight → K06

**Entry by use case:**
- Multi-phase task with irreversible later phases → K01
- Single destructive or high-blast-radius action → K02
- Agent stuck in a retry loop → K03
- Any external state change → K04
- File/document write preview → K05
- Autonomous pipeline with an escape hatch → K06

**Progression from maximum to minimum oversight:**
K01 (phase gates) → K02 (action gates) → K04 (side-effect review) → K05 (file preview) → K03 (failure escalation) → K06 (monitoring only)

**Cross-family links:** K01 and K02 overlap with J08 (Human Approval Gate in the security family). K01 checkpoints map naturally to phase boundaries in Family B (Task Decomposition). K06 connects to Family M (Observability) — monitoring infrastructure enables human-on-the-loop.

---

Last updated: 2026-08-24
