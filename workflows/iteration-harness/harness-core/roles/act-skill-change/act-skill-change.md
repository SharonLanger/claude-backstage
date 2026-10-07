# Act: act-skill-change

Every actor in this act MUST load this file first.

---

## Purpose

Apply changes to the skill under development. This is the ONLY act that has write access to `~/.claude/skills/example-skill/`.

---

## Shared Rules (all actors in this act)

1. You are NOT allowed to modify test files (`blueprint.md`, `asserts.md`, `input/`). Tests are locked after the Director approves them.
2. You MUST create a backup BEFORE every change to the skill.
3. Never pass task details in sub-agent prompts — point actors to their role file.
4. All actors: Model = opus, Effort = high.
5. You do NOT decide what to fix — you receive fix instructions and implement them.

---

## Actors

| Role | Actor | File | Spawned By |
|------|-------|------|-----------|
| Lead | Skill-Change-Agent | `skill-change.md` | Main Agent |
| Cast | Backup Agent | `backup.md` | Skill-Change-Agent |

---

## Flow

```text
Skill-Change-Agent (Lead)
  ├── reads fix instructions from skill/ folder
  ├── spawns Backup Agent → snapshots current skill
  └── applies changes to ~/.claude/skills/example-skill/
```

---

## Inputs

| Input | Source |
|-------|--------|
| Fix instructions | `harness-core/skill/<milestone>-round-<N>/fix-NN-*.md` |
| Skill source | `~/.claude/skills/example-skill/` |
| Version history | `~/.claude/skills/example-skill/backups/version-log.md` |

---

## Outputs

| Output | Location |
|--------|----------|
| Modified skill files | `~/.claude/skills/example-skill/` |
| Version backup | `~/.claude/skills/example-skill/backups/V<N>/` |
| Version log entry | `~/.claude/skills/example-skill/backups/version-log.md` |

---

## Boundaries

- This act modifies. It does NOT evaluate whether changes are good.
- After this act completes, `act-test-runner` validates the result.
- If a fix instruction is ambiguous or contradicts the skill's architecture, STOP and escalate to the Director (via the Reasoner's decision file).
