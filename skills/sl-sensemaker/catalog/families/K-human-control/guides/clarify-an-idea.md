# Clarify an idea before implementation

## Purpose

Use a focused conversation to turn a rough intention into behavior the person can approve.

## When to use this guide

- You know roughly what you want but struggle to express it.
- The assistant fills in consequential choices before you have decided them.

Conversation control is enough. Saving a specification requires file access; implementation checks apply only when the idea becomes code. A person with authority over the requirement must settle business choices.

## Quick tip

Ask: “Help me clarify this idea before implementation. Start with the question whose answer most changes the result. Use an example, then summarize what we decide and what remains open.”

## Guide content

1. State the rough goal, who it serves, any binding constraints, and what is still undecided. Ask for clarification before edits.
2. Have the assistant ask about consequential choices. Use a small set of meaningful alternatives when helpful, with room for your own answer. It should identify visible contradictions rather than quietly select a requirement.
3. Work through one ordinary situation and one boundary case. Correct the predicted outcome before selecting an implementation.
4. Review a short agreement: goal, expected behavior, exclusions, constraints, and unresolved choices. Keep it in the chat for a small task or save an approved specification for continuing work.
5. Move to planning when the next bounded step is clear. Reopen only choices affected by new information; do not turn clarification into an endless interview.

**Original illustration:** “I want notifications” could mean an immediate interruption or a daily digest. Ask what the recipient needs to do when an event occurs. Agree which events are urgent and what happens to routine events overnight before proposing a delivery mechanism.

## Limits

This is a catalog adaptation of the interview advice found through BP-02. The assistant can help articulate intent but cannot supply missing stakeholder authority or guarantee it will challenge every bad request. For a verified, fully specified fix, proceed directly. For one disputed domain term, use the narrower terminology guide.

## Related patterns

- [Clarify domain terms](../../E-context-engineering/guides/clarify-domain-terms.md) — resolve conflicting meanings.
- [Plan → Execute](../../B-task-decomposition/patterns/B1-plan-execute.md) — plan once the task is understood.
- [Human-in-the-Loop Checkpoint](../patterns/K01-human-in-the-loop-checkpoint.md) — obtain decisions at a phase boundary.
- [Assess before naming a fix](../../I-reliability-recovery/patterns/root-cause-before-retry.md#in-a-session-assess-before-naming-a-fix) — distinguish evidence from a proposed diagnosis.

## Sources

- Anthropic — [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first), “Brainstorm with Claude first,” living guide, consulted 2026-11-22. Documents an assistant-led interview leading to a specification. The prioritization of questions, stopping condition, chat-only variation, and notification example are catalog adaptations, not measured improvements.
