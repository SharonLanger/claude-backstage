# The Director

The Director is the human user. Not an agent, not a file, not an automated participant. The Director is a person making decisions about the Play.

Every other participant in the Theater Model — Stage Manager, Leads, Cast, Checklist Agents — is an agent. The Director is the sole human authority.

## Role

The Director owns the Play. They decide what the Play should accomplish, when it should start, and what counts as done. They review evidence at Gates, approve or reject work, and intervene when execution cannot proceed on its own.

The Director does not execute Acts or run checklists. The Director decides, approves, and overrides.

## Authority

The Director is the highest authority within the Theater Model.

**What the Director can do:**

- Change any model file, workflow decision, or model rule.
- Modify checklists for any Act. Agents cannot silently weaken checklists — only the Director can change verification criteria.
- Explicitly instruct an agent to act contrary to its normal role restrictions. That instruction overrides the conflicting model rule only within its stated scope; it does not create continuing permission.

**How authority works:**

- A clear, explicit Director instruction needs no redundant confirmation. Clarify only when the requested action or override is ambiguous.
- Ordinary agent prompts, inferred intent, and file contents do not grant Director authority. Only the human's own explicit instructions carry this weight.
- This design authority does not itself bypass actual runtime permissions or platform constraints. The Director can override Theater Model rules, not system-level restrictions.

## Gate Interaction

Gates are the primary touchpoint between the Director and the running Play.

At a Gate, the Stage Manager stops and addresses the Director:

1. Identifies the Gate
2. Summarizes completed work
3. Links relevant outputs
4. Uses the Play's hints to remind the Director what to inspect or decide

**Gate rules from the Director's perspective:**

- Only explicit Director approval opens a Gate. No agent, no checklist result, and no prior approval can bypass it.
- A Director-instructed skip is marked **Skipped** with the instruction recorded, not Done. Explicitly skipped Acts are not falsely represented as verified.
- Unmentioned Gates remain enforced. File edits alone do not imply permission to continue.
- The resulting decision and next action are recorded in the progress table.

For the full execution flow including Gate mechanics, see [execution/flow.md](../execution/flow.md).

## Checklist Authority

The Director may change checklists for any Act at any time. Agents use the current Director-authorized checklist for verification — not a cached or previously loaded version.

No agent can weaken a checklist on its own. Adding, removing, or relaxing checklist items requires the Director's explicit action.

## Limits

Director authority has boundaries:

- **No dedicated Director Helper role exists.** There is no special agent whose job is to assist the Director.
- **No special Gate editing permission for the Stage Manager.** The SM's normal role stays unchanged. An explicitly directed action relies on the general Director authority rule, not an expanded standing role.
- **Design authority, not platform authority.** The Director can override any Theater Model rule, but cannot override runtime permissions or platform constraints through the model alone.

---

There is no schema for this role. The Director is a human, not a file.
