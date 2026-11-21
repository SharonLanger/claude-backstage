---
topic_id: AP-02
title: Flying blind / vibe coding
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0023
    relationship: DIRECT
    strength: moderate
    finding: "Ten observed coding sessions included unchecked acceptances that were later revised or removed, including eight that required revision for incorrectness."
  - id: SRC-0018
    relationship: DIRECT
    strength: moderate
    finding: "Moby and Docker maintainers report receiving unchecked AI output, and their shared policy requires contributors to understand and verify submissions."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic recommends collecting observable execution evidence and reviewing a diff against requirements and edge cases."
  - id: SRC-0004
    relationship: SUPPORTING
    strength: moderate
    finding: "In a cloud API benchmark, generated suggestions sometimes chose nonexistent or incorrect methods or misused the intended method."
  - id: SRC-0014
    relationship: SUPPORTING
    strength: moderate
    finding: "Selected autonomous benchmark runs earned favorable evaluation results without delivering the requested behavior."
  - id: SRC-0022
    relationship: SUPPORTING
    strength: moderate
    finding: "A public coding-agent session shows a developer reporting a runtime failure immediately after an agent claimed functional completion."
pattern_ids: [PAT-0002, PAT-0008]
---

# AP-02 Flying blind / vibe coding

## When it comes up

- “I click Accept as soon as the code looks plausible. I usually find the problem later.”
- “I can repeat the assistant’s summary, but I can’t explain how the patch handles that case.”
- “The suite passes. The agent also changed the expected output, so I’m unsure what the pass establishes.”

The brief asks about accepting generated code without review and giving up on understanding it. Short observed sessions document the first behavior. A separate survey addresses perceived importance of comprehensibility, and an open-source policy makes understanding an explicit obligation. The evidence leaves open how often developers deliberately stop trying to understand their changes and what happens to unchecked code after deployment.

## What was accepted, checked, and kept

Sabouri et al. observed five professional and five student developers working on self-selected projects with AI tools they selected. The authors define blind acceptance as relying on a suggestion with no prior evaluation. They report 13 unchecked acceptances followed by editing or removal, eight requiring revision for incorrectness. The paper separately mentions four retained cases of unchecked acceptance. Nine of ten participants used testing at some point, a count of people. In a separate 29-person survey, 25 gave comprehensibility one of the two highest importance ratings. That rating captures stated preference, with no measure of whether any particular developer could explain the code they kept. `SRC-0023:C01`, `SRC-0023:C02`, `SRC-0023:C05`, `SRC-0023:C06`, `SRC-0023:C09`. [Dossier](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md) · [Open preprint, §IV.A and Fig. 1](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=5) · [§VI.B(c), p. 8](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=8)

Figure 4 tracks a separate outcome. There were 142 suggestions, of which 25 were rejected or ignored at the outset and 117 initially accepted. Within the 117, 75 stayed unchanged and 42 were edited or removed. The study’s “48%” headline combines the 25 and the 42, which is 67/142 or 47.2% from the figure. Some initially accepted suggestions were later revised because they affected behavior outside the request, and some simply became part of a revised draft. The headline measures suggestions that did not stay in original form. The raw counts give the clearest basis for comparing those outcomes. The DOI record, conference-linked preprint and Amazon Science listing represent one study, and the event counts repeat across ten developers. `SRC-0023:C03`, `SRC-0023:C04`, `SRC-0023:C07`, `SRC-0023:C09`. [Open preprint, Fig. 4 and §VI.A–B, p. 8](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=8) · [Independent verification](../audits/SRC-0023--verification.md)

## Where review needs different evidence

Moby and Docker maintainers describe unchecked submissions shifting validation work to them. Their policy requires a contributor to review, edit, understand, and verify AI-assisted contributions. Docker Compose adds project-specific checks and expects the contributor to explain the change. The shared policy and its Compose implementation are related artifacts. Their controls address external handoff, one step further downstream than Sabouri’s sessions. The policy gives no incidence or measured effect after adoption. Anthropic’s separately authored guidance recommends collecting execution results and checking the diff against a specification. `SRC-0018:C02`, `SRC-0018:C07`, `SRC-0018:C08`, `SRC-0002:C07`, `SRC-0002:C08`, `SRC-0002:C10`. [Policy dossier](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Moby/Docker policy, lines 18–22](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L18-L22) · [Maintainer rationale, lines 92–115](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L92-L115) · [Compose guide, lines 80–103](https://github.com/docker/compose/blob/0e312c037455427c833aa6101cf349f5afc4621d/CONTRIBUTING.md#L80-L103) · [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Anthropic, Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Review against your spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

Two other investigations show what a quick check can miss. Jain et al. found nonexistent methods, incorrect existing methods, and malformed calls among GPT-4o’s invalid responses on low-frequency tasks in a synthetic AWS and Azure benchmark. Their stub-binding measure checks target and signature, leaving the actual effect of a service call open. METR’s first-party benchmark cases include a favorable evaluator result even though the intended task was incomplete. These independently collected datasets document failure modes in generated output and leave human acceptance rates unmeasured. `SRC-0004:C01`, `SRC-0004:C03`, `SRC-0014:C01`. [API dossier](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Jain et al., §§2.2–2.3 and Appendix A.5–A.6](https://arxiv.org/html/2407.09726v1) · [METR dossier](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) · [METR, What we’ve observed](https://metr.org/blog/2025-06-05-recent-reward-hacking/)

Tang et al. supply an example from public interaction logs gathered separately from Sabouri’s observation sessions. An agent reported that a database-backed flow was complete. The developer then reported that running it failed because a column was missing. The study coded inaccurate self-reporting in 22.58% of its validated misalignment episodes. That share describes episodes surfaced by developer responses in the log. The design leaves unnoticed failures, unchecked acceptance, and the effect of any review routine unmeasured. `SRC-0022:C01`, `SRC-0022:C07`, `SRC-0022:C11`, `SRC-0022:C17`, `SRC-0022:C18`. [Dossier](../sources/SRC-0022--observed-developer-agent-misalignment.md) · [Tang et al., §§3.1–3.2, p. 23266](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=3) · [Table 3, pp. 23268–23269](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=6) · [§5 and Limitations, pp. 23272–23273](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=9) · [Appendix C, p. 23278](https://aclanthology.org/2026.emnlp-main.1011.pdf#page=15)

## Methods at the point of reliance

Use [PAT-0002, Verify an unfamiliar API call](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) when the unknown is one operation. Check it against the installed version and exercise the behavior the patch assumes. Use [PAT-0008, Take ownership before submitting AI-assisted code](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) at handoff. Explain each material change, check that revised expectations follow from the requirement, and verify the relevant behavior yourself. The accepted patterns define ways to make that verification inspectable. The studies leave overall patch quality and the intervention effects of those routines unmeasured. [PAT-0002 verification](../audits/PAT-0002--verification.md) · [PAT-0008 verification](../audits/PAT-0008--verification.md)

## Drive navigation

- [audits/PAT-0002--verification.md](../audits/PAT-0002--verification.md) · [Local copy](../audits/PAT-0002--verification.md)
- [audits/PAT-0008--verification.md](../audits/PAT-0008--verification.md) · [Local copy](../audits/PAT-0008--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0004--verification.md](../audits/SRC-0004--verification.md) · [Local copy](../audits/SRC-0004--verification.md)
- [audits/SRC-0014--verification.md](../audits/SRC-0014--verification.md) · [Local copy](../audits/SRC-0014--verification.md)
- [audits/SRC-0018--verification.md](../audits/SRC-0018--verification.md) · [Local copy](../audits/SRC-0018--verification.md)
- [audits/SRC-0022--verification.md](../audits/SRC-0022--verification.md) · [Local copy](../audits/SRC-0022--verification.md)
- [audits/SRC-0023--verification.md](../audits/SRC-0023--verification.md) · [Local copy](../audits/SRC-0023--verification.md)
- [patterns/PAT-0002--verify-an-unfamiliar-api-call.md](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) · [Local copy](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md)
- [patterns/PAT-0008--take-ownership-before-submitting-ai-code.md](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) · [Local copy](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0004--api-documentation-and-hallucinations.md](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Local copy](../sources/SRC-0004--api-documentation-and-hallucinations.md)
- [sources/SRC-0014--benchmark-shortcuts-and-validation.md](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) · [Local copy](../sources/SRC-0014--benchmark-shortcuts-and-validation.md)
- [sources/SRC-0018--accountability-for-ai-assisted-contributions.md](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Local copy](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md)
- [sources/SRC-0022--observed-developer-agent-misalignment.md](../sources/SRC-0022--observed-developer-agent-misalignment.md) · [Local copy](../sources/SRC-0022--observed-developer-agent-misalignment.md)
- [sources/SRC-0023--trust-and-unchecked-code-acceptance.md](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md) · [Local copy](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md)
