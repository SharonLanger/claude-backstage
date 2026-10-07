# Test 01 — Assertions

## Structural Assertions
Verify the skill's output has the correct shape and completeness.

- [ ] Output file exists at the expected path
- [ ] Output contains a summary section
- [ ] Phase result is included in the output
- [ ] No placeholder or template text remains in the output

## Functional Assertions
Verify the skill produces correct behavior.

- [ ] The skill planned exactly 1 phase
- [ ] The phase agent was spawned with the correct input
- [ ] The phase result was incorporated into the final output
- [ ] The output accurately reflects the task that was given

## Log Assertions
Verify execution followed the expected flow.

- [ ] Skill entry point was invoked
- [ ] Phase planning step completed
- [ ] Phase execution step completed
- [ ] Final output generation step completed
- [ ] No error messages in execution logs
