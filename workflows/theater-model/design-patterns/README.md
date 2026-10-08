# Design Patterns

The Theater Model wasn't designed by intuition and then justified after the fact. It was built on top of established AI agent design patterns — the same patterns published by Anthropic, OpenAI, Google, AWS, Microsoft, and OWASP as best practices for building reliable, efficient, and controllable agent systems.

This folder traces **36 of those patterns** back to the specific structural decisions in the Theater Model that implement them.

## Why this matters

Most multi-agent frameworks solve one problem well and ignore the rest. They optimize for orchestration but leak context. They add retries but lose state. They checkpoint but don't scope. The Theater Model's architecture addresses four concerns simultaneously — not because it tries to do everything, but because the same structural choices (fresh agents, file-based state, fixed decomposition, role-scoped loading) produce multiple benefits at once.

That's not a coincidence. It's what happens when the underlying patterns reinforce each other instead of competing.

## The four benefits

| Benefit | What it means | Why it's hard to get without the right patterns |
|---------|---------------|--------------------------------------------------|
| **Consolidation** | One folder is the entire system of record | Most systems scatter state across conversations, databases, and memory — making recovery a reconstruction project |
| **Cache efficiency** | Stable structure produces high prompt-cache hit rates | Dynamic prompt construction defeats caching; fixed decomposition + file-based references make it structural |
| **Recoverability** | Bounded failure, structured recovery, zero re-work | Retries without checkpoints re-do work; retries without fresh context repeat mistakes; retries without bounds burn money |
| **Minimal context** | Each agent loads only what it needs | Shared-context architectures grow quadratically; the Theater Model's context is O(1) per agent regardless of Play size |

## In this folder

| File | What it covers |
|------|----------------|
| [consolidation.md](consolidation.md) | 8 patterns — how file-based state eliminates external dependencies |
| [cache-efficiency.md](cache-efficiency.md) | 12 patterns — how fixed structure and `@` references maximize prompt caching |
| [recoverability.md](recoverability.md) | 15 patterns — how bounded retries, checkpoints, and escalation prevent waste |
| [minimal-context.md](minimal-context.md) | 15 patterns — how role-scoping and fresh agents keep context small and focused |
| [pattern-summary.md](pattern-summary.md) | Cross-reference table of all 36 patterns with source publication links |

Each file describes the benefit in plain terms, explains how the Theater Model achieves it structurally, and includes a table mapping each relevant pattern to its implementation — with every pattern name linking to the original published research.
