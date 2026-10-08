# Checklist Writing Guidelines

Recommendations for writing effective checklists. These are guidance, not mandatory rules — the mandatory constraints live in [agents/golden-rules.md](../agents/golden-rules.md) and [agents/checklist-agent.md](../agents/checklist-agent.md).

## Prefer deterministic checks

Deterministic checks produce the same result regardless of who runs them. They are reproducible, debuggable, and leave no room for interpretation drift across verification rounds.

**Good deterministic checks:**

- File `handoffs/act-01-review/findings.md` exists.
- The `status` field in the response schema is one of: `active`, `inactive`, `pending`.
- All functions in `src/api/` have at least one unit test.
- The migration runs without errors against the test database.

**When you need judgment:** Some checks genuinely require model judgment — "Is the error message helpful?" or "Does the architecture handle the stated scale requirements?" When judgment is unavoidable, say so explicitly in the check description. Do not disguise a judgment call as a deterministic check.

A check like "Code quality is acceptable" is not deterministic and not useful. Replace it with specific, observable criteria: "No function exceeds 50 lines," "Every public API endpoint has error handling for 4xx and 5xx responses."

## State explicit pass criteria

Every check item should make its pass condition clear enough that two independent Checklist Agent instances would reach the same verdict given the same evidence.

**Vague:** "API responses are correct."
**Specific:** "Every endpoint in `src/api/routes/` returns the status codes documented in `reference/api-spec.md` for both success and error cases."

The pass criteria should reference observable artifacts — files, outputs, tool results — not intentions or design goals.

## Verify each Act's required outputs

A checklist should cover every output declared in the Act file's `## Outputs` section. If the Act promises three files in `handoffs/`, the checklist should verify all three exist and meet their stated criteria.

A missing required file is a failure. The producing Act's checklist — not a downstream Act's — should detect it. Catching the omission at the source prevents later Acts from working against incomplete inputs.

## Design for useful failures

A well-written check produces useful information when it fails. The Checklist Agent's golden rules require reporting expected vs. actual results, evidence, and corrections needed. Write checks that make this easy:

- Name the specific file or artifact being checked.
- State what the expected result looks like.
- Make the evidence location obvious.

If a failure report would say only "check failed" with no path to correction, the check is too abstract.

## Retain reproducible evidence

Checks that depend on transient state — a running server, a live API, a temporary file — are fragile. When possible, write checks against persistent artifacts: committed files, saved outputs, logged results.

If a check must run against transient state, note this in the check description so the Checklist Agent and Stage Manager understand the constraint.

## Judgment checks: identify them clearly

When a check requires model judgment rather than mechanical verification, mark it explicitly. This helps the Checklist Agent calibrate its reporting — judgment checks are more likely to produce "unable to verify" results, and that is acceptable.

**Example:** "JUDGMENT: Does the error handling strategy cover the failure modes described in `reference/failure-modes.md`?"

The Checklist Agent applies the same truthfulness rules to judgment checks as to deterministic ones. It cannot soften a judgment-based failure into a pass just because the check is subjective.

---

**Related files:**

- [agents/golden-rules.md](../agents/golden-rules.md) — the 8 mandatory rules governing Checklist Agent behavior
- [agents/checklist-agent.md](../agents/checklist-agent.md) — the Checklist Agent's role, access, and report format
- [schemas/play-md.md](../schemas/play-md.md) — where checklists are defined within the Play file
