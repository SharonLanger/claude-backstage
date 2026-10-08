# Writing Guide: play.md

How to author a Play definition. Assumes you have read [definition.md](definition.md) and know what a Play is.

## Step by step

### 1. Start with the title and goal

Write the Play title heading (`# Play: <title>`) and 1-3 sentences that say what this Play achieves. The goal anchors every scoping decision that follows.

### 2. Identify the stages

Break the goal into sequential stages. Each stage becomes an Act. Apply the one-Act-one-goal principle — if a stage has two separable goals, it should be two Acts.

Stages must be ordered so each Act's inputs are available from shared references or prior Acts' handoffs. If two stages need each other's output, they are one Act with internal coordination, not two Acts.

### 3. Name the Acts

Use the pattern `act-NN-slug` — two-digit order number, 1-3 descriptive hyphen-separated words.

The name should describe what the Act *does*, not what it *is about*:
- `act-01-run-tests` (what it does)
- `act-01-testing` (too vague)

### 4. Assign agents

For each Act, decide:

- **Lead** (required): who coordinates the work and produces outputs.
- **Cast** (optional): specialized agents the Lead can delegate to.

A simple Act that one agent can handle needs only a Lead. Add Cast when the work benefits from specialized sub-agents working on focused subtasks.

### 5. Write the Acts and Actors summary table

Before the individual Act sections, write a summary table listing every Act with its Lead and Cast. This gives readers the full cast at a glance. List actor file paths below the table.

### 6. Define inputs and outputs

For each Act:

- **Inputs**: what the Act reads. Reference paths, prop paths, or handoffs from earlier Acts.
- **Outputs**: what the Act produces in `handoffs/<act>/`. Be specific — name the output files and describe them.

The first Act's inputs come from `reference/` and its own `props/`. Later Acts also read earlier handoffs.

### 7. Write checklists

Each Act gets a checklist — a list of verification criteria the Checklist Agent will check.

Write checks that are:
- **Specific** — "Both output files exist" beats "Outputs are complete."
- **Verifiable from files** — the Checklist Agent checks by reading outputs, not by rerunning work.
- **Complete** — cover the Act's stated outputs and the important quality properties.

Avoid generic checks ("The Act completed successfully") and procedural steps ("Run the tests"). Checklists describe what should be true about the outputs, not what the Act should do.

### 8. Place Gates

Gates go between Acts where the Director must make a decision before work continues. Common Gate placements:

- **After a review Act, before an action Act** — the Director approves which findings to act on.
- **After a high-stakes Act** — the Director confirms the output before it feeds into later work.
- **Not needed** between every Act pair — only where a human decision genuinely adds value.

Each Gate needs:
- **Presentation instructions** — what evidence to show the Director.
- **Decision needed** — the specific question the Director answers.
- **A name** — `gate-<slug>`, agents use max 3 words; Play authors may use more when clarity requires it.

### 9. List shared references

At the top of `play.md`, list the `reference/` paths that multiple Acts use. Each entry should have a short description.

## Sequencing decisions

### How many Acts?

Too few Acts bundles unrelated work together, making verification broad and failures hard to diagnose. Too many Acts creates overhead without proportional benefit.

A good Act is large enough to produce a meaningful, verifiable output and small enough that its checklist is specific.

### Where to put Gates?

A Gate is justified when:
- The next Act's work depends on a *human judgment* about the current Act's output — not just whether it passed verification.
- The cost of proceeding with a wrong decision is high enough to warrant stopping.

If the checklist alone determines whether to proceed, a Gate is unnecessary.

## Common mistakes

### Duplicating management content in play.md

Generic retry logic, verification procedures, and agent coordination rules belong in `management/`. If you find yourself writing "the Stage Manager should..." in `play.md`, move it.

### Writing procedural checklists

Checklists describe *what should be true*, not *what to do*:
- Wrong: "Run each test case and record the result."
- Right: "Every required test has a recorded expected/actual result with evidence."

### Vague inputs/outputs

"Reads relevant files" tells nobody anything. Name the specific paths:
- Wrong: "Inputs: relevant reference files."
- Right: "Inputs: `reference/skill-baseline/`, `reference/requirements.md`."

### Overloading an Act

If an Act's checklist needs to verify two unrelated properties, the Act likely does too much. Split it.

### Missing the goal

Every decision (Act scoping, Gate placement, checklist criteria) should trace back to the Play's stated goal. If a component doesn't serve the goal, it doesn't belong.
