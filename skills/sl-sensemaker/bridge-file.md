# Symptom-to-Catalog Bridge — Skill Internal Routing Table

## Purpose

This file is the **Phase 2 lookup** for the AI working patterns skill. After Phase 1 (understand the user's question), the skill reads this file to translate natural-language symptoms into candidate catalog entries. Use the explanations only as search hints and read the entries before giving advice.

This is NOT a user-facing document. It's a routing table the skill uses internally.

---

## How the skill uses this file

1. User describes a problem in Phase 1
2. Skill identifies keywords / intent from the conversation
3. Skill scans the **Symptom Routing Table** below for matching rows
4. Skill reads the relevant catalog entries
5. Skill synthesizes a tailored answer in Phase 3

Multiple rows may match — compound problems are the norm, not the exception.

---

## Routing Zones

The table is split into three zones. Most real questions land in Zone 1 or Zone 2; Zone 3 is for users who already know what they want.

| Zone | User arrives with... | Example |
|------|---------------------|---------|
| **Zone 1 — Practitioner symptoms** | A behavior they observe while working with AI | "My agent keeps deleting tests instead of fixing bugs" |
| **Zone 2 — System design questions** | An architecture or design decision | "Should I use multiple agents or one?" |
| **Zone 3 — Named concept lookup** | A specific pattern/concept name | "Tell me about context engineering" |

Zone 2 and Zone 3 are already well-served by the catalog's existing navigation ([catalog-lookup.md](catalog/catalog-lookup.md), [use-cases/README.md](catalog/use-cases/README.md)). This bridge file focuses on **Zone 1** — the practitioner symptoms that the catalog can't route today.

---

## Zone 1: Practitioner Symptom Routing Table

### 1A — Agent produces bad output

| User says something like... | What's actually happening | Why (LLM behavior) | Read these |
|---|---|---|---|
| "Agent fixes one bug but creates another" / "fixes the test instead of the code" / "deletes failing tests" | Agent has write access to tests + self-certifies completion. Optimizes for "no failures" by any path, including deleting evidence. | **Compliance bias** — the model optimizes for appearing helpful. Removing a failing test is the shortest path to "all tests pass." Combined with **obedient contractor** — prioritizes quick completion over correctness. | [AP01](catalog/anti-patterns/AP01-self-certified-completion.md), [AP10](catalog/anti-patterns/AP10-overpowered-coding-agent.md), [D02-test-before-done](catalog/families/D-verification-evaluation/patterns/D02-test-before-done.md), [J01-least-privilege](catalog/families/J-security-trust/patterns/J01-least-privilege.md), [H02-programmatic-gate](catalog/families/H-deterministic-control/patterns/H02-programmatic-gate.md) |
| "Agent says it verified but it didn't actually check" / "claims done but the output is wrong" | No deterministic verification. Agent self-reports success. | **Compliance bias** + **obedient contractor** — agent treats "report success" as the task, not "achieve success." Self-certification is the path of least resistance. | [AP01](catalog/anti-patterns/AP01-self-certified-completion.md), [D01-deterministic-validator](catalog/families/D-verification-evaluation/patterns/D01-deterministic-validator.md), [D03-evidence-based-completion](catalog/families/D-verification-evaluation/patterns/D03-evidence-based-completion.md), [H02-programmatic-gate](catalog/families/H-deterministic-control/patterns/H02-programmatic-gate.md) |
| "Agent hallucinates APIs/methods that don't exist" / "invents function signatures" / "uses outdated syntax" | Model generates plausible-looking code from training data patterns, not from actual API docs. | **Hallucination** — the model generates statistically likely completions, not verified facts. Code hallucinations are self-revealing (won't compile) but waste time. | [D01-deterministic-validator](catalog/families/D-verification-evaluation/patterns/D01-deterministic-validator.md), [F03-executable-feedback-loop](catalog/families/F-harness-environment/patterns/F03-executable-feedback-loop.md), [E/just-in-time-retrieval](catalog/families/E-context-engineering/patterns/just-in-time-retrieval.md), [use-cases/debugging/wrong-outputs](catalog/use-cases/debugging/wrong-outputs.md) |
| "Agent output was great at first but quality dropped" / "early in the session it's sharp, later it gets sloppy" | Context window filling up. Earlier instructions lose influence as conversation grows. | **Context rot** — instructions at the start of context lose influence as new content pushes them further from the attention head. The "effective zone" feels productive but guidance is silently deprioritized. | [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [E/progressive-disclosure](catalog/families/E-context-engineering/patterns/progressive-disclosure.md), [I/fresh-context-retry](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md), [use-cases/debugging/context-problems](catalog/use-cases/debugging/context-problems.md) |
| "Agent ignores my instructions" / "I told it not to do X and it does X anyway" | Two possible causes: (1) instruction competes with training patterns, (2) negation activates the concept. | **Selective hearing** — when your instruction contradicts millions of training examples, training wins. **Negative bleedthrough** — "don't do X" activates X in token space. Saying "don't use var" makes `var` *more* likely. | [E/role-scoped-context](catalog/families/E-context-engineering/patterns/role-scoped-context.md), [H01-deterministic-override](catalog/families/H-deterministic-control/patterns/H01-deterministic-override.md), [F06-structured-repository-instructions](catalog/families/F-harness-environment/patterns/F06-structured-repository-instructions.md) |
| "Agent keeps doing the same thing even when I correct it" / "I tell it to change approach and it reverts" | Model latches onto the first approach in context. Corrections compete with the original plan. | **Solution fixation** — the model treats its first hypothesis as a fact. Combined with **context rot** — your correction is recent but the original approach has more reinforcing tokens in context. | [I/fresh-context-retry](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md), [I/root-cause-before-retry](catalog/families/I-reliability-recovery/patterns/root-cause-before-retry.md), [B/B6-reconnaissance-first](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md) |
| "Same prompt gives different results each time" / "it works sometimes and fails sometimes" | Inherent stochastic sampling. Temperature + top-p create variation even with identical inputs. | **Non-determinism** — same input → different output is fundamental to LLM architecture. Retries may diverge rather than converge. | [use-cases/debugging/non-determinism](catalog/use-cases/debugging/non-determinism.md), [D01-deterministic-validator](catalog/families/D-verification-evaluation/patterns/D01-deterministic-validator.md), [I/bounded-retry](catalog/families/I-reliability-recovery/patterns/bounded-retry.md), [H/H01-deterministic-override](catalog/families/H-deterministic-control/patterns/H01-deterministic-override.md) |
| "Agent's response is way too long" / "gives me 200 lines when I need 10" / "drowns me in explanation" | Default training rewards comprehensive, verbose responses. | **Excess verbosity** — training data rewards thoroughness over conciseness. Secondary damage: verbose output fills context faster → accelerates context rot. | [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [E/role-scoped-context](catalog/families/E-context-engineering/patterns/role-scoped-context.md), [O/structured-output-boundary](catalog/families/O-output-integration/patterns/structured-output-boundary.md) |
| "Agent makes small errors that compound" / "each step is slightly off and by the end it's totally wrong" | Reliability drops with task size. Small errors cascade. | **Degradation under complexity** — accuracy per step multiplied across steps yields exponential error growth. A 95% per-step accuracy over 10 steps = 60% total accuracy. | [B/B5-milestone-checkpoint](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md), [D/D12-step-level-diagnostic](catalog/families/D-verification-evaluation/patterns/D12-step-level-diagnostic.md), [A/iterative-refinement](catalog/families/A-workflow-topology/patterns/iterative-refinement.md), [I/checkpoint-and-resume](catalog/families/I-reliability-recovery/patterns/checkpoint-and-resume.md) |

### 1B — Human workflow problems

| User says something like... | What's actually happening | Why (human behavior) | Read these |
|---|---|---|---|
| "I've been going back and forth for 20 messages and it's getting worse" / "should I keep trying or start over?" | Sunk cost. Continuing a failing conversation instead of restarting. Diminishing returns after 3-4 iterations. | **Sunk cost fallacy** — "I've invested so much context, starting over would waste it." But degraded context is negative value — starting fresh is cheaper than rehabilitating a poisoned conversation. | [I/fresh-context-retry](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md), [L/checkpoint-state](catalog/families/L-memory-state/patterns/checkpoint-state.md), [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md) |
| "I just accept what the AI writes, I can't keep up with reviewing everything" / "I stopped reading the code" | Throughput mismatch. AI generates faster than humans can review. Review is skipped, not accelerated. | **Flying blind / vibe coding** — the productivity gain is illusory if review is skipped. Time saved on creation is lost (or worse) on debugging unreviewed code. | [D01-deterministic-validator](catalog/families/D-verification-evaluation/patterns/D01-deterministic-validator.md), [F03-executable-feedback-loop](catalog/families/F-harness-environment/patterns/F03-executable-feedback-loop.md), [K01-human-in-the-loop-checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) |
| "I told the AI exactly how to solve it and the result was bad" / "I described the solution in my prompt" | Embedding your solution in the question limits the AI's solution space. You've constrained it to your preconceived approach. | **Answer injection** — the narrowing is invisible. You don't realize how much the AI's exploration was limited by your framing. The AI sees your solution as a constraint, not a suggestion. | [B/B6-reconnaissance-first](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md), [E/role-scoped-context](catalog/families/E-context-engineering/patterns/role-scoped-context.md) |
| "I have too many things going at once" / "AI makes it so easy to start things but I can't finish any" | AI lowers friction for starting work, creating task overload. | **Cognitive overload** — AI eliminates the natural friction that previously limited work-in-progress. Starting is cheap; finishing and integrating is still expensive. Damage is at team level: everyone loses the shared picture. | [B/B5-milestone-checkpoint](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md), [K01-human-in-the-loop-checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) |
| "I prefer working with AI over my teammates" / "I don't need pair programming anymore" | Ask whether the concern is team knowledge sharing, human oversight of agent actions, or the quality of automated evaluations. | The catalog covers monitoring and evaluation. The effect on team knowledge sharing is a gap. | For monitoring agent actions, read [Human-on-the-Loop Monitoring](catalog/families/K-human-control/patterns/K06-human-on-the-loop-monitoring.md). For calibrating automated judges against human judgments, read [Human Calibration](catalog/families/D-verification-evaluation/patterns/D10-human-calibration.md). |
| "I just prompt → light edit → ship" / "the AI does 95% of the work" | Using AI output without adding human judgment. The "slop test": if anyone with your prompt gets the same result, you added no value. | **AI slop** — the risk isn't bad code (tests catch that). The risk is losing the understanding of *why* the code works, making future changes blind. | [D/D10-human-calibration](catalog/families/D-verification-evaluation/patterns/D10-human-calibration.md), [K01-human-in-the-loop-checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md), [F03-executable-feedback-loop](catalog/families/F-harness-environment/patterns/F03-executable-feedback-loop.md) |
| "The AI made a massive change and I can't review it" / "PR is 2000 lines, all AI-generated" | AI enables massive changes that are impossible to review. No incremental delivery discipline. | **Big chunk working** — timeline compression: three months of solo spiraling now happens in days, but reviewers still bear the full cognitive cost. | [B/B5-milestone-checkpoint](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md), [K/K01-human-in-the-loop-checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md), [K/K04-review-before-side-effect](catalog/families/K-human-control/patterns/K04-review-before-side-effect.md) |
| "I keep adding more rules to CLAUDE.md but it doesn't help" / "the more instructions I give, the worse it gets" | Rules compete for limited attention in context. More rules = worse compliance per rule. | **Obsessing over rules** — each instruction dilutes every other instruction. Large initial context also accelerates context rot. The fix is mechanical enforcement (code), not more words (prompts). | [AP03](catalog/anti-patterns/AP03-giant-instruction-manual.md), [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [E/progressive-disclosure](catalog/families/E-context-engineering/patterns/progressive-disclosure.md), [H01-deterministic-override](catalog/families/H-deterministic-control/patterns/H01-deterministic-override.md), [F/F04-mechanical-architecture-constraints](catalog/families/F-harness-environment/patterns/F04-mechanical-architecture-constraints.md) |
| "AI agreed with something that doesn't make sense" / "it accepted contradictory requirements without pushing back" | AI's compliance bias means it won't flag contradictions. Misalignment goes undetected. | **Silent misalignment** — the hardest part is suspecting misalignment exists. The AI accepted your contradictions because pushing back would conflict with being "helpful." | [D/D03-evidence-based-completion](catalog/families/D-verification-evaluation/patterns/D03-evidence-based-completion.md), [D/D06-generator-critic](catalog/families/D-verification-evaluation/patterns/D06-generator-critic.md), [H/H02-programmatic-gate](catalog/families/H-deterministic-control/patterns/H02-programmatic-gate.md) |

### 1C — Context and session management

| User says something like... | What's actually happening | Why | Read these |
|---|---|---|---|
| "Design drifts when I work across sessions" / "agent forgets architectural decisions from yesterday" | No persistent design constraints enforced mechanically. Earlier decisions lose influence. | **Context rot** across sessions + **no external state**. Context only lives within a session. Between sessions, the agent starts cold. Unless decisions are written to durable files, they evaporate. | [L/external-durable-state](catalog/families/L-memory-state/patterns/external-durable-state.md), [F06-structured-repository-instructions](catalog/families/F-harness-environment/patterns/F06-structured-repository-instructions.md), [L/checkpoint-state](catalog/families/L-memory-state/patterns/checkpoint-state.md), [use-cases/debugging/context-problems](catalog/use-cases/debugging/context-problems.md) |
| "My CLAUDE.md / system prompt is huge and the agent still ignores half of it" | Context overload. Instructions compete for attention. | **Limited attention** + **AP03 giant instruction manual**. Loading everything upfront means everything competes. The more you load, the less reliable any single instruction becomes. | [AP03](catalog/anti-patterns/AP03-giant-instruction-manual.md), [E/progressive-disclosure](catalog/families/E-context-engineering/patterns/progressive-disclosure.md), [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [F/F06-structured-repository-instructions](catalog/families/F-harness-environment/patterns/F06-structured-repository-instructions.md) |
| "I need the agent to remember X from earlier in the conversation" | Information has fallen out of the effective context zone or been compacted away. | **Context rot** — the "focus zone" (recent tokens) gets full attention; the "effective zone" (middle) gets partial; the "red zone" (old) gets almost none. Your earlier instruction is in the red zone. | [L/scoped-memory](catalog/families/L-memory-state/patterns/scoped-memory.md), [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [L/summarized-memory](catalog/families/L-memory-state/patterns/summarized-memory.md), [use-cases/debugging/context-problems](catalog/use-cases/debugging/context-problems.md) |
| "Context window is filling up, how do I manage it?" | Direct context engineering question. | Not a failure mode — this is a design challenge. Context is a scarce resource that needs active management. | [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [E/context-offloading](catalog/families/E-context-engineering/patterns/context-offloading.md), [E/context-isolation](catalog/families/E-context-engineering/patterns/context-isolation.md), [E/role-scoped-context](catalog/families/E-context-engineering/patterns/role-scoped-context.md), [use-cases/debugging/context-problems](catalog/use-cases/debugging/context-problems.md) |
| "How do I pass information between agents without losing it?" | Handoff loss between agents. Information degrades at each hop. | Each handoff is a lossy compression. The sending agent summarizes; the receiving agent interprets the summary. Two levels of lossy inference. | [E/minimal-context-handoff](catalog/families/E-context-engineering/patterns/minimal-context-handoff.md), [E/artifact-based-handoff](catalog/families/E-context-engineering/patterns/artifact-based-handoff.md), [L/shared-memory-gateway](catalog/families/L-memory-state/patterns/shared-memory-gateway.md), [AP07](catalog/anti-patterns/AP07-shared-context-everywhere.md) |
| "Agent doesn't use the tools/files I set up for it" | Agent doesn't know the tools/files exist, or the tool descriptions don't match the agent's vocabulary. | **Selective hearing** (the agent's training patterns don't map to your tool names) + poor tool discoverability. The agent can only use tools it can find and understand. | [G/G09-tool-discovery-progressive-exposure](catalog/families/G-tool-action-design/patterns/G09-tool-discovery-progressive-exposure.md), [F/F05-agent-accessible-tools](catalog/families/F-harness-environment/patterns/F05-agent-accessible-tools.md), [F/F01-agent-legible-repository](catalog/families/F-harness-environment/patterns/F01-agent-legible-repository.md) |

### 1D — Cost, performance, and scaling

| User says something like... | What's actually happening | Why | Read these |
|---|---|---|---|
| "My agent costs too much" / "token usage is way too high" | Need to decompose: is it the model tier, the context size, the retry count, or the agent count? | Phase 1 should clarify *which* cost driver before routing. Skill asks: how many agents, what model, how many retries, how big is the context? | [use-cases/cost-and-performance/reducing-cost](catalog/use-cases/cost-and-performance/reducing-cost.md), [N/cost-aware-stopping](catalog/families/N-efficiency-routing/patterns/cost-aware-stopping.md), [N/complexity-based-model-routing](catalog/families/N-efficiency-routing/patterns/complexity-based-model-routing.md), [N/context-minimization](catalog/families/N-efficiency-routing/patterns/context-minimization.md) |
| "Agent is too slow" / "takes forever to respond" | Latency question — could be model size, sequential steps, or unnecessary round-trips. | Again needs Phase 1 clarification. Common causes: sequential when parallel is possible, large model for simple tasks, sending too much context. | [use-cases/cost-and-performance/latency](catalog/use-cases/cost-and-performance/latency.md), [N/parallel-execution](catalog/families/N-efficiency-routing/patterns/parallel-execution.md), [N/small-model-first-escalation](catalog/families/N-efficiency-routing/patterns/small-model-first-escalation.md), [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md) |
| "We have too many agents and it's expensive" | Multi-agent overhead without proportional quality gain. | **AP05 multi-agent by default** — each agent adds latency + token cost. If agents aren't genuinely specialized, consolidate. | [AP05](catalog/anti-patterns/AP05-multi-agent-by-default.md), [use-cases/cost-and-performance/reducing-cost](catalog/use-cases/cost-and-performance/reducing-cost.md), [C/do-you-need-multi-agent](catalog/families/C-orchestration/guides/do-you-need-multi-agent.md), [N/complexity-based-model-routing](catalog/families/N-efficiency-routing/patterns/complexity-based-model-routing.md) |

### 1E — Security and trust

| User says something like... | What's actually happening | Why | Read these |
|---|---|---|---|
| "Agent has access to everything" / "I'm worried about what it can do" | Overpowered agent — too many capabilities in one context. | **AP10** — the conjunction of private data + untrusted content + external comms is the security trifecta. Any two is manageable; all three is dangerous. | [AP10](catalog/anti-patterns/AP10-overpowered-coding-agent.md), [J01-least-privilege](catalog/families/J-security-trust/patterns/J01-least-privilege.md), [J02-sandbox](catalog/families/J-security-trust/patterns/J02-sandbox.md), [J10-capability-minimization](catalog/families/J-security-trust/patterns/J10-capability-minimization.md), [use-cases/security/privilege-and-trust](catalog/use-cases/security/privilege-and-trust.md) |
| "Can the agent be tricked by input?" / "what about prompt injection?" | Prompt injection concern. | Untrusted input in agent context is a fundamental problem. The model can't reliably distinguish instructions from data. | [J06-untrusted-context-isolation](catalog/families/J-security-trust/patterns/J06-untrusted-context-isolation.md), [use-cases/security/prompt-injection](catalog/use-cases/security/prompt-injection.md), [O/sanitized-output-boundary](catalog/families/O-output-integration/patterns/sanitized-output-boundary.md) |
| "How do I add approval gates?" / "I want human review before the agent acts" | Human control design question. | Not a failure — this is good design. The question is *where* to put gates (high-risk actions vs. every action). | [K/K01-human-in-the-loop-checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md), [K/K02-high-risk-action-gate](catalog/families/K-human-control/patterns/K02-high-risk-action-gate.md), [K/K04-review-before-side-effect](catalog/families/K-human-control/patterns/K04-review-before-side-effect.md), [use-cases/human-in-the-loop/approval-workflows](catalog/use-cases/human-in-the-loop/approval-workflows.md) |

### 1F — Evaluation and testing

| User says something like... | What's actually happening | Why | Read these |
|---|---|---|---|
| "How do I know if my agent is working?" / "what should I measure?" | Starting eval from scratch. | Start with real failures, not generic metrics. The most common mistake is adopting standard ML metrics before understanding what actually goes wrong. | [AP08](catalog/anti-patterns/AP08-generic-evals-before-error-analysis.md), [use-cases/evaluation/evaluating-agents](catalog/use-cases/evaluation/evaluating-agents.md), [D/D11-end-to-end-task-success](catalog/families/D-verification-evaluation/patterns/D11-end-to-end-task-success.md), [M/M09-failure-categorization](catalog/families/M-observability-debugging/patterns/M09-failure-categorization.md) |
| "Tests pass but users complain" / "evals look fine but something is off" | Eval-reality gap. Metrics don't capture what users care about. | **AP08** — generic evals before error analysis. You're measuring the wrong thing. Build evals FROM production failures, not from academic benchmarks. | [AP08](catalog/anti-patterns/AP08-generic-evals-before-error-analysis.md), [use-cases/evaluation/evals-from-errors](catalog/use-cases/evaluation/evals-from-errors.md), [D/D10-human-calibration](catalog/families/D-verification-evaluation/patterns/D10-human-calibration.md), [N/silent-quality-degradation](catalog/families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) |
| "Agent worked yesterday but broke today" / "regression after model update" | Regression — behavior changed without code change. | Model updates, temperature drift, or context changes can all cause regressions. Need deterministic anchors. | [use-cases/evaluation/regression-testing](catalog/use-cases/evaluation/regression-testing.md), [D/D02-test-before-done](catalog/families/D-verification-evaluation/patterns/D02-test-before-done.md), [H/H03-structural-test](catalog/families/H-deterministic-control/patterns/H03-structural-test.md) |

---

## Zone 2: System Design Questions (catalog redirect)

These questions are already well-routed by the catalog. The skill should redirect to existing navigation.

| User asks about... | Redirect to |
|---|---|
| Workflow design (sequential, parallel, DAG) | [catalog-lookup.md](catalog/catalog-lookup.md) → "I have a problem to solve" → Family A |
| Multi-agent architecture | [use-cases/designing/multi-agent.md](catalog/use-cases/designing/multi-agent.md) + [C/do-you-need-multi-agent](catalog/families/C-orchestration/guides/do-you-need-multi-agent.md) |
| Tool design for agents | [use-cases/designing/tool-design.md](catalog/use-cases/designing/tool-design.md) + Family G |
| Memory and state design | [use-cases/designing/memory-and-state.md](catalog/use-cases/designing/memory-and-state.md) + Family L |
| Starting from scratch | [use-cases/designing/new-system.md](catalog/use-cases/designing/new-system.md) |
| Security review | [use-cases/security/security-review.md](catalog/use-cases/security/security-review.md) |

---

## Zone 3: Named Concept Lookup (direct file access)

When the user asks about a specific named pattern, family, or concept — go directly to that file. No routing needed.

Examples:
- "Tell me about prompt chaining" → [families/A-workflow-topology/patterns/prompt-chaining.md](catalog/families/A-workflow-topology/patterns/prompt-chaining.md)
- "What is AP01?" → [anti-patterns/AP01-self-certified-completion.md](catalog/anti-patterns/AP01-self-certified-completion.md)
- "Explain context engineering" → [families/E-context-engineering/README.md](catalog/families/E-context-engineering/README.md)

---

## Compound Problem Patterns

Most real problems involve 2-3 interacting issues. These are the most common combinations.

| Compound symptom | Primary issue | Secondary issue | Tertiary issue |
|---|---|---|---|
| "Agent modifies tests to pass instead of fixing the bug" | Compliance bias (agent optimizes for no-failures) | Self-certified completion (no external check) | Overpowered agent (has write access to tests) |
| "Quality was fine, then gradually degraded, now it's wrong" | Context rot (quality drops) | Excess verbosity (fills context faster) | Solution fixation (latches onto degraded approach) |
| "Agent loops forever and costs a fortune" | Infinite loop (no real stop condition) | Retry without new info (same approach each time) | No deterministic validation (can't tell when done) |
| "I keep adding rules but agent gets worse" | Giant instruction manual (AP03) | Limited attention (rules compete) | Context rot (rules accelerate degradation) |
| "Agent works in testing but fails on real repos" | Missing harness (test env has ideal context) | Context overload (real repo has more files) | Selective hearing (real repo has conflicting patterns) |
| "I can't keep up with what the agent produces" | Throughput mismatch (flying blind) | Big chunk working (massive changes) | Cognitive overload (too many parallel tasks) |

---

## Extending the bridge

When a new pattern is approved for the catalog, add its local file to the rows it answers. Test the route from the engineer's symptom through the lookup to the entry. If an entry covers only part of the symptom, keep that limit explicit in the answer.
