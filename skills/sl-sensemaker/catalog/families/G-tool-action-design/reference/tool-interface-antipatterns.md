# Reference: Tool Interface Anti-Patterns

## Purpose

Use this reference to identify and fix common tool design mistakes. Each anti-pattern describes a recurring tool design error, its observable symptoms, and the correct approach. Review this before designing new tools or when debugging persistent agent-tool interaction failures.

---

## 1. The Swiss-Army Tool

**What it is:** A single tool that does many unrelated things, selected via a "mode" or "action" parameter.

**Symptoms:**
- Tool has a `mode` or `action` parameter with 5+ options
- Agent frequently picks the wrong mode
- Tool description is a paragraph listing all capabilities
- Different modes have completely different parameter requirements

**Why it fails:** The agent must understand a complex internal dispatch table. The more modes, the more likely it picks the wrong one. Parameter requirements change per mode, creating confusing conditional schemas.

**Fix:** Split into separate, focused tools — one per action. Each tool has a clear name, a simple description, and consistent parameters. See [G02 — Narrow Tool Interface](../patterns/G02-narrow-tool-interface.md).

---

## 2. The Firehose Output

**What it is:** A tool that returns unbounded output — full file contents, complete database tables, or verbose API responses without pagination or truncation.

**Symptoms:**
- Tool results frequently overflow the context window
- Agent's subsequent reasoning degrades after receiving a large tool result
- Agent cannot find the relevant part of the output
- Costs spike on turns that include tool results

**Why it fails:** The context window is a fixed resource. A single tool result that consumes 50% of it crowds out everything else — instructions, conversation history, and reasoning space.

**Fix:** Add pagination, filtering, or summarization to tool output. Return metadata first ("found 47 results"), then let the agent request specific items. Set hard output limits. See [G01 — Typed Schema-Constrained Tool](../patterns/G01-typed-schema-constrained-tool.md).

---

## 3. The Silent Failure

**What it is:** A tool that returns success (or nothing) when it actually failed or partially failed.

**Symptoms:**
- Agent proceeds confidently after tool call but subsequent steps fail
- Agent re-calls the same tool repeatedly because it cannot detect failure
- Debugging requires checking tool internals — the agent's view shows no error
- Partial writes or mutations go undetected

**Why it fails:** The agent can only reason about what it observes. If the tool reports success, the agent assumes success. Silent failures cascade into larger, harder-to-diagnose failures downstream.

**Fix:** Return explicit error states with actionable messages. Distinguish success, partial success, and failure in the response structure. Include what succeeded and what did not. See [G08 — Tool Result Validation](../patterns/G08-tool-result-validation.md).

---

## 4. The Ambiguous Twin

**What it is:** Two or more tools with overlapping purposes and unclear boundaries — the agent cannot reliably choose between them.

**Symptoms:**
- Agent alternates between two tools for the same task
- Agent calls the wrong tool and then corrects itself (wasting a turn)
- Tool descriptions use similar language ("gets information about..." vs. "retrieves details of...")
- Users must add prompt instructions explaining when to use each tool

**Why it fails:** If the tool descriptions do not make the distinction clear, the model will guess — and guessing correctly requires exactly the kind of disambiguation that should be in the tool design, not the prompt.

**Fix:** Either merge the tools (if they truly overlap) or make their descriptions explicitly contrastive ("Use X for live data from the API; use Y for cached historical data"). Add "do NOT use this when..." clauses. See [G09 — Tool Discovery / Progressive Exposure](../patterns/G09-tool-discovery-progressive-exposure.md).

---

## 5. The Unguarded Destructor

**What it is:** A tool that performs destructive or irreversible operations with no confirmation, gating, or safety check.

**Symptoms:**
- Agent accidentally deletes, overwrites, or corrupts data
- There is no distinction in tool design between "read" and "write" operations
- Recovery from agent mistakes requires manual intervention
- Users are afraid to give the agent access to certain tools

**Why it fails:** Models are probabilistic. Given enough calls, they will eventually invoke a destructive tool incorrectly — wrong parameters, wrong context, or simple hallucination. Without gates, there is no recovery point.

**Fix:** Separate read from write tools. Gate destructive actions behind confirmation or approval. Make destructive tools require explicit parameters that are hard to pass accidentally (e.g., require typing the resource name, not just an ID). See [G05 — Read-Write Separation](../patterns/G05-read-write-separation.md) and [G06 — Tool Gate](../patterns/G06-tool-gate.md).

---

## 6. The Context-Blind Tool

**What it is:** A tool that requires information the agent does not naturally have — internal IDs, encoded references, or state from a previous session that is not in the current context.

**Symptoms:**
- Agent hallucinates parameter values (makes up IDs)
- Agent must call a "lookup" tool before it can call the "action" tool every time
- Tool errors are frequently "not found" or "invalid ID"
- Workflows require 3+ tool calls to accomplish what should be 1

**Why it fails:** The agent only knows what is in its context. If the tool requires a UUID that the agent has never seen, the agent will guess or fabricate one. Requiring hidden prerequisites creates fragile multi-step chains.

**Fix:** Accept human-readable identifiers (names, paths, descriptions) and resolve them internally. If an ID is needed, provide a discovery tool that returns usable IDs first. Chain-dependent tools should accept the output format of the preceding tool directly.

---

## 7. The Undocumented Side Effect

**What it is:** A tool that mutates state beyond what its name or description implies.

**Symptoms:**
- Agent calls a "read" tool and state changes unexpectedly
- Agent cannot predict the consequences of a tool call
- Tool description says "gets X" but internally also updates Y
- System state becomes inconsistent after seemingly safe operations

**Why it fails:** The agent plans based on its understanding of what each tool does. If a tool has hidden side effects, the agent's mental model of system state diverges from reality. Every subsequent decision is based on wrong assumptions.

**Fix:** Tools should do exactly what their name says — no more. If a side effect is necessary, make it a separate tool or document it prominently. Read operations must never mutate. See [G05 — Read-Write Separation](../patterns/G05-read-write-separation.md) and [G10 — Idempotent Action Wrapper](../patterns/G10-idempotent-action-wrapper.md).

---

## Quick Reference Table

| Anti-Pattern | Core Problem | Fix Pattern |
|---|---|---|
| Swiss-Army Tool | Too many responsibilities | G02 — Narrow Tool Interface |
| Firehose Output | Unbounded output size | G01 — Typed Schema-Constrained Tool |
| Silent Failure | Errors not reported | G08 — Tool Result Validation |
| Ambiguous Twin | Unclear tool boundaries | G09 — Tool Discovery |
| Unguarded Destructor | No safety gates | G05 + G06 — Read-Write + Tool Gate |
| Context-Blind Tool | Requires unknowable inputs | Internal resolution + discovery tools |
| Undocumented Side Effect | Hidden state mutation | G05 — Read-Write Separation |

---

## Sources

- AWS — [MCP Tool Scope Strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html)
- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- OpenAI — [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- AWS — [System Design and Security Recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html)
