---
name: brain-rule
description: Turn a correction from the user into a rule in the right brain, sharpening an existing rule before adding a new one. Use whenever the user corrects Claude ("no", "wrong", "not like that", "I told you", "always", "never again") or asks to "make it a rule".
---

# Brain rule

A correction becomes a rule in the same turn, but rules must earn their place.

1. **Scope:** does it apply in every session (global `~/.claude/CLAUDE.md`), one project (that brain's `topics/` or `learnings/`), or one task type (a skill)? Pick the narrowest scope that would have prevented the mistake. Memory is NOT a rule store: only tool tricks and facts with no home yet.
2. **Search first:** grep the target brain and global files for the rule that should have caught this. If it exists, sharpen THAT rule (clearer wording, add a pass/fail test). Only if none exists, add one.
3. **Hook instead of line?** If it must happen every time with zero exceptions and a script can check it, propose a hook instead of a text rule.
4. **Format:** incident (date, what happened), rule in the imperative, why, mechanical pass/fail test.
5. **Cost check:** an `@` imported topic must stay small (under ~15 KB per file); if a rule would exceed that, put it where it loads on demand (`reference/`, a project skill) and link it.
6. Add a `log.md` line (skill `log`) and commit if the folder is a git repo.
7. Tell the user in one line where the rule now lives.
