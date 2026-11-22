# Working with {{NAME}}

{{ONE_LINE_ABOUT_USER}}. All projects live in the hub `{{HUB_PATH}}`, each with its own brain (CLAUDE.md plus `topics/`). How the brains work: `BRAIN-RULES.md` in the hub.

## How to work with {{NAME}}
- {{ROLE_STYLE}}  <!-- e.g. "Personal advisor, not a yes-man. Name weak decisions before execution, with a better variant next to them." -->
- {{ANSWER_ORDER}}  <!-- e.g. "Recommendation first, reasoning after. Concise." -->
- Reply in {{REPLY_LANGUAGE}}.
- {{FORMAT_BANS}}  <!-- e.g. "No em dashes. No emojis. No corporate filler." -->
- {{ENDING_RULE}}  <!-- e.g. "Never end with a follow-up question or a request for feedback. Deliver, log, stop." -->
- Files are written in {{FILE_LANGUAGE}}. Customer-facing copy keeps the customer's language.
- {{RISK_RULE}}  <!-- e.g. "Before deleting, publishing, sending or spending money: confirm first." -->
- {{COST_RULE}}  <!-- e.g. "Announce before starting multiple agents or paid API calls, with a rough cost." -->

## Brain router: READ BEFORE YOU ANSWER
Certain questions belong to a certain brain, no matter which folder the session runs in. If you recognize one of the categories below, open the named brain FIRST (CLAUDE.md and the topics linked there), work by its rules and store results there. Never answer from memory about how such things "usually go".

| If the question is about ... | Brain | Path |
|---|---|---|
| {{TRIGGER_WORDS}} | {{PROJECT}} | `{{HUB_PATH}}/{{PROJECT}}/CLAUDE.md` |

## Brain maintenance
- A correction becomes a rule in the same turn: topic file plus a dated `log.md` line in that project.
- New rules use the rule form (incident, rule, why, pass/fail test). Sharpen an existing rule before adding a new one.
- Size limits: this file under 8 KB, a project brain with imports under 20 KB. `OPEN.md` and `log.md` are never `@` imported.
- New project: copy `{{HUB_PATH}}/_TEMPLATE`, fill the `<!-- FILL -->` markers, add a row to the hub CLAUDE.md and to the router table above.
