# Which Pattern Family Do I Need?

## Scenario

You have a specific problem or requirement and want to know which pattern family (A through O) contains the relevant solutions. This is the starting-point decision tree for navigating the catalog.

## Quick Answer

- **"How should work flow between steps?"** → [A: Workflow Topology](../../families/A-workflow-topology/)
- **"How do I break big tasks into smaller ones?"** → [B: Task Decomposition](../../families/B-task-decomposition/)
- **"How do multiple agents coordinate?"** → [C: Orchestration](../../families/C-orchestration/)
- **"How do I know if the output is correct?"** → [D: Verification & Evaluation](../../families/D-verification-evaluation/)
- **"How do I manage what the LLM sees?"** → [E: Context Engineering](../../families/E-context-engineering/)
- **"How do I set up the agent's environment?"** → [F: Harness & Environment](../../families/F-harness-environment/)

## Decision Tree

Start with your primary concern:

### "My agent produces wrong or unreliable results"

```
Is the output format wrong (invalid JSON, missing fields)?
  YES → D: Verification (D01 Deterministic Validator)
       + O: Output Integration (Schema Validation)
  NO ↓

Is the agent doing the right steps but getting a bad final answer?
  YES → D: Verification
        • D01 Deterministic Validator for known invariants
        • D09 LLM-as-Judge for rubric-based judgments
  NO ↓

Is the agent taking wrong actions or calling wrong tools?
  YES → G: Tool & Action Design (constrained tools)
       + H: Deterministic Control (override wrong paths)
  NO ↓

Is the agent looping or never finishing?
  YES → I: Reliability & Recovery (stop conditions, bounded retry)
       + A: Workflow Topology (bounded loop)
  NO ↓

Is the agent forgetting context or losing track?
  YES → E: Context Engineering (compaction, offloading)
       + L: Memory & State (checkpoint, scoped memory)
```

### "I need to design my agent architecture"

```
Is it a single task with defined steps?
  YES → A: Workflow Topology (prompt chaining, sequential)
  NO ↓

Does it need to break a complex goal into subtasks?
  YES → B: Task Decomposition (plan-execute, hierarchical)
  NO ↓

Does it need multiple specialized agents?
  YES → C: Orchestration (coordinator-specialists, handoff)
  NO ↓

Does it need to interact with external systems?
  YES → G: Tool & Action Design (typed schemas, idempotent wrappers)
       + F: Harness & Environment (sandboxing, capabilities)
  NO ↓

Start simple → A: Workflow Topology (single LLM call or prompt chain)
```

### "I have operational concerns"

```
Concern: Security / trust / permissions
  → J: Security & Trust (least privilege, permission boundaries)
  → K: Human Control (approval checkpoints)

Concern: Cost / speed / efficiency
  → N: Efficiency & Routing (model routing, caching, cost-aware stopping)

Concern: Debugging / understanding failures
  → M: Observability & Debugging (traces, event logs)
  → D: Verification (regression suite, failure analysis)

Concern: Human oversight / approval workflows
  → K: Human Control (human-in-the-loop, escalation)

Concern: State management / persistence
  → L: Memory & State (checkpoints, external state, sessions)

Concern: Output format / integration with downstream systems
  → O: Output Integration (schema validation, typed results)
```

## Family Quick-Reference Table

| Family | Core Question | Use When... |
|--------|--------------|-------------|
| **A** Workflow Topology | How does work flow? | Designing step sequences, loops, routing |
| **B** Task Decomposition | How to break it down? | Complex goals need subtask planning |
| **C** Orchestration | How do agents coordinate? | Multiple agents must collaborate |
| **D** Verification | Is the output correct? | Need quality assurance at any stage |
| **E** Context Engineering | What does the LLM see? | Context window limits, relevance, focus |
| **F** Harness & Environment | What's the agent's world? | Setting up execution environment, sandboxes |
| **G** Tool & Action Design | How does it act? | Defining and constraining tool interfaces |
| **H** Deterministic Control | When to override AI? | Hard rules that AI must not violate |
| **I** Reliability & Recovery | What if it fails? | Error handling, retries, graceful degradation |
| **J** Security & Trust | What's it allowed to do? | Permission scoping, trust boundaries |
| **K** Human Control | When do humans intervene? | Approval gates, oversight, escalation |
| **L** Memory & State | What does it remember? | Persistence, sessions, cross-turn memory |
| **M** Observability | What happened and why? | Debugging, tracing, understanding behavior |
| **N** Efficiency & Routing | How to do it cheaply/fast? | Cost optimization, model selection, caching |
| **O** Output Integration | How does output reach consumers? | Format guarantees, validation, sanitization |

## Common Combinations

Most real systems need patterns from multiple families. Here are frequent pairings:

| Building... | Primary Family | Usually Also Need |
|-------------|---------------|-------------------|
| Code generation agent | A + B | D (validation), F (sandbox), I (retry) |
| Customer support agent | A + C | E (context), K (escalation), J (data access) |
| Data pipeline agent | A + G | H (deterministic steps), O (output format) |
| Research/analysis agent | B + C | E (context limits), N (cost control), L (memory) |
| Multi-agent system | C | J (trust), M (observability), K (oversight) |

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
