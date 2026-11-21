# Design-pattern research

This collection asks what engineers can do when AI-assisted coding goes off track and what published evidence supports those practices. Start with the [source–topic map](raw/source-topic-map.md) to look up a symptom, find a method, and trace it to the research behind it.

## Start here

1. **Source–topic map.** Which topics, methods, and sources relate to the problem I’m investigating? Start with “Find a practice by symptom” or the coverage table. [Open the map](raw/source-topic-map.md)
2. **Original brief and research runbook.** What questions did the researchers start with, and how did they turn publications into dossiers and methods? The mission and execution phases explain the approach. Appendix A contains the original assignment. [Open the runbook](raw/00-START-HERE-RESEARCH-RUNBOOK.md)
3. **Final quality audit.** Which claims and examples did reviewers check, what changed, and where does the evidence stop? [Open the audit](raw/audits/final-quality-audit.md)

## Inventory

| Location | Files | What you’ll find |
| --- | ---: | --- |
| [`raw/`](raw/) | 3 | The original brief and runbook, the [source–topic map](raw/source-topic-map.md), and the [research status](raw/research-status.md) with decisions, assignments, and the artifact register. The runbook’s pre-research status reflects when it was written. |
| [`raw/topics/`](raw/topics/) | 31 | One synthesis per starting question: 12 model behavior obstacles, nine human workflow anti-patterns, and ten proposed practices. Each note compares what supports or complicates the proposition and what remains open. [Coverage table](raw/source-topic-map.md#coverage-of-the-31-research-questions) |
| [`raw/patterns/`](raw/patterns/) | 8 | One reviewed method per file. Each gives symptoms, steps, a worked example, tradeoffs, and evidence for the recommendations. A method can address several topics. [Methods by symptom](raw/source-topic-map.md#find-a-practice-by-symptom) |
| [`raw/sources/`](raw/sources/) | 24 | One dossier per distinct publication, with an analytical reading, numbered claims, exact source locations, and scope and reuse notes. A dossier can support multiple findings. [Source register](raw/source-topic-map.md#source-register) |
| [`raw/audits/`](raw/audits/) | 33 | 24 source reviews, eight method reviews, and the [final collection audit](raw/audits/final-quality-audit.md). |

The map’s 31 topic IDs, eight method IDs, and 24 source IDs match the folder inventory. Findings are the observations recorded in topic syntheses and claim ledgers. The research counts 263 distinct dossier claims. The 99 imported Markdown files include the pre-existing runbook and all 98 published research outputs. The final review’s 97-file readback predates its own publication.

## How to follow the evidence

1. In the map’s coverage table, find **OB-09 Hallucination in code**. The row links to the topic, its method, and three dossiers. [Coverage table](raw/source-topic-map.md#coverage-of-the-31-research-questions)
2. Open OB-09. The note explains how an API call can look legitimate even when the receiver, arguments, or operation are wrong. It links to **Verify an unfamiliar API call** below that comparison. [OB-09 topic note](raw/topics/OB-09--hallucination-in-code.md)
3. In **PAT-0002**, open “Why it might work.” The second row adapts the study into a check against the installed dependency and links to **SRC-0004**. [PAT-0002 evidence table](raw/patterns/PAT-0002--verify-an-unfamiliar-api-call.md#why-it-might-work)
4. In **SRC-0004**, read claims **C03** and **C07** in the ledger. The first distinguishes absent methods, misused targets, and wrong existing operations among invalid calls in a specific benchmark slice. The second explains what a name-only check can miss. The ledger gives the original paper’s table and section. The benchmark measured generated calls on synthetic Python tasks, so the effect of manual verification in a working repository remains open. [SRC-0004 claim ledger](raw/sources/SRC-0004--api-documentation-and-hallucinations.md#claim-level-evidence-ledger)

## What was checked

**Original research.** The researchers scouted public papers, documentation, and practitioner accounts, tracked overlapping evidence, and separated measured results, author advice, and adaptations. The 24 dossiers and eight methods each record an independent PASS review. The final reviewer traced the research links in both directions, checked sample claims against original publications, ran four illustrative examples, and issued an ACCEPT verdict. The reviewer did not rerun the underlying experiments. All eight methods draw on the same Anthropic guide for at least one step, alongside other kinds of evidence. [Research status](raw/research-status.md#acceptance-and-review) · [Final audit](raw/audits/final-quality-audit.md)

**Repository import.** The import used the stored Markdown directly. It preserved the directory structure and compared each internal Drive destination with the listed file or folder identity, using the original relative destinations as a cross-check where paired. The import also checked local paths and headings, rendered the map and representative files, and compared public URL destinations with the originals. Public citations retain their destinations. These checks establish what was copied and where it leads. The research audits document what the evidence supports.

## Known gaps

- The final audit grades all 31 starting propositions as partially supported. There are method routes for 28 topics. Negative bleedthrough (OB-05), cognitive overload (AP-04), and rule accumulation (AP-08) have evidence notes and open questions, with no approved method. Repository outcomes, unseen misalignment, and review fatigue still have evidence gaps. [Audit coverage and limitations](raw/audits/final-quality-audit.md#coverage-dependence-and-rights)
- The runbook’s **Parent project** points outside the collection and is now plain text. The excluded parent material comprises `discovery-backlog.md`, `mvp-local-blog-library.md`, `mvp-runtime-workflow.md`, `mvp-shipped-state.md`, `mvp-sunday-delivery.md`, and the empty `blogs/` folder. The runbook names a separate `source-research-brief.md` email attachment that is absent from the research folder. Its text is embedded in Appendix A. [Research runbook](raw/00-START-HERE-RESEARCH-RUNBOOK.md)
- The original text still uses labels such as “Drive navigation” in headings and describes the historical publication process. The links under those headings now lead to the local files. The import found no unresolved internal destination or Google heading fragment in the original links.

## How this relates to /sl-mentor

PR #5 documents the 270-file catalog baseline that the installed skill uses for recommendations. To consider a research finding for the catalog, follow its evidence and review, compare the proposed guidance with the corresponding catalog entry, and decide whether it improves that entry or warrants a new one. Files in this research folder are reference material. Adding one has no effect on the installed skill or its recommendations.
