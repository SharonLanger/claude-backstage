---
artifact_id: SRC-0007
artifact_type: source_verification
reviewer: review_collab
reviewed: "2026-11-21"
initial_verdict: PASS WITH CHANGES
verdict: PASS
---

# Independent source review of SRC-0007

**Final disposition — PASS.** I checked all 11 claims against the 16-page accepted author manuscript and checked the underlying survey questions where respondents’ words or preferences affect interpretation. One correction to the statement of reuse rights was requested, made and independently rechecked. [Source dossier](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Original manuscript](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf)

## Numbered findings

| Finding | Item | Finding and first-pass disposition |
|---|---|---|
| 1 | Identity, publication and disclosure | Pass. The manuscript's title page names all six authors and identifies their affiliations. Its footer records acceptance at IEEE TSE and DOI 10.1109/TSE.2026.3655626. The coauthor institution lists January 27, 2026. The issue citation is 52(7), 2095–2110. The manuscript's printed page numbers differ from the issue pagination. The acknowledgment names JetBrains as a funder, and the phase-one IDE requirement is disclosed. [Manuscript p. 1](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=1) · [Acknowledgment p. 15](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=15) · [JetBrains Research](https://kairos.jetbrains.com/research/publications/genai-human-interactions) · [DBLP issue citation](https://dblp.uni-trier.de/rec/journals/tse/SalomonKSHMF26.html) |
| 2 | SRC-0007:C01 | Pass. Of 34 participants, 30 met the five-workday threshold. They represented 22 countries, contributed 627 experience samples and 207 daily responses across 5–12 days, and 22 completed interviews. The schedule and agreement check of 115 data points (κ = 0.704) match the methods. These are repeated reports. [Abstract and §§3.1–3.1.4, pp. 1, 4–6](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=4) |
| 3 | SRC-0007:C02 | Pass. The 29-question survey retained 131 of 194 respondents, drawn from 52 countries. Eighty-six identified as senior. Eligibility included individual and team use, employer permission and more than three months of corporate use. Recruitment limits generalization. [§3.2 and Tables 3–5, pp. 7–8](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=7) |
| 4 | SRC-0007:C03 | Pass. Section 4.1 reports 66 of 131 agreed with shifting technical help toward AI and separately reports 62% found AI easier to ask without embarrassment. Table 3E supplies the question wording and the accounts distinguish substituted questions from ones a person might never have asked. [§4.1, Table 6, p. 9](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=9) |
| 5 | SRC-0007:C04 | Pass. The three categories in the interruption question total 131. Counts of 37, 42 and 52 correspond to reported percentages of 28%, 32% and 40%, respectively, for agreement, disagreement and neutrality. The result qualifies the accounts of improved focus. [§4.2, p. 10](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=10) |
| 6 | SRC-0007:C05 | Pass. Table 5 places 9% in the fully integrated category. Section 4.2 reports the exploratory integration association at p = .03 and identifies the other predictors as unreliable. The same section supplies the separate perceived speed and confidence figures (59% and 39%). No effect magnitude is reported there. [Table 5, p. 7](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=7) · [§4.2 and footnote 8, p. 10](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=10) |
| 7 | SRC-0007:C06 | Pass. GenAI choices for algorithm implementation, task breakdown and brainstorming were 93, 78 and 77 of 131, respectively. The source asked where respondents would take each question. [Table 3G, p. 8](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=8) · [§4.3, p. 11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=11) |
| 8 | SRC-0007:C07 | Pass. The colleague counts were 85 for clarifying requirements or business logic and 66 for work history. Validation drew 62 GenAI choices and 53 colleague choices. Documentation and the web were also offered. [§4.3, p. 11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=11) |
| 9 | SRC-0007:C08 | Pass. The accounts of initial exploration precede the survey results. Approximately 52 respondents reported more intentional collaboration, and 96 agreed with the separate alternative-approaches item. The dossier distinguishes generated options from options surfaced by peers. [Table 3E, p. 8](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=8) · [§§4.3–4.4, pp. 10–11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=10) |
| 10 | SRC-0007:C09 | Pass. Theme 8 includes participants’ accounts of actively seeking company and conversation. They support the account of continued contact. Neither prevalence nor long-term social isolation was measured by those accounts. [§4.4, p. 11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=11) |
| 11 | SRC-0007:C10 | Pass. The implications accompanying the media-effects framework propose intentional mentorship, additional perspectives for consequential decisions and informal contact. The study did not evaluate the effects of implementing these practices. [§5 and Figure 3, pp. 11–13](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=12) |
| 12 | SRC-0007:C11 | Pass. The authors describe self-report and recruitment limitations and call for team-level research and behavioral corroboration. The plugin prompted reports. Individual differences in team setting also qualify the results, including one participant who reported interacting only with customers. [§§6.3–6.4.3, pp. 13–15](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=14) |
| 13 | Topic fit, related publications and independence | Pass. AP-05 is supported for changes in where some developers seek help. Sustained withdrawal, reduced pairing and overall teamwork effects remain unresolved. The example involving payment retries and the proposed handoff format are labeled catalog adaptations. The related sources’ own results support the limited contrast drawn. Neither serves as an independent repeat of this survey. [Al Haque et al., §4.3](https://arxiv.org/html/2408.04032v1) · [Vaz Pereira et al., §IV-A and Fig. 2](https://escholarship.org/content/qt59h2f5hs/qt59h2f5hs_noSplash_384d9a7089e80d3d0ceb978ca827ba7f.pdf#page=5) |
| 14 | Original expression and permissions | Change requested. The manuscript footer identifies CC BY-NC-ND 4.0. The dossier uses independent prose and factual results, with no reproduced article, graphic or interview passage. The first rights paragraph said additional permission was required for every use outside the license. The CC deed preserves applicable legal exceptions and limitations. [Manuscript footer, p. 1](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=1) · [License deed, Notices](https://creativecommons.org/licenses/by-nc-nd/4.0/) |

## Recheck and limits

I reopened the corrected dossier. Its rights record now states that uses outside the license may require permission unless permitted under an applicable exception or limitation. The frontmatter limits the license grant to unchanged, attributed, noncommercial sharing with the required notices. Finding 14 is closed.

This audit verified the published findings, method descriptions and survey wording. It did not recalculate the exploratory regression or recode participant responses. The hosting institution, issue index and dataset landing page describe the same publication or underlying study. The accessible evidence for the source claims is the accepted manuscript. [Dataset record](https://zenodo.org/records/17049655) · [Manuscript](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf)

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0007--developer-collaboration-and-ai.md](../sources/SRC-0007--developer-collaboration-and-ai.md) · [Local copy](../sources/SRC-0007--developer-collaboration-and-ai.md)
