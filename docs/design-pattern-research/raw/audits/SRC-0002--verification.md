---
source_id: SRC-0002
artifact_type: independent_source_verification
reviewed: 2026-11-21
verdict: PASS
claims_checked: 17
corrections_required: 0
---
# Independent verification of SRC-0002

**PASS.** All 17 ledger claims are supported at their named locations. They document a vendor’s advice or its description of product behavior. No effectiveness estimate is available. [Source dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Original guide](https://code.claude.com/docs/en/best-practices)

## Numbered findings

1. **Provenance.** I independently opened the canonical HTML before receiving the dossier, then reopened the publisher’s Markdown and the legacy URL. The legacy URL redirected to the cited HTML. The heading and publisher match. I found no named author, displayed revision date, or article version. The access date identifies the reading of a changing document. The guide was freely readable. [Canonical page](https://code.claude.com/docs/en/best-practices) · [Publisher Markdown](https://code.claude.com/docs/en/best-practices.md) · [Redirecting address](https://docs.anthropic.com/en/docs/claude-code/best-practices)

2. **Claim checks.** I compared each ledger proposition and caveat against the page. The following pointers identify the passages used. Numbered line spans are positions in the HTML text rendering on the access date.

| Claim | Check against original | Result |
|---|---|---|
| SRC-0002:C01 | The first cost-management bullet at lines 435–439 names switching tasks as a reason to clear. | Pass |
| SRC-0002:C02 | The next bullet gives a focused summary example and identifies its processing cost. | Pass |
| SRC-0002:C03 | Lines 441–448 use two unsuccessful attempts to correct the same problem as a practical stopping point. The dossier preserves the heuristic’s status. | Pass |
| SRC-0002:C04 | Lines 446–449 describe separate choices for conversation and files. File recovery covers edits made with the main conversation’s file tools. “Tracked” in the dossier refers to those checkpoints, irrespective of Git tracking. | Pass |
| SRC-0002:C05 | The example at lines 183–189 persists the product decisions before switching to a clean implementation session. | Pass |
| SRC-0002:C06 | Lines 165–182 distinguish a specified fix from an intentionally open-ended exploration. | Pass |
| SRC-0002:C07 | Lines 253–264 offer several observable completion checks, including a screenshot requiring interpretation. | Pass |
| SRC-0002:C08 | Line 269 requests evidence of execution and explicitly allows visual evidence. | Pass |
| SRC-0002:C09 | Line 268 describes fresh context for the terminal review command. The dossier separately addresses shared assumptions. | Pass |
| SRC-0002:C10 | Lines 271–277 specify review against requirements, edge-case test coverage, and findings that affect correctness. | Pass |
| SRC-0002:C11 | Lines 278–295 show exit code 2 and explain the repeated-block exception when there is no intervening tool call. | Pass |
| SRC-0002:C12 | Lines 134–152 and 296–307 distinguish model instructions and application controls, including model-judged hooks. The dossier limits enforcement to the relevant operation and control. | Pass |
| SRC-0002:C13 | Lines 190–217 give concrete cases for inclusion in persistent guidance, including misleading legacy examples. | Pass |
| SRC-0002:C14 | Lines 218–235 separate path-triggered rules from skills whose full procedure can be loaded on use. | Pass |
| SRC-0002:C15 | Lines 404–420 describe moving noisy tasks or reviews to another context, its extra requests, and possible repeated exploration. | Pass |
| SRC-0002:C16 | Lines 451–460 identify five readiness questions for unattended work, including bounds and human approval. | Pass |
| SRC-0002:C17 | The first comparison row at lines 503–509 revises older guidance while retaining a role for clearing between tasks. | Pass |

3. **Evidence and topic scope.** The dossier treats the interview and written spec as examples for BP-01 and BP-02, focused history as guidance for BP-06, and steering as advice relevant to AP-01 and part of BP-03. AP-02 and AP-08 have direct practical guidance. AP-09, OB-01, OB-04, OB-10, and BP-09 have explicit limits. In particular, the page offers ways to surface assumptions but supplies no experiment on accepting contradictions. The parallel-session example supplies no comparison among candidate implementations. The source cannot establish a long-context performance curve. Its superseded-advice table is important when using it alongside experimental work.

4. **Originality and reuse.** The analytical prose and import example are independent explanations. Section names, product commands, filenames, and short technical expressions function as locators. The dossier reproduces no substantive prompt, code sample, or extended passage. I found no article-specific whole-text reuse grant on the guide. The recorded rights status is appropriate.

5. **Disposition.** No claim repairs or re-review are required. I reviewed the living document as published and did not test command behavior or independently measure outcomes. The orchestrator can record acceptance and attach reciprocal identifiers as reviewed patterns become available.

## Drive navigation

- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
