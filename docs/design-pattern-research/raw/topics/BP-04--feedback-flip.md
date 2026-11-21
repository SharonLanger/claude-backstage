---
topic_id: BP-04
title: Feedback flip
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0008
    relationship: DIRECT
    strength: moderate
    finding: "The benchmark compares diagnosis and repair by the generating model with feedback from another model or a human, with gains that depend on the repair setup."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic recommends runnable checks and a separate-context evaluation of the diff against the specification."
pattern_ids: [PAT-0004]
---

# BP-04 Feedback flip

## When it comes up

- “The assistant wrote the patch. Can it now help identify what the patch missed?”
- “The agent explained the failing test, but its explanation sounds like a defense of the implementation.”
- “Would I get more useful review from the same session, a second model, or a teammate?”

The brief asks whether the producer can become an evaluator and catch problems it introduced. There is evidence for diagnosis and repair after an observable failure on programming benchmarks. The effect of a general producer-to-reviewer role switch in the same coding conversation remains open.

## How the evidence fits

Olausson et al. let the evaluator test the generated program and pass failure evidence into a diagnosis-and-repair step. In the same-model condition, the diagnosis and repair come from one completion. Gains relative to fresh-only sampling depend on the model, benchmark, and split between initial candidates and repairs. The design leaves unresolved what the natural-language diagnosis adds relative to providing the test failure alone. It also leaves prompt wording and review accuracy outside the comparison. The finding concerns finding a passing program with access to executable benchmark tests. `SRC-0008:C01`, `SRC-0008:C02`, `SRC-0008:C05`, `SRC-0008:C06`, `SRC-0008:C11`. [Dossier](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [ICLR §§2–3.2, Figs. 1–2, pp. 2–5](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=3) · [§4.1, pp. 5–7](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=5)

The paper reports stronger results from different feedback sources in some configurations. Stronger-model feedback improved on same-model repair and fresh-only baselines for the tested pairs under candidate-count accounting. That comparison also changed the prompting from joint to separate stages. With 40 failing programs drawn from 20 APPS tasks, 52.60% of sampled GPT-4 repairs passed with human-written diagnoses and 33.30% with GPT-4 diagnoses. The participants had access to model explanations, and the repaired programs share tasks, starting programs, and diagnoses. These are two experiments within the same publication. Neither estimates the time required for human review. `SRC-0008:C08`, `SRC-0008:C09`, `SRC-0008:C10`. [ICLR §§4.2–4.3, Fig. 5 and Table 1, pp. 7–9](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=8) · [Appendix D, p. 24](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=24)

Anthropic’s separate product guide puts runnable checks and review against a specification alongside generation. Its review subagent starts in a fresh context. That gives a practitioner a way to evaluate a change before revising it. A separate context can still share the same model family, incomplete checks, and mistaken requirements. The guide offers advice and a documented feature. It gives no comparison of defect-detection rates across review arrangements. `SRC-0002:C07`, `SRC-0002:C08`, `SRC-0002:C09`, `SRC-0002:C10`, `SRC-0002:C15`. [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Review against your spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

## Use in coding work

[PAT-0004, Compare repair with fresh candidates](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) applies the findings to a bounded failure. State what the program did and what it should have done, check the proposed diagnosis against that evidence, then test a repair or fresh candidate against the same acceptance checks. The explicit diagnostic check and reviewer-controlled acceptance tests are catalog adaptations. Claims that a same-session role prompt reliably catches bugs, that it can replace independent review, or that the routine saves review time lack direct tests in these sources. [Pattern verification](../audits/PAT-0004--verification.md)

## Drive navigation

- [audits/PAT-0004--verification.md](../audits/PAT-0004--verification.md) · [Local copy](../audits/PAT-0004--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0008--verification.md](../audits/SRC-0008--verification.md) · [Local copy](../audits/SRC-0008--verification.md)
- [patterns/PAT-0004--compare-repair-with-fresh-candidates.md](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) · [Local copy](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0008--self-repair-versus-fresh-samples.md](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Local copy](../sources/SRC-0008--self-repair-versus-fresh-samples.md)
