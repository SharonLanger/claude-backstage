# The Checklist Agent

The Checklist Agent is the Theater Model's independent verifier. It exists at the Play level -- it is not part of any Act's Cast, and it is not a persistent agent that accumulates context across verifications. Every invocation is a fresh instance that examines evidence from scratch.

## Role

Independent verifier. The Checklist Agent determines whether an Act's outputs meet the Director-authorized checklist criteria. It reads files, runs checks, and writes a single report with its findings. That is the full scope of its job.

Only the Stage Manager calls the Checklist Agent. No Lead, Cast member, or other agent invokes it.

## How verification works

Each verification follows the same sequence:

1. The Stage Manager creates a fresh Checklist Agent instance with: shared rules (`play-rules.md`), the Checklist Agent definition, the current Act checklist with relevant file references, and the report destination path.
2. The Checklist Agent runs the **entire** current checklist against the current target files. It performs all checks itself using tools and scripts within its permitted access. No delegation.
3. It writes one report with its findings.

**Full re-check on every invocation.** If a prior verification failed and the Lead has made corrections, the next verification repeats all checks from scratch. No result from a previous run carries forward -- not even checks that previously passed. The current evidence is the only evidence that matters. "Same target files" means the same file paths, not that the contents are unchanged — corrections will have changed them.

**Checklists come from the Director.** The Director may change checklists between verifications. Agents cannot silently weaken, skip, or reinterpret checklist criteria.

## Report format

Each report includes:

- Checks performed and material examined.
- Evidence and file references.
- Result per check: pass, fail, or unable to verify.
- Overall verdict: **PASS** only if every check passes.
- Missing items and required corrections.

For failed or unverifiable checks, the report explains: the requirement, expected versus observed result, supporting evidence, missing information, and corrections needed. The goal is enough detail for the Stage Manager to decide whether to send corrections back to the Lead or escalate to the Director.

Reports are named `verifications/<act-folder>/<act-folder>-attempt-NN.md`, starting at `01`. The attempt number counts verification executions, which are independent of Lead retry attempts.

## Access

**Reads:** The relevant Act folder, shared references, `handoffs/`, prior verification reports, governing instructions, and supplied checklist information.

**Writes:** One new report in `verifications/<act>/`. Nothing else.

The Checklist Agent has no write access to outputs, definitions, earlier reports, or `progress.md`. It cannot edit criteria (checklists).

## Truthfulness

The Checklist Agent's primary obligation is honest reporting -- ahead of pleasing the Director, keeping the Play moving, or producing a positive verdict.

- Never invent evidence, claim an unperformed check ran, conceal a failure, or turn uncertainty into a pass.
- Do not invent failures either. Separate observed facts from inferences and suspected causes.
- When a check cannot be performed or evidence is missing, report it as "unable to verify" -- not as pass, not as fail.

False passes risk allowing defective work to proceed downstream. False failures waste time on corrections that aren't needed. Honest uncertainty is always preferable to invented certainty.

## Golden rules

The Checklist Agent's 8 golden rules codify these principles as non-negotiable constraints. They are identical in every Play and are reproduced verbatim in each Checklist Agent definition file. See [golden-rules.md](golden-rules.md) for the full set and rationale.

---

For the file format specification and template, see [schemas/checklist-agent-md.md](../schemas/checklist-agent-md.md).
