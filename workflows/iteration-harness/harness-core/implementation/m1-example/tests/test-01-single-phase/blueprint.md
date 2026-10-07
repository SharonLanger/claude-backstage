# Test 01 — Single-Phase Execution

## Blueprint

### Trigger
Invoke the skill with a single-phase task.

### Input
- Task: "Execute a one-step workflow"
- Configuration: default settings, single phase

### Expected Behavior
1. The skill reads the task input
2. Plans a single phase of work
3. Spawns an agent for the phase
4. Collects the phase result
5. Produces a final output summarizing the result

### Environment
- Standard agent environment
- No special setup required
