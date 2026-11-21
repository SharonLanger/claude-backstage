# Provenance-Tagged Memory

**Family:** L — Memory & State
**Also known as:** Source-Annotated Memory, Attributed Memory, Traceable Memory
**Related patterns:** [External Durable State](external-durable-state.md), [Shared-Memory Gateway](shared-memory-gateway.md), [Summarized Memory](summarized-memory.md), [Scoped Memory](scoped-memory.md)

## Problem

An agent system accumulates facts, decisions, and findings in its memory store over time. Without tracking where each piece of information came from, the system cannot answer: Is this fact still current, or was it written hours ago by a now-outdated agent? Which agent wrote this? Was it derived from a tool call result, a model inference, or human input? How confident should we be in it? When something goes wrong — a decision was made on a stale fact, a finding was fabricated, a constraint was quietly overwritten — there is no way to trace the error back to its source. Memory becomes an opaque black box.

## Forces

- Memory entries can be written by multiple agents, humans, and tools; authorship is otherwise lost.
- The confidence and freshness of a memory entry varies enormously by its source.
- Auditing and debugging require being able to reconstruct which agent believed what, and why.
- Agents downstream of a memory store need to assess whether to trust an entry before acting on it.
- Tagging every write adds metadata overhead that must be borne on every read.

## Solution

Attach provenance metadata to every memory write. Each entry in the memory store carries a structured tag alongside its content:

- **Source:** which agent, tool, or human wrote this entry (agent ID, tool name, user ID).
- **Timestamp:** when the entry was written (ISO 8601; machine-readable for staleness checks).
- **Confidence:** the writing agent's self-assessed confidence in the entry (a score or enum: `high / medium / low / inferred`).
- **Derivation:** was this entry directly observed (tool output, human input) or inferred (model reasoning, summary)?
- **Version:** a monotonically increasing counter or hash that increments on each write to the same key.

Agents reading from the store receive the full tagged entry, not just the value. The reading agent can apply staleness checks (`if entry.age > N: re-verify`), confidence filters (`skip entries with confidence = low unless required`), and source filters (`trust only human-authored constraints`).

## Structure

<details>
<summary><b>Provenance-Tagged Memory — Write and Read Flow</b></summary>

```mermaid
flowchart TD
    A([Writing Agent]) --> B[Compose entry:\nvalue + provenance tag]
    B --> C{Writing via\nGateway}
    C --> D[(Memory Store\nvalue + tag)]

    E([Reading Agent]) --> F[Read entry\nfrom store]
    F --> G[Evaluate provenance:\nage, source, confidence]
    G --> H{Trust\ncriteria met?}
    H -- Yes --> I[Use entry value]
    H -- No --> J{Staleness?}
    J -- Yes --> K[Re-verify:\nre-run tool or ask agent]
    J -- No --> L[Discard or\nflag low-confidence]
    K --> I
    K --> D

    subgraph Tag Structure
        T1["source: agent-id / tool / human"]
        T2["timestamp: ISO 8601"]
        T3["confidence: high / medium / low"]
        T4["derivation: observed / inferred"]
        T5["version: integer"]
    end

    B --> Tag Structure

    style A fill:#1a3a6b,color:#fff
    style E fill:#1a3a6b,color:#fff
    style D fill:#5c1a1a,color:#fff
    style I fill:#1a5c2a,color:#fff
    style K fill:#3a1a5c,color:#fff
```

</details>

## Implementation Notes

**Pseudocode — provenance-tagged write and read:**

```
# Write with provenance
function write_memory(key, value, agent_id, confidence, derivation):
  entry = {
    value:       value,
    source:      agent_id,
    timestamp:   now_iso8601(),
    confidence:  confidence,       # "high" | "medium" | "low" | "inferred"
    derivation:  derivation,       # "observed" | "inferred" | "summarized"
    version:     current_version(key) + 1
  }
  store.upsert(key, entry)

# Read with staleness and trust check
function read_memory(key, max_age_seconds=3600, min_confidence="medium"):
  entry = store.get(key)
  if entry is None:
    return None, MISSING
  if entry.age_seconds() > max_age_seconds:
    return entry, STALE                  # caller decides whether to re-verify
  if confidence_rank(entry.confidence) < confidence_rank(min_confidence):
    return entry, LOW_CONFIDENCE         # caller decides whether to use
  return entry, OK
```

- **Tag schema standardization:** all agents in the system must use the same tag schema. Define it in a shared schema file; enforce at the gateway.
- **Derivation chain:** for multi-hop derivations (agent A inferred X from tool result Y, agent B summarized X into Z), store the derivation chain, not just the immediate source. A flat `derivation` field is a minimum; a linked list of source references is more complete.
- **Confidence assignment guidelines:** provide explicit rules so agents assign confidence consistently: `high` = direct tool output or human input; `medium` = single-step model inference with supporting evidence; `low` = multi-step inference or speculative reasoning.
- **Staleness TTL vs. age check:** for time-sensitive facts (prices, availability, live system state), apply a short TTL and auto-expire. For stable facts (code structure, user preferences), use age-based staleness checks rather than expiry.
- **Failure mode — confidence inflation:** agents consistently mark their outputs as `high` confidence to avoid re-verification. Audit confidence distributions periodically; if everything is `high`, the signal is lost.
- **Failure mode — source spoofing:** an agent writes an entry claiming to be `source: human-admin`. Enforce source tagging in the gateway using the writing agent's authenticated identity, not a self-reported value.
- **Cost tradeoff:** provenance tags add ~100–300 bytes per entry. Negligible for most stores; significant for high-frequency writes. Use compact representations (e.g., timestamp as Unix integer, confidence as single byte) if storage is constrained.

## Examples

**1. Multi-agent research system.** A researcher agent writes findings: `{"value": "library X is deprecated", "source": "researcher-agent-7", "confidence": "high", "derivation": "observed", "timestamp": "2026-08-24T14:00Z"}`. A drafter agent reads this and includes the finding. A reviewer agent, finding the timestamp is 6 hours old, flags it for re-verification before publication.

**2. Constraint management.** A planning agent writes constraints to shared memory. Each constraint carries `source: human-operator` (set by the gateway when a human writes via the UI) vs. `source: planner-agent` (set when the agent infers a constraint). An execution agent treats human-operator constraints as hard limits and agent-inferred constraints as soft hints.

**3. Tool-call result caching.** A shared cache stores expensive tool results. Each entry is tagged with `timestamp` and `confidence: high, derivation: observed`. Before using a cached result, agents check the age; results older than 1 hour for volatile data sources trigger a fresh tool call. The provenance tag makes this policy enforceable without special-casing each tool.

## Consequences

### Benefits
- Makes memory auditable: every fact has a traceable origin.
- Enables trust-aware reading: agents can filter by source, confidence, and freshness.
- Simplifies debugging: when a bad decision is made, trace back through provenance tags to the source of the faulty fact.
- Supports human oversight: human-authored entries are distinguishable from agent-inferred ones.

### Liabilities
- Adds metadata overhead to every write (storage) and every read (evaluation logic).
- Confidence is self-reported and subject to miscalibration or strategic inflation.
- Full derivation chains are complex to maintain and query for multi-hop inferences.
- Requires consistent adoption across all agents; a single agent that omits tags breaks the audit chain.

## Related Families

- **E — Context Engineering:** When loading memory into context, provenance tags guide what to include: prefer high-confidence, recent, observed entries; flag or exclude stale/inferred entries.
- **F — Harness:** The gateway (F) enforces tag attachment at write time using the agent's authenticated identity rather than trusting self-reported source fields.
- **I — Reliability:** Provenance tags enable reliability patterns to detect stale inputs before executing a step — a form of pre-condition checking.
- **M — Observability:** Provenance tags are the primary data source for M audit trails; they answer "who believed what, when, and how confidently" across the full agent lifecycle.

## Sources

- Microsoft Azure Architecture Center — Microsoft's cloud architecture team; stresses instrumenting every agent operation and handoff. [AI Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- Anthropic Engineering — AI safety company; authors of Claude. [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- OpenAI Engineering — AI research company; authors of GPT and Codex. [Harness Engineering](https://openai.com/index/harness-engineering/)
