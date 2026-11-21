# Designing Output Integration

## Scenario

Your agent produces output (text, code, data, decisions) that needs to flow into a downstream system — a UI, an API, a database, a pipeline, or a human review process. You need to ensure the output is correctly structured, validated, safe, and properly connected to what comes next.

## Quick Answer

1. **Define the output contract first** — before building the agent, specify exactly what format, structure, and constraints the output must satisfy. See [O-output-integration](../../families/O-output-integration/).
2. **Validate programmatically, not hopefully** — never trust that the LLM will produce valid output. Always validate with deterministic checks before passing downstream. See [schema-validation.md](../../families/O-output-integration/patterns/schema-validation.md).
3. **Separate the agent boundary from the system boundary** — the agent's raw output and what reaches the downstream system should pass through a sanitization layer. See [sanitized-output-boundary.md](../../families/O-output-integration/patterns/sanitized-output-boundary.md).

## Decision Guide: What Kind of Output Integration?

### Step 1: Characterize the downstream consumer

| Consumer | Key constraint | Primary concern |
|----------|---------------|-----------------|
| API / service | Must match schema exactly | Structural validity |
| Database | Types, constraints, foreign keys | Data integrity |
| UI / frontend | Rendering expectations, XSS safety | Format + security |
| Human reviewer | Readability, traceability | Clarity + provenance |
| Another agent | Context budget, relevance | Minimal + structured |
| Pipeline / workflow | Triggering conditions, idempotency | Reliability + ordering |

### Step 2: Choose validation strategy

| Strategy | When to use | Pattern |
|----------|-------------|---------|
| Schema validation | Output has a known structure (JSON, XML, typed) | [schema-validation.md](../../families/O-output-integration/patterns/schema-validation.md) |
| Programmatic postcondition | Business rules that go beyond schema | [programmatic-postcondition.md](../../families/O-output-integration/patterns/programmatic-postcondition.md) |
| Parse and reject | Output must be parseable; reject if not | [parse-and-reject.md](../../families/O-output-integration/patterns/parse-and-reject.md) |
| Typed result object | Strongly typed output with metadata | [typed-result-object.md](../../families/O-output-integration/patterns/typed-result-object.md) |

### Step 3: Choose boundary strategy

| Concern | Pattern | What it does |
|---------|---------|-------------|
| Prevent injection / XSS | [sanitized-output-boundary.md](../../families/O-output-integration/patterns/sanitized-output-boundary.md) | Strips dangerous content before output reaches consumers |
| Enforce structure | [structured-output-boundary.md](../../families/O-output-integration/patterns/structured-output-boundary.md) | Ensures output conforms to expected shape |
| Type safety | [typed-result-object.md](../../families/O-output-integration/patterns/typed-result-object.md) | Wraps output in a typed container with success/failure states |

## Integration Patterns by Use Case

### Agent produces structured data (JSON, records)

| Step | Pattern | Purpose |
|------|---------|---------|
| 1. Format | Request structured output from model | Get parseable response |
| 2. Parse | [parse-and-reject.md](../../families/O-output-integration/patterns/parse-and-reject.md) | Verify it is valid syntax |
| 3. Validate | [schema-validation.md](../../families/O-output-integration/patterns/schema-validation.md) | Verify it matches expected schema |
| 4. Check | [programmatic-postcondition.md](../../families/O-output-integration/patterns/programmatic-postcondition.md) | Verify business rules |
| 5. Deliver | Write to API/DB | Integration complete |

### Agent produces code

| Step | Pattern | Purpose |
|------|---------|---------|
| 1. Generate | Agent writes code | Raw output |
| 2. Validate syntax | Parse/compile check | Catches syntax errors |
| 3. Test | [D01-deterministic-validator.md](../../families/D-verification-evaluation/patterns/D01-deterministic-validator.md) | Run tests against output |
| 4. Review | [maker-checker.md](../../families/C-orchestration/patterns/maker-checker.md) | Second agent or human reviews |
| 5. Deliver | Commit/deploy with guards | Integration complete |

### Agent produces decisions or recommendations

| Step | Pattern | Purpose |
|------|---------|---------|
| 1. Generate | Agent reasons and decides | Raw decision |
| 2. Structure | [typed-result-object.md](../../families/O-output-integration/patterns/typed-result-object.md) | Wrap in decision object with confidence, reasoning |
| 3. Validate | [programmatic-postcondition.md](../../families/O-output-integration/patterns/programmatic-postcondition.md) | Check decision is within allowed bounds |
| 4. Gate | [K01-human-in-the-loop-checkpoint.md](../../families/K-human-control/patterns/K01-human-in-the-loop-checkpoint.md) | Human approves high-stakes decisions |
| 5. Deliver | Execute decision or pass to system | Integration complete |

### Agent produces content for humans

| Step | Pattern | Purpose |
|------|---------|---------|
| 1. Generate | Agent writes content | Raw text |
| 2. Sanitize | [sanitized-output-boundary.md](../../families/O-output-integration/patterns/sanitized-output-boundary.md) | Remove unsafe content |
| 3. Format | Apply presentation rules | Match UI expectations |
| 4. Deliver | Render in UI | Integration complete |

## Handling Validation Failures

When output fails validation, you need a recovery strategy:

| Strategy | When to use | Pattern |
|----------|-------------|---------|
| Retry with error feedback | Fixable formatting issues | [retry-with-feedback.md](../../families/I-reliability-recovery/patterns/retry-with-feedback.md) |
| Retry with fresh context | Model is stuck in a bad pattern | [fresh-context-retry.md](../../families/I-reliability-recovery/patterns/fresh-context-retry.md) |
| Fallback to simpler model/approach | Complex output failing repeatedly | [fallback-model-workflow.md](../../families/I-reliability-recovery/patterns/fallback-model-workflow.md) |
| Human escalation | Cannot resolve automatically | [human-escalation.md](../../families/I-reliability-recovery/patterns/human-escalation.md) |
| Reject and report | Better to fail than deliver bad output | [parse-and-reject.md](../../families/O-output-integration/patterns/parse-and-reject.md) |

## Design Checklist

- [ ] Output schema/format fully specified before agent implementation
- [ ] Validation logic is deterministic (not another LLM call)
- [ ] Failure path defined (what happens when validation fails?)
- [ ] Retry budget bounded (max attempts before escalation)
- [ ] Sanitization layer between agent and downstream consumer
- [ ] Output includes metadata (confidence, source, timestamp) where relevant
- [ ] Idempotency considered (what if the same output is delivered twice?)
- [ ] Downstream system gracefully handles partial or degraded output

## Anti-Patterns to Watch For

- [Retry Without New Information](../../families/I-reliability-recovery/anti-patterns/retry-without-new-information.md) — retrying output generation without telling the model what was wrong
- [Silent Quality Degradation](../../families/N-efficiency-routing/anti-patterns/silent-quality-degradation.md) — accepting "close enough" output without measuring quality over time
- [Infinite/Weakly-Bounded Loop](../../families/I-reliability-recovery/anti-patterns/infinite-weakly-bounded-loop.md) — unbounded retry loops trying to get valid output

## Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://openai.com/index/harness-engineering/
- https://openai.com/index/unlocking-the-codex-harness/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html
