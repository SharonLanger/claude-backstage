# Cache Efficiency — Stable Structure, Predictable Loads

When agents load files via `@` references, the LLM provider's prompt caching activates. The Theater Model is designed so that the cacheable prefix (system prompt + referenced files) is large and stable, while the variable suffix (current task context) is small. Multiple agents referencing the same file benefit from the same cache entry.

## Why this matters

Zero additional inference cost and near-zero latency on cached content. A Play with 5 Acts where each agent loads `play-rules.md` pays the encoding cost once. The fixed decomposition means the structure of each agent's prompt is predictable before execution begins — the cache can be warm before the agent even starts.

Smaller context also means faster inference on cache misses. An agent loading ~1,800 tokens per call instead of ~40,000 gets better attention allocation and faster response times regardless of cache state.

## How the model achieves this

The Play is defined upfront and frozen before execution. Each agent gets a high-signal, low-noise context scoped to its role. Reference material lives in external files (stable across calls) rather than inlined into prompts. Content is retrieved only when a step explicitly needs it. Each Act's agent receives only its instructions — not the full Play or future Acts.

The system prompt stays small (~800 tokens vs ~6,000 for a full manual). Each agent starts fresh with no accumulated conversation history. The Stage Manager's context holds only the Play structure and `progress.md` — not the full state of all workers.

## Patterns implemented

| Pattern | Family | How the Theater Model applies it |
|---------|--------|----------------------------------|
| [Caching](https://www.anthropic.com/engineering/building-effective-agents) | N — Efficiency & Routing | Stable system prompts + stable `@` referenced files = high cache hit rates across agents. |
| [Fixed Decomposition](https://www.anthropic.com/engineering/building-effective-agents) | B — Task Decomposition | The Play is defined upfront and frozen. Predictable structure = stable prompt prefixes = cacheable. |
| [Role-Scoped Context](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Each agent gets context scoped to its role. ~600 tokens of role-specific context from a 4,000-token shared state. |
| [Context Offloading](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Reference material lives in external files, not inlined into prompts. Stable across calls — prime caching candidates. |
| [Just-in-Time Retrieval](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Content is retrieved only when a step needs it. Average: ~1,800 tokens vs 40,000 for full upfront load. |
| [Progressive Disclosure](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | Each Act's agent receives only its instructions. Prior outputs passed as compact artifacts, not full transcripts. |
| [Map-Not-Manual](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | E — Context Engineering | System prompt stays small. Deeper knowledge fetched on demand. ~800 tokens instead of ~6,000. |
| [Context Minimization](https://www.anthropic.com/engineering/building-effective-agents) | N — Efficiency & Routing | No accumulated conversation history. Each agent starts fresh. Prompt size drops ~85% vs shared-context. |
| [Orchestrator-Workers](https://www.anthropic.com/engineering/building-effective-agents) | C — Orchestration | Stage Manager's context stays small — Play structure + progress.md. Workers are isolated and bounded. |
| [P5 — Context Is a Designed Resource](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Principle | Context is designed per-Act, not accumulated per-Play. "Everything it might need" performs worse than "precisely what it needs." |
| [Avoids AP03 — Giant Instruction Manual](https://openai.com/index/harness-engineering/) | Anti-pattern avoided | No unbounded prompt growth. No buried directives. Each agent gets a small, focused Act. |
| [Avoids AP07 — Shared Context Everywhere](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anti-pattern avoided | Agents get only their Act's context. No quadratic token cost growth. No cross-contamination. |
