---
source_id: SRC-0009
audit_type: independent_source_review
reviewed: 2026-11-21
reviewer: review_domain
initial_verdict: PASS WITH CHANGES
verdict: PASS
---
# Independent verification of SRC-0009

**Initial verdict — PASS WITH CHANGES.** The workflow claims are supported. Finding 8 requires a correction to release attribution and chronology. [Source dossier](../sources/SRC-0009--domain-language-and-decisions.md)

## Review scope

I independently reopened the AI Hero article, both issue threads, the repository skill and its two format guides, two versioned release pages, the repository license and AI Hero’s general terms. The page displays Matt Pocock as author and August 24, 2026 as its update date. A separate first-publication date and numbered article revision could not be verified from the page. The author distributes the skill. His article and repository document the same workflow. The two user reports give additional project context. No comparative evaluation appears in these materials. [Article and byline](https://www.aihero.dev/skills-domain-modeling) · [Skill definition](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)

## Findings

1. **SRC-0009:C01 — supported.** The design discussion tests the boundary of a term with concrete cases. A settled definition triggers an immediate glossary update. Both actions are explicit instructions. [What it does](https://www.aihero.dev/skills-domain-modeling#what-it-does) · [During the session](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md#during-the-session)
2. **SRC-0009:C02 — supported.** The rules limit entries to local concepts, permit one or two sentences and identify replaced synonyms. The map determines which glossary to use when multiple contexts exist. [Prerequisites](https://www.aihero.dev/skills-domain-modeling#prerequisites) · [Glossary format](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/GLOSSARY-FORMAT.md#rules)
3. **SRC-0009:C03 — supported.** The source’s whole-order cancellation example demonstrates a clarification before editing. It is an illustration. The dossier’s warehouse case is explicitly original. [Cross-referencing](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops)
4. **SRC-0009:C04 — supported.** All three ADR criteria must hold. The default template asks for one to three sentences and makes additional sections optional. The dossier attributes the selection criteria to the author and labels its later-editor instructions as adaptations. [Two artifacts, two bars](https://www.aihero.dev/skills-domain-modeling#two-artifacts-two-bars) · [ADR format](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/ADR-FORMAT.md#when-to-offer-an-adr)
5. **SRC-0009:C05 — supported.** The author limits default checks to code and committed domain records. Issue 717’s reporter manually checked two ambiguous names. A prior issue had resolved one. The other remained open in the project’s terminology. The reporter describes adding a local tracker-search instruction. The feature request itself displayed Open at review. [Article, cross-reference scope](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops) · [Issue 717, Where I hit this and Workaround we used](https://github.com/mattpocock/skills/issues/717)
6. **SRC-0009:C06 — supported.** Pocock describes skipped invocation and overgrown glossaries. He advises explicit invocation and removing misplaced details before splitting a glossary. The dossier preserves the qualitative nature of his reports. [When to reach for it](https://www.aihero.dev/skills-domain-modeling#when-to-reach-for-it) · [Common questions](https://www.aihero.dev/skills-domain-modeling#common-questions)
7. **SRC-0009:C07 — supported.** The FAQ distinguishes formal names from everyday prose and covers a one-day project, review burden and an objection about agent behavior under plain-English prompts. The dossier assigns no measured improvement to using domain terms. [Common questions, glossary value](https://www.aihero.dev/skills-domain-modeling#common-questions)
8. **SRC-0009:C08 — correction required on first review.** The recommendation to scaffold a glossary and the figure of more than 50 questions match the FAQ. The figure is a single reported experience. The rename shipped across the skills distribution in v1.3.0 on October 4. The setup-assisted migration appears separately in v1.3.2 on October 29. The August 24 date displayed by the article cannot serve as a reliable date for those statements in the live FAQ. The draft called v1.3.0 a version of the individual skill. The reviewer requested precise attribution and a release link. [Common questions, naming and scaffolding](https://www.aihero.dev/skills-domain-modeling#common-questions) · [v1.3.0, change 006a52b](https://github.com/mattpocock/skills/releases/tag/v1.3.0) · [v1.3.2, change ed0de59](https://github.com/mattpocock/skills/releases/tag/v1.3.2)
9. **SRC-0009:C09 — supported.** The article’s two customization routes are accurately described. The FAQ still calls the split request open. GitHub records closure as not planned on October 6, 2026 and labels the preceding owner-account comment as generated by AI during triage. [Common questions, custom ADR format](https://www.aihero.dev/skills-domain-modeling#common-questions) · [Issue 557, October 6 activity](https://github.com/mattpocock/skills/issues/557)

## Topic and rights checks

AP-09 and BP-02 fit the prescribed intervention when a person’s intent conflicts with code. BP-07 covers the part of semantic anchoring concerned with shared names. BP-09 covers the use of a decision record to preserve rationale. The dossier places limits on both mappings. Superiority over plain English and prevention of future accidental reversals remain open questions. Linking the ADR from tests or comments is catalog advice. [Article, FAQ and selection criteria](https://www.aihero.dev/skills-domain-modeling)

The explanatory prose and warehouse example are original. Source-specific labels, file paths, named criteria and short factual examples are attributed. Article reuse remains unverified. Section 2 of the website terms addresses reproduction, while the repository’s MIT grant covers its software and associated documentation and carries a notice condition. I found no article-specific grant in the material checked. [Site terms, §2](https://www.aihero.dev/privacy) · [Repository license](https://github.com/mattpocock/skills/blob/main/LICENSE)

## Disposition

**Final verdict — PASS after correction, November 21, 2026.** I reread the revised provenance, C08 and related-work passage against the FAQ and both release entries. C08 now identifies v1.3.0 as a distribution release. The dossier dates the setup-assisted migration separately and flags the limitation of the displayed article date. The remaining eight ledger claims passed the first review. No substantive issues remain open. [v1.3.0 release notes](https://github.com/mattpocock/skills/releases/tag/v1.3.0) · [v1.3.2 release notes](https://github.com/mattpocock/skills/releases/tag/v1.3.2)

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0009--domain-language-and-decisions.md](../sources/SRC-0009--domain-language-and-decisions.md) · [Local copy](../sources/SRC-0009--domain-language-and-decisions.md)
