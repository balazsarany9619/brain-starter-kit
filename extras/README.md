# Extras: skills and hooks

Optional. The templates work without them; these make the brains maintain themselves.

| File | What it does |
|---|---|
| `skills/log` | Writes a dated line into the right project's `log.md` and commits it. |
| `skills/brain-rule` | Turns a correction into a rule in the narrowest place, sharpening before adding. |
| `skills/brain-prune` | Monthly pass: every line must prevent a real mistake, the rest goes. |
| `hooks/brain-router.py` | Routes a question to the right project brain from any folder (keyword match, silent otherwise). |
| `hooks/memory-check.py` | Blocks new memory files that copy rules which belong in a brain. |

Install: copy `skills/*` to `~/.claude/skills/`, `hooks/*.py` to `~/.claude/hooks/`, and merge `hooks/settings-snippet.json` into `~/.claude/settings.json` (merge, never overwrite). Then fill `ROUTES` in `brain-router.py` with your projects. Claude Code does this for you in step 5 of `CLAUDE-SETUP.md`.
