# Practitioner research intake — batch 2

Source review and intake: 2026-11-22. Base: merged main `1fd26b1d50760b72093ff9dce642da6588749074`, including PRs #8 and #9.

## Outcome

Six agreed practitioner topics become four new guides and two enrichments of existing entries. They support a short tip, reusable wording, or a deeper explanation without requiring a custom harness. The Understand → Research → Deliver flow is unchanged. Existing first-turn clarification still applies; a README example is not a promise of an immediate diagnosis.

The README presentation lives separately in PR #10. This batch supplies its six destinations and exact symptom aliases. Raw research is unchanged and remains outside the installed catalog. Runtime guidance resides in the canonical entries below.

## Comparison and disposition

| Research candidate | Existing entries read and overlap | Disposition and distinct contribution | Canonical destination |
|---|---|---|---|
| [PAT-0007](raw/patterns/PAT-0007--ask-for-an-assessment-before-naming-a-fix.md) | B6 Reconnaissance-First gathers context; Root-Cause-Before-Retry diagnoses failure. | Enrich the latter with a practitioner procedure separating observations from a suggested cause. Avoid a duplicate diagnosis pattern. | [Assess before naming a fix](../../skills/sl-sensemaker/catalog/families/I-reliability-recovery/patterns/root-cause-before-retry.md#in-a-session-assess-before-naming-a-fix) |
| [PAT-0002](raw/patterns/PAT-0002--verify-an-unfamiliar-api-call.md) | Just-in-Time Retrieval obtains references; F03 exposes checks. Neither walks a reviewer through the dependency contract. | Write a D-family guide covering receiver, installed version, arguments, return contract, and behavior. | [Verify an unfamiliar API](../../skills/sl-sensemaker/catalog/families/D-verification-evaluation/guides/verify-unfamiliar-api.md) |
| [PAT-0004](raw/patterns/PAT-0004--compare-repair-with-fresh-candidates.md) | Fresh-Context Retry restores a session; Root-Cause-Before-Retry and the non-determinism use case address diagnosis and system variance. | Write an I-family guide for selecting among bounded implementations using common requirements and checks. | [Repair or a fresh attempt](../../skills/sl-sensemaker/catalog/families/I-reliability-recovery/guides/repair-or-fresh-attempt.md) |
| [BP-02](raw/topics/BP-02--active-partnership.md) | B1 Plan → Execute assumes a recognizable task; Clarify Domain Terms resolves particular ambiguous meanings. | Write a K-family guide for an interview that helps formulate the request before planning. | [Clarify an idea](../../skills/sl-sensemaker/catalog/families/K-human-control/guides/clarify-an-idea.md) |
| [AP-04](raw/topics/AP-04--cognitive-overload-too-many-starts.md) | B5 stages one task; K06 monitors agent execution. Neither addresses a person's queue of incoming decisions across tasks. | Write a K-family practical guide with attributed advice and local adaptations. This is not a new empirically established anti-pattern or concurrency limit. | [Manage review overload](../../skills/sl-sensemaker/catalog/families/K-human-control/guides/manage-review-overload.md) |
| [BP-09](raw/topics/BP-09--decision-guards.md) | Clarify Domain Terms already records rationale; D05 reviews behavior and F06 organizes instructions. | Enrich the domain guide with discoverability near the affected code and a compatibility-check example; cross-link existing protected-check guidance. | [Decision visibility](../../skills/sl-sensemaker/catalog/families/E-context-engineering/guides/clarify-domain-terms.md#make-an-intentional-decision-visible-at-the-edit) |

## Source checks and evidence boundaries

Original sections were opened and read for the retained claims. Research methods and topic notes supplied navigation and synthesis; acceptance in research alone was not treated as runtime inclusion. One relevant source can support advice; controlled effectiveness evidence is not required to present an author's scoped recommendation.

| Source / registry number | Original locator and contribution | Limits and reuse |
|---|---|---|
| Anthropic, Best practices for Claude Code / 26 | “Write a specific prompt,” “Brainstorm with Claude first,” “Give Claude a check to run,” short/scoped guidance, and instruction versus control sections. | Vendor advice. Interview stopping conditions and new prompts are catalog adaptations. Living source rechecked 2026-11-22. |
| Matt Pocock, The /domain-modeling Skill / 28 | “Two artifacts, two bars” and “Cross-referencing, and where it stops.” | Practitioner advice about rationale and discovery. Nearby references and compatibility checks are adaptations, not measured edit protection. |
| Jain et al., On Mitigating Code LLM Hallucinations with API Documentation / 31 | [2024 preprint v1](https://arxiv.org/html/2407.09726v1), §2.3, §3 and Appendix A.5–A.6. | Synthetic Python cloud-API tasks; not an evaluation of manual version matching or real project defect rates. The cited preprint is a version of SRC-0004's publication, not an independent second study. |
| Olausson et al., Is Self-Repair a Silver Bullet for Code Generation? / 32 | [ICLR 2024 paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf), §§3–5. | Test-based comparisons do not establish developer selection quality or optimal review time. The manual selection workflow is adapted from PAT-0004. |
| Counts / Haas interview with researcher Ye / 33 | [February 18, 2026 interview](https://newsroom.haas.berkeley.edu/ai-promised-to-free-up-workers-time-uc-berkeley-haas-researchers-found-the-opposite/), methodology and final answer. | One workplace account plus author advice. Queue inspection and a review-before-start trial are our applications. No intervention efficacy or universal task cap is claimed. |
| Sharma et al., Towards Understanding Sycophancy in Language Models / 34 | [v4](https://arxiv.org/html/2310.13548v4), §§3.2–3.3. | QA experiments motivate caution about user suggestions and unsupported challenges. The coding diagnosis sequence is an adaptation, not a measured cure for sycophancy. |

The entries cite public originals and summarize their relevant contributions. Newly composed prompts and examples are labeled. No external article text, figure, table, or code is reproduced. This batch does not modify batch 1's separately attributed ROSE adaptation. The remaining sources in PAT-0004/PAT-0007 are not imported as additional citations because this scoped intake does not rely on their distinct claims.

## Controls and short-answer walkthroughs

These are content and route checks, not measured effectiveness. Both the bridge and session lookup point to the same canonical entry; D, I, K, and E family indexes expose it as well.

| README symptom | Required context or controls | Supported next action | Boundary |
|---|---|---|---|
| Agrees with every diagnosis | An open cause and inspectable observations | Ask for assessment before edits; compare a prediction with evidence | Do not hide clues or reopen a verified diagnosis |
| Method does not exist | Installed dependency identity and a matching reference | Verify receiver, version, signature and effect | State untested integration behavior |
| Keeps patching the same thing | A bounded requirement, saved baseline, common checks | Preserve current work; compare a repair and a fresh candidate within a budget | No universal retry count or automatic winner |
| Cannot explain the idea | Conversation control and requirement ownership | Ask about the consequential choice; review an example and short agreement | An interview cannot decide unavailable business policy |
| Five tasks waiting for me | Control over task starts and routine review periods | Identify the pending human actions and try planned review periods | Preserve urgent escalation; no ideal concurrency cap |
| Intentional code rewritten | Current rationale and editable project files | Make the decision discoverable and inspect a compatibility check | Comments do not enforce behavior |

The original deleted-test route still reaches D02/AP10 and human review. The rejected-decision route still reaches session recovery. Team isolation and inaccessible instructions still produce explicit gaps.

## Coverage and integration

The [57-scenario inventory](practitioner-coverage.md) changes from 21 covered / 28 partial / 8 missing to **25 covered / 28 partial / 4 missing**. Stable IDs and original symptom wording are retained. P-09, P-25, P-35, and P-37 gain scoped coverage. P-13, P-43, and P-44 gain partial guidance; general pushback, delegation priorities, and optimal work-in-progress remain open. Missing scenarios are P-33, P-46, P-47, and P-48b.

Four guides and two guide indexes raise the catalog from 272 to 278 Markdown files; pattern count remains 137 and guide count rises from 9 to 13. The registry grows from 30 to 34 sources. Family, subfolder, use-case, lookup, and inventory routes are updated; no new family, top-level anti-pattern, or principle is introduced.

## Validation

- Local-link and anchor validation: 1,909 skill-local links and 127 research-record links checked, zero unresolved destinations.
- Install/reinstall checks pass, including all six README phrases and the original five practitioner routes. Protected-check routing, preserved user additions, missing-cache recovery, and exclusion of research records remain checked.
- Coverage table retains 57 scenario IDs and six columns. Source registry has 34 unique IDs. Actual catalog totals agree with the inventory.
- Read-through checks distinguish a generic explanation from an applicable action and keep the six entries usable as short tips.
- A separate read-only agent exercise used the skill, six README prompts, and illustrative user follow-ups. It selected the six canonical destinations, gave scoped tips for five situations, and continued with a consequential clarification question for the rough notification idea. This was a file-grounded simulation, not a live Claude Code run or a Windows test.
- Raw research, contributor rules, setup, SKILL.md, and the README from PR #10 are unchanged by this batch.
