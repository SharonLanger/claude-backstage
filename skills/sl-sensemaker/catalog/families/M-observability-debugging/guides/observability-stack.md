# Guide: Observability Stack — What to Instrument and in What Order

## Purpose

Use this guide when building observability for an agent system from scratch. It defines what to instrument, in what priority order, and what each layer tells you that others cannot.

## The Four Layers

Instrument in this order. Each layer builds on the previous one:

```
Layer 4: Evals (are we getting better or worse?)
         ↑ depends on
Layer 3: Metrics (how much, how often, how expensive?)
         ↑ depends on
Layer 2: Logs (what happened in detail?)
         ↑ depends on
Layer 1: Traces (what was the execution path?)
```

**Do not skip layers.** Metrics without traces are unactionable (you see something is slow but cannot find where). Evals without logs are misleading (you see quality dropped but cannot find why).

---

## Layer 1: Traces (Start Here)

**What it answers:** "What path did execution take through the system?"

A trace is a tree of spans representing the full execution of one agent run — from user request to final output.

### What to capture per span:

| Field | Example | Why |
|-------|---------|-----|
| Span ID | `span-abc123` | Unique identifier for correlation |
| Parent span ID | `span-parent456` | Reconstructs the execution tree |
| Operation name | `tool_call:search_code` | What happened |
| Start/end timestamp | `2026-08-24T10:00:00Z` | Duration and ordering |
| Input summary | Truncated first 200 chars | What went in |
| Output summary | Truncated first 200 chars | What came out |
| Status | `success` / `error` / `timeout` | Did it work |
| Agent ID | `planner-agent` | Which agent in multi-agent |
| Model | `claude-sonnet-4-20250514` | Which model answered |

### Minimum viable trace:

For a single-agent system, you need at minimum:
1. One root span per user request
2. One child span per LLM call
3. One child span per tool call
4. Error status propagation from child to parent

### Priority: instrument this FIRST because everything else references it.

---

## Layer 2: Logs (Detail Within Spans)

**What it answers:** "What exactly happened inside this span?"

Logs attach to spans. They capture the full content that traces only summarize.

### What to log:

| Event | Log Content | Retention |
|-------|-------------|-----------|
| LLM request | Full prompt (system + user + tools) | 7–30 days |
| LLM response | Full completion text | 7–30 days |
| Tool call | Function name, full arguments | 30 days |
| Tool result | Full return value (or truncated if >10KB) | 30 days |
| Decision point | Why the agent chose action A over B | 30 days |
| Error | Full error message, stack trace, context | 90 days |
| Retry | Which attempt, what changed | 30 days |

### Structured format:

```json
{
  "trace_id": "trace-xyz",
  "span_id": "span-abc",
  "timestamp": "2026-08-24T10:00:01.234Z",
  "level": "info",
  "event": "tool_call",
  "tool": "search_code",
  "args": {"query": "handleError", "language": "typescript"},
  "duration_ms": 450,
  "result_size_bytes": 2340
}
```

### Priority: instrument this SECOND. Traces tell you where to look; logs tell you what you find there.

---

## Layer 3: Metrics (Aggregates Over Time)

**What it answers:** "How is the system performing overall? What are the trends?"

Metrics are numeric aggregates computed from traces and logs.

### Essential metrics (start with these):

| Metric | Type | What It Reveals |
|--------|------|----------------|
| Task completion rate | Gauge | % of runs that succeed end-to-end |
| Latency p50/p95/p99 | Histogram | How long runs take (and tail cases) |
| Token usage per run | Counter | Cost driver; also signals prompt bloat |
| Tool call count per run | Histogram | Efficiency; high counts may signal loops |
| Error rate by category | Counter | Which failure modes are most frequent |
| Retry rate | Gauge | System reliability; high retries = flaky tools |
| Human intervention rate | Gauge | Agent autonomy health |
| Cost per run | Histogram | Financial sustainability |

### Derived metrics (add once basics are stable):

| Metric | Formula | What It Reveals |
|--------|---------|----------------|
| Tool efficiency | successful_tool_calls / total_tool_calls | Are tools well-designed? |
| Reasoning overhead | planning_tokens / total_tokens | Is the agent overthinking? |
| Context utilization | used_context / available_context | Are we wasting context window? |
| Escalation quality | valid_escalations / total_escalations | Is the agent escalating appropriately? |

### Priority: instrument this THIRD. Metrics require traces and logs as raw material.

---

## Layer 4: Evals (Quality Measurement)

**What it answers:** "Is the system getting better or worse? Where specifically?"

Evals are tests run against real or synthetic inputs that measure output quality.

### Eval types (in priority order):

1. **Regression evals** — "Does the system still handle cases it used to handle correctly?" Run after every change.
2. **Failure-driven evals** — "Does the system now handle the specific failure we just debugged?" Created from real incidents.
3. **Domain evals** — "Does the system perform well across the breadth of its intended use?" Measures coverage.
4. **Comparative evals** — "Is version B better than version A?" Measures improvement.

### Key principle: evals MUST be grounded in real failures.

Do not write generic evals ("can the agent answer questions about Python?"). Write evals derived from actual failures observed in production traces:

1. Find a failure in traces/logs
2. Understand root cause
3. Write an eval that would have caught it
4. Verify the fix passes the eval
5. Keep the eval in the regression suite

### Priority: instrument this LAST. Evals without traces/logs/metrics are guesswork — you do not know what to eval until you have observed real failures.

---

## Instrumentation Order Summary

| Week | Layer | Deliverable |
|------|-------|-------------|
| 1 | Traces | Every run produces a span tree; can reconstruct execution path |
| 2 | Logs | Full prompt/response/tool content logged with trace correlation |
| 3 | Metrics | Dashboard with completion rate, latency, cost, error rate |
| 4+ | Evals | First eval suite derived from real failures found in weeks 1–3 |

## Common Mistakes

1. **Starting with metrics.** Without traces, you cannot diagnose what the metrics reveal.
2. **Starting with evals.** Without observing real failures, your evals test the wrong things.
3. **Logging everything at maximum verbosity permanently.** Start verbose, then tune down. Use sampling for high-volume spans.
4. **Not correlating across layers.** If a metric spikes, you must be able to drill into the traces and logs that caused it. Trace IDs are the correlation key.

## Related Patterns

- [M01: Structured Trace](../patterns/M01-structured-trace.md) — the trace format pattern
- [M02: Tool Call Event Log](../patterns/M02-tool-call-event-log.md) — logging tool interactions
- [M06: Token Cost Metrics](../patterns/M06-token-cost-metrics.md) — cost-specific instrumentation
- [M08: Trace-Linked Eval](../patterns/M08-trace-linked-eval.md) — connecting evals to traces
- [M09: Failure Categorization](../patterns/M09-failure-categorization.md) — classifying errors for metrics

## Sources

- Microsoft — [AI Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- Hamel Husain & Shreya Shankar — [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/)
- Hamel Husain & Shreya Shankar — [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- OpenAI — [Harness Engineering](https://openai.com/index/harness-engineering/)
