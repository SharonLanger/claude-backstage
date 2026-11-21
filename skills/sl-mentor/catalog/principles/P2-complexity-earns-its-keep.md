# Principle 2 — Complexity Must Earn Its Keep

> Single-call → fixed workflow → single agent → multi-agent should be an escalation path, not a maturity ladder.

## Why This Matters

Every additional component in an agentic system multiplies failure surfaces: more handoffs that can lose context, more coordination logic that can deadlock, more points where errors compound silently. Teams frequently jump to multi-agent architectures or elaborate orchestration because they associate complexity with capability — treating the escalation path as a maturity ladder rather than a cost tradeoff.

This principle appears across every major source because all of them observed the same failure mode: teams that start with multi-agent systems before proving a simpler architecture cannot handle the task. Anthropic explicitly recommends starting with a single LLM call and adding complexity only when measurably necessary. OpenAI's harness engineering treats every added component as something that must justify its existence through demonstrated improvement. Google's pattern selection framework treats agent count and coordination complexity as costs that require triggering conditions. AWS warns that multi-agent patterns introduce distributed-system failure modes (partial failure, message ordering, state inconsistency) that simply do not exist in simpler topologies.

## Which Sources Converge

| Organization | How They Express This Principle |
|---|---|
| **Anthropic** | "Start with the simplest solution" — the escalation ladder from prompt → workflow → agent is explicit architectural guidance |
| **OpenAI** | Harness engineering starts simple and adds components only when failures demonstrate the need |
| **Google Cloud** | Pattern selection criteria explicitly include task complexity thresholds — don't use multi-agent if single-agent suffices |
| **AWS** | Multi-agent patterns are positioned as solutions to coordination problems that simpler patterns cannot address |
| **Stanford** | Andrew Ng's agentic design patterns course teaches reflection and tool use before multi-agent collaboration |

## Patterns That Implement This Principle

- [Escalation Topology](../families/A-workflow-topology/) — choose the simplest topology that handles the task
- [Orchestrator → Workers](../families/C-orchestration/) — use only when a single agent genuinely cannot hold the full task
- [Confidence-Based Routing](../families/N-efficiency-routing/) — route simple tasks to simple paths, complex tasks to complex paths
- [Plan → Execute → Verify](../families/B-task-decomposition/) — decompose only when the task exceeds single-pass capability

## Anti-Patterns This Prevents

- **Multi-Agent by Default** — deploying multiple coordinating agents for tasks a single agent with good tooling could handle, paying coordination costs without capability gains

## Practical Application

1. **Start with a single prompt:** Before building a pipeline, test whether a single well-crafted prompt with good context can solve the task. Measure quality. Only add components when quality is measurably insufficient.

2. **Fixed workflow before dynamic orchestration:** If you need multiple steps, wire them as a deterministic pipeline (step A → step B → step C) before introducing an orchestrator agent that dynamically decides the flow. The fixed pipeline is easier to debug, test, and monitor.

3. **Single agent with tools before multi-agent:** A single agent with access to code execution, file read/write, and search tools handles most coding tasks. Add a second agent only when you can demonstrate that the coordination overhead is recouped by measurably better results (e.g., independent verification by a separate model instance).

4. **Cost/latency gates:** Before adding a component, estimate its cost in tokens, latency, and debugging complexity. If a simpler approach achieves 95% of the quality at 20% of the cost, the simpler approach wins unless that last 5% is safety-critical.

## Sources

- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- AWS — [Agentic AI Patterns and Workflows](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- Stanford — [CS224G — Agentic Design Patterns](https://web.stanford.edu/class/cs224g/lectures/Agentic_Design_Patterns.pdf)
