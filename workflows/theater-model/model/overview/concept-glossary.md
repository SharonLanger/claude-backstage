# Concept Glossary

Alphabetized. Each entry links to the relevant section in the model documentation.

| Concept | Definition |
|---|---|
| **Act** | A focused stage of work within a Play. Has exactly one Lead, zero or more Cast, and its own workspace. See [acts/](../acts/). |
| **Cast** | A supporting agent within an Act, assigned by the Lead. Does specialized work within a narrow scope. See [acts/roles.md](../acts/roles.md). |
| **Checklist** | A list of verifications defined in `play.md` that must pass before an Act is marked Done. See [play/](../play/). |
| **Checklist Agent** | An independent verifier. Fresh instance per verification, no delegation, writes only its report. See [agents/checklist-agent.md](../agents/checklist-agent.md). |
| **Director** | The human user. Highest authority — approves Gates, may override any rule within stated scope. See [agents/director.md](../agents/director.md). |
| **Gate** | A mandatory hard stop in the workflow. Only explicit Director approval opens it. See [play/](../play/). |
| **Handoff** | An Act's shared output folder (`handoffs/<act>/`). Readable by all subsequent Acts. See [workspace/](../workspace/). |
| **Lead** | The primary agent in an Act. Coordinates Cast, produces outputs, may work alone. Exactly one per Act. See [acts/roles.md](../acts/roles.md). |
| **Play** | A complete workflow definition: goal, Acts, Gates, Checklists, and participants. Defined in `play.md`. See [play/](../play/). |
| **Props** | Static supporting files for an Act (`acts/<act>/props/`). Read-only during execution. See [workspace/](../workspace/). |
| **Progress** | The execution record (`progress.md`). Tracks Act/Gate status, timestamps, attempts, and Director decisions. Only the Stage Manager writes it. See [execution/](../execution/). |
| **Reference** | Shared static files (`reference/`) available to all Acts. Read-only during execution. See [workspace/](../workspace/). |
| **Run** | One execution of a Play. Each Run uses a fresh Play folder. See [execution/](../execution/). |
| **Stage** | An Act's mutable workspace (`acts/<act>/stage/`). Internal work and actor-to-actor file exchange happen here. See [workspace/](../workspace/). |
| **Stage Manager** | The coordinator agent. Runs the Act sequence, calls Leads and Checklist Agent, enforces Gates, maintains progress. Does no Act work. See [agents/stage-manager.md](../agents/stage-manager.md). |
| **Verification** | A Checklist Agent run that checks an Act's outputs. Produces a report in `verifications/<act>/`. See [agents/checklist-agent.md](../agents/checklist-agent.md). |
