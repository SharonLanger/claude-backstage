# Reading a diagram

1. Read the surrounding Markdown and nearby explanation first.
2. Resolve the actual SVG image link relative to that Markdown document, decoding URL-encoded spaces. Asset directories may be named `diagrams`, `sl-diagrams`, or something else.
3. Read the matching `.agent.md` beside the resolved SVG: `flow.svg` has companion `flow.agent.md`.
4. Read SVG source when editing, debugging, or resolving information missing from the prose and companion. If the companion is absent, say so and inspect source only as needed.

This is reading guidance, not an access restriction. It does not require loading the authoring skill.
