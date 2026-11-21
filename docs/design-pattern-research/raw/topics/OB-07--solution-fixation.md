---
topic_id: OB-07
title: "Solution fixation"
coverage: partially supported
source_edges:
  - id: SRC-0003
    relationship: SUPPORTING
    strength: moderate
    finding: "A specification-only restart improved final HumanEval pass rates at some model-specific schedules, but the study did not isolate commitment to the first approach."
  - id: SRC-0008
    relationship: SUPPORTING
    strength: moderate
    finding: "Allocating most candidates to repairs of a few original programs sometimes lost to fresh sampling under matched candidate caps."
  - id: SRC-0016
    relationship: DIRECT
    strength: moderate
    finding: "Some failed agent trajectories repeated unsuccessful actions, including a documented debugging example where switching approaches helped."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic advises clearing the session after repeated unsuccessful correction of the same mistake."
pattern_ids: [PAT-0004, PAT-0001]
publication_status: published
---

# OB-07 — Solution fixation

“I keep showing the same failing case and the assistant keeps patching around it.” “It keeps calling its first guess the root cause, even after the logs point somewhere else.” The brief asks whether the model prematurely narrows the search and treats an initial hypothesis as settled. Repeated behavior is documented in coding evaluations. How often an initial idea causes that behavior, suppresses alternatives or becomes an apparently established fact is still open.

## What the sources show

- **Repeated steps occur in failed runs.** Kwa et al. coded repetition in 12/31 failed GPT-4 1106 runs and 2/32 failed o1 runs. Premature abandonment was also present, in 8/31 and 16/32 respectively. These are failure-only samples with different task mixes. A selected Python debugging trajectory shows additional problems during correction and eventual success after a change of approach. These records show a behavior a developer can recognize, with no estimate of its prevalence across all runs. SRC-0016:C06–C07, §3.3 Table 2 and Appendix D.2.1. [Dossier](../sources/SRC-0016--task-duration-and-reliability.md) · [Versioned paper](https://arxiv.org/html/2503.14499v4)
- **Starting over sometimes improves the same-budget result.** Adnan and Kuhn compare continued feedback-conditioned repair with a new specification-only generation at a scheduled attempt. In the nine Table 2 rows, each model improved at one or both schedules, and two got worse at the earlier tested schedule. Treat the published table as the numerical basis because the neighboring prose disagrees with it. Earlier successes exit the retry pool, so changing task difficulty can contribute to lower rescue rates later. A restart also drops failed code and execution feedback and changes the request from repair to generation. The proposed accounts include repeated exploitation, context effects and accumulated errors. SRC-0003:C02–C03, C06–C11, RQ3 pp. 4–5, Table 2 pp. 6–7 and Discussion pp. 9–10. [Dossier](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Paper](https://www.nature.com/articles/s41598-025-27846-5)
- **A repair still has value when it starts from a useful failure.** Olausson et al. found GPT-4 on APPS at 66.1% with ten initial programs and one repair per initial program, versus 63.1% for a matched fresh-only cap of 20. With two initial programs and ten repairs per initial program, the hybrid scored 61.8% versus 63.4% at a cap of 22. Those repairs are siblings from a common program, so the second case measures investment in few starting programs without an accumulated repair conversation. A separate comparison found more test-passing repairs with human diagnoses, indicating that feedback quality can matter as well. SRC-0008:C02, C04–C06, C09–C11, Fig. 3b p. 6 and §4.3 Table 1 pp. 8–9. [Dossier](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Conference paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=6)

Adnan and Kuhn and Olausson et al. ran separate experiments with shared HumanEval tasks, different repair protocols and different outcomes. The APPS comparison and METR's agent runs add distinct task evidence. None tracks the model's ranking of alternative explanations across turns. Calling the observed behavior anchoring is a hypothesis, especially when the first idea came from the user or the failing test gives little diagnostic information.

## Where the patterns apply

[Compare repair with fresh candidates](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) holds the requirement and acceptance checks fixed when the current implementation is only one plausible candidate. [Recover a drifting coding session](../patterns/PAT-0001--recover-a-drifting-coding-session.md) fits when several turns keep reintroducing a disproved assumption and there is a reliable handoff to preserve. Anthropic's two-correction cue is practitioner advice for recognizing repeated mistakes. Its guide supplies no optimum turn count. SRC-0002:C03. [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session)

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/PAT-0004--verification.md](../audits/PAT-0004--verification.md) · [Local copy](../audits/PAT-0004--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [audits/SRC-0008--verification.md](../audits/SRC-0008--verification.md) · [Local copy](../audits/SRC-0008--verification.md)
- [audits/SRC-0016--verification.md](../audits/SRC-0016--verification.md) · [Local copy](../audits/SRC-0016--verification.md)
- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [patterns/PAT-0004--compare-repair-with-fresh-candidates.md](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) · [Local copy](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
- [sources/SRC-0008--self-repair-versus-fresh-samples.md](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Local copy](../sources/SRC-0008--self-repair-versus-fresh-samples.md)
- [sources/SRC-0016--task-duration-and-reliability.md](../sources/SRC-0016--task-duration-and-reliability.md) · [Local copy](../sources/SRC-0016--task-duration-and-reliability.md)
