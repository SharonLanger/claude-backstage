---
name: svg-diagram
description: Create or update editable SVG diagrams embedded in Markdown documentation. Use when the user asks for a diagram, or when explaining a flow, API interaction, architecture, decision, or state transition in a README or design document would benefit from a visual.
argument-hint: "[Markdown path] [what to explain]"
user-invocable: true
---

# SVG diagram

Turn the behavior being explained into a readable SVG and embed it in the relevant Markdown document. Work in the caller's project. The installed skill directory contains instructions; it is never the default output directory.

## Establish the target

- Treat `$ARGUMENTS`, when supplied, as the requested Markdown path and diagram brief. Otherwise use the document and topic already established in the conversation.
- Read applicable repository instructions, the target document, nearby image conventions, and the source or specification needed to understand the behavior.
- Resolve a relative document path against the caller's working directory once, then use the resolved document directory for asset placement and image links. Do not assume that the working directory is the repository root.
- If the document is being created as part of the current task, use its agreed destination. If neither a target document nor an output destination can be inferred, ask one short question before writing files.
- For a request to show a standalone diagram, honor an explicit SVG output path. If none is given and no document is in scope, ask where to save it; do not create an arbitrary README.
- Automatic invocation fits an existing documentation or explanation task. It does not authorize unrelated document rewrites, commits, pushes, or publishing.

## Choose where the SVG belongs

Apply these rules in order:

1. Honor the user's explicit destination.
2. Follow an established image/diagram convention used by the target document or its documentation area.
3. Otherwise create a `diagrams/` directory immediately beside the Markdown file.

Default filenames are `<document-stem>-<topic>.svg`, using descriptive lowercase kebab-case names. For a README, use `readme` as the stem. Keep existing filenames when updating a diagram.

| Markdown document | Default SVG | Link from that document |
| --- | --- | --- |
| `README.md` | `diagrams/readme-overview.svg` | `diagrams/readme-overview.svg` |
| `docs/design.md` | `docs/diagrams/design-request-flow.svg` | `diagrams/design-request-flow.svg` |
| `docs/api/auth.md` | `docs/api/diagrams/auth-token-refresh.svg` | `diagrams/auth-token-refresh.svg` |

Multiple diagrams for one document use distinct topic names in the same directory. Multiple documents in the same directory share that `diagrams/` folder, with document prefixes preventing collisions. Do not silently overwrite an unrelated asset; choose a more specific name.

Do not create a repository-root asset folder merely because several diagrams are needed. A diagram genuinely shared across documentation areas may use an existing shared asset location or a user-selected destination. Compute each document's link relative to that document, including `../` when needed.

## Explain the behavior before drawing

Identify the reader's question and the one main point the diagram should communicate. Trace the relevant components, ordering, inputs, outputs, decisions, and meaningful failure or no-op branches. Use source identifiers where useful, but keep labels short.

Choose the form that fits:

- Flowchart: ordered processing with decisions and alternate outcomes.
- Sequence diagram: requests and responses across participants over time.
- Component diagram: ownership, dependencies, and system boundaries.
- State diagram: states and the events that cause transitions.

Distinguish current implementation from proposed behavior in the caption or labels. Do not invent endpoints, branches, guarantees, or timings. If an unknown affects the explanation, resolve it or explicitly label the uncertainty.

Split a crowded diagram into an overview and focused detail. Keep surrounding prose for qualifications and implementation details.

## Author an editable SVG

Write SVG as text using ordinary vector shapes, paths, arrows, and text. Use an existing project renderer if appropriate, retaining its editable source and reproducible command. Never rely on a generated bitmap for technical labels.

- Include the SVG namespace, a correctly sized `viewBox`, a descriptive `<title>`, and a `<desc>` describing the main flow.
- Use standard system fonts, explicit text colors, and a neutral background that remains legible when embedded on light and dark pages. Follow an existing theme convention when present.
- Use a small consistent palette. Labels and line styles must carry meaning without relying on color alone.
- Keep text readable at normal document width. Wrap long labels with `<tspan>`; grow boxes to fit text instead of shrinking it excessively.
- Align nodes, leave generous padding, and route connectors away from labels. Put arrowheads at the destination and label decision branches.
- Prefer a compact vertical layout when a wide sequence would become unreadable on a narrow screen.
- Use self-contained SVG: no scripts, event handlers, external fonts or images, or `foreignObject`. Escape XML special characters and use unique IDs for markers and other definitions.
- Keep the SVG text maintainable. If generated from another source file, edit that source and regenerate rather than allowing the files to diverge.

## Embed and show

Place the image near the explanation it supports, outside code fences:

```markdown
![Request passes through validation, execution, and response formatting](diagrams/design-request-flow.svg)
```

Use informative alt text and a short caption or adjacent paragraph when needed. Use forward slashes and a document-relative URL; percent-encode spaces in the URL. Do not embed an absolute local path or a raw `<svg>` block in GitHub Markdown.

Preserve unrelated document content. When replacing an existing diagram, update its existing reference rather than adding duplicate images. Reuse the existing asset when the request is an update.

In the final response, link to the Markdown document and SVG and summarize what the diagram explains. Show a rendered preview if the interface supports it. A terminal may display only links; do not claim it displayed an image when it did not.

## Verify before finishing

1. Parse the SVG as XML; check the namespace, viewBox, title/description, and local definition references.
2. Resolve the image URL from the Markdown file's parent directory and confirm it points to the intended SVG. Check any retained renderer source and referenced local files exist.
3. Render the SVG with an available browser or SVG renderer and inspect it at normal document width and a narrow viewport. Fix clipped text, overlapping boxes, ambiguous arrows, tiny labels, and poor contrast. Use temporary storage for preview PNGs unless the user needs them.
4. Compare labels, branch outcomes, and direction of flow with the source or specification. Verify that proposed behavior is labeled.
5. Review the diff for accidental edits and report what was actually checked.

If rendering is unavailable, complete structural and path checks and explicitly report that visual verification remains unperformed. Do not present XML validity as proof of visual correctness.
