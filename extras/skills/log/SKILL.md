---
name: log
description: Append a dated entry to the right project's log.md (newest first) and commit it. Use at the end of a work block, after a decision, or when the user says "log this", "write it down", "keep this".
---

# Log

1. **Pick the project:** the hub project the work belongs to (cwd, or the brain the Brain-Router named), not the folder the session happens to run in.
2. **Write the entry** in that project's `log.md`, newest first, under `## YYYY-MM-DD` (create the heading if today's is missing):
   - Bold lead of 3 to 8 words, then what was done or decided, why, and where the file lives.
   - Numbers only with a source. Unknown facts as `[ ]`, never guessed.
   - 1 to 4 lines. Done items from `OPEN.md` move here and are removed there.
3. **Commit** if the folder is a git repo: `git add log.md <touched brain files> && git commit -m "log: <lead>"`. Never push without being asked.
4. If the entry contains a correction by the user, also run the `brain-rule` skill.
