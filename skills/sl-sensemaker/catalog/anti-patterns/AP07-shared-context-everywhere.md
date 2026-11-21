# AP07 — Shared Context Everywhere

## Symptoms

- Every agent or step in the pipeline sees the full conversation history regardless of relevance
- Token costs grow quadratically as context accumulates across steps
- Agents become confused by information from earlier steps that contradicts or is irrelevant to their current task
- Performance degrades as conversations get longer because the model attends to stale or irrelevant context
- Sensitive information from one stage leaks into stages that should not see it
- The system becomes slower and more expensive with each additional step in the pipeline

## Root Cause

Teams default to passing the entire conversation context to every component because it is the simplest implementation — no filtering logic required. This works in prototypes with short conversations but fails at scale. The model's attention mechanism distributes finite capacity across all tokens in context; irrelevant tokens dilute attention on relevant ones. Additionally, shared context creates implicit coupling between stages — a change in one stage's output format can break downstream stages that attend to it. The discipline of deciding what each component needs to see is engineering work that teams defer until costs or failures force the issue.

## Failure Scenario

A multi-step document processing pipeline passes the full context to each stage: extraction, validation, enrichment, and formatting. By the enrichment stage, the context contains 40,000 tokens of raw OCR output, validation errors, and intermediate results. The enrichment model — which only needs the structured extracted fields — starts "enriching" validation error messages as if they were document content. It also hallucinates field values from unrelated documents earlier in the conversation. The formatting stage then produces a polished but factually wrong output because it attended to hallucinated enrichment over the original extraction. Debugging takes hours because the context is too large for any human to review.

## Counter-Patterns

- [E07 — Minimal-Context Handoff](../families/E-context-engineering/patterns/minimal-context-handoff.md) — Pass only what the next stage needs
- [E03 — Context Isolation](../families/E-context-engineering/patterns/context-isolation.md) — Each agent gets its own scoped context
- [E10 — Role-Scoped Context](../families/E-context-engineering/patterns/role-scoped-context.md) — Filter context by the component's role
- [E01 — Artifact-Based Handoff](../families/E-context-engineering/patterns/artifact-based-handoff.md) — Pass structured artifacts, not raw conversation history

## Sources

- Anthropic — [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
