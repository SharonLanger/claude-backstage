---
pattern_id: PAT-0002
status: accepted
name: "Verify an unfamiliar API call"
type: workflow
families: [reliability, code-review]
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
topic_ids: [AP-02, BP-06, OB-09, OB-10]
symptoms: ["The method the agent suggested is missing", "The example uses a keyword my installed library rejects", "The call runs but returns a different kind of object than the patch expects"]
source_ids: [SRC-0004, SRC-0002]
review: PASS
---

# Verify an unfamiliar API call

## When users need this

A generated patch calls an unfamiliar method and several lines below it assume a particular result. The editor might underline the name, the runtime might reject a keyword, or everything might type-check while the program reads the wrong resource. Start at the first questionable call. Resolving it can change what the rest of the patch needs to do.

## Context and prerequisites

Use this during implementation or review when you can identify the dependency and the concrete object receiving the call. You need a reference for the project’s actual version, such as the installed package’s help, types, source, or matching official documentation. An existing integration test can supply the behavior check if it exercises the intended case and observes the result. Without access to the relevant service or runtime, the static part of the review is still possible.

## Core principle

Answer three questions separately. **Does this object expose the operation? Can this version accept these arguments? Does calling it produce the effect the feature needs?** A positive answer to the first two leaves the third open.

## How to work this way

1. **Name the required effect.** In one sentence, identify the input, intended object or resource, and an observable result. Locate the first proposed call on which the rest of the change depends. For a search operation, for instance, say whether you want an exact object or a list of possible matches. See evidence row 1.
2. **Match the reference to the actual dependency.** Establish the installed language binding, package version and receiver type. Look up that receiver’s operation and read its description. Verify that the described resource and action fit step 1. If the name is missing, or a similarly named operation acts on a different resource, look up the required operation by its purpose. If published docs and the installed interface disagree, resolve the discrepancy against the deployed version or record exactly what remains unknown. See row 2.
3. **Check the proposed invocation.** Compare positional and keyword arguments, required values and the return contract used by the caller. Give the agent the matched signature, the relevant behavior detail, and the smallest correction to attempt. Revisit lines that consume the original call’s result. A response field or error handler may rely on the same mistaken assumption. See row 3.
4. **Exercise the behavior and inspect the result.** Use a fixture or suitable test environment where the expected outcome is known. Assert something that would discriminate between the intended operation and the plausible wrong one. Record the command and observed output. For a service you cannot exercise, distinguish what you verified locally from the behavior that still needs an integration check. See row 4.

## Worked example

A Python archive inspector must display the uncompressed size of a named member and recognize a missing name. The agent proposes `archive.read("report.csv").file_size`. Both the method and that argument exist. The call returns the file’s bytes, while the consumer expects metadata. That is the first point to fix.

In the project interpreter, `help(zipfile.ZipFile.getinfo)` identifies the named-member metadata operation. The bound signature in the example below is `(name)`. A focused request to the agent would be “Use the named member’s metadata. Read its uncompressed size, and check what happens when that name is missing.” The corrected caller uses `archive.getinfo("report.csv").file_size`.

This original fixture can be run with `python -` and the following code on standard input. It was run with Python 3.12.14 while preparing this entry.

```python
import inspect
import io
import sys
import zipfile

data = io.BytesIO()
with zipfile.ZipFile(data, "w") as archive:
    archive.writestr("report.csv", b"x,y\n")

with zipfile.ZipFile(data, "r") as archive:
    print(sys.version.split()[0], inspect.signature(archive.getinfo))
    member = archive.getinfo("report.csv")
    assert member.file_size == 4
    try:
        archive.getinfo("missing.csv")
    except KeyError:
        print("size=4, missing=KeyError")
    else:
        raise AssertionError("expected KeyError for missing.csv")
```

Observed output:

```text
3.12.14 (name)
size=4, missing=KeyError
```

The fixture confirms the field value and the exception that the surrounding feature must handle. It exercises the library call only. The application’s rendering and missing-file message need their own checks if they are part of the change.

## Why it might work

| Step | Source claims and original locators | Evidence and practitioner adaptation |
|---|---|---|
| 1. State the observable effect and find the dependent call | [SRC-0002:C06][s2], [specific-fix example][specific]. [SRC-0004:C03–C04][s4], [Appendix A.5–A.6, Fig. 14 and Table 4][errors] and [§II-A, Table I][prefix]. | Anthropic advises specifying the symptom and success criterion. Jain et al. distinguish several API mistakes. In a separate experiment, replacing a correct name with an invented one reduced similarity to the reference continuation. Reviewing the first doubtful call before its consumers is our ordering decision. |
| 2. Confirm receiver, existence, purpose and reference match | [SRC-0004:C01, C03, C06–C07][s4], [§2.2–2.3, evaluation][bench], [Appendix A.6, Table 4][errors], [§IV-A, Table III][docs] and [§IV-C, Table IV][results]. | Among GPT-4o’s invalid calls on the low-frequency slice, 53.05% used a nonexistent method, 33.54% misused the target, and 13.41% chose a different existing method. Name lookup alone misses the last two. The retrieval results depend on whether the supplied reference matches the target. Checking the project's installed version and receiver manually is our adaptation. |
| 3. Check arguments, share matched documentation and revisit consumers | [SRC-0004:C01, C04–C06][s4], [§2.3, scoring][bench], [§II-A, Table I][prefix], [§III-B, Fig. 6][docs] and [§IV-C, Table IV][results]. | With the correct document guaranteed, giving StarCoder2-3B the target signature raised benchmark validity from 41.80% to 86.82%. The experiment scored the first call. Choosing a short passage manually and examining return fields and error handlers extend beyond that result. |
| 4. Test the intended outcome and retain evidence | [SRC-0002:C07–C08][s2], [verification examples and execution evidence][check]. [SRC-0004:C01, C09][s4], [§2.3, scoring][bench] and [preprint §§7–8, limitations and ethics][limits]. | Anthropic advises running an interpretable check and requesting its command and result. Jain et al. recommend human review and sandbox execution. Their benchmark checks target identity and argument binding. The discriminating fixture and the distinction between a local check and a live-service result are our implementation of that advice. |

## Different source perspectives

Jain and colleagues measured generated Python calls on 622 short synthetic tasks for AWS and Azure. Anthropic’s living guide gives general practitioner advice for evaluating coding changes. These are separate publications with different contributions. Neither measured whether developers using this four-step workflow found more defects or spent less time reviewing patches.

The study also gives a reason to select the reference carefully. With one retrieved document and the correct target included half the time, unconditional retrieval improved GPT-4o’s low-frequency validity from 38.58% to 47.94% while common-call validity fell from 93.66% to 54.63%. Those conditions differ from a developer opening the correct version’s reference. They give no basis for withholding correct documentation for a familiar call. [SRC-0004:C06][s4] · [§IV-C, Table IV][results]

## Tradeoffs and variations

- **Existing coverage.** A current test may already drive this exact dependency, input and result. Inspect its assertion and use that test for step 4. A mock programmed to return the field the patch expects can check the caller, while leaving the library’s actual return contract unverified. This is an adaptation of row 4.
- **Private, generated or remote interfaces.** Use a version-matched generated type or the installed interface for steps 2–3. A stub can establish the local argument shape. Service permissions, responses and side effects may require a separate integration environment. If that environment is unavailable, report those open questions with the static evidence. This is an adaptation of rows 2–4.
- **When to use a different approach.** If the operation, signature and response are already confirmed and the mismatch occurs in application-specific transformation logic, start with a failing assertion for that transformation. Repeating the API lookup adds little. This stopping rule is our adaptation of rows 1 and 4.

## Related topics and families

**OB-09, hallucination in code**, is the primary match. **AP-02, accepting generated code without review**, is relevant when a recognizable call passes without checking its meaning. **BP-06, context management**, applies narrowly to selecting the correct documentation for a call. The paper studied retrieval in short tasks. This entry addresses API verification and has no session-reset rule.

## Sources and review

- Nihal Jain, Robert Kwiatkowski, Baishakhi Ray, Murali Krishna Ramanathan and Varun Kumar. *On Mitigating Code LLM Hallucinations with API Documentation*. ICSE-SEIP, 2025. [SRC-0004 dossier][s4] · [Original publication](https://www.amazon.science/publications/on-mitigating-code-llm-hallucinations-with-api-documentation) · [Independent source audit](../audits/SRC-0004--verification.md)
- Anthropic. *Best practices for Claude Code*. Living documentation, publication date unspecified, inspected November 21, 2026. [SRC-0002 dossier][s2] · [Original guide](https://code.claude.com/docs/en/best-practices) · [Independent source audit](../audits/SRC-0002--verification.md)

Developer time cost and the effect of manual version matching on real project defect rates remain unmeasured in these sources.

[s2]: ../sources/SRC-0002--claude-code-best-practices.md
[s4]: ../sources/SRC-0004--api-documentation-and-hallucinations.md
[specific]: https://code.claude.com/docs/en/best-practices#write-a-specific-prompt
[check]: https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run
[errors]: https://arxiv.org/html/2407.09726v1#A1
[bench]: https://arxiv.org/html/2407.09726v1#S2
[limits]: https://arxiv.org/html/2407.09726v1#S7
[prefix]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=2
[docs]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=5
[results]: https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf#page=7

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/PAT-0002--verification.md)

## Drive navigation

- [audits/PAT-0002--verification.md](../audits/PAT-0002--verification.md) · [Local copy](../audits/PAT-0002--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0004--verification.md](../audits/SRC-0004--verification.md) · [Local copy](../audits/SRC-0004--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0004--api-documentation-and-hallucinations.md](../sources/SRC-0004--api-documentation-and-hallucinations.md) · [Local copy](../sources/SRC-0004--api-documentation-and-hallucinations.md)
- [topics/AP-02--flying-blind-vibe-coding.md](../topics/AP-02--flying-blind-vibe-coding.md) · [Local copy](../topics/AP-02--flying-blind-vibe-coding.md)
- [topics/BP-06--context-management-discipline.md](../topics/BP-06--context-management-discipline.md) · [Local copy](../topics/BP-06--context-management-discipline.md)
- [topics/OB-09--hallucination-in-code.md](../topics/OB-09--hallucination-in-code.md) · [Local copy](../topics/OB-09--hallucination-in-code.md)
- [topics/OB-10--limited-attention-focus.md](../topics/OB-10--limited-attention-focus.md) · [Local copy](../topics/OB-10--limited-attention-focus.md)
