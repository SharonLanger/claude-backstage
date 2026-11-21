---
pattern_id: PAT-0004
status: accepted
name: "Compare repair with fresh candidates"
type: workflow
families: [reliability, debugging, code-review]
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
topic_ids: [AP-01, BP-03, BP-04, BP-08, OB-06, OB-07]
symptoms: ["Should I spend the next attempt repairing this implementation or asking for another one?", "Two plausible implementations disagree on an edge case", "The assistant can explain its patch, but I still need to know which version to keep"]
source_ids: [SRC-0008, SRC-0003, SRC-0002, SRC-0019]
review: PASS
publication_status: published
---

# Compare repair with fresh candidates

## When users need this

A small implementation fails a reproducible case. You could give the assistant that failure and ask for a repair, or give it the original specification and ask for another implementation. The practical question is which candidate earns review within the time you have. A repair that passes is useful, but its success alone tells you little about whether spending the same budget on fresh candidates would usually work better.

## Context and prerequisites

Use this for a bounded change with an agreed contract, a common starting revision, and checks that a developer controls and can apply to every candidate. A pure function, parser rule or command with deterministic output is a good fit. Know which adjacent behavior the change must preserve. When the product decision itself is open, settle it with the person responsible before generating more code.

## Core principle

Treat the existing implementation as one candidate. Spend the next attempt on information you can use. A reproducible failure can guide a repair. A fresh attempt can explore the same contract without inheriting the failed code. Use a common test to eliminate candidates and a review of the surviving diff to decide what to keep.

## How to work this way

1. **Fix the contract and the check.** Write down an input that fails, its expected result and where that expectation comes from. Run the check on the existing attempt. Include a case that already works. Keep the checks under the reviewer's control so each candidate faces the same requirements. If the expected answer is disputed, pause here. [Evidence 1 and 5](#evidence-for-the-decisions)
2. **Set a budget and a baseline.** For example, after the failed implementation allow two more generated programs. A mixed allocation buys one repaired and one fresh candidate. A fresh-only alternative buys two fresh candidates. Each has the same two-program ceiling. If you intend to compare the policies empirically, apply both to comparable problems and record actual resource use. Trying the mixed allocation on one task lets you choose a patch for that task. It supplies no estimate of the other policy's success rate. Count diagnosis time, execution, and review separately when they matter to your decision. [Evidence 2 and 3](#evidence-for-the-decisions)
3. **Give each attempt the appropriate evidence.** Give a repair attempt the original contract, failed implementation, failing input and observed versus expected result. Add a diagnosis if you can substantiate it. Give the fresh attempt the same contract, starting revision and relevant interfaces, with the failed solution and its diagnosis omitted. Keep each candidate's edits separate. If only one attempt remains, use repair when the failure identifies a specific fix you can verify, or use a fresh attempt when you lack a defensible diagnosis and the task is cheap to reconstruct. This last choice is a judgment call. [Evidence 3 and 4](#evidence-for-the-decisions)
4. **Select, review or stop.** Run the same checks on each candidate. A passing result qualifies the diff for review. Read it against the complete contract, including untested edge cases, compatibility and the scope of the change. If two pass, decide on a requirement that matters to the project, record why, and add a distinguishing case if behavior differs. If candidates disagree, use their first differing input to ask what the contract requires. Agreement can also hide a shared bug. If neither passes at the cap, inspect the failures or seek a human diagnosis before spending more. A flaw in the check invalidates the comparison. Correct it against the agreed requirement and rerun it on every candidate. [Evidence 1, 4, 5 and 6](#evidence-for-the-decisions)

## Concrete example

**Original worked exercise.** An invoicing service needs a pure Python function that allocates a nonnegative integer number of cents among a positive integer number of recipients. Shares must sum to the input, differ by at most one cent, and assign larger shares to the earliest recipients. The signed-off example for two cents across four recipients is therefore `[1, 1, 0, 0]`. A first attempt returns `[0, 0, 0, 0]` because it repeats the integer quotient and discards the remainder.

Allow two additional programs. The repair prompt includes the failing example, actual result and the observation that floor division lost the remainder. The fresh prompt includes the same behavioral contract and function signature. Imagine the repair puts the whole remainder on the first recipient, while the fresh candidate distributes one cent at a time across the earliest recipients. Run this original exercise with Python 3 to see which cases distinguish them.

```python
def repair(cents, recipients):
    base, extra = divmod(cents, recipients)
    return [base + extra] + [base] * (recipients - 1)


def fresh(cents, recipients):
    base, extra = divmod(cents, recipients)
    return [base + 1] * extra + [base] * (recipients - extra)


cases = [
    (6, 3, [2, 2, 2]),      # already worked in the initial attempt
    (5, 2, [3, 2]),         # both candidates preserve the total
    (2, 4, [1, 1, 0, 0]),   # the approved example distinguishes them
    (0, 2, [0, 0]),
]
for candidate in (repair, fresh):
    failures = []
    for cents, recipients, expected in cases:
        actual = candidate(cents, recipients)
        if actual != expected:
            failures.append((cents, recipients, actual, expected))
    print(candidate.__name__, failures)
```

The output is `repair [(2, 4, [2, 0, 0, 0], [1, 1, 0, 0])]` and `fresh []`. A check that looked only at the total would have accepted both. In reviewing the survivor, the developer can see that `divmod` yields a remainder smaller than the recipient count. The function emits exactly that many larger shares first and fills the remaining positions with the quotient. This argument covers all inputs in the stated domain. The reviewer still needs to check that the caller supplies recipients in the promised order. If the business owner actually intends to prioritize the *last* recipients, both the written requirement and the test need correction before either candidate can be selected.

## Evidence for the decisions

| Decision | Claim IDs and original locations | Evidence and adaptation |
|---|---|---|
| 1. Establish an external check and qualify survivors | SRC-0008:C01, SRC-0008:C02, SRC-0008:C11. [Olausson et al., §§2–3.2, pp. 2–5](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=3) · [§5, p. 9](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=9) | Experimental setup and limitation. The evaluator can run the full benchmark suite, use failures in repair, and recognize a passing program. A separate private suite was not required. Our safeguards are to establish who decides expected behavior, retain an already-working case, and rerun all candidates if the check changes. |
| 2. Compare equal caps and account for costs | SRC-0008:C02, SRC-0008:C05, SRC-0008:C06, SRC-0008:C07. [§§3.2–4.1 and Fig. 3b, pp. 4–6](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=6) · [App. A, algorithms and figures, pp. 13–17](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=13) | Comparative experiment. On APPS with GPT-4, ten starting draws with one repair each scored 66.1% versus 63.1% fresh-only at a cap of 20 programs. Two starting draws with ten sibling repairs each scored 61.8% versus 63.4% fresh-only at a cap of 22. Each comparison has its own matched cap. Token accounting and stopping rules affect the tradeoff. Our two-program example and review-time budget are local choices. |
| 3. Include a fresh alternative | SRC-0008:C01, SRC-0008:C06 and SRC-0003:C02, SRC-0003:C06, SRC-0003:C08, SRC-0003:C11. [Olausson et al., §3.1 and Figs. 2–5, pp. 3–7](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=4) · [Publisher PDF, Table 2](https://www.nature.com/articles/s41598-025-27846-5.pdf?code=7b2&error=cookies_not_supported#page=6) · [Adnan and Kuhn, RQ3 and debugging protocol, pp. 4–5](https://www.nature.com/articles/s41598-025-27846-5) · [Table 2, baseline and both restart columns](https://www.nature.com/articles/s41598-025-27846-5/tables/2) | Two benchmark designs. In the second, one scheduled spec-only restart within six attempts improved final solve rate for all nine configurations at the later schedule. Two configurations did worse at the earlier one. Separate copies of the same repository base, the symptom-based choice for a final attempt, and the decision to stop at a local cap are our adaptations. |
| 4. Ground a repair in observed failure and scrutinize the diagnosis | [Appendix D, p. 24](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=24) · SRC-0008:C01, SRC-0008:C09, SRC-0008:C10. [§3.1, Figs. 1–2](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=3) · [§4.3, Table 1, pp. 8–9](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=8) | Direct experimental design and sampled outcomes. For the same 40 failing GPT-4 programs on 20 APPS tasks, 52.60% of repairs passed with human diagnoses versus 33.30% with GPT-4 diagnoses. Participants had access to model explanations. The unit is a repaired program. This does not measure human selection among candidates. Checking a diagnosis against observed behavior before spending a repair is our adaptation. |
| 5. Review behavior that the check cannot settle | SRC-0002:C07, SRC-0002:C08, SRC-0002:C10 and SRC-0008:C02, SRC-0008:C11. [Anthropic, “Give Claude a check to run,” examples and evidence request](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [“Review against your spec,” review prompt](https://code.claude.com/docs/en/best-practices#review-against-your-spec) · [Olausson et al., §5, p. 9](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf#page=9) | Practitioner guidance supports executable checks and reviewing a diff against its spec and edge cases. The benchmark authors identify limits of the test-based setup. Our human sign-off, tie decision, and rule for an ambiguous or incorrect expectation apply those limits to a repository. |
| 6. Test concrete disagreements and check shared answers | SRC-0019:C01, SRC-0019:C02, SRC-0019:C03, SRC-0019:C05, SRC-0019:C08. [Ouyang et al., §§3.2–3.4.1, procedure and measures](https://kclpure.kcl.ac.uk/ws/files/365277933/An_Empirical_Study_of_the_Non-Determinism_of_ChatGPT_in_Code_Generation_Version_of_Record.pdf#page=7) · [§4.1.1, Table 2 and Figs. 2–3](https://kclpure.kcl.ac.uk/ws/files/365277933/An_Empirical_Study_of_the_Non-Determinism_of_ChatGPT_in_Code_Generation_Version_of_Record.pdf#page=11) · [§4.3, Table 6, request grouping](https://kclpure.kcl.ac.uk/ws/files/365277933/An_Empirical_Study_of_the_Non-Determinism_of_ChatGPT_in_Code_Generation_Version_of_Record.pdf#page=16) · [§7.2, best-of-five selection and shared errors](https://kclpure.kcl.ac.uk/ws/files/365277933/An_Empirical_Study_of_the_Non-Determinism_of_ChatGPT_in_Code_Generation_Version_of_Record.pdf#page=25) | Repeated-call experiment. Five identical requests to GPT-3.5 Turbo at temperature one yielded both a zero-pass and an all-pass program on 39.63% of HumanEval problems. The study identified higher-scoring candidates retrospectively using the tests and found recurring error types in groups where all candidates failed. Our adaptation is to resolve disagreement against a stated requirement and check a shared answer with an external example. |

## Different source perspectives

Olausson and colleagues compared independent starting draws and sibling repairs conditioned on a particular failure. Adnan and Kuhn tested sequential repairs, with a fresh generation substituted at a scheduled attempt. The papers have different investigators and protocols but share HumanEval. Ouyang and colleagues also used HumanEval and APPS, alongside CodeContests. They measured how programs from repeated calls behaved on the same tests. Their request-grouping comparison varied how five candidates were requested. Concurrent versus sequential developer work and the return on engineer time were outside its design. Separate requests can share a failure mode. Their number alone cannot support a calculation that assumes each candidate has an independent chance of correctness. [Evidence 6](#evidence-for-the-decisions) Adnan and Kuhn's restart changes both the available history and what the model is asked to generate, so improvements cannot identify which change mattered. Anthropic's guidance concerns working developers and supplies no comparative estimate of repair versus regeneration.

A fresh-only benchmark's **pass@k** measures the chance that at least one of up to *k* sampled programs passes the test suite. It does not tell you whether a reviewer will select a correct change when the suite is incomplete, whether two passing changes are equally maintainable, or whether simultaneous generation saves developer time. The human participants in Olausson et al. supplied failure diagnoses. The paper did not test a human choosing the best patch in a pile of passing proposals. [Evidence 1, 2 and 4](#evidence-for-the-decisions)

## Tradeoffs and variations

- **An expensive check or a long diff.** Generate and check one candidate at a time. Stop when a candidate clears the tests and a reviewer can accept the change. If elapsed time is scarce and checks are cheap, prepare candidates concurrently on separate copies of the baseline. Measure time to an accepted result and reviewer effort if you need to assess the value of concurrency. This scheduling choice and measurement are our adaptations. Both generation and review consume the budget. [Evidence 2, 5 and 6](#evidence-for-the-decisions)
- **An uncertain diagnosis.** An assistant can propose one explanation and a prediction for a new input. Run it. A wrong prediction is grounds to discard the explanation. This optional feedback exercise adapts the study's use of observed failures. The paper does not isolate a benefit from simply assigning the same model an evaluator role. [Evidence 4](#evidence-for-the-decisions)
- **A weak or missing oracle.** A requirement such as “make the search feel better” leaves no reliable winner. First collect examples and get the owner to judge the desired behavior. For performance, use a representative workload and a defined measurement. Generating candidates while acceptance remains disputed adds alternatives without resolving the disagreement. These are our applications of the benchmark's dependence on trusted checks. [Evidence 1 and 5](#evidence-for-the-decisions)

## Related patterns and topics

Use this entry for a choice among **implementations**. Use PAT-0001 when a continuing conversation repeatedly loses a known requirement and the developer needs to preserve or recover its working state. A single conversation can remain well oriented while producing several wrong implementations. [PAT-0001 · Recover a drifting coding session](PAT-0001--recover-a-drifting-coding-session.md)

BP-08 is the closest topic. BP-04 concerns the narrower role of feedback after an observed failure. BP-03 and AP-01 concern deciding whether to spend another attempt on an existing implementation. OB-06 has direct evidence for behavioral variation across repeated requests with fixed wording in the configurations tested by Ouyang and colleagues. The studies did not measure psychological sunk cost in developers or establish a universal retry count.

## Sources

- Theo X. Olausson, Jeevana Priya Inala, Chenglong Wang, Jianfeng Gao and Armando Solar-Lezama, “Is Self-Repair a Silver Bullet for Code Generation?” ICLR 2024. [SRC-0008](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Independent source audit](../audits/SRC-0008--verification.md) · [Conference paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- Muntasir Adnan and Carlos C. N. Kuhn, “Measuring and mitigating debugging effectiveness decay in code language models.” Scientific Reports, December 18, 2025. [SRC-0003](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Independent source audit](../audits/SRC-0003--verification.md) · [Publisher paper](https://www.nature.com/articles/s41598-025-27846-5)
- Anthropic, “Best practices for Claude Code.” Living product guide, accessed November 21, 2026. [SRC-0002](../sources/SRC-0002--claude-code-best-practices.md) · [Independent source audit](../audits/SRC-0002--verification.md) · [Product guide](https://code.claude.com/docs/en/best-practices)

- Shuyin Ouyang, Jie M. Zhang, Mark Harman and Meng Wang, “An Empirical Study of the Non-Determinism of ChatGPT in Code Generation.” ACM Transactions on Software Engineering and Methodology, January 22, 2025. [SRC-0019](../sources/SRC-0019--repeatability-of-code-generation.md) · [Independent source audit](../audits/SRC-0019--verification.md) · [ACM version of record](https://kclpure.kcl.ac.uk/ws/files/365277933/An_Empirical_Study_of_the_Non-Determinism_of_ChatGPT_in_Code_Generation_Version_of_Record.pdf)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/PAT-0004--verification.md)

## Drive navigation

- [audits/PAT-0004--verification.md](../audits/PAT-0004--verification.md) · [Local copy](../audits/PAT-0004--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0003--verification.md](../audits/SRC-0003--verification.md) · [Local copy](../audits/SRC-0003--verification.md)
- [audits/SRC-0008--verification.md](../audits/SRC-0008--verification.md) · [Local copy](../audits/SRC-0008--verification.md)
- [audits/SRC-0019--verification.md](../audits/SRC-0019--verification.md) · [Local copy](../audits/SRC-0019--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0003--debugging-effectiveness-decay.md](../sources/SRC-0003--debugging-effectiveness-decay.md) · [Local copy](../sources/SRC-0003--debugging-effectiveness-decay.md)
- [sources/SRC-0008--self-repair-versus-fresh-samples.md](../sources/SRC-0008--self-repair-versus-fresh-samples.md) · [Local copy](../sources/SRC-0008--self-repair-versus-fresh-samples.md)
- [sources/SRC-0019--repeatability-of-code-generation.md](../sources/SRC-0019--repeatability-of-code-generation.md) · [Local copy](../sources/SRC-0019--repeatability-of-code-generation.md)
- [topics/AP-01--sunk-cost-over-iteration.md](../topics/AP-01--sunk-cost-over-iteration.md) · [Local copy](../topics/AP-01--sunk-cost-over-iteration.md)
- [topics/BP-03--happy-to-delete-start-fresh.md](../topics/BP-03--happy-to-delete-start-fresh.md) · [Local copy](../topics/BP-03--happy-to-delete-start-fresh.md)
- [topics/BP-04--feedback-flip.md](../topics/BP-04--feedback-flip.md) · [Local copy](../topics/BP-04--feedback-flip.md)
- [topics/BP-08--parallel-implementations.md](../topics/BP-08--parallel-implementations.md) · [Local copy](../topics/BP-08--parallel-implementations.md)
- [topics/OB-06--non-determinism.md](../topics/OB-06--non-determinism.md) · [Local copy](../topics/OB-06--non-determinism.md)
- [topics/OB-07--solution-fixation.md](../topics/OB-07--solution-fixation.md) · [Local copy](../topics/OB-07--solution-fixation.md)
