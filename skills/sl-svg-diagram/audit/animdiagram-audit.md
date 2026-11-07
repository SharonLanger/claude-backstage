# animdiagram local-processing audit — 2026-11-07

## Decision
Reuse the pinned core compiler and templates. Do not describe the entire
unmodified repository as guaranteed offline. The gallery loads Google Fonts;
browser preview/export need enforced egress restrictions for a strict policy.
No intentional project-upload or telemetry implementation was found in the
reviewed project source. This is a bounded source review and test result,
not a guarantee about arbitrary inputs, future updates, browsers, or dependencies.

## Identity and provenance
Repository: https://github.com/praveenvijayan/animdiagram
Commit: a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486
Git tree: b89feab729bede798158f518e67b47e4935fa2f3
Plugin metadata version: 1.1.0; SKILL.md metadata version: 1.1.
GitHub releases API returned no releases. The clone contains tag v1.0.0,
which resolves to ad1af85ec039c984691a51f8d6971d9a10e6df2a (not this audit).
Use the full audited commit, not a claim that a v1.1.0 release tag was verified.
License: MIT, copyright 2026 Praveen Vijayan. Retain notice on redistribution.
At the audit stage, the upstream checkout remained unmodified and no skill was installed. The later wrapper integration is described separately below.

## Scope
Inventoried all 62 tracked files (599,550 bytes), with SHA-256 for every file.
Read executable Python, embedded browser JavaScript, skill/reference instructions,
installation metadata, license, and documentation. Parsed all JSON and SVG;
inspected PNG chunk structure (three raster branding assets, no text metadata).
Reviewed seven Python files, 26 SVG files, 11 animation specifications,
HTML gallery/template, and local templates. The generated gallery was rebuilt
byte-for-byte from its reviewed template, JSON, specs, and builder.
No private project data was used: only public examples and synthetic fixtures.
The permitted enterprise AI connection is outside the third-party-tool boundary.

## Component findings
1. scripts/timeline.py
   Python standard library. Reads explicit JSON and SVG paths; writes the chosen
   SVG; prints the schedule. No network client, upload, telemetry, automatic
   update, project scanning, shell execution, or dependency installation found.
   Some spec values are directly interpolated into CSS/XML. This is an authoring
   compiler for trusted inputs, not an untrusted-input sanitizer.

2. scripts/check.py
   Local XML and style checks, standard library only. Blocks obvious scripts,
   external hrefs, event handlers, and lower-case @import/url() in style blocks.
   Does not establish that an SVG is safe to render with network access.
   Confirmed four external-capable fixtures pass with no errors or warnings:
   inline CSS url(), a presentation-attribute url(), uppercase @IMPORT, and an
   xml-stylesheet processing instruction. Three produced HTTP request attempts
   when inlined by preview; all requests were intercepted and aborted.
   The processing-instruction fixture did not request anything when inlined in
   HTML; standalone XML processing-instruction behavior was not tested.

3. scripts/skin.py
   Local regex-based theme conversion, standard library only. It preserves
   unrecognized input rather than sanitizing it. No network behavior found.

4. scripts/preview.py
   Writes an HTML file containing the input SVG verbatim. Its own JavaScript
   only controls local playback, seeking, zoom and page background. No external
   script/font/image references in its template. --open delegates to the user's
   default browser. It does not invoke check.py or enforce a network policy.
   Untrusted SVG and filenames must not be assumed safe: SVG is inlined and
   the filename is inserted into HTML without escaping.

5. scripts/export.py
   Optional local Playwright/Chromium rendering, local screenshots piped into
   ffmpeg via argument-list subprocess calls (no shell=True). --doctor checks
   availability and prints install commands; it does not run an installer.
   Inlines the supplied SVG, launches Chromium, and has no outbound-request
   interception or sandbox policy of its own. Playwright, Chromium, ffmpeg,
   Python and OS internals were not source-audited or supply-chain-certified.

6. docs/build.py and gallery
   Builder is standard-library local file processing. Generated docs/index.html
   and docs/template.html lines 26–28 preload/connect to Google Fonts and load
   its CSS. Opening this gallery therefore violates a strict zero-third-party-
   network policy. A browser test recorded the Google Fonts stylesheet request.
   The gallery's JavaScript stores theme choice locally and copies the install
   command to the clipboard on click; no analytics/upload implementation found.
   Remote ordinary hyperlinks and social-preview metadata are also present;
   they are distinct from the active Google Fonts stylesheet load.

7. Installation and instruction surface
   Plugin JSON contains metadata and a local marketplace source; no bundled
   MCP service, hooks, postinstall program, package manifest, or updater found.
   README offers npx/marketplace installation; these installer ecosystems were
   not audited. Prefer the direct, pinned checkout. The skill links to other
   projects and suggests handoffs; this audit does not extend to those projects.
   It explicitly forbids automatic dependency installation for optional export.

8. Shipped SVG/assets
   All 26 SVGs were scanned for external references, active elements, CSS URLs,
   DTDs and stylesheet instructions; none were found. All 26 were rendered
   inline in Chromium; no page-level HTTP requests were observed.
   Font family names in the SVGs are local fallback stacks, not font downloads.

## Test evidence
Environment: Linux, Python 3.12.14, system Chromium 156.0.8078.79,
ffmpeg 7.1.5-0+deb13u1 with libx264, existing Python Playwright installation.
No additional dependencies installed.

- Upstream smoke suite: 8/8 passed, also under unshare -Urn with strace -f.
- All 11 specs regenerated their shipped SVGs byte-for-byte.
- All 11 regenerated examples passed check.py error checks. PKCE has one
  non-security warning: seven phase/show labels versus a budget of six.
- The two branding SVGs fail animation-format checks, as expected for assets
  outside the diagram contract; these are not external-resource findings.
- Command-line injection, strict validation of the async example, skin conversion,
  preview HTML creation, and gallery rebuilding passed in a network namespace
  with no external network interface. strace recorded no network syscalls for
  this combined core workflow (only child-process signal records).
- All 26 shipped SVGs rendered in Chromium with HTTP routing intercepted.
- Rate-limiter preview: visible phase at 2s was ALLOW; at 6s was REFUSE.
  No HTTP request attempts from that preview. Screenshots retained.
- Gallery produced a Google Fonts request attempt, aborted before transmission.
- Three validator-bypass fixtures produced request attempts to audit.invalid,
  aborted before transmission; no real service or private payload was used.
- MP4 export completed offline: 8-second example, desktop 1920x1080, 1fps,
  eight frames, 74KB output. A test harness supplied the installed system
  Chromium path to Playwright because the default downloaded Chromium binary
  was absent. This is not a test of default export installation readiness.
- Browser process network trace contains attempted external connections even
  with local documents; all were denied by the network namespace. Page-request
  interception alone therefore does not prove process-wide zero networking.
  The trace does not establish that project content was in those attempts.
- Source checkout clean after tests.

## Recommended integration (not implemented)
Pin the full commit and file hashes. Keep compiler, theme tool, checker, needed
templates/references, and license. Do not launch the gallery; remove remote font
links if adopting gallery HTML. No automatic pull/update/install or handoffs to
unreviewed tools. Re-audit changed files before upgrading.
For strict privacy, execute preview/export/browser rendering with OS- or
organization-enforced egress denial covering subprocesses, not merely a prompt
instruction or the upstream checker. An enterprise-managed browser policy may
provide the equivalent boundary. These controls must be verified on the user's
machine; the Linux audit does not install a macOS/Windows policy.
Validate generated assets, reject external resource references, and treat the
upstream checker as supplementary. Avoid ingesting arbitrary third-party SVGs
as trusted input. Local files still contain sensitive information: using them
in a public repository or hosted README intentionally publishes that content.

## Suggested skill statement
"Uses animdiagram commit a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486,
reviewed on 2026-11-07. Core compilation and theme conversion process local
files and require no external diagram service. Browser preview/export must run
with outbound networking blocked for the strict local-only workflow. The
bundled online-font gallery is excluded. Your organization's approved Claude
connection is separate. Re-audit before updating the pinned dependency."

Do not claim: "Everything in this clone is guaranteed never to contact the
network" or "passing check.py proves the SVG cannot make requests."

## Evidence files
inventory-and-checks.json: tracked-file hashes, imports, SVG checks, spec results,
                          raster chunks, validator fixtures.
core-results.json: exact core commands and stdout.
core-network.log / smoke-network.log: syscall traces in network isolation.
browser-results.json: all SVG renders, phase observations, blocked URL attempts.
browser-network.log: browser/export process network syscall trace.
audit_local.py / core_workflow.py / audit_browser.py: reproduction harnesses.
Tests are finite and configuration-specific. Browser/OS security, adversarial
parser exploits, installers, external linked skills, and future source changes
are not certified by this report.

## Integration status

The SL wrapper now implements commit/file verification, a verified execution snapshot, and local installation. It does not expose gallery execution, video export, or preview --open. It does not install a browser firewall or fix upstream check.py. The original audit findings above remain scoped to the pinned upstream source.

The SHA-256 inventory is shipped as [verified-files.sha256](verified-files.sha256). Raw audit traces and reproduction harnesses were retained in the audit workspace; they are not distributed in this skill. [results-summary.json](results-summary.json) preserves the relevant outcomes without machine-specific logs.

## Agent context and future enforcement

A ~40-token CLAUDE.md rule breaks even after approximately (SVG tokens avoided minus replacement explanation tokens) / 40 fresh instruction loads. Example: (800 - 100) / 40 = 17.5 loads for a simple flow; (8000 - 500) / 40 = 187.5 for a detailed flow. If the prose is already in context, the points are 20 and 200. These are illustrative estimates, not tokenizer measurements. Reading Markdown normally includes only the image reference, not SVG bytes.

Continuing turns normally retain one copy of instructions, while repeated model input processing can affect cost; prompt caching changes billing rather than context occupancy. Restarts/resumes/compactions count as another load only when the instructions actually enter a newly constructed context. Context capacity is local to each session, not pooled across sessions.

A future System One Harness integration could intercept SVG reads, prefer a matching .agent.md, allow explicit visual editing, and handle missing companions. The actual Claude hook contract must be verified first. A Read-tool-only block would not prevent shell or other-tool reads. No hook is implemented or certified by this skill.

## Wrapper validation

Run from the Claude Backstage checkout:

```sh
python3 -I skills/sl-svg-diagram/tests/test_wrapper.py /path/to/audited/animdiagram
```

The suite uses disposable checkouts/installations. It covers silent valid execution, changed and missing files, a different commit with identical content, symlinks, added tracked files, Python-path injection, malformed configuration, blocked browser launching (including option abbreviations), real generation, installation/rerun behavior, and execution of verified bytes after the checkout changes. A fresh download/setup and an installed wrapper/compiler run with network isolation were also exercised.

Five installed verification invocations measured 39.7–51.8 ms (median 41.3 ms) in the Linux audit environment before the malformed-configuration guard was added; this is an indicative observation, not a performance guarantee. Core wrapper/compiler network tracing observed no network syscalls. No live Claude Code invocation or macOS/Windows execution is claimed.
