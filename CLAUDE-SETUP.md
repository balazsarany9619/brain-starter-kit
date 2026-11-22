# Setup instructions for Claude Code

You are reading this because the user dropped `brain-starter-kit.zip` (or this folder) into Claude Code and said something like **"set up the brain structure"**. Follow these steps in order. Do not skip the questions, they are the point.

## 0. Ground rules for this setup
- Talk to the user in **their** language (detect it from their messages). Files you write stay in the language the user picks in question G7.
- Ask with the **AskUserQuestion** tool: 2 to 4 options per question, at most 4 questions per call, put your recommended option first and mark it "(Recommended)". The tool adds an "Other" field automatically, so the user can always type their own answer. Never add an "Other" option yourself.
- If your client has no AskUserQuestion tool, print the questions as numbered lists with letters (a, b, c, d) plus "e) other: ____" and wait for the answers.
- **Infer before you ask.** If something can be read from the machine (existing `~/.claude/CLAUDE.md`, an existing project folder with README, package.json, code), read it first and offer the detected value as the recommended option, labeled "(detected)". Skip questions the user already answered in their first message.
- **Never overwrite** an existing file. If `~/.claude/CLAUDE.md` exists, copy it to `~/.claude/CLAUDE.md.backup-<date>` first, then merge: keep every rule the user already has, add the new sections around them.
- Show the user what you are about to write (a short summary, not the full file) before writing global files.

## 1. Unpack
1. Find the kit: the path the user dropped (a cloned folder or a zip). If there is none, search the Downloads and Desktop folders for `brain-starter-kit*`.
2. A zip: extract it into a fresh temp folder (not into the home folder). A folder: read it in place. Read `BRAIN-RULES.md`, then the files in `questionnaire/`.

## 2. Global brain (once per machine)
1. Run the questions in `questionnaire/01-global.md` (3 rounds).
2. Fill `global/CLAUDE.md` from the answers. Replace every `{{PLACEHOLDER}}`, delete sections that do not apply. Keep it **under 8 KB**, it loads in every session.
3. Write it to `~/.claude/CLAUDE.md` (Windows: `C:\Users\<name>\.claude\CLAUDE.md`), merged with any existing file as described above.
4. Create the hub folder the user chose (G8). Copy `project-template/` into it as `_TEMPLATE/` and write `global/HUB-CLAUDE.md` as `<hub>/CLAUDE.md`. Copy `BRAIN-RULES.md` into the hub.

## 3. First project brain
1. Ask: "Which project should get the first brain?" Options: an existing folder you detected, a new project, skip for now.
2. Run `questionnaire/02-project.md`. Rounds P4 (selling) and P5 (product build) only when they apply.
3. Copy `_TEMPLATE` to `<hub>/<Project Name>/`. Choose **lean** or **full** (question P3.4):
   - lean: keep `identity-and-role.md`, `format-rules.md`, `workflow-and-cadence.md`, plus `tech-stack.md` if code is involved. Delete the other topic files and their `@` lines in CLAUDE.md.
   - full: keep all 10 topics.
4. Fill every `<!-- FILL -->` you have an answer for. Where the user gave no answer, leave a one-line `<!-- OPEN: question -->` instead of inventing content. **Never invent facts, numbers, customers or proof.**
5. Write the first `log.md` entry (**Creation**) and put open questions into `OPEN.md`.
6. Add the project as a row to the hub CLAUDE.md table and to the router table in `~/.claude/CLAUDE.md` with 3 to 6 trigger words, so questions about it get routed there from any folder.

## 5. Extras (ask first)
Ask once: "Install the maintenance skills and hooks too?" (Recommended: yes). If yes, follow `extras/README.md`: copy the skills and hooks, merge the settings snippet into `~/.claude/settings.json` (back it up first, never overwrite), and fill `ROUTES` in `brain-router.py` with the projects created above.

## 4. Verify and report
- Check: every `@topics/...` line in each CLAUDE.md points to an existing file; no `{{PLACEHOLDER}}` left in global files; global CLAUDE.md under 8 KB; each project CLAUDE.md plus its imported topics under 20 KB.
- Report to the user in 5 to 8 lines: what was created where, which answers are still open, how to start (`cd "<hub>/<Project>"` then `claude`), and the maintenance rule: every correction becomes a rule plus a `log.md` line in the same turn.
- Delete the temp extraction folder (only if you extracted a zip).
