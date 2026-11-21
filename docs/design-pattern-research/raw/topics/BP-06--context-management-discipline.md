---
topic_id: BP-06
title: Context management discipline
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0002
    relationship: DIRECT
    strength: moderate
    finding: "Anthropic recommends focused compaction for ongoing work and clearing between unrelated tasks or after repeated failure on the same correction."
  - id: SRC-0006
    relationship: DIRECT
    strength: moderate
    finding: "Pocock describes retaining planning context when a specification may be truncated and giving bounded tickets to fresh implementation sessions."
  - id: SRC-0001
    relationship: SUPPORTING
    strength: high
    finding: "Controlled fixed-prompt tasks show that use of relevant material depends on its placement, distractors, model and task."
  - id: SRC-0003
    relationship: SUPPORTING
    strength: moderate
    finding: "Replacing a sequential repair with spec-only generation sometimes improved HumanEval results under a fixed attempt cap."
  - id: SRC-0004
    relationship: SUPPORTING
    strength: high
    finding: "Correct API documentation improved call validity in a benchmark, while unreliable retrieval could lower it."
  - id: SRC-0020
    relationship: CONTRADICTORY
    strength: moderate
    finding: "Automatically generated repository context files raised inference costs without a clear resolution benefit on two issue-resolution benchmarks."
pattern_ids: [PAT-0001, PAT-0002]
---

# BP-06 Context management discipline

## When it comes up

- “We’re still on one task, but the useful findings are buried in logs.”
- “The agent has gone back to the same rejected assumption twice.”
- “The API contract is missing. Should I paste the whole reference?”
- “I’ll start a fresh session once the plan is ready. What will it need to continue?”

The brief asks how to choose what to add, carry forward or reset. There is direct procedural guidance for those choices and experimental evidence for specific context interventions. Routine manual context trimming, a universal restart interval and the relative merits of compaction versus a fresh session on the same repository task remain unmeasured here.

## What goes into the next turn

Anthropic recommends focused compaction for a continuing task and clearing between unrelated tasks. Two failed corrections of the same mistake are its cue to reconsider the session. A written spec can carry agreed requirements into a fresh implementation session. The current guide also lists aggressive window management among its earlier recommendations that users can drop, citing current context capacity and automatic compaction. Pocock independently describes keeping specification and ticket decomposition together when the spec might be truncated on retrieval, with fresh implementation sessions for bounded tickets. The two workflows put the boundary where the next session has a complete enough handoff. Pocock’s article and companion skill describe the same workflow. SRC-0002:C01–C05, SRC-0002:C17, SRC-0006:C01–C03 and SRC-0006:C09. [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Compaction and session boundaries](https://code.claude.com/docs/en/best-practices#keep-cost-and-context-down) · [Steering](https://code.claude.com/docs/en/best-practices#steer-the-session) · [Superseded advice](https://code.claude.com/docs/en/best-practices#what-you-can-stop-doing) · [Pocock dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Planning and ticket dispatch](https://www.aihero.dev/skills-to-tickets#common-questions)

Actual information needs can outweigh the cost of an addition. In CloudAPIBench, giving StarCoder2-3B the guaranteed correct signature raised overall call validity from 41.80% to 86.82%. A separate retrieval condition at 50% correct-document inclusion improved GPT-4o’s rare-call slice and hurt its common-call slice. Liu and colleagues found that many tested models used middle evidence less successfully in long QA inputs. Repeating the query yielded large gains on UUID lookup and little or adverse change on most QA positions. Together the experiments favor checking relevance and sufficiency case by case. They manipulate different tasks and give no measured rule for the order or size of an agent handoff. SRC-0004:C05, SRC-0004:C06, SRC-0001:C02, SRC-0001:C06 and SRC-0001:C08. [API documentation dossier](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Oracle documentation, §III-B and Fig. 6](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5) · [Retrieval precision results, Fig. 7 and Table IV](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=7) · [Long-context dossier](../sources/SRC-0001--lost-in-the-middle.md) · [QA positions, §2.3 and Fig. 5](https://aclanthology.org/2024.tacl-1.9.pdf#page=5) · [Query duplication, §4.2](https://aclanthology.org/2024.tacl-1.9.pdf#page=7)

Blanket appending faces a separate counterpoint from repository tasks. Gloaguen and colleagues found that generated agent files raised mean inference cost by 20% and 23% on the two tested benchmarks. The task-resolution comparisons against omission were inconclusive. This limits a default of loading generated repository background at the start of every issue. Selectively opening a needed file during work is a different intervention. SRC-0020:C01, SRC-0020:C02, SRC-0020:C04 and SRC-0020:C10. [Repository context file dossier](../sources/SRC-0020--repository-context-files.md) · [Resolution and cost, §4.2 and Tables 2–3](https://arxiv.org/pdf/2602.11988v3#page=6)

## When to preserve or restart

On HumanEval, Adnan and Kuhn compared continuing sequential repair with a scheduled fresh generation from the benchmark spec. All nine displayed configurations improved at the later schedule in Table 2, while two fell below baseline at the earlier schedule. Clearing the history also changed the assignment from repair to generation. The result supports trying a fresh path for some bounded tasks. It cannot settle whether old context, the failing code or the change in task caused the improvement. These experiments, the fixed-prompt studies and the practitioner workflows have distinct provenance and interventions. SRC-0003:C06, SRC-0003:C08, SRC-0003:C10 and SRC-0003:C11. [Restart study dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Table 2](https://www.nature.com/articles/s41598-025-27846-5/tables/2) · [Discussion and limitations](https://www.nature.com/articles/s41598-025-27846-5)

[PAT-0001, Recover a drifting coding session](../patterns/PAT-0001--recover-a-drifting-coding-session.md) applies these findings to the next step. If a missing requirement explains the problem, add its authoritative source and a case that distinguishes the expected behavior. If the task is coherent and history is mostly noise, summarize for that goal and reopen exact contracts as needed. If the task changes or a rejected assumption keeps returning, take a checked handoff into a fresh session. Inspect the working diff as a separate decision about what edits to preserve. The handoff format, pre-edit orientation question and post-edit check are catalog adaptations. The check establishes recovery on the chosen case. [Pattern verification](../audits/PAT-0001--verification.md)

[PAT-0002, Verify an unfamiliar API call](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) covers the targeted-append case. Match the reference to the installed dependency and receiver, then supply the verified signature and behavior detail needed for the next edit. The catalog pattern pairs that reference with an observable behavior check because a valid invocation can still do the wrong thing. [Pattern verification](../audits/PAT-0002--verification.md)

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/PAT-0002--verification.md](../audits/PAT-0002--verification.md) · [Local copy](../audits/PAT-0002--verification.md)
- [audits/SRC-0001--verification.md](../audits/SRC-0001--verification.md) · [Local copy](../audits/SRC-0001--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [audits/SRC-0004--verification.md](../audits/SRC-0004--verification.md) · [Local copy](../audits/SRC-0004--verification.md)
- [audits/SRC-0006--verification.md](../audits/SRC-0006--verification.md) · [Local copy](../audits/SRC-0006--verification.md)
- [audits/SRC-0020--verification.md](../audits/SRC-0020--verification.md) · [Local copy](../audits/SRC-0020--verification.md)
- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [patterns/PAT-0002--verify-an-unfamiliar-api-call.md](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) · [Local copy](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0001--lost-in-the-middle.md](../sources/SRC-0001--lost-in-the-middle.md) · [Local copy](../sources/SRC-0001--lost-in-the-middle.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
- [sources/SRC-0004--api-documentation-and-hallucinations.md](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Local copy](../sources/SRC-0004--api-documentation-and-hallucinations.md)
- [sources/SRC-0006--vertical-slices-for-agent-tickets.md](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Local copy](../sources/SRC-0006--vertical-slices-for-agent-tickets.md)
- [sources/SRC-0020--repository-context-files.md](../sources/SRC-0020--repository-context-files.md) · [Local copy](../sources/SRC-0020--repository-context-files.md)
