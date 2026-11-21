# Source Registry & Citation Rules

Verified sources approved for citation, plus rules for how to cite them.

---

## Citation Rules

1. **Every pattern file MUST have a Sources section** with 2–6 links.
2. **Every link MUST be verifiable** — it must point to a real, published blog post, documentation page, or academic resource.
3. **Never invent URLs.** If you cannot find a real source for a claim, do not make the claim.
4. **Use only sources from the Verified Source Registry** (below) unless you have personally verified a new URL exists.
5. **Format:** `- Author/Org — [Article Title](URL)`

### What counts as a valid source

| Valid | Not Valid |
|---|---|
| Published blog post with a URL | "Common industry practice" |
| Official documentation page | "Well-known pattern" |
| Academic paper or lecture material | A URL you constructed but didn't verify |
| Open-source repository README | Hearsay or "I've seen this used" |
| OWASP/NIST/ISO published standard | A blog that no longer exists |

### Mapping sources to claims

Every substantial claim in a pattern file (the Problem, the Solution Structure, the trade-offs) must be supportable by at least one source in the Sources section. The source doesn't need to use the exact same name — it needs to describe the same structural solution to the same recurring problem.

### Adding a new source

1. Verify the URL resolves to a real, published page
2. Add it to the appropriate table below with the next sequential number
3. Add a Family–Source Mapping entry if the source is relevant to specific families

---

## Verified Source Registry

### Primary Sources (high-authority engineering guidance)

| # | Org | Title | URL |
|---|---|---|---|
| 1 | Anthropic | Building Effective Agents | https://www.anthropic.com/engineering/building-effective-agents |
| 2 | Anthropic | Effective Context Engineering for AI Agents | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| 3 | Anthropic | Demystifying Evals for AI Agents | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents |
| 4 | OpenAI | Harness Engineering | https://openai.com/index/harness-engineering/ |
| 5 | OpenAI | A Practical Guide to Building AI Agents | https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/ |
| 6 | OpenAI | Unrolling the Codex Agent Loop | https://openai.com/index/unrolling-the-codex-agent-loop/ |
| 7 | OpenAI | Unlocking the Codex Harness | https://openai.com/index/unlocking-the-codex-harness/ |
| 8 | OpenAI | Open-Source Codex Orchestration: Symphony | https://openai.com/index/open-source-codex-orchestration-symphony/ |
| 9 | Google Cloud | Choose a Design Pattern for Your Agentic AI System | https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system |
| 10 | Microsoft | AI Agent Orchestration Patterns | https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns |
| 11 | AWS | Agentic AI Patterns and Workflows | https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html |
| 12 | AWS | Agent Patterns | https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html |
| 13 | AWS | System Design and Security Recommendations | https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-system-design.html |
| 14 | AWS | MCP Tool Scope Strategy | https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html |
| 15 | OWASP | Top 10 for Agentic Applications 2026 | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ |
| 16 | OWASP | LLM Top 10 | https://genai.owasp.org/llm-top-10/ |
| 17 | OWASP | Prompt Injection | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ |

### Practitioner / Expert Sources

| # | Author | Title | URL |
|---|---|---|---|
| 18 | Hamel Husain & Shreya Shankar | Evals Skills for Coding Agents | https://hamel.dev/blog/posts/evals-skills/ |
| 19 | Hamel Husain & Shreya Shankar | LLM Evals FAQ | https://hamel.dev/blog/posts/evals-faq/ |
| 20 | Hamel Husain & Shreya Shankar | Evaluating Agentic Workflows | https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html |
| 21 | Hamel Husain & Shreya Shankar | Why Is Error Analysis Important | https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html |
| 22 | Simon Willison | The Lethal Trifecta for AI Agents | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ |
| 23 | Simon Willison | Living Dangerously with Claude | https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/ |

### Academic / Educational

| # | Institution | Title | URL |
|---|---|---|---|
| 24 | Stanford | CS224G — Agentic Design Patterns | https://web.stanford.edu/class/cs224g/2025/lectures/Agentic_Design_Patterns.pdf |

### Open Source

| # | Org | Title | URL |
|---|---|---|---|
| 25 | AWS Samples | Agentic Design Patterns Repository | https://github.com/aws-samples/sample-agentic-design-patterns |

---

## Family–Source Mapping

Which sources are most relevant to each family. When writing a pattern file, cite from its family's primary sources first.

| Family | Primary Sources (by registry #) | Why |
|---|---|---|
| **A — Workflow Topology** | 1, 5, 9, 12, 10 | Anthropic defines the topology taxonomy; Google/AWS/OpenAI/Microsoft validate it |
| **B — Task Decomposition** | 1, 4, 9, 24 | Anthropic+Google define decomposition; OpenAI harness drives plan→execute; Stanford/Ng teaches planning |
| **C — Orchestration** | 5, 8, 10, 9, 12 | OpenAI Symphony + Guide; Microsoft distributed-systems framing; Google coordinator patterns |
| **D — Verification** | 3, 18, 19, 20, 21, 9 | Anthropic evals guide; Hamel/Shreya evaluation methodology; Google review/critique patterns |
| **E — Context Engineering** | 2, 4, 10, 9 | Anthropic coined context engineering; OpenAI map-not-manual; Microsoft minimal-context handoff |
| **F — Harness Engineering** | 4, 6, 7, 8 | OpenAI coined and defined harness engineering across 4 articles |
| **G — Tool Design** | 5, 14, 12, 13 | OpenAI agent guide tool design; AWS MCP tool scope + agent patterns + security |
| **H — Deterministic Control** | 13, 4, 1, 12 | AWS deterministic-override principle; OpenAI mechanical enforcement; Anthropic gate patterns |
| **I — Reliability** | 12, 4, 9, 25 | AWS validation-retry + error classification; OpenAI bounded loops; Google loop termination |
| **J — Security** | 22, 23, 15, 16, 17, 13 | Simon Willison lethal trifecta; OWASP agentic+LLM top 10 + injection; AWS security design |
| **K — Human Control** | 9, 5, 10, 15 | Google human-in-the-loop; OpenAI guide; Microsoft human participation; OWASP oversight |
| **L — Memory & State** | 10, 13, 9, 4 | Microsoft external persistent state; AWS session isolation + shared memory; Google context persistence |
| **M — Observability** | 10, 18, 19, 4 | Microsoft per-agent observability; Hamel trace-driven eval; OpenAI harness feedback loops |
| **N — Efficiency & Routing** | 1, 9, 12, 25 | Anthropic routing pattern; Google cost/latency criteria; AWS confidence routing |
| **O — Output & Integration** | 5, 12, 15, 13 | OpenAI structured output + guardrails; AWS schema validation; OWASP improper output handling |

---

Last updated: 2026-11-19
