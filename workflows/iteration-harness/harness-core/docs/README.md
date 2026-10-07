# Docs

Human-readable documentation explaining the methodology — the "why" and "how it works" behind the scaffold. These docs complement the operational files (role definitions, iteration guide, test rules) with explanatory content for humans reading the repo.

---

## Reading Order

Start here, then follow the order below:

1. **[Iteration Algorithm](iteration-algorithm.md)** — the core 9-step loop (test → reason → fix → review → decide), with a flow diagram
2. **[Theater Model](theater-model.md)** — how agents are organized (acts, leads, cast), milestones, review dimensions
3. **[Walkthrough](walkthrough.md)** — guided tour through one full iteration cycle, connecting all mock files
4. **[Version Evolution](version-evolution.md)** — how skills improve over time, typical progression patterns
5. **[Design Patterns](design-patterns.md)** — 3 core patterns that define the system, plus a full 35-pattern reference appendix

The walkthrough is the best starting point if you want to see how everything fits together in practice.

---

## File Tree

```
docs/
├── README.md                  ← you are here
├── iteration-algorithm.md     ← the 9-step iteration loop + Mermaid flow diagram
├── theater-model.md           ← agent hierarchy, acts, roles, milestones, review dimensions
├── walkthrough.md             ← end-to-end guided tour connecting all mock files
├── version-evolution.md       ← how versions evolve, typical progression, what to expect
└── design-patterns.md         ← 3 core patterns + full 35-pattern reference appendix
```
