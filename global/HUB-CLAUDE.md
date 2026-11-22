# Project hub: overview

Every subfolder is a standalone project with its own brain (CLAUDE.md with `@topics/` imports, `reference/` on demand, `OPEN.md`, `log.md`). How it works: `BRAIN-RULES.md`. On conflict between an old doc and the brain, the brain wins.

## Projects

| Project | What it is | Status |
|---|---|---|
| **{{PROJECT}}** | {{ONE_LINE}} | {{STAGE}}. Brain ✅ ({{lean / full}}). Next: {{NEXT_STEP}} |

## Connections between projects
<!-- Add a line when two projects share an audience, code, a niche or compete for the same hours. -->

## Convention for new projects
1. Copy `_TEMPLATE`, rename, fill the `<!-- FILL -->` markers (CLAUDE.md and identity-and-role first).
2. `docs/` for details, `reference/` for on-demand deep docs, `source-assets/` for raw material (not in the root).
3. Add a row here and a router row in `~/.claude/CLAUDE.md`.
4. Maintain `log.md`. Every correction becomes a rule plus a log line in the same turn.
