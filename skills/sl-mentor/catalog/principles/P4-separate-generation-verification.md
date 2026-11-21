# Principle 4 — Separate Generation From Verification

> The system that produced uncertain output should not be the only source establishing correctness.

## Why This Matters

A model that generates output and then evaluates its own output exhibits confirmation bias — it is structurally inclined to judge its work as correct because the same reasoning process that produced the output also assesses it. This is not a matter of model capability; it is a structural property of self-evaluation. The same weights, context, and reasoning patterns that led to a particular output will tend to confirm that output when asked to review it. Independent verification — by a different model instance, a different prompt, a deterministic validator, or a human reviewer — catches errors that self-review systematically misses.

This principle appears across nearly every source because it maps directly to a well-understood property of complex systems: the producer of output is the worst auditor of that output. Google's evaluator-optimizer pattern, Anthropic's orchestrator-worker verification loops, AWS's maker-checker pattern, and Hamel's independent evaluation methodology all implement the same structural insight. The pattern names differ but the principle is identical: generation and verification must be architecturally separated to achieve reliable correctness.

## Which Sources Converge

| Organization | How They Express This Principle |
|---|---|
| **Google Cloud** | Evaluator-optimizer pattern: a separate evaluator scores output and decides whether to loop back for revision |
| **Anthropic** | Orchestrator-worker patterns where the orchestrator verifies worker output before accepting it |
| **AWS** | Maker-checker pattern: one agent generates, a separate component validates |
| **Hamel Husain** | Evaluation methodology requires independent measurement separate from the generation pipeline |
| **OpenAI** | Harness engineering uses tests and linters (independent verifiers) rather than asking the model to self-assess |
| **Stanford** | Reflection pattern explicitly separates the generation step from the critique step |

## Patterns That Implement This Principle

- [Generator → Critic → Revision](../families/D-verification-evaluation/) — separate model instance critiques output before final acceptance
- [Independent Verifier](../families/D-verification-evaluation/) — verification performed by a structurally separate system
- [Evaluator-Optimizer Loop](../families/A-workflow-topology/) — cyclic topology where evaluation drives re-generation
- [Parallel Independent Review](../families/C-orchestration/) — multiple independent reviewers assess the same output
- [Deterministic Validation Gate](../families/H-deterministic-control/) — code-based validators that cannot be influenced by the generator's reasoning

## Anti-Patterns This Prevents

- **Self-Certified Completion** — the generating agent declares its own output correct without independent verification, leading to plausible-looking but incorrect results that propagate downstream

## Practical Application

1. **Separate review prompt:** After a model generates code, use a separate prompt (or a separate model instance with fresh context) to review that code for bugs, security issues, and requirement compliance. The reviewer has no access to the generator's reasoning chain — only the output.

2. **Automated test execution as verification:** Don't ask the model "did you write correct code?" — run the tests. The test framework is an independent verifier that shares no reasoning state with the generator.

3. **Multi-model consensus:** For high-stakes outputs (security-relevant code, data migrations), run the same task through two different models or two differently-prompted instances. Disagreements surface errors that self-review would miss.

4. **Human-in-the-loop for irreversible actions:** Before executing destructive operations (database migrations, production deployments, sending communications), require human review. The human is the ultimate independent verifier — they share no context window with the model.

## Sources

- Google Cloud — [Choose a Design Pattern for Your Agentic AI System](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- Anthropic — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- Hamel Husain & Shreya Shankar — [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
- Stanford — [CS224G — Agentic Design Patterns](https://web.stanford.edu/class/cs224g/2025/lectures/Agentic_Design_Patterns.pdf)
