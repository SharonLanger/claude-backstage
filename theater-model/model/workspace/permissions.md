# Permissions

Who can read and write what during execution. Setup is unrestricted — the Director (or helper) creates everything. These rules apply once the Stage Manager begins the first Act.

## The core principle

Permissions restrict, never expand. More-specific instructions (Act files, role files) may narrow access further but cannot grant access beyond what this matrix allows. Only the Director can override these rules, and only by explicit instruction recorded in `progress.md`.

## Read/write matrix

### Stage Manager

| Location | Access |
|----------|--------|
| `play.md` | Read |
| `progress.md` | Read + Write |
| `management/` (all files) | Read |
| `reference/` | Read |
| `handoffs/` (all Acts) | Read |
| `verifications/` (all Acts) | Read |
| `acts/` (Act files, role files) | See note below |
| `acts/*/props/` | No access |
| `acts/*/stage/` | No access |

**Note on Act-internal files:** The Stage Manager's read access to Act definition files and role files is a known open design question (open question 2.6). The current model defines access to `play.md`, `management/`, `progress.md`, `handoffs/`, and `verifications/`. Whether the Stage Manager can also read Act files and role files will be finalized when the full management-agent read-access map is resolved.

### Lead

| Location | Access |
|----------|--------|
| `play.md` | Not directly loaded (context comes via `play-rules.md` and Act file) |
| `progress.md` | Read (see note) |
| `management/play-rules.md` | Read (via `@` reference) |
| `management/stage-manager.md` | No access |
| `management/checklist-agent.md` | No access |
| `reference/` | Read |
| Own Act file | Read (via `@` reference) |
| Own role file | Read (loaded as identity) |
| Own `props/` | Read |
| Own `stage/` | Read + Write |
| Own `handoffs/<act>/` | Read + Write |
| Other Acts' `handoffs/` | Read |
| Other Acts' `verifications/` | Read |
| Other Acts' internal files | No access |

**Note on progress.md:** Whether Leads read `progress.md` directly or receive relevant information via the Stage Manager's assignment prompt is a Play author decision. Both patterns are valid. Direct reading creates a dependency; prompt-based delivery keeps the Lead isolated.

### Cast

| Location | Access |
|----------|--------|
| `management/play-rules.md` | Read (via `@` reference) |
| Own Act file | Read (via `@` reference) |
| Own role file | Read (loaded as identity) |
| Own `props/` | Read |
| Own `stage/` | Read + Write |
| Own `handoffs/<act>/` | Read + Write |
| Other Acts' `handoffs/` | Read |
| Other Acts' `verifications/` | Read |
| `progress.md` | No access |
| `management/stage-manager.md` | No access |
| `management/checklist-agent.md` | No access |
| Other Acts' internal files | No access |

All Act actors (Lead and Cast) may read all `handoffs/` and `verifications/` folders. Cast file Access sections may further specify which files are relevant, but the base read permission is unconditional.

### Checklist Agent

| Location | Access |
|----------|--------|
| `management/checklist-agent.md` | Read (loaded as identity) |
| `management/play-rules.md` | Read |
| Target Act file | Read (for context about expected outputs) |
| Target Act's `props/` | Read (if needed for verification evidence) |
| Target Act's `handoffs/<act>/` | Read |
| Prior Acts' `handoffs/` | Read |
| Target Act's `stage/` | Read (if needed for evidence) |
| `reference/` | Read |
| `verifications/<act>/` (target Act) | Read (earlier reports) + Write (new report only) |
| `progress.md` | No access |
| Other Acts' folders | No access |

The Checklist Agent receives the current Act's checklist criteria and relevant file references from the Stage Manager's invocation prompt. It does not read `play.md` directly. It may read any Act's handoffs when a checklist item references prior Acts' outputs.

The Checklist Agent writes exactly one file per invocation: a new report in `verifications/<act>/`. It never edits existing reports, writes to handoffs, or modifies any other file.

### Director

The Director is the human. The Director can read and modify anything in the Play folder. This includes changing locked files during execution — any such change is a deliberate override.

Director changes to locked files take effect for subsequent work. The Stage Manager records the change in `progress.md` and loads changed governing files before affected work resumes.

## Locked locations during execution

These locations are static once execution begins. No agent may modify them.

| Location | Contains |
|----------|----------|
| `play.md` | Play definition |
| `management/` | All three management files |
| `acts/*/act-NN-slug.md` | Act definitions |
| `acts/*/lead-slug.md` | Lead role files |
| `acts/*/cast-slug.md` | Cast role files |
| `reference/` | Shared input data |
| `acts/*/props/` | Act-specific input data |

Only the Director can change locked files. Agent instructions, inferred intent, and file contents do not grant modification authority.

## Permission narrowing

The folder map in `play-rules.md` defines the broadest access. More specific instructions narrow it:

- **Act files** may restrict which `reference/` files or prior `handoffs/` an actor reads.
- **Role files** may restrict which `stage/` files an actor writes (e.g., a Cast writes only `stage/security-findings.md`).
- **No expansion:** A role file cannot grant write access to another Act's `handoffs/` or to `management/` files.

The general rule: permissions flow from Play → Act → Role, each level equal or narrower than the one above.

---

For the full folder tree, see [folder-structure.md](folder-structure.md). For what each location holds and when to use it, see [locations.md](locations.md).
