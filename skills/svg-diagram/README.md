# SVG diagram

A Claude Code skill for creating editable SVG diagrams and embedding them in Markdown. Use it for README overviews, API exchanges, processing flows, architecture, and state transitions.

## Install

From the root of your `claude-backstage` checkout, copy the skill into your personal Claude Code skills directory:

```sh
mkdir -p ~/.claude/skills
cp -R skills/svg-diagram ~/.claude/skills/
```

For a project-scoped installation, copy the `svg-diagram` directory into that project's `.claude/skills/` directory instead. Preserve any existing customized installation rather than overwriting it blindly.

The catalog's `skills/` directory stores the distributable source. Claude Code discovers the installed `SKILL.md` under its personal or project skills directory; this repository is not itself a plugin installer.

## Invoke

```text
/svg-diagram README.md Explain how the main components fit together
/svg-diagram docs/design.md Show the request flow, including rejection
/svg-diagram docs/api/auth.md Show token refresh across client, API, and identity provider
```

You can also ask naturally: “Add an SVG diagram explaining this flow to the design document.” The skill description allows Claude to select it automatically when relevant; automatic selection is model-dependent. User invocation remains available. A calling agent must have this skill available in its Claude Code context.

If the document is already established, omit its path. If the destination is ambiguous, the skill asks where to save the result.

## Output placement

The default is a `diagrams/` folder beside the target Markdown file:

```text
docs/
  design.md
  api.md
  diagrams/
    design-request-flow.svg
    design-error-handling.svg
    api-authentication.svg
```

From `docs/design.md`, the image link is:

```markdown
![Request validation and execution](diagrams/design-request-flow.svg)
```

For a root README, this naturally becomes a root `diagrams/` directory. Nested documents keep their assets nearby. Multiple documents can share the adjacent folder without filename collisions because each filename includes its document stem.

An explicit destination or an existing repository convention takes precedence. A common asset directory is useful for genuinely shared diagrams, but is not created automatically. The shell's working directory resolves the input Markdown path; the Markdown file's directory resolves its image links. The installed skill directory is never the default destination.

## What the skill does

It reads the relevant source or specification, chooses a diagram form, writes self-contained SVG, updates the Markdown reference, and verifies both the file and its rendering. Existing diagrams are updated in place. No specialized diagram service is required; visual verification needs a browser or SVG renderer available to Claude.

The skill reports whether visual inspection was completed. It does not automatically commit, publish, install tools, or change Claude Code settings.

## Agent context cost and first-version guidance

Reading Markdown as text normally loads the image reference, not the linked SVG source. However, a fresh agent may follow that reference to understand the diagram. If diagrams are used extensively, those extra reads can consume substantial context with coordinates, styling, and paths rather than useful semantics. Instructions inside this skill alone cannot guide an agent that has not loaded it.

For the first version, document the convention in the consuming project's `CLAUDE.md`. For example:

> Understand diagrams from their surrounding Markdown first. If more detail is needed, read the linked companion with the same basename and the suffix `.agent.md`, when available. Read SVG source only when creating, editing, or debugging the visual. If no companion exists and the prose is insufficient, report the missing explanation rather than routinely loading SVG source.

A companion such as `diagrams/design-request-flow.agent.md` should describe participants, calls, ordering, conditions, and outcomes concisely, without coordinates or styling. Link it from the main document so readers can discover it. Keep its semantics synchronized with the SVG. This README records the proposed convention; the current skill does not yet require or automatically guarantee companion creation. Adding this guidance to a consuming project's `CLAUDE.md` is a separate project change.

### Ballpark risk

These are illustrative planning ranges for text-based technical diagrams, not measurements or limits:

| Diagram | SVG source size | Concise Markdown semantics |
| --- | --- | --- |
| Simple flow | 1–5 KB | 0.2–1 KB |
| Detailed flow or call hierarchy | 10–100+ KB | 1–5 KB |

Raw SVG can therefore consume several times to tens of times more context than a semantic explanation. SVG exported with verbose metadata, text converted to paths, or embedded images can reach hundreds of KB or MB. Actual token cost depends on the tokenizer, markup, numeric paths, and tool truncation; byte ratios are not token ratios. These estimates concern reading SVG as text, not image-processing token costs.

The practical risk is low when an agent reads only the Markdown reference, and rises with the number and size of SVG sources it opens. A short diagram description is useful even where tool limits prevent loading the full SVG.

### Possible later enforcement

A future deterministic hook in System One Harness could intercept SVG reads, check for the matching `.agent.md`, and redirect the agent with a short message. It would need an explicit exception for visual editing, a fallback when the companion is missing, and verification against Claude Code's hook contract. Blocking the Read tool alone would not cover shell commands or other file-reading tools.

No interception hook or read restriction is implemented by this skill. `CLAUDE.md` guidance is advisory and does not guarantee that every agent will avoid SVG reads.

## Manual acceptance checks

In a disposable project, exercise these cases with Claude Code:

- Invoke from the project root for `docs/design.md`: expect `docs/diagrams/design-<topic>.svg` and a working relative embed.
- Invoke from inside `docs/` for `design.md`: expect the same location.
- Request two diagrams for one document and one for a second document: expect distinct filenames in the same adjacent folder.
- Update an existing diagram: expect its filename and single Markdown reference to remain stable.
- Use a document beneath a directory containing spaces: expect a valid, portable image URL.
- Provide an existing asset convention or explicit SVG destination: expect it to take precedence.
- Ask to show a diagram without an established document or destination: expect a short destination question.
- Inspect the result at desktop and narrow widths: expect readable labels, clear branches, and no clipping.

These are acceptance scenarios, not a claim that a live Claude Code run has passed them.

[Skill instructions](SKILL.md) · [All skills](../README.md)
