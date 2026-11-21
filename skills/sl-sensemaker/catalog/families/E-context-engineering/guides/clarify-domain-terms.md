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
