---
name: frame
description: Interviews you about one job your company still does by hand, one question at a time, then writes how you do it (the steps, what done means, a good and a bad example, what you never want, your checks before it goes out) as a skill your AI follows on every run of that job. Use when you want AI to do a job your way, or when AI keeps giving generic work for a job.
---

You are helping me write down one job of my company the way I do it, so that you and any AI after you do it my way. Ask me one question at a time and wait for my answer before you go on; a follow-up question is its own turn too. Do not write any file unless I ask: print everything here.

- Ask me which job I still do by hand that I want AI to do, and what it produces at the end. Wait for my answer.
- Ask me to walk you through the last time I did it myself, start to finish. Wait for my answer.
- Write it back as numbered steps, one action each, and ask whether that is how I do it. Wait, and fix it by my answer.
- Ask me what a finished result must have so I would send it without touching it. Write it as three to five lines, each one I could check with a yes or a no, show them to me and ask whether they are right. Wait, and fix them by my answer.
- Ask me for one real example of a result I was happy with, and one I threw away and why. Wait for each.
- Ask me what I never want in it: words, tone, promises, guesses. Write them as a list. Wait, and fix it by my answer.
- Ask me what I check before it goes out, and what makes me stop it. Wait for my answer.
- Write it as a skill: a folder named after the job holding one SKILL.md, with a name (lowercase words joined by hyphens, like monthly-books) and a one-line description of when to use it at the top, then these parts in this order: what the job is for, the steps, what "done" means, the good example, the bad example and why, what I never want, what I check before it goes out. Print it whole.
- Ask me which AI I will run this job in: ChatGPT, Codex, Claude Code or Claude.ai. Wait for my answer, then give me only its steps, exactly these:
  - Claude Code: save the folder as ~/.claude/skills/<the job's name>/SKILL.md, start a new session, and type /<the job's name>.
  - Codex: save the folder as ~/.agents/skills/<the job's name>/SKILL.md, start Codex again, and type $<the job's name>.
  - Claude.ai: zip the folder, open Customize > Skills, click +, then Create skill, then Upload a skill, and choose the zip; code execution must be on in your settings. Then start a new chat and write: Use the <the job's name> skill.
  - ChatGPT: zip the folder, open Plugins in the sidebar, go to the Skills tab, click Create, then Upload from your computer, and choose the zip; skills are on Business, Enterprise, Healthcare and Edu plans. Then start a new chat and type @ to pick the skill.
  - Anything else, or a plan without skills: paste the same text at the start of every run of this job.
- Tell me to change a line the day I change my mind, and to run my check list on the first three results before I trust it.
