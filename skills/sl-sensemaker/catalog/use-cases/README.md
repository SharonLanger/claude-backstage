# Use-Cases: Scenario Index

Cross-cutting index for the AI/Agent Design Patterns catalog. Developers rarely arrive knowing which pattern family they need — they arrive with a problem. This folder maps those arrival points to the relevant families and anti-patterns.

---

## Directory Tree

```
use-cases/
├── README.md                          ← this file — master hub and quick-lookup index
│
├── onboarding/
│   ├── new-to-agents.md               ← "Start here" path for developers new to agent systems
│   └── mental-models.md               ← Core concepts to understand before reading any pattern
│
├── designing/
│   ├── new-system.md                  ← Building an agent system from scratch
│   ├── multi-agent.md                 ← Deciding whether and how to use multiple agents
│   ├── tool-design.md                 ← Designing tools and actions an agent can take
│   ├── memory-and-state.md            ← Deciding how agents remember and share information
│   └── output-integration.md         ← Connecting agent output to downstream systems
│
├── debugging/
│   ├── agent-not-completing.md        ← Agent loops, stalls, or never finishes
│   ├── wrong-outputs.md               ← Agent produces incorrect or unexpected results
│   ├── tool-failures.md               ← Tool calls failing, misused, or producing errors
│   ├── context-problems.md            ← Context window issues, lost state, prompt degradation
│   └── non-determinism.md             ← Flaky behavior, inconsistent results across runs
│
├── security/
│   ├── security-review.md             ← Full security review checklist for agent systems
│   ├── prompt-injection.md            ← Protecting against prompt injection and hijacking
│   └── privilege-and-trust.md         ← Least-privilege design, trust boundaries, sandboxing
│
├── cost-and-performance/
│   ├── reducing-cost.md               ← Cutting token usage and API spend
│   ├── latency.md                     ← Reducing end-to-end latency
│   └── routing-and-scaling.md         ← Routing requests to right model/tier, scaling patterns
│
├── human-in-the-loop/
│   ├── when-to-interrupt.md           ← Deciding when agents should pause for human input
│   └── approval-workflows.md          ← Designing review gates and approval checkpoints
│
├── evaluation/
│   ├── evaluating-agents.md           ← How to measure if an agent system is working
│   ├── regression-testing.md          ← Detecting regressions after changes
│   └── evals-from-errors.md           ← Building evals from production failures (not generically)
│
└── decision-trees/
    ├── which-family.md                ← "I have X problem — which family?" decision tree
    ├── architecture-choices.md        ← Key architecture forks with tradeoffs
    └── anti-pattern-detector.md       ← Symptoms → which anti-pattern you may have
```

---

## New to Agents? Start Here

1. **`onboarding/mental-models.md`** — Build the conceptual foundation: what agents are, how orchestration works, why patterns matter.
2. **`onboarding/new-to-agents.md`** — A curated reading path through the catalog. Starts with the 3 families every system needs, then branches by what you're building.
3. **`designing/new-system.md`** — First design decisions when starting from scratch.
4. **`decision-trees/which-family.md`** — Once you have a concrete problem, use this to land in the right family.

---

## Master Quick-Lookup Table

Arrive with a scenario. Find your families and watch out for the anti-patterns listed.

| Scenario | Start here | Watch for Anti-Patterns |
|---|---|---|
| Building an agent system from scratch | A, B, C | Multi-Agent by Default; Giant Instruction Manual |
| Choosing workflow topology (sequential vs parallel vs DAG) | A, C | Infinite/Weakly Bounded Agent Loop |
| Decomposing a complex task into subtasks | B, C | Multi-Agent by Default; Prompt-as-Policy |
| Designing tools/actions for an agent | G, F | Overpowered Coding Agent; Model as Security Boundary |
| Agent loops or never finishes | H, I, A | Infinite/Weakly Bounded Agent Loop; Retry Without New Information |
| Agent produces wrong or hallucinated outputs | D, E, L | Self-Certified Completion; Generic Evals Before Error Analysis |
| Tool calls are failing or being misused | G, D, F | Self-Certified Completion |
| Context window filling up / state lost | E, L | Shared Context Everywhere; Giant Instruction Manual |
| Non-deterministic / flaky behavior | H, D, M | Self-Certified Completion; Retry Without New Information |
| Debugging a production agent failure | M, D, I | Generic Evals Before Error Analysis |
| Security review of an agent system | J, G, K | Model as Security Boundary; Overpowered Coding Agent; Prompt-as-Policy |
| Protecting against prompt injection | J | Model as Security Boundary |
| Least-privilege and trust boundary design | J, K, G | Overpowered Coding Agent; Model as Security Boundary |
| Reducing cost (tokens / API spend) | N, E, B | Shared Context Everywhere; Multi-Agent by Default |
| Reducing latency | N, A, C | Multi-Agent by Default |
| Routing to right model or tier | N, A | — |
| Deciding when to pause for human input | K, H | Infinite/Weakly Bounded Agent Loop; Self-Certified Completion |
| Designing approval gates and review checkpoints | K, H, D | Self-Certified Completion |
| How agents remember and share state | L, E | Shared Context Everywhere |
| Connecting agent output to downstream systems | O, G | — |
| Measuring if an agent system is working | D, M | Generic Evals Before Error Analysis; Self-Certified Completion |
| Building evals after production failures | D, M | Generic Evals Before Error Analysis |
| Decisions or requirements lost in a long session | [Context problems](debugging/context-problems.md) | Giant Instruction Manual; Retry Without New Information |
| Coding agent changed the test that defines success | [Regression testing](evaluation/regression-testing.md) | Overpowered Coding Agent |
| Regression testing after changes | D, M, F | Generic Evals Before Error Analysis |
| Multi-agent: do I need it? | A, B, C | Multi-Agent by Default |
| Multi-agent: how to orchestrate | C, A, J | Shared Context Everywhere; Model as Security Boundary |
| Instruction/prompt design is getting unwieldy | E, B | Giant Instruction Manual; Prompt-as-Policy |
| Agent keeps retrying the same failing action | I, H | Retry Without New Information |
| Observability — can't see what the agent did | M, F | — |

---

## Family Reference (A–O)

| Code | Family | One-liner |
|---|---|---|
| A | workflow-topology | Shape of the agent graph: linear, parallel, DAG, loop |
| B | task-decomposition | Breaking work into subtasks; what stays together vs splits |
| C | orchestration | Coordinating agents: who directs whom, handoffs, routing |
| D | verification-evaluation | Checking outputs are correct; evals and judges |
| E | context-engineering | What goes in the prompt; compression, retrieval, windowing |
| F | harness-environment | The runtime the agent lives in; sandboxing, execution environment |
| G | tool-action-design | Designing the tools agents call; scope, safety, idempotency |
| H | deterministic-control | Forcing predictable behavior; constraints, structured output, guardrails |
| I | reliability-recovery | Handling failures gracefully; retries, fallbacks, checkpointing |
| J | security-trust | Trust boundaries, privilege, injection, adversarial inputs |
| K | human-control | When and how humans stay in the loop; interrupts, approvals |
| L | memory-state | How agents store, retrieve, and share state across time |
| M | observability-debugging | Logging, tracing, inspecting what agents actually did |
| N | efficiency-routing | Cost, latency, model selection, caching, routing |
| O | output-integration | Getting agent output into downstream systems safely |

---

## Anti-Pattern Reference

| Anti-Pattern | Core Problem | Key Families to Consult |
|---|---|---|
| Self-Certified Completion | Agent reports done without verifying | D, K |
| Prompt-as-Policy | Instructions encode business logic instead of behavior | E, B |
| Giant Instruction Manual | Monolithic prompt that can't be maintained or debugged | E, B |
| Retry Without New Information | Looping on failure without changing conditions | I, H |
| Multi-Agent by Default | Adding agents for complexity's sake, not capability | A, B, C |
| Model as Security Boundary | Trusting the model to enforce security guarantees | J, G |
| Shared Context Everywhere | All agents share one context; no isolation | L, E, J |
| Generic Evals Before Error Analysis | Running broad evals before understanding real failures | D, M |
| Infinite/Weakly Bounded Agent Loop | No termination condition; agent runs indefinitely | H, A |
| Overpowered Coding Agent | Agent given write access far beyond task scope | G, J, K |

---

Last updated: 2026-08-24
