# Practitioner research intake — batch 1

Source intake: 2026-11-21; reconciliation and verification: 2026-11-22

Initial comparison: `17a09cc`. Reconciled against preparation PR #8 on main at `ae01ad6466c390e34817c0bef8c7d87ae91c779f`.

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

One relevant, verifiable source is sufficient; additional sources may support or qualify a claim. PR #8's contributor instructions are retained. Only new source rows, evidence notes, and family mappings are added to its registry.

## Intake records under PR #8

The comparison above records the existing entries read, destination, and enrich/write decision. The following completes the candidate records with source location, controls, evidence, and limits. The relevant original publications and selected dossiers were read during the initial intake; this reconciliation checks those contributions against the newly merged rules.

| Candidate | Source locations and contribution | User controls | Evidence, adaptation, and limits |
|---|---|---|---|
| PAT-0001 | Anthropic “Steer the session,” plus its recovery/verification advice: redirect and recover a conversation. SRC-0002. | Can inspect the agreed decision and start or summarize a conversation; optional file access to preserve work. | Documented vendor advice. Checked handoff, rejected-option reminder, and distinguishing prediction are adaptations; no universal reset threshold or guarantee. |
| PAT-0003 | Pocock “Tracer bullets, not layers,” “Blocking edges,” “The wide-refactor exception,” “Common questions”; Anthropic “Give Claude a check to run” and “Review against your spec.” SRC-0006/SRC-0002. | Can scope requests, inspect and preserve the diff, and review proposed milestones. | Practitioner/vendor advice. Review prompts and neighboring checks are adaptations. No measured review-time benefit; wide changes may require integration. |
| PAT-0005 | ROSE lesson's feedback structure and optional elements for already produced work; research method's worked checks. SRC-0010. | Can inspect the output, agree expected behavior, and check the revision; executable claims need execution evidence. | Documented teaching practice. New retry-count illustration and paired check; no permanent learning claim. Modified session subsection carries CC BY-SA 4.0 attribution. |
| PAT-0006 | Pocock “Cross-referencing and where it stops,” “Two artifacts, two bars,” “Common questions”; Anthropic requirements/specification review. SRC-0009/SRC-0002. | Can consult a decision owner or settled specification; project access only for persistent glossary/decisions. | Practitioner/vendor advice. Owner decision, deciding case, and paired verification are adaptations. Does not settle unavailable requirements or enforce all future edits. |
| PAT-0008 | Pinned Moby AI_POLICY.md contribution requirements; Anthropic “Review against your spec.” SRC-0018/SRC-0002. | Can inspect implementation and tests, assess actual evidence, and accept responsibility under project rules. | Project-specific policy plus vendor advice. CSV example and targeted neighboring checks are adaptations. Neither policy nor selected tests prove general correctness. |

Each contribution supplies a recognizable situation, practical action, explicit controls, a newly labeled illustration, limits, and local related guidance. Existing engineering sections remain available. No new anti-pattern or principle was introduced, so those indexes and the pattern count do not change.

## Coverage summary

The authoritative [57-scenario inventory](practitioner-coverage.md) keeps every stable ID from PR #8. Its revised disposition is **21 covered, 28 partially covered, 8 missing**, compared with 13 / 33 / 11 before intake. Eight scenarios gain scoped guidance; two response-format cases move from missing to partial. “Covered” means an applicable next step under the stated controls, not a guarantee.

All 48 design sentences and Sharon's explicit scenarios have bridge routes or explicit gaps. The bridge retains PR #8's organization and D02/AP10 protected-check routes, adding direct practical destinations. General pushback, intent elicitation, task triage, hidden-instruction visibility, team isolation, and diagram maintenance remain limited or absent. No external collection links or source inventory were added.

## Retrieval and installation

The existing Understand → Research → Deliver flow is unchanged. The lookup now leads directly to five practical destinations; family indexes expose the same entries. Bridge rows start with what a person can observe and do, and label partial matches rather than silently routing every session problem to infrastructure.

The inventory changes from 270 to 272 catalog Markdown files: one guide plus its family guide index. Pattern count remains 137; guide count becomes 9. Five original sources are added to the registry.

## Validation

- Local-link and anchor check: 1,841 links checked, zero unresolved.
- Install/reinstall check: passed. Retains the protected-test route and checks all five practical destinations; verifies research records stay outside the cache.
- Seven static walkthroughs in the scenario inventory cover deleted tests, lost decisions, rejected approaches, large diffs, superficial feedback, domain terms, and team isolation.
- Coverage and batch-record links: 136 checked, zero unresolved. The rendered coverage table has 57 rows, six columns per row, and all 48 design sentences are present in the bridge.
- PR #8's authoring, intake, classification, contributor overview, citation rules, skill flow, and setup are retained. Raw research is unchanged; no conflict markers remain.
- Whitespace/diff validation and the 272-file catalog count passed.
- These are content, route, and installation checks, not an interactive Claude evaluation or measured practitioner effectiveness.

The five research method files and their raw source dossiers are unchanged. PR #8 is now the contribution baseline. The merge retains its authoring and intake files unchanged, its citation rules, its 57-scenario inventory, and its tests. PR #9 adds the five selected contributions and integrates their coverage, navigation, and source records.
