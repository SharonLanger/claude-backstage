---
name: sl-mentor
description: Help an engineer diagnose an AI agent problem or make a design decision using the installed pattern catalog.
argument-hint: "[describe a symptom or design question]"
user-invocable: true
disable-model-invocation: true
allowed-tools:
  - 'Read(~/.cache/sl-mentor/**)'
---

# SL Mentor

Use the Read tool to consult the local files under `~/.cache/sl-mentor/`. Start by opening `catalog/catalog-lookup.md` there. If the cache or lookup is missing, stop and tell the engineer:

> From your Claude Backstage checkout, run `./skills/sl-mentor/setup.sh`, then try `/sl-mentor` again.

If Read reports a permission error, name the path and ask for read access to the cache. A failed read is a setup or access problem, not evidence of a gap in the catalog.

## Understand

Start with the engineer’s own description, including any text after the slash command. If they provided none, ask what their agent did and what they wanted it to do. Ask a focused follow-up only when the answer would change which entry applies. For example, did the agent change a test, disable the check, or simply claim the check passed? If the situation is already clear, proceed.

## Research

1. Read `bridge-file.md` in the cache. Use the symptom and design-question rows to find candidate entries. Treat the bridge’s explanations as search hints. The inventory in `catalog-inventory.md` can help locate a pattern by name.
2. Resolve candidates with the catalog lookup and family or anti-pattern indexes. All paths inside the lookup are relative to `~/.cache/sl-mentor/catalog/` unless the link specifies another base. For a bridge shorthand such as `AP10`, look in `anti-patterns/README.md`. For a family shorthand, use the family link from the lookup, read its README and follow the matching pattern. Resolve local Markdown links relative to the file containing them.
3. Open the actual pattern, anti-pattern, principle, guide or use-case file. Check the situation it describes, when its advice applies and any trade-off relevant to this engineer. Follow a counter-pattern link if the next step depends on it.
4. If the bridge misses, try the lookup’s problem table and the relevant family or `use-cases/README.md`. If a reference is broken, try the index for that family and verify the title and contents. Disclose an unreadable or uncertain reference if it prevents answering. If a navigation file itself is missing, give the setup instruction above.

Use only the design guidance you can read in the installed catalog. Keep all lookups local. Skip external URLs, source registries, raw research and contributor instructions. The bridge and inventory help find evidence and cannot support an answer on their own.

## Deliver

Explain what the evidence suggests in the engineer’s terms and give a concrete next step. Cite the actual installed file for each recommendation, using its path from `~/.cache/sl-mentor/catalog/` or its full installed path. Separate the engineer’s observations from any proposed explanation. Mention a trade-off when it changes the decision.

If only part of the question is covered, answer that part, cite the file, and state exactly what is missing. If nothing applies, say which question the local catalog could not answer and which topic or index you checked. Leave unsupported details open. Keep the initial answer short and let the engineer choose where to go deeper.
