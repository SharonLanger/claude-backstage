# Pattern Summary

The Theater Model implements or directly avoids **36 patterns** from the AI agent design patterns research literature.

## Count by family

| Family | Count | Primary sources |
|--------|------:|-----------------|
| E — Context Engineering | 10 | [Anthropic: Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| I — Reliability & Recovery | 4 | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents), [Microsoft: Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns), [AWS: Agentic Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html) |
| K — Human Control | 3 | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| L — Memory & State | 3 | [Microsoft: Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns), [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| N — Efficiency & Routing | 2 | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| D — Verification & Evaluation | 2 | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| F — Harness & Environment | 2 | [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/) |
| J — Security & Trust | 2 | [OWASP: Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [AWS: Agentic Security](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html) |
| B — Task Decomposition | 2 | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| C — Orchestration | 2 | [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| H — Deterministic Control | 1 | [AWS: Agentic Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html) |
| Principles | 2 | [Google: Agent Design Patterns](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system), [Anthropic: Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |
| Anti-patterns avoided | 2 | [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/), [Anthropic: Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |

## All patterns

| Pattern | Family | Consolidation | Cache hits | Recoverability | Minimal context |
|---------|--------|:---:|:---:|:---:|:---:|
| [Context Isolation](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | | | | x |
| [Role-Scoped Context](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | | x | | x |
| [Context Offloading](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | | x | | x |
| [Just-in-Time Retrieval](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | | x | | x |
| [Minimal-Context Handoff](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | | | x | x |
| [Artifact-Based Handoff](https://www.anthropic.com/engineering/building-effective-agents) | E | | | x | |
| [Repository-as-System-of-Record](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | x | | x | |
| [Progressive Disclosure](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | | x | | x |
| [Map-Not-Manual](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | x | x | | x |
| [Context Compaction](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E | x | | | |
| [Bounded Retry](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html) | I | | | x | |
| [Checkpoint and Resume](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | I | x | | x | |
| [Fresh-Context Retry](https://www.anthropic.com/engineering/building-effective-agents) | I | | | x | |
| [Human Escalation](https://www.anthropic.com/engineering/building-effective-agents) | I | x | | x | |
| [Caching](https://www.anthropic.com/engineering/building-effective-agents) | N | | x | | |
| [Context Minimization](https://www.anthropic.com/engineering/building-effective-agents) | N | | x | | x |
| [Human-in-the-Loop Checkpoint](https://www.anthropic.com/engineering/building-effective-agents) | K | | | x | |
| [High-Risk Action Gate](https://www.anthropic.com/engineering/building-effective-agents) | K | | | x | |
| [Failure-Threshold Escalation](https://www.anthropic.com/engineering/building-effective-agents) | K | | | x | |
| [Independent Verifier](https://www.anthropic.com/engineering/building-effective-agents) | D | | | x | x |
| [Evidence-Based Completion](https://www.anthropic.com/engineering/building-effective-agents) | D | | | x | |
| [Repository-Local System of Record](https://openai.com/index/harness-engineering/) | F | x | | | |
| [Persistent Task Artifacts](https://openai.com/index/harness-engineering/) | F | x | | | |
| [Least Privilege](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | J | | | | x |
| [Read/Write Separation](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html) | J | | | | x |
| [Checkpoint State](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | L | x | | | |
| [Artifact State](https://www.anthropic.com/engineering/building-effective-agents) | L | x | | | |
| [State Machine](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | L | | | x | |
| [Fixed Decomposition](https://www.anthropic.com/engineering/building-effective-agents) | B | | x | x | |
| [Milestone Checkpoint](https://www.anthropic.com/engineering/building-effective-agents) | B | x | | | |
| [Orchestrator-Workers](https://www.anthropic.com/engineering/building-effective-agents) | C | | x | | x |
| [Maker-Checker](https://www.anthropic.com/engineering/building-effective-agents) | C | | | x | |
| [Programmatic Gate](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html) | H | | | x | |
| [P4 — Separate Generation / Verification](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) | Principle | | | x | |
| [P5 — Context Is a Designed Resource](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Principle | | x | | x |
| Avoids [AP03 — Giant Instruction Manual](https://openai.com/index/harness-engineering/) | Anti-pattern | | x | | x |
| Avoids [AP07 — Shared Context Everywhere](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anti-pattern | | x | | x |

## Source publications

| Publisher | Paper | Patterns drawn |
|-----------|-------|---------------:|
| Anthropic | [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 12 |
| Anthropic | [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | 16 |
| Microsoft | [AI Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | 3 |
| AWS | [Agentic AI Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html) | 2 |
| AWS | [Agentic AI Security Best Practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html) | 1 |
| Google | [Choose Design Pattern for Agentic AI](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) | 1 |
| OpenAI | [Harness Engineering](https://openai.com/index/harness-engineering/) | 3 |
| OWASP | [Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | 1 |
