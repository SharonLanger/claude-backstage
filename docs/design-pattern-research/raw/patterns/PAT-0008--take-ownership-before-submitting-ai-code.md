---
pattern_id: PAT-0008
status: accepted
name: "Take ownership before submitting AI-assisted code"
type: workflow
families: [code-review, collaboration, verification]
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
topic_ids: [AP-02, AP-06, OB-03, OB-11, OB-12]
symptoms: ["I can paste the agent's summary, but I can't explain this diff", "The suite passes and the expected output changed too", "The maintainer had to tell me which checks to run", "I clicked Accept so I could try the suggestion, then forgot to read it"]
source_ids: [SRC-0018, SRC-0014, SRC-0002, SRC-0011, SRC-0023]
review: PASS
publication_status: published
---

# Take ownership before submitting AI-assisted code

## When users need this

A contributor is about to open a pull request. The assistant says the fix is ready. Can the contributor name the user-visible failure, show what now happens, and explain why a changed test still detects that failure? If the first person able to answer those questions would be the maintainer, there is still author work to do. Another signal is a polished description that claims wider coverage than the contributor can demonstrate.

## Context and prerequisites

Use this at the point of offering a change for review in a shared repository. Have the proposed diff against its actual base, the issue or agreed requirement, the target repository's current contribution instructions, and access to whatever evidence the relevant checks require. Confirm issue-approval rules early enough to avoid investing in an unwanted change. An exploratory question to a maintainer about intended behavior can precede a patch.

## Core principle

Take responsibility for the behavior that the diff will ship. A reviewer should be able to challenge your reasoning, repeat a meaningful check and reach you about a regression.

## How to work this way

1. **Establish the project's need and rules.** Find the issue or decision that authorizes the intended behavior. Read the target repository's contribution guide and any instructions for the affected component. Identify applicable approval, test, disclosure and sign-off requirements. If the policy requires prior issue approval, check that it was actually granted. Other projects can set different rules. [Evidence 1](#evidence-and-provenance)
2. **Read the diff alongside the behavior it promises.** If you clicked Accept to try a suggestion locally, treat the inserted code as provisional. Before keeping it for the submission, explain what each material hunk does and why it belongs. Inspect both the implementation and changes to expected outputs, fixtures and checks. Ask what specific wrong result would still make the check fail. When an expectation legitimately changes, trace the new expectation to the agreed requirement and identify an existing behavior that still deserves protection. Remove unrelated changes. Resolve conflicting requirements with the decision owner. [Evidence 2](#evidence-and-provenance)
3. **Verify the claim the reviewer will read.** Run the applicable project checks in the required environment. For a behavioral fix, exercise the reported case and a relevant case that should still work. Where practical, apply the same reproduction to the base and candidate revisions. Read the result yourself and record the command, observed outcome and meaningful coverage limits. If a required environment or check is unavailable, identify that blocker and follow the project's process before presenting the change as ready. [Evidence 3](#evidence-and-provenance)
4. **Explain the change and own the response.** Write a short opening that states who encounters the problem, what changed, and what evidence supports it. Give the required disclosure and sign-off. Use your own judgment to check any assistant-drafted prose against the diff and the run. Answer review questions, rerun relevant checks after revisions, and take responsibility for investigating reported regressions after merge. [Evidence 4](#evidence-and-provenance)

## Worked example

**Original illustrative scenario.** A catalog exporter omits its CSV header when a filter matches zero rows. A maintainer-approved issue says downstream readers need the column names even for an empty export. In this fictional repository, contributors must run the export tests and disclose AI assistance. The assistant moves the header write outside the row loop and updates the expected empty-export fixture.

The contributor clicks Accept to try the patch locally. Before deciding to keep it, they inspect the old and new fixture. The changed expectation is justified by the issue, but an empty-file check alone cannot show whether the revised exporter also handles populated results. The contributor uses the CSV reader supported by the project to inspect both cases. The following are illustrative expected observations, supplied so a developer can repeat the comparison in an equivalent repository.

| Input | Base revision | Proposed revision | What the reviewer can verify |
|---|---|---|---|
| Filter matches no records | No CSV records | One record containing the column names `id` and `name` | An empty result still exposes the two fields, with no invented data row. |
| Filter matches record 7, named Ada | Header followed by `7,Ada` | Same two records, in the same order | The existing populated case still has exactly one header and one data row. |

After running the required export tests and inspecting those outputs, the contributor can open with “An empty export now emits the same column names as a populated export. Writing the header before iterating over matches also handles zero iterations. I checked zero and one match and ran the export suite. I used an assistant to draft the implementation and fixture change.” If a reviewer asks about a name containing a comma, the contributor inspects whether the field writer changed and runs a matching case before claiming support. If a downstream reader later reports a compatibility problem, the contributor obtains a representative file and investigates the discrepancy.

## Evidence and provenance

| Step | Claim IDs and original locator | What the evidence supports | Our adaptation |
|---|---|---|---|
| 1. Establish need and rules | SRC-0018:C05, SRC-0018:C06, SRC-0018:C08. [Shared policy, lines 55–90](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L55-L90) · [Compose guide, lines 80–103](https://github.com/docker/compose/blob/0e312c037455427c833aa6101cf349f5afc4621d/CONTRIBUTING.md#L80-L103) | Direct policy evidence. The shared policy requires prior project approval for a previously unreported problem. Compose requires a linked approved issue for every AI-assisted PR and specifies tests and environment access. | Consult the target's actual rules before submitting elsewhere. Neither policy establishes a universal issue gate. |
| 2. Inspect the behavior and the meaning of its checks | SRC-0018:C02, SRC-0018:C03. [Shared policy, lines 18–44](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L18-L44). SRC-0002:C10. [Anthropic, “Review against your spec,” review prompt](https://code.claude.com/docs/en/best-practices#review-against-your-spec). SRC-0014:C01. [METR, “What we’ve observed,” Rust contest and kernel cases](https://metr.org/blog/2025-06-05-recent-reward-hacking/) | The policy calls for human verification and focused changes. The guide recommends inspecting the diff against requirements and edge cases. The benchmark cases show that a favorable evaluation result can diverge from task success under selected autonomous conditions. | Ask what wrong result a changed expectation can still detect. Checking the expectation against an independently agreed requirement is our procedure. The benchmark did not evaluate this procedure in repositories. |
| 2. Evaluate a suggestion before relying on it | SRC-0023:C01, SRC-0023:C03, SRC-0023:C05, SRC-0023:C08, SRC-0023:C09. [Sabouri et al., §§VI.A–B(c), Fig. 4, pp. 7–8](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=8) · [§VII, guidelines G3–G4, pp. 9–10](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=9) · [§IX, p. 11](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=11) | The researchers observed acceptance without prior evaluation. Their guidance recommends assessing suggestions before acceptance and looking for unintended changes. | When a tool requires inserting code to exercise it, distinguish that trial from the decision to retain the code for submission. Applying this distinction to a complete diff is our adaptation. |
| 3. Run and interpret the checks | SRC-0018:C08. [Compose guide, lines 80–103](https://github.com/docker/compose/blob/0e312c037455427c833aa6101cf349f5afc4621d/CONTRIBUTING.md#L80-L103). SRC-0002:C07, SRC-0002:C08. [Anthropic, “Give Claude a check to run,” examples and evidence request](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) | Compose spells out contributor duties for its environment. Anthropic recommends observable checks and recording execution evidence. Both are guidance. | The base/candidate comparison and neighboring case are ways to make a behavioral claim inspectable. A passing pair covers those inputs only. |
| 4. Explain, disclose and follow up | SRC-0018:C01, SRC-0018:C02, SRC-0018:C03, SRC-0018:C04. [Shared policy, lines 3–53](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L3-L53). SRC-0011:C03, SRC-0011:C08. [Becker et al., §2.3, p. 6](https://arxiv.org/pdf/2507.09089v2#page=6) · [Appendix C.1.4, p. 20](https://arxiv.org/pdf/2507.09089v2#page=20) | Direct policy support for disclosure, sign-off, review of posted text, concise summaries and contributor follow-up. In the separate developer study, the authors' time measure included work after review. Review and cleanup of AI output occupied about 9% of time in 44 analyzed AI-allowed recordings. | Put the observed behavior and checks in the opening, and revisit them when review changes the patch. The study provides context for budgeting contributor time. It did not test this handoff or measure maintainers' time saved. |

## Different source perspectives

Sabouri and colleagues observed ten developers using tools of their choice on their own projects. Across 142 suggestions, they recorded 117 initial acceptances and 25 rejections, including ignored suggestions. Of the 117 initially accepted, 75 remained unchanged at session end and 42 were edited or removed. The researchers separately identified 13 suggestions accepted without prior evaluation that were later edited or removed, including eight that needed changes for incorrectness. Four unchecked suggestions stayed. A click establishes an initial choice. The researchers needed observations around that choice to tell whether the developer had evaluated the code, and later observations to tell whether it stayed. The study ended with the sessions. It gives no estimate of unchecked code reaching production or of the effect of a PR policy. [SRC-0023:C01, C03, C05, C09, §§III.B, VI.A–B(c), Fig. 4 and §IX](https://cdn.amazon.science/99/78/f02aeaa049b4ba514d7f2790ade7/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications.pdf#page=8)

The Moby/Docker maintainers describe unchecked submissions and the verification work these leave to volunteers. Their shared policy and the Compose guide have a common development history. They establish expectations in participating projects and provide a maintainer account of the problem. Anthropic's product guide offers practitioner advice on obtaining evidence. METR's benchmark report and the developer-time paper are separate investigations with organizational and author overlap. The former supplies examples from autonomous evaluations. The latter observes contributor activity in experienced developers' real repositories. These sources address different questions. None compares this pre-submission routine against ordinary review or measures a reduction in review fatigue. [Maintainers' rationale, lines 92–115](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L92-L115) · [Developer study, §3.2 and Fig. 6](https://arxiv.org/pdf/2507.09089v2#page=10)

## Tradeoffs, variations and when to skip it

For a one-line documentation correction, inspect the rendered instruction or exercise the documented command when relevant. Match the explanation to the scope of the change. For an intentional behavior change, retain the decision that explains the revised assertion and include an unaffected case. For an early design discussion without a candidate diff, describe the open question and ask for the needed decision. The submission routine becomes useful once a change is ready to inspect. A human sign-off or review marker alone gives the next reader little information about which behavior was checked.

## Related patterns and topics

AP-06 covers forwarding lightly edited output that still imposes validation work on a maintainer. AP-02 covers submitting code the contributor cannot explain. OB-03 concerns checking apparent success against task intent. OB-11 supplies the review-work context, with limited evidence on fatigue itself. When the diff is too large to understand in one review, [PAT-0003, Slice a change for review](PAT-0003--slice-a-change-for-review.md) addresses how to divide the work earlier. When a reviewer has already identified a missed condition, [PAT-0005, Turn review feedback into a check](PAT-0005--turn-review-feedback-into-a-check.md) addresses the subsequent revision.

## Sources and verification

- Moby and Docker open source projects, *AI Usage Policy*, merged September 29, 2026. [Dossier](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Original](https://github.com/moby/.github/blob/main/AI_POLICY.md) · [Source audit](../audits/SRC-0018--verification.md)
- Sydney Von Arx, Lawrence Chan and Beth Barnes, *Recent Frontier Models Are Reward Hacking*, METR, June 5, 2025. [Dossier](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) · [Original](https://metr.org/blog/2025-06-05-recent-reward-hacking/) · [Source audit](../audits/SRC-0014--verification.md)
- Anthropic, *Best practices for Claude Code*, living documentation accessed November 21, 2026. [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Original](https://code.claude.com/docs/en/best-practices) · [Source audit](../audits/SRC-0002--verification.md)
- Sadra Sabouri and colleagues, *Trust Dynamics in AI-Assisted Development: Definitions, Factors, and Implications*, ICSE 2025. [Dossier](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md) · [Original](https://www.amazon.science/publications/trust-dynamics-in-ai-assisted-development-definitions-factors-and-implications) · [Source audit](../audits/SRC-0023--verification.md)
- Joel Becker, Nate Rush, Beth Barnes and David Rein, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, arXiv v2. [Dossier](../sources/SRC-0011--review-work-and-developer-time.md) · [Original](https://arxiv.org/html/2507.09089v2) · [Source audit](../audits/SRC-0011--verification.md)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/PAT-0008--verification.md)

## Drive navigation

- [audits/PAT-0008--verification.md](../audits/PAT-0008--verification.md) · [Local copy](../audits/PAT-0008--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0011--verification.md](../audits/SRC-0011--verification.md) · [Local copy](../audits/SRC-0011--verification.md)
- [audits/SRC-0014--verification.md](../audits/SRC-0014--verification.md) · [Local copy](../audits/SRC-0014--verification.md)
- [audits/SRC-0018--verification.md](../audits/SRC-0018--verification.md) · [Local copy](../audits/SRC-0018--verification.md)
- [audits/SRC-0023--verification.md](../audits/SRC-0023--verification.md) · [Local copy](../audits/SRC-0023--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0011--review-work-and-developer-time.md](../sources/SRC-0011--review-work-and-developer-time.md) · [Local copy](../sources/SRC-0011--review-work-and-developer-time.md)
- [sources/SRC-0014--benchmark-shortcuts-and-validation.md](../sources/SRC-0014--benchmark-shortcuts-and-validation.md) · [Local copy](../sources/SRC-0014--benchmark-shortcuts-and-validation.md)
- [sources/SRC-0018--accountability-for-ai-assisted-contributions.md](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md) · [Local copy](../sources/SRC-0018--accountability-for-ai-assisted-contributions.md)
- [sources/SRC-0023--trust-and-unchecked-code-acceptance.md](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md) · [Local copy](../sources/SRC-0023--trust-and-unchecked-code-acceptance.md)
- [topics/AP-02--flying-blind-vibe-coding.md](../topics/AP-02--flying-blind-vibe-coding.md) · [Local copy](../topics/AP-02--flying-blind-vibe-coding.md)
- [topics/AP-06--ai-slop.md](../topics/AP-06--ai-slop.md) · [Local copy](../topics/AP-06--ai-slop.md)
- [topics/OB-03--obedient-contractor.md](../topics/OB-03--obedient-contractor.md) · [Local copy](../topics/OB-03--obedient-contractor.md)
- [topics/OB-11--keeping-up-review-fatigue.md](../topics/OB-11--keeping-up-review-fatigue.md) · [Local copy](../topics/OB-11--keeping-up-review-fatigue.md)
- [topics/OB-12--excess-verbosity.md](../topics/OB-12--excess-verbosity.md) · [Local copy](../topics/OB-12--excess-verbosity.md)
