# Family I — Reliability & Recovery: Patterns

11 patterns covering how agents handle partial failure, loops, repeated mistakes, and loss of progress. These patterns are the cures for the **Infinite / Weakly Bounded Agent Loop** and **Retry Without New Information** anti-patterns documented in the sibling `anti-patterns/` folder.

---

## Practitioner entry points

- [Recover a drifting session](fresh-context-retry.md#in-a-session-recover-decisions-without-losing-useful-work) — the session returns to an abandoned approach or forgets a decision.
- [Turn feedback into a check](retry-with-feedback.md#in-a-session-turn-feedback-into-a-check) — the agent agrees with feedback but the fix is still wrong.

## File Tree

```
patterns/
├── README.md                         ← this file
├── bounded-retry.md                  ← hard numeric cap on retry attempts
├── checkpoint-and-resume.md          ← persist progress so work survives failures
├── circuit-breaker.md                ← open the circuit after N failures; stop hammering a broken resource
├── fallback-model-workflow.md        ← route to an alternative when the primary fails
├── fresh-context-retry.md            ← retry with a cleared or rebuilt context window
├── human-escalation.md               ← route unresolvable failures to a human
├── retry-with-feedback.md            ← inject failure details into the next attempt
├── root-cause-before-retry.md        ← diagnose before retrying; never retry blind
├── stop-condition.md                 ← define a testable success predicate before the loop starts
├── structured-error-classification.md ← classify errors before deciding how to handle them
└── validation-retry-loop.md          ← retry only when output fails a validation check
```

---

## File Descriptions

| File | What it covers |
|------|----------------|
| bounded-retry.md | Hard cap on loop iterations — guarantees termination regardless of what happens inside the loop; should be present in every retry loop |
| checkpoint-and-resume.md | Persist intermediate progress at defined points so a failed agent can resume from the last checkpoint rather than restarting |
| circuit-breaker.md | Track failure rate against a resource; open the circuit (stop attempts) after a threshold; attempt recovery after a cooldown |
| fallback-model-workflow.md | When the primary model or workflow fails, route to a pre-defined alternative (different model, cached data, simpler path) |
| fresh-context-retry.md | Retry with a rebuilt or truncated context window to escape failure modes caused by accumulated context confusion |
| human-escalation.md | Routing pattern: when automated recovery is exhausted, exit the loop and hand the task to a human with full diagnostic context |
| retry-with-feedback.md | On failure, include the error details, validation output, or diagnostic findings in the next prompt — never retry with identical input |
| root-cause-before-retry.md | Diagnose the failure before retrying; ensures each retry has a changed premise rather than repeating the same action |
| stop-condition.md | Define a testable success predicate before writing the loop; the success-based exit complementary to bounded-retry's failure-based exit |
| structured-error-classification.md | Classify errors by type (transient, permanent, retriable, non-retriable) before deciding whether and how to retry |
| validation-retry-loop.md | Retry only when output fails a validation check; the check result is injected as feedback into the next attempt |

---

## Schema

Each engineering pattern follows this structure:

| Section | Contents |
|---------|----------|
| Title | `# Pattern Name` |
| Family + Type tags | `**Family:** I — Reliability & Recovery` and `**Type:** Pattern` |
| Problem | What failure mode occurs without this pattern |
| Solution | The mechanism that prevents or recovers from that failure |
| Solution Structure | Mermaid flow diagram in a `<details>` block |
| Structure | Pseudocode showing the core implementation skeleton |
| When to Use | Conditions that call for this pattern |
| When Not to Use | Conditions where it would be wrong or counterproductive |
| Trade-offs | Pros/cons table |
| Example | Concrete scenario showing the pattern in action |
| Related Patterns | Cross-links within Family I with brief contrasts |
| Related Anti-Patterns | Links to `anti-patterns/` files this pattern directly addresses |
| Sources | AWS, Google Cloud, and/or Anthropic citations with URLs |

---

## How to Navigate

**"My loop never terminates."** — Start with `bounded-retry.md` (failure exit) and `stop-condition.md` (success exit). Every loop needs both.

**"My agent retries but never makes progress."** — `retry-with-feedback.md` and `root-cause-before-retry.md`. Retrying with identical input is the Retry Without New Information anti-pattern.

**"A downstream service is broken and the agent keeps hitting it."** — `circuit-breaker.md` stops the hammering; `fallback-model-workflow.md` routes around it.

**"The agent fails halfway through a long task and has to restart from zero."** — `checkpoint-and-resume.md`.

**"Different errors need different handling."** — `structured-error-classification.md` first; it feeds into bounded-retry, circuit-breaker, and human-escalation.

**"Nothing automated can fix this."** — `human-escalation.md` is the terminal exit for unresolvable failures.

**Dependency reading order for new readers:** `stop-condition` → `bounded-retry` → `structured-error-classification` → `retry-with-feedback` → `validation-retry-loop` → remaining patterns.

---

Last updated: 2026-08-24
