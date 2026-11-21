---
topic_id: OB-01
title: "Context rot / degradation"
coverage: partially supported
source_edges:
  - id: SRC-0001
    relationship: DIRECT
    strength: high
    finding: "In controlled long inputs that fit the model, many tested models answered less accurately with the evidence in the middle."
  - id: SRC-0003
    relationship: SUPPORTING
    strength: moderate
    finding: "Some scheduled specification-only restarts improved HumanEval solve rates under the same attempt cap, with the source of the improvement unresolved."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Claude Code documents clearing unrelated history and recommends focused compaction for work that continues."
pattern_ids: [PAT-0001]
publication_status: published
---

# OB-01 — Context rot / degradation

“It followed our constraint at first, but after several turns it keeps changing the wrong file.” “The window still has room. Why did the answer get worse?” Controlled results support performance losses at some positions within usable windows. Evidence for a growing coding conversation weakening a particular earlier instruction is indirect. The proposed focus, effective and red zones have no validated cutoffs in this set.

## What the sources measure

- **Where evidence sits can matter before the window is full.** Liu et al. moved the supporting paragraph within 10-, 20- and 30-document question-answering inputs. Many model variants scored worse in the middle than at the ends. GPT-3.5-Turbo and its 16K variant had similar position curves where both could process the 10- and 20-document inputs. The effect was task- and model-dependent. Adding another copy of the query brought GPT-3.5-Turbo (16K) to perfect 300-pair lookup in that condition, whereas the QA comparison showed small gains at the start and small losses elsewhere. These experiments move evidence in a single assembled input. They leave the trajectory of an earlier instruction across chat turns open. SRC-0001:C01–C04, C06, C11, §§2.1–2.3 Fig. 5, §§3.1–3.2 Fig. 7, §4.2 Fig. 9 and Appendices D–E. [Dossier](../sources/SRC-0001--lost-in-the-middle.md) · [Original paper](https://aclanthology.org/2024.tacl-1.9/)
- **A clean specification can help after unsuccessful repairs.** Adnan and Kuhn compared feedback-conditioned repairs with a scheduled specification-only generation on HumanEval under a six-attempt cap. Table 2 records improvement at one or both schedules for all nine listed models, while two fell below baseline at the earlier tested schedule. The table and adjacent narrative disagree, so the comparison uses the table. The retry pool also changes as solved problems leave it. Restarting removes failed code and execution feedback and changes the request from repair to generation. Those changes prevent isolation of long-history degradation, and the baseline history depth is unspecified. SRC-0003:C02–C03, C06–C08, C10–C11, RQ3 pp. 4–5, Table 2 pp. 6–7 and Discussion pp. 9–10. [Dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Original paper](https://www.nature.com/articles/s41598-025-27846-5)
- **Current product advice depends on the task boundary.** Anthropic advises clearing an unrelated task and supplying a focus when compacting a continuing one. Its guide also de-emphasizes aggressive routine context management given larger windows and automatic compaction. These are recommendations and product descriptions with no controlled measure of quality by context fill. SRC-0002:C01–C03, C17, “Keep cost and context down,” “Steer the session” and “What you can stop doing.” [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Original guide](https://code.claude.com/docs/en/best-practices)

Liu et al. and Adnan and Kuhn use distinct tasks and outcomes. A position effect on answer retrieval and a restart effect on passing code tests can coexist without sharing a mechanism. The code study itself builds on the PyCapsule protocol. The vendor guide supplies a separate operational judgment rather than a replication. Together the sources leave open when chat growth matters most, which constraints become vulnerable and whether usable context has distinct zones.

## Where the pattern applies

[Recover a drifting coding session](../patterns/PAT-0001--recover-a-drifting-coding-session.md) fits a repeatedly missed requirement with a concrete check and a reliable handoff. It provides a way to preserve the working state, carry forward the requirement and verify the behavior after compaction or restart. The combined repository workflow and a universal restart threshold remain unmeasured.

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/SRC-0001--verification.md](../audits/SRC-0001--verification.md) · [Local copy](../audits/SRC-0001--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0001--lost-in-the-middle.md](../sources/SRC-0001--lost-in-the-middle.md) · [Local copy](../sources/SRC-0001--lost-in-the-middle.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
