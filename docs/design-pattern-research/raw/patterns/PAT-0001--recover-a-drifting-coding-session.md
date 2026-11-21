---
pattern_id: PAT-0001
status: accepted
name: "Recover a drifting coding session"
type: workflow
families: [context_management, reliability, workflow]
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
topic_ids: [AP-01, BP-01, BP-03, BP-06, OB-01, OB-07, OB-10]
symptoms: ["It keeps restoring a decision we already reversed.", "I still need the investigation, but the chat is mostly logs.", "Will starting a new chat undo the useful changes?"]
source_ids: [SRC-0001, SRC-0002, SRC-0003]
review: PASS
publication_status: published
---

# Recover a drifting coding session

## When users need this

A developer has corrected a requirement, yet the assistant’s next edit implements the old behavior again. In another session the assistant still understands the requirement, but several screens of diagnostic output obscure the few findings needed for the next change. Both users want to preserve useful work. The first has reason to replace the conversation. The second can often continue with a focused summary.

## Context and prerequisites

You need access to the current working files, a way to inspect changes, and a person or specification that can settle what the change should do. Choose an observable result that distinguishes the intended behavior from the recurring mistake. A unit test, an example invocation, or a manual interaction can serve. If two requirements conflict, settle which one governs before asking the assistant to resume.

## Core principle

Choose what to carry forward by asking which facts the next edit depends on. Record the governing decision and the check that would expose a violation. Decide separately which conversation history and which file changes are worth keeping.

## How to work this way

1. **Identify the mismatch.** Compare the last action or proposed edit with the requirement. Name a concrete input on which the two behaviors diverge. If the requirement was missing or ambiguous, clarify it and let the current session try it. If successive failures each reveal a different defect and the agent still follows the plan, continue debugging. [Evidence 1 and 2 below.]
2. **Save a handoff that can be checked.** Record the goal, the exact requirement or its file location, useful findings with their source paths, the state of the relevant edits, and the next check and expected result. Mark any decision still open. Inspect the actual changes before describing them. A line is worth carrying forward if losing it would change the next action or its acceptance test. [Evidence 2 and 3.]
3. **Choose the conversation boundary.** For one coherent task with useful findings buried in bulky output, request a focused summary that retains the items in step 2. Reopen the underlying files when exact wording or values matter. For unrelated work, start a clean conversation. For the same task repeatedly returning to a discredited assumption, start a clean conversation with the checked handoff. Anthropic suggests a reset after two unsuccessful corrections of the *same* mistake. Use that as a cue to inspect progress. For a small function whose expected behavior and tests are already clear, a fresh implementation from the specification is another option. Save the current diff, leave failed implementations out of the new prompt, and compare the results on the same checks. A chat reset and a file rollback are separate actions. Review the diff before deciding whether any edit needs to be reverted. [Evidence 3, 4 and 6.]
4. **Verify recovery on the missed case.** Before another edit, ask the assistant to use the governing decision to predict the result for the input from step 1 and identify where that decision is recorded. Compare its answer with the original requirement. If it predicts the wrong behavior, resolve the discrepancy before implementation. After the edit, run the check on the actual code, inspect the command and result, and confirm the test still asserts the agreed behavior. A correct prediction checks orientation. A passing check establishes what happened on the case it exercised. [Evidence 2 and 5.]

## Worked example

This is an original, hypothetical example. A command-line tool prints a list of tracks from a playlist. The issue requires the default output to preserve playlist order. An earlier proposal to sort by title was rejected. The assistant has twice restored the sort after being corrected. One useful edit already decodes escaped titles correctly.

The developer inspects the diff and saves this handoff in the issue: “Default listing follows input order. If the input titles are Zebra then Apple, output must be Zebra then Apple. The issue’s default-order paragraph governs. The decoder change in `playlist/reader.py` handles escaped titles and should be preserved. Inspect `playlist/listing.py` for the ordering change. Run `pytest tests/test_listing.py::test_default_preserves_input_order`.”

The old conversation repeatedly brought back the rejected sort, so the developer opens a new one with that handoff and points it to the pending changes. The assistant reads the issue and predicts Zebra first. It then removes the default sort from the listing code. The developer checks the diff for the decoder change and the test’s expected order, and asks for the command and result. In this scenario the focused test passes. The developer also runs the existing escaped-title check because retaining that edit was part of the handoff. If the earlier conversation had stayed aligned and had merely accumulated parser traces, the developer could instead have compacted it around the order rule, decoder finding, file paths, and tests.

## Evidence for the decisions

| Evidence | Claim IDs | What the original supports | How this pattern uses it |
|---|---|---|---|
| 1. A supplied fact can still be missed | SRC-0001:C01, SRC-0001:C02, SRC-0001:C04 | Many tested models answered single-prompt Wikipedia questions less accurately with the answer passage in the middle. Performance on exact key lookup varied by model and task. [§§2.1 and 2.3, Fig. 5, pp. 159–162](https://aclanthology.org/2024.tacl-1.9.pdf#page=3) · [§3.2, Fig. 7, p. 163](https://aclanthology.org/2024.tacl-1.9.pdf#page=7) | Empirical support for the diagnostic possibility only. Asking for a concrete mismatch before changing sessions is our adaptation. The experiment supplies no test of coding-session drift, reset or compaction. |
| 2. Make the requirement retrievable | SRC-0002:C05, SRC-0002:C06 | Anthropic advises eliciting decisions, writing a spec that a fresh implementation session can read, and specifying the location, symptom, and success condition of a fix. [Interview and saved-spec example](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first) · [Fix prompt example](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt) | Direct practitioner advice for a written handoff. The field selection, one distinguishing input and prediction before editing are our adaptations. |
| 3. Preserve useful history or switch tasks | SRC-0002:C01, SRC-0002:C02, SRC-0002:C17 | The guide recommends clearing between unrelated tasks and naming what a summary should retain during a continuing task. It revises older advice about aggressive window management. [Cost and context, clear and compact bullets](https://code.claude.com/docs/en/best-practices#keep-cost-and-context-down) · [Superseded advice, first table row](https://code.claude.com/docs/en/best-practices#what-you-can-stop-doing) | Direct vendor guidance. Our decision criterion uses the value of the remaining history. Checking summary details against their sources is our safeguard. |
| 4. Recognize a failed correction and separate the file decision | SRC-0002:C03, SRC-0002:C04 | The guide gives its two-correction heuristic and describes separate conversation and file rewind choices. Its checkpoints cover edits made with the main conversation’s file tools. [Session steering, clear and rewind bullets and checkpoint warning](https://code.claude.com/docs/en/best-practices#steer-the-session) | The trigger is practitioner judgment. The rewind choices describe Claude Code. Inspecting the diff and recording useful partial work make this distinction usable across tools. |
| 5. Obtain evidence after recovery | SRC-0002:C07, SRC-0002:C08, SRC-0002:C10 | Anthropic recommends giving the assistant a check, requesting execution evidence, and reviewing changes against the spec and edge cases. [Checks, examples and evidence request](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Spec review prompt](https://code.claude.com/docs/en/best-practices#review-against-your-spec) | Direct practitioner advice. Reusing the particular missed case and inspecting its assertion are our adaptations. A passing case supplies limited evidence for that case. |
| 6. Retry a bounded problem from its specification | SRC-0003:C01, SRC-0003:C02, SRC-0003:C06, SRC-0003:C07, SRC-0003:C08 | On HumanEval, the researchers compared continued repair against a scheduled fresh generation from the original problem statement, with six attempts available under each policy. Table 2 reports higher final solve rates for all nine model configurations at the later model-specific schedule. At the earlier schedule seven improved and two declined (Codestral 22B and Devstral 24B). Counts follow the table where the surrounding prose differs. [RQ3 and protocol, pp. 4–5](https://www.nature.com/articles/s41598-025-27846-5.pdf?code=7b2&error=cookies_not_supported#page=4) · [Table 2, baseline and two restart columns, p. 6](https://www.nature.com/articles/s41598-025-27846-5/tables/2?code=7b2&error=cookies_not_supported) | Empirical evidence for a spec-only retry on short Python functions with executable tests. Our choice to preserve a working diff and compare candidates against the missed case adapts the experiment to a developer’s repository. The benchmark retained no handoff for the fresh generation. |

## Different source perspectives

Liu and colleagues varied the position of evidence in single prompts. Their retrieval results help explain why it is worth checking whether an assistant can apply a supplied fact. Anthropic offers operational guidance for Claude Code, including automatic compaction on current models. Its two-correction cue concerns repetitions of the same mistake. Adnan and Kuhn independently tested a related intervention on short Python tasks. Their model-specific schedules used measured repair effectiveness across benchmark problems, so their results cannot calibrate Anthropic’s cue for an individual chat.

The benchmark restart changed two things together. The model lost the failed repair history and received a request to generate a solution from the original specification. Also, each successful problem left the repair pool, changing which problems were eligible on subsequent attempts. Neither a declining rescue rate nor a successful restart identifies why a particular assistant repeated a mistake. The full workflow here, including a checked handoff and selective retention of repository edits, awaits a comparative test. [SRC-0003:C02, C03, C06, C10 and C11, protocol pp. 4–5 and discussion pp. 9–10](https://www.nature.com/articles/s41598-025-27846-5.pdf?code=7b2&error=cookies_not_supported#page=5)

## Tradeoffs, failure modes, and when to skip the pattern

Starting fresh can discard the only record of a design decision. Compaction can preserve a mistaken premise or omit an exact compatibility rule. Verify the handoff while the original record is still available. A fresh chat can reopen files that still encode the mistaken change. Check the working tree even if the conversation is empty. If the repository or specification itself contains the wrong rule, correct or clarify that source first.

A long session making verifiable progress can continue. A series of different failing tests can give good reasons for further investigation. A missing reproduction, an unavailable dependency, or an undecided product behavior calls for resolving that obstacle. Repeated resets alone supply none of those prerequisites.

## Variations and practical adaptations

- **No compaction command.** Write the focused handoff yourself and open a new chat with it. This recreates continuity from selected facts and may require rediscovery. Our adaptation of evidence 2 and 3.
- **Exact wording matters.** Point to the precise specification paragraph and ask the new session to apply it to the disputed input. Keep the summary as an index. Our adaptation of evidence 2 and 5.
- **Visual behavior.** For a clipping bug, identify the viewport and sample content that made the problem visible and inspect the result at that size after the edit. This adapts Anthropic’s screenshot-based verification example in evidence 5.

## Related topics and families

BP-06 (context management) is the primary retrieval path. BP-01 covers preserving a decision across sessions, AP-01 covers repeated failed corrections, and BP-03 covers starting a conversation afresh while assessing existing code separately. OB-01 and OB-10 describe possible symptoms. This pattern gives no diagnostic test for an underlying attention mechanism. Related families are context management, workflow, and reliability. [Catalog and topic map](../source-topic-map.md)

## Sources and verification

- Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. “Lost in the Middle: How Language Models Use Long Contexts.” *Transactions of the Association for Computational Linguistics* 12 (2024), 157–173. [SRC-0001 dossier](../sources/SRC-0001--lost-in-the-middle.md) · [Local dossier](../sources/SRC-0001--lost-in-the-middle.md) · [Independent source audit](../audits/SRC-0001--verification.md) · [Original paper](https://aclanthology.org/2024.tacl-1.9/)
- Anthropic. “Best practices for Claude Code.” Claude Code Docs, accessed 2026-11-21. Publication date and version unknown. [SRC-0002 dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Local dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Independent source audit](../audits/SRC-0002--verification.md) · [Original guide](https://code.claude.com/docs/en/best-practices)
- Muntasir Adnan and Carlos C. N. Kuhn. “Measuring and mitigating debugging effectiveness decay in code language models.” *Scientific Reports* 15, 44120 (18 December 2025). [SRC-0003 dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Independent source audit](../audits/SRC-0003--verification.md) · [Original paper](https://www.nature.com/articles/s41598-025-27846-5)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/PAT-0001--verification.md)

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/SRC-0001--verification.md](../audits/SRC-0001--verification.md) · [Local copy](../audits/SRC-0001--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0001--lost-in-the-middle.md](../sources/SRC-0001--lost-in-the-middle.md) · [Local copy](../sources/SRC-0001--lost-in-the-middle.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
- [topics/AP-01--sunk-cost-over-iteration.md](../topics/AP-01--sunk-cost-over-iteration.md) · [Local copy](../topics/AP-01--sunk-cost-over-iteration.md)
- [topics/BP-01--knowledge-checkpointing.md](../topics/BP-01--knowledge-checkpointing.md) · [Local copy](../topics/BP-01--knowledge-checkpointing.md)
- [topics/BP-03--happy-to-delete-start-fresh.md](../topics/BP-03--happy-to-delete-start-fresh.md) · [Local copy](../topics/BP-03--happy-to-delete-start-fresh.md)
- [topics/BP-06--context-management-discipline.md](../topics/BP-06--context-management-discipline.md) · [Local copy](../topics/BP-06--context-management-discipline.md)
- [topics/OB-01--context-rot.md](../topics/OB-01--context-rot.md) · [Local copy](../topics/OB-01--context-rot.md)
- [topics/OB-07--solution-fixation.md](../topics/OB-07--solution-fixation.md) · [Local copy](../topics/OB-07--solution-fixation.md)
- [topics/OB-10--limited-attention-focus.md](../topics/OB-10--limited-attention-focus.md) · [Local copy](../topics/OB-10--limited-attention-focus.md)
