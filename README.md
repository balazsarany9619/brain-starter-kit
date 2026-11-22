# Brain Starter Kit for Claude Code

Give Claude Code a permanent memory: who you are, how you want to work, and the rules of every project. Setup takes about 10 minutes of multiple-choice questions. Claude writes the files, you answer.

```
~/.claude/CLAUDE.md          global brain: how Claude works with you, every session
<hub>/CLAUDE.md              map of all projects and a router
<hub>/<Project>/
  CLAUDE.md                  short project brain, imports topics with @
  topics/                    identity, tech stack, format rules, ... loaded every session
  reference/                 long material, loaded only on demand
  OPEN.md                    open questions instead of invented answers
  log.md                     decisions and corrections, newest first
```

## Why bother
- **A short brain plus topic files is cheaper.** In my own setup one project brain went from about 30,000 to 5,700 tokens per session start after splitting it this way.
- **Stable context gets cached.** Prompt caching cuts the cost of reused context by up to 90 % ([Anthropic](https://www.anthropic.com/news/prompt-caching)).
- **More context is not better context.** Models lose accuracy as the input grows ([Chroma, Context Rot](https://research.trychroma.com/context-rot)). The structure keeps only what matters in every session.
- **Corrections stick.** Every correction becomes a rule plus a `log.md` line, so the same mistake does not happen twice.

## Quick start
1. Get the kit: `git clone https://github.com/balazsarany9619/brain-starter-kit` (or Code, Download ZIP).
2. Start Claude Code in your home folder.
3. Drag the folder into the Claude Code window and add: `set up the brain structure`

Claude reads `CLAUDE-SETUP.md` and asks the questions. Details for humans: `INSTALL.md`. The rules behind the structure: `BRAIN-RULES.md`.

## What is inside
| Path | Content |
|---|---|
| `CLAUDE-SETUP.md` | Step by step instructions for Claude Code |
| `questionnaire/` | The global and the project questions |
| `global/` | Templates for `~/.claude/CLAUDE.md` and the hub `CLAUDE.md` |
| `project-template/` | One project brain with 10 topic files (lean mode keeps 3 to 4) |
| `extras/` | Optional skills (`log`, `brain-rule`, `brain-prune`) and hooks (brain router, memory check) |

Made by Balazs Arany, [techwithbali.com](https://techwithbali.com). MIT licensed.
