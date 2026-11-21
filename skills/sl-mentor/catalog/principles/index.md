# Principles — Cross-Reference Index

One-page mapping of all 8 principles to the pattern families they govern, the anti-patterns they prevent, and the tensions between them.

---

## Principle × Family Matrix

Rows = principles. Columns = pattern families A–O. An **X** marks where a principle is a primary driver of that family's patterns.

| Principle | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P1** Prefer Determinism | | | | | | | X | X | | | | | | | X |
| **P2** Complexity Earns Its Keep | | X | X | | | | | | | | | | | X | |
| **P3** Give Agents Ground Truth | | | | | X | X | | | | | | X | | | |
| **P4** Separate Generation / Verification | X | | X | X | | | | | | | | | | | |
| **P5** Context Is a Designed Resource | | | | | X | X | | | | | | X | | | |
| **P6** Security Boundaries Outside Model | | | | | | | X | X | | X | | | | | |
| **P7** Measure Real Task Success | | | | X | | X | | | | | | | X | | |
| **P8** Failures Improve the Harness | | | | | | X | | | X | | | | X | | |

### Family Key

| Code | Family |
|---|---|
| A | Workflow Topology |
| B | Task Decomposition |
| C | Orchestration |
| D | Verification & Evaluation |
| E | Context Engineering |
| F | Harness Engineering |
| G | Tool Design |
| H | Deterministic Control |
| I | Reliability & Recovery |
| J | Security & Trust |
| K | Human Control |
| L | Memory & State |
| M | Observability |
| N | Efficiency & Routing |
| O | Output & Integration |

---

## Principle → Anti-Pattern Mapping

Each principle, when violated, manifests as one or more named anti-patterns.

| Principle | Anti-Patterns Prevented |
|---|---|
| **P1** Prefer Determinism | Prompt-as-Policy, Model as Security Boundary |
| **P2** Complexity Earns Its Keep | Multi-Agent by Default |
| **P3** Give Agents Ground Truth | Giant Instruction Manual, Shared Context Everywhere |
| **P4** Separate Generation / Verification | Self-Certified Completion |
| **P5** Context Is a Designed Resource | Giant Instruction Manual, Shared Context Everywhere |
| **P6** Security Boundaries Outside Model | Prompt-as-Policy, Model as Security Boundary, Overpowered Coding Agent |
| **P7** Measure Real Task Success | Generic Evals Before Error Analysis, Self-Certified Completion |
| **P8** Failures Improve the Harness | Retry Without New Information, Generic Evals Before Error Analysis |

---

## Tension Matrix

Principles sometimes pull in opposite directions. This matrix names the tensions and when each side wins.

| Tension | Pulls Toward | Pulls Away From | Resolution |
|---|---|---|---|
| **P1 vs P2** | Deterministic enforcement adds code | Simplicity says less code is better | Add deterministic checks only when the failure mode is real and recurring — not speculatively |
| **P2 vs P4** | Separate verification adds a component | Simplicity says fewer components | Separate when the cost of undetected bad output exceeds the cost of a verification step |
| **P3 vs P5** | More ground truth means more context | Context must be curated and bounded | Provide ground truth through tools that return focused results, not by dumping everything into the prompt |
| **P5 vs P3** | Designing context means filtering | Agents need real evidence to reason | Filter for relevance, never filter out execution results or error messages |
| **P1 vs P8** | Deterministic gates are static | Harness improvement requires iteration | Gates enforce known invariants; harness improvements address newly discovered failure modes |

---

## How to Use This Index

- **Designing a system?** Find the families you're working in (columns), then read the principles that govern them (rows with X).
- **Debugging a failure?** Identify the anti-pattern from the mapping table, then read the principle that prevents it.
- **Resolving a design tradeoff?** Check the tension matrix to see if two principles are pulling in opposite directions.

---

## Sources

- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- Hamel Husain & Shreya Shankar — [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
