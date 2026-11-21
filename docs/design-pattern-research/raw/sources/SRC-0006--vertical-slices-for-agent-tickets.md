---
source_id: SRC-0006
status: accepted
original_title: "The /to-tickets Skill"
authors: ["Matt Pocock"]
publisher: "AI Hero"
source_type: practitioner_blog
published: unknown
updated: 2026-08-24
accessed: 2026-11-21
original_url: "https://www.aihero.dev/skills-to-tickets"
source_version: "Live AI Hero article with a displayed update of August 24, 2026. No numbered article version verified."
full_text_reuse: not_authorized_or_unverified
topic_link_scope: "Navigation includes direct, supporting and contrasting evidence. The linked topic note specifies the scope of each connection."
related_topics: [AP-07, BP-01, BP-05, BP-06, OB-08, OB-11]
related_patterns: [PAT-0003]
review: PASS
publication_status: published
---

# The /to-tickets Skill

## Provenance and scope read

Matt Pocock wrote this practitioner guide in AI Hero’s *AI Skills for Real Engineers* series. The live page shows an August 24, 2026 update and gives no separate first-publication date in the accessible article. Pocock teaches and distributes the workflow he describes, and the article links to his training material as well as the source repository. Its strongest evidence is a firsthand account of what the skill is designed to do. [AI Hero article](https://www.aihero.dev/skills-to-tickets)

Read the complete public article from “What it does” through “Related reading,” including the tracker comparison, refactor exception and troubleshooting. Also read the linked `SKILL.md` on the repository’s live `main` branch for the drafting, approval and publication sequence, and inspected the two tracker reports the article cites. These materials establish what was documented or reported. No skill execution or tracker mutation was performed. The team postmortem mentioned in the article was unavailable for inspection. [AI Hero article](https://www.aihero.dev/skills-to-tickets) · [Linked skill definition](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md) · [Report #513](https://github.com/mattpocock/skills/issues/513) · [Report #554](https://github.com/mattpocock/skills/issues/554)

## Reader's orientation

Pocock addresses how to hand off a feature that is already shaped but will take several implementation sessions. He proposes organizing each ticket around an observable outcome. The ticket covers enough of the affected system to make that outcome demonstrable or testable after its recorded prerequisites have landed, and it fits the capacity of a fresh agent session. The article calls such a ticket a *tracer bullet*. [What it does](https://www.aihero.dev/skills-to-tickets#what-it-does) · [Tracer bullets, not layers](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers)

The article concerns ticket decomposition and sequencing. It describes a downstream review step along with testing and implementation, but it supplies no measurements of pull-request size, reviewer time, review quality, defects found in review, or review fatigue. The connection to BP-05 is the availability of a discrete behavior and an observable check that could give a reviewer a bounded task. Review outcomes remain an open question. [Where it fits](https://www.aihero.dev/skills-to-tickets#where-it-fits)

## Detailed analytical reading (original words)

### Choose an outcome that fits a fresh session

The skill accepts an existing specification, a plan, or decisions already made in the current conversation. Pocock places clarification upstream when decisions are still unsettled. For work that already fits in a single context window, he suggests implementing it directly, which avoids creating a separate planning artifact for a tiny change. Where `/to-spec` and `/to-tickets` run in sequence, he recommends keeping the spec-writing and ticket-writing steps in the same context. A large tracker issue can be incomplete when retrieved. Individual implementation tickets then go to fresh sessions. That distinction matters because the planning task needs the whole settled feature and the implementation task needs a complete account of its own narrower outcome. [When to reach for it](https://www.aihero.dev/skills-to-tickets#when-to-reach-for-it) · [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions) · [Where it fits](https://www.aihero.dev/skills-to-tickets#where-it-fits)

Suppose a behavior needs persistence, a service boundary and a screen. If the three teams of work ship separately, a ticket can report its own component done while the result remains impossible to observe through the application. Acceptance also becomes ambiguous when the demonstration depends on a change assigned to an unrelated open ticket. Pocock’s boundary is the smallest useful path through the affected layers. The ticket owns the work needed for that path and specifies any upstream work that genuinely must already exist. Independence is therefore relative to the point at which the ticket becomes ready. A ticket can depend on earlier groundwork and still be independently demonstrable once the groundwork has landed. [What it does](https://www.aihero.dev/skills-to-tickets#what-it-does) · [Tracer bullets, not layers](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) · [Blocking edges](https://www.aihero.dev/skills-to-tickets#blocking-edges)

### Check the proposed boundaries and acceptance criteria

Pocock has the skill look for preparatory refactoring first. The user then inspects an ordered proposal and can merge small fragments, narrow a ticket that is too big, or remove a dependency that is merely a preferred order. The proposal shows the behavior delivered and the required predecessors. The `SKILL.md` explicitly puts this discussion before publication. The article reports that the tool can still suggest layer-based work or split a small change into too many fragments, so the approval step serves a practical purpose. [Tracer bullets, not layers](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) · [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions) · [Skill definition, Process §§2–5](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md#process)

At approval, the human can name the exact observation a finished ticket should make possible. The article describes three flawed acceptance criteria. One already passes before work starts, another relies on an outcome owned by a different unfinished ticket, and a third simply restates the request without specifying an observable result. Pocock suggests identifying what would falsify each criterion and checking against the base commit the implementer will use. The criterion for new behavior should fail on that starting commit and pass with the change. If a ticket depends on groundwork, assess that base after the groundwork has landed. [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions) · [It's working if](https://www.aihero.dev/skills-to-tickets#its-working-if)

### Publish and work from explicit prerequisites

The documented skill has a configured destination and label vocabulary. It writes one local Markdown file per ticket or one issue per ticket in a supported tracker. Publishing predecessors first allows later tickets to point to existing IDs. The current skill definition calls for native blocking relationships where the tracker supports them, with a ticket-text fallback. Parent-child links express membership in a specification. A blocking relationship gates when the work starts, which is a separate concern. Pocock describes the ready set as all tickets whose predecessors have finished. That set may contain several tickets, but `/to-tickets` itself produces the planning artifact. The article describes manual dispatch and says operators may need to update ticket completion themselves. It separately describes a downstream workflow that runs ready tickets on a shared integration branch. [Prerequisites](https://www.aihero.dev/skills-to-tickets#prerequisites) · [Blocking edges](https://www.aihero.dev/skills-to-tickets#blocking-edges) · [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions) · [Where it fits](https://www.aihero.dev/skills-to-tickets#where-it-fits) · [Skill definition, Process §5](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md#5-publish-the-tickets-to-the-configured-tracker)

### Read the rework case at its evidence strength

Pocock reports that one team planned a 26-ticket stack around layers called corpus, producer, aggregator and selector. The reported workload was approximately 20 agent runs per closed ticket and about three quarters of the runs were rework. He attributes the explanation to the team’s postmortem, which assigned the classes of failure to the decomposition. This makes the case a prompt for diagnosis when completion depends on work scattered across ticket boundaries. The article gives no underlying logs, count of tickets closed, criteria for classifying a run as rework, or comparable vertical implementation. There is no independent basis here for estimating the change in agent runs if a team adopts vertical slicing. [Tracer bullets, not layers](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers)

### Use a migration sequence when no behavioral slice can land green

Pocock's exception is a single mechanical change with a large, coupled set of callers, such as a shared symbol or column rename. If an isolated edit would break callers and there is no viable end-to-end slice, he proposes expand–contract. Introduce the new form alongside the old and make it possible for both to coexist. Migrate callers in batches organized by package or a comparable ownership boundary. Each batch depends on the expansion, and the closing removal depends on all migration batches and the absence of callers of the old form. The compatibility period is how the sequence can keep CI passing between batches. If the batches still cannot pass independently, Pocock proposes gathering them on an integration branch with a final integration-and-verification ticket that waits on all batches. The green checkpoint then applies at final integration. [The wide-refactor exception](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception)

## Claim-level evidence ledger

| Claim ID | Accurate source-supported proposition | Nature | Exact source locator | Support and caveat |
|---|---|---|---|---|
| SRC-0006:C01 | `/to-tickets` accepts a plan, specification or current conversation and produces tickets describing which work must finish before each can start. | Doc behavior | [What it does, first paragraph](https://www.aihero.dev/skills-to-tickets#what-it-does) | Direct for the documented interface. |
| SRC-0006:C02 | A feature ticket should carry one independently demonstrable or testable behavior through the affected layers and be feasible in a fresh context window. | Practitioner advice | [What it does, second paragraph](https://www.aihero.dev/skills-to-tickets#what-it-does) and [Tracer bullets, not layers, first paragraph](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) | Direct guidance. Documented predecessors can exist. Context capacity varies. |
| SRC-0006:C03 | Clarify unsettled decisions upstream and skip ticket decomposition when the whole change already fits an implementation session. | Practitioner advice | [When to reach for it, scenario table](https://www.aihero.dev/skills-to-tickets#when-to-reach-for-it) and [Common questions, over-decomposition](https://www.aihero.dev/skills-to-tickets#common-questions) | Direct guidance. No objective size threshold is given. |
| SRC-0006:C04 | The skill looks for preparatory refactoring and presents the candidate tickets, outcomes and blocking prerequisites for human revision and approval before publishing. | Doc behavior and practitioner advice | [Tracer bullets, not layers, final paragraph](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) and [Skill definition, draft and approval steps](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md#3-draft-vertical-slices) | Direct as designed. The article recounts over-splitting and layer-shaped drafts in practice. |
| SRC-0006:C05 | Use a demo or test to inspect a ticket boundary. For each new-behavior criterion, identify what would show it false and check it against the implementer’s starting commit. | Practitioner advice | [Common questions, layer-shaped tickets and acceptance criteria](https://www.aihero.dev/skills-to-tickets#common-questions) | Direct. The article offers a demo-path field as an optional reported aid. |
| SRC-0006:C06 | Local Markdown uses a separate file for each ticket with text prerequisites. On a tracker, publish blockers before their dependents and use native blocking relationships where supported. A ticket is ready when all blockers are done. | Doc behavior | [Blocking edges, comparison table](https://www.aihero.dev/skills-to-tickets#blocking-edges) and [Skill definition, Publish step](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md#5-publish-the-tickets-to-the-configured-tracker) | Direct as designed. Historical issue reports show publishing can miss native links or parents. |
| SRC-0006:C07 | Pocock recounts one 26-ticket layer-based effort with roughly 20 agent runs per closed ticket and about three quarters rework. He reports the team attributed failure classes to its slicing. | Author-reported anecdote | [Tracer bullets, not layers, second paragraph](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) | Direct for what Pocock reports. Underlying postmortem and comparator unavailable. |
| SRC-0006:C08 | For a mechanical refactor that cannot land as green vertical slices, add a compatible new form, migrate bounded groups, and remove the old form after all migrations. If batches cannot stay green, use a shared branch and a final integration verification gate. | Practitioner advice | [The wide-refactor exception, full section](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception) | Direct conditional guidance. Applicability turns on compatibility and the affected callers. |
| SRC-0006:C09 | Keep the specification and decomposition in one planning context if tracker retrieval may truncate the spec. Use a fresh implementation context for each ticket. `/to-tickets` itself stops at the ticket artifact. | Practitioner advice and doc behavior | [Common questions, spec truncation and dispatch](https://www.aihero.dev/skills-to-tickets#common-questions) and [Where it fits, main chain](https://www.aihero.dev/skills-to-tickets#where-it-fits) | Direct. The companion workflow for parallel implementation is distinct from the ticket generator. |
| SRC-0006:C10 | The published workflow places code review downstream of implementation. The article includes no review-outcome evaluation. | Doc behavior and scope assessment | [Where it fits, main chain](https://www.aihero.dev/skills-to-tickets#where-it-fits) and the [complete article](https://www.aihero.dev/skills-to-tickets) | Supporting for a proposed application to BP-05. No estimate of reviewer burden or review quality. |

## Extractable practitioner insights

### Worked adaptation for saved invoice searches

This example was constructed for the dossier. Consider a billing console with an existing invoice list. The planned feature lets staff save a search, reopen it by name and share it with teammates. A split into database, routes and UI would leave the demonstration waiting on the final layer. A first slice can instead let a staff member save and reopen one private search. It spans persisted ownership and filter values, the service operations required to save and load them, the existing list screen, and an automated check. Use a small invoice fixture so a saved overdue filter brings back a known result on reload. Seed a second user to confirm the first user’s private search cannot be reopened by that account. On the starting revision, the save-and-reopen observation fails. Once the ticket lands, it is testable through the product without sharing. [Basis for the adaptation, SRC-0006:C02 and C05](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers)

| Proposed ticket | Required predecessor | Observation after the ticket lands |
|---|---|---|
| A. Save and reopen one private search | None in this scenario | A staff member filters the invoice list, saves the search, reloads the page and restores the same filter and expected invoice results. A different account cannot load the private search. |
| B. Rename a private search | A, because it changes a saved search that already exists | The owner renames a saved search, reloads and sees the new name with the original filter. |
| C. Share a saved search with an authorized teammate | A, because sharing requires a persisted search | An authorized teammate can open the shared filter from their own account. An account outside the team cannot load it. |

At the planning check, B should not appear as a blocker for C merely because the planner expects it to ship first. Confirm that sharing makes sense with the original name and that the product specification permits it. If the branches would edit the same permission checks, their implementation might be possible in parallel but integration could still require coordination. A finite demo path also gives a reviewer a way to inspect the promised behavior. This example does not show that two small pull requests would take less review time than one larger one. [Blocking edges, basis for the prerequisite check](https://www.aihero.dev/skills-to-tickets#blocking-edges) · [Where it fits, scope of review evidence](https://www.aihero.dev/skills-to-tickets#where-it-fits)

### Limits to apply before turning this into a catalog pattern

- **AP-07 Big chunk working.** Direct practitioner guidance for a multi-session change that would otherwise defer integration until the end. Look for an observable behavior and enough affected-layer work to deliver it. The guidance also guards against over-decomposition when a small, coherent change already fits one implementation session. `SRC-0006:C02–C05`. [When to reach for it](https://www.aihero.dev/skills-to-tickets#when-to-reach-for-it) · [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions)
- **BP-05 Slice for review.** Supporting material for bounded behavior and testable criteria. Ticket size and mechanical dependency order do not determine pull-request count, review depth or reviewer workload. A risky or tightly coupled slice can still merit prior design review or additional integration verification. That qualification is an application inference, while the migration exception is explicit in the article. `SRC-0006:C02`, `C05`, `C08`, `C10`. [The wide-refactor exception](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception) · [Where it fits](https://www.aihero.dev/skills-to-tickets#where-it-fits)
- **BP-06 Context management discipline.** Direct advice about when to carry context across a planning handoff and when to start fresh for execution. Supporting evidence for the broader topic, with no experiment on context degradation. `SRC-0006:C01–C03`, `C09`. [Common questions](https://www.aihero.dev/skills-to-tickets#common-questions) · [Where it fits](https://www.aihero.dev/skills-to-tickets#where-it-fits)

The candidate practice is to make an end-to-end outcome and its required predecessors explicit before dispatching a multi-session change.

## Related work, conflicts, and limitations

The linked `SKILL.md` is the author’s implementation artifact and the repository documentation closely mirrors the AI Hero article. They provide additional locators for the workflow, with shared provenance. The GitHub issues contain original user reports about specific publication errors. One concerns a dependency expressed in issue text and the other concerns missing parent-child linkage. They illustrate that agents may publish structurally incomplete tickets even if the proposed dependency ordering is sound. They say nothing about the comparative effectiveness of vertical and layer-based tickets. Implementation details and reported fixes vary with version and tracker setup. [Linked skill definition](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md) · [Repository documentation](https://github.com/mattpocock/skills/blob/main/docs/engineering/to-tickets.md) · [Report #513](https://github.com/mattpocock/skills/issues/513) · [Report #554](https://github.com/mattpocock/skills/issues/554)

The guide gives a practical decomposition heuristic and a single reported rework case. It leaves open how often the process yields meaningful slices, what it costs to plan and integrate them, and whether different slice sizes change review or production outcomes. The wide-refactor exception also means the advice has an explicit case where a passing checkpoint belongs to integrated work. [Tracer bullets, not layers](https://www.aihero.dev/skills-to-tickets#tracer-bullets-not-layers) · [The wide-refactor exception](https://www.aihero.dev/skills-to-tickets#the-wide-refactor-exception)

## Retrieval hints (plain-language user symptoms, families, tags)

- “Our database and API tickets are done, but we still can’t demo the feature.”
- “Each new agent needs the entire earlier conversation before it can start.”
- “The ticket passes its acceptance criteria even on the base branch.”
- “Every ticket says it is blocked, and we cannot work out which blockers are real.”
- “We need to rename a shared type and every package breaks if it moves alone.”

Families include work decomposition, verification scope, and session handoffs. Useful search terms include vertical slice, tracer bullet, acceptance criteria, dependency graph, independent demo, fresh context, and expand–contract migration.

## Original article access and copyright/permission record

The canonical AI Hero article was publicly readable on November 21, 2026. The site page did not display an article-specific reuse grant, and the general terms contain a reproduction provision. The separate public repository has an MIT license for its software and associated documentation, subject to preserving the notices for copies or substantial portions. That license is recorded for the repository copy. Full-text reuse of the AI Hero publication remains unverified, and this dossier contains original analysis and navigational citations. [Original AI Hero article](https://www.aihero.dev/skills-to-tickets) · [AI Hero general terms, §2](https://www.aihero.dev/privacy) · [Repository license](https://github.com/mattpocock/skills/blob/main/LICENSE)

## Reviewer disposition

Accepted after independent PASS on 2026-11-21. [Verification findings](../audits/SRC-0006--verification.md)

## Drive navigation

- [audits/PAT-0003--verification.md](../audits/PAT-0003--verification.md) · [Local copy](../audits/PAT-0003--verification.md)
- [audits/SRC-0006--verification.md](../audits/SRC-0006--verification.md) · [Local copy](../audits/SRC-0006--verification.md)
- [patterns/PAT-0003--slice-a-change-for-review.md](../patterns/PAT-0003--slice-a-change-for-review.md) · [Local copy](../patterns/PAT-0003--slice-a-change-for-review.md)
- [source-topic-map.md](../source-topic-map.md) · [Local copy](../source-topic-map.md)
- [topics/AP-07--big-chunk-working.md](../topics/AP-07--big-chunk-working.md) · [Local copy](../topics/AP-07--big-chunk-working.md)
- [topics/BP-01--knowledge-checkpointing.md](../topics/BP-01--knowledge-checkpointing.md) · [Local copy](../topics/BP-01--knowledge-checkpointing.md)
- [topics/BP-05--slice-for-review.md](../topics/BP-05--slice-for-review.md) · [Local copy](../topics/BP-05--slice-for-review.md)
- [topics/BP-06--context-management-discipline.md](../topics/BP-06--context-management-discipline.md) · [Local copy](../topics/BP-06--context-management-discipline.md)
- [topics/OB-08--degradation-under-complexity.md](../topics/OB-08--degradation-under-complexity.md) · [Local copy](../topics/OB-08--degradation-under-complexity.md)
- [topics/OB-11--keeping-up-review-fatigue.md](../topics/OB-11--keeping-up-review-fatigue.md) · [Local copy](../topics/OB-11--keeping-up-review-fatigue.md)
