# Questionnaire 1: global brain (who the user is, how Claude should work)

Run as 3 AskUserQuestion calls (rounds), max 4 questions each. Translate questions and options into the user's language. "Header" is the short chip label (max 12 characters). The tool adds a free-text "Other" field to every question automatically, that is where the user writes their own answer when no option fits. Put the recommended option first with "(Recommended)" only where a recommendation is given below. "Maps to" says which placeholder the answer fills.

Before round 1, ask in plain text (no options): **"What should I call you, and what do you do in one sentence?"** Maps to `{{NAME}}`, `{{ONE_LINE_ABOUT_USER}}`.

## Round 1: how you want to work with Claude

**G1. Header "Claude role"**: How should Claude behave when you ask for something? (single)
- Honest advisor (Recommended): points out weak decisions before doing them, with a better version next to it.
- Executor: does what you ask, only flags real errors.
- Teacher: explains the why, helps you learn while building.
- Sparring partner: challenges ideas, asks back, plays devil's advocate.
Maps to `{{ROLE_STYLE}}`.

**G2. Header "Answer style"**: How should answers be structured? (single)
- Recommendation first, then reasoning, short (Recommended)
- Step-by-step explanation, more detail
- Only the result, no explanation unless asked
- Options compared side by side, I decide
Maps to `{{ANSWER_ORDER}}`.

**G3. Header "Ending"**: How should Claude end a reply? (single)
- Deliver and stop, no follow-up question (Recommended): fewer interruptions.
- Suggest the next step in one line
- Ask if anything should change
Maps to `{{ENDING_RULE}}`.

**G4. Header "Format bans"**: Which writing habits should Claude never use? (multiSelect)
- Long dashes (em dashes): typical AI tell.
- Emojis
- Corporate filler ("seamless", "unlock", "elevate")
- Heavy markdown (lots of headings and bold)
Maps to `{{FORMAT_BANS}}`.

## Round 2: languages and safety

**G5. Header "Reply lang"**: In which language should Claude reply to you? (single)
- Offer the detected language of the user's messages first, labeled "(detected)".
- English
- German
- Same language I write in
Maps to `{{REPLY_LANGUAGE}}`.

**G6. Header "Risky acts"**: What should Claude ask before doing? (multiSelect)
- Deleting or overwriting files (Recommended)
- Publishing, sending emails or messages, pushing to git (Recommended)
- Spending money (paid APIs, credits, subscriptions)
- Installing software or changing system settings
Maps to `{{RISK_RULE}}`.

**G7. Header "File lang"**: In which language should brain files be written? (single)
- English (Recommended): fewer tokens, so cheaper and faster per session.
- Same as my reply language
- Per project, decide each time
Maps to `{{FILE_LANGUAGE}}`.

**G8. Header "Hub folder"**: Where should all projects and their brains live? (single)
- `~/Desktop/Claude Code Projects` (Recommended): visible, easy to drag files in.
- `~/Documents/Claude Projects`
- `~/Projects` or `~/code`
- An existing folder I detected: `<path>` (offer only if one was found)
Maps to `{{HUB_PATH}}`.

## Round 3: what you work on (sets up the router)

**G9. Header "Projects"**: What kinds of projects do you use Claude Code for? (multiSelect)
- Apps, websites or software
- A business, service or sales (clients, outreach, offers)
- Content (YouTube, social, writing, music)
- Personal (fitness, finance, learning, life admin)
Used to suggest projects for the router table and lean vs. full brains.

**G10. Header "Cost"**: How careful should Claude be with usage limits and paid tools? (single)
- Announce before multi-agent runs or paid calls, with rough cost (Recommended)
- Always use the cheapest approach, ask before anything heavy
- Do not worry, speed over cost
Maps to `{{COST_RULE}}`.

**G11. Header "Router"**: Which projects should get their own brain now? (multiSelect)
- Offer up to 4 project names detected on the machine or mentioned so far, each with a one-line description.
- If none are known, ask in plain text instead: "Name your 1 to 5 active projects, one line each."
Each chosen project becomes a router row: ask for (or propose) 3 to 6 trigger words per project.
