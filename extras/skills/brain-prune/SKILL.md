---
name: brain-prune
description: Monthly prune pass on one project brain (or the global files) with the test "would removing this line cause a mistake?". Manual only, run as /brain-prune <project or global>.
disable-model-invocation: true
---

# Brain prune: $ARGUMENTS

Goal: fewer, sharper rules. Bloated CLAUDE.md files make Claude ignore instructions (code.claude.com/docs/en/best-practices).

1. Note the size of the target first (bytes of `CLAUDE.md` plus every `@` imported file).
2. Read the target's `CLAUDE.md` and every `@` imported file. For `global`: `~/.claude/CLAUDE.md` and `MEMORY.md`.
3. Classify every rule or paragraph in a table:
   | Line | Verdict | Reason |
   - **keep**: removing it would cause a real mistake, and Claude does not do it by default.
   - **cut**: Claude does it anyway, it is generic advice, template filler, outdated, or duplicated elsewhere.
   - **move**: needed only sometimes, goes to `reference/` or a project skill.
   - **hook**: must happen every time and a script can check it.
   - **merge**: two rules say the same thing.
   A rule that a `log.md` incident still cites is keep unless the incident is obsolete.
4. Show the table to the user and wait for a go before deleting anything. Then apply and report the size before and after.
5. Commit (`git commit -m "prune: <project>"`) and add a `log.md` line with the numbers.
