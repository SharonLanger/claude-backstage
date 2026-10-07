# Test 02 — Multi-Phase Execution

## Blueprint

### Trigger
Invoke the skill with a multi-phase task requiring sequential execution.

### Input
- Task: "Execute a three-step workflow where each step builds on the previous"
- Configuration: default settings, 3 phases

### Expected Behavior
1. The skill reads the task input
2. Plans 3 phases of work in sequence
3. Executes phase 1, passes result to phase 2, passes result to phase 3
4. Collects all phase results
5. Produces a final output combining all phase results

### Environment
- Standard agent environment
- No special setup required
