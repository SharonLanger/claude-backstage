---
artifact_id: PAT-0005
verdict: PASS
review_date: 2026-11-21
review_role: independent_pattern_reviewer
source_ids: [SRC-0010, SRC-0002, SRC-0005]
---

# Independent review of PAT-0005

**PASS.** A reviewer can use the entry to turn a comment on an existing patch into a request with an observable acceptance condition. I read the three accepted dossiers, reopened all three original publications, read the lesson handout from its publisher’s repository, checked the local links, and executed the example from the pattern text. [Reviewed pattern](../patterns/PAT-0005--turn-review-feedback-into-a-check.md)

## Findings

1. **Step 1.** Ördög distinguishes a present observation from a possible later consequence. The guide’s login example combines a symptom, a location and a reproducing test. The PAT credits those sources and identifies minimization and tentative diagnoses as its own procedure. Its example observes a parser value and makes a conditional prediction about an operator’s job. That distinction preserves what the check can establish. [SRC-0010:C01, C02, C04](../sources/SRC-0010--rose-feedback-exercise.md) · [Lesson, concept and final bullets](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) · [SRC-0002:C06](../sources/SRC-0002--claude-code-best-practices.md) · [Login example](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt)
2. **Step 2.** The handout’s package example asks both for specific changes and for additional ideas. The paper’s Figure 2 distinguishes conceding a mistake from changing an initially correct answer. Its Figure 3 compares model accuracy under suggested answers with neutral prompts across two free-form QA datasets. These experiments support the concern about answering under user pressure. The PAT labels the choice to request reproduction or leave the implementation open as a code-review adaptation. [SRC-0010:C02, C07](../sources/SRC-0010--rose-feedback-exercise.md) · [Teaching handout](https://github.com/sammancoaching/website/blob/main/assets/images/rose_pattern_handout.svg) · [SRC-0005:C03, C05](../sources/SRC-0005--sycophancy-and-user-beliefs.md) · [Sharma et al., §§3.2–3.3, Figures 2–3](https://arxiv.org/html/2310.13548v4)
3. **Step 3.** The lesson allows elements to be omitted or reordered and describes an immediate observable outcome. Anthropic proposes a runnable check and review of stated edge cases. The PAT contributes the choice of a neighboring case that would catch one plausible incorrect fix and the explicit source of its expected value. A documented default gives the worked example that authority. [SRC-0010:C02–C04](../sources/SRC-0010--rose-feedback-exercise.md) · [Concept and qualifications](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#concept-the-rose-feedback-pattern) · [SRC-0002:C07, C10](../sources/SRC-0002--claude-code-best-practices.md) · [Runnable checks](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Spec review](https://code.claude.com/docs/en/best-practices#review-against-your-spec)
4. **Step 4 and variations.** The kata exercise offers an optional inspection of the agent’s result. The guide asks for a command plus output or a screenshot, and supplies a separate prompt for checking a diff against a specification. The PAT takes responsibility for the reviewer’s rerun and inspection of changed assertions. Its screenshot example limits the conclusion to what the reviewer can see. Where a requirement is undecided it directs the reader to the owner, a stated extension of the spec-interview advice. [SRC-0010:C06](../sources/SRC-0010--rose-feedback-exercise.md) · [Kata exercise, final step](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html#write-rose-prompts-for-the-tennis-kata-25-min) · [SRC-0002:C05, C08, C10](../sources/SRC-0002--claude-code-best-practices.md) · [Evidence options](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) · [Spec review](https://code.claude.com/docs/en/best-practices#review-against-your-spec) · [Spec interview](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first)
5. **Independence and rights.** The named method and its handout constitute one teaching source. The guide is vendor advice. The paper acknowledges Anthropic affiliations and reports a different task and outcome. The entry claims no independent replication or measured effect of ROSE on code changes. It attributes the framework to Ördög and uses original explanatory prose, a new review comment, and separate Python examples. The lesson footer identifies CC BY-SA 4.0 and the paper identifies CC BY 4.0. I found no reproduced handout, expressive source passage, or vendor example in the pattern. [Lesson credit and license](https://sammancoaching.org/learning_hours/agentic_engineering/rose_feedback.html) · [Paper affiliation and license](https://arxiv.org/html/2310.13548v4) · [Vendor guide](https://code.claude.com/docs/en/best-practices)

## Executed usability check

I ran the two Python blocks together, then ran the same inputs against the two substitutions specified in the worked example. For explicit zero, omitted key and positive two, in that order, the proposed parser printed `3, 3, 2`. Changing the fallback constant to zero printed `0, 0, 2`. Passing the default as the second argument to `get` printed `0, 3, 2`. The omitted-key case exposes a failure that testing explicit zero alone would miss. All three results matched the text. This verifies the instructional example for its stated integer inputs. It supplies no measurement of agent behavior in a real code review.

## Disposition

No pattern-content repairs required. All outgoing relative artifact links resolved locally. Publication and reciprocal source references belong to the integration pass after acceptance.

## Drive navigation

- [patterns/PAT-0005--turn-review-feedback-into-a-check.md](../patterns/PAT-0005--turn-review-feedback-into-a-check.md) · [Local copy](../patterns/PAT-0005--turn-review-feedback-into-a-check.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
