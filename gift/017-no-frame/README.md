# Frame

Frame asks you about one job your company still does by hand, one
question at a time: the steps, what a finished result must have, one
good and one bad example, what you never want in it, and what you check
before it goes out. Then it writes your answers as a skill, so your AI
starts every run of that job from the way you do it.

## Install it

Pick the one AI you use.

### Claude Code

Type these two lines in Claude Code, one after the other:

```
/plugin marketplace add slavpetroff/agent-receipts
/plugin install frame@agent-receipts
```

Then type `/frame:frame` and answer its questions.

### Codex

Run these two lines in your terminal:

```
codex plugin marketplace add slavpetroff/agent-receipts
codex plugin add frame@agent-receipts
```

Then start Codex and ask it to use the frame skill.

### Claude.ai

1. Download [frame.zip](https://github.com/slavpetroff/agent-receipts/raw/main/gift/017-no-frame/frame.zip).
2. In Claude, open Customize > Skills, click +, then Create skill, then
   Upload a skill, and choose `frame.zip`.
3. Start a new chat and write: "Use the frame skill."

Skills on Claude.ai need code execution turned on in your settings.

### ChatGPT

1. Download [frame.zip](https://github.com/slavpetroff/agent-receipts/raw/main/gift/017-no-frame/frame.zip).
2. In ChatGPT, open Plugins in the sidebar, go to the Skills tab, click
   Create, then Upload from your computer, and choose `frame.zip`.
3. Start a new chat and write: "Use the frame skill."

ChatGPT skills are on Business, Enterprise, Healthcare and Edu plans.

### Any other AI, or a plan without skills

Open [skills/frame/SKILL.md](skills/frame/SKILL.md), copy everything
below the second `---` line, and paste it as the first message of a new
chat.

## After it runs

Frame prints your skill whole and tells you how to install it in the AI
you use. If your AI cannot take a skill, paste that text at the start of
every run of the job. The day you change how the job is done, change
that one line in the skill. Run your own check list on the first three
results before you trust it.
