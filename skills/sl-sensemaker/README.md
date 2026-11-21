# SL Sensemaker

**Understand the problem. Discover better ways to work.**

Start with `/sl-sensemaker` and describe something you’re running into while working with an LLM or AI agent. Sensemaker asks questions until it understands what happened and what you want to achieve. Then it suggests a practical next step, shows you the catalog entry behind it, and tells you where the evidence runs out.

## Try a conversation

In Claude Code, type `/sl-sensemaker` on its own to let Sensemaker open the conversation. You can also start with a specific problem:

```text
/sl-sensemaker I asked my agent to fix the padding on a button. It made CI green by disabling the failing check. How should I scope its access next time?
```

Sensemaker might ask, “Which files did the agent need to change?” Reply in the same chat: “Only the button’s stylesheet. A separate CI job runs the checks.”

That detail matters. The agent could edit the very check that judged its work. For this task, Sensemaker can suggest giving it write access to the stylesheet and read-only access to the CI configuration. You can keep talking, for example by asking how the advice changes if the agent also needs to run a test locally. [Overpowered Coding Agent](catalog/anti-patterns/AP10-overpowered-coding-agent.md)

## Install

From the root of your Claude Backstage checkout, run:

```sh
./skills/sl-sensemaker/setup.sh
claude
```

Setup uses a POSIX shell and standard file utilities. It installs the skill at `~/.claude/skills/sl-sensemaker/SKILL.md`. You can then invoke it from any project.

## Where the guidance comes from

SL Sensemaker is the first skill that uses the shared pattern catalog. The [symptom bridge](bridge-file.md) and [catalog lookup](catalog/catalog-lookup.md) help it locate entries. Sensemaker reads the entries themselves before recommending an approach. If they answer only part of your question, it explains what they cover and what remains open.

Setup installs the catalog and navigation files under `~/.cache/sl-mentor/`, the original cache location. Catalog lookup works locally. Future skills, such as transcript analysis or workflow evaluation, can reuse those same files.

## Update or switch from SL Mentor

From your checkout, run:

```sh
git pull --ff-only
./skills/sl-sensemaker/setup.sh
```

Open Claude Code and invoke `/sl-sensemaker`. Setup refreshes bundled files and preserves additions you’ve saved under their own names. If you previously installed SL Mentor, the new command uses your existing catalog. The old command may still appear because it was installed in a separate skill folder.

If the catalog is missing, rerun setup. If Claude reports a read-permission error, check its access to `~/.cache/sl-mentor/`.
