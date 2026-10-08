# Naming and Identity

Every participant in the Theater Model has a naming convention that doubles as its runtime identity. Names are how agents are addressed, resumed, and distinguished from each other during execution.

## Naming conventions

| Artifact | Pattern | Examples |
|----------|---------|----------|
| Lead file | `lead-<slug>.md` | `lead-schema-check.md`, `lead-api-design.md` |
| Cast file | `cast-<slug>.md` | `cast-test-writer.md`, `cast-lint-fixer.md` |
| Act folder | `act-NN-<slug>` | `act-01-planning`, `act-02-code-gen` |
| Gate | `gate-<slug>` | `gate-review`, `gate-deploy-approval` |
| Handoff folder | `handoffs/act-NN-<slug>/` | `handoffs/act-01-planning/` |
| Verification folder | `verifications/act-NN-<slug>/` | `verifications/act-01-planning/` |

**Slug rules:**

- 1 to 3 descriptive, hyphen-separated words for agent-generated slugs.
- Act folder slugs exclude the `act-NN-` prefix when counting words.
- Gate slugs follow the same max-3-word convention for agent-generated names. The Director (human Play author) may use longer slugs when clarity requires it.

**Invalid names:** Bare numbers (`act-01/`), generic filenames (`lead.md`, `cast.md`), and slugs without the required prefix all violate convention. Every Lead file is `lead-<slug>.md`, every Cast file is `cast-<slug>.md`, every Act folder is `act-NN-<slug>`.

Handoff and verification subfolders use the full Act folder name — `handoffs/act-01-planning/`, not `handoffs/planning/`.

## Instance identity and addressing

The naming convention provides stable identities for the Agent tool at runtime. The slug in a Lead or Cast filename is the agent's name.

When the Stage Manager needs to reach a Lead — whether for initial assignment or for retry after a failed checklist — it uses the name directly:

```
SendMessage(to: "lead-schema-check")
```

No special addressing syntax, no instance registry, no session IDs. The Agent tool's `to` field accepts the name, and the runtime resolves it. This was open question 2.1 — now resolved: the existing naming convention and Agent tool behavior are sufficient.

## Instance lifecycle by role

| Role | Initial context | On retry | Notes |
|------|----------------|----------|-------|
| Stage Manager | One instance per Run | N/A — not retried, escalates to Director | Persistent for the Run's lifetime |
| Lead | Fresh (not forked from SM) | Same instance resumes with retained context | SM sends corrective prompt via `SendMessage` |
| Cast | Fresh or forked — Lead decides | Lead decides (new instance or reuse) | Same definition can be instantiated multiple times |
| Checklist Agent | Always fresh | Always fresh | Never forked, never resumed; every invocation starts clean |

**Lead retry** is the critical case. When a checklist fails and the Stage Manager sends corrections, the same Lead instance continues — it has the context of what it already tried. The SM does not spawn a new Lead; it resumes the existing one with a short corrective prompt.

**Cast context** is the Lead's call. Fresh context is appropriate for independent subtasks. Forked context is appropriate when the Cast needs the Lead's accumulated knowledge. Unless governing instructions prescribe the choice, the Lead decides per invocation.

**Checklist Agent** is always fresh by design. Independence requires starting from scratch every time — no carried-forward state, no residual context from prior verification runs.

## Resume and fallback

If the original Lead instance cannot be resumed — context lost, session ended, runtime limit hit — the Agent tool spawns a fresh agent with the same name. This is standard Agent tool behavior, not Theater Model-specific logic.

The consequence: a fresh Lead on retry loses the context of prior attempts. The corrective prompt from the Stage Manager must be self-contained enough for the Lead to understand what failed and what to do differently. This is a degraded path, not the normal one.

This was open question 2.2 — now resolved: the Agent tool's existing behavior (resume if alive, spawn fresh if not) serves as the fallback. No separate recovery mechanism is needed.

---

**Cross-references:**

- [agents/stage-manager.md](../agents/stage-manager.md) — SM delegation and recovery mechanics
- [acts/roles.md](../acts/roles.md) — Lead/Cast context decisions and delegation chain
- [agents/checklist-agent.md](../agents/checklist-agent.md) — fresh-instance design rationale
- [open-questions.md](../../claude-analysis/open-questions/open-questions.md) — questions 2.1 and 2.2 (resolved), question 1.4 (Gate slug length, resolved)
