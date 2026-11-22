# Clarify domain terms before coding

## Purpose

Help a person and their assistant resolve words that imply different behavior before those assumptions become code.

## When to use this guide

- The ticket and the agent use the same term but predict different results.
- Two people use one word for different events.
- The assistant proposes simplifying an intentional trade-off whose rationale is missing.

You need the request and someone authorized to settle the affected requirement. For a personal project, that may be you. A settled specification may already answer the question.

You can do the clarification in a conversation. Persisting a shared glossary or decision requires project-file access; for a one-off chat, keep the agreed case in the conversation. Executable verification applies when the work becomes code.

## Guide content

1. Ask the agent to locate the term in the request, code, and existing decisions. Compare the implied behavior. Include relevant issue history if the decision lives there.
2. Choose one input where competing meanings produce different outcomes. Have the decision owner resolve it; do not let a plausible agent-written definition become policy by accident.
3. For recurring terminology, save the agreed meaning and confusing aliases in the existing domain glossary. Keep implementation detail elsewhere. For a one-off task, an explicit expectation in the task can suffice.
4. Record a rationale separately when a choice is costly to reverse, surprising without context, and involves a genuine trade-off. Reuse the team's decision format.
5. Ask the assistant to apply the agreement to the distinguishing case before editing. Verify that case and a neighboring case in the resulting change.

**Original illustration:** A report asks for “daily visits.” One person enters twice on Monday. Should that count as one visit or two scans? The reporting owner chooses one member per local calendar day; another member counts separately. Keep individual scans for audit and compute visits in the report. Ask: “Show the expected Monday count for one returning member and one new member. Explain why retaining both scans matters before proposing changes.”

If the agent later proposes deleting repeated scans, point it to the recorded rationale. If the underlying requirement changed, reconsider the decision explicitly rather than treating every old choice as permanent.

## Make an intentional decision visible at the edit

Use this when the agent replaces unusual code whose reason is already settled. You need editable project files; actual enforcement also requires control over checks or permissions.

**Quick tip:** Put a short reason or reference near the affected code, link the governing decision, and identify a representative compatibility check. Ask the agent to explain the requirement before changing it. Inspect edits to the check as carefully as the implementation.

Confirm the decision is still current. Use the existing decision record rather than duplicating its full history in comments. If it lives in an issue or external document, supply that location explicitly. Verify both the unusual case and ordinary behavior; a comment alone cannot block an edit. When the owner changes the requirement, update the record and affected check together.

**Original illustration:** A parser accepts a legacy date format because supported archived exports still contain it. A nearby reference identifies that compatibility decision and its regression check. A proposed cleanup must preserve the legacy case unless support is explicitly withdrawn.

This extends BP-09's decision-discovery advice. Pocock's decision records and cross-references support documenting rationale; Anthropic's [short guidance](https://code.claude.com/docs/en/best-practices#keep-claudemd-short) and [instruction/control distinction](https://code.claude.com/docs/en/best-practices#deterministic-and-non-deterministic-instructions) qualify what a note can do. The nearby reference, paired compatibility check, and illustration are catalog adaptations, not measured protection against every reversal. For protected verification use [D02](../../D-verification-evaluation/patterns/D02-test-before-done.md); for excessive write access see [AP10](../../../anti-patterns/AP10-overpowered-coding-agent.md). Source sections rechecked 2026-11-22.

## Limits

This is a clarification procedure, not a model-control guarantee. It covers terminology and documented decisions, not every form of disagreement or abandoned proposal. For repeated conversational reversion after the requirement is clear, use [session recovery](../../I-reliability-recovery/patterns/fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work).

Review persisted definitions; stale or contradictory notes can mislead. Do not create a glossary for every short conversation, or ask the assistant to decide a business rule its owner has not settled.

## Related patterns

- [Repository-as-System-of-Record](../patterns/repository-as-system-of-record.md) — store settled decisions where later work can find them.
- [Context Offloading](../patterns/context-offloading.md) — load only the needed definitions.
- [Milestone planning](../../B-task-decomposition/patterns/B5-milestone-checkpoint.md) — divide implementation after the meaning is settled.
- [Review Pass](../../D-verification-evaluation/patterns/D05-review-pass.md) — inspect the implemented behavior and retained checks.

## Sources

- Matt Pocock — [The /domain-modeling Skill](https://www.aihero.dev/skills-domain-modeling): sections “Cross-referencing and where it stops,” “Two artifacts, two bars,” and “Common questions”; advice on terms, glossaries, and selective decision records; consulted 2026-11-21.
- Anthropic — [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first): clarifying requirements and saving an agreed specification.

The deciding case, explicit owner decision, and paired verification are catalog adaptations from research method PAT-0006. The illustration is newly written. Neither cited guide measures a general reduction in drift from this procedure.
