# Eval Type Selector

**Purpose:** Answer "what eval do I need?" with a structured decision process. Work through the questions in order; stop at the first pattern that fits.

---

## Decision Tree

<details>
<summary><b>Eval Type Selector — Full Decision Tree</b></summary>

```mermaid
flowchart TD
    START([What do I need\nto evaluate?]) --> Q1{Do I know\nwhich step in my\npipeline is failing?}
    Q1 -->|no — find the failing step| P12[D12: Step-Level\nDiagnostic Eval]
    Q1 -->|yes — I know the step\nor have a single-step agent| Q2

    Q2{Is there a\nrunnable test suite\nthat defines 'done'?}
    Q2 -->|yes| P02[D02: Test-Before-Done]
    Q2 -->|no| Q3

    Q3{Is the output\nschema- or rule-\nconstrained?}
    Q3 -->|yes| P01[D01: Deterministic\nValidator]
    Q3 -->|no| Q4

    Q4{Must completion\nbe backed by cited\nartefacts or sources?}
    Q4 -->|yes| P03[D03: Evidence-Based\nCompletion]
    Q4 -->|no| Q5

    Q5{Is there a checklist\nof required properties\nto scan systematically?}
    Q5 -->|yes| P05[D05: Review Pass]
    Q5 -->|no| Q6

    Q6{Would the generating\nagent's context bias\nthe check?}
    Q6 -->|yes| P04[D04: Independent\nVerifier]
    Q6 -->|no| Q7

    Q7{Should low-quality\noutput trigger another\ngeneration attempt?}
    Q7 -->|yes — binary approve/revise| P06[D06: Generator-Critic]
    Q7 -->|yes — with graded score feedback| P07[D07: Evaluator-Optimizer]
    Q7 -->|no| Q8

    Q8{Do you need\nhigh-confidence via\nmultiple reviewers?}
    Q8 -->|yes| P08[D08: Multi-Review\n/ Ensemble]
    Q8 -->|no| Q9

    Q9{Is the quality\ncriterion qualitative —\ntone, reasoning, style?}
    Q9 -->|yes| P09[D09: LLM-as-Judge]
    Q9 -->|no| Q10

    Q10{Is your LLM judge\ncalibrated against\nhuman labels?}
    Q10 -->|no — calibrate first| P10[D10: Human\nCalibration]
    Q10 -->|yes| Q11

    Q11{Does the whole\ntask need a pass/fail\non the real outcome?}
    Q11 -->|yes| P11[D11: End-to-End\nTask-Success Eval]
    Q11 -->|no| DONE([Your current\nevals are sufficient])

    style START fill:#1a3a6b,color:#fff
    style P01 fill:#1a5c2a,color:#fff
    style P02 fill:#1a5c2a,color:#fff
    style P03 fill:#1a5c2a,color:#fff
    style P04 fill:#3a1a5c,color:#fff
    style P05 fill:#1a5c2a,color:#fff
    style P06 fill:#3a1a5c,color:#fff
    style P07 fill:#3a1a5c,color:#fff
    style P08 fill:#3a1a5c,color:#fff
    style P09 fill:#3a1a5c,color:#fff
    style P10 fill:#5c1a1a,color:#fff
    style P11 fill:#5c1a1a,color:#fff
    style P12 fill:#5c1a1a,color:#fff
    style DONE fill:#1a5c2a,color:#fff
```

</details>

---

## Quick-Reference Table

| Question | If yes → use | Pattern |
|----------|-------------|---------|
| Do I need to find which step failed? | Step-Level Diagnostic | [D12](../patterns/D12-step-level-diagnostic.md) |
| Does passing a test suite define "done"? | Test-Before-Done | [D02](../patterns/D02-test-before-done.md) |
| Is the output schema-valid or rule-compliant? | Deterministic Validator | [D01](../patterns/D01-deterministic-validator.md) |
| Must completion cite concrete evidence? | Evidence-Based Completion | [D03](../patterns/D03-evidence-based-completion.md) |
| Is there a checklist of required properties? | Review Pass | [D05](../patterns/D05-review-pass.md) |
| Would generator context bias the check? | Independent Verifier | [D04](../patterns/D04-independent-verifier.md) |
| Should failure trigger binary revision? | Generator-Critic | [D06](../patterns/D06-generator-critic.md) |
| Should failure trigger graded revision? | Evaluator-Optimizer | [D07](../patterns/D07-evaluator-optimizer.md) |
| Need high-confidence via N reviewers? | Multi-Review / Ensemble | [D08](../patterns/D08-multi-review-ensemble.md) |
| Is the criterion qualitative? | LLM-as-Judge | [D09](../patterns/D09-llm-as-judge.md) |
| Is the LLM judge uncalibrated? | Human Calibration | [D10](../patterns/D10-human-calibration.md) |
| Does the full task need a real-outcome check? | End-to-End Task-Success | [D11](../patterns/D11-end-to-end-task-success.md) |

---

## Stacking Rules

Multiple evals can and should be stacked. Common stacks:

**Structured output pipeline:**
```
D01 (schema) → D03 (evidence present) → D09 (quality) → D10 (calibration)
```

**Coding agent:**
```
D01 (syntax / lint) → D02 (tests pass) → D04 (independent logic review)
```

**Research / report agent:**
```
D03 (sources cited) → D05 (required sections present) → D09 (quality judge) → D10 (calibration)
```

**High-stakes pipeline (legal / medical / financial):**
```
D01 → D02 or D03 → D04 → D08 (ensemble) → D10 → D11 (E2E gate)
```

**Debugging a failing pipeline:**
```
D11 (confirm E2E failure) → D12 (find failing step) → targeted fix → D11 (regression check)
```

---

## The Hamel Husain Sequencing Rule

Before designing any eval:

1. **Collect real failing traces** from production or staging. Minimum 20 examples.
2. **Read every trace manually.** Do not skim; look for what actually went wrong.
3. **Build a failure taxonomy.** Label each failure. Count frequencies.
4. **Run D11 (E2E eval) first.** Confirm which tasks fail end-to-end.
5. **Apply D12 (step-level diagnostic)** to failing E2E cases to identify root-cause steps.
6. **Then design targeted evals** for the top failure categories. Use this selector to pick the right pattern per category.

Never design evals from first principles without inspecting real failures. Generic quality axes that were not observed in actual traces waste time and produce misleading metrics.

---

## Related Guides

- [verification-ladder.md](verification-ladder.md) — when to escalate check type (cost vs. capability table).

## Sources

- **Hamel Husain & Shreya Shankar** — independent ML practitioners; leading voices on LLM evaluation methodology. [Why Error Analysis Matters](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html) | [How to Evaluate Agentic Workflows](https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html)
- **Anthropic Engineering** — AI safety company; authors of Claude. [Demystifying Evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **OpenAI Engineering** — AI research company; authors of GPT and Codex. [A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
