# Writing Guide: Acts and Roles

How to author Act definitions and role files. Assumes you have read [definition.md](definition.md) and [roles.md](roles.md).

## Step by step

### 1. Define the Act's goal

Write one or two sentences that say what this Act achieves. Apply the one-Act-one-goal principle — if the goal has two separable parts, split into two Acts.

The goal should describe the outcome, not the process:
- Good: "Produce a test report covering all required scenarios with evidence."
- Bad: "Run tests." (too vague — what tests? what output?)

### 2. Name the Act

Use the pattern `act-NN-slug`:
- NN is a two-digit order number starting at 01.
- Slug is 1-3 hyphen-separated words describing what the Act *does*.

Create the folder `acts/act-NN-slug/` and the Act file `act-NN-slug.md` inside it.

### 3. Define the workspace

Point `## Workspace` to `acts/act-NN-slug/stage/` with a one-line description of how actors use it. This is a required section.

### 4. Define inputs and outputs

**Inputs** — what the Act reads. List specific paths:
- `reference/` paths for shared static data.
- `acts/act-NN-slug/props/` for Act-specific input data.
- `handoffs/act-MM-slug/` for outputs from earlier Acts.

**Outputs** — what the Act produces. Everything lands in `handoffs/act-NN-slug/`. Name the specific files and describe what each contains.

The first Act's inputs come only from `reference/` and its own `props/`. Later Acts also read earlier Acts' handoffs.

### 5. Write the internal flow

The `## Flow` section describes the coordination inside the Act: who does what, in what order, and where intermediate files land in `stage/`.

Number the steps. Each step names the actor (Lead or specific Cast) and the action:

```
1. Lead reads inputs and creates the assignment plan in stage/.
2. Cast-Test-Runner executes each test case, writing results to stage/.
3. Cast-Result-Verifier checks each result against expected values in stage/.
4. Lead consolidates Cast outputs into handoffs/act-01-run-tests/test-report.md.
```

The flow is a coordination plan, not a procedure manual. Describe what each actor does, not how they do it internally. Note that any Act agent (Lead or Cast) may write to `handoffs/act-NN-slug/` — the Lead does not have exclusive access there.

### 6. Decide: Lead-only or Lead + Cast

**Lead-only** when:
- The work is straightforward enough for one agent.
- There's no natural decomposition into focused subtasks.

**Lead + Cast** when:
- The work has distinct subtasks that benefit from focused agents.
- Different parts need different scope constraints or expertise.
- The Lead's main job is coordination and synthesis.

If you add Cast, each Cast member should have a single focused task. If a Cast member's responsibilities span two unrelated things, split it.

### 7. Write the Lead file

Create `lead-slug.md` in the Act folder. The slug describes what this Lead does (not the Act name):
- Good: `lead-test-coordinator.md`, `lead-skill-fixer.md`
- Bad: `lead.md` (no slug), `lead-act-01.md` (describes the Act, not the role)

The Lead file starts with two mandatory `@` references:
```
@../../management/play-rules.md
@./act-NN-slug.md
```

Then fill in: Responsibilities, Access (reads/writes), Cast coordination, Runtime overrides.

### 8. Write Cast files (if any)

Create `cast-slug.md` for each Cast member. Same `@` references as the Lead file. Fill in: Responsibilities (narrow, focused), Access, Runtime overrides.

### 9. Define Act rules and runtime defaults

**Rules** (`## Rules`) — mandatory constraints for this Act that actors cannot weaken. If the Act has no special rules, write: "No Act-specific rules beyond the shared Play rules."

**Runtime defaults** (`## Runtime defaults`) — inheritable settings like model or reasoning effort. If no Act-level overrides: "Inherit from `play-rules.md`." Role files can override these further.

Rules and defaults are separate sections — rules are not overridable; defaults are.

### 10. Set up the folder

Create the Act's folder structure:
```
acts/act-NN-slug/
├── act-NN-slug.md       ← Act definition
├── lead-slug.md         ← Lead file
├── cast-slug.md         ← Cast file(s), if any
├── props/               ← Static input data for this Act
└── stage/               ← Mutable workspace (empty at setup)
```

## Common mistakes

### Overloading an Act

If the Act's checklist needs to verify two unrelated properties, the Act does too much. Split it.

### Vague inputs/outputs

"Reads relevant files" tells nobody anything. Name the specific paths:
- Bad: "Inputs: relevant reference files."
- Good: "Inputs: `reference/skill-baseline/`, `reference/requirements.md`."

### Flow that describes internal agent behavior

The flow describes coordination (who does what, where), not how an agent thinks internally:
- Bad: "Lead analyzes the requirements and determines the best approach."
- Good: "Lead reads requirements and writes the review plan to `stage/plan.md`."

### Cast with broad responsibilities

Each Cast should have one focused task. If a Cast member is doing review AND fixing AND testing, it's doing too much — split into separate Cast or let the Lead handle it.

### Missing @ references

Every Lead and Cast file must start with the two `@` references before any heading. Forgetting these means the agent won't load shared rules or the Act definition.

### Putting checklist items in the Act file

Checklists belong in `play.md`, not in the Act file. The Act file describes what the Act does; verification criteria are defined at the Play level.

### Duplicating management content

Retry logic, generic coordination rules, and verification procedures belong in `management/`. If you're writing "the Stage Manager should..." in an Act file, it belongs elsewhere.
