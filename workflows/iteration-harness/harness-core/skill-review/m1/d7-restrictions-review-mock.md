> **Mock example** — this file demonstrates the format and content generated during the iteration process. Replace with real data from your own runs.

# Dimension Review: D7 — Restriction Consistency

## Score: 6/10

## Justification

Most restrictions are stated consistently, but two restrictions defined in the phase-type spec are absent from the agent spec. An agent reading only its own spec file gets an incomplete restriction set. One restriction also has a semantic mismatch between the two files.

## Checklist Results

| Check | Verdict | Evidence |
|-------|---------|----------|
| 7.1 "Cannot read other phase folders" | PASS | Stated identically in both files. |
| 7.2 "Cannot write outside output/" | PASS | Stated identically in both files. |
| 7.3 "Cannot spawn sub-agents" | PASS | Stated identically in both files. |
| 7.4 "Cannot access internet" | FAIL | Phase-type defines it. Agent spec omits it entirely. |
| 7.5 "Cannot modify briefing" | FAIL | Phase-type defines it. Agent spec omits it entirely. |
| 7.6 "Orchestrator never performs work" | PASS | Clear in orchestrator spec. |
| 7.7 "Planner never performs phase work" | PASS | Boundaries section is clear. |

## Findings

### Finding 1: Missing "cannot access internet" restriction

- **Severity:** Major
- **Location:** Agent spec, Boundaries section
- **Issue:** Phase-type defines "Cannot access the internet" but agent spec does not include it. An agent reading only its spec gets an incomplete restriction set.
- **Delta category:** Correctness
- **Delta magnitude:** 1 line addition

### Finding 2: Missing "cannot modify briefing" restriction

- **Severity:** Major
- **Location:** Agent spec, Boundaries section
- **Issue:** Phase-type defines "Cannot modify the briefing or input" but agent spec omits both. Same gap as Finding 1.
- **Delta category:** Correctness
- **Delta magnitude:** 1 line addition

### Finding 3: Communication restriction semantic mismatch

- **Severity:** Minor
- **Location:** Agent spec says "cannot communicate with other phases"; phase-type says "cannot communicate with orchestrator about workflow decisions"
- **Issue:** Different scopes — one restricts inter-phase communication, the other restricts upward communication about decisions. Both are valid restrictions but they describe different things using similar language.
- **Delta category:** Robustness
- **Delta magnitude:** Wording clarification, ~1 line
