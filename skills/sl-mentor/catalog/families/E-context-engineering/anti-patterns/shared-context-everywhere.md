# Anti-Pattern: Shared Context Everywhere

## Name

Shared Context Everywhere

## Symptoms

- Every agent in a multi-agent system receives the same system prompt or context payload
- Specialist agents reference tools, knowledge, or instructions irrelevant to their role
- Context window usage is dominated by "just in case" information rather than task-relevant information
- Agents produce off-topic or confused outputs because they are attending to context meant for other agents
- Removing context from one agent breaks another (tight coupling through shared context)
- Debugging requires understanding what each agent is attending to in a shared blob
- Security-sensitive information (credentials, internal docs, user PII) is visible to agents that do not need it

## Root Cause

Teams default to a shared context bus — one large context payload that every agent receives — because it is the simplest initial architecture. Rather than designing what each agent needs, the team gives everyone everything. This works at small scale (2-3 agents, small context) but breaks as the system grows.

The root cause is treating context as free. In reality, every token of irrelevant context: (1) competes for the model's attention with relevant tokens, (2) increases the probability of the model acting on the wrong instruction, (3) exposes information to agents that should not have access to it, and (4) increases latency and cost proportionally.

## Failure Scenario

A customer support system has four agents: a router, a billing specialist, a technical specialist, and a quality reviewer. The team creates one shared context document containing:
- All company policies
- All product documentation
- All billing procedures
- All escalation paths
- Customer history
- Internal agent coordination instructions

Every agent receives the full context on every turn. Results:
- The billing agent occasionally answers technical questions (seeing technical docs in its context) rather than routing to the technical specialist
- The technical agent sometimes quotes billing policies incorrectly (partial attention to billing docs)
- The quality reviewer's assessments are influenced by seeing internal coordination instructions — it evaluates based on how well agents followed the internal protocol rather than customer satisfaction
- A prompt injection in a customer message exfiltrates internal escalation procedures because all agents can see them
- Context is 80% irrelevant on any given turn, wasting tokens and degrading quality

## Counter-Patterns

- [Context Isolation](../patterns/context-isolation.md) — each agent receives only the context relevant to its role
- [Role-Scoped Context](../patterns/role-scoped-context.md) — design context packages per role/specialization
- [Minimal-Context Handoff](../patterns/minimal-context-handoff.md) — pass only what the next agent needs, not everything the previous agent had
- [Artifact-Based Handoff](../patterns/artifact-based-handoff.md) — share structured outputs, not raw context

## Sources

- Anthropic — [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
