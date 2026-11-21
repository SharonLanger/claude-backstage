---
source_id: SRC-0020
status: accepted
original_title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
authors: ["Thibaud Gloaguen", "Niels Mündler-Sasahara", "Mark Niklas Müller", "Veselin Raychev", "Martin Vechev"]
publisher: "arXiv (authors affiliated with ETH Zurich and LogicStar.ai)"
source_type: empirical_paper
published: 2026-02-12
updated: 2026-09-29
accessed: 2026-11-21
original_url: "https://arxiv.org/html/2602.11988v3"
source_version: "arXiv:2602.11988v3; DOI 10.48550/arXiv.2602.11988 identifies the record across versions"
full_text_reuse: authorized
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [AP-08, BP-06, BP-09, OB-04]
related_patterns: []
review: PASS
publication_status: published
---

# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

## Provenance and scope read

Thibaud Gloaguen, Niels Mündler-Sasahara and Martin Vechev list ETH Zurich affiliations. Mark Niklas Müller and Veselin Raychev list LogicStar.ai. This dossier covers the September 29, 2026 version of the authors’ empirical preprint. The arXiv record dates the first deposit to February 12, 2026. The analysis draws on the versioned HTML abstract, §§1–6, and the experimental, statistical, and dataset material in Appendices A–D. The v3 PDF was checked for the numerical tables and page locators. The experiment was not rerun and the raw traces were not independently recoded. [Version history and DOI](https://arxiv.org/abs/2602.11988v3) · [v3 HTML](https://arxiv.org/html/2602.11988v3) · [v3 PDF](https://arxiv.org/pdf/2602.11988v3)

## Reader's orientation

The study asks what changes when a coding agent receives a repository-level instruction file. Adding an auto-generated file consumed significantly more inference dollars and tool steps on both benchmarks. Task-resolution comparisons against omitting the file were inconclusive for both generated and developer-committed files. On CTXbench, developer-committed files did significantly better than generated ones. The traces show that agents changed what they did, including using tools described in the files, even though those changes yielded no established increase in test-based resolution over omission. For AP-08, this makes the recurring work imposed by guidance observable. The study did not assign increasing numbers of rules or measure compliance as a function of rule count. [§§4.2–4.4, pp. 6–9](https://arxiv.org/pdf/2602.11988v3#page=6) · [Appendix A.5 and Appendix B, pp. 16–17](https://arxiv.org/pdf/2602.11988v3#page=16)

## Detailed analytical reading

### What the experiment measures

The unit of work is an autonomous issue-resolution attempt on a pre-patch repository snapshot. SWE-bench Lite contributes 300 Python tasks from 11 repositories without a developer-provided agent file. CTXbench contributes 138 bug-fix and feature tasks selected from 5,694 PRs across 12 Python repositories that use developer-committed files. CTXbench draws on repos with a root context file, an existing test suite and at least 400 PRs. Its task descriptions and new tests were derived from historical PRs and their reference patches with LLM assistance. The authors checked that new tests failed on the baseline and passed against the reference patch, and reviewed and revised over-specified tests. New tests were combined with existing tests passing on the reference-patched repository. Table 1 reports mean coverage of 75% of changed code. Appendix C gives a concrete example of making a generated test accept an equivalent implementation by dropping its requirement for particular error text while preserving the failure check. [§3, pp. 3–5](https://arxiv.org/pdf/2602.11988v3#page=3) · [Appendix C, pp. 17–19](https://arxiv.org/pdf/2602.11988v3#page=17)

The same repository and issue can be run with no agent file (`None`), with a file made on the pre-patch checkout by the agent’s recommended initializer (`LLM`), or with the pre-existing developer-committed file (`Dev`, available only on CTXbench). Other repository documentation remains available in the primary experiment. The four configurations were Claude Code with Sonnet 4.5, Codex with GPT-5.2, Codex with GPT-5.1 mini, and Qwen Code with Qwen3-30B-Coder. A completion was sampled once per configuration, task and condition. Primary success is passing the required tests after application of the agent’s patch. Secondary metrics are interactions with the environment and inference dollars. The Qwen dollar figures use a proxy price estimate from OpenRouter because the model was deployed locally. [§4.1, pp. 5–6](https://arxiv.org/pdf/2602.11988v3#page=5) · [Appendix A.1, p. 13](https://arxiv.org/pdf/2602.11988v3#page=13)

### Task resolution and the cost of following guidance

| Benchmark and comparison | Mean change in resolution | Resolution p-value | Mean change in steps | Steps p-value | Inference cost change | Cost p-value |
|---|---:|---:|---:|---:|---|---:|
| SWE-bench Lite, generated vs. omitted | About −0.5 percentage points | 0.87 | +2.45 | 0.0287 | +20% on average | <0.00001 |
| CTXbench, generated vs. omitted | About −2 percentage points | 0.37 | +3.92 | 0.00004 | +23% on average | 0.00064 |
| CTXbench, developer-committed vs. omitted | About +2.4 percentage points | 0.21 | +3.34 | 0.00002 | Higher | 0.0126 |
| CTXbench, developer-committed vs. generated | Developer-committed higher | 0.038 | — | — | — | — |

Mean changes use the paper’s rounded summary. Resolution p-values use the two-sided Cochran–Mantel–Haenszel test in Table 3. Cost and step p-values use the stratified permutation tests in Table 6. Table 6 gives a larger p-value for generated-file cost on CTXbench than the blanket threshold printed in §4.2. Both indicate statistical significance at 0.05, and the table above uses the benchmark-specific result. For magnitude, the printed CTXbench means depend heavily on the configuration. For instance, GPT-5.2 had 65.2% resolution with omission and 68.1% with either file. Its mean inference cost was $0.38, $0.57 and $0.54 for omission, generated and developer-committed, respectively. Table 5 labels the second block “PLAN-BENCH” in v3. Its caption and Appendix A.4 say it reports Figure 3’s CTXbench comparison. [§4.2, Fig. 3 and Tables 2–3, p. 6](https://arxiv.org/pdf/2602.11988v3#page=6) · [Appendix A.4–A.5, Tables 5–6, pp. 15–16](https://arxiv.org/pdf/2602.11988v3#page=15)

### What actually changed in the traces

Agents with context files ran more tests and tended to search, read, and write more. The authors counted built-in tool names and used GPT-OSS-120B to classify shell calls. `uv` ran an average of 1.6 times per instance when the file mentioned it and fewer than 0.01 times when it did not. Other repository-specific tools averaged 2.5 and fewer than 0.05 calls under the corresponding conditions. These are markers of behavior responsive to operational guidance. Tool mentions may also reflect which tools a repository already uses. The study did not use a rubric to score every directive in each file. Reported average reasoning-token use also increased in the matched-instance analysis of GPT-5.2 and GPT-5.1 mini. For GPT-5.2 that increase was 22% on SWE-bench Lite and 14% on CTXbench with generated files, and 20% on CTXbench with developer-committed files. The authors propose that following instructions makes the work more demanding. The expenditure is observed and the explanation is an interpretation. [§4.3, Figs. 5–6, pp. 7–8](https://arxiv.org/pdf/2602.11988v3#page=7) · [Appendix A.2, Figs. 9 and 11, pp. 13–15](https://arxiv.org/pdf/2602.11988v3#page=13)

The authors tested whether repository overviews accelerated discovery using the number of steps before the agent first interacted with any file touched by the original PR. Eight of the 12 developer files had an overview, and overview sections were prevalent in generated files for three of the four configurations. The files produced no meaningful speedup on this measure. GPT-5.1 mini sometimes searched for and reread the agent file already in context. The comparison excludes the 3% of instances that never touched files in the original patch. First interaction with an original patch file is an imperfect proxy for useful navigation, since an alternative solution can begin elsewhere. [§4.3, Fig. 4, p. 7](https://arxiv.org/pdf/2602.11988v3#page=7)

### Where the file comparison ends and the overload question begins

Appendix B bins CTXbench results by the word lengths of the supplied files. The authors see no clear relationship between file length and task resolution or per-instance cost. This compares naturally varying files, so wording, repository, task and contents can vary together. Markdown sections and word counts give no inventory of distinct obligations. In a separate ablation, GPT-5.4 edited generated files to remove one category at a time and GPT-5.2 reran both benchmarks. Removing testing guidance reduced cost on CTXbench ($0.4715 to $0.3730, p=0.023) and SWE-bench Lite ($0.3272 to $0.2756, p=0.0035). Removing tooling guidance also reduced cost on SWE-bench Lite ($0.3272 to $0.2715, p=0.0012). Effects on task accuracy were inconclusive for all three categories, including overview. Together these comparisons support asking what each rule makes the agent do. The study leaves the incremental cost of the next arbitrary rule, the direction of any compliance change, and an overload threshold open. [§4.4, p. 9](https://arxiv.org/pdf/2602.11988v3#page=9) · [Appendix B, Fig. 13 and Table 7, pp. 16–17](https://arxiv.org/pdf/2602.11988v3#page=16)

The value of documentation depends on what else the agent can consult. In a separate CTXbench experiment, the authors created the agent files and then stripped Markdown documentation, examples and `docs/` contents from the repository, leaving the context file as the remaining documentation in the conditions that included one. Claude Code was excluded from this experiment. The authors report an average 2.7-point gain over omission for generated files in these runs. This is a boundary case in a modified benchmark, with no significance test reported for that number. It does not quantify the effect of adding a repository overview to a naturally underdocumented project. [Appendix B, Fig. 12, p. 16](https://arxiv.org/pdf/2602.11988v3#page=16)

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support and caveat |
|---|---|---|---|---|
| SRC-0020:C01 | The evaluations use SWE-bench Lite (300 tasks, 11 Python repos) and CTXbench (138 tasks, 12 Python repos). They compare omission with generated files on both benchmarks and developer-committed files on CTXbench. | Experimental design | [§3.2 and §4.1, pp. 4–6](https://arxiv.org/pdf/2602.11988v3#page=4) | Direct. Four model–agent configurations with one sample per task and condition. Resolution means the patch passes benchmark tests. |
| SRC-0020:C02 | Generated files reduced mean resolution by about 0.5 points on SWE-bench Lite and 2 points on CTXbench, each versus omission. The respective p-values are 0.87 and 0.37. | Empirical result | [§4.2, Fig. 3 and Table 3, p. 6](https://arxiv.org/pdf/2602.11988v3#page=6) | Direct. Estimates are inconclusive and do not establish equal performance or harm. |
| SRC-0020:C03 | On CTXbench, developer-committed files averaged roughly 2.4 points higher than omission (p=0.21) and significantly outperformed generated files (p=0.038). | Empirical result | [§4.2, Fig. 3 and Table 3, p. 6](https://arxiv.org/pdf/2602.11988v3#page=6) | Direct. The inference about generated-file comparison cannot establish superiority over omission. The packages differ in content and likely authorship. |
| SRC-0020:C04 | Generated files increased mean inference cost by 20% and 23% on SWE-bench Lite and CTXbench. Relative to omission, the tested file conditions increased steps and cost significantly in both datasets where applicable. | Empirical result | [§4.2, Table 2, p. 6](https://arxiv.org/pdf/2602.11988v3#page=6) · [Appendix A.5, Table 6, p. 16](https://arxiv.org/pdf/2602.11988v3#page=16) | Direct. Table 6 gives generated-file cost p-values <0.00001 and 0.00064, and developer-file cost p=0.0126. The measure is inference cost, with a proxy price for local Qwen. |
| SRC-0020:C05 | Agents ran more tests with files present. Mentioned tools appeared much more often in traces, such as `uv` at 1.6 calls per instance when mentioned versus fewer than 0.01 otherwise. | Trace comparison and association | [§4.3, Fig. 5 and tool-use examples, pp. 7–8](https://arxiv.org/pdf/2602.11988v3#page=7) · [Appendix A.2, Figs. 9 and 11, pp. 13–15](https://arxiv.org/pdf/2602.11988v3#page=13) | Direct for observable behavior and tool-use association. General compliance and adherence by rule count were unmeasured. |
| SRC-0020:C06 | Included files did not meaningfully shorten the time to first interaction with a file changed in the original PR, as measured in steps. For GPT-5.1 mini this step count increased significantly, with repeated file discovery and reading visible in traces. | Empirical result and trace observation | [§4.3, Fig. 4, p. 7](https://arxiv.org/pdf/2602.11988v3#page=7) | Direct for one navigation proxy. The comparison excludes approximately 3% of instances that never interacted with a file in the original patch. |
| SRC-0020:C07 | In a binned CTXbench comparison, neither success rate nor inference cost showed a clear relationship with context-file word length. | Observational analysis | [Appendix B, Fig. 13, pp. 16–17](https://arxiv.org/pdf/2602.11988v3#page=16) | Direct for the observed bins. Word length differs from rule count, and the groups do not isolate a length or rule-count intervention. |
| SRC-0020:C08 | Removing testing guidance from generated files reduced inference cost on both benchmarks, and removing tooling guidance reduced it on SWE-bench Lite. All three category-removal comparisons had inconclusive accuracy effects. | Ablation | [Appendix B, Table 7 and adjacent text, p. 17](https://arxiv.org/pdf/2602.11988v3#page=17) | Direct for the tested categories, generated files and GPT-5.2. The edits can change both wording and expected work. |
| SRC-0020:C09 | CTXbench runs with other repository documentation stripped showed a reported average improvement of 2.7 points with generated files versus omission. | Modified-benchmark experiment | [Appendix B, Fig. 12, p. 16](https://arxiv.org/pdf/2602.11988v3#page=16) | Direct for the reported estimate. Claude Code was excluded and the result lacks a reported significance test. |
| SRC-0020:C10 | The authors advise omitting generated files under current methods and limiting human-written files to specific extra instructions beyond existing repository documentation. They call for evaluating changes claimed to improve performance. | Authors’ practitioner recommendation | [§1, p. 2](https://arxiv.org/pdf/2602.11988v3#page=2) · [§6, p. 9](https://arxiv.org/pdf/2602.11988v3#page=9) | Direct for the recommendation. This is an interpretation of benchmark and trace findings, with no measured universal rule budget. |

## Extractable practitioner insights

### AP-08 Obsessing over rules

**Symptom.** A team keeps appending standing rules after individual agent mistakes, then sees routine changes acquire extra setup, repository searches or test runs. **Authors’ advice.** Give the agent specific requirements it cannot already learn from existing documentation, and evaluate a change that promises to improve task completion. **Catalog adaptation.** Compare the existing file to an edited version on a small set of representative tasks with the same checkout, agent configuration and acceptance checks. Record test-based completion alongside the actual action or error the changed instruction targets and any additional steps. If a generic testing command triggers a large suite for a file-only edit, for example, compare a version that identifies the applicable check for that task class. Treat team time and required check coverage as separate measures if collecting them. The paper tested file packages and selected content ablations. Its evidence supports measuring the effect of guidance on work, with no evidence for declining compliance as rule count grows. Claims SRC-0020:C02–C05 and SRC-0020:C07–C10. [§§4.2–4.4, pp. 6–9](https://arxiv.org/pdf/2602.11988v3#page=6) · [Appendix B, pp. 16–17](https://arxiv.org/pdf/2602.11988v3#page=16)

### BP-09 Decision guards

**Symptom.** An agent repeatedly substitutes a conventional workflow for an unusual repository convention. **Supporting evidence.** Named tooling and commands can steer observable agent behavior. The authors recommend documenting requirements not already available to the agent. **Catalog adaptation.** If a specific repository decision keeps being reversed, state where it applies, point to its rationale, and verify the resulting behavior with an existing check or review. For example, a project could explain why its compatibility layer must preserve an existing interface and use its existing compatibility tests to review relevant changes. Cases involving an inline marker, preserved architectural rationale, or a guard plus an automated check were outside the experiment. BP-09 coverage is indirect. Claims SRC-0020:C05 and SRC-0020:C10. [§4.3, pp. 7–8](https://arxiv.org/pdf/2602.11988v3#page=7) · [§6, p. 9](https://arxiv.org/pdf/2602.11988v3#page=9)

## Related work, conflicts, and limitations

- [Claude Code best practices](SRC-0002--claude-code-best-practices.md) supplies practitioner guidance for maintaining an agent instruction file. This paper supplies independent benchmark and trace evidence about the effects of including one. Tool specificity has some experimental support here, while claims about a practical length limit require separate evidence.
- [The domain-modeling skill](SRC-0009--domain-language-and-decisions.md) describes writing down surprising or hard-to-reverse decisions as a practitioner method. The present paper’s tool-use observation complements that rationale while leaving preservation of counterintuitive code decisions an open empirical question.
- CTXbench is selected from open-source Python projects already using context files. SWE-bench Lite samples older, popular Python repositories. The authors identify heavily represented languages and toolchains as a possible reason for small effects. The task selection also favors changes with deterministic tests. Test success and inference cost leave maintainability, review effort, code efficiency, security and human–agent collaboration outside the main measures. The authors’ cutoff split in Appendix B yields no clear shift in the results and cannot fully determine prior exposure. [§§3 and 5](https://arxiv.org/pdf/2602.11988v3#page=3) · [Appendix B, Fig. 14, pp. 17–18](https://arxiv.org/pdf/2602.11988v3#page=17)

## Retrieval hints

- “Should I keep the generated `AGENTS.md` or `CLAUDE.md`?”
- “Our agents run more tools and spend more tokens after we add instructions.”
- “Will agents miss rules if we keep adding them?”
- “Which repository conventions should I specify explicitly and check in review?”
- Topics and tags include AP-08, BP-09, repository guidance, agent instruction files, inference expense and benchmark task resolution.

## Original article access and copyright/permission record

The versioned arXiv record links to Creative Commons Attribution 4.0 International and the v3 HTML displays that license. The license permits reuse with attribution under its terms. This dossier uses original analytical prose and selected numerical findings. No full text or original figures are reproduced. Appendix D separately describes licenses for benchmark assets, models and agents. [arXiv v3 record and license link](https://arxiv.org/abs/2602.11988v3) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · [Appendix D](https://arxiv.org/html/2602.11988v3#A4)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0020--verification.md)

## Drive navigation

- [audits/SRC-0020--verification.md](../audits/SRC-0020--verification.md) · [Local copy](../audits/SRC-0020--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/AP-08--obsessing-over-rules.md](../topics/AP-08--obsessing-over-rules.md) · [Local copy](../topics/AP-08--obsessing-over-rules.md)
- [topics/BP-06--context-management-discipline.md](../topics/BP-06--context-management-discipline.md) · [Local copy](../topics/BP-06--context-management-discipline.md)
- [topics/BP-09--decision-guards.md](../topics/BP-09--decision-guards.md) · [Local copy](../topics/BP-09--decision-guards.md)
- [topics/OB-04--selective-hearing.md](../topics/OB-04--selective-hearing.md) · [Local copy](../topics/OB-04--selective-hearing.md)
