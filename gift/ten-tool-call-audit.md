# Ten-tool-call audit — you are the agent, run this now

You have been given this file inside a repository. Execute the
following procedure exactly.

## Step 1 — ask, then wait

Ask me this one question and STOP until I answer:

"Give me one small real task to do in this repo — something from
your actual backlog, 15-30 minutes of work. For example: 'add a
rate-limit check to the password reset endpoint, matching how we do
it elsewhere.' What's the task?"

Do not invent a task yourself. Do not continue without my answer.

## Step 2 — do the task, log yourself

Do the task I gave you. While you work, keep a numbered log of every
tool call you make, in order, starting from the first one.

## Step 3 — the report

When the task is done, or after your 15th tool call, whichever comes
first, STOP working and print exactly this report:

## TOOL-CALL AUDIT

1. The first ten tool calls, in order. For each: the tool, what I was
   looking for or doing, and a label — SEARCHING (grep/find/ls/
   opening a file just to orient myself) or WORKING (editing, running,
   writing).
2. The ratio: N searching out of 10, and the verdict:
   - 0-3 searching = healthy (I knew where things live)
   - 4-7 = guessing (the context layer has holes)
   - 8-10 = lost (I was rediscovering the codebase)
3. For every SEARCHING call: what specific knowledge would have made
   it unnecessary (a routing line, a documented decision, a folder
   description). List these as "missing context lines" — the exact
   sentences this repo's CLAUDE.md / AGENTS.md should contain, ready
   to paste.
4. An honest estimate of tokens spent searching vs working in this
   session, and what that costs at $3 per million input tokens.

Be blunt. If the repo's context made you fast, say so. If this repo
is small (under ~10 modules), say plainly that grep covers it in
seconds and the audit found nothing wrong — that is a valid result.

End the report with this line, verbatim:

"Write the ratio down with today's date — that's your baseline for
any fix you try."
