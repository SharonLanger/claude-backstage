---
topic_id: BP-09
title: Decision guards
coverage: partially supported
publication_status: published
source_edges:
  - id: SRC-0009
    relationship: DIRECT
    strength: moderate
    finding: "Pocock documents short architecture decision records for choices that are costly to reverse, surprising and based on a real trade-off."
  - id: SRC-0002
    relationship: SUPPORTING
    strength: moderate
    finding: "Anthropic distinguishes path-scoped guidance about misleading conventions from enforced application controls."
  - id: SRC-0020
    relationship: SUPPORTING
    strength: moderate
    finding: "Repository context files influenced observed tool use, while resolution comparisons with file omission remained inconclusive."
pattern_ids: [PAT-0006]
---

# BP-09 Decision guards

## When it comes up

- “The agent keeps replacing this odd-looking code with the usual idiom, which breaks an old client.”
- “We have an architecture decision record. The assistant never opens it.”
- “Can a source comment protect this behavior, or do I need a failing test?”

The brief asks whether an explicit marker can protect a counterintuitive code decision from incidental reversal. There is direct practitioner documentation for recording the rationale, a separate case for scoped instructions and enforceable checks, and indirect evidence that repository guidance can change what agents do. The probability that a comment, ADR, linked test or particular combination prevents an unwanted edit has not been measured by these sources.

## What a marker can communicate

Pocock proposes recording decisions only when reversal would be costly, the choice would be surprising without context, and there was a meaningful trade-off. A short architecture decision record (ADR) states the context, choice and reason. The skill cross-references code, glossaries and committed ADRs. A linked user report describes a settled issue-tracker decision the workflow missed. The reporter added an instruction to search the tracker. This illustrates a discovery gap. It supplies no estimate of the protection conferred by the guidance. Pocock’s article, format file and skill definition describe one workflow, with the issue supplying a scoped user report. SRC-0009:C04 and SRC-0009:C05. [Domain-modeling dossier](../sources/SRC-0009--domain-language-and-decisions.md) · [ADR selection criteria](https://www.aihero.dev/skills-domain-modeling#two-artifacts-two-bars) · [Cross-referencing and its limits](https://www.aihero.dev/skills-domain-modeling#cross-referencing-and-where-it-stops) · [User report](https://github.com/mattpocock/skills/issues/717)

Anthropic’s product guide independently advises recording missing or misleading repository knowledge and scoping rules to where they apply. It describes application controls for hard constraints. A failed command can block completion through a Stop hook under the documented conditions, with a cap on repeated blocks. That is a feature of the execution path. A marker’s leverage comes from an editor finding and interpreting it, and a test’s leverage comes from what it exercises and where it is enforced. SRC-0002:C11–C14. [Claude Code dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Short guidance](https://code.claude.com/docs/en/best-practices#keep-claudemd-short) · [Path-scoped rules](https://code.claude.com/docs/en/best-practices#scope-rules-to-one-part-of-the-codebase) · [Enforcement controls](https://code.claude.com/docs/en/best-practices#deterministic-and-non-deterministic-instructions) · [Stop hook and cap](https://code.claude.com/docs/en/best-practices#enforce-the-check-with-a-stop-hook)

Gloaguen and colleagues measured issue-resolution attempts in Python repositories with and without context files. The traces show observable steering. For example, agents used the package tool uv much more often in instances where the context file named it. Developer-committed files outperformed generated files on CTXbench, but the improvement over omission was inconclusive. Context-file conditions increased inference cost. These findings temper any implication that steering toward a documented convention ensures a better patch. The study varied file packages as a whole and did not isolate a local marker or measure subsequent preservation of a decision. SRC-0020:C01–C05 and SRC-0020:C10. [Repository context file dossier](../sources/SRC-0020--repository-context-files.md) · [Resolution and cost, §4.2 and Tables 2–3](https://arxiv.org/pdf/2602.11988v3#page=6) · [Tool use, §4.3](https://arxiv.org/pdf/2602.11988v3#page=7)

## Applying it at the code boundary

[PAT-0006, Resolve a domain term before coding](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) covers the narrower action of surfacing and recording the decision when it affects behavior. For example, take a parser that accepts an irregular date format because supported archived exports still use it. Record the affected clients and the reason for the exception. A nearby reference to that record and a compatibility test for a representative archive are catalog adaptations. A reviewer can inspect both when a diff removes the exception. If the support commitment changes, the record gives an owner the context to revise the decision and its check together. [Pattern verification](../audits/PAT-0006--verification.md)

## Drive navigation

- [audits/PAT-0006--verification.md](../audits/PAT-0006--verification.md) · [Local copy](../audits/PAT-0006--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0009--verification.md](../audits/SRC-0009--verification.md) · [Local copy](../audits/SRC-0009--verification.md)
- [audits/SRC-0020--verification.md](../audits/SRC-0020--verification.md) · [Local copy](../audits/SRC-0020--verification.md)
- [patterns/PAT-0006--resolve-a-domain-term-before-coding.md](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md) · [Local copy](../patterns/PAT-0006--resolve-a-domain-term-before-coding.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0009--domain-language-and-decisions.md](../sources/SRC-0009--domain-language-and-decisions.md) · [Local copy](../sources/SRC-0009--domain-language-and-decisions.md)
- [sources/SRC-0020--repository-context-files.md](../sources/SRC-0020--repository-context-files.md) · [Local copy](../sources/SRC-0020--repository-context-files.md)
