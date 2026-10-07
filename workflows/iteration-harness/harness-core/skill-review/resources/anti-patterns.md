# Anti-Patterns Catalog

> **This is a mock example** (`-mock` content) showing the format of anti-pattern entries discovered through iteration. In practice, this catalog grows organically as reviews expose recurring issues. Replace these entries with patterns from your own skill development.

---

## How Anti-Patterns Are Added

1. A Dimension Reviewer identifies a recurring issue across multiple reviews
2. The Synthesis Agent flags it as a pattern (not a one-off)
3. The pattern is cataloged here with an ID for future reference
4. Future reviewers check against this catalog to catch regressions

---

## Catalog

### AP-01: Passive Instruction Language

- **What it looks like:** Skill instructions describe what should happen ("the output should contain...") instead of commanding it ("write the output to...")
- **Why it's a problem:** Agents interpret passive language as informational context, not actionable directives. Causes execution loops where the agent plans but never acts.
- **How to fix:** Rewrite all instructions in imperative form. Every step should start with a verb: "read", "write", "create", "copy", "spawn".
- **Example:** "The planner should produce a plan" → "Write the plan to `workspace/planner.md`"
- **First seen:** M1 review-1, D4 (Flow Coherence)
- **Severity:** Critical — causes complete execution failure

### AP-02: Duplicated Source of Truth

- **What it looks like:** The same concept (e.g., output format, error handling rules) is defined in two or more files with slightly different wording.
- **Why it's a problem:** Agents pick up one definition and miss the other. When definitions drift apart, behavior becomes non-deterministic depending on which file the agent reads first.
- **How to fix:** Pick one canonical location. All other files reference it with a pointer: "See `format.md` section X for the output format."
- **Example:** Log format defined in both `orchestrator.md` and `format.md` with different column orders.
- **First seen:** M1 review-1, D2 (SSOT)
- **Severity:** Major — causes intermittent inconsistencies

### AP-03: Unbounded Agent Read Scope

- **What it looks like:** An agent's instructions say "read all relevant files" or "review the skill" without specifying which files.
- **Why it's a problem:** The agent reads everything, consuming tokens on irrelevant content. Worse, it may act on information outside its responsibility scope.
- **How to fix:** Every agent's Input Contract lists exactly which files it reads. Use explicit paths, not categories.
- **Example:** "Review the skill for quality" → "Read `SKILL.md`, `actors/orchestrator.md`, and `phase-types/mono.md`"
- **First seen:** M1 review-1, D3 (Token Efficiency)
- **Severity:** Major — wastes 20-40% of token budget on irrelevant reads

### AP-04: Missing Error Recovery Path

- **What it looks like:** The skill defines the happy path but not what happens when an agent fails mid-execution.
- **Why it's a problem:** When an agent hits an error, it either stops silently or improvises a recovery path that may corrupt the workspace state.
- **How to fix:** For each actor, define: (1) what constitutes a failure, (2) what the actor writes on failure, (3) what the orchestrator does when it detects the failure artifact.
- **Example:** Phase agent fails to create output file → orchestrator retries indefinitely instead of escalating.
- **First seen:** M2 review-1, D5 (Scenario Completeness)
- **Severity:** Major — causes silent failures or infinite loops

### AP-05: Cross-File Restriction Drift

- **What it looks like:** A restriction in an actor file ("cannot spawn sub-agents") doesn't appear in the corresponding phase-type file, or vice versa.
- **Why it's a problem:** The agent may follow one file's rules and violate the other's. Restrictions must be stated identically in every file that governs the agent's behavior.
- **How to fix:** Maintain a restriction registry. Every restriction has one canonical source and is quoted verbatim (not paraphrased) in all other locations.
- **Example:** `phase-agent.md` says "maximum 3 retries" but `mono.md` says "retry until success".
- **First seen:** M1 review-1, D7 (Restriction Consistency)
- **Severity:** Critical — causes unpredictable boundary violations
