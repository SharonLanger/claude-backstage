---
pattern_id: PAT-0003
status: accepted
name: "Slice a change for review"
type: workflow
families: [code-review, incremental-delivery]
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
topic_ids: [AP-07, BP-05, OB-08, OB-11]
symptoms: ["The agent split the work by directory and I still cannot try the feature", "Three tickets have to land before I can tell if the first one works", "The diff changes several behaviors and I cannot tell which changes belong together"]
source_ids: [SRC-0006, SRC-0002]
review: PASS
publication_status: published
---

# Slice a change for review

## When users need this

A reviewer opens the first of several proposed changes and asks, “What can I try once this lands?” The answer is “wait for the last ticket.” Or a single generated patch implements several independently useful behaviors and the reviewer cannot tell which changes are necessary for any one of them. Both symptoms suggest a boundary problem. A change can touch several directories and still answer one clear review question.

## Context and prerequisites

Use this when a feature has an agreed outcome, spans more than one work session, and can be exercised through a real entry point such as a command, screen, or service operation. Identify the starting revision, any prerequisites it needs, and a way to observe results. A local demo is sufficient if the effect requires human judgment. Resolve material product decisions before asking an agent to partition the implementation. [Evidence, steps 1–3](#why-it-might-work)

## Core principle

Give each review one behavior to decide on and enough of the system to observe that behavior. If a reviewer cannot tell success from failure until an unfinished sibling lands, redraw the boundary or declare the genuine dependency.

## How to work this way

1. **Choose the first question a reviewer can answer.** Give the agent the agreed feature and ask it to propose one outcome with an actor, action, and observable result. Decide which nearby outcomes can wait. If the entire feature already fits one implementation session and has a coherent demonstration, use that whole change. Stop decomposing. [Evidence, step 1](#why-it-might-work)
2. **Trace one input to its result.** Ask which entry point receives the input, which code makes the decision, and where the result becomes observable. Include the necessary edits and tests on that path. Record a predecessor only when the path cannot work without it. Inspect the proposed boundary before implementation. If two proposed tickets can only be exercised together, combine them or identify a different observable result. [Evidence, step 2](#why-it-might-work)
3. **Try to falsify the acceptance check on the starting revision.** Supply concrete inputs and expected results. For a new behavior, run the check on the intended base after prerequisites have landed. Inspect the failure reason. An unavailable database or broken test runner leaves the baseline unknown. Include a counterexample that an obvious wrong implementation would mishandle and retain a check for adjacent behavior that should already pass. [Evidence, step 3](#why-it-might-work)
4. **Implement the path and hand it to review.** Ask for the command, observed results, and the diff against that base. The reviewer can rerun the check, follow the input through the changed code, and compare the diff with the agreed behavior and edge cases. Stop extending this slice once the behavior is demonstrable, the counterexample is handled, and the applicable existing checks pass. Keep the next outcome separate. If the review uncovers an unresolved requirement, settle it before treating the change as ready. [Evidence, step 4](#why-it-might-work)

## Concrete example of using the pattern

**Original, runnable exercise.** A team wants open-task filtering and CSV export in a command-line task list. Filtering printed titles already has value on its own. The first review question is whether asking for open tasks hides completed work while an ordinary listing still shows both. CSV export can use the original listing independently unless the product explicitly requires filtered exports.

To try it, save these two files in an empty directory with Python 3. The starting command lists all titles from a SQLite database.

`tasks.py`

```python
import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument("database")
args = parser.parse_args()

with sqlite3.connect(args.database) as db:
    query = "SELECT title FROM tasks"
    for (title,) in db.execute(query + " ORDER BY title"):
        print(title)
```

`check_slice.py`

```python
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile

command = Path(__file__).with_name("tasks.py")
with tempfile.TemporaryDirectory() as directory:
    database = Path(directory) / "tasks.db"
    with sqlite3.connect(database) as db:
        db.execute("CREATE TABLE tasks (title TEXT, done INTEGER)")
        db.executemany("INSERT INTO tasks VALUES (?, ?)", [
            ("Pack", 0), ("Reserve", 1)
        ])

    for options, expected in [([], ["Pack", "Reserve"]), (["--open"], ["Pack"])]:
        result = subprocess.run(
            [sys.executable, str(command), str(database), *options],
            text=True, capture_output=True
        )
        actual = result.stdout.splitlines()
        if result.returncode or actual != expected:
            raise SystemExit(f"FAIL {options}: expected {expected}, got {actual}, "
                             f"exit {result.returncode} {result.stderr.strip()}")
        print(f"PASS {options}: {actual}")
```

Run `python3 check_slice.py`. The ordinary listing passes. The new invocation fails because the command rejects `--open`. To implement this slice, insert `parser.add_argument("--open", action="store_true")` immediately before `args = parser.parse_args()`. Insert the following after the `query` assignment, at the same indentation as that assignment.

```python
    if args.open:
        query += " WHERE done = 0"
```

Rerun the same command. Its two passing lines show both titles for the default invocation and only `Pack` for `--open`. The reviewer can trace one input through argument parsing, SQL selection and printed output. A parser-only patch still prints `Reserve` with the flag. A permanently filtered query hides `Reserve` even without the flag. Both errors are observable with this fixture. A database containing only open tasks would hide the first error. This slice is ready for review without a CSV serializer.

## Why it might work

| Step or decision | Dossier claims | Original locator | Evidence and our adaptation |
|---|---|---|---|
| 1. Select an outcome, stop when the change already fits, clarify unsettled behavior first. | SRC-0006:C02, SRC-0006:C03 | Pocock, [What it does, paragraph 2](https://www.aihero.dev/skills-to-tickets#what-it-does) and [When to reach for it, scenario table](https://www.aihero.dev/skills-to-tickets#when-to-reach-for-it) | Practitioner guidance for tickets and available implementation context. Framing the unit as a question a reviewer can answer is our adaptation. |
| 2. Carry a behavior through its affected layers, identify true blockers and inspect the split. | SRC-0006:C02, SRC-0006:C04, SRC-0006:C06 | Pocock, [Tracer bullets, not layers, opening and refactoring discussion](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers), [Blocking edges, tracker comparison](https://www.aihero.dev/skills-to-tickets#blocking-edges), and [Common questions, over-splitting](https://www.aihero.dev/skills-to-tickets#common-questions) | Practitioner advice and documented planning workflow. Following a specific input through the diff with a reviewer is our application. |
| 3. Check the real baseline, challenge the criterion and exercise a counterexample. | SRC-0006:C05, SRC-0002:C07, SRC-0002:C10 | Pocock, [Common questions, acceptance criteria](https://www.aihero.dev/skills-to-tickets#common-questions); Anthropic, [Give Claude a check to run, opening and examples](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) and [Review against your spec, edge cases](https://code.claude.com/docs/en/best-practices#review-against-your-spec) | Pocock recommends falsifying new criteria at the intended base. Anthropic recommends runnable checks and checking edge-case coverage. The paired new-behavior and preserved-behavior cases, and diagnosing the failure reason, are our test design. |
| 4. Report results and compare the diff with requirements before starting the next outcome. | SRC-0002:C08, SRC-0002:C10, SRC-0006:C10 | Anthropic, [Give Claude a check to run, paragraph requesting command and output](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) and [Review against your spec, correctness review](https://code.claude.com/docs/en/best-practices#review-against-your-spec); Pocock, [Where it fits, implementation and review sequence](https://www.aihero.dev/skills-to-tickets#where-it-fits) | Direct vendor advice about verification and spec review, plus a practitioner's documented sequencing. Applying these to a human review handoff and setting a stopping rule are our synthesis. |
| Wide mechanical change requires a different boundary. | SRC-0006:C08 | Pocock, [The wide-refactor exception, migration sequence and integration fallback](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception) | Direct conditional practitioner guidance. The shared-field illustration below adapts Pocock’s column-rename example. |

## Different source perspectives

Pocock addresses how to divide work before handing it to implementers. His account of rework on a layer-based project has no comparable implementation using vertical tickets. Anthropic addresses how to verify a change against the specification after implementation. The publications have separate authorship and cover complementary operations. Neither compares review time, defect detection, or fatigue between slicing strategies. A persuasive demo can still miss a bug elsewhere in the diff. [Pocock’s reported case, SRC-0006:C07](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) · [Anthropic’s review guidance, SRC-0002:C10](https://code.claude.com/docs/en/best-practices#review-against-your-spec)

## Tradeoffs, failure modes and when to use another approach

A feature with one short path can cost more to specify in pieces than to show in full. A hidden dependency can also make a clean-looking ticket impossible to test until another team lands a change. State which revision or interface is needed and wait for it, or reshape the unit around an available path. A line-count target alone cannot resolve either problem. [Pocock, when decomposition is useful](https://www.aihero.dev/skills-to-tickets#when-to-reach-for-it) · [Pocock, blocking prerequisites](https://www.aihero.dev/skills-to-tickets#blocking-edges)

For a wide mechanical refactor, one isolated path may break callers that still need the old form. For example, when renaming a shared field, introduce a compatible form, migrate bounded groups of callers, verify the old form has no remaining consumers, then remove it. If the batches cannot each pass required checks, coordinate them on an integration branch and put the passing check at the final combined revision. An intermediate batch still awaiting integration must be described that way in review. [Pocock, wide-refactor exception, SRC-0006:C08](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception)

## Variations and practical adaptations

For a screen change, record the starting fixture, the action, the visible result and one condition that would make the result wrong. Supply before-and-after screenshots when presentation matters. In a service with no screen, exercise its public operation and observe its response or durable effect. A reviewer who cannot recreate a costly environment can inspect recorded evidence and identify which behavior remains unverified. These are adaptations of the same acceptance step. [Anthropic, checks and visual evidence, SRC-0002:C07 and SRC-0002:C08](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run)

## Related patterns, topics and families

AP-07 (big chunk working) identifies the workflow symptom. BP-05 (slice for review) identifies the proposed practice. Use the incremental-delivery family when planning a split and the code-review family when turning it into a checkable handoff.

## Sources and verification

- Matt Pocock. *The /to-tickets Skill*. AI Hero. Updated August 24, 2026. [Original](https://www.aihero.dev/skills-to-tickets) · [SRC-0006 dossier](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Independent source audit](../audits/SRC-0006--verification.md)
- Anthropic. *Best practices for Claude Code*. Claude Code Docs. Publication date unavailable, consulted November 21, 2026. [Original](https://code.claude.com/docs/en/best-practices) · [SRC-0002 dossier](../sources/SRC-0002--claude-code-best-practices.md) · [Independent source audit](../audits/SRC-0002--verification.md)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/PAT-0003--verification.md)

## Drive navigation

- [audits/PAT-0003--verification.md](../audits/PAT-0003--verification.md) · [Local copy](../audits/PAT-0003--verification.md)
- [audits/SRC-0002--verification.md](../audits/SRC-0002--verification.md) · [Local copy](../audits/SRC-0002--verification.md)
- [audits/SRC-0006--verification.md](../audits/SRC-0006--verification.md) · [Local copy](../audits/SRC-0006--verification.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [sources/SRC-0002--claude-code-best-practices.md](../sources/SRC-0002--claude-code-best-practices.md) · [Local copy](../sources/SRC-0002--claude-code-best-practices.md)
- [sources/SRC-0006--vertical-slices-for-agent-tickets.md](../sources/SRC-0006--vertical-slices-for-agent-tickets.md) · [Local copy](../sources/SRC-0006--vertical-slices-for-agent-tickets.md)
- [topics/AP-07--big-chunk-working.md](../topics/AP-07--big-chunk-working.md) · [Local copy](../topics/AP-07--big-chunk-working.md)
- [topics/BP-05--slice-for-review.md](../topics/BP-05--slice-for-review.md) · [Local copy](../topics/BP-05--slice-for-review.md)
- [topics/OB-08--degradation-under-complexity.md](../topics/OB-08--degradation-under-complexity.md) · [Local copy](../topics/OB-08--degradation-under-complexity.md)
- [topics/OB-11--keeping-up-review-fatigue.md](../topics/OB-11--keeping-up-review-fatigue.md) · [Local copy](../topics/OB-11--keeping-up-review-fatigue.md)
