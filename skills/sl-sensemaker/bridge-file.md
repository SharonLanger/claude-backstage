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

Zone 2 and Zone 3 are already well-served by the catalog's existing navigation ([catalog-lookup.md](catalog/catalog-lookup.md), [use-cases/README.md](catalog/use-cases/README.md)). This bridge file focuses on **Zone 1** — practitioner symptoms, including direct session procedures and explicitly partial matches.

---

## Zone 1: Practitioner Symptom Routing Table

### Route from the person's control surface

Start with what the person can observe and do in their current chat or CLI. Read only the relevant entry or subsection, then its limits. Do not require a new harness, multi-agent system, or code-based gate unless the person controls that system and needs that stronger boundary.

The rows are candidates, not diagnoses. “Partial” means the entry answers only the stated part; “Gap” means there is no matching practitioner remedy here. Say what is missing rather than presenting related architecture guidance as a complete answer. These examples describe problems; they are not proof of a particular model mechanism.

### 1A — Output, intent, and feedback

| User says something like… | Check before advising | Read first / coverage |
|---|---|---|
| "Agent fixes one bug but creates another" / "fixes the test instead of the code" / "deletes failing tests" / "changes assertions instead of fixing the bug" / "coverage is high but I don't trust it" | Inspect the requirement, implementation, changed assertions, and removed checks. A legitimate requirement change can justify a test change; deletion alone does not establish motive. | [Human review pass](catalog/families/D-verification-evaluation/patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them); [Feedback into a check](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check). Only if configured write scope is part of the problem: [AP10](catalog/anti-patterns/AP10-overpowered-coding-agent.md). |
| "Agent says it verified but it didn't actually check" / "claims done but the output is wrong" | Separate a reported result from observable execution. Find what was run and what it established. | [Evidence-based completion](catalog/families/D-verification-evaluation/patterns/D03-evidence-based-completion.md); [Human review pass](catalog/families/D-verification-evaluation/patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them). |
| "Agent hallucinates APIs/methods that don't exist" / "invents function signatures" / "uses outdated syntax" / "I keep correcting the same library usage" | Check the actual installed version and relevant API docs before choosing a repair. | [Reconnaissance first](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md); [Just-in-time retrieval](catalog/families/E-context-engineering/patterns/just-in-time-retrieval.md); [Feedback into a check](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check). |
| "I want a safe place to try the API before changing the project" | Check whether an isolated experiment can establish the uncertain behavior. A sandbox's protections depend on configuration. | [Sandboxed execution](catalog/families/F-harness-environment/patterns/F08-sandboxed-execution.md). Partial: infrastructure guidance, not a complete chat-only practice. |
| "It says yes but misunderstood me" / "implements before I notice" / "accepted contradictory requirements without pushing back" / "never challenges a bad request" | Use one case with competing expected outcomes. Determine who can settle the requirement before implementation. | [Clarify domain terms](catalog/families/E-context-engineering/guides/clarify-domain-terms.md); [Draft/preview before apply](catalog/families/K-human-control/patterns/K05-draft-preview-before-apply.md). Partial: does not establish a general remedy for uncritical agreement. |
| "It followed my words but missed the goal" / "feedback was technically satisfied but the result is useless" | Separate the intended result from the proposed fix; use a case where literal compliance fails the goal. | [Feedback into a check](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check); [Clarify domain terms](catalog/families/E-context-engineering/guides/clarify-domain-terms.md). |
| "It improved code that was intentionally written that way" / "forgot why we made that decision" | Locate the rationale and confirm whether it still governs. Do not invent a justification for old code. | [Clarify domain terms](catalog/families/E-context-engineering/guides/clarify-domain-terms.md); [Recover a drifting session](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work); [Repository as system of record](catalog/families/E-context-engineering/patterns/repository-as-system-of-record.md). |
| "Its first explanation became fact" / "it fixes things based on an unverified assumption" / "I told it exactly how to solve it and the result was bad" / "I described the solution in my prompt" | Distinguish an observed failure from a guessed cause. Inspect evidence before another edit. | [Reconnaissance first](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md); [Feedback into a check](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check); [Root cause before retry](catalog/families/I-reliability-recovery/patterns/root-cause-before-retry.md). |
| "Same prompt gives different results each time" / "works sometimes and fails sometimes" | Compare task inputs, retrieved context, tools, and acceptance checks as well as model settings; do not assume one cause. | [Non-determinism troubleshooting](catalog/use-cases/debugging/non-determinism.md); [Evidence-based completion](catalog/families/D-verification-evaluation/patterns/D03-evidence-based-completion.md). Partial: much of the destination concerns system controls. |

### 1B — Human workflow and review

| User says something like… | Check before advising | Read first / coverage |
|---|---|---|
| "I just accept what the AI writes" / "I stopped reading the code" / "prompt → light edit → ship" / "the AI does 95% of the work" / "reviewing generated tests is overwhelming" | Find the smallest behavior and diff the person can inspect and explain. Test execution and human understanding answer different questions. | [Reviewable milestones](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review); [Human review pass](catalog/families/D-verification-evaluation/patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them). |
| "The AI made a massive change and I can't review it" / "PR is 2000 lines, all AI-generated" / "too much code" | Split by observable behavior and real dependencies. Preserve the existing patch before reorganizing it; line count is not the target. | [Reviewable milestones](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review); [Human review pass](catalog/families/D-verification-evaluation/patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them). |
| "Big tasks lose requirements" / "one session handles too many responsibilities" / "small errors compound" / "quality drops as the codebase grows" | Check whether the task has observable milestones and relevant context. Repository size alone does not identify the cause. | [Reviewable milestones](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review); [Reconnaissance first](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md). Partial: neither covers every source of large-repository failure. |
| "Agent ignores my instructions" / "I told it not to do X" / "important steps get skipped" / "I can't tell whether it followed the rules" | Find a concrete violated expectation and the evidence needed to check it. A prompt is not an enforced restriction. | [Feedback into a check](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check); [Evidence-based completion](catalog/families/D-verification-evaluation/patterns/D03-evidence-based-completion.md). For an actual mandatory boundary the user controls, consult [Programmatic gate](catalog/families/H-deterministic-control/patterns/H02-programmatic-gate.md). |
| "Response is way too long" / "200 lines when I need 10" / "drowns me in explanation" / "wrong level of detail" / "I struggle to explain what I need" / "domain experts and developers mean different things" | Distinguish output length, missing task context, and conflicting domain meaning. | [Clarify domain terms](catalog/families/E-context-engineering/guides/clarify-domain-terms.md) covers meanings; [Feedback into a check](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check) covers revising an existing response against an explicit expectation. Partial: no dedicated communication-level guide. |
| "I lead with my answer" / "we never explore alternatives" / "the conversation drifts" | Separate a required constraint from a suggested implementation. Check whether the agreed goal is still active. | [Reconnaissance first](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md); [Recover a drifting session](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work). Partial: no complete guide to comparing alternatives or avoiding leading questions. |
| "Repetitive chores need the same explanations" / "routine work costs too much and needs constant supervision" | Identify a stable repeatable procedure and its completion evidence. Distinguish setup cost from repeated mistakes. | [Agent skills / procedures](catalog/families/F-harness-environment/patterns/F07-agent-skills-procedures.md); [Evidence-based completion](catalog/families/D-verification-evaluation/patterns/D03-evidence-based-completion.md); see Zone 1D for cost. Partial: packaged procedures need supported tooling and do not guarantee consistent compliance. |
| "Side tasks derail me" / "too many things going at once" / "AI makes starting easy but I can't finish anything" | Identify the current deliverable and a checkpoint for returning to it. | [Reviewable milestones](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review); [Recover a drifting session](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work). Partial: task checkpoints are covered, personal work-in-progress management is not. |
| "I miss when the agent needs my input" / "it asks me to do things it could do itself" / "it doesn't use the tools/files I set up" | Check the requested decision, actual access, discoverability, and configured permissions. Human authorization is not interchangeable with a tool capability. | [Human escalation](catalog/families/I-reliability-recovery/patterns/human-escalation.md); [Agent-accessible tools](catalog/families/F-harness-environment/patterns/F05-agent-accessible-tools.md). Partial: escalation/tool design; no complete practitioner notification or delegation guide. |
| "I prefer AI over teammates" / "I don't need pair programming anymore" / "shared understanding is declining" / "docs and diagrams drift from the work" | Distinguish stale artifacts from loss of team discussion and shared understanding. | [Repository as system of record](catalog/families/E-context-engineering/patterns/repository-as-system-of-record.md); [Human review pass](catalog/families/D-verification-evaluation/patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them) address inspectable artifacts and personal ownership. Gap: neither establishes a remedy for team isolation or maintains diagrams automatically. |

### 1C — Context and session management

| User says something like… | Check before advising | Read first / coverage |
|---|---|---|
| "I repeat my preferences and project facts" / "corrections disappear next session" / "reset loses the plan" / "design drifts across sessions" / "forgets architectural decisions from yesterday" | Check what was saved, whether it is still current, and whether the next session actually loaded it. | [Recover a drifting session](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work); [Repository as system of record](catalog/families/E-context-engineering/patterns/repository-as-system-of-record.md). A checked handoff can be pasted into a chat when file access is unavailable. |
| "Earlier instructions are ignored" / "I need it to remember X from earlier" / "long session quality got worse" / "early on it's sharp, later sloppy" / "research or tool output buries the task" / "context window is filling" | Look for the specific lost requirement or competing material. Session length alone is not a reason to reset. | [Recover a drifting session](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work); [Context compaction](catalog/families/E-context-engineering/patterns/context-compaction.md); [Context offloading](catalog/families/E-context-engineering/patterns/context-offloading.md). |
| "It returns to the same decision we abandoned" / "I tell it to change approach and it reverts" / "keeps doing the same thing after correction" / "20 messages and getting worse" / "keep trying or start over?" | Confirm the settled decision, rejected option, and evidence. Keep useful edits separate from the conversation being reset. | [Recover a drifting session](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work); [Feedback into a check](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check). No fixed message-count reset rule. |
| "My CLAUDE.md / system prompt is huge" / "I keep adding rules and it gets worse" / "saved notes contradict each other or are outdated" | Identify the current authoritative instruction and conflicting notes before adding more text. | [Map-not-manual](catalog/families/E-context-engineering/patterns/map-not-manual.md); [Repository as system of record](catalog/families/E-context-engineering/patterns/repository-as-system-of-record.md); [Clarify domain terms](catalog/families/E-context-engineering/guides/clarify-domain-terms.md) for unresolved meaning. Partial: a smaller map still needs current content and actual retrieval. |
| "How do I pass information between agents without losing it?" | Inspect which facts the recipient needs and whether the handoff preserves decisions and open questions. | [Artifact-based handoff](catalog/families/E-context-engineering/patterns/artifact-based-handoff.md); [Minimal-context handoff](catalog/families/E-context-engineering/patterns/minimal-context-handoff.md). For a person's next session, start with [Recover a drifting session](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work). |


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

## Compound problems

When several rows match, choose the first unresolved question rather than assigning a model or human bias.

| Observed combination | Start with | Then |
|---|---|---|
| Agent modifies tests and says the bug is fixed | [Human review pass](catalog/families/D-verification-evaluation/patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them): inspect the changed assertion against the requirement | [Feedback into a check](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check): check the original failure and neighboring behavior |
| Session forgets decisions and repeats rejected approaches | [Recover a drifting session](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work): reconcile decisions and preserve useful work | [Clarify domain terms](catalog/families/E-context-engineering/guides/clarify-domain-terms.md) if the requirement itself is still ambiguous |
| Large diff and the person no longer understands the code | [Reviewable milestones](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review): select a reviewable behavior | [Human review pass](catalog/families/D-verification-evaluation/patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them): explain and check that change |
| Retry loop adds cost without progress | [Root cause before retry](catalog/families/I-reliability-recovery/patterns/root-cause-before-retry.md) | [Stop condition](catalog/families/I-reliability-recovery/patterns/stop-condition.md); reset only if session recovery fits |
| More rules, stale notes, and conflicting behavior | [Repository as system of record](catalog/families/E-context-engineering/patterns/repository-as-system-of-record.md): find the governing record | [Map-not-manual](catalog/families/E-context-engineering/patterns/map-not-manual.md): make relevant records discoverable |
| Works on a small example but fails on a real repository | [Reconnaissance first](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md): inspect the actual task, version, and context | Choose the specific output, context, or task-size row after finding the mismatch |

---

## Extending the bridge

When a new pattern is approved for the catalog, add its local file to the rows it answers. Test the route from the engineer's symptom through the lookup to the entry. If an entry covers only part of the symptom, keep that limit explicit in the answer.

