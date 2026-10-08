# Minimal Context — Each Agent Loads Only What It Needs

No agent sees the full Play. No agent inherits the previous agent's conversation. Each agent's context is constructed from its Act definition, its `@` references, and the current state from `progress.md`. Everything else is structurally excluded.

## Why this matters

Smaller context = better attention allocation = higher quality output. LLMs have finite attention — as context grows, each directive gets less reliable attention. The Theater Model achieves context minimization structurally (fresh agents per Act) rather than through brittle prompt engineering.

A 5-Act Play where each agent needs 2,000 tokens beats a single-agent approach that accumulates 40,000 tokens by Act 5. The structural guarantee matters more than the token count: there is no mechanism by which irrelevant context can leak in.

## How the model achieves this

Each agent gets its own isolated context, constructed fresh and torn down on completion. Roles are defined in configuration files that scope what each agent sees. Stable reference material lives in files, not in prompts — retrieved only when needed. Handoff objects contain only the task output and relevant decisions. The system prompt stays small; deeper knowledge is fetched on demand.

Each agent's tool surface is also minimized: agents get only the tools and permissions for their task, reducing both context overhead and risk.

## Patterns implemented

| Pattern | Family | How the Theater Model applies it |
|---------|--------|----------------------------------|
| [Context Isolation](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Each agent gets isolated context, constructed fresh and torn down on completion. No context crosses a boundary unless serialized. |
| [Role-Scoped Context](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Each agent gets context scoped to its role. Roles defined in configuration, not in the prompt. |
| [Context Offloading](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Stable reference material in files, not prompts. The prompt contains a pointer; content retrieved on demand. |
| [Just-in-Time Retrieval](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Context contains retrieved content only while being used. ~1,800 tokens vs 40,000 for full upfront load. |
| [Minimal-Context Handoff](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Handoff objects contain the task output and relevant decisions — nothing else. ~400 tokens instead of ~4,000. |
| [Progressive Disclosure](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Information revealed incrementally. Each step under 2,000 tokens; full upfront load would be 7,000. |
| [Map-Not-Manual](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | System prompt stays small. Deeper knowledge fetched on demand. ~800 tokens instead of ~6,000. |
| [Context Minimization](https://www.anthropic.com/engineering/building-effective-agents) | N — Efficiency & Routing | No accumulated conversation history. Each agent starts fresh. Prompt size drops ~85% vs shared-context. |
| [Orchestrator-Workers](https://www.anthropic.com/engineering/building-effective-agents) | C — Orchestration | Stage Manager's context is small — Play structure + progress.md. Workers are isolated and independently testable. |
| [Independent Verifier](https://www.anthropic.com/engineering/building-effective-agents) | D — Verification & Evaluation | Checklist Agent receives only the specification and the artifact. No generator reasoning trace. Clean, minimal context. |
| [Least Privilege](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | J — Security & Trust | Each agent gets only the tools and permissions for its task. Less tool surface = less context overhead. |
| [Read/Write Separation](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html) | J — Security & Trust | Read-only agents don't need write credentials. Fewer permissions = smaller tool definitions = less context. |
| [P5 — Context Is a Designed Resource](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Principle | "Everything it might need" performs worse than "precisely what it needs." Context designed per-Act, not per-Play. |
| [Avoids AP03 — Giant Instruction Manual](https://openai.com/index/harness-engineering/) | Anti-pattern avoided | No unbounded prompt growth. No buried directives getting less attention. |
| [Avoids AP07 — Shared Context Everywhere](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anti-pattern avoided | No quadratic cost growth. No cross-contamination. No information leaking across stages. |
