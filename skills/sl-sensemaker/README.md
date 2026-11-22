# 🧭 SL Sensemaker

**Your agent did what you asked. Somehow, that wasn’t what you meant.**

Describe what happened. Untangle the problem. Find something useful to try next.

Start with `/sl-sensemaker` and describe something you’re running into while working with an LLM or AI agent. Sensemaker asks questions until it understands what happened and what you want to achieve. Then it suggests a practical next step, shows you the catalog entry behind it, and tells you where the evidence runs out.

## 💬 Sound familiar? Try asking…

| | Start here |
|---|---|
| 🤝 **Too agreeable?** | “It agrees with every diagnosis I suggest. How do I get a useful second opinion?” |
| 👻 **Imaginary APIs?** | “That method doesn’t exist. This is the third time. What should I do differently?” |
| 🔁 **Another fix, another failure?** | “We keep patching the same thing. When should I try a fresh approach?” |
| 💭 **An idea you can’t quite explain?** | “Help me figure out what I mean before the agent starts building it.” |
| 🧩 **Too many tasks, one brain?** | “I delegated five things. Now everything is waiting for me.” |
| 🛑 **‘Improved’ right into a regression?** | “That strange-looking code was intentional. How do I stop it being rewritten?” |

## 🔎 Choose how deep to go

> “Give me one practical tip.”

> “Show me what I could say to my agent.”

> “Walk me through an example.”

> “Explain why this helps and show me the source.”

**You don’t need to know the pattern’s name. Start with the frustration.**

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

SL Knowledge Atlas is the shared local knowledge base. SL Sensemaker is its first skill. The [symptom bridge](bridge-file.md) and [catalog lookup](catalog/catalog-lookup.md) help it locate entries. Sensemaker reads the entries themselves before recommending an approach. If they answer only part of your question, it explains what they cover and what remains open.

Setup installs the catalog and navigation files under `~/.cache/sl-knowledge-atlas/`. Catalog lookup works locally. Future skills, such as transcript analysis or workflow evaluation, can reuse those same files.

## Update or repair

From your checkout, run:

```sh
git pull --ff-only
./skills/sl-sensemaker/setup.sh
```

Open Claude Code and invoke `/sl-sensemaker`. Setup refreshes bundled files and preserves additions you’ve saved under their own names.

If the catalog is missing, rerun setup. If Claude reports a read-permission error, check its access to `~/.cache/sl-knowledge-atlas/`.
