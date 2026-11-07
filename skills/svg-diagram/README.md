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
