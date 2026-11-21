# Guide: Harness Assessment Checklist

## Purpose

Use this checklist to evaluate whether your repository and development environment are ready for an agent to work in reliably. Most agent failures attributed to "model limitations" are actually harness failures — the environment does not give the agent what it needs to succeed.

---

## How to Use

Score each item: **Yes** (2), **Partial** (1), or **No** (0). A score below 16/30 indicates significant harness gaps that will cause agent failures regardless of model quality or prompt engineering.

---

## Section 1: Repository Legibility

Can the agent understand your codebase?

| # | Criterion | Score | Notes |
|---|---|---|---|
| 1.1 | There is a top-level instruction file (AGENTS.md, CLAUDE.md, or equivalent) that acts as a map to the repository | | |
| 1.2 | The instruction file is < 3,000 tokens (a map, not a manual) | | |
| 1.3 | Project conventions are documented in the repository (not in team Slack or someone's head) | | |
| 1.4 | File and folder naming is consistent and predictable (an agent can guess where things live) | | |
| 1.5 | There is no required "tribal knowledge" that is not written down anywhere | | |

**Section score:** ___/10

---

## Section 2: Feedback Loops

Can the agent verify its own work?

| # | Criterion | Score | Notes |
|---|---|---|---|
| 2.1 | The agent can run tests and see results (test suite exists and is runnable) | | |
| 2.2 | The agent can run a type checker or linter and see errors | | |
| 2.3 | The agent can build the project and see build errors | | |
| 2.4 | Feedback is fast (< 30 seconds for incremental check) | | |
| 2.5 | Error messages are actionable (they point to the problem, not just "build failed") | | |

**Section score:** ___/10

---

## Section 3: Mechanical Constraints

Are invariants enforced by code rather than instructions?

| # | Criterion | Score | Notes |
|---|---|---|---|
| 3.1 | Code style is enforced by formatters/linters (not just documented) | | |
| 3.2 | Architectural boundaries are enforced (import restrictions, dependency rules, schema validation) | | |
| 3.3 | Pre-commit hooks or CI checks catch violations before they merge | | |
| 3.4 | Security-critical rules (auth, input validation) are enforced by middleware/framework, not convention | | |
| 3.5 | The agent cannot accidentally bypass these constraints (no `--force` or `--no-verify` escape hatches in its tool set) | | |

**Section score:** ___/10

---

## Scoring Interpretation

| Score | Assessment | Recommended Action |
|---|---|---|
| 24–30 | Agent-ready | Minor refinements; focus on prompt quality |
| 16–23 | Partially ready | Fix gaps before expecting reliable agent output |
| 8–15 | Significant gaps | Invest in harness before investing in agent features |
| 0–7 | Not ready | The agent will fail regardless of model capability |

---

## Common Gaps and Quick Fixes

| Gap | Quick Fix | Time Investment |
|---|---|---|
| No instruction file | Write a 50-line map of the repo | 1 hour |
| Tests exist but agent can't run them | Add a single command the agent can invoke | 30 minutes |
| Conventions in Slack, not docs | Move top conventions into repo | 2 hours |
| No linter/formatter | Add Prettier/ESLint with default config | 1 hour |
| Error messages are cryptic | Add context to the 5 most common errors | 2 hours |

---

## When the Checklist Reveals Problems

If your score is below 16, the most effective investment is NOT better prompts — it is harness improvement. Consult these patterns:

- [F01 — Agent-Legible Repository](./patterns/F01-agent-legible-repository.md) — making the repo navigable
- [F02 — Repository-Local System of Record](./patterns/F02-repository-local-system-of-record.md) — documenting conventions in the repo
- [F03 — Executable Feedback Loop](./patterns/F03-executable-feedback-loop.md) — giving the agent verifiable feedback
- [F04 — Mechanical Architecture Constraints](./patterns/F04-mechanical-architecture-constraints.md) — enforcing rules with code

---

## Sources

- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- OpenAI — [Unrolling the Codex Agent Loop](https://openai.com/index/unrolling-the-codex-agent-loop/)
- OpenAI — [Unlocking the Codex Harness](https://openai.com/index/unlocking-the-codex-harness/)
