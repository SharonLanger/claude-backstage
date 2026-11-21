---
source_id: SRC-0007
status: accepted
original_title: "From Disruptions to Discussions: How GenAI Impacts Human Interactions in Software Development"
authors: ["Marie Salomon", "Ekaterina Koshchenko", "Agnia Sergeyuk", "Reid Holmes", "Gail C. Murphy", "Thomas Fritz"]
publisher: "IEEE Transactions on Software Engineering, IEEE"
source_type: empirical_paper
published: 2026-01-27
updated: unknown
accessed: 2026-11-21
original_url: "https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf"
publication_url: "https://ieeexplore.ieee.org/document/11363384"
source_version: "Accepted author manuscript, DOI 10.1109/TSE.2026.3655626. Journal issue 52(7), pp. 2095–2110."
full_text_reuse: authorized
reuse_basis: "CC BY-NC-ND 4.0 notice in the accepted author manuscript. Permission covers sharing unchanged licensed material noncommercially with attribution and the required notices."
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [AP-05, BP-02, OB-11]
related_patterns: [PAT-0006]
review: PASS
publication_status: published
---

# From Disruptions to Discussions: How GenAI Impacts Human Interactions in Software Development

## Provenance and scope read

Marie Salomon and colleagues report a two-phase mixed-method study in *IEEE Transactions on Software Engineering*. JetBrains Research, a coauthor affiliation, dates its publication listing January 27, 2026. The journal issue citation is volume 52, issue 7, pages 2095–2110. The IEEE Xplore article page returned a JavaScript verification gate, and the publisher PDF did not load through the web reader. The review below uses the 16-page accepted author manuscript hosted by coauthor Reid Holmes at UBC. All page references below use its printed pages 1–16. [Author manuscript](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf) · [Coauthor institution listing](https://kairos.jetbrains.com/research/publications/genai-human-interactions) · [IEEE Xplore record](https://ieeexplore.ieee.org/document/11363384) · [Issue citation in dblp](https://dblp.uni-trier.de/rec/journals/tse/SalomonKSHMF26.html)

The reading covers the abstract, §§1–7, Tables 1–6, Figures 1–3, acknowledgments, and references relevant to the comparison below. The manuscript links a supplementary package containing study materials, data and a codebook. The Zenodo version 1 listing was inspected. The underlying files and regression estimates were outside this reading. Two authors are at JetBrains Research, JetBrains contributed funding, and phase one required a research plugin for JetBrains IDEs. UBC and University of Zurich researchers also coauthored the paper, and participants used tools from several vendors. [Author manuscript, pp. 1, 4 and 15](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=4) · [Dataset version 1 record](https://zenodo.org/records/17049655)

## Reader's orientation

The paper asks which reasons for talking to teammates change when a developer can privately ask an AI tool. The distinction that emerges is between getting an answer to a routine technical question and using a conversation to learn project history, weigh competing tradeoffs, or build a relationship. Some developers described AI as both a substitute for routine help and a way to prepare for more substantial conversations with peers. The survey shows wider variation in whether interruptions decreased.

The study measures individual accounts and hypothetical help-seeking choices. It leaves open whether teams experience a net change in interaction volume, pair programming, mentorship, knowledge transfer or isolation over time. It also leaves open how much the effect depends on team practices and tools.

## Detailed analytical reading (original words)

### Study design and what each phase can show

Phase one followed 30 professional developers from 22 countries for 5–12 days in their ordinary work. Thirty-four took part and four fell below the inclusion threshold of five workdays. A JetBrains IDE plugin prompted brief self-reports three times per day and a separate end-of-workday reflection. The 627 experience samples and 207 daily surveys are repeated reports from those 30 people. Twenty-two members of the same group also completed optional interviews. The researchers coded the contemporaneous responses inductively, assessed coder agreement on a held-out subset (115 data points, Cohen's κ = 0.704), then used the interview material to elaborate the resulting themes. The study defines human interaction broadly enough to include customers and other project stakeholders. One phase-one developer worked alone and interacted only with customers in a typical week. [Author manuscript, pp. 3–7 and 14](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=3)

Phase two surveyed 131 eligible respondents from 52 countries out of 194 responses. Its 29 questions were informed by phase one and asked about perceived changes and preferences. Eligibility included active work use by the respondent and their team, employer permission, and more than three months of corporate GenAI use. Two-thirds of respondents identified as senior (86/131, reported as 66%). The second phase tests whether themes resonate across a wider sample of adopters. It supplies neither a comparison group of non-adopters nor a baseline measured before adoption. [Author manuscript, §§3.2–3.2.2 and Tables 3–5, pp. 7–8](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=7)

### Routine questions, perceived interruptions and the missing baseline

Participants described asking AI for implementation help, explanations, or debugging before seeking a teammate. Immediacy mattered in asynchronous teams, where a response from a colleague could arrive hours later. Some developers also reported that they could ask an elementary question privately without worrying about embarrassment. In phase two, 66 of 131 agreed or strongly agreed with the shift toward AI for technical help and the paper reports that 62% found AI easier to ask without fear of embarrassment. A question now sent to AI may previously have gone to a teammate or may previously have gone unasked. The study does not estimate the share of each. [Author manuscript, §§4.1–4.2 and Table 6, pp. 8–10](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=8)

The interruption measure provides a check on how far the qualitative accounts travel. Of 131 respondents, 37 (28%) agreed or strongly agreed that colleague interruptions fell, 42 (32%) disagreed or strongly disagreed, and 52 (40%) were neutral. The authors report that full integration into team workflows was associated with reporting fewer interruptions in an exploratory ordinal-logistic model (p = .03). The survey put about 9% of respondents in that integration category. The main text gives no effect size for the association and reports that team size, duration of AI use, frequency of team use and experience level did not reliably predict reported reductions. In the same survey, 59% reported faster team task completion and 39% reported more confidence in team solutions. Perceived speed and fewer interruptions are separate outcomes. [Author manuscript, Table 5, p. 7 and §4.2, pp. 9–10](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=10)

### Why some questions still go to colleagues

The survey shows how the preferred source depended on the question. Respondents most often chose AI for an algorithm implementation question (93/131), breaking work into subtasks (78/131), and brainstorming implementation options (77/131). They most often chose a colleague for clarifying business logic or requirements (85/131) and learning how something had been done before (66/131). Checking whether a solution made sense before implementation yielded a closer split (62/131 AI and 53/131 colleague). The survey scenarios capture reported preferences, with documentation and the web also available as choices. [Author manuscript, Table 3 section G and §4.3, pp. 8 and 10–11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=11)

Participants described cases where a colleague already knew the local constraints and could answer readily. They also described cases where AI supplied outside technical expertise unavailable in the team. Some interview accounts described junior developers bringing preliminary work from AI into a discussion with more experienced teammates. About 40% of survey respondents reported collaborating more intentionally, and 96/131 (73%) said working with teammates surfaced alternative approaches that AI had not suggested. The latter result can coexist with the 77 respondents who chose AI for initial brainstorming. The questions concern different jobs: generating a starting set of options and noticing omissions or tradeoffs in those options. Separately, some qualitative participants described deliberately seeking human company and conversation even when they had little need for technical help. [Author manuscript, §§4.3–4.4, pp. 10–11](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=10)

### What the authors propose teams try

The authors suggest handling bounded technical queries independently when practical, drawing teammates into context-heavy decisions, scheduling explicit mentoring for complex problems, bringing additional viewpoints into critical decisions, and creating lightweight occasions for informal contact. They use McLuhan's media-effects framework to reason about how a gain in access to immediate help could reduce incidental opportunities to learn or connect, particularly in hybrid work. Their interpretation distinguishes tendencies raised by developers from long-run effects that remain forward-looking. The study did not test the proposed changes to team routines. [Author manuscript, §5 and Figure 3, pp. 11–13](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=12)

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support / caveat |
|---|---|---|---|---|
| SRC-0007:C01 | Phase one gathered 627 experience samples and 207 end-of-workday responses from 30 developers over 5–12 days, plus 22 interviews with a subset of that group. | Study method | Abstract p. 1, §§3.1–3.1.4 pp. 4–6, Figure 1 p. 5 | Direct. Repeated individual reports and overlapping interview sample. |
| SRC-0007:C02 | A later phase-one-informed survey retained 131 eligible respondents across 52 countries, including 86 who identified as senior. Eligible teams were already active GenAI users. | Study method | §§3.2.1–3.2.2 and Table 4 p. 7, Table 3 p. 8 | Direct. Recruited sample of developers whose employers permitted use. |
| SRC-0007:C03 | Participants described moving routine technical help to AI. In the survey, 66/131 agreed or strongly agreed with the shift in technical help, and 62% found asking AI easier without fear of embarrassment. | Qualitative theme and descriptive survey result | §4.1 pp. 8–9, Table 6 themes 1–3 p. 9, Table 3 section E p. 8 | Direct for reported perceptions and practices. No interaction count or measure of lasting withdrawal. |
| SRC-0007:C04 | Survey respondents split 37/131 agree, 42/131 disagree and 52/131 neutral on whether colleague interruptions had declined. | Descriptive survey result | §4.2 p. 10, Table 3 section E p. 8 | Direct. The largest group was neutral and disagreement exceeded agreement. |
| SRC-0007:C05 | The authors report an exploratory association between full team-workflow integration and reporting fewer interruptions (p = .03). | Exploratory survey association | §4.2 and footnote 8 p. 10, Table 5 p. 7 | Direct as reported. Small integration category, perception outcome, no causal inference. |
| SRC-0007:C06 | Survey respondents most often chose AI for algorithm implementation (93/131), decomposing a task (78/131) and brainstorming implementation (77/131). | Hypothetical survey preference | §4.3 p. 11, Table 3 section G p. 8 | Direct for the presented scenarios. Choices do not establish answer quality or work outcomes. |
| SRC-0007:C07 | Respondents most often chose a colleague to clarify business logic or requirements (85/131), or ask about prior work (66/131). For pre-implementation validation, AI drew 62/131 and a colleague 53/131. | Hypothetical survey preference | §4.3 p. 11, Table 3 section G p. 8 | Direct and task-specific. Validation preferences were comparatively close. |
| SRC-0007:C08 | Developers described using AI for initial exploration and holding subsequent human discussions about context and tradeoffs. About 40% of the survey sample reported more intentional collaboration, and 96/131 said peers provided alternatives AI had not suggested. | Qualitative theme and descriptive survey result | §§4.3–4.4 pp. 10–11, Table 6 themes 5–7 p. 9, Table 3 section E p. 8 | Direct for the reported experiences. The two survey items measure different perceptions. |
| SRC-0007:C09 | Some qualitative participants said they sought contact with colleagues for social reasons alongside continuing to use AI. | Qualitative theme | §4.4 p. 11, Table 6 theme 8 p. 9 | Direct for participants' accounts. The authors' longer-run loss-of-contact argument in §5 remains interpretive. |
| SRC-0007:C10 | The authors propose preserving human input on consequential decisions, dedicating time to mentoring and creating informal opportunities for contact. | Author advice | §5 pp. 11–13, practical implications under the four framework categories, and §7 p. 15 | Practical proposals drawn from perceptions. Their benefits were not measured in this study. |
| SRC-0007:C11 | The authors describe their evidence as individual self-reports subject to recall, interpretation and selection biases. They propose team-level observations and communication records as follow-up. | Study limitation | §§6.3–6.4.3 pp. 13–15 | Direct. IDE prompts were for reporting. The analysis does not measure interaction logs or longitudinal team outcomes. |

## Extractable practitioner insights

### Decide who to ask based on who holds the missing information

A developer can use AI to orient themselves on a general library feature or understand an error. A domain owner is the better first contact when the next decision depends on a local business rule or historical compatibility constraint. An example for this catalog is a developer using AI to learn how library retries work and asking the service owner why retries were disabled for one payment event. A short account of the proposed change and the unresolved question can make that discussion more concrete. The example and the handoff format are catalog adaptations. The study supports differences in preferences and reported experiences across question types. Related to AP-05 and SRC-0007:C03, C06–C08. [Author manuscript, §§4.1, 4.3 and 5, pp. 8–13](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=10)

### Give developers a way to reach peers for judgment and learning

If teammates rarely see each other's reasoning after routine help-seeking moves to private chats, the authors suggest arranging mentoring for complex decisions and making room for informal contact. A catalog adaptation would reserve an existing team slot for a developer to bring a decision still open to change, including the option they are considering and the local assumptions they need help checking. The study motivates trying such a practice, and its mixed interruption data give teams reason to check whether the change works in their setting. Related to AP-05 and SRC-0007:C04, C08–C11. [Author manuscript, §§4.2–4.4 and 5, pp. 9–13](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=12)

## Related work, conflicts, and limitations

In §§2.2.2 and 6.2, Salomon and colleagues compare their accounts with research that frames collaboration differently. Al Haque and colleagues' preprint reports reduced face-to-face interactions and organic knowledge sharing as perceptions from an information-seeking study. Vaz Pereira and colleagues' case study in a single Brazilian company reports modest perceived collaboration changes, with many seeing no improvement in that dimension. These are related studies with different settings and questions. Their measurements cannot establish a shared effect size or resolve whether the differences arise from adoption maturity, workplace context, or other factors. These related papers are context for the comparison, with their estimates outside this dossier's claim ledger. [Al Haque et al., preprint §IV-B, Project and Team Impact](https://arxiv.org/html/2408.04032v1) · [Vaz Pereira et al., §IV-A and Figure 2](https://escholarship.org/content/qt59h2f5hs/qt59h2f5hs_noSplash_384d9a7089e80d3d0ceb978ca827ba7f.pdf) · [Salomon et al., §6.2](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=13)

The strongest fit is AP-05 as evidence of perceived substitution and continued human contact. The study cannot establish widespread isolation, systematic avoidance of teammates, reduced pair programming, the durability of onboarding or mentoring outcomes, or improvements in team output. The phase-one IDE requirement, senior-heavy phase-two sample and recruitment among active adopters matter when translating the results to junior-heavy teams or teams early in adoption. The two study phases provide complementary perspectives within one publication. The UBC manuscript, IEEE version of record and Zenodo dataset share study provenance. The same authors' later developer-persona paper explicitly draws from the phase-two survey of 131 respondents, so that analysis shares the underlying sample. [Author manuscript, §6.4, pp. 14–15](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf#page=14) · [Developer-persona paper, §III-A, p. 2](https://www.cs.ubc.ca/~rtholmes/papers/icsme_2026_salomon.pdf#page=2)

## Retrieval hints (plain-language user symptoms, families, tags)

- “Everyone asks the AI instead of asking a teammate.” “We get fewer little questions, but I don't know whether people are blocked or learning.”
- “AI can explain the library, but it doesn't know why we built our system this way.” “I want someone to challenge a design the assistant helped me draft.”
- “New hires bring AI answers to a mentor.” “We do less informal troubleshooting together.”
- Family: team collaboration and knowledge sharing. Tags: AP-05, help seeking, peer review, mentoring, async collaboration, project history, requirements clarification, perceived interruptions.

## Original article access and copyright/permission record

The accepted manuscript explicitly displays CC BY-NC-ND 4.0. That license permits sharing the covered material unchanged for noncommercial purposes with attribution and required notices. Uses outside the license may require separate permission unless an applicable legal exception or limitation permits them. This dossier contains original analysis, factual study results and links. The dataset is a separate record with its own rights information. [Author manuscript and license notice](https://www.cs.ubc.ca/~rtholmes/papers/tse_2026_salomon.pdf) · [CC BY-NC-ND 4.0 terms](https://creativecommons.org/licenses/by-nc-nd/4.0/) · [Canonical article DOI](https://doi.org/10.1109/TSE.2026.3655626)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0007--verification.md)

## Drive navigation

- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/SRC-0007--verification.md](../audits/SRC-0007--verification.md) · [Local copy](../audits/SRC-0007--verification.md)
- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/AP-05--ai-isolation.md](../topics/AP-05--ai-isolation.md) · [Local copy](../topics/AP-05--ai-isolation.md)
- [topics/BP-02--active-partnership.md](../topics/BP-02--active-partnership.md) · [Local copy](../topics/BP-02--active-partnership.md)
- [topics/OB-11--keeping-up-review-fatigue.md](../topics/OB-11--keeping-up-review-fatigue.md) · [Local copy](../topics/OB-11--keeping-up-review-fatigue.md)
