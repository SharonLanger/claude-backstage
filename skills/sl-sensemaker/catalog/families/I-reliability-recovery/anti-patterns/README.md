# Family I — Reliability & Recovery: Anti-Patterns

2 named failure modes that the patterns in the sibling `patterns/` folder are designed to prevent. Read these to recognize the problem; read the linked patterns for the cures.

---

## File Tree

```
anti-patterns/
├── README.md                          ← this file
├── infinite-weakly-bounded-loop.md    ← loop with no hard exit; runs until external limit fires
└── retry-without-new-information.md   ← retry with identical input; never makes progress
```

---

## File Descriptions

| File | What it covers |
|------|----------------|
| infinite-weakly-bounded-loop.md | A loop with no hard numeric cap — or a cap so large it is effectively absent. Runs until context exhaustion, token budget depletion, or operator intervention. Covers recognition signals, why it happens, and the dual-exit (stop condition + bounded retry) cure. |
| retry-without-new-information.md | Retrying after a failure with the same prompt and no injected feedback. The model that failed once is statistically likely to fail the same way again. Covers how to detect this pattern and how to break it with feedback injection or root-cause diagnosis. |

---

## Schema

Both files follow this structure:

| Section | Contents |
|---------|----------|
| Title | `# Anti-Pattern Name` |
| Family + Type tags | `**Family:** I — Reliability & Recovery` and `**Type:** Anti-Pattern` |
| Problem | What goes wrong; what the failure looks like at runtime |
| Solution | The corrective approach and links to the patterns that implement it |
| Solution Structure | Mermaid diagram contrasting the anti-pattern with the correct structure |
| When to Use (Recognition Signals) | Observable signals that identify this anti-pattern in existing code |
| Why It Happens | Root causes — optimistic design, deferred hardening, framework omissions |
| Trade-offs | Table showing what the anti-pattern appears to provide vs. what it actually delivers |
| Example | Concrete scenario where the anti-pattern causes failure, followed by the correct fix |
| Related Patterns (Cures) | Links to `patterns/` files that directly fix this anti-pattern |
| Related Anti-Patterns | Cross-links to the other anti-pattern file (they frequently co-occur) |
| Sources | AWS, Google Cloud, and/or Anthropic citations with URLs |

---

## How to Navigate

**"Does my code have an infinite loop?"** — Read `infinite-weakly-bounded-loop.md`'s Recognition Signals section. Each signal is a concrete code smell to grep for.

**"My retries aren't helping — the agent keeps failing the same way."** — `retry-without-new-information.md`.

**"These two anti-patterns sound similar."** — They often co-occur but are distinct: infinite-weakly-bounded-loop is about *termination* (will the loop ever stop?); retry-without-new-information is about *progress* (is each attempt different from the last?). A loop can be bounded but still retry without new information, and vice versa.

**Going from diagnosis to cure:** Each file's "Related Patterns (Cures)" section links directly to the `patterns/` files that fix the problem. Start with `bounded-retry.md` and `stop-condition.md` for loop termination; `retry-with-feedback.md` and `root-cause-before-retry.md` for informationally static retries.

---

Last updated: 2026-08-24
