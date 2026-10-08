# Theater Model

Most multi-agent workflows fail the same way: context bloats, retries repeat mistakes, state scatters across conversations, and recovery means starting over. The Theater Model is a structured execution framework — built on [36 established design patterns](design-patterns/README.md) from Anthropic, OpenAI, Google, AWS, Microsoft, and OWASP — that solves these problems architecturally, not with prompting tricks.

A **Play** defines the work. **Acts** break it into sequential steps. **Leads** and **Cast** do the work. A **Stage Manager** coordinates. A **Checklist Agent** verifies. A **Director** (human) decides at **Gates**. Every agent gets fresh context, bounded retries, and file-based state — producing cache-efficient, recoverable, auditable executions by default.

Need human approval before a critical step? Add a **Gate**. No agent has ever passed one autonomously — structurally impossible, not just discouraged. Need confidence that Act 3's output is actually correct before Act 4 begins? The **Checklist Agent** runs in a fresh, isolated context with no access to the generator's reasoning — zero confirmation bias, just evidence against criteria. And because Acts are self-contained units with defined inputs and outputs, a Play is composable like building blocks: swap an Act, add one, reorder the sequence — the model adapts to your workflow, not the other way around.

## Quick start

1. Copy `template/` to a new folder
2. Rename placeholders in `play.md`
3. Define your Acts, Leads, and Cast
4. Place reference material in `reference/`
5. Hand off to a Stage Manager agent

See `template/README.md` for the full 10-step setup guide.

## How a Play runs

```
Setup (human authors the Play)
  │
  ▼
Stage Manager reads play.md, starts Act 1
  │
  ▼
Lead (+ Cast) execute the Act, write outputs to stage/ and handoffs/
  │
  ▼
Checklist Agent verifies the Act's outputs → PASS or FAIL
  │
  ▼
Gate? ─── yes ──→ Director (human) reviews and decides
  │                  │
  no                 ▼
  │              approved / rejected / skip
  ▼                  │
Stage Manager advances to next Act ◄─────┘
  │
  ▼
All Acts complete → Play done, progress.md records final state
```

On failure: Stage Manager retries the Act (up to 2 retries, same Lead instance). On retry exhaustion: escalates to the Director.

## Folder layout

```
theater-model/
├── README.md              ← you are here
├── model/                 ← learn the model (concepts, schemas, rules, guides)
├── template/              ← copy this to create a new Play
└── example/               ← see it in action (annotated Play examples)
```

### model/ — understand the model

| Folder | What's there |
|--------|-------------|
| `overview/` | What the model is, glossary, narrative walkthrough |
| `execution/` | Lifecycle, execution flow, recovery rules |
| `schemas/` | One file per Play file type — the format spec |
| `play/` | Play definition, authoring guide, examples |
| `acts/` | Act definition, Lead vs Cast roles, authoring guide |
| `agents/` | Director, Stage Manager, Checklist Agent, golden rules |
| `workspace/` | Folder structure, locations, read/write permissions |
| `runtime/` | Settings precedence, context loading, agent identity |
| `rules/` | Mandatory constraints: authority, delegation, truthfulness |
| `guidelines/` | Recommended practices for checklists, verification, exceptions |

Three reading paths depending on your goal:

1. **5-minute orientation** — `overview/` (all 3 files)
2. **Play author** — `overview/` → `execution/flow.md` → `play/` → `acts/` → relevant `schemas/` → `workspace/`
3. **Full model** — all of the above + `agents/` → `runtime/` → `rules/` → `guidelines/`

### template/ — create a Play

The template IS a Play folder. Copy it, rename it, fill in the `{{placeholders}}`. It mirrors the canonical folder structure with all required files, sections, and default content in place.

15 files: 9 content templates, 1 README, 5 `.gitkeep` for empty directories.

### example/ — see it in action

Two annotated Play examples showing different task structures:
- **Compact** — test → fix → review (3 Acts, minimal Cast)
- **Detailed** — review → fix → test (3 Acts, multi-Cast)

## Key concepts

| Concept | What it is |
|---------|-----------|
| **Play** | A complete task definition: goal, Acts, Gates, checklists, rules |
| **Run** | One execution of a Play (a Play can be run multiple times) |
| **Act** | A sequential step with one goal, one Lead, optional Cast |
| **Lead** | The primary agent for an Act — coordinates Cast, writes outputs |
| **Cast** | Specialist agents under a Lead — one focused task each |
| **Director** | The human — makes decisions at Gates, owns the final call |
| **Stage Manager** | Coordinates execution — calls Leads, updates progress, handles recovery |
| **Checklist Agent** | Independent verifier — fresh instance per check, no delegation, 8 golden rules |
| **Gate** | A hard stop requiring human approval before the next Act proceeds |
| **progress.md** | The checkpoint file — tracks what's done, what's running, what's next |

## Scope and limitations

Current version supports:
- Sequential Acts (one at a time, in order)
- Bounded recovery (2 retries per Act per Run)
- Forward-only execution (no backward jumps)
- File-based communication between agents

Not yet supported:
- Parallel Acts
- Looping or conditional branching
- Automatic backward recovery
- Real-time inter-agent messaging
