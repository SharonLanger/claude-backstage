# Diagram rules

Read these defaults and applicable personal preferences when planning a diagram. Task-specific directions override personal preferences, which override shipped defaults. Factual correctness, integrity verification, and privacy remain mandatory. Strength is **default**, **required**, or **avoid**; explain an unsatisfied required preference.

| Rule ID | Condition | Behavior | Strength |
|---|---|---|---|
| `layout.independent-grid` | More than five independent peer items | Use a grid, initially up to three columns. | default |
| `layout.ordered-flow` | Steps have execution order | Preserve clear order through placement and arrows; item count alone must not choose a grid. | default |
| `layout.side-explanation` | A legend, tag key, or explanatory grid supports the flow | Reserve a dedicated side panel, preferably right. | default |
| `layout.outer-padding` | Every diagram | Reserve clearance around visible content, including bottom labels and moving tags. | default |
| `text.readability` | Labels do not fit | Wrap or rearrange before reducing type size. | default |
| `animation.scenario-pause` | Scenario transitions | Include a readable outcome pause and reset. | default |
| `style.avoid` | Every diagram | Avoid cramped edges, overlapping tags, decorative motion, and moving nodes between scenarios. | avoid |

These are qualitative authoring rules. [Versioned defaults](../defaults/v1.json) are the numeric authority; translate applicable preferences into typed `settings` in the saved [semantic spec](generation.md). The runtime never interprets prose.

## Saved preferences

Personal preferences live at `~/.claude/sl-svg-diagram/preferences.md`, outside the installed skill bundle. If absent, use defaults. Setup must not create, populate, or overwrite this file. Reinstalling the skill preserves it. The skill **adapts to your saved preferences**; persistence is explicit.

Fix the current diagram when corrected. If feedback appears reusable, propose a concise rule and scope. Save only when the user explicitly asks to remember it or accepts that proposal. Do not ask after every successful diagram. Keep one-time exceptions in that diagram's spec (for the manual route, record qualitative exceptions in its companion when the motion schema has no suitable field).

For example, “Make these labels larger” changes this diagram only. “Remember to use larger labels in my diagrams” authorizes a personal rule. Use stable IDs with condition, behavior, and strength, for example:

```markdown
| Rule ID | Condition | Behavior | Strength |
|---|---|---|---|
| text.readability | My diagrams | Prefer larger labels; wrap or rearrange to fit. | default |
```

Update an existing ID instead of accumulating contradictory entries. Resolve conflicting instructions with the user. Never modify dependency code or its manifest for a preference. During generation, translate applicable prose into saved typed overrides; the runtime must not interpret arbitrary Markdown or call another model.
