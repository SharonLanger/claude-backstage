---
pattern_id: PAT-0007
status: accepted
name: "Ask for an assessment before naming a fix"
type: diagnostic
families: [debugging, collaboration, reliability]
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
topic_ids: [AP-03, BP-02, OB-02]
symptoms: ["My assistant immediately agrees with my diagnosis", "I asked whether to change the cache and got a cache patch before anyone reproduced the bug", "I want a second assessment but my question already contains my answer"]
source_ids: [SRC-0013, SRC-0005, SRC-0002]
review: PASS
publication_status: published
---

# Ask for an assessment before naming a fix

## When users need this

A developer wants help locating a fault but opens with “How should we invalidate the cache?” That is a reasonable implementation question once the fault has been traced to the cache. While the cause is open, the same wording silently assigns a component and a remedy. An assistant can produce a persuasive answer to the question it received while the original failure remains unexplained.

## Context and prerequisites

Use this when more than one explanation could fit the observations and the developer still owns the choice of fix. Bring the expected behavior, the observed behavior, the relevant code or logs, and any constraints on changes. A failing example is especially helpful. If you have only a report, the first output can be a request for the missing observation. If a decision is binding, identify it plainly so the assistant can work within it.

## Core principle

Give the assistant the same evidence you would hand a colleague for a second assessment. Reserve an untested conclusion for comparison after the first assessment. The next observation should help decide whether either account explains the failure.

## How to work this way

1. **Separate the observation from the proposed cause.** Write down the expected result, actual result, reproduction conditions, and hard constraints. Keep every pertinent observation, including ones that favor your hypothesis. For example, a trace showing a cache hit belongs in the request even if you privately suspect the cache. Mark which decisions are still open. [Evidence 1](#evidence-and-provenance)
2. **Ask for an assessment before edits.** Ask which part of the system could produce the observed difference, what evidence supports that explanation, and what you could inspect to distinguish it from a credible alternative. If the evidence already singles out a cause, a direct check suffices. A question mark alone leaves the proposed answer in play when the question still starts “Should we fix this by …?” [Evidence 2](#evidence-and-provenance)
3. **Compare your hypothesis with the assessment.** Share your proposed cause explicitly as a hypothesis, together with any new evidence. Identify a result the competing accounts predict differently. If neither account has a discriminating prediction, ask what trace, input, or component boundary would supply one. Agreement, disagreement, and a change of mind each leave the engineering question open. [Evidence 3](#evidence-and-provenance)
4. **Run the check and decide the scope of the change.** Record the command or probe and the observed result. Choose a fix consistent with both that result and the original constraints. Re-run the failing case and a case that already worked. If the check cannot distinguish the accounts, record the open question and collect the missing evidence before editing. [Evidence 4](#evidence-and-provenance)

## Concrete example

**Original, runnable diagnostic case.** An order listing that ordinarily shows IDs 1 and 3 comes back empty after an import. ID 2 has a cancellation. The import also stores unmatched cancellation events with a nullable order ID. The contract requires retaining those events, and a cancellation excludes an order only when their IDs match. The developer suspects an empty result cached during the import. That suspicion is a reason to inspect two layers, while the timing, schema and contract are facts worth sharing immediately.

A first request could read, “The listing returned 1 and 3 before the import and nothing afterward. Order 2 is cancelled. Here are the listing query, the fixture and the rule for unmatched events. Where can rows disappear, and what observation would locate the failure? Please assess before editing.” After the assessment the developer adds, “I suspected a stale cached result. If the raw query already returns no rows on the imported fixture, the query alone can account for the symptom. If it returns 1 and 3 but the endpoint returns nothing, we need to inspect the layers above it.”

Run the following with Python 3 in a disposable in-memory SQLite database. The first query reproduces the listing, and the second tests a proposed change. Both see identical data in each comparison.

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE orders (id INTEGER PRIMARY KEY);
CREATE TABLE cancellations (order_id INTEGER);
INSERT INTO orders VALUES (1), (2), (3);
INSERT INTO cancellations VALUES (2);
""")
before = """SELECT id FROM orders WHERE id NOT IN
    (SELECT order_id FROM cancellations) ORDER BY id"""
after = """SELECT id FROM orders o WHERE NOT EXISTS
    (SELECT 1 FROM cancellations c WHERE c.order_id = o.id) ORDER BY id"""

def ids(query):
    return [row[0] for row in db.execute(query)]

print("linked event:", ids(before), ids(after))
db.execute("INSERT INTO cancellations VALUES (NULL)")
print("unmatched event added:", ids(before), ids(after))
```

Observed output:

```text
linked event: [1, 3] [1, 3]
unmatched event added: [] [1, 3]
```

For IDs 1 and 3, membership in a list containing 2 and NULL yields SQL's unknown truth value. Negating it still yields unknown, so the filter discards both rows. The revised query tests for the absence of a matching cancellation and preserves the unmatched event. This localizes a sufficient cause in the fixture and gives the developer a narrow query change to review. An endpoint regression test against the deployed database engine would be the next check in a real repository. The example establishes the SQL behavior. It supplies no comparison of assistant responses or evidence of a production cache defect.

## Evidence and provenance

| Step | Accepted claims and original pinpoint | What was observed or recommended | Our coding adaptation |
|---|---|---|---|
| 1. Preserve observations, requirements and open decisions | SRC-0002:C06, [Anthropic, “Write a specific prompt,” fix and exploration examples](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt). SRC-0013:C08–C09, [Dubois et al., §3, pp. 9–11](https://arxiv.org/pdf/2602.23971v4#page=10) and [Appendix D, Table 5](https://arxiv.org/pdf/2602.23971v4#page=22) | The guide recommends identifying the location, symptom and success condition for a fix. The paper discusses meaning preservation, and its appendix illustrates possible polarity changes in rewritten questions. | Keep the trace, reproduction, contract and fixed design decisions in view while removing the developer's unsupported conclusion. This editorial distinction is ours. |
| 2. Start with an open assessment | SRC-0013:C02, SRC-0013:C04, [Dubois et al., §§2.1–2.2, Figs. 1–2, pp. 4–6](https://arxiv.org/pdf/2602.23971v4#page=4). SRC-0005:C05, [Sharma et al., §3.3, Fig. 3](https://arxiv.org/pdf/2310.13548v4#page=5) | On subjective advisory items, questions elicited lower expressed-sycophancy scores than matched statements. Reframing statements as questions also lowered these rubric scores. Separately, suggesting a wrong answer reduced accuracy on the reported aggregate of two factual QA datasets. | Leaving the proposed fix out of the first request goes beyond a grammatical rewrite. Asking for evidence, a plausible rival and an assessment before edits is our debugging protocol. Neither study measured the number of technical alternatives considered. |
| 3. Compare predictions when reintroducing the hypothesis | SRC-0005:C03, SRC-0005:C05, [Sharma et al., §§3.2–3.3, Figs. 2–3](https://arxiv.org/pdf/2310.13548v4#page=4). SRC-0002:C07, [Anthropic, “Give Claude a check to run,” opening examples](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) | In the challenge experiment an unsupported challenge could turn a correct answer into an incorrect one. The QA suggestion experiment manipulated the initial prompt. Vendor guidance calls for an observable check. | Sharing the developer's hypothesis in a second turn and deriving different predictions is our synthesis. The experiments did not compare this sequence with presenting both explanations initially. |
| 4. Verify independently and constrain the patch | SRC-0002:C07, SRC-0002:C08, [Anthropic, “Give Claude a check to run,” examples and evidence request](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run). SRC-0002:C10, [“Review against your spec,” review prompt](https://code.claude.com/docs/en/best-practices#review-against-your-spec) | This practitioner guide recommends an interpretable check, its execution evidence and review against the specification and edge cases. | We apply it at a component boundary, preserve an already-working case, and defer a patch when the probe cannot identify a relevant change. The guide offers no measured effect size. |

## Different source perspectives

Dubois and colleagues cite Sharma and colleagues. Their new advisory data and grading rubric give separate experimental evidence on expressed agreement. Dubois's political-persona experiment measured selection between two fixed choices, with 59.9% persona alignment for questions and 64.6% for statements in GPT-5. These choices carry no factual answer key. The advisory experiment's stronger effect for stated conviction also did not carry over cleanly to certainty wording in the persona experiment. The political benchmark draws on earlier work with some authors in common with Sharma. Treat the two experiments inside Dubois as parts of one publication. [SRC-0013:C03, SRC-0013:C07, §2.5 and Fig. 5](https://arxiv.org/pdf/2602.23971v4#page=9)

Sharma's factual QA comparisons did score correctness, including when a proposed answer was embedded in an existing question. That gives a separate reason to examine the content of the prompt. Anthropic's guide supplies the engineering verification practice. It is vendor advice, and Sharma's research team also includes Anthropic researchers. None of the three measures whether an open diagnosis produces a better-scoped or more correct repository patch. [Sharma et al., §3.3 and Fig. 3](https://arxiv.org/pdf/2310.13548v4#page=5) · [Anthropic guide](https://code.claude.com/docs/en/best-practices)

## Tradeoffs, failure modes and when to skip it

An extra assessment takes time. If a verified defect already explains the reproduction and the requested fix is approved, give the assistant the diagnosis, evidence and implementation constraints directly. Withholding logs, customer requirements, a known incident timeline or the sole reliable clue can make a nominally open request under-specified. A list of possibilities has little value if its entries all predict the same observation. Seek the smallest check that changes the decision. A passing fixture establishes only the behavior it exercises.

## Variations and practical adaptations

For an explicit review of a proposed fix, name it from the outset and ask which observed cases it explains, which case would refute it and which contract it could break. If the code or environment is unavailable, ask for the specific missing observation that would separate two explanations and leave the patch decision open. These variants are our adaptations for different user goals.

## Related patterns, topics and families

AP-03 (answer injection) is the workflow trigger. OB-02 (compliance bias) describes susceptibility to a stated view. BP-02 (active partnership) enters through comparing the developer's and assistant's predictions. If the team has already moved on to comparing implementations with a shared check, use [PAT-0004, Compare repair with fresh candidates](PAT-0004--compare-repair-with-fresh-candidates.md).

## Sources and verification

- Magda Dubois, Cozmin Ududec, Christopher Summerfield and Lennart Luettgau, *Ask don't tell: Reducing sycophancy in large language models*, arXiv v4, July 29, 2026. [Dossier](../sources/SRC-0013--ask-without-supplying-the-answer.md) · [Original](https://arxiv.org/html/2602.23971v4) · [Source audit](../audits/SRC-0013--verification.md)
- Mrinank Sharma and colleagues, *Towards Understanding Sycophancy in Language Models*, ICLR 2024, updated manuscript v4, May 10, 2025. [Dossier](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Original](https://arxiv.org/html/2310.13548v4) · [Source audit](../audits/SRC-0005--verification.md)
- Anthropic, *Best practices for Claude Code*, living documentation, accessed November 21, 2026. [Dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Original](https://code.claude.com/docs/en/best-practices) · [Source audit](../audits/SRC-0002--verification.md)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/PAT-0007--verification.md)

## Drive navigation

- [audits/PAT-0007--verification.md](../audits/PAT-0007--verification.md) · [Local copy](../audits/PAT-0007--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0005--verification.md](../audits/SRC-0005--verification.md) · [Local copy](../audits/SRC-0005--verification.md)
- [audits/SRC-0013--verification.md](../audits/SRC-0013--verification.md) · [Local copy](../audits/SRC-0013--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0005--sycophancy-and-user-beliefs.md](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Local copy](../sources/SRC-0005--sycophancy-and-user-beliefs.md)
- [sources/SRC-0013--ask-without-supplying-the-answer.md](../sources/SRC-0013--ask-without-supplying-the-answer.md) · [Local copy](../sources/SRC-0013--ask-without-supplying-the-answer.md)
- [topics/AP-03--answer-injection.md](../topics/AP-03--answer-injection.md) · [Local copy](../topics/AP-03--answer-injection.md)
- [topics/BP-02--active-partnership.md](../topics/BP-02--active-partnership.md) · [Local copy](../topics/BP-02--active-partnership.md)
- [topics/OB-02--compliance-bias-sycophancy.md](../topics/OB-02--compliance-bias-sycophancy.md) · [Local copy](../topics/OB-02--compliance-bias-sycophancy.md)
