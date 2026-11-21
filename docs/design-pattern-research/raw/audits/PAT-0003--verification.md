---
pattern_id: PAT-0003
artifact_type: pattern_verification
reviewer: review_slice
reviewed: 2026-11-21
verdict: PASS
initial_verdict: PASS WITH CHANGES
---

# PAT-0003 independent verification

**PASS after correction and independent recheck.** The method is usable and each step has a traceable basis. The initial verdict was PASS WITH CHANGES for the illustration attribution documented in finding 7. [Reviewed pattern](../patterns/PAT-0003--slice-a-change-for-review.md) · [Pocock dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Anthropic dossier](../sources/SRC-0002--claude-code-best-practices.md)

## Findings

1. **Choosing the first review question, step 1.** SRC-0006:C02–C03 support an observable outcome, settling decisions ahead of implementation and proceeding directly when the whole change fits one session. A reviewer's question is an original way to describe that outcome. The symptom of waiting on unrelated tickets is a good match. [Pocock, What it does](https://www.aihero.dev/skills-to-tickets#what-it-does) · [When to reach for it](https://www.aihero.dev/skills-to-tickets#when-to-reach-for-it)
2. **Tracing the path, step 2.** SRC-0006:C02, C04 and C06 support identifying affected layers, challenging the proposed boundaries and checking that dependencies really prevent work from starting. The pattern lets completed predecessors form part of the starting revision. A reviewer can follow an actual input across several files without requiring an entire feature to ship first. [Pocock, Tracer bullets](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) · [Blocking edges](https://www.aihero.dev/skills-to-tickets#blocking-edges)
3. **Testing the starting revision, step 3.** SRC-0006:C05 locates the failed new-behavior check at the implementer's actual base. SRC-0002:C07 and C10 support running a check and covering specified edge cases. The pattern explicitly contributes the adjacent passing case and diagnosis of a failure caused by the test environment. That distinction matters when a test fails before it reaches the changed behavior. [Pocock, Common questions, acceptance criteria](https://www.aihero.dev/skills-to-tickets#common-questions) · [Anthropic, Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Review against your spec](https://code.claude.com/docs/en/best-practices#review-against-your-spec)
4. **Handoff and stopping rule, step 4.** SRC-0002:C08 and C10 support collecting concrete run evidence and reviewing the diff against requirements. SRC-0006:C10 supports the sequence from implementation into review. The pattern identifies its human handoff and stopping rule as synthesis. Screenshot and service-response variants preserve that distinction. [Anthropic, verification evidence](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Spec review](https://code.claude.com/docs/en/best-practices#review-against-your-spec) · [Pocock, Where it fits](https://www.aihero.dev/skills-to-tickets#where-it-fits)
5. **Usability test.** I extracted both Python files from the pattern into a temporary directory and ran its command against four implementations. On the original revision the default listing passed and the command rejected the unknown flag with exit code 2. Adding the parser alone left the completed task visible for the flagged invocation. Filtering unconditionally hid it in the default listing. Applying both edits as written passed both checks, producing `Pack, Reserve` by default and `Pack` with the flag. Filtering was demonstrable independently of CSV export. These results establish what this fixture exercises.
6. **Limits, independence and rights.** Pocock describes decomposition and recounts one team's experience. Anthropic describes checks and review in its own product documentation. Their separate publications give complementary advice. Neither measures reviewer fatigue, review duration or defect detection for the proposed workflow. The feature example and its Python code are distinct from both originals. The method uses short section names for navigation, without republishing either article. [Pocock, case discussion](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) · [Anthropic, review example](https://code.claude.com/docs/en/best-practices#review-against-your-spec)
7. **Provenance correction requested.** SRC-0006:C08 accurately describes the compatible migration and final integration fallback. The original explicitly illustrates this case with a column rename and a shared-symbol change. The evidence row described its analogous shared-field migration as the pattern author's own illustration. Credit it as an adaptation of Pocock's example. [Pocock, The wide-refactor exception](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception)
8. **Navigation.** The pattern's relative links resolve to both accepted dossiers and both independent source audits. All cited claim IDs are present. The topic references are AP-07 and BP-05. On the initial review the dossiers awaited reciprocal PAT-0003 references and the draft awaited its audit link. These are integration tasks for publication. [SRC-0006 audit](SRC-0006--verification.md) · [SRC-0002 audit](SRC-0002--verification.md)

## Disposition

I reread the revised evidence row and its linked passage. The row now credits Pocock’s column-rename example as the source of the shared-field illustration. Finding 7 is resolved. The pattern passes substantive review. Drive publication and reciprocal navigation remain the integrator’s separate checks.

## Drive navigation

- [patterns/PAT-0003--slice-a-change-for-review.md](../patterns/PAT-0003--slice-a-change-for-review.md) · [Local copy](../patterns/PAT-0003--slice-a-change-for-review.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
