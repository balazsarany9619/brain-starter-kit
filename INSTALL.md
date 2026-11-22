# Brain Starter Kit: installation guide

Gives Claude Code a permanent memory of who you are, how you want to work and the rules of each of your projects. Setup takes about 10 minutes and works by answering multiple-choice questions.

## What you need
- Claude Code installed and logged in (terminal, desktop app or VS Code).
- This kit: `git clone https://github.com/balazsarany9619/brain-starter-kit` or GitHub's "Code, Download ZIP". A zip does not need unzipping, Claude does that.

## Installation (3 steps)

1. **Start Claude Code** in your home folder:
   - Terminal: open a terminal and type `claude`
   - Desktop app: open a new session

2. **Drag the `brain-starter-kit` folder (or the zip) into the Claude Code window.** This pastes the path into the input field.

3. **Type behind the path and press Enter:**

   ```
   set up the brain structure
   ```

   Full message looks like: `C:\Users\you\Downloads\brain-starter-kit set up the brain structure`

Claude then unpacks the kit, reads `CLAUDE-SETUP.md` and asks you questions in rounds. Every question has suggestions; pick one, or choose **"Other"** and type your own answer. Skipping is fine, skipped questions are saved in `OPEN.md` for later.

## What gets created
| Where | What |
|---|---|
| `~/.claude/CLAUDE.md` | Your global brain: how Claude works with you, in every session. An existing file is backed up first and merged, not overwritten. |
| `<hub folder>/` | One folder for all projects, with an overview `CLAUDE.md`, `BRAIN-RULES.md` and `_TEMPLATE/`. |
| `<hub folder>/<Project>/` | A project brain: `CLAUDE.md`, `topics/`, `reference/`, `OPEN.md`, `log.md`. |

## Daily use
- Work on a project: `cd "<hub folder>/<Project>"` then `claude`. The brain loads automatically.
- Claude makes a mistake? Correct it once and say "make it a rule". It goes into the topic file and `log.md`.
- New project later: say `create a new project brain for <name>`. Claude copies `_TEMPLATE` and asks the project questions again.

## Rules of thumb
- Read `BRAIN-RULES.md` once, it explains the structure and the size limits.
- Keep the global brain short (under 8 KB). It loads in every session and costs tokens every time.
- The value grows with the corrections you log, not with the template.
