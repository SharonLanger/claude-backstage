# Verify an unfamiliar API call

## Purpose

Check a generated dependency call against the interface and behavior the project actually uses.

## When to use this guide

- A method is missing, an argument is rejected, or a real call produces the wrong kind of result.
- The agent keeps guessing library details after corrections.

You need the package version, receiver type, and matching documentation, installed types, help, or source. Running a behavior check requires a suitable local or integration environment. No custom harness is required.

## Quick tip

Ask: “Verify this call against our installed version: does it exist, do these arguments fit, and does its result mean what this feature needs? Show the reference and the smallest useful check.” A mock that returns the assumed answer does not verify the real dependency.

## Guide content

1. State the intended effect: input, affected resource, and observable result. Find the first call on which the rest of the patch depends.
2. Establish the installed version and concrete receiver. Read that version's operation description and signature. Resolve mismatches between published docs and the installed interface before patching.
3. Check arguments and the return contract. Inspect downstream field access and error handling for assumptions inherited from the same mistake. Give the agent the relevant reference passage rather than unrelated documentation.
4. Exercise a case that distinguishes the intended operation from a plausible wrong one. Record what ran and what it returned. Separate static verification from any untested service behavior.

**Original illustration:** An archive feature needs a member's metadata, but the proposed call returns its contents. A real method name and valid filename are insufficient. Check the metadata operation, assert a known member's size, and check the missing-member outcome before reviewing the caller.

## Limits

These steps are a practitioner adaptation of research method PAT-0002. They do not establish that the surrounding application is correct. If the interface is already verified and the failure is in application logic, investigate that logic instead. Persist only checked, version-scoped corrections; this guide does not provide automatic memory across sessions.

## Related patterns

- [Just-in-Time Retrieval](../../E-context-engineering/patterns/just-in-time-retrieval.md) — obtain the specific reference needed.
- [Executable Feedback Loop](../../F-harness-environment/patterns/F03-executable-feedback-loop.md) — make checks available to an agent.
- [Review Pass](../patterns/D05-review-pass.md) — inspect the complete change and its tests.

## Sources

- Nihal Jain et al. — [On Mitigating Code LLM Hallucinations with API Documentation](https://arxiv.org/html/2407.09726v1), 2024 preprint, §2.3, §3, Appendix A.5–A.6. The cloud-API benchmark distinguishes nonexistent operations, wrong existing operations, and invalid arguments. Retrieval quality affects validity; unrelated documentation can hurt. This does not evaluate our manual version-checking workflow.
- Anthropic — [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run), living guide, consulted 2026-11-22. Supplies practitioner advice to use observable checks. Version matching, consumer review, and the example above are catalog adaptations.
