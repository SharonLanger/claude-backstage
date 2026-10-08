# Play Rules — {{play-title}}

## Rules

- **Authority:** Director > model rules > agent instructions. An explicit Director override applies only within its stated scope.
- **Delegation:** Stage Manager calls Leads; Leads call Cast. Cast do not call other Cast. Stage Manager calls Checklist Agent (exception to Lead-only delegation).
- **Locked locations:** `play.md`, `management/`, Act definitions, role files, `reference/`, `props/` — all static during execution, including retries.
- **Write permissions:** Act actors write own `stage/` and `handoffs/<act>/`. Stage Manager writes `progress.md` only. Checklist Agent writes own new report in `verifications/<act>/`.
- **Read permissions:** All actors read all `handoffs/` and `verifications/`. Act actors read `reference/`, own `props/`, own `stage/`. Stage Manager reads Play, progress, all handoffs, all verifications.
<!-- Play author decision: Should Leads read progress.md directly? If yes, add "Leads read progress.md." above. If no, the SM provides relevant context via assignment prompts. -->
- **Gates:** Mandatory hard stop. Present evidence, wait for Director. Record decision. Skip = Skipped (not Done).
- **Recovery:** Two retries per Act per Run. Resume same Lead. Forward-only. Ask Director when unclear or exhausted.
- **Truthfulness:** Mandatory for all agents. No invented evidence, false passes, or hidden failures. Pause and report conflicts.

## Folder map

```
play/
├── play.md                          [static]
├── progress.md                      [writable by: Stage Manager]
├── management/                      [static]
├── reference/                       [static, read: all]
├── verifications/<act>/             [writable by: Checklist Agent (new reports only)]
├── handoffs/<act>/                  [writable by: that Act's actors]
└── acts/<act>/
    ├── act-NN-slug.md               [static]
    ├── lead-slug.md                 [static]
    ├── cast-slug.md                 [static]
    ├── props/                       [static]
    └── stage/                       [writable by: that Act's actors]
```

## Runtime defaults

- model: {{model-choice or "(unspecified — implementation choice)"}}
- effort: {{effort-level or "(unspecified — implementation choice)"}}

More-specific definitions may override these. Omitted settings are inherited.
