# 🎭 Claude Backstage

**Skills, workflows, scripts, and ideas behind my work with Claude Code.**

A growing collection of reusable tools and practical approaches to agent coordination, context management, and development automation. Each item includes its own documentation and examples.

## 🧩 [Skills](skills/README.md)

Reusable instructions that teach Claude Code how to perform specific tasks.

*Skills and usage guides will be listed here as they are added.*

---

## [Workflows](workflows/README.md)

Structured processes that bring agents, skills, and stages together.

### [Theater Model](theater-model/README.md)

Most multi-agent workflows fail the same way: context bloats, retries repeat mistakes, state scatters across conversations, and recovery means starting over. The Theater Model is a structured execution framework — built on 36 established design patterns from Anthropic, OpenAI, Google, AWS, Microsoft, and OWASP — that solves these problems architecturally, not with prompting tricks.

A **Play** defines the work. **Acts** break it into sequential steps. **Leads** and **Cast** do the work. A **Stage Manager** coordinates. A **Checklist Agent** verifies. A **Director** (human) decides at **Gates**. Every agent gets fresh context, bounded retries, and file-based state — producing cache-efficient, recoverable, auditable executions by default.

Need human approval before a critical step? Add a **Gate** — no agent has ever passed one autonomously, and the architecture makes it structurally impossible. Need confidence that an Act's output is correct before the next one begins? The **Checklist Agent** runs in a fresh, isolated context with no access to the generator's reasoning — zero confirmation bias, just evidence against criteria. Acts are self-contained with defined inputs and outputs, so a Play is composable like building blocks: swap an Act, add one, reorder the sequence. The model adapts to your workflow, not the other way around.

→ See [`theater-model/README.md`](theater-model/README.md) for the model, templates, and examples.

---

### [Iteration Harness](harness-core/README.md)

Shipping a skill that "works in the demo" is easy. Shipping one that survives real inputs, edge cases, and months of use is a different problem — and most iteration approaches amount to "run it, eyeball it, tweak it, repeat." The Iteration Harness replaces that with a structured methodology: define milestones, lock immutable tests, iterate through automated test-reason-fix-review cycles, and advance only when evidence says you're ready.

Tests are written first and locked after approval — the skill adapts to the tests, never the other way around. When tests fail, a **Reasoner** performs root-cause analysis and writes fix instructions. A **Skill-Change Agent** applies the fix with full version control. When tests pass, an independent **Review** act scores the skill across 8 quality dimensions. Findings go back through the Reasoner with explicit delta-acceptance thresholds — not every finding is worth fixing, and the system knows the difference.

The harness enforces strict separation of concerns: the test-runner can't edit skills, the skill-changer can't run tests, the reviewer can't modify anything. Agents communicate through files, not prompts. Every decision, fix, and review finding is a versioned artifact — making the entire development history auditable and recoverable.

→ See [`harness-core/README.md`](harness-core/README.md) for the full production guide, role definitions, and implementation details.

---

## 🛠️ [Scripts](scripts/README.md)

Utilities for automating repetitive work and supporting development workflows.

*Scripts and usage examples will be listed here as they are added.*

## 📚 [Docs](docs/README.md)

The models, methods, and design ideas behind the tools and workflows.

*Documentation will be listed here as it is added.*

## Exploring Backstage

This page highlights the main items. Category READMEs provide fuller catalogs, while individual folders contain detailed instructions, examples, and related resources.

The collection evolves as I build, test, and refine new approaches.
