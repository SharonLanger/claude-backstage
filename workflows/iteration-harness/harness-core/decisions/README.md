# Decisions

Decision files are written here by the **Reasoner** agent after analyzing test results or review findings.

Each decision file contains:
- The evidence examined (test results, review scores)
- Root-cause analysis
- Delta assessment (is this worth fixing?)
- Fix instructions or "skip" verdict

Decision files are the institutional memory of the iteration process.

---

## Mock Examples

The `-mock` files in this folder demonstrate the format and content of real decision documents. They are templates only — replace them with actual decisions from your iteration runs.

- `decision-m1-test-failure-mock.md` — Reasoner analysis of test failures with root-cause identification
- `decision-m1-review-findings-mock.md` — Reasoner analysis of review findings with delta acceptance rules
