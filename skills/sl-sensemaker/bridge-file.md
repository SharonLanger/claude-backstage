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

Multiple rows may match. Explanations are hypotheses. Use a distinction only when it helps select an entry, and check that the user has the controls the entry requires.

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

| User says something like… | What to check or consider | Read these |
|---|---|---|
| "Agent fixes one bug but creates another" / "fixes the test instead of the code" / "deletes failing tests" / "it changes assertions instead of fixing the code" / "it deleted the regression test and introduced another bug" | If the task did not require test edits, check what the agent could write. If a protected baseline exists, check whether the fix passes it and whether independent checks cover the new bug. | [AP10 — Overpowered Coding Agent](catalog/anti-patterns/AP10-overpowered-coding-agent.md), [D02 — Test-Before-Done](catalog/families/D-verification-evaluation/patterns/D02-test-before-done.md) |
| "Agent says it verified but it didn't actually check" / "claims done but the output is wrong" | Check what evidence was produced and whether someone or something independent can inspect it. | [AP01](catalog/anti-patterns/AP01-self-certified-completion.md), [D01-deterministic-validator](catalog/families/D-verification-evaluation/patterns/D01-deterministic-validator.md), [D03-evidence-based-completion](catalog/families/D-verification-evaluation/patterns/D03-evidence-based-completion.md), [H02-programmatic-gate](catalog/families/H-deterministic-control/patterns/H02-programmatic-gate.md) |
| "Agent hallucinates APIs/methods that don't exist" / "invents function signatures" / "uses outdated syntax" | Check which library version is installed and whether the agent can retrieve relevant docs or run checks. Validation may miss a valid API used for the wrong operation. | [Just-in-Time Retrieval](catalog/families/E-context-engineering/patterns/just-in-time-retrieval.md), [F03 — Executable Feedback Loop](catalog/families/F-harness-environment/patterns/F03-executable-feedback-loop.md) |
| "Agent output was great at first but quality dropped" / "early in the session it's sharp, later it gets sloppy" / "it followed instructions earlier, then stopped" | Accumulated history or tool output might be competing with the task. Check whether the earlier instruction is still available and current before choosing compaction or a restart. | [Context Compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [Fresh-Context Retry](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md) |
| "Agent ignores my instructions" / "I told it not to do X and it does X anyway" / "it ignores certain rules" | Check if the rule was available, relevant, and current. Repository instructions require editable project files. A deterministic override requires implementation control and a rule that can be evaluated mechanically. | [F06 — Structured Repository Instructions](catalog/families/F-harness-environment/patterns/F06-structured-repository-instructions.md), [H01 — Deterministic Override](catalog/families/H-deterministic-control/patterns/H01-deterministic-override.md) |
| "Agent keeps doing the same thing even when I correct it" / "I tell it to change approach and it reverts" / "it keeps proposing an approach we explicitly rejected" | If rejected attempts are still present and the goal is clear, consider a clean session with the actionable facts. If the failure cause is unknown, investigate it before retrying. A recurring proposal and an edit to intentionally unusual code are distinct cases. The catalog has no dedicated conversational fixation or intentional-code guard procedure. | [Fresh-Context Retry](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md), [Root-Cause-Before-Retry](catalog/families/I-reliability-recovery/patterns/root-cause-before-retry.md), [B6 — Reconnaissance-First](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md) |
| "Same prompt gives different results each time" / "it works sometimes and fails sometimes" | Variation could come from sampling, changed context or tools, or execution order. Check whether the difference affects correctness or is acceptable variation. | [use-cases/debugging/non-determinism](catalog/use-cases/debugging/non-determinism.md), [D01-deterministic-validator](catalog/families/D-verification-evaluation/patterns/D01-deterministic-validator.md), [I/bounded-retry](catalog/families/I-reliability-recovery/patterns/bounded-retry.md), [H/H01-deterministic-override](catalog/families/H-deterministic-control/patterns/H01-deterministic-override.md) |
| "Agent's response is way too long" / "gives me 200 lines when I need 10" / "drowns me in explanation" | Gap for adjusting conversational length or level. For a window filling from accumulated output, see the context-window route below. | No direct entry. |
| "Agent makes small errors that compound" / "each step is slightly off and by the end it's totally wrong" | With a multi-step task, check whether intermediate outputs can be verified independently. Step-level diagnostics require implementation access. | [B5 — Milestone / Checkpoint Planning](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md), [D12 — Step-Level Diagnostic](catalog/families/D-verification-evaluation/patterns/D12-step-level-diagnostic.md) |
| "Important steps get skipped" | If steps have known success criteria, check whether the agent can follow a scoped plan or stop at milestones. Enforcing order mechanically requires implementation control. | [B1 — Plan → Execute](catalog/families/B-task-decomposition/patterns/B1-plan-execute.md), [State Machine](catalog/families/L-memory-state/patterns/state-machine.md) |

### 1B — Working with an agent

| User says something like… | What to check or consider | Read these |
|---|---|---|
| "I've been going back and forth for 20 messages and it's getting worse" / "should I keep trying or start over?" | Repeated failed attempts may be adding noise. Check whether the next attempt has new evidence and whether useful state can be preserved before a reset. | [Fresh-Context Retry](catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md), [Context Compaction](catalog/families/E-context-engineering/patterns/context-compaction.md) |
| "I just accept what the AI writes, I can't keep up with reviewing everything" / "I stopped reading the code" / "it produces more code than I can review" | If the agent can pause between phases, route to checkpoints and reviewable milestones. Checks can verify specific properties. They leave human understanding and review capacity open. | [B5 — Milestone / Checkpoint Planning](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md), [K01 — Human-in-the-Loop Checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) |
| "I told the AI exactly how to solve it and the result was bad" / "I described the solution in my prompt" | Check whether the suggested solution was a hard requirement or an option. Reconnaissance can ground a coding plan if the agent can inspect the project. Prompt framing to avoid steering remains a gap. | [B6 — Reconnaissance-First](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md) |
| "I have too many things going at once" / "AI makes it so easy to start things but I can't finish any" | Milestones can track progress within one task. The catalog has no direct method for prioritizing or limiting the user’s active tasks across projects. | [B5 — Milestone / Checkpoint Planning](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md) |
| "I prefer working with AI over my teammates" / "I don't need pair programming anymore" / "working with AI isolates me from teammates" / "shared understanding declines" | Team isolation and knowledge sharing are gaps. For the separate concern of monitoring agent actions, consult the human-control family. | No direct entry. |
| "I just prompt → light edit → ship" / "the AI does 95% of the work" | Check whether the issue is verifiable behavior, or whether the user needs to understand the change before accepting it. Checkpoints support inspecting evidence. A practitioner ownership workflow remains a gap. | [K01 — Human-in-the-Loop Checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) |
| "The AI made a massive change and I can't review it" / "PR is 2000 lines, all AI-generated" / "the diff is enormous" | For future work that can be staged, check whether there are independently reviewable milestones and whether the agent can pause. Draft previews apply when writes can be held for approval. A procedure for reviewing or splitting an already oversized diff remains a gap. | [B5 — Milestone / Checkpoint Planning](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md), [K01 — Human-in-the-Loop Checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md), [K05 — Draft/Preview Before Apply](catalog/families/K-human-control/patterns/K05-draft-preview-before-apply.md) |
| "I keep adding more rules to CLAUDE.md but it doesn't help" / "the more instructions I give, the worse it gets" | If the instruction file loads lots of material irrelevant to the current task, route to Map-Not-Manual when project files can be edited and retrieved. | [AP03 — Giant Instruction Manual](catalog/anti-patterns/AP03-giant-instruction-manual.md), [Map-Not-Manual](catalog/families/E-context-engineering/patterns/map-not-manual.md) |
| "AI agreed with something that doesn't make sense" / "it accepted contradictory requirements without pushing back" / "it says yes but misunderstands me" / "it implements before I notice" | If execution can pause, a plan with success criteria or a human checkpoint can expose some disagreements before writing. The catalog lacks a dedicated conversational approach for eliciting pushback or checking shared meaning. | [B1 — Plan → Execute](catalog/families/B-task-decomposition/patterns/B1-plan-execute.md), [K01 — Human-in-the-Loop Checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) |
| "It improves code that was intentionally written that way" / "it forgets why we made that trade-off" | A repository decision log can preserve rationale when the user controls project files. A known, mechanically checkable invariant can use a gate if the user controls implementation. Intentional-code markers and conversational fixation remain distinct gaps. | [F02 — Repository-Local System of Record](catalog/families/F-harness-environment/patterns/F02-repository-local-system-of-record.md), [H02 — Programmatic Gate](catalog/families/H-deterministic-control/patterns/H02-programmatic-gate.md) |
| "Large tasks lose requirements" / "one session handles too many responsibilities" | If the work can be staged, check whether a plan with success criteria and verifiable milestones will carry requirements across phases. If unrelated work is sharing one context and the tool supports separate contexts, see Context Isolation. | [B1 — Plan → Execute](catalog/families/B-task-decomposition/patterns/B1-plan-execute.md), [B5 — Milestone / Checkpoint Planning](catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md), [Context Isolation](catalog/families/E-context-engineering/patterns/context-isolation.md) |
| "Repeated chores require the same explanations" / "can I delegate this routine task?" | For stable, repeatable procedures where the user can install or edit a skill file. The catalog does not cover automatic learning from demonstrations. | [F07 — Agent Skills / Procedures](catalog/families/F-harness-environment/patterns/F07-agent-skills-procedures.md) |
| "My feedback produces another technically compliant but unhelpful result" | If there is a concrete failure or fixed criterion, route to review and retry. A method for turning qualitative feedback into a check remains a gap. | [Retry-With-Feedback](catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md), [D05 — Review Pass](catalog/families/D-verification-evaluation/patterns/D05-review-pass.md) |

### 1C — Context and session management

| User says something like… | What to check or consider | Read these |
|---|---|---|
| "Design drifts when I work across sessions" / "agent forgets architectural decisions from yesterday" / "I keep repeating preferences and project facts" / "corrections disappear in the next session" | Check if the facts or decisions have a current canonical record and whether a new session can read it. Repository and instruction-file routes require control of project files. Personal preferences across projects or chat sessions remain a gap. | [Repository-as-System-of-Record](catalog/families/E-context-engineering/patterns/repository-as-system-of-record.md), [F06 — Structured Repository Instructions](catalog/families/F-harness-environment/patterns/F06-structured-repository-instructions.md), [Context Compaction](catalog/families/E-context-engineering/patterns/context-compaction.md) |
| "My CLAUDE.md / system prompt is huge and the agent still ignores half of it" | Check whether material can be moved into files the agent reads on demand. Keep rules needed at every step available. | [AP03 — Giant Instruction Manual](catalog/anti-patterns/AP03-giant-instruction-manual.md), [Map-Not-Manual](catalog/families/E-context-engineering/patterns/map-not-manual.md) |
| "I need the agent to remember X from earlier in the conversation" / "it forgot decisions or requirements in a long session" | Check whether the detail is still in the conversation, was lost during compaction, or lives in a separate record. Compaction can preserve accessible decisions and findings. A repository record requires file access. Neither recovers unavailable history. | [Context Compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [Repository-as-System-of-Record](catalog/families/E-context-engineering/patterns/repository-as-system-of-record.md) |
| "Context window is filling up, how do I manage it?" / "resetting loses valuable planning" / "research and tool output bury the task" | If the history is still available, compaction can keep decisions and current state. Offload reference material if file retrieval is available. Preserve a separate record if lossless history matters. | [Context Compaction](catalog/families/E-context-engineering/patterns/context-compaction.md), [Context Offloading](catalog/families/E-context-engineering/patterns/context-offloading.md), [Repository-as-System-of-Record](catalog/families/E-context-engineering/patterns/repository-as-system-of-record.md) |
| "How do I pass information between agents without losing it?" | Check whether downstream agents can read shared artifacts and which information disappeared or changed during handoff. | [E/minimal-context-handoff](catalog/families/E-context-engineering/patterns/minimal-context-handoff.md), [E/artifact-based-handoff](catalog/families/E-context-engineering/patterns/artifact-based-handoff.md), [L/shared-memory-gateway](catalog/families/L-memory-state/patterns/shared-memory-gateway.md), [AP07](catalog/anti-patterns/AP07-shared-context-everywhere.md) |
| "Agent doesn't use the tools/files I set up for it" | Check whether the tool or file is exposed to this session and whether its description or location is discoverable. | [G/G09-tool-discovery-progressive-exposure](catalog/families/G-tool-action-design/patterns/G09-tool-discovery-progressive-exposure.md), [F/F05-agent-accessible-tools](catalog/families/F-harness-environment/patterns/F05-agent-accessible-tools.md), [F/F01-agent-legible-repository](catalog/families/F-harness-environment/patterns/F01-agent-legible-repository.md) |
| "Quality drops as the codebase gets harder to navigate" | Check if the repo is difficult to navigate and whether the user can edit a project map. The symptom alone does not tell you why quality changed. | [F01 — Agent-Legible Repository](catalog/families/F-harness-environment/patterns/F01-agent-legible-repository.md), [B6 — Reconnaissance-First](catalog/families/B-task-decomposition/patterns/B6-reconnaissance-first.md) |

### 1D — Cost, performance, and scaling

| User says something like… | What to check or consider | Read these |
|---|---|---|
| "My agent costs too much" / "token usage is way too high" | Distinguish model cost, context size, retries, and agent count. Many optimizations require settings or implementation access. | [use-cases/cost-and-performance/reducing-cost](catalog/use-cases/cost-and-performance/reducing-cost.md), [N/cost-aware-stopping](catalog/families/N-efficiency-routing/patterns/cost-aware-stopping.md), [N/complexity-based-model-routing](catalog/families/N-efficiency-routing/patterns/complexity-based-model-routing.md), [N/context-minimization](catalog/families/N-efficiency-routing/patterns/context-minimization.md) |
| "Agent is too slow" / "takes forever to respond" | Possible contributors include model latency, sequential dependencies, and too much context. Look for the bottleneck first. | [use-cases/cost-and-performance/latency](catalog/use-cases/cost-and-performance/latency.md), [N/parallel-execution](catalog/families/N-efficiency-routing/patterns/parallel-execution.md), [N/small-model-first-escalation](catalog/families/N-efficiency-routing/patterns/small-model-first-escalation.md), [E/context-compaction](catalog/families/E-context-engineering/patterns/context-compaction.md) |
| "We have too many agents and it's expensive" | Check whether separate agents contribute distinct value that offsets the extra calls and handoffs. | [AP05](catalog/anti-patterns/AP05-multi-agent-by-default.md), [use-cases/cost-and-performance/reducing-cost](catalog/use-cases/cost-and-performance/reducing-cost.md), [C/do-you-need-multi-agent](catalog/families/C-orchestration/guides/do-you-need-multi-agent.md), [N/complexity-based-model-routing](catalog/families/N-efficiency-routing/patterns/complexity-based-model-routing.md) |

### 1E — Security and trust

| User says something like… | What to check or consider | Read these |
|---|---|---|
| "Agent has access to everything" / "I'm worried about what it can do" | Identify which permissions the task requires and which settings or policies can narrow them. | [AP10](catalog/anti-patterns/AP10-overpowered-coding-agent.md), [J01-least-privilege](catalog/families/J-security-trust/patterns/J01-least-privilege.md), [J02-sandbox](catalog/families/J-security-trust/patterns/J02-sandbox.md), [J10-capability-minimization](catalog/families/J-security-trust/patterns/J10-capability-minimization.md), [use-cases/security/privilege-and-trust](catalog/use-cases/security/privilege-and-trust.md) |
| "Can the agent be tricked by input?" / "what about prompt injection?" | Check whether untrusted content reaches the agent and what data and actions the same context can access. | [J06-untrusted-context-isolation](catalog/families/J-security-trust/patterns/J06-untrusted-context-isolation.md), [use-cases/security/prompt-injection](catalog/use-cases/security/prompt-injection.md), [O/sanitized-output-boundary](catalog/families/O-output-integration/patterns/sanitized-output-boundary.md) |
| "How do I add approval gates?" / "I want human review before the agent acts" | Check whether review should happen at phase boundaries, before state changes, or for high-risk actions. Hard gates require control over execution. | [K/K01-human-in-the-loop-checkpoint](catalog/families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md), [K/K02-high-risk-action-gate](catalog/families/K-human-control/patterns/K02-high-risk-action-gate.md), [K/K04-review-before-side-effect](catalog/families/K-human-control/patterns/K04-review-before-side-effect.md), [use-cases/human-in-the-loop/approval-workflows](catalog/use-cases/human-in-the-loop/approval-workflows.md) |
| "It needs a safe place to test assumptions" | If running code requires a disposable workspace or narrower access, check whether the user controls the execution environment. | [F08 — Sandboxed Execution](catalog/families/F-harness-environment/patterns/F08-sandboxed-execution.md) |
| "I miss when the agent needs me" / "routine work needs too much supervision" | For managed workflows, check whether the tool can surface approvals or monitoring alerts. The patterns require such a channel or control over implementation. For where a workflow should pause, see the human-control use case. | [K06 — Human-on-the-Loop Monitoring](catalog/families/K-human-control/patterns/K06-human-on-the-loop-monitoring.md), [When to Interrupt](catalog/use-cases/human-in-the-loop/when-to-interrupt.md) |

### 1F — Evaluation and testing

| User says something like… | What to check or consider | Read these |
|---|---|---|
| "How do I know if my agent is working?" / "what should I measure?" | Check which real task outcomes and failures the evaluation needs to measure. | [AP08](catalog/anti-patterns/AP08-generic-evals-before-error-analysis.md), [use-cases/evaluation/evaluating-agents](catalog/use-cases/evaluation/evaluating-agents.md), [D/D11-end-to-end-task-success](catalog/families/D-verification-evaluation/patterns/D11-end-to-end-task-success.md), [M/M09-failure-categorization](catalog/families/M-observability-debugging/patterns/M09-failure-categorization.md) |
| "Tests pass but users complain" / "evals look fine but something is off" | Checks may omit user-visible failures. Compare the checks with actual outcomes and the failures users report. | [AP08](catalog/anti-patterns/AP08-generic-evals-before-error-analysis.md), [use-cases/evaluation/evals-from-errors](catalog/use-cases/evaluation/evals-from-errors.md), [D/D10-human-calibration](catalog/families/D-verification-evaluation/patterns/D10-human-calibration.md), [N/silent-quality-degradation](catalog/families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) |
| "Agent worked yesterday but broke today" / "regression after model update" | Check what changed in the model, settings, or supplied context and whether a baseline exists for comparison. | [use-cases/evaluation/regression-testing](catalog/use-cases/evaluation/regression-testing.md), [D/D02-test-before-done](catalog/families/D-verification-evaluation/patterns/D02-test-before-done.md), [H/H03-structural-test](catalog/families/H-deterministic-control/patterns/H03-structural-test.md) |

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

## Extending the bridge

When a new pattern is approved for the catalog, add its local file to the rows it answers. Test the route from the engineer's symptom through the lookup to the entry. If an entry covers only part of the symptom, keep that limit explicit in the answer.
