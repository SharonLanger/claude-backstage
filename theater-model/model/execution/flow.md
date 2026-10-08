# Execution Flow

The sequence the Stage Manager follows when running a Play.

## Sequence

```
Setup (Director)
  │
  ▼
Stage Manager reads play.md, play-rules.md
  │
  ▼
Initialize progress.md
  │
  ▼
┌─── For each Act in order ───┐
│                              │
│  1. Call the Lead            │
│  2. Lead does work           │
│     (delegates to Cast       │
│      if the Act has any)     │
│  3. Act agents publish to     │
│     handoffs/<act>/          │
│  4. Call Checklist Agent     │
│     (fresh instance)         │
│  5. Checklist Agent writes   │
│     report to                │
│     verifications/<act>/     │
│                              │
│  If FAIL → recovery/retry    │
│  If PASS → mark Done         │
│                              │
│  If Gate follows → stop,     │
│     present evidence,        │
│     wait for Director        │
│                              │
└──────────────────────────────┘
  │
  ▼
All Acts Done + all Gates Open
  │
  ▼
Play Completed
```

## Progress updates

The Stage Manager updates `progress.md`:
- **Before** invoking each Act.
- **After** results, verification, and Director decisions.
- **On resume** from interruption — inspect recorded progress, continue from last confirmed state.

Recording dispatch is not proof that the invocation completed. An interruption alone is not a failure and does not consume a retry.

## Forward-only execution

Acts execute sequentially, in order. The Stage Manager cannot go back to a previous Act. If an earlier Act's output is discovered to be wrong, the Stage Manager stops and asks the Director.
