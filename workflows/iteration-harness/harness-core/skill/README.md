# Fix Instructions

Fix instruction files are written here by the **Reasoner** agent and read by the **Skill-Change-Agent**.

Each fix instruction file contains:
- What to change (specific files and sections)
- Why (root cause from the decision document)
- How (precise description of the fix)
- What NOT to change (boundaries to prevent scope creep)

The Skill-Change-Agent reads these instructions and applies them to the skill files.

---

## Mock Examples

The `-mock` files in this folder demonstrate the format and content of real fix instructions. They are templates only — replace them with actual fix instructions from your iteration runs.

- `fix-01-restore-execution-loop-mock.md` — Fix instruction showing problem, root cause, suggested change, and acceptance criteria
