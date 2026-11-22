# Questionnaire 2: project brain (what the project is about)

Run per project. Rounds P1 to P3 always, P4 only if the project sells something, P5 only if code or a product is built. Max 4 questions per AskUserQuestion call. The tool adds a free-text "Other" field automatically.

**Infer first.** If the project folder exists, read README, package.json / pyproject / app config and the folder tree before asking. Turn what you find into suggestions labeled "(detected)" and put them first. Skip a question entirely when the answer is obvious from the files, and say so in one line.

Before round 1, ask in plain text: **"Describe the project in one or two sentences, like you would to a friend."** Use the answer to tailor all options below (replace the generic examples with ones that fit).

## Round P1: what it is

**P1.1 Header "Type"**: What kind of project is it? (single)
- Product (app, game, software, tool)
- Service or business (clients pay you for work)
- Content or brand (channel, writing, music, community)
- Personal or learning (training, finance, a skill, a hobby)
Maps to: lean vs. full default, which topics matter.

**P1.2 Header "Stage"**: Where does it stand today? (single)
- Idea, nothing built yet
- Prototype or first version, no real users
- Live, first users or clients, little or no revenue
- Running with revenue or a real routine
Maps to identity-and-role "reality", OPEN.md.

**P1.3 Header "Goal"**: What is the ONE goal for the next 3 months? (single)
- First paying customer or first revenue
- Ship a working version to real users
- Learn or build a portfolio piece
- Grow what already works (more users, more revenue)
Follow up in plain text for the number: "What number would make it a success, and by when?"

**P1.4 Header "Time"**: How much time per week goes into it? (single)
- Under 5 hours
- 5 to 10 hours
- 10 to 20 hours
- Full time
Maps to identity-and-role "reality you remind me of".

## Round P2: Claude's job and the audience

**P2.1 Header "Claude hat"**: Which role should Claude play in this project? (single, tailor options to P1.1)
- Product: Senior engineer / Product partner / Designer / Tech lead and reviewer
- Service: Strategist and advisor / Sales and outreach partner / Delivery specialist (e.g. web designer) / Operations and automation builder
- Content: Script writer / Creative director / Growth and analytics partner / Editor
- Personal: Coach with data / Analyst / Planner / Research assistant
Maps to identity-and-role "What Claude's role is".

**P2.2 Header "Audience"**: Who is it for? (single, tailor)
- Businesses (B2B)
- Consumers (B2C)
- Myself only
- An employer or a team I work with
Maps to icp-and-personas, follow up in plain text: "Describe the ideal user or customer in one sentence."

**P2.3 Header "Out lang"**: In which language is the OUTPUT (what customers, users or the public see)? (single)
- Same as my reply language
- English
- The customer's local language
- Mixed, depends on the piece
Maps to tone-and-style "Language".

**P2.4 Header "Voice"**: How should public-facing output sound? (multiSelect)
- Direct and confident, no hype
- Friendly and casual
- Expert and precise
- Playful, humor allowed
Maps to tone-and-style "output voice".

## Round P3: rules and risks

**P3.1 Header "Drift risk"**: What usually goes wrong for you on projects like this? (multiSelect)
- Scope creep: adding features or extras before the core works
- Building before checking if anyone wants it
- Perfectionism: polishing instead of shipping
- Jumping between projects, nothing finished
Maps to anti-drift-and-checklist "drift patterns" and identity-and-role "standing questions".

**P3.2 Header "Hard rule"**: Which hard rule must Claude never break here? (single, tailor)
- Never invent facts, numbers or proof
- Never ship without testing it myself
- Never contact customers or publish without my OK
- Never change the core concept without asking
Maps to CLAUDE.md "Critical gotchas". Follow up: "Any other hard no for this project?"

**P3.3 Header "Tracker"**: Where is progress or data tracked? (single)
- Nothing yet, start with a markdown file in the project (Recommended)
- Spreadsheet (Excel, Google Sheets)
- Notion, Airtable or similar
- A CRM or a project tool (HubSpot, Linear, Trello)
Maps to tracker-and-tools.

**P3.4 Header "Brain size"**: How big should this brain be? (single)
- Recommend from P1.1: "Lean, 3 to 4 topics (Recommended)" for product, content, personal; "Full, 10 topics (Recommended)" for service or business.
- The other option without "(Recommended)".
Maps to the lean/full choice in CLAUDE-SETUP.md step 3.

## Round P4: only if the project sells something

**P4.1 Header "Offer"**: What does the customer buy? (single)
- One-time project
- Monthly retainer or subscription
- Product purchase or license
- Mix: setup fee plus monthly
Maps to offer-and-pricing.

**P4.2 Header "Price"**: Price range per customer? (single, tailor currency to the user)
- Under 500
- 500 to 2,000
- 2,000 to 10,000
- Not decided yet
Follow up: "What makes the price obviously worth it for the buyer?"

**P4.3 Header "Proof"**: What proof do you have today? (single)
- None yet, founder-led story
- First results or a test case
- Paying clients with results
- Strong track record or testimonials
Maps to positioning "Proof". Never invent proof.

**P4.4 Header "Channel"**: How do customers find you? (multiSelect)
- Cold outreach (email, LinkedIn, calls)
- Content and social
- Referrals and network
- Ads or marketplaces
Maps to workflow-and-cadence.

## Round P5: only if code or a product is built

**P5.1 Header "Stack"**: Which tech stack? (single, put detected stack first)
- (detected) stack from the repo
- Web: React / Next.js / Vite
- Mobile: Expo / React Native, Swift or Kotlin
- No-code or other (Framer, Webflow, Godot, Python scripts)
Maps to tech-stack.

**P5.2 Header "Hosting"**: Where does it run? (single)
- Vercel, Netlify or Cloudflare
- App stores
- Local only for now
- Own server or cloud (AWS, GCP, Supabase)

**P5.3 Header "Quality"**: What must be true before something counts as done? (multiSelect)
- Tests pass
- I tested it myself on the real device or in the browser
- Builds without warnings, linter clean
- Reviewed by Claude before commit
Maps to format-rules / anti-drift pre-ship checklist.

**P5.4 Header "Git"**: How should Claude handle git? (single)
- Commit only when I say so (Recommended)
- Commit after each finished step, never push
- Commit and push freely on feature branches
Maps to CLAUDE.md "Critical gotchas".

## After the rounds
Summarize the project in 3 lines and ask in plain text: "Anything wrong or missing?" Then write the brain. Unanswered points go into `OPEN.md` under "Unanswered setup questions", never into the topics as guesses.
