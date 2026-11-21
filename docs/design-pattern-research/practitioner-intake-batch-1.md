# Practitioner research intake — batch 1

Date: 2026-11-21  
Compared against main: `17a09cce854bd511c81302babc037b87df3fc318`

## Outcome and scope

Five previously selected practitioner methods were compared with the existing catalog. Four extend an existing pattern; one becomes a guide in an existing family. There is no new family or duplicate pattern for a synonym. This batch concerns a person directing, correcting, understanding, and reviewing an assistant in a chat or CLI.

The research remains in `raw/`. Its selected guidance is now also available in the installed catalog. Runtime answers do not depend on opening research files or external sites. This report is the editorial provenance record, not a runtime entry.

## Comparison and disposition

| Research method | Existing material compared | Decision and distinct contribution | Canonical destination |
|---|---|---|---|
| [PAT-0001: recover a drifting session](raw/patterns/PAT-0001--recover-a-drifting-coding-session.md) | Fresh-Context Retry, Context Compaction, Artifact-Based Handoff | Enrich Fresh-Context Retry: distinguish noisy but aligned context from repeated reversion; preserve governing decisions, rejected options, and useful edits in a checked handoff. Compaction and handoff remain related mechanisms. | [Session recovery](../../skills/sl-sensemaker/catalog/families/I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work) |
| [PAT-0003: slice a change for review](raw/patterns/PAT-0003--slice-a-change-for-review.md) | B5 Milestone / Checkpoint Planning | Enrich B5: a person asks for independently inspectable behavior, dependencies, a review order, and acceptance evidence. Preserve a large existing patch before restructuring; allow wide-refactor integration constraints. | [Reviewable milestones](../../skills/sl-sensemaker/catalog/families/B-task-decomposition/patterns/B5-milestone-checkpoint.md#in-a-session-slice-a-change-for-review) |
| [PAT-0005: turn review feedback into a check](raw/patterns/PAT-0005--turn-review-feedback-into-a-check.md) | Retry-With-Feedback; D02 Test-Before-Done; D03 Evidence-Based Completion | Enrich Retry-With-Feedback: separate observation from suspected cause, state the desired behavior, and inspect the revision against a failing and neighboring case. D02/D03 still cover execution and completion evidence. | [Feedback into a check](../../skills/sl-sensemaker/catalog/families/I-reliability-recovery/patterns/retry-with-feedback.md#in-a-session-turn-feedback-into-a-check) |
| [PAT-0006: resolve a domain term](raw/patterns/PAT-0006--resolve-a-domain-term-before-coding.md) | Context Offloading; Repository-as-System-of-Record; existing E guides | Add a guide: existing patterns explain storing and retrieving context but do not guide a person through choosing a distinguishing case, obtaining the owner's decision, and recording a settled meaning. | [Clarify domain terms](../../skills/sl-sensemaker/catalog/families/E-context-engineering/guides/clarify-domain-terms.md) |
| [PAT-0008: take ownership before submitting AI code](raw/patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) | D05 Review Pass; D02 Test-Before-Done; D03 Evidence-Based Completion | Enrich D05: a human inspects implementation and test changes, checks retained regression coverage, explains the change, and follows the target project's contribution rules. Passing selected tests does not establish complete correctness. | [Human review pass](../../skills/sl-sensemaker/catalog/families/D-verification-evaluation/patterns/D05-review-pass.md#in-a-session-review-ai-changes-before-accepting-them) |

## Evidence and adaptation

The original sources were checked on 2026-11-21. Registry IDs 26–30 point to those publications. Each destination retains its existing structural sources and adds the relevant practitioner source; source count is not an evidence score.

| Source | What it supports here | What this catalog adds or does not claim |
|---|---|---|
| Anthropic, [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) | Session steering, requirements, verification, and review | The checked decision handoff, rejected-option reminder, and paired examples are adaptations. No fixed turn-count or context-percentage reset rule. |
| Matt Pocock, [The /to-tickets Skill](https://www.aihero.dev/skills-to-tickets) | Demonstrable slices, dependencies, avoiding excessive splitting, wide-refactor exceptions | The human review prompts and neighboring-case examples are adaptations. No claimed measured reduction in review time or bugs. |
| Matt Pocock, [The /domain-modeling Skill](https://www.aihero.dev/skills-domain-modeling) | Reconcile language with code, concise glossaries, selective decision records | The explicit decision owner and distinguishing case are an applied procedure, not a guarantee against drift. |
| Ivett Ördög / Samman Coaching, [ROSE Feedback](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html) | Flexible risk/observation/solution/expected-outcome feedback on produced work | The modified session subsection is attributed and licensed CC BY-SA 4.0; it uses a new retry-count illustration and additional verification. No claim of permanent model learning. |
| Moby / Docker maintainers, [AI Usage Policy](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md) | Contributor verification, focused changes, ownership, and project-specific disclosure | This is a policy example, not a universal approval rule. The CSV illustration is newly written. |

One relevant, verifiable source is sufficient; additional sources may support or qualify a claim. The three contributor checklists are aligned on that rule. This batch does not redesign other contribution requirements.

## Coverage of the 17 pain-point groups

All groups are represented as ordinary symptom sentences in [the bridge](../../skills/sl-sensemaker/bridge-file.md). A route is not a diagnosis or a claim that every aspect is solved.

| Group | Example symptoms | Coverage after this batch |
|---|---|---|
| 1 | Repeating preferences, corrections lost next session, reset loses planning | Checked handoff and durable records; user must review and reload them. |
| 2 | Earlier instructions ignored, long conversation, research/tool output buries task | Session recovery and context compaction; diagnose the specific missing requirement first. |
| 3 | Giant instruction file, stale or contradictory saved notes | Existing map and system-of-record entries; partial until conflicting content is resolved. |
| 4 | “Improves” intentional code; forgets why a choice was made | Domain clarification and rationale, plus decision recovery when the choice was already settled. |
| 5 | Agrees without understanding, starts too soon, never challenges | Clarification and preview for ambiguity; partial for general uncritical agreement. |
| 6 | Literal compliance misses goal; unhelpful response to feedback | Outcome-based corrective feedback and distinguishing cases. |
| 7 | First explanation becomes fact, unverified fix, more retries worsen it | Reconnaissance, corrective feedback, and conditional session recovery. |
| 8 | Changes assertions, deletes tests, coverage creates false confidence, test review overload | Human review of test changes, feedback checks, and smaller review units. |
| 9 | Too much generated code, huge diff, accepts without understanding | Reviewable milestones and ownership review. |
| 10 | Invented or obsolete APIs, repeated library corrections, safe experiments | Existing retrieval and reconnaissance; sandbox guidance is partial and requires actual configuration. |
| 11 | Large tasks lose requirements, too many session responsibilities, growing repository | Milestones and reconnaissance; partial for broader repository failure modes. |
| 12 | Rules ignored, steps skipped, unclear compliance | Observable completion evidence and feedback; enforced boundaries only when needed and controllable. |
| 13 | Too verbose, wrong detail, difficulty explaining, domain mismatch | Domain guide and response feedback; dedicated communication-level guidance remains a gap. |
| 14 | Leading with own answer, no alternatives, conversation drifts | Reconnaissance and session recovery; systematic alternatives comparison remains a gap. |
| 15 | Inconsistent results, repeated chores, cost and supervision | Existing debugging and procedures; partial, since tooling and execution controls vary. |
| 16 | Side tasks, unfinished work, missed input requests, needless delegation back to user | Milestones, recovery, escalation and access checks; notification and personal task-management gaps remain explicit. |
| 17 | AI replaces teammate interaction, lost shared understanding, stale docs/diagrams | Artifact records and personal review cover part; team isolation and automatic diagram maintenance remain gaps. |

No external collection links or collection source inventory were added. Symptom strings are search vocabulary; original research sources supply the actual guidance.

## Retrieval and installation

The existing Understand → Research → Deliver flow is unchanged. The lookup now leads directly to five practical destinations; family indexes expose the same entries. Bridge rows start with what a person can observe and do, and label partial matches rather than silently routing every session problem to infrastructure.

The inventory changes from 270 to 272 catalog Markdown files: one guide plus its family guide index. Pattern count remains 137; guide count becomes 9. Five original sources are added to the registry.

## Validation

- Existing local-link and anchor check: 1,774 links, zero unresolved.
- Existing install/reinstall test: passed, including copying the complete catalog, preserving a local addition, and missing-catalog recovery instructions.
- Static route walkthroughs: test deletion → human review; rejected approach → checked handoff; oversized diff → B5; feedback shortcut → retry-count counterexample; ambiguous daily visits → owner decision; team isolation → explicit gap.
- Whitespace/diff validation: passed.
- These are content, route, and installation checks, not an interactive Claude evaluation or measured practitioner effectiveness.

The five research method files and their raw source dossiers are unchanged. This implementation is separate from preparation design PR #7; it does not implement all of that design. Merge review should reconcile overlapping contributor/navigation edits if another implementation of #7 lands first.
