---
name: sl-svg-diagram
description: Create animated SVG walkthroughs for Markdown that show how inputs and conditions activate different execution paths, API calls, and method chains.
argument-hint: "[Markdown path] [flow or scenarios to explain]"
user-invocable: true
---

# Animated SVG walkthrough

Create an animated explanation, not a static diagram with decorative motion. Use the audited local animdiagram dependency through this skill's wrapper. This skill can be selected for a relevant documentation task or invoked explicitly.

## Invocation and integrity

Resolve this installed skill's directory from its location, never from the project working directory. In the commands below, `<skill>` means that absolute directory.

Invoke tools only through `python3 -I <skill>/scripts/run-animdiagram.py`. Each tool invocation checks the exact audited commit and SHA-256 manifest, then executes a temporary snapshot of the verified bytes. Successful integrity checks are silent; do not add a separate verification call or narrate checks during ordinary work.

If integrity fails, stop. Report the short failure and direct the user to the README installation instructions. Never bypass the wrapper, update the pinned commit or manifest, automatically repair the dependency, or run a direct upstream script. Setup downloads only when the user requests installation.

## Workflow and references

1. Establish the target document and grounded behavior from the task and relevant sources. Label hypothetical or planned behavior. Never invent calls, branches, concurrency, or measured timings.
2. Read [diagram rules](references/diagram-rules.md) and, if it exists, `~/.claude/sl-svg-diagram/preferences.md`. Missing personal preferences mean use shipped defaults. Apply task directions before personal preferences before defaults; correctness, integrity, and privacy remain mandatory. Explain any required preference that cannot be met.
3. Choose a supported `flow`, `branch`, or independent `grid` preset and author compact semantic JSON using [generation](references/generation.md). Resolve applicable preferences into typed saved settings and run `build` through the wrapper. Use the manual template/timeline route in [authoring](references/authoring.md) for unsupported layouts or unusual motion. Load only the references needed for the chosen route.
4. Keep SVG self-contained and script-free. Build and check through the wrapper. Render only in an environment with enforced outbound network denial covering the browser and subprocesses. The checker is structural, not a visual or security pass. If safe rendering is unavailable, report visual verification as pending. Do not install a browser or alter network policy automatically.
5. Retain the animated `.svg`, editable `.spec.json`, and concise `.agent.md` together. Update their meaning consistently; embed a relative Markdown image and companion link, URL-encoding spaces. Follow the detailed placement and verification procedure in authoring.
6. Fix corrections in the current diagram. Save reusable preferences only when the user asks to remember them or accepts a proposed rule; see the rules reference. For optional scenario-selecting HTML use `build --preview` and [preview verification](references/preview.md); preserve the standalone animated SVG. Report artifact links, scenario meaning, and verification status.

For understanding an existing diagram, use [reading diagrams](references/reading-diagrams.md); it does not require the authoring workflow. Never upload diagrams, source, or specs to another service. The approved enterprise Claude connection is separate. Do not use the upstream gallery, automatic browser launch, or video export. No automatic commits, pushes, publishing, or project `CLAUDE.md` changes.
