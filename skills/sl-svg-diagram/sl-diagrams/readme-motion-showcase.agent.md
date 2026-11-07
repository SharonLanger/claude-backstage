# Motion showcase semantics

Illustrative design samples, not a real API or measured execution trace. Three independent panels repeat on a seven-second clock:

- **Follow the call:** a request packet travels to `handle()`, then a result packet travels onward. Shows sequential handoffs.
- **Watch it accumulate:** a gauge fills from empty to full in five steps, then resets. Shows accumulation; it is not a live metric.
- **See work happen together:** worker A and worker B pulse at the same times. Shows synchronization, not alternative branches.

All panels are animation mechanisms to reuse, not different input scenarios. Reduced motion hides moving packets/pulses and displays the full bar; static labels retain the explanation.

The matching `.spec.json` edits motion; keep the matching SVG for layout. Copy all three assets with the referencing README, preserving or updating relative links.
