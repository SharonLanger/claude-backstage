---
source_id: SRC-0002
status: accepted
original_title: "Best practices for Claude Code"
authors: []
publisher: "Anthropic (Claude Code Docs)"
source_type: docs
published: unknown
updated: unknown
accessed: 2026-11-21
original_url: "https://code.claude.com/docs/en/best-practices"
source_version: unknown
full_text_reuse: not_authorized_or_unverified
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [AP-01, AP-02, AP-03, AP-06, AP-08, AP-09, BP-01, BP-02, BP-03, BP-04, BP-05, BP-06, BP-09, BP-10, OB-01, OB-03, OB-04, OB-07, OB-09, OB-10, OB-12]
related_patterns: [PAT-0001, PAT-0002, PAT-0003, PAT-0004, PAT-0005, PAT-0006, PAT-0007, PAT-0008]
review: PASS
---

# Best practices for Claude Code

## Provenance and scope read

- Anthropic publishes this living guide in Claude Code Docs. No individual byline, visible publication date, revision date, or page version was identified. The former Anthropic documentation address redirected to the current publisher page. [Canonical HTML](https://code.claude.com/docs/en/best-practices) · [Legacy URL](https://docs.anthropic.com/en/docs/claude-code/best-practices)
- Accessed 2026-11-21. The complete article body was accessible publicly, including the opening diagnostics, instructions and project knowledge, checks and review, permissions, default changes, session steering, unattended work, and the table of superseded advice. The publisher’s Markdown representation corroborated the relevant sections. Linked references were outside the reading scope. The examples and product behavior were read as documentation and were not executed. [Article](https://code.claude.com/docs/en/best-practices) · [Publisher Markdown](https://code.claude.com/docs/en/best-practices.md)
- As product documentation from the vendor, the guide is primary evidence of what Anthropic advises and how it describes Claude Code behavior. Its efficacy assertions are practitioner judgments. The page presents no study sample, comparison group, error rate, or independent evaluation.

## Reader's orientation

Three different symptoms can look alike from the user’s seat. An agent can use an incomplete picture of the task, continue with history that gives the wrong instruction prominence, or end after producing a plausible patch with weak evidence. A larger prompt has no single effect across these cases. A written acceptance criterion can fill an information gap. A fresh session can remove obsolete discussion. A focused check can expose a failure that a well-oriented session would still miss. This is the analytical distinction used below. Anthropic supplies product-specific methods for each, with no measured comparison between workflows. [Scope of the guide](https://code.claude.com/docs/en/best-practices)

## Detailed analytical reading (original words)

### Reset, compact, and rewind address different kinds of history

In the current page, an automatically compacted conversation and a large advertised context window are ordinary features of supported models. Anthropic still recommends a boundary between unrelated tasks. Every new turn inherits the conversation, and unused history still has a cost that depends on caching. For a long task that remains coherent, the guide offers focused compaction, with an example that names API changes and test commands to retain. Compaction performs a summarization pass over the old conversation. The distinction matters for a requirement whose exact wording controls implementation. A summary can orient the next turn, while a durable requirement in a file can be opened and checked verbatim. [Keep cost and context down](https://code.claude.com/docs/en/best-practices#keep-cost-and-context-down)

The steering section starts from visible drift. Interrupting retains work completed so far, rewinding can change the conversation, the working files, or both, and clearing starts a new conversation. Reading these controls together suggests two decisions for a practitioner: whether the chat’s assumptions are worth carrying forward, and whether the existing edits are worth carrying forward. Those decisions can differ. A useful partial correction may survive a session reset. A mistaken edit may warrant a file rollback even when the original task brief remains sound. The guide expressly limits the built-in checkpoints to tracked edits made with Claude’s own file tools in the main conversation. A shell-only edit can survive a restore. [Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session)

Anthropic uses two failed corrections as the trigger in its restart heuristic. The heuristic responds to repetition of the same mistake, so it has limited bearing on a series of tests uncovering distinct issues. The guide also explicitly revisits its older framing of the context window as the main bottleneck. A fixed percentage threshold or a universal restart interval cannot be inferred from this page. [Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session) · [What you can stop doing](https://code.claude.com/docs/en/best-practices#what-you-can-stop-doing)

### A written spec bridges the conversation boundary and the review boundary

The guide’s rate-limiter example begins with unresolved design choices such as who shares a limit and what happens after it is exceeded. It puts question-asking before implementation, saves the answers in `SPEC.md`, and directs a new session to build from that file. The same file becomes the reference for review. The useful handoff is a set of decisions relevant to observable behavior. In a different task, a team could write down how imported rows with duplicate IDs are handled and whether failure discards all rows or only the invalid ones. A later conversation can test such statements even when it never sees the discussion that produced them. The import scenario is an analyst example. [Brainstorm with Claude first](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first) · [Review against your spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

Persistent repository guidance is another place to put durable knowledge, with a different audience. Anthropic distinguishes always-loaded material from path-scoped rules and procedures loaded as skills. Consider a repository where a deprecated helper still appears in many files. A short note can prevent the existing examples from silently teaching the wrong default in work that touches that helper. A procedure that applies in one directory can instead be scoped to that directory, reducing the chance it intrudes on unrelated tasks. This is a relevance judgment about what the agent can reliably discover from the repository. The guide gives no evaluation of competing instruction-file lengths. [Keep CLAUDE.md short](https://code.claude.com/docs/en/best-practices#keep-claudemd-short) · [Scope rules to one part of the codebase](https://code.claude.com/docs/en/best-practices#scope-rules-to-one-part-of-the-codebase) · [Put team procedures in skills](https://code.claude.com/docs/en/best-practices#put-team-procedures-in-skills)

### A runnable check and a fresh review detect different failures

A check gives the implementation session an observable result. A test or compiler can give a repeatable outcome. A screenshot comparison can expose visible defects, with interpretation still involved. The guide asks the agent to return evidence of the run. The evidence can tell a reader which command actually ran and which behavior the output supports. A narrowly green test leaves uncertainty about behaviors it never exercised. That uncertainty matters when the same agent also chose or edited the test. The last two observations are analyst inference from the verification loop. [Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run)

The fresh reviewer in the guide sees the change without inheriting the implementation conversation. In the spec-directed variant, it checks requirements, edge-case tests, and correctness gaps. The source also presents a reviewer with read-only tools and a separate-session option where a person carries findings back. With a compact diff and a clear spec, the second session can notice a missing obligation without first hearing the author’s explanation for the implementation. When the spec itself omits a requirement, the second reader can reproduce the same blind spot. The guide also notes the cost of having a fresh agent gather context already collected in the original session. [Review against your spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec) · [Know what subagents cost](https://code.claude.com/docs/en/best-practices#know-what-subagents-cost) · [Run sessions in parallel](https://code.claude.com/docs/en/best-practices#run-sessions-in-parallel)

### Match the strength of enforcement to the consequence

Anthropic distinguishes model judgment from controls in the application that applies permissions and runs configured hooks. This difference is easy to miss when a prompt, a goal, and a hook all express a similar completion criterion. The goal feature asks a separate model to evaluate progress. A command-based `Stop` hook uses the command’s result and can feed back an error, subject to a limit on repeated blocks under the described conditions. Either can detect some premature stops. A system that needs an independent barrier to publishing a broken result still has to place that barrier at a relevant action, such as merge approval. A tool-level denial similarly depends on what the rule actually matches. Anthropic describes the sandbox as a separate layer for shell access and notes that strict mode disables requesting an out-of-sandbox retry. [Deterministic and non-deterministic instructions](https://code.claude.com/docs/en/best-practices#deterministic-and-non-deterministic-instructions) · [Enforce the check with a Stop hook](https://code.claude.com/docs/en/best-practices#enforce-the-check-with-a-stop-hook) · [Limit access with permission rules and the sandbox](https://code.claude.com/docs/en/best-practices#limit-access-with-permission-rules-and-the-sandbox)

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support / caveat |
|---|---|---|---|---|
| SRC-0002:C01 | Use `/clear` between unrelated tasks. | Practitioner advice | [Keep cost and context down](https://code.claude.com/docs/en/best-practices#keep-cost-and-context-down), `/clear` bullet | Direct. Applies to continuity of conversation, with no claim about restoring files. |
| SRC-0002:C02 | Use focused `/compact` for a continuing task. | Practitioner advice | [Keep cost and context down](https://code.claude.com/docs/en/best-practices#keep-cost-and-context-down), `/compact` bullet | Direct. Focus is an instruction to the summarizer. Exact retention and savings are unmeasured. |
| SRC-0002:C03 | After two unsuccessful corrections of the same mistake, clear and restate the task. | Practitioner advice | [Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session), `/clear` bullet | Direct. A vendor heuristic without a measured optimum. |
| SRC-0002:C04 | Rewind can restore conversation, tracked code, or both. | Documented product behavior | [Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session), `/rewind` bullet and checkpoint warning | Direct. Edits made solely through a Bash command fall outside the described checkpoint. |
| SRC-0002:C05 | Elicit a spec through questions, then implement it in a fresh session. | Practitioner advice | [Brainstorm with Claude first](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first), rate-limiter example | Direct. Illustrated guidance for a task with unresolved decisions. |
| SRC-0002:C06 | Specify location, symptom, and success criteria for a fix. | Practitioner advice | [Write a specific prompt](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt), login example | Direct. Open-ended prompts are also allowed for exploration. |
| SRC-0002:C07 | Supply a runnable check with an interpretable result. | Practitioner advice | [Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run), opening and examples | Direct. The check can only observe what it exercises. |
| SRC-0002:C08 | Request the command and output, or visual evidence. | Practitioner advice | [Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run), paragraph after the review option | Direct. A report provides an audit trail and may need corroboration. |
| SRC-0002:C09 | `/code-review` uses a subagent without the implementation transcript. | Documented product behavior | [Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run), `/code-review` bullet | Direct for this product feature. An independent context alone does not establish independent judgment or accuracy. |
| SRC-0002:C10 | Ask a reviewer to compare the diff with spec requirements and edge-case tests, prioritizing correctness. | Practitioner advice | [Review against your spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec), review prompt and note on style | Direct. A targeted spec review gives limited coverage outside the stated scope. |
| SRC-0002:C11 | A command-based Stop hook can block completion on a failing check. | Documented product behavior | [Enforce the check with a Stop hook](https://code.claude.com/docs/en/best-practices#enforce-the-check-with-a-stop-hook), typecheck and block-cap example | Direct. The illustrated hook returns exit code 2 on failure. The documented cap can override repeated consecutive blocks when no tool call intervenes. |
| SRC-0002:C12 | Put inflexible rules in controls enforced by the application. | Practitioner advice | [Deterministic and non-deterministic instructions](https://code.claude.com/docs/en/best-practices#deterministic-and-non-deterministic-instructions), comparison table and examples | Direct. Covers hooks, deny rules, and managed settings. Scope and possible alternate tool paths matter. |
| SRC-0002:C13 | Keep always-loaded repository guidance short and focused on missing or misleading knowledge. | Practitioner advice | [Keep CLAUDE.md short](https://code.claude.com/docs/en/best-practices#keep-claudemd-short), opening and sample file | Direct. The examples include test commands and legacy code that should not be copied. |
| SRC-0002:C14 | Load path-specific rules and team procedures when applicable. | Practitioner advice | [Scope rules to one part of the codebase](https://code.claude.com/docs/en/best-practices#scope-rules-to-one-part-of-the-codebase) and [Put team procedures in skills](https://code.claude.com/docs/en/best-practices#put-team-procedures-in-skills) | Direct. An eligible skill can expose its description initially, with the full file loaded when invoked. |
| SRC-0002:C15 | Subagents can isolate noisy work or review independently, at additional usage and possible time cost. | Practitioner advice | [Know what subagents cost](https://code.claude.com/docs/en/best-practices#know-what-subagents-cost), benefits, costs and read-only reviewer | Direct. Relevance of the cost depends on context a new agent must reconstruct. |
| SRC-0002:C16 | Unattended work needs completion criteria, verification, limits on access and spend or turns, and human sign-off. | Practitioner advice | [Let Claude run without you](https://code.claude.com/docs/en/best-practices#let-claude-run-without-you), five readiness questions | Direct. The scope is unattended work in Claude Code. |
| SRC-0002:C17 | The current guide drops aggressive context-window management as a default while still recommending `/clear` at task boundaries. | Practitioner advice | [What you can stop doing](https://code.claude.com/docs/en/best-practices#what-you-can-stop-doing), first table row | Direct. Rationale is large windows on most current models and automatic compaction. The source does not quantify quality by window utilization. |

## Extractable practitioner insights

### Carry decisions across a boundary

When a thread repeatedly rebuilds the wrong thing, record the task’s confirmed scope and success condition before starting anew. If existing changes may be useful, inspect them independently of the reset decision. When the current thread still holds useful continuity, summarize with an explicit focus and treat the durable spec as the reference when wording matters. This synthesis combines C01–C06 and C17. Direct topic relevance is BP-01 and BP-06. The restart part supports AP-01 and part of BP-03. The article gives no rule that regeneration generally beats patching.

### Ask two questions of a finished patch

Ask which check actually ran and what its result covers. Where success depends on several distinct requirements, give a fresh reviewer the spec, the relevant changes, and a request for missing behavior or missing test cases. The proposed two-question workflow combines C07–C10 and C15. It supports AP-02 and gives a practical way to surface AP-09. A review grounded in the same spec can still miss a shared mistaken assumption. BP-02 has direct support for an interview-led specification conversation, independent of review. [Brainstorm with Claude first](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first)

### Give recurring rules an appropriate home

If the agent keeps rediscovering a misleading repo convention, write down the missing decision near the work it affects. If a boundary must hold every time, identify the operation at which it can actually be enforced. These are adaptations of C11–C14 and support AP-08 and part of BP-09. The article supports short project guidance about misleading conventions and hard controls for genuine invariants. It has no evaluation of decision records or a particular marker syntax for protecting counterintuitive code.

## Related work, conflicts, and limitations

- OB-01 and OB-10 have contextual support through the guide’s discussion of mixed history, focused conversation, compaction, and instruction scope. The source does not reproduce an instruction-decay experiment, isolate position effects, or validate a focus/effective/red zone model. The newer guide’s product advice against aggressive default management can coexist with empirical evidence about older models or specific tasks. Test designs, context composition, and model version would be needed to substantiate that comparison.
- OB-04 has contextual support for the occurrence of missed instructions, with possible explanations or controls offered by the vendor. The guide does not test whether training overrides a conflicting prompt. AP-09 coverage concerns surfacing assumptions via explicit specs and review, with no evidence for the prevalence or causes of silent acceptance of contradictory requirements.
- A fresh reviewer’s context is distinct from the implementer’s, while model family, specification, repository and evaluation target may still be shared. This source therefore does not establish independent empirical confirmation or same-context self-review for BP-04. Its parallel section discusses separate work items and isolated checkouts, with no comparison of competing implementations of the same problem for BP-08. Its illustrations also provide no evidence about a vertical-slice review method for BP-05.
- Page content and described defaults can change across releases, surfaces, plans, and providers. Product procedures are anchored to the access date. The portable ideas are task boundaries, durable acceptance criteria, observable checks, independent-context review, and enforcement where appropriate. Product names and command semantics should be verified before reuse.

## Retrieval hints (plain-language user symptoms, families, tags)

| User might say | Evidence to reach for |
|---|---|
| “It keeps making the same change after I correct it.” | C03–C06, session steering and explicit handoff |
| “This thread is full of old tasks, but I need to retain part of the current one.” | C01–C02, C17, reset versus focused compaction |
| “Will starting over undo the files the agent touched?” | C04, separation of session history and rollback |
| “It built something plausible, but missed an edge case we agreed on.” | C05, C07–C10, spec and verification |
| “Adding the rule again hasn’t helped.” | C11–C14, instruction placement and controls |

Families and tags include session management, context drift, specification, review, verification, instruction scope, and operational constraints.

## Original article access and copyright/permission record

Publicly readable HTML and Markdown were available from the publisher. No page-specific redistribution license or grant for whole-article reuse was verified. The dossier uses original analysis and minimal terms needed to identify sections, commands, and mechanisms. It includes no copied article body, sample prompt, or code block. [Original article](https://code.claude.com/docs/en/best-practices) · [Publisher Markdown](https://code.claude.com/docs/en/best-practices.md)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0002--verification.md)

## Drive navigation

- [audits/PAT-0001--verification.md](../audits/PAT-0001--verification.md) · [Local copy](../audits/PAT-0001--verification.md)
- [audits/PAT-0002--verification.md](../audits/PAT-0002--verification.md) · [Local copy](../audits/PAT-0002--verification.md)
- [audits/PAT-0003--verification.md](../audits/PAT-0003--verification.md) · [Local copy](../audits/PAT-0003--verification.md)
- [audits/PAT-0004--verification.md](../audits/PAT-0004--verification.md) · [Local copy](../audits/PAT-0004--verification.md)
- [audits/PAT-0005--verification.md](../audits/PAT-0005--verification.md) · [Local copy](../audits/PAT-0005--verification.md)
- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/PAT-0007--verification.md](../audits/PAT-0007--verification.md) · [Local copy](../audits/PAT-0007--verification.md)
- [audits/PAT-0008--verification.md](../audits/PAT-0008--verification.md) · [Local copy](../audits/PAT-0008--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [patterns/PAT-0001--recover-a-drifting-coding-session.md](../patterns/PAT-0001--recover-a-drifting-coding-session.md) · [Local copy](../patterns/PAT-0001--recover-a-drifting-coding-session.md)
- [patterns/PAT-0002--verify-an-unfamiliar-api-call.md](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md) · [Local copy](../patterns/PAT-0002--verify-an-unfamiliar-api-call.md)
- [patterns/PAT-0003--slice-a-change-for-review.md](../patterns/PAT-0003--slice-a-change-for-review.md) · [Local copy](../patterns/PAT-0003--slice-a-change-for-review.md)
- [patterns/PAT-0004--compare-repair-with-fresh-candidates.md](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md) · [Local copy](../patterns/PAT-0004--compare-repair-with-fresh-candidates.md)
- [patterns/PAT-0005--turn-review-feedback-into-a-check.md](../patterns/PAT-0005--turn-review-feedback-into-a-check.md) · [Local copy](../patterns/PAT-0005--turn-review-feedback-into-a-check.md)
- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md) · [Local copy](../patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md)
- [patterns/PAT-0008--take-ownership-before-submitting-ai-code.md](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md) · [Local copy](../patterns/PAT-0008--take-ownership-before-submitting-ai-code.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/AP-01--sunk-cost-over-iteration.md](../topics/AP-01--sunk-cost-over-iteration.md) · [Local copy](../topics/AP-01--sunk-cost-over-iteration.md)
- [topics/AP-02--flying-blind-vibe-coding.md](../topics/AP-02--flying-blind-vibe-coding.md) · [Local copy](../topics/AP-02--flying-blind-vibe-coding.md)
- [topics/AP-03--answer-injection.md](../topics/AP-03--answer-injection.md) · [Local copy](../topics/AP-03--answer-injection.md)
- [topics/AP-06--ai-slop.md](../topics/AP-06--ai-slop.md) · [Local copy](../topics/AP-06--ai-slop.md)
- [topics/AP-08--obsessing-over-rules.md](../topics/AP-08--obsessing-over-rules.md) · [Local copy](../topics/AP-08--obsessing-over-rules.md)
- [topics/AP-09--silent-misalignment.md](../topics/AP-09--silent-misalignment.md) · [Local copy](../topics/AP-09--silent-misalignment.md)
- [topics/BP-01--knowledge-checkpointing.md](../topics/BP-01--knowledge-checkpointing.md) · [Local copy](../topics/BP-01--knowledge-checkpointing.md)
- [topics/BP-02--active-partnership.md](../topics/BP-02--active-partnership.md) · [Local copy](../topics/BP-02--active-partnership.md)
- [topics/BP-03--happy-to-delete-start-fresh.md](../topics/BP-03--happy-to-delete-start-fresh.md) · [Local copy](../topics/BP-03--happy-to-delete-start-fresh.md)
- [topics/BP-04--feedback-flip.md](../topics/BP-04--feedback-flip.md) · [Local copy](../topics/BP-04--feedback-flip.md)
- [topics/BP-05--slice-for-review.md](../topics/BP-05--slice-for-review.md) · [Local copy](../topics/BP-05--slice-for-review.md)
- [topics/BP-06--context-management-discipline.md](../topics/BP-06--context-management-discipline.md) · [Local copy](../topics/BP-06--context-management-discipline.md)
- [topics/BP-09--decision-guards.md](../topics/BP-09--decision-guards.md) · [Local copy](../topics/BP-09--decision-guards.md)
- [topics/BP-10--rose-feedback.md](../topics/BP-10--rose-feedback.md) · [Local copy](../topics/BP-10--rose-feedback.md)
- [topics/OB-01--context-rot.md](../topics/OB-01--context-rot.md) · [Local copy](../topics/OB-01--context-rot.md)
- [topics/OB-03--obedient-contractor.md](../topics/OB-03--obedient-contractor.md) · [Local copy](../topics/OB-03--obedient-contractor.md)
- [topics/OB-04--selective-hearing.md](../topics/OB-04--selective-hearing.md) · [Local copy](../topics/OB-04--selective-hearing.md)
- [topics/OB-07--solution-fixation.md](../topics/OB-07--solution-fixation.md) · [Local copy](../topics/OB-07--solution-fixation.md)
- [topics/OB-09--hallucination-in-code.md](../topics/OB-09--hallucination-in-code.md) · [Local copy](../topics/OB-09--hallucination-in-code.md)
- [topics/OB-10--limited-attention-focus.md](../topics/OB-10--limited-attention-focus.md) · [Local copy](../topics/OB-10--limited-attention-focus.md)
- [topics/OB-12--excess-verbosity.md](../topics/OB-12--excess-verbosity.md) · [Local copy](../topics/OB-12--excess-verbosity.md)
