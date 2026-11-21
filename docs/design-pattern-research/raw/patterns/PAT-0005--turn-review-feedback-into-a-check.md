---
pattern_id: PAT-0005
status: accepted
name: "Turn review feedback into a check"
type: workflow
families: [code-review, feedback, verification]
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
topic_ids: [AP-03, BP-10, OB-02]
symptoms: ["The agent agreed with my review but the same input still fails", "My comment suggests a fix before I know what caused the bug", "The patch fixes my example and breaks the neighboring case"]
source_ids: [SRC-0010, SRC-0002, SRC-0005]
review: PASS
publication_status: published
---

# Turn review feedback into a check

## When users need this

An assistant has already proposed a patch. You can point to a line you would send back, but “fix the default” could mean changing the default value, changing when it applies, or editing the test that raised the question. Use the review comment to give the next person or agent enough information to tell whether a revision addresses the concern.

## Context and prerequisites

Have the proposed change, a way to locate the affected behavior, and some authority for what should happen, such as a documented interface or a product decision. A small input and a visible result are often sufficient. If nobody has decided what the behavior should be, take that question to the owner first. A failing assertion that encodes one person's guess can steer a revision just as firmly as an explicit implementation demand.

## Core principle

Ivett Ördög teaches **ROSE** for feedback on an agent's existing work. **Risk** names what could go wrong. **Observation** identifies something the reviewer can point to now. **Solution** asks for an action. **Expected outcome** describes the difference the revision should make. Ördög allows reviewers to omit or reorder elements when the context is clear. Our addition pairs the expected outcome with a check the reviewer can repeat, including an adjacent case when an obvious shortcut would satisfy the reported example. [Ördög, concept and guidance after the definitions](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern)

## How to work this way

1. **Reproduce the observation and name the risk.** Find the smallest example that exposes the concern on the proposed patch. Record the input, actual result and relevant symbol. State separately what might happen if the patch ships. If your suspected cause is uncertain, ask the implementer to investigate it. [Evidence 1](#evidence-for-the-decisions)
2. **Choose what to ask for.** If the contract determines the change, specify the behavior to restore. If several designs could satisfy it, leave the mechanism open. If the observation itself is disputed, make the requested action a reproduction or an explanation and defer the edit. Acknowledgment from the agent gives you a reply to investigate. [Evidence 2](#evidence-for-the-decisions)
3. **Write an expected outcome that distinguishes a repair from a shortcut.** Name the expected result and its authority. Add a case that already works if a plausible fix would break it. Put these in the same comment as the observation and requested action. A one-line comment suffices when the diff and existing check already express the rest. [Evidence 3](#evidence-for-the-decisions)
4. **Close the comment against the revised behavior.** Ask for the command and output, or for a visible demonstration when appropriate. Repeat the check where feasible. Read the diff for changes to expectations or adjacent behavior. If the check and the agreed contract disagree, resolve the expectation with its owner before accepting the revision. [Evidence 4](#evidence-for-the-decisions)

## Worked example

**Original, hypothetical code review.** A job runner accepts an optional nonnegative integer `retries`. Its configuration guide says an omitted value allows three retries and an explicit zero disables retries. A proposed parser contains this Python expression.

```python
def retry_limit(config):
    return config.get("retries") or 3
```

A reviewer might write “the default should be zero.” That change would break every caller relying on the documented default. A comment the implementer can act on reads as follows.

> On this patch, `retry_limit({"retries": 0})` returns `3`. An operator who disables retries could see a failed job run again. Please make the parser preserve an explicit retry count. The configuration guide gives three as the default when the setting is absent. Show the results for zero, an omitted setting, and a positive count.

The first sentence supplies the **observation**, the second gives the **risk**, and the request to preserve an explicit count gives the **solution** at the behavioral level. The contract and requested cases define the **expected outcome**. The parser output is observable here. Whether any job actually reran would require separate evidence.

```python
for config in ({"retries": 0}, {}, {"retries": 2}):
    print(retry_limit(config))
```

The candidate prints `3, 3, 2` on successive lines. Replacing the fallback constant with zero would print `0, 0, 2`, so the omitted-key case catches a superficially responsive edit. In this example, `return config.get("retries", 3)` prints the expected `0, 3, 2`. In the diff, the reviewer checks that the caller actually uses the revised parser and that the test for the omitted key still expects three. These examples cover the stated integer contract. A separate policy decision would be needed if null also became a supported value.

## Evidence for the decisions

| Decision | Claim IDs and original locations | Evidence and our adaptation |
|---|---|---|
| 1. Ground the observation and identify its consequence | SRC-0010:C01, SRC-0010:C02, SRC-0010:C04. [Ördög, “Concept,” four definitions and final two bullets](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern). SRC-0002:C06. [Anthropic, “Write a specific prompt,” login example](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt) | Direct practitioner advice on risk, observations, locations and symptoms. Reducing the failure to a reproducible input and explicitly labeling a tentative diagnosis are our review procedure. |
| 2. Ask for an action at the level the evidence warrants | SRC-0010:C02, SRC-0010:C07. [Ördög, concept definitions](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) · [teaching handout, package-installation example](https://github.com/sammancoaching/website/blob/main/assets/images/rose_pattern_handout.svg). SRC-0005:C03, SRC-0005:C05. [Sharma et al., §§3.2–3.3, Figs. 2–3](https://arxiv.org/html/2310.13548v4) | Ördög's material illustrates concrete requests and invitations for ideas. In separate question-answering experiments, an unsupported challenge could dislodge a correct answer, and a wrong suggested answer reduced aggregate accuracy for the five tested assistants. Leaving implementation open or asking for reproduction first is our application to code review. The experiments did not compare review comments. |
| 3. Specify the distinction a passing check must preserve | SRC-0010:C02, SRC-0010:C03, SRC-0010:C04. [Ördög, “Concept,” definitions and subsequent qualifications](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern). SRC-0002:C07, SRC-0002:C10. [Anthropic, “Give Claude a check to run,” examples](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [“Review against your spec,” edge-case review prompt](https://code.claude.com/docs/en/best-practices#review-against-your-spec) | Direct advice on flexible feedback, identifiable outcomes and runnable checks. Choosing a neighboring case specifically to distinguish a tempting shortcut, and citing the authority for its expected value, are our adaptations. |
| 4. Verify the revision | SRC-0010:C06. [Ördög, kata exercise, final optional step](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#write-rose-prompts-for-the-tennis-kata-25-min). SRC-0002:C08, SRC-0002:C10. [Anthropic, evidence request after the check examples](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [spec review prompt](https://code.claude.com/docs/en/best-practices#review-against-your-spec) | The lesson invites participants to try a prompt and inspect the result if time permits. The vendor asks for check output and comparison with the spec. Making a reviewer's rerun and review of changed assertions part of closing a comment is our extension. |

## Different source perspectives

Ördög's Samman Coaching lesson directly documents the named practice and reports no evaluation results. Anthropic's product guide supplies separately published advice about executable checks. Sharma and colleagues' experiments concern responses to user cues in question answering, including changes from a correct first answer after a challenge. Effects varied by task and model. The paper and the Claude Code guide share an Anthropic connection and address different questions. None of these sources measures whether ROSE improves patches or prevents intentional or literal compliance. A reviewer's ability to replay a particular check can be demonstrated locally. General effectiveness remains unmeasured. [Lesson exercise](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#write-rose-prompts-for-the-tennis-kata-25-min) · [Product guide](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Paper, §3](https://arxiv.org/html/2310.13548v4)

## Variations, tradeoffs and limits

- **An existing test already says it all.** Link its failure, say why the assertion matters, and ask for the output after repair. Repeating the four labels can obscure a short request. If an agent cannot read a selected IDE line, include the symbol or the failing case in the comment. This adapts Ördög's point about optional elements and selection visibility. [SRC-0010:C03, concept qualifications](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern)
- **The concern requires judgment.** For a crowded settings page, identify which control a user has difficulty finding and ask for a screenshot of the affected state. A reviewer can judge that image against the design, then decide whether usability testing is needed. A screenshot alone cannot establish how quickly users complete the task. This is our application of the guide's visual-evidence option. [SRC-0002:C08, evidence request](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run)
- **The requirement is open.** If support and engineering disagree about whether zero means “disable” or “inherit,” ask the owner to decide and record the answer. Labeling one team's guess as the expected result would conceal the disagreement. This is our boundary for using the pattern. [SRC-0002:C05, specification by interview](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first)

## Related patterns and topics

BP-10 indexes the feedback method directly. OB-02 and AP-03 are supporting retrieval paths for users who see unearned agreement or recognize their own unverified fix in a prompt. Use this entry to write and resolve one review comment. When the open decision is whether to spend another attempt repairing the implementation or to generate a fresh candidate, use [PAT-0004 · Compare repair with fresh candidates](PAT-0004--compare-repair-with-fresh-candidates.md).

## Sources

- Ivett Ördög, “ROSE Feedback,” Samman Coaching Society, undated lesson. [SRC-0010 dossier](../sources/SRC-0010--rose-feedback-exercise.md) · [Source verification](../audits/SRC-0010--verification.md) · [Original lesson](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html)
- Anthropic, “Best practices for Claude Code,” living product documentation, accessed November 21, 2026. [SRC-0002 dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Source verification](../audits/SRC-0002--verification.md) · [Original guide](https://code.claude.com/docs/en/best-practices)
- Mrinank Sharma and colleagues, “Towards Understanding Sycophancy in Language Models,” first released in 2023, version 4 consulted. [SRC-0005 dossier](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Source verification](../audits/SRC-0005--verification.md) · [Original paper](https://arxiv.org/html/2310.13548v4)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/PAT-0005--verification.md)

## Drive navigation

- [audits/PAT-0005--verification.md](../audits/PAT-0005--verification.md) · [Local copy](../audits/PAT-0005--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0005--verification.md](../audits/SRC-0005--verification.md) · [Local copy](../audits/SRC-0005--verification.md)
- [audits/SRC-0010--verification.md](../audits/SRC-0010--verification.md) · [Local copy](../audits/SRC-0010--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0005--sycophancy-and-user-beliefs.md](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Local copy](../sources/SRC-0005--sycophancy-and-user-beliefs.md)
- [sources/SRC-0010--rose-feedback-exercise.md](../sources/SRC-0010--rose-feedback-exercise.md) · [Local copy](../sources/SRC-0010--rose-feedback-exercise.md)
- [topics/AP-03--answer-injection.md](../topics/AP-03--answer-injection.md) · [Local copy](../topics/AP-03--answer-injection.md)
- [topics/BP-10--rose-feedback.md](../topics/BP-10--rose-feedback.md) · [Local copy](../topics/BP-10--rose-feedback.md)
- [topics/OB-02--compliance-bias-sycophancy.md](../topics/OB-02--compliance-bias-sycophancy.md) · [Local copy](../topics/OB-02--compliance-bias-sycophancy.md)
