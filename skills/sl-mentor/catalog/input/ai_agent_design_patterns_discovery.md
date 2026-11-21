# AI / Agent Design Patterns — Discovery Research

**Status:** Discovery phase — evidence gathering before freezing the taxonomy  
**Date:** 2026-08-24  
**Scope:** Model-independent, reusable engineering patterns for developers working with LLMs and coding agents, with emphasis on day-to-day practices and a secondary focus on advanced agent architectures.

---

## 1. Executive Discovery Summary

The field does not yet have one universally accepted “Gang of Four” catalog for AI/agent development. Instead, several overlapping vocabularies are converging around the same recurring engineering problems: workflow decomposition, orchestration, context management, tool use, verification/evaluation, reliability/recovery, security boundaries, human control, memory/state, observability, cost/latency, and the surrounding agent harness.

The strongest discovery is that the field is moving away from “prompt engineering” as the primary unit of design. Leading sources increasingly describe the important engineering work as designing **systems around the model**: workflows, tools, context, persistent state, evaluation, feedback loops, deterministic enforcement, sandboxes, and orchestration.

A second strong convergence is **simplicity before autonomy**. Anthropic, OpenAI, Google, AWS, and Microsoft all independently recommend avoiding unnecessary agentic complexity: use deterministic code when possible, start with a single agent or fixed workflow, and add multi-agent/model-driven orchestration only when the task genuinely requires it.

A third convergence is that **verification must be externalized**. Strong sources repeatedly distinguish between a model producing a result and a system establishing that the result is correct. Deterministic validators, tests, structured checks, independent critics/evaluators, human review, and task-success evals repeatedly appear as more reliable mechanisms than accepting the agent’s own declaration of completion.

A fourth convergence is that **security is architectural, not merely prompting**. OWASP, AWS, OpenAI, and independent security practitioners emphasize least privilege, sandboxing, tool gates, authorization outside the model, session/context isolation, and preventing the combination of private data + untrusted content + external communication.

Finally, a distinct **harness engineering** discipline is emerging around coding agents. OpenAI explicitly uses this term to describe engineering the repository, tools, instructions, feedback loops, tests, observability, architectural invariants, and execution environment that allow coding agents to work reliably. Community usage in 2026 strongly mirrors this framing.

---

# 2. Working Definition

> **An AI / agent design pattern is a reusable solution structure for a recurring engineering problem that appears when building or working with probabilistic models or autonomous agents.**

A pattern should usually contain:

1. A recurring problem or failure mode.
2. A reusable structural response.
3. Defined responsibilities or boundaries.
4. Trade-offs.
5. Conditions under which it should or should not be used.
6. At least one concrete implementation shape.
7. Preferably independent evidence that the shape recurs across sources or systems.

Keep these distinct:

- **Principle** — “Do not blindly trust probabilistic output.”
- **Pattern** — “Independent Verifier.”
- **Technique** — “Run a second model with isolated context and require PASS/FAIL.”
- **Best practice** — “Run tests before declaring completion.”
- **Architecture** — an entire agent platform or workflow containing several patterns.
- **Anti-pattern** — a recurring structure that causes failure, such as self-certified completion.

---

# 3. How the Discovery Was Conducted

The discovery intentionally did **not** begin by treating the initial 15 families as fixed. Instead, sources were sampled across several evidence classes:

## Primary / high-authority engineering sources
- Anthropic Engineering
- OpenAI Engineering
- Google Cloud Architecture Center
- AWS Prescriptive Guidance
- Microsoft Azure Architecture Center
- OWASP GenAI Security Project

## Practitioner / expert sources
- Hamel Husain
- Shreya Shankar
- Simon Willison
- LangChain engineering material and talks

## Academic / teaching sources
- Stanford CS224G Agentic Design Patterns material
- Andrew Ng’s widely-used framing of reflection, tool use, planning, and multi-agent collaboration

## Open source / community sources
- GitHub agent-pattern catalogs
- AWS sample implementations
- Coding-agent harness projects
- Reddit / Claude Code workflow discussions
- Community attempts to formalize GoF-like agent-pattern catalogs

Search terms included:
`agentic design patterns`, `agent workflow patterns`, `agent architecture`, `coding agent workflow`, `AI engineering patterns`, `LLM application patterns`, `context engineering`, `harness engineering`, `agent reliability`, `agent evaluation`, `agent observability`, `agent security`, `tool-use patterns`, `human-in-the-loop`, `multi-agent orchestration`, `AI anti-patterns`, `agent failure modes`.

---

# 4. Major Source Families and What Each Contributes

## 4.1 Anthropic — simple composable agentic workflows

### Key sources
- Building Effective Agents  
  https://www.anthropic.com/engineering/building-effective-agents
- Effective Context Engineering for AI Agents  
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Demystifying Evals for AI Agents  
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

### Main contribution
Anthropic provides one of the clearest workflow taxonomies:
- Prompt chaining
- Routing
- Parallelization
- Orchestrator-workers
- Evaluator-optimizer
- Autonomous agents

It also draws a critical boundary:

- **Workflow:** code predetermines the control flow.
- **Agent:** the model dynamically controls its process and tool usage.

### Important principles discovered
- Start with the simplest solution.
- Add complexity only when it demonstrably improves outcomes.
- Fixed workflows are preferable when the task structure is known.
- Agents are preferable when flexibility is genuinely required.
- Agents need environmental “ground truth” from tool outputs/code execution.
- Explicit stopping conditions matter.
- Tool interfaces are part of the agent-computer interface and must be carefully designed and tested.
- Context engineering is broader than prompt engineering and includes the entire evolving token state.

### Pattern implications
Strong support for:
- Sequential / chaining
- Routing
- Parallel sectioning
- Parallel voting
- Orchestrator-workers
- Generator/critic
- Evaluator-optimizer
- Ground-truth feedback
- Bounded loop
- Human checkpoint
- Context curation
- Tool-interface design

---

## 4.2 OpenAI — harness engineering, orchestration, tools and guardrails

### Key sources
- Harness Engineering: Leveraging Codex in an Agent-First World  
  https://openai.com/index/harness-engineering/
- A Practical Guide to Building Agents  
  https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- Unrolling the Codex Agent Loop  
  https://openai.com/index/unrolling-the-codex-agent-loop/
- Unlocking the Codex Harness  
  https://openai.com/index/unlocking-the-codex-harness/
- Open-Source Codex Orchestration: Symphony  
  https://openai.com/index/open-source-codex-orchestration-symphony/

### Main contribution
OpenAI has made **harness engineering** explicit: reliable agent behavior depends heavily on the system around the model rather than only on model intelligence.

The Codex harness encompasses:
- Agent loop
- Thread lifecycle and persistence
- Configuration/authentication
- Tool execution
- Sandboxing
- MCP/skills
- Policy
- State
- Review and feedback loops
- Observability
- Repository-level structure

### Important engineering findings
OpenAI’s internal Codex project reported that the main bottleneck was often not model capability but an **underspecified environment**.

Strong practical patterns in the Harness Engineering article include:
- Humans specify intent; agents execute.
- Break large goals into smaller design/code/review/test building blocks.
- Treat failures as evidence of a missing capability or missing constraint, not merely a cue to “try harder.”
- Keep a short `AGENTS.md` as a **map**, not a giant manual.
- Put deeper knowledge in structured repository-local documentation.
- Make the repository the system of record.
- Prefer agent-legible, versioned artifacts.
- Enforce architectural invariants mechanically.
- Use linters/structural tests rather than relying on instructions for must-hold rules.
- Agents review other agents.
- Build feedback loops from tests, traces and runtime behavior.
- Automate end-to-end validation and evidence collection where possible.

### Pattern implications
Strong support for:
- Progressive disclosure / map-not-manual
- Repository-as-system-of-record
- Agent-legible environment
- Deterministic architecture enforcement
- Agent-to-agent review
- Evidence-producing validation
- Tool/harness boundary
- Persistent execution state
- Automated feedback loop
- Increasing autonomy only as the harness becomes capable enough

---

## 4.3 Google — explicit agent design-pattern taxonomy

### Key source
- Choose a Design Pattern for Your Agentic AI System  
  https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system

### Main contribution
Google explicitly calls these **agent design patterns** and frames pattern choice around:
- Task characteristics
- Latency/performance
- Cost
- Human involvement

### Patterns directly named
- Single-agent
- Sequential multi-agent
- Parallel multi-agent
- Loop
- Iterative refinement
- Review and critique / generator-critic
- Coordinator
- Hierarchical task decomposition
- ReAct
- Human-in-the-loop

### Important principles
- Predictable workflows often do not need model-driven orchestration.
- Single-agent systems are the recommended starting point.
- Multi-agent complexity introduces evaluation, security, reliability, access-control, and cost burdens.
- Context engineering includes isolation, persistence, and compression.
- Loop patterns require strong termination conditions to avoid runaway execution/cost.
- Hierarchical decomposition has a real quality/complexity/cost trade-off.

### Pattern implications
Google’s taxonomy strongly validates that workflow topology itself is a legitimate pattern family.

---

## 4.4 AWS — deterministic boundaries, tool gates, memory security and modular patterns

### Key sources
- Agentic AI Patterns and Workflows  
  https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html
- Agent Patterns  
  https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
- System Design and Security Recommendations  
  https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html
- Tool Scope / MCP Strategy  
  https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html
- Agentic Design Pattern Sample Repository  
  https://github.com/aws-samples/sample-agentic-design-patterns

### Main contribution
AWS explicitly defines agentic patterns as reusable, composable building blocks. It also introduces a useful distinction between reasoning that genuinely needs AI and rules that should remain deterministic.

### Particularly useful candidate patterns
The AWS sample catalog contains names such as:
- Agentic Loop
- Deterministic Override
- Tool Gate
- Validation-Retry Loop
- Structured Error Classification
- Confidence-Based Routing
- Review Pass
- Coordinator-Subagent Hierarchy

### Important principles
- Use deterministic execution logic unless AI is needed.
- Separate read and write capabilities where practical.
- Tool interfaces should be designed for the LLM, not simply expose every underlying API.
- Prefer deterministic tool execution.
- Use an agent-as-tool only when intelligent branching is actually necessary.
- Shared memory should be treated as partially trusted.
- Use a deterministic gateway/proxy for shared-memory validation in higher-risk systems.
- Session isolation prevents cross-task/context contamination.

### Pattern implications
AWS is particularly strong evidence for a family of **deterministic control patterns** that our initial taxonomy did not name clearly enough.

---

## 4.5 Microsoft — orchestration as distributed-systems engineering

### Key source
- AI Agent Orchestration Patterns  
  https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns

### Main contribution
Microsoft treats multi-agent orchestration as a distributed-system problem and stresses:
- explicit handoffs
- context compaction
- external persistent state
- per-agent and end-to-end observability
- integration testing
- human participation

### Important principles
- Do not pass accumulated context if the next agent does not need it.
- Persist long-running state externally instead of trusting only conversational context.
- Instrument every agent operation and handoff.
- Test both agents individually and the system as a whole.
- Multi-agent workflows require distributed-systems thinking.

### Pattern implications
Strong evidence for:
- Minimal-context handoff
- Context compaction between stages
- External durable state
- Instrumented handoff
- Per-agent testability
- End-to-end orchestration testing

---

## 4.6 Hamel Husain & Shreya Shankar — evaluation as failure discovery, not generic scoring

### Key sources
- Evals Skills for Coding Agents  
  https://hamel.dev/blog/posts/evals-skills/
- LLM Evals FAQ  
  https://hamel.dev/blog/posts/evals-faq/
- How Do I Evaluate Agentic Workflows?  
  https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html
- Why Is Error Analysis So Important?  
  https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html

### Main contribution
This body of work provides a strong corrective to generic “LLM-as-a-judge” thinking.

The recommended sequence is:
1. Inspect real traces.
2. Discover actual failure modes.
3. Build a failure taxonomy.
4. Define task-specific success criteria.
5. Evaluate end-to-end task success first.
6. Use step-level diagnostics after locating failing workflows.
7. Validate automated evaluators against human labels.

### Important principles
- Error analysis should precede generic eval metrics.
- Product evals measure whether **your system performs your task on your data**, not whether the foundation model is globally capable.
- End-to-end task success is the first question.
- Step-level diagnostics are for understanding why an already-identified failure occurred.
- “Hallucination” is often too broad a category to be useful.
- LLM judges themselves require validation/calibration.

### Pattern implications
Strong support for:
- Failure-taxonomy-first
- Task-success evaluation
- Trace-driven evaluation
- First-upstream-failure analysis
- Validated evaluator
- Human calibration loop
- Eval-as-feedback-system

---

## 4.7 Simon Willison + OWASP — prompt injection and trust boundaries

### Key sources
- Simon Willison — The Lethal Trifecta for AI Agents  
  https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Simon Willison — Living Dangerously with Claude  
  https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/
- OWASP Top 10 for Agentic Applications 2026  
  https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP LLM Top 10  
  https://genai.owasp.org/llm-top-10/
- OWASP Prompt Injection  
  https://genai.owasp.org/llmrisk/llm01-prompt-injection/

### Main contribution
Security research strongly rejects the idea that prompting alone can create a trustworthy security boundary.

Simon Willison’s useful “lethal trifecta” is:
1. Access to private data.
2. Exposure to untrusted content.
3. Ability to communicate externally.

Combining all three creates a powerful exfiltration path after prompt injection.

OWASP’s agentic risk taxonomy includes areas such as:
- Agent goal hijacking
- Tool misuse
- Identity/privilege abuse
- Agentic supply-chain vulnerabilities
- Unexpected code execution

### Important principles
- Treat untrusted context as attacker-controlled.
- Do not give the model authority that can be enforced deterministically elsewhere.
- Apply least privilege.
- Isolate secrets.
- Reduce blast radius.
- Sandboxing and authorization belong outside model reasoning.
- Security depends heavily on tool capabilities and context provenance.

### Pattern implications
Strong support for:
- Least-privilege agent
- Trust-boundary separation
- Untrusted-context isolation
- Read/write capability separation
- Tool gateway
- Deterministic authorization
- Human approval for high-impact side effects
- Sandbox
- External-communication restriction

---

## 4.8 LangChain / context-engineering community

### Key material
- Context Engineering for Agents (LangChain talk/blog ecosystem)
- Later materials describe common operations as **write/select/compress/isolate** and **offload/reduce/isolate**.

### Main contribution
The context-engineering literature reframes the problem from “write a better prompt” to:

> Which subset of all available information should be visible to this model at this exact step?

Recurring strategies include:
- Write useful state outside the immediate context.
- Select only relevant information.
- Compress/summarize older information.
- Isolate context across subagents/tasks.
- Offload large references and intermediate work to files.
- Use progressive disclosure for tools and documentation.

### Pattern implications
Strong support for:
- Progressive disclosure
- Context isolation
- Context offloading
- Context compaction
- Just-in-time retrieval
- Role-scoped context
- Artifact-based handoff

---

# 5. Discovered Pattern Families

The initial 15 families remain useful, but discovery suggests several refinements.

## Family A — Workflow Topology

Recurring problem: a single model call is too coarse, or the task requires structured progression.

Candidate patterns:
- Prompt chaining
- Sequential workflow
- Routing
- Parallel sectioning
- Parallel voting
- Iterative refinement
- Generator-critic
- Evaluator-optimizer
- ReAct
- Bounded loop

**Confidence:** Very high  
**Evidence:** Anthropic, Google, AWS, Stanford/Ng, open-source catalogs.

---

## Family B — Task Decomposition & Planning

Recurring problem: large/ambiguous tasks overload one reasoning step.

Candidate patterns:
- Plan → execute
- Hierarchical task decomposition
- Dynamic decomposition
- Fixed decomposition
- Milestone/checkpoint planning
- Reconnaissance-before-implementation

**Confidence:** High  
**Evidence:** Google, Anthropic, OpenAI harness practice, community coding-agent workflows.

---

## Family C — Orchestration & Role Separation

Recurring problem: one agent has too many responsibilities or needs dynamic specialization.

Candidate patterns:
- Manager → workers
- Orchestrator → workers
- Coordinator → specialists
- Agent-as-tool
- Decentralized handoff
- Hierarchical coordinator
- Specialist reviewer
- Synthesizer/aggregator
- Maker-checker

**Confidence:** Very high  
**Evidence:** OpenAI, Google, Anthropic, AWS, Microsoft.

---

## Family D — Verification & Evaluation

Recurring problem: generated work may look plausible without satisfying the real task.

Candidate patterns:
- Deterministic validator
- Test-before-done
- Evidence-based completion
- Independent verifier
- Review pass
- Generator-critic
- Evaluator-optimizer
- Multi-review / ensemble
- LLM-as-judge
- Human calibration
- End-to-end task-success eval
- Step-level diagnostic eval

**Confidence:** Very high  
**Evidence:** Hamel/Shreya, Anthropic, Google, AWS, OpenAI coding practice.

---

## Family E — Context Engineering

Recurring problem: too little, too much, stale, conflicting, or irrelevant context reduces performance.

Candidate patterns:
- Map-not-manual
- Progressive disclosure
- Context isolation
- Minimal-context handoff
- Just-in-time retrieval
- Context compaction
- Context offloading
- Role-scoped context
- Artifact-based handoff
- Repository-as-system-of-record

**Confidence:** Very high  
**Evidence:** Anthropic, OpenAI Harness Engineering, Microsoft, LangChain, Google.

---

## Family F — Harness / Environment Engineering

Recurring problem: model capability alone is insufficient for reliable long-horizon software work.

Candidate patterns:
- Agent-legible repository
- Repository-local system of record
- Executable feedback loop
- Mechanical architecture constraints
- Agent-accessible tools
- Structured repository instructions
- Agent skills/procedures
- Sandboxed execution
- Persistent task artifacts
- Agent-to-agent review
- Capability-gap feedback

**Confidence:** High and rapidly increasing  
**Evidence:** OpenAI explicitly uses “harness engineering”; community usage in 2026 strongly converges on the same concept.

---

## Family G — Tool and Action Design

Recurring problem: the model must translate ambiguous intent into safe deterministic actions.

Candidate patterns:
- Typed/schema-constrained tool
- Narrow tool interface
- Tool gateway
- Agent-as-tool
- Read/write separation
- Tool gate
- Deterministic tool execution
- Tool result validation
- Tool discovery / progressive exposure
- Idempotent action wrapper

**Confidence:** Very high  
**Evidence:** OpenAI, AWS, Anthropic, OWASP.

---

## Family H — Deterministic Control Boundaries

**Newly elevated family discovered during research.**

Recurring problem: developers encode must-hold rules in prompts even though the rule can be enforced mechanically.

Candidate patterns:
- Deterministic override
- Programmatic gate
- Structural test
- Policy hook
- Typed boundary
- Schema validator
- Authorization outside the model
- Non-AI fallback path

Core rule:

> If a property can be checked or enforced deterministically, do not rely solely on probabilistic obedience.

**Confidence:** Very high  
**Evidence:** AWS, OpenAI Harness Engineering, Anthropic prompt-chaining gates, OWASP security principles.

---

## Family I — Reliability & Recovery

Recurring problem: agents fail partially, loop, repeat mistakes, or lose progress.

Candidate patterns:
- Validation-retry loop
- Retry-with-feedback
- Structured error classification
- Bounded retry
- Stop condition
- Human escalation
- Checkpoint and resume
- Fresh-context retry
- Fallback model/workflow
- Circuit breaker
- Root-cause-before-retry

**Confidence:** High  
**Evidence:** OpenAI, Google, AWS, community long-horizon harnesses.

---

## Family J — Security & Trust Boundaries

Recurring problem: model-controlled actions can cross security boundaries after prompt injection or model error.

Candidate patterns:
- Least privilege
- Sandbox
- Secret isolation
- Tool gateway
- Deterministic authorization
- Untrusted-context isolation
- Session isolation
- Human approval gate
- External-communication restriction
- Capability minimization
- Read/write separation

**Confidence:** Very high  
**Evidence:** OWASP, Simon Willison, AWS, OpenAI.

---

## Family K — Human Control

Recurring problem: not every decision should be autonomous.

Candidate patterns:
- Human-in-the-loop checkpoint
- High-risk action gate
- Failure-threshold escalation
- Review-before-side-effect
- Draft/preview-before-apply
- Human-on-the-loop monitoring

**Confidence:** Very high  
**Evidence:** Google, OpenAI, Microsoft, OWASP.

---

## Family L — Memory & State

Recurring problem: long-running work cannot rely solely on an ever-growing conversational context.

Candidate patterns:
- External durable state
- Artifact state
- Checkpoint state
- Shared-memory gateway
- Session isolation
- Scoped memory
- Summarized memory
- State machine
- Provenance-tagged memory

**Confidence:** High  
**Evidence:** Microsoft, AWS, Google, OpenAI harness/thread persistence.

---

## Family M — Observability & Debugging

Recurring problem: when an agent fails, developers often cannot reconstruct what actually happened.

Candidate patterns:
- Structured trace
- Tool-call event log
- Agent/subagent execution tree
- Instrumented handoff
- Artifact lineage
- Token/cost metrics
- Replayable run
- Trace-linked eval
- Failure categorization

**Confidence:** High  
**Evidence:** Microsoft, Hamel/Shreya, OpenAI harness, AWS.

---

## Family N — Efficiency & Model Routing

Recurring problem: reliability improvements can make inference unnecessarily slow or expensive.

Candidate patterns:
- Complexity-based model routing
- Confidence-based routing
- Small-model-first escalation
- Parallel execution
- Context minimization
- Caching
- Tool/result reuse
- Budgeted agent loop
- Cost-aware stopping

**Confidence:** High  
**Evidence:** Anthropic routing, Google pattern-selection criteria, AWS confidence routing, OpenAI production concerns.

---

## Family O — Output & Integration Boundaries

Recurring problem: natural-language model output must safely enter deterministic software.

Candidate patterns:
- Structured output boundary
- Schema validation
- Typed result object
- Parse-and-reject
- Programmatic postcondition
- Sanitized output boundary

**Confidence:** Very high  
**Evidence:** OpenAI tool/guardrail guidance, AWS schema validation and structured tool calls, OWASP improper-output handling.

---

# 6. Important Anti-Patterns / Failure Modes Discovered

These should be researched as first-class entries because many good patterns are simply structural answers to these failures.

## 6.1 Self-Certified Completion
Agent performs task → agent says “done” → no independent evidence.

Counter-patterns:
- Test-before-done
- Independent verifier
- Evidence-based completion
- Deterministic validation

---

## 6.2 Prompt-as-Policy
A must-hold security, architecture, or correctness rule exists only as natural-language instruction.

Counter-patterns:
- Deterministic override
- Structural test
- Tool gate
- Policy hook
- Authorization outside the model

---

## 6.3 Giant Instruction Manual
Every rule/reference is injected into one huge `AGENTS.md`, `CLAUDE.md`, or system prompt.

Observed risks:
- Context crowding
- Low salience
- Staleness
- Weak navigability
- Hard-to-verify documentation coverage

Counter-patterns:
- Map-not-manual
- Progressive disclosure
- Repository system of record
- Just-in-time retrieval

---

## 6.4 Retry Without New Information
The agent fails and is simply told to retry.

Observed risk:
- Repeated identical failure
- Token waste
- False progress

Counter-patterns:
- Structured error classification
- Retry-with-feedback
- Root-cause-before-retry
- Fresh-context retry
- Human escalation

---

## 6.5 Multi-Agent by Default
A system uses teams of agents when a single deterministic workflow or single agent would suffice.

Observed costs:
- More inference
- More context management
- Harder debugging
- More security surfaces
- Coordination failures
- Higher latency

Counter-principle:
- Start simple and prove the need for additional agents.

---

## 6.6 Model as Security Boundary
The model decides whether it is authorized to perform a sensitive action.

Counter-patterns:
- Deterministic authorization
- Least privilege
- Tool gateway
- Human approval
- Capability scoping

---

## 6.7 Shared Context Everywhere
All agents receive all history/reference material.

Risks:
- Token growth
- Context pollution
- instruction conflicts
- privacy leakage
- lower task focus

Counter-patterns:
- Minimal-context handoff
- Context isolation
- Scoped memory
- Compaction

---

## 6.8 Generic Evals Before Error Analysis
The team adopts generic “hallucination” or quality metrics without studying real failures.

Counter-pattern:
- Trace review → failure taxonomy → task-specific evals.

---

## 6.9 Infinite / Weakly Bounded Agent Loop
Autonomous loop continues until the model informally believes it is complete.

Counter-patterns:
- Explicit terminal states
- Maximum iteration/token/time budgets
- Objective completion criteria
- Escalation threshold

---

## 6.10 Overpowered Coding Agent
The coding agent simultaneously has:
- secrets/private repository access
- untrusted external content
- unrestricted external communication or shell/network tools

This maps closely to Simon Willison’s “lethal trifecta.”

Counter-patterns:
- Sandbox
- secret isolation
- constrained networking
- trust-boundary separation
- least privilege

---

# 7. Day-to-Day Developer Pattern Candidates

These are especially important because the final catalog should not be only enterprise architecture.

## Foundation

### Explicit Definition of Done
Before execution, define concrete completion criteria.

### Test-Before-Done
Require actual tests/build/lint/runtime evidence rather than verbal confirmation.

### Read Before Write
Inspect relevant code/files/state before editing.

### Plan Before Large Change
For non-trivial work, produce a bounded plan/decomposition first.

### Small Scoped Context
Provide the model what it needs, not everything available.

### Deterministic Check Where Possible
Use compiler/test/schema/linter results instead of model judgment when available.

### Review the Diff, Not the Story
Validate actual artifacts/changes rather than relying on the agent’s description.

### High-Risk Action Confirmation
Require explicit approval before destructive or irreversible operations.

---

## Intermediate

### Plan → Execute → Verify
Separate intent, implementation, and validation.

### Evidence-Based Completion
Completion requires attached evidence: test output, diff, screenshots, command results, etc.

### Retry With Feedback
A failed attempt receives the actual failure output, not just “try again.”

### Progressive Disclosure
Keep a short top-level instruction/map and load deeper references only when needed.

### Context Isolation
Run a specialized task/reviewer with only the context needed for that responsibility.

### Generator → Critic → Revision
Use a separate critique phase with explicit criteria.

### Deterministic Gate
Use scripts/hooks/tests to block invalid states.

### Task-Specific Eval
Define success in terms of the actual developer task rather than generic “quality.”

---

## Advanced / Power User

### Independent Verifier
A separate agent/process evaluates the artifact against the task and evidence.

### Orchestrator → Specialized Workers
Use dynamic decomposition when subtasks cannot be predicted upfront.

### Parallel Independent Review
Multiple independent reviewers inspect distinct dimensions or vote on uncertain findings.

### Durable External State
Long-running workflows store progress/artifacts outside chat history.

### Agent-Legible Repository
Documentation, architecture constraints, tools and workflows are organized so agents can navigate and validate them.

### Automated Agent Review Loop
Worker → reviewer → feedback → repair → deterministic gate.

### Capability-Scoped Agents
Each specialist receives only the tools/permissions/context required for its role.

### Cross-Model Verification
Use a different model/provider for selected high-value validation when correlated failure is a concern.

---

# 8. Community / Open-Source Signals

Community evidence should not be treated as authoritative by itself, but it is useful for discovering recurring real-world practices.

## AWS sample-agentic-design-patterns
https://github.com/aws-samples/sample-agentic-design-patterns

Notable because it provides runnable shapes with pattern names such as:
- Deterministic Override
- Tool Gate
- Validation-Retry Loop
- Structured Error Classification
- Confidence-Based Routing
- Review Pass
- Coordinator-Subagent Hierarchy

This repository is particularly valuable because the pattern labels correspond to concrete code shapes rather than only prose.

---

## Antonio Gulli / Agentic Design Patterns ecosystem
Several GitHub repositories mirror or implement material from the book *Agentic Design Patterns* by Antonio Gulli and Mauro Sauco.

Common catalog entries include:
- Prompt chaining
- Routing
- Parallelization
- Reflection
- Tool use
- Planning
- Multi-agent collaboration
- Memory
- Learning/adaptation
- Guardrails
- Evaluation
- Human-in-the-loop
- Exception handling
- Resource optimization

This is evidence that a GoF-like cataloging effort is actively emerging, but naming and scope are not yet standardized.

---

## Claude Code / coding-agent harness community

Recent 2026 community posts repeatedly converge on:
- short repository instruction files
- progressive disclosure
- persistent state artifacts
- independent verifier agents
- automated test gates
- bounded loops
- fresh-context retries
- specialized subagents
- deterministic hooks
- cross-model review
- DAG-style parallelism

Examples discovered include discussions/projects around:
- harness engineering
- multi-agent review harnesses
- long-running “nightshift” harnesses
- mutation-testing gates
- structured workflow gates
- cross-model code review

Community evidence is weaker than primary guidance, but the recurrence is notable because it independently reproduces many patterns seen in OpenAI/Anthropic/AWS guidance.

---

# 9. Most Important Taxonomy Change From Discovery

The original broad family list was good, but discovery suggests the final taxonomy should explicitly separate **four layers of design**:

## Layer 1 — Model Interaction
What happens inside or immediately around one model’s reasoning cycle.

Examples:
- reflection
- ReAct
- tool use
- structured output
- retry with feedback

## Layer 2 — Workflow / Agent Composition
How multiple calls, roles, or agents are combined.

Examples:
- chaining
- routing
- parallelism
- orchestrator-workers
- generator-critic
- coordinator
- handoff

## Layer 3 — Harness / Runtime
The environment that makes agent behavior reliable.

Examples:
- context loading
- persistent state
- tool interfaces
- sandboxes
- hooks
- architectural linters
- test gates
- observability
- permissions

## Layer 4 — Development / Governance Process
How developers decide whether the whole system is good enough and safe enough.

Examples:
- evals
- trace review
- failure taxonomy
- human approval
- regression testing
- cost/performance monitoring
- security review

This layered view may be more useful than one flat list of 15 families.

---

# 10. Strong Cross-Source Principles

These principles appeared repeatedly enough to treat them as high-confidence discoveries.

## Principle 1 — Prefer Determinism Where the Problem Is Deterministic
Do not spend model reasoning on conditions a program can reliably decide.

Supported strongly by AWS, OpenAI, Anthropic and security guidance.

---

## Principle 2 — Complexity Must Earn Its Keep
Single-call → fixed workflow → single agent → multi-agent should be an escalation path, not a maturity ladder.

Supported strongly by Anthropic, OpenAI, Google and AWS.

---

## Principle 3 — Give Agents Ground Truth
Execution results, tests, compiler output, tool results and runtime evidence are more useful than asking the agent to imagine whether something worked.

Supported strongly by Anthropic and OpenAI coding-agent practice.

---

## Principle 4 — Separate Generation From Verification
The system that produced uncertain output should not be the only source establishing correctness.

Supported by evaluator-optimizer, generator-critic, maker-checker, independent review, ensemble review, and deterministic validation patterns.

---

## Principle 5 — Context Is a Designed Resource
More context is not monotonically better. Context must be selected, scoped, compressed, isolated and made navigable.

Supported strongly by Anthropic, OpenAI, Microsoft, LangChain and Google.

---

## Principle 6 — Security Boundaries Belong Outside the Model
Prompts are not authorization systems.

Supported extremely strongly by OWASP, Simon Willison, AWS and OpenAI.

---

## Principle 7 — Measure Real Task Success
A beautiful reasoning trace or fluent answer is irrelevant if the requested outcome did not happen.

Supported especially strongly by Hamel Husain / Shreya Shankar and Anthropic eval guidance.

---

## Principle 8 — Failures Should Improve the Harness
When an agent repeatedly fails, inspect what capability, documentation, feedback, boundary, or validator is missing.

Supported directly by OpenAI Harness Engineering and echoed by the coding-agent community.

---

# 11. Recommended Next Research Phase

The Discovery Phase now provides enough evidence to begin a deeper **Pattern Catalog Research Phase**.

Do not research every pattern equally at first. Start with patterns that satisfy all three:

1. High day-to-day usefulness for an individual developer.
2. Recurrence across independent sources.
3. Clear problem → structure → trade-off relationship.

Recommended first batch:

1. Explicit Definition of Done
2. Evidence-Based Completion
3. Deterministic Validation Gate
4. Independent Verifier
5. Plan → Execute → Verify
6. Retry With Feedback
7. Generator → Critic → Revision
8. Progressive Disclosure / Map-Not-Manual
9. Context Isolation
10. Repository-as-System-of-Record
11. Orchestrator → Workers
12. Parallel Independent Review
13. Bounded Agent Loop
14. Least-Privilege Tool Access
15. Human Approval Gate
16. External Durable State
17. Trace-Driven Error Analysis
18. Task-Success Evaluation

For each pattern, the next researcher should capture:

- Canonical name, if one exists.
- Common aliases.
- Recurring problem.
- Failure mode / anti-pattern.
- Minimal structure.
- Beginner implementation.
- Intermediate implementation.
- Advanced implementation.
- When to use.
- When not to use.
- Cost/latency implications.
- Security implications.
- Context implications.
- Known failure cases.
- Evidence/source quality.
- Real code or workflow examples.
- Framework/model-specific implementations only as examples, not as definitions.
- Confidence that this is truly a reusable pattern rather than a local trick.

---

# 12. Discovery Source Index

## Primary sources
1. Anthropic — Building Effective Agents  
   https://www.anthropic.com/engineering/building-effective-agents

2. Anthropic — Effective Context Engineering for AI Agents  
   https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

3. Anthropic — Demystifying Evals for AI Agents  
   https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

4. OpenAI — Harness Engineering  
   https://openai.com/index/harness-engineering/

5. OpenAI — A Practical Guide to Building Agents  
   https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/

6. OpenAI — Unrolling the Codex Agent Loop  
   https://openai.com/index/unrolling-the-codex-agent-loop/

7. OpenAI — Unlocking the Codex Harness  
   https://openai.com/index/unlocking-the-codex-harness/

8. OpenAI — Symphony orchestration  
   https://openai.com/index/open-source-codex-orchestration-symphony/

9. Google Cloud — Choose a Design Pattern for Your Agentic AI System  
   https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system

10. Microsoft Azure Architecture Center — AI Agent Orchestration Patterns  
    https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns

11. AWS Prescriptive Guidance — Agentic AI Patterns  
    https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html

12. AWS — System Design and Security Recommendations  
    https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html

13. AWS — MCP Tool Scope  
    https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html

14. OWASP — Top 10 for Agentic Applications 2026  
    https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

15. OWASP — LLM Top 10  
    https://genai.owasp.org/llm-top-10/

16. OWASP — Prompt Injection  
    https://genai.owasp.org/llmrisk/llm01-prompt-injection/

## Practitioner / expert sources
17. Hamel Husain & Shreya Shankar — Evals Skills for Coding Agents  
    https://hamel.dev/blog/posts/evals-skills/

18. Hamel Husain & Shreya Shankar — LLM Evals FAQ  
    https://hamel.dev/blog/posts/evals-faq/

19. Hamel Husain & Shreya Shankar — Evaluating Agentic Workflows  
    https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html

20. Simon Willison — The Lethal Trifecta for AI Agents  
    https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

21. Simon Willison — Living Dangerously with Claude  
    https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/

## Academic / educational
22. Stanford CS224G — Agentic Design Patterns  
    https://web.stanford.edu/class/cs224g/lectures/Agentic_Design_Patterns.pdf

## Open source
23. AWS Sample Agentic Design Patterns  
    https://github.com/aws-samples/sample-agentic-design-patterns

24. Agentic Design Patterns example catalog  
    https://github.com/zeljkoavramovic/agentic-design-patterns

25. Runnable agentic pattern implementations  
    https://github.com/josephsenior/Agentic-Design-Patterns

---

# 13. Final Discovery Conclusion

There is enough convergence to conclude that **AI/agent design patterns are becoming a genuine software-engineering discipline**, but the field has not standardized its vocabulary.

The mature part of the field is not “prompt tricks.” It is the recurring engineering structure around probabilistic components:

**define → decompose → provide context → execute through constrained tools → observe ground truth → verify → recover → persist state → enforce boundaries → evaluate real task success.**

For individual developers, the highest-value area is likely the intersection of:

- verification,
- deterministic gates,
- context engineering,
- harness engineering,
- bounded workflow design,
- tool permissions,
- and trace/eval-driven improvement.

Those areas should receive priority in the next deep-research phase.
