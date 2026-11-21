# AI Design Patterns Catalog — Inventory

Installed catalog: `~/.cache/sl-knowledge-atlas/catalog/`
Total files: 272 markdown files

## Summary

| Category | Count |
|---|---|
| Families | 15 (A–O) |
| Patterns (across families) | 137 |
| Anti-patterns (top-level) | 10 (AP01–AP10) |
| Anti-patterns (family-level) | 10 |
| Principles | 8 (P1–P8) |
| Guides | 9 |
| Comparisons | 2 |
| Reference docs | 2 |
| Use-case files | 26 articles across 8 categories, plus 9 indexes |
| Contributing/meta files | 5 |
| Input/research files | 1 |
| Index/README files | ~47 |

---

## Top-level navigation files

| File | Purpose |
|---|---|
| `catalog-lookup.md` | Main navigation — Quick Lookup by Problem table, anti-pattern→counter-pattern reference, principle→family reference, layer-based navigation |
| `README.md` | Catalog overview and structure |

---

Use the [symptom bridge](bridge-file.md) for conversational wording and the [catalog lookup](catalog/catalog-lookup.md#quick-lookup-by-problem) for topic routes. In the family inventory below, start with B5 and K01/K05 for staged review, Context Compaction and Repository-as-System-of-Record for decisions lost in a session, and Fresh-Context Retry for repeated failed attempts.

## Families (A–O)

### A — Workflow Topology (10 patterns)

| File | Title |
|---|---|
| `bounded-loop` | Bounded Loop |
| `evaluator-optimizer` | Evaluator-Optimizer |
| `generator-critic` | Generator-Critic |
| `iterative-refinement` | Iterative Refinement |
| `parallel-sectioning` | Parallel Sectioning |
| `parallel-voting` | Parallel Voting |
| `prompt-chaining` | Prompt Chaining |
| `react` | ReAct (Reason + Act) |
| `routing` | Routing |
| `sequential-workflow` | Sequential Workflow |

### B — Task Decomposition (6 patterns)

| File | Title |
|---|---|
| `B1-plan-execute` | Plan → Execute |
| `B2-hierarchical-decomposition` | Hierarchical Task Decomposition |
| `B3-dynamic-decomposition` | Dynamic Decomposition |
| `B4-fixed-decomposition` | Fixed Decomposition |
| `B5-milestone-checkpoint` | Milestone / Checkpoint Planning |
| `B6-reconnaissance-first` | Reconnaissance-First |

### C — Orchestration (9 patterns, 1 anti-pattern, 1 guide, 2 comparisons)

**Patterns:**

| File | Title |
|---|---|
| `agent-as-tool` | Agent-as-Tool |
| `coordinator-specialists` | Coordinator → Specialists |
| `decentralized-handoff` | Decentralized Handoff |
| `hierarchical-coordinator` | Hierarchical Coordinator |
| `maker-checker` | Maker-Checker |
| `manager-workers` | Manager → Workers |
| `orchestrator-workers` | Orchestrator → Workers |
| `specialist-reviewer` | Specialist Reviewer |
| `synthesizer-aggregator` | Synthesizer / Aggregator |

**Anti-patterns:** multi-agent-by-default
**Guides:** do-you-need-multi-agent
**Comparisons:** manager-vs-orchestrator-vs-coordinator, reviewer-vs-checker-vs-synthesizer

### D — Verification & Evaluation (12 patterns, 2 guides)

**Patterns:**

| File | Title |
|---|---|
| `D01-deterministic-validator` | Deterministic Validator |
| `D02-test-before-done` | Test-Before-Done |
| `D03-evidence-based-completion` | Evidence-Based Completion |
| `D04-independent-verifier` | Independent Verifier |
| `D05-review-pass` | Review Pass |
| `D06-generator-critic` | Generator-Critic |
| `D07-evaluator-optimizer` | Evaluator-Optimizer |
| `D08-multi-review-ensemble` | Multi-Review / Ensemble |
| `D09-llm-as-judge` | LLM-as-Judge |
| `D10-human-calibration` | Human Calibration |
| `D11-end-to-end-task-success` | End-to-End Task-Success Eval |
| `D12-step-level-diagnostic` | Step-Level Diagnostic Eval |

**Guides:** eval-type-selector, verification-ladder

### E — Context Engineering (10 patterns, 2 anti-patterns, 4 guides)

**Patterns:**

| File | Title |
|---|---|
| `artifact-based-handoff` | Artifact-Based Handoff |
| `context-compaction` | Context Compaction |
| `context-isolation` | Context Isolation |
| `context-offloading` | Context Offloading |
| `just-in-time-retrieval` | Just-in-Time Retrieval |
| `map-not-manual` | Map-Not-Manual |
| `minimal-context-handoff` | Minimal-Context Handoff |
| `progressive-disclosure` | Progressive Disclosure |
| `repository-as-system-of-record` | Repository-as-System-of-Record |
| `role-scoped-context` | Role-Scoped Context |

**Anti-patterns:** giant-instruction-manual, shared-context-everywhere
**Guides:** clarify-domain-terms, context-design-worksheet, context-failure-modes, context-vs-memory-vs-state

### F — Harness / Environment Engineering (11 patterns)

| File | Title |
|---|---|
| `F01-agent-legible-repository` | Agent-Legible Repository |
| `F02-repository-local-system-of-record` | Repository-Local System of Record |
| `F03-executable-feedback-loop` | Executable Feedback Loop |
| `F04-mechanical-architecture-constraints` | Mechanical Architecture Constraints |
| `F05-agent-accessible-tools` | Agent-Accessible Tools |
| `F06-structured-repository-instructions` | Structured Repository Instructions |
| `F07-agent-skills-procedures` | Agent Skills / Procedures |
| `F08-sandboxed-execution` | Sandboxed Execution |
| `F09-persistent-task-artifacts` | Persistent Task Artifacts |
| `F10-agent-to-agent-review` | Agent-to-Agent Review |
| `F11-capability-gap-feedback` | Capability-Gap Feedback |

### G — Tool & Action Design (10 patterns, 2 reference)

**Patterns:**

| File | Title |
|---|---|
| `G01-typed-schema-constrained-tool` | Typed/Schema-Constrained Tool |
| `G02-narrow-tool-interface` | Narrow Tool Interface |
| `G03-tool-gateway` | Tool Gateway |
| `G04-agent-as-tool` | Agent-as-Tool |
| `G05-read-write-separation` | Read/Write Separation |
| `G06-tool-gate` | Tool Gate |
| `G07-deterministic-tool-execution` | Deterministic Tool Execution |
| `G08-tool-result-validation` | Tool Result Validation |
| `G09-tool-discovery-progressive-exposure` | Tool Discovery / Progressive Exposure |
| `G10-idempotent-action-wrapper` | Idempotent Action Wrapper |

**Reference:** tool-design-checklist, tool-interface-antipatterns

### H — Deterministic Control Boundaries (8 patterns)

| File | Title |
|---|---|
| `H01-deterministic-override` | Deterministic Override |
| `H02-programmatic-gate` | Programmatic Gate |
| `H03-structural-test` | Structural Test |
| `H04-policy-hook` | Policy Hook |
| `H05-typed-boundary` | Typed Boundary |
| `H06-schema-validator` | Schema Validator |
| `H07-authorization-outside-model` | Authorization Outside the Model |
| `H08-non-ai-fallback-path` | Non-AI Fallback Path |

### I — Reliability & Recovery (11 patterns, 2 anti-patterns)

**Patterns:**

| File | Title |
|---|---|
| `bounded-retry` | Bounded Retry |
| `checkpoint-and-resume` | Checkpoint and Resume |
| `circuit-breaker` | Circuit Breaker |
| `fallback-model-workflow` | Fallback Model / Workflow |
| `fresh-context-retry` | Fresh-Context Retry |
| `human-escalation` | Human Escalation |
| `retry-with-feedback` | Retry-With-Feedback |
| `root-cause-before-retry` | Root-Cause-Before-Retry |
| `stop-condition` | Stop Condition |
| `structured-error-classification` | Structured Error Classification |
| `validation-retry-loop` | Validation-Retry Loop |

**Anti-patterns:** infinite-weakly-bounded-loop, retry-without-new-information

### J — Security & Trust Boundaries (11 patterns, 2 anti-patterns)

**Patterns:**

| File | Title |
|---|---|
| `J01-least-privilege` | Least Privilege |
| `J02-sandbox` | Sandbox |
| `J03-secret-isolation` | Secret Isolation |
| `J04-tool-gateway` | Tool Gateway |
| `J05-deterministic-authorization` | Deterministic Authorization |
| `J06-untrusted-context-isolation` | Untrusted Context Isolation |
| `J07-session-isolation` | Session Isolation |
| `J08-human-approval-gate` | Human Approval Gate |
| `J09-external-comm-restriction` | External Communication Restriction |
| `J10-capability-minimization` | Capability Minimization |
| `J11-read-write-separation` | Read/Write Separation |

**Anti-patterns:** AP-model-as-security-boundary, AP-overpowered-coding-agent

### K — Human Control (6 patterns)

| File | Title |
|---|---|
| `K01-human-in-the-loop-checkpoint` | Human-in-the-Loop Checkpoint |
| `K02-high-risk-action-gate` | High-Risk Action Gate |
| `K03-failure-threshold-escalation` | Failure-Threshold Escalation |
| `K04-review-before-side-effect` | Review Before Side Effect |
| `K05-draft-preview-before-apply` | Draft/Preview Before Apply |
| `K06-human-on-the-loop-monitoring` | Human-on-the-Loop Monitoring |

### L — Memory & State (9 patterns)

| File | Title |
|---|---|
| `artifact-state` | Artifact State |
| `checkpoint-state` | Checkpoint State |
| `external-durable-state` | External Durable State |
| `provenance-tagged-memory` | Provenance-Tagged Memory |
| `scoped-memory` | Scoped Memory |
| `session-isolation` | Session Isolation |
| `shared-memory-gateway` | Shared-Memory Gateway |
| `state-machine` | State Machine |
| `summarized-memory` | Summarized Memory |

### M — Observability & Debugging (9 patterns, 1 anti-pattern, 2 guides)

**Patterns:**

| File | Title |
|---|---|
| `M01-structured-trace` | Structured Trace |
| `M02-tool-call-event-log` | Tool-Call Event Log |
| `M03-execution-tree` | Agent/Subagent Execution Tree |
| `M04-instrumented-handoff` | Instrumented Handoff |
| `M05-artifact-lineage` | Artifact Lineage |
| `M06-token-cost-metrics` | Token/Cost Metrics |
| `M07-replayable-run` | Replayable Run |
| `M08-trace-linked-eval` | Trace-Linked Eval |
| `M09-failure-categorization` | Failure Categorization |

**Anti-patterns:** AP-generic-evals-before-analysis
**Guides:** debugging-runbook, observability-stack

### N — Efficiency & Model Routing (9 patterns, 2 anti-patterns)

**Patterns:**

| File | Title |
|---|---|
| `budgeted-agent-loop` | Budgeted Agent Loop |
| `caching` | Caching |
| `complexity-based-model-routing` | Complexity-Based Model Routing |
| `confidence-based-routing` | Confidence-Based Routing |
| `context-minimization` | Context Minimization |
| `cost-aware-stopping` | Cost-Aware Stopping |
| `parallel-execution` | Parallel Execution |
| `small-model-first-escalation` | Small-Model-First Escalation |
| `tool-result-reuse` | Tool/Result Reuse |

**Anti-patterns:** premature-optimization, silent-quality-degradation

### O — Output & Integration Boundaries (6 patterns)

| File | Title |
|---|---|
| `parse-and-reject` | Parse-and-Reject |
| `programmatic-postcondition` | Programmatic Postcondition |
| `sanitized-output-boundary` | Sanitized Output Boundary |
| `schema-validation` | Schema Validation |
| `structured-output-boundary` | Structured Output Boundary |
| `typed-result-object` | Typed Result Object |

---

## Anti-Patterns (top-level, AP01–AP10)

| ID | Title |
|---|---|
| AP01 | Self-Certified Completion |
| AP02 | Prompt-as-Policy |
| AP03 | Giant Instruction Manual |
| AP04 | Retry Without New Information |
| AP05 | Multi-Agent by Default |
| AP06 | Model as Security Boundary |
| AP07 | Shared Context Everywhere |
| AP08 | Generic Evals Before Error Analysis |
| AP09 | Infinite / Weakly Bounded Agent Loop |
| AP10 | Overpowered Coding Agent |

Note: AP03, AP04, AP05, AP06, AP07, AP08, AP09, AP10 also appear as family-level anti-patterns in their respective families (E, I, C, J, E, M, I, J).

---

## Principles (P1–P8)

| ID | Title |
|---|---|
| P1 | Prefer Determinism Where the Problem Is Deterministic |
| P2 | Complexity Must Earn Its Keep |
| P3 | Give Agents Ground Truth |
| P4 | Separate Generation From Verification |
| P5 | Context Is a Designed Resource |
| P6 | Security Boundaries Belong Outside the Model |
| P7 | Measure Real Task Success |
| P8 | Failures Should Improve the Harness |

Cross-reference: `principles/index.md` maps principles × families × anti-patterns.

---

## Use Cases (26 articles across 8 categories)

### Debugging (5 files)
| File | What it covers |
|---|---|
| `agent-not-completing` | Agent hangs, loops, or never finishes |
| `context-problems` | Context-related failures |
| `non-determinism` | Same input, different outputs |
| `tool-failures` | Tool call failures and errors |
| `wrong-outputs` | Decision tree: wrong output type → fix pattern |

### Decision Trees (3 files)
| File | What it covers |
|---|---|
| `anti-pattern-detector` | Symptom → anti-pattern lookup with diagnostic questions, compound anti-patterns |
| `architecture-choices` | Architecture decision tree |
| `which-family` | Which family applies to your situation |

### Cost & Performance (3 files)
| File | What it covers |
|---|---|
| `reducing-cost` | Cost reduction checklist: high/medium/lower impact tiers + decision tree |
| `latency` | Latency optimization |
| `routing-and-scaling` | Routing and scaling strategies |

### Designing (5 files)
| File | What it covers |
|---|---|
| `new-system` | Starting from scratch |
| `multi-agent` | Multi-agent system design |
| `tool-design` | Tool interface design |
| `memory-and-state` | Memory/state design decisions |
| `output-integration` | Output integration design |

### Evaluation (3 files)
| File | What it covers |
|---|---|
| `evaluating-agents` | How to evaluate agent performance |
| `evals-from-errors` | Building evals from observed errors |
| `regression-testing` | Regression test strategy |

### Human-in-the-Loop (2 files)
| File | What it covers |
|---|---|
| `approval-workflows` | Approval workflow design |
| `when-to-interrupt` | When human intervention is needed |

### Onboarding (2 files)
| File | What it covers |
|---|---|
| `new-to-agents` | Starting guide for agent newcomers |
| `mental-models` | Mental models for agent systems |

### Security (3 files)
| File | What it covers |
|---|---|
| `privilege-and-trust` | Privilege and trust boundary design |
| `prompt-injection` | Prompt injection defenses |
| `security-review` | Security review checklist |

---

## Contributing / Meta (5 files)

| File | Purpose |
|---|---|
| `source-registry.md` | 30 verified source URLs + family-source mapping |
| `authoring-guide.md` | How to write pattern files |
| `catalog-intake.md` | How to add new patterns to the catalog |
| `classification-guide.md` | How to classify patterns into families |
| `README.md` | Contributing overview |

---

## Input (1 file)

| File | Purpose |
|---|---|
| `ai_agent_design_patterns_discovery.md` | Raw research the catalog was built from |

---

## Source Registry Summary

The registry lists 30 sources across four categories.

| Category | Sources | Examples |
|---|---|---|
| Primary (high-authority) | 18 | Anthropic (4), OpenAI (5), Google (1), Microsoft (1), AWS (4), OWASP (3) |
| Practitioner / Expert | 8 | Hamel Husain (4), Simon Willison (2), Matt Pocock (2) |
| Academic / Educational | 2 | Stanford CS224G, Samman Coaching |
| Open Source | 2 | AWS Samples repo, Moby AI usage policy |

Selected research is now adapted into four existing patterns (Fresh-Context Retry, B5, Retry-With-Feedback, D05) and the new Clarify Domain Terms guide. Their practical session sections, examples, limits, and source attribution are bundled locally; full source articles are not bundled.

---

Last updated: 2026-11-21
