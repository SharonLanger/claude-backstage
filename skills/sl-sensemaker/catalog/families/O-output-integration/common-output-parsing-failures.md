# Reference: Common Output Parsing Failures

## Purpose

Use this reference when designing output parsing logic or debugging parsing errors. It catalogs the most common ways model output breaks parsers, with concrete examples and mitigations for each.

---

## Failure Category 1: Structural Wrapping

The model wraps the expected output in additional structure you did not ask for.

| Failure | Example | Why It Happens |
|---------|---------|---------------|
| Markdown code fences | `` ```json\n{"key": "val"}\n``` `` | Model trained on markdown; defaults to formatting code |
| Preamble text | `"Here is the JSON:\n{"key": "val"}"` | Model's helpful instinct adds explanation |
| Trailing commentary | `{"key": "val"}\n\nLet me know if you need changes.` | Model's conversational nature adds follow-up |
| Nested in object | `{"response": {"key": "val"}}` | Model adds a wrapper object for "clarity" |
| XML-style wrapping | `<output>{"key": "val"}</output>` | Model uses tags when it sees tags in context |

**Mitigation:**
- Strip common wrappers before parsing: trim whitespace, remove `` ```json...``` `` fences, remove text before first `{` or `[`
- Use a lenient parser that finds the JSON/structured content within surrounding text
- Make format instructions extremely explicit: "Output ONLY valid JSON. No explanation, no markdown, no wrapper."

---

## Failure Category 2: Schema Violations

The model produces structurally valid output that does not match the expected schema.

| Failure | Example | Why It Happens |
|---------|---------|---------------|
| Missing required field | `{"name": "Alice"}` when `age` is required | Model does not enforce schemas internally |
| Extra fields | `{"name": "Alice", "age": 30, "mood": "happy"}` | Model adds fields it thinks are helpful |
| Wrong type | `"count": "three"` instead of `"count": 3` | Model treats values as natural language |
| Wrong enum value | `"status": "done"` when allowed values are `"completed"/"failed"` | Model paraphrases rather than using exact values |
| Null instead of value | `"result": null` | Model uses null for "I don't know" |
| Array instead of object | `[{"name": "Alice"}]` instead of `{"name": "Alice"}` | Model wraps single items in arrays inconsistently |

**Mitigation:**
- Validate output against schema IMMEDIATELY after parsing
- On schema failure: include the validation error in a retry prompt
- For enums: list the exact allowed values in the prompt AND validate
- For types: coerce where safe (string "3" → number 3) but reject where ambiguous

---

## Failure Category 3: Partial/Truncated Output

The model produces incomplete output due to context window limits or stop sequences.

| Failure | Example | Why It Happens |
|---------|---------|---------------|
| Truncated JSON | `{"items": [{"id": 1}, {"id": 2` | Output hit max_tokens limit |
| Missing closing brackets | `{"nested": {"deep": {"value": 1}` | Deep nesting exhausts attention |
| Ends mid-string | `{"text": "This is a long para` | String content pushes past limit |
| Stops at stop sequence | `{"command": "stop"}` ← generation stopped on "stop" | Stop sequence triggered inside content |
| Empty response | `` (nothing) | Model hit safety filter or errored silently |

**Mitigation:**
- Set `max_tokens` generously above expected output size
- Check output completeness (balanced brackets, valid JSON) before parsing
- If truncated: retry with explicit instruction to be more concise, or split output across multiple calls
- Avoid stop sequences that appear in valid content
- Handle empty responses explicitly (retry or escalate)

---

## Failure Category 4: Encoding and Escaping

The model produces output with incorrect character handling.

| Failure | Example | Why It Happens |
|---------|---------|---------------|
| Unescaped quotes in JSON | `{"text": "She said "hello""}` | Model forgets JSON string escaping rules |
| Unescaped newlines in JSON | `{"text": "line1\nline2"}` (literal newline, not `\n`) | Model outputs actual newlines inside strings |
| Unicode escaping inconsistency | `"\u0041" vs "A"` mixed in same output | Model randomly chooses representations |
| HTML entities in plain text | `"5 &gt; 3"` instead of `"5 > 3"` | Model confuses output contexts |
| Backslash handling | `"path": "C:\new\folder"` (interprets `\n` as newline) | Model does not double-escape backslashes |

**Mitigation:**
- Use a lenient JSON parser that handles common escape failures
- Post-process strings: normalize unicode, fix unescaped characters
- For code output: validate syntax before executing
- For file paths: normalize separators and reject if malformed after normalization

---

## Failure Category 5: Semantic Correctness Issues

The output is structurally valid but semantically wrong in ways that break downstream logic.

| Failure | Example | Why It Happens |
|---------|---------|---------------|
| Hallucinated IDs | `"file_id": "abc123"` (does not exist) | Model invents plausible-looking identifiers |
| Stale references | `"function": "handleClick"` (function was renamed) | Model uses outdated context |
| Impossible values | `"confidence": 1.5` (should be 0–1) | Model does not enforce numeric constraints |
| Circular references | Step 3 depends on Step 5 which depends on Step 3 | Model does not track dependency graphs well |
| Off-by-one in lists | `"items": [...]` has 9 items when 10 were requested | Model counts poorly |

**Mitigation:**
- Validate IDs against actual data before using
- Range-check all numeric values
- Validate graph structures (DAG check for dependencies)
- Count array elements explicitly rather than trusting the model's count
- Cross-reference claims against source data

---

## Failure Category 6: Inconsistency Across Calls

The model produces output that contradicts its previous output in multi-turn scenarios.

| Failure | Example | Why It Happens |
|---------|---------|---------------|
| Different schema each time | First call returns `{name, age}`, second returns `{full_name, years}` | Model paraphrases field names |
| Different enum values | First uses "high/medium/low", second uses "critical/warning/info" | Model generates synonyms |
| Contradicting facts | "The file has 10 functions" → later → "All 8 functions are tested" | Model does not maintain consistency across turns |
| Format drift | First call: JSON. Fifth call: markdown table. Tenth call: prose. | Model drifts without strong anchoring |

**Mitigation:**
- Include the exact schema in EVERY call (not just the first)
- Use few-shot examples that demonstrate the exact format
- Validate output format consistency across calls
- For multi-turn: include a "format reminder" in each turn's prompt

---

## Parser Robustness Strategies (Summary)

| Strategy | Complexity | Robustness Gain |
|----------|-----------|----------------|
| Strip wrappers (fences, preamble) | Low | Handles 60% of Category 1 |
| Lenient JSON parser (finds JSON in text) | Low | Handles 80% of Category 1 |
| Schema validation + retry with error | Medium | Handles 90% of Category 2 |
| max_tokens headroom + completeness check | Low | Handles 70% of Category 3 |
| String post-processing (escaping fixes) | Medium | Handles 60% of Category 4 |
| Semantic validation (range, existence) | High | Handles Category 5 |
| Format anchoring (schema every call) | Low | Prevents most of Category 6 |

---

## Quick Diagnostic: "My Parser Broke"

```
What does the raw output look like?
│
├── Cannot find JSON/structure at all → Category 1 (wrapping) or Category 3 (empty)
├── Found structure but parser rejects it → Category 4 (encoding) or Category 3 (truncation)
├── Parsed successfully but validation fails → Category 2 (schema) or Category 5 (semantic)
└── Works sometimes, fails randomly → Category 6 (inconsistency) or Category 3 (truncation at limit)
```

## Related Patterns

- [Output Boundary Checklist](output-boundary-checklist.md) — the full checklist for output boundaries
- [O patterns](patterns/) — patterns for structured output, validation, and guardrails

## Sources

- OpenAI — [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- AWS — [Agent Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agent-patterns.html)
- OWASP — [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
