---
topic_id: AP-08
title: "Obsessing over rules"
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0020
    relationship: SUPPORTING
    strength: moderate
    finding: "Repository instruction files increased inference expense and tool steps in benchmark runs, while their effect on resolution against file omission remained inconclusive."
  - id: SRC-0002
    relationship: DIRECT
    strength: low
    finding: "Anthropic recommends short always-loaded guidance, scoped instructions and application controls for inflexible requirements."
  - id: SRC-0001
    relationship: SUPPORTING
    strength: low
    finding: "Controlled retrieval experiments show that evidence placement affects performance for many tested models, with varying results across tasks and checkpoints."
pattern_ids: []
---

# AP-08 Obsessing over rules

- “We add a standing instruction every time the agent misses something. It still misses the important ones.”
- “A one-file change now makes the agent inspect every component and run the whole suite.”
- “All of our guidance is in one file. Which parts affect this task, and which are required every time?”

The brief asks whether continually adding rules makes an agent less compliant because the rules compete for attention. The sources establish recurring work from loaded guidance and offer ways to scope that guidance. There is no measured relationship here between the number of simultaneous obligations and the proportion followed. The proposed attention mechanism remains untested for this workflow.

## What changes when guidance is loaded

Gloaguen and colleagues compared omitted, generated and, on CTXbench, developer-committed repository context files. Automatically generated files increased mean inference cost by **20%** on SWE-bench Lite and **23%** on CTXbench. Tool steps also increased. Resolution estimates versus omission were inconclusive for both file types. Developer-committed files performed better than generated files on CTXbench, and agents used named tools more often. That result distinguishes the ability to steer an action from the ability to improve test-based task resolution. The study compared packages of guidance in Python repositories, so wording and contents varied together. SRC-0020:C01–C06. [Dossier](../sources/SRC-0020--repository-context-files.md) · [§4.2, Fig. 3 and Tables 2–3](https://arxiv.org/pdf/2602.11988v3#page=6) · [§4.3, Figs. 4–6](https://arxiv.org/pdf/2602.11988v3#page=7) · [Appendix A.5, Table 6](https://arxiv.org/pdf/2602.11988v3#page=16)

Longer files showed no clear relationship with cost or resolution in the CTXbench bins. Removing some categories of guidance lowered cost in a separate ablation, with inconclusive accuracy changes. A modified CTXbench with other documentation removed yielded a reported 2.7-point improvement from generated files without a reported significance test. These findings put limits on treating longer files or additional guidance as inherently worse. Natural file lengths are an imperfect proxy for the number of applicable rules. The benchmark outcome concerns patch tests and leaves individual rule adherence unscored. SRC-0020:C07–C10. [Appendix B, Figs. 12–13 and Table 7](https://arxiv.org/pdf/2602.11988v3#page=16)

Anthropic’s independently authored product guide favors brief standing instructions about facts that are unavailable or misleading in the repo, path-scoped rules and procedures loaded when needed. It puts hard requirements in application controls with defined scope. These are design choices practitioners can inspect. The guide offers no controlled test of compliance by rule count, and its Stop-hook example has a documented consecutive-block cap. Liu and colleagues’ independent long-context experiments found many models retrieved evidence less successfully from the middle. Placement effects varied across checkpoints, and a query repetition that helped a simple lookup had mixed effects in question answering. Those experiments concern retrieval of evidence among distractors. They provide an analogy for why where a rule appears might matter, while leaving instruction competition and an optimal number of rules unresolved. SRC-0002:C11–C14 and SRC-0001:C01–C06, C11. [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Short repository guidance](https://code.claude.com/docs/en/best-practices#keep-claudemd-short) · [Path-specific rules](https://code.claude.com/docs/en/best-practices#scope-rules-to-one-part-of-the-codebase) · [Application controls](https://code.claude.com/docs/en/best-practices#deterministic-and-non-deterministic-instructions) · [Stop-hook example](https://code.claude.com/docs/en/best-practices#enforce-the-check-with-a-stop-hook) · [Liu et al. dossier](../sources/SRC-0001--lost-in-the-middle.md) · [§2.3 and Fig. 5](https://aclanthology.org/2024.tacl-1.9.pdf#page=5) · [§4.2 and Fig. 9](https://aclanthology.org/2024.tacl-1.9.pdf#page=7)

## Work on the rule that caused the problem

There is no accepted catalog pattern for testing rule accumulation. A practitioner adaptation is to identify the behavior a proposed standing rule should change and the contexts where it applies. For example, if a global rule makes documentation edits run the full integration suite, compare the current guidance with a version that points edits of that kind to the applicable documentation check. Keep the checkout, agent configuration and acceptance checks comparable. Record both whether the agent obeyed the target rule and whether the patch meets the task, alongside the steps and checks it used. Keep facts that apply across the repository in standing guidance and move a component convention to its scope. Where an invariant has to hold even when prose is missed, use an enforceable check on the applicable path. This comparison and its decision criteria are local adaptations. Testing the brief’s mechanism would require varying the number of simultaneously applicable rules and measuring adherence to each while controlling for placement, wording and task mix. SRC-0020:C05, C07–C10 and SRC-0002:C11–C14. [Gloaguen et al., §4.3](https://arxiv.org/pdf/2602.11988v3#page=7) · [Appendix B, ablations](https://arxiv.org/pdf/2602.11988v3#page=16) · [BP-09, Decision guards](BP-09--decision-guards.md)

## Drive navigation

- [audits/SRC-0001--verification.md](../audits/SRC-0001--verification.md) · [Local copy](../audits/SRC-0001--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0020--verification.md](../audits/SRC-0020--verification.md) · [Local copy](../audits/SRC-0020--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0001--lost-in-the-middle.md](../sources/SRC-0001--lost-in-the-middle.md) · [Local copy](../sources/SRC-0001--lost-in-the-middle.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0020--repository-context-files.md](../sources/SRC-0020--repository-context-files.md) · [Local copy](../sources/SRC-0020--repository-context-files.md)
