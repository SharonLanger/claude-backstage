# Test 02 — Assertions

## Structural Assertions
Verify the skill's output has the correct shape and completeness.

- [ ] Output file exists at the expected path
- [ ] Output contains results from all 3 phases
- [ ] Each phase result is labeled with its phase number
- [ ] Summary section references all phases

## Functional Assertions
Verify the skill produces correct behavior.

- [ ] The skill planned exactly 3 phases
- [ ] Phases executed in the correct order (1, 2, 3)
- [ ] Phase 2 received phase 1's output as input
- [ ] Phase 3 received phase 2's output as input
- [ ] The final output combines all phase results correctly

## Log Assertions
Verify execution followed the expected flow.

- [ ] Skill entry point was invoked
- [ ] Phase planning step completed for 3 phases
- [ ] Phase 1 execution completed
- [ ] Phase 2 execution completed
- [ ] Phase 3 execution completed
- [ ] Final output generation step completed
- [ ] No error messages in execution logs
