---
source_id: SRC-0018
status: accepted
original_title: "AI Usage Policy"
authors: ["Guillaume Lours (introducing commit and pull request author)"]
publisher: "Moby and Docker open source projects (moby/.github)"
source_type: docs
published: 2026-09-29
updated: unknown
accessed: 2026-11-21
original_url: "https://github.com/moby/.github/blob/main/AI_POLICY.md"
source_version: "512ca97347590b4ecaf892adaf780797b1e637b9 (published main-branch merge, matching main at access)"
full_text_reuse: authorized
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [AP-02, AP-06, BP-05, OB-03, OB-11, OB-12]
related_patterns: [PAT-0008]
review: PASS
publication_status: published
---

# AI Usage Policy

## Provenance and scope read

Guillaume Lours introduced the document in commit `0f9a4d1` on September 17, 2026. During review, commit `869d86f` moved instructions for repositories adopting the policy into the shared README. The September 29 merge of pull request #1 is the publication date used here. The merged file and the file retrieved from `main` on November 21 had identical content and blob ID `73b318169ec55c57302ef616b080727b2fea9258`. GitHub showed a subsequent formatting proposal, PR #2, as open and unmerged. The ledger cites the immutable September 29 revision. [Introducing commit](https://github.com/moby/.github/commit/0f9a4d16a6cd7a8161f0adc067b23eadc2ed8acc) · [README change](https://github.com/moby/.github/commit/869d86f3c5e1263abd197caa0f14cdc7b9c109cc) · [Merged PR #1](https://github.com/moby/.github/pull/1) · [Pinned policy](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md) · [Open PR #2](https://github.com/moby/.github/pull/2)

The reading covered all 115 lines, the adoption README, the introducing PR and its review history, and the relevant sections of the Moby and Docker Compose contribution guides. The central document is first-party governance evidence about how these projects want submissions prepared and moderated. The people setting the rules describe their own workload and interests. The adopting guides establish what their respective repositories say they require. This reading did not examine a sample of enforcement decisions, submissions or review outcomes. [Shared README, lines 6–17](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/README.md#L6-L17) · [Moby adoption](https://github.com/moby/moby/blob/28adcd247b5d2ce1ce61064875264fadb4bd7d63/CONTRIBUTING.md#L350-L353) · [Compose adoption](https://github.com/docker/compose/blob/0e312c037455427c833aa6101cf349f5afc4621d/CONTRIBUTING.md#L80-L103)

## Reader's orientation

The policy makes the contributor responsible for a submission that a maintainer can assess. Posting a PR, issue or response means taking responsibility for the AI-assisted content under one’s name. The source treats disclosure, author verification, a focused contribution and follow-through as distinct parts of that responsibility. AI help remains welcome, including for drafting a response across a language barrier. The maintainers describe unverified, convention-breaking and unnecessary submissions as consuming volunteer review time. They supply no count of those submissions or estimate of what the policy changes. [Policy, lines 3–22](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L3-L22) · [Policy rationale, lines 92–115](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L92-L115)

## Detailed analytical reading

### What the contributor owns before sharing work

The policy calls for a human to read, edit, understand and check the material before it goes out. The rule applies to the prose around the change too. For a review reply drafted by AI, that means the writer owns factual claims about what the patch does, even if the text is fluent or AI assistance was mainly linguistic. For code, the person opening the PR signs off and stays responsible. Where AI was used, the submitter names the tools and describes their rough contribution in the issue or PR description. The policy warns of closure when a maintainer suspects undisclosed assistance. AI tools are excluded from commit `Co-Authored-By:` trailers, which are reserved for people who contributed. Disclosure makes the assistance visible and the review obligation remains. [Policy, lines 7–22](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L7-L22)

### How the submission uses a reviewer’s time

A short plain-language opening should tell the reader what problem to assess or what change is proposed. The policy demonstrates folding useful detail into a Markdown `<details>` block, so logs or prior attempts can remain available after the actionable summary. The code equivalent is to keep the diff tied to the issue. Incidental formatting, typo corrections or refactors can have their own submission if there is a reason to do them. The maintainers argue that smaller diffs reduce review effort and risk. The policy offers no comparative data for either benefit. After opening a PR, the contributor is expected to answer questions and help if a regression appears, including after merge. [Policy, lines 24–49](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L24-L49)

### When a repository expects issue approval

The shared rules prohibit contribution farming. Examples include skipping problem verification or solution testing, splitting one logical change into trivial pieces without a reason, sending changes with no concrete benefit, and submitting an AI-assisted PR for a previously unreported problem without first filing an issue, giving maintainers a chance to validate the need and obtaining their approval. A small first contribution is welcome when it meets a verified need. Maintainers may close submissions that violate the policy and sanction repeat offenders. [Policy, lines 51–78](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L51-L78)

Repositories can impose a broader approval rule for AI-assisted PRs and specify how approval is recorded. The common document points contributors to repository-level guides and gives maintainers discretion over their own AI use. Moby adopted the baseline by linking to it in its contribution guide. The guide visible at access additionally asks for a `Created with: <AGENT NAME>` note on AI-assisted PRs. Compose adopted a synced copy and sets a stricter rule for all its AI-assisted PRs. Compose requires a linked issue labeled `status/approved`, named checks and relevant end-to-end tests, the ability to test the affected platform or environment, adherence to existing code patterns, and the ability to explain every line. Its guide says to remove an agent-generated review marker if present after the contributor has reviewed the change, and describes an automated check that blocks merge while the marker exists. The marker check can detect a file’s presence. A reviewer still needs evidence that the substantive review happened. [Shared policy, lines 80–90](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L80-L90) · [Moby guide at access](https://github.com/moby/moby/blob/master/CONTRIBUTING.md#ai-usage-policy) · [Compose guide, pinned adoption revision, lines 80–103](https://github.com/docker/compose/blob/0e312c037455427c833aa6101cf349f5afc4621d/CONTRIBUTING.md#L80-L103) · [Compose workflow introduction](https://github.com/docker/compose/commit/a53594adb2a7de94a7fca861adb786e6ac1396ba)

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support and caveat |
|---|---|---|---|---|
| SRC-0018:C01 | The shared policy covers AI-assisted issues, PRs and discussion. Contributors disclose the tools and approximate extent of assistance in issue or PR descriptions. PR openers sign off and own the change, and AI tools are excluded from commit co-author trailers. | Shared baseline requirements | [Policy, lines 3–16](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L3-L16) | Direct. The baseline gives no formula for quantifying assistance and warns of closure for suspected nondisclosure. |
| SRC-0018:C02 | A human must review and edit AI-assisted code or prose before posting and understand and verify it. AI-assisted reply drafting, including language help, is allowed. | Shared baseline requirements | [Policy, lines 18–22](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L18-L22) | Direct. The review obligation applies to issues, PR descriptions, review replies and code changes. |
| SRC-0018:C03 | A submission should start with a short explanation and make extended supporting material available in a collapsible section. The diff should address the intended change without unrelated cleanup. | Shared submission guidance | [Policy, lines 24–44](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L24-L44) | Direct for the advice. Faster review and lower risk are the maintainers’ rationale. |
| SRC-0018:C04 | Contributors are expected to help with follow-up questions and regressions. Maintainers may close submissions that violate the policy and restrict or ban repeat offenders. | Ownership expectation and enforcement policy | [Policy, lines 46–53](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L46-L53) · [Lines 73–78](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L73-L78) | Direct. Enforcement frequency is unknown. |
| SRC-0018:C05 | The anti-farming rule covers unverified or untested submissions and AI-assisted PRs for previously unreported problems submitted before maintainers verify and approve the need, along with trivial fragmentation and changes lacking a concrete benefit. | Shared rule and examples | [Policy, “No contribution farming,” lines 55–78](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L55-L78) | Direct. A verified, useful small fix or a first-time contribution can be welcome. |
| SRC-0018:C06 | Repositories may impose a maintainer-approved issue requirement and choose local labels and procedures. The outside-contribution rules give maintainers room for judgment in their own AI use. | Scope and delegation | [Policy, “Approved issues for AI-assisted PRs,” lines 80–90](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L80-L90) · [README, lines 6–17](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/README.md#L6-L17) | Direct. `status/approved` is an example at the shared level. |
| SRC-0018:C07 | Maintainers say they are seeing unchecked AI output, submissions that do not follow project conventions and submissions without a real project need. They frame those submissions as passing validation work to volunteer maintainers. | Maintainer observations and rationale | [Policy, lines 92–115](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L92-L115) | Direct as a report of maintainer experience. No counts, comparison, causal attribution or intervention evaluation. |
| SRC-0018:C08 | Compose operationalizes its stricter rule with an approved-issue label, test and platform requirements, contributor ability to explain the change, and a review marker that the contributor clears after review. | Repository-specific adoption evidence | [Compose guide, “AI-assisted contributions,” lines 80–103](https://github.com/docker/compose/blob/0e312c037455427c833aa6101cf349f5afc4621d/CONTRIBUTING.md#L80-L103) | Direct for what Compose requires. The marker records a step and cannot attest to the quality of review. |

## Extractable practitioner insights

### Add verifiable information before asking someone else to review

For AP-06, the source motivates checking whether the submission contributes an understandable problem, a scoped change and useful evidence. A catalog adaptation is to prepare a short account of the observed behavior and expected behavior, then keep test output or logs available below it. A practical symptom is a polished PR description whose author cannot point to a reproduction or name the change that fixes it. In that case a rewrite alone leaves the central question unanswered. Claims SRC-0018:C02–C05 and C07. [Policy, lines 18–49](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L18-L49) · [Anti-farming examples, lines 55–78](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L55-L78)

### Rehearse explaining and checking the changed behavior

For AP-02, the policy supports understanding and checking a change before presenting it, and the Compose guide makes the expectation concrete. In an illustrative adaptation, a contributor gets an AI draft for a reported bug where a Compose command prints the wrong service name in an error. They check whether the issue has the local approval label, reproduce the wrong name, examine why the old code selected it, remove unrelated cleanup, run the project’s checks and verify the specific scenario with the patch. The contributor can then explain how the patch selects the correct name, disclose where AI helped and respond to review. If the failure is platform-specific and the contributor lacks a suitable environment, the verification constraint applies even when the draft looks plausible. The scenario and the suggested sequence are catalog adaptations. Claims SRC-0018:C01–C03, C05–C06 and C08. [Shared review requirement, lines 7–22](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/AI_POLICY.md#L7-L22) · [Compose checks, lines 86–100](https://github.com/docker/compose/blob/0e312c037455427c833aa6101cf349f5afc4621d/CONTRIBUTING.md#L86-L100)

## Related work, conflicts, and limitations

The shared policy directly supports AP-06 and AP-02 as conduct concerns in open-source project submissions. Applying the practices to a private team or personal prototype requires judgment about handoff and consequences. The shared and Compose texts establish rules. Whether those rules change contributor behavior, submissions admitted, maintainer hours or production defects remains open. The Compose guide is an implementation from the same project family. Moby’s PR explicitly traces the central document back to Compose PR #13550, so the central and local documents are related evidence. [Central PR #1](https://github.com/moby/.github/pull/1) · [Compose antecedent, PR #13550](https://github.com/docker/compose/pull/13550)

The METR developer study observes developer review and cleanup in a limited recording subset, and its post-PR-review timing measures time spent by the submitter. It offers independent context for the work of verification. Its results cannot estimate the consequences of a project adopting disclosure, approval labels or a review marker. A separate METR report shows benchmark cases where superficially passing evaluations credited work that failed to meet the intended task. Those cases motivate checking what a test establishes, with a different setting and no measurement of contribution quality. [SRC-0011, claims C03 and C08–C10](SRC-0011--review-work-and-developer-time.md#claim-level-evidence-ledger) · [SRC-0014, claims C01 and C03–C05](SRC-0014--benchmark-shortcuts-and-validation.md#claim-level-evidence-ledger)

## Retrieval hints

- “I have an AI-written fix, but I can’t explain why it works.”
- “The PR description looks convincing, but I haven’t reproduced the bug.”
- “Where do I disclose the coding agent’s contribution?”
- “An AI change is mixed with formatting and unrelated cleanup.”
- “Do I need maintainer approval before I submit this AI-assisted PR?”
- Search terms include human review before posting, contributor responsibility, contribution farming, project approval, AI disclosure, scope discipline and post-merge follow-through.

## Original article access and copyright/permission record

The public GitHub main-branch policy and pinned revision were readable on November 21, 2026. The shared repository carries Apache License 2.0 at the pinned revision. Redistribution of covered repository material is subject to its terms, including section 4. The dossier reproduces no policy passages in full and uses original analysis, section references and exact identifiers. [Canonical policy](https://github.com/moby/.github/blob/main/AI_POLICY.md) · [Pinned repository license](https://github.com/moby/.github/blob/512ca97347590b4ecaf892adaf780797b1e637b9/LICENSE)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0018--verification.md)

## Drive navigation

- [audits/PAT-0008--verification.md](../audits/PAT-0008--verification.md) · [Local copy](../audits/PAT-0008--verification.md)
- [audits/SRC-0018--verification.md](../audits/SRC-0018--verification.md) · [Local copy](../audits/SRC-0018--verification.md)
- [patterns/PAT-0008--take-ownership-before-submitting-ai-code.md](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) · [Local copy](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/AP-02--flying-blind-vibe-coding.md](../topics/AP-02--flying-blind-vibe-coding.md) · [Local copy](../topics/AP-02--flying-blind-vibe-coding.md)
- [topics/AP-06--ai-slop.md](../topics/AP-06--ai-slop.md) · [Local copy](../topics/AP-06--ai-slop.md)
- [topics/BP-05--slice-for-review.md](../topics/BP-05--slice-for-review.md) · [Local copy](../topics/BP-05--slice-for-review.md)
- [topics/OB-03--obedient-contractor.md](../topics/OB-03--obedient-contractor.md) · [Local copy](../topics/OB-03--obedient-contractor.md)
- [topics/OB-11--keeping-up-review-fatigue.md](../topics/OB-11--keeping-up-review-fatigue.md) · [Local copy](../topics/OB-11--keeping-up-review-fatigue.md)
- [topics/OB-12--excess-verbosity.md](../topics/OB-12--excess-verbosity.md) · [Local copy](../topics/OB-12--excess-verbosity.md)
