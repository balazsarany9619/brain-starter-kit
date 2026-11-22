# How the brain structure works

A "brain" is a set of markdown files Claude Code loads automatically, so it knows who you are, how you want to work and the hard rules of each project without you repeating them. It is built on Claude Code's own mechanism: `CLAUDE.md` files load at session start, and lines starting with `@path` import other files.

## Three levels

```
~/.claude/CLAUDE.md                 GLOBAL BRAIN: loads in every session, any folder
<hub>/CLAUDE.md                     HUB MAP: which project lives where, what state
<hub>/<Project>/
  CLAUDE.md                         PROJECT BRAIN: identity, hard rules, @topics imports
  topics/*.md                       rule files, always loaded via @ import
  reference/index.md                map of deep docs, opened ON DEMAND only
  OPEN.md                           open questions and next steps (not imported)
  log.md                            dated learnings log (not imported)
```

Why hybrid: hard rules (tone, bans, phase cuts) must always be loaded, the `@` import guarantees that. Heavy detail (specs, research, briefs) would bloat every session, so it stays behind `reference/index.md` and Claude opens it when a task needs it.

## The brain router
The global CLAUDE.md has a table: "if the question is about X, open brain Y first". That way a question about a project gets the right rules even when the session runs in another folder.

## Size limits (context costs tokens in every session)
| What | Limit |
|---|---|
| Global CLAUDE.md | 8 KB |
| One imported topic file | 15 KB |
| Project CLAUDE.md plus all imports | 20 KB |
| OPEN.md, log.md | never `@` imported, read on demand |

If a file grows past its limit: shorten it or move detail into `reference/`.

## Rule form
Every new rule in a topic file carries:
1. **Incident**: date and what happened.
2. **Rule** in the imperative.
3. **Why.**
4. **Pass/fail test**: a mechanical check (e.g. "grep the draft for long dashes, zero hits").

Before adding a rule, search for the existing one that should have prevented the mistake and sharpen THAT one instead of adding a second next to it. A limit never gets a tolerance; if content does not fit, something drops.

## Maintenance
- **A correction becomes a rule in the same turn**: topic file plus a `log.md` line. Never "I will remember".
- `log.md` entries are dated (`## YYYY-MM-DD`) and start with a bold word: **Creation**, **Update**, **Win**, **Loss**, **Learning**, **Deprecation**.
- Once a month: promote recurring log learnings into topics, delete rules that no longer apply, check the size limits.
- The structure is about 20% of the value. The accumulated learnings are the other 80%.

## Lean vs. full
- **Lean (3 to 4 topics)**: products, apps, games, personal projects. identity-and-role, format-rules, workflow-and-cadence, tech-stack.
- **Full (10 topics)**: anything you sell or market (service, agency, outreach). Adds positioning, offer-and-pricing, icp-and-personas, tone-and-style, anti-drift-and-checklist, tracker-and-tools.
