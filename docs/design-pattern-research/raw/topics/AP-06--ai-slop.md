---
topic_id: AP-06
title: "AI slop"
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0018
    relationship: DIRECT
    strength: moderate
    finding: "Moby maintainers report receiving unchecked, poorly scoped or unneeded AI-assisted submissions and describe the validation work this passes to maintainers."
  - id: SRC-0011
    relationship: SUPPORTING
    strength: moderate
    finding: "Recorded work on real issues shows contributors spent time reviewing and cleaning up generated output before handoff."
  - id: SRC-0023
    relationship: SUPPORTING
    strength: moderate
    finding: "Observed coding sessions show unchecked suggestions later edited, removed or left in place within the session."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: low
    finding: "Anthropic describes making an AI-assisted change inspectable with a runnable check, execution evidence and a spec-based diff review."
pattern_ids: [PAT-0008]
---

# AP-06 AI slop

- “The PR description looks finished, but I still have to work out what problem the patch solves.”
- “The contributor pasted the summary and made a few edits. No one can show how the fix was checked.”
- “The change is small. Why does its review include unrelated cleanup and pages of generated explanation?”

The brief asks what happens when a contributor generates a draft, edits it lightly and ships it without adding human value. In shared code, that value is visible in the contributor’s judgment about project need and scope, their verification of the behavior, and their ability to explain and support the change. The evidence includes maintainers’ accounts of unchecked submissions and a separate measure of author verification work. It leaves the prevalence of lightly edited submissions, their defect rate and their incremental cost to reviewers open.

## What the sources establish

Moby’s shared policy describes submissions that arrive without validation, a clear project need or adherence to existing conventions. The maintainers explain that they are left to check whether the work should exist and whether it succeeds. The policy requires review and verification of code and prose before posting, focused diffs, short explanations with supporting material available, and a contributor who can handle follow-up. It also permits language assistance and welcomes useful, verified small contributions. The Compose guide implements stricter approved-issue and testing requirements. The shared policy and Compose guide derive from the same project family, with the central adoption PR pointing to the earlier Compose work. Their report establishes the experience and the project response, with no measured participation, review time or policy effect. SRC-0018:C01–C08. [Dossier](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Baseline, lines 3–53](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L3-L53) · [Rationale, lines 92–115](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L92-L115) · [Central adoption PR](https://github.com/moby/.github/pull/1) · [Compose guide, lines 80–103](https://github.com/docker/compose/blob/0e312c037455427c833aa6101cf349f5afc4621d/CONTRIBUTING.md#L80-L103)

Becker and colleagues’ independent study observes contributor work where checking actually occurred. Review and cleanup took about **9%** of recorded time across 44 analyzed AI-allowed recordings. Acceptance of Cursor generations was below 44% in the 13-developer tool-analytics group. Participants also reported checking, retrying, editing and reverting output. Acceptance measures a tool interaction, and the time measure covers the contributor. Neither measures the quality of accepted code or the reviewer work that unverified submissions would cause. The study therefore documents a substantive human step between generation and handoff. Anthropic’s independently authored guide proposes a runnable check, an execution report and a comparison with the spec and edge cases. It gives a way to document that step. It contains no evaluation of submission quality or reviewer savings. SRC-0011:C03, C07–C10 and SRC-0002:C07, C08, C10. [Developer-time dossier](../sources/SRC-0011--review-work-and-developer-time.md) · [Becker et al., §2.4](https://arxiv.org/pdf/2507.09089v2#page=7) · [§3.2, Fig. 6](https://arxiv.org/pdf/2507.09089v2#page=10) · [§C.1.4](https://arxiv.org/pdf/2507.09089v2#page=20) · [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Runnable check and evidence](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Review against the spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

The separate Trust Dynamics study followed individual suggestions as ten developers used AI in short coding sessions. Of 117 initially accepted suggestions, 42 were later edited or removed. Within that group, the authors report 13 suggestions accepted without evaluation, including eight requiring a change for incorrectness. Four unchecked suggestions stayed in the code at session end. These events distinguish accepting a suggestion into a workspace from deciding what belongs in a submitted change. The study followed sessions, with no evidence about whether the code was ultimately submitted, deployed or reviewed by maintainers. SRC-0023:C01, C03, C05, C09. [Dossier](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md) · [§§VI.A–VI.B(c), Fig. 4](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=8) · [§IX, limitations](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=11)

The sources address different handoffs and supply no comparison of light editing with any defined level of human revision. The maintainer examples place the problem in the contents and evidence a submission gives its reviewer. The developer recordings also show that some assisted workflows already include substantial checking. The amount of rewriting alone could miss both useful, verified drafts and heavily revised changes whose claims are still unsupported.

## Apply the accepted method

[PAT-0008, Take ownership before submitting AI-assisted code](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) applies before a patch is presented as ready for review. Confirm the need and the target project’s rules, inspect the diff for irrelevant changes and changes to assertions, run and read the relevant checks, then explain the observed behavior and the coverage you can substantiate. For a proposed fix whose only evidence is a polished description, obtain a reproduction, locate the change that addresses it and record what actually happened on the candidate. If an expectation changed, cite the decision for it. The reviewer can assess that evidence without guessing how much text or code the assistant wrote. This is a catalog application of the policy and verification advice. Its effect on reviewer workload has not been tested. SRC-0018:C02–C05, C08 and SRC-0002:C07–C10. [Pattern verification](../audits/PAT-0008--verification.md)

## Drive navigation

- [audits/PAT-0008--verification.md](../audits/PAT-0008--verification.md) · [Local copy](../audits/PAT-0008--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0011--verification.md](../audits/SRC-0011--verification.md) · [Local copy](../audits/SRC-0011--verification.md)
- [audits/SRC-0018--verification.md](../audits/SRC-0018--verification.md) · [Local copy](../audits/SRC-0018--verification.md)
- [audits/SRC-0023--verification.md](../audits/SRC-0023--verification.md) · [Local copy](../audits/SRC-0023--verification.md)
- [patterns/PAT-0008--take-ownership-before-submitting-ai-code.md](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) · [Local copy](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0011--review-work-and-developer-time.md](../sources/SRC-0011--review-work-and-developer-time.md) · [Local copy](../sources/SRC-0011--review-work-and-developer-time.md)
- [sources/SRC-0018--accountability-for-ai-assisted-contributions.md](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Local copy](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md)
- [sources/SRC-0023--trust-and-unchecked-code-acceptance.md](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md) · [Local copy](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md)
