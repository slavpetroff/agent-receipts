# The pickup line — you are the agent, run this now

You have been given this file inside a repository. Execute the
procedure exactly. Report only. Do not edit, create or delete any
file, and do not run any build or test.

## Step 1 — ask, then wait

Ask me this and STOP until I answer:

"Which folder holds the staged or multi-step agent work you want
checked (a pipeline, a workflow, a workspace)? Give me the path."

Do not guess. Do not continue without the path.

## Step 2 — find where the state lives

Inside that folder:

1. List the files an agent reads first: the root context file
   (CLAUDE.md, AGENTS.md or equivalent) and any file that names
   stages, steps or phases.
2. List every file whose name or first line says where things stand
   right now: RUN, STATUS, STATE, PROGRESS, TODO, NEXT, a checklist
   with ticks, a log with a last entry. Quote the exact line that
   carries the current position, with its file path.
3. For each stage or step, say whether its output is a FILE on disk
   (name it) or exists only in a chat, a terminal, or someone's head.

## Step 3 — the cold pickup, simulated

Pretend you were just started fresh in this folder with the single
instruction "Continue the work in progress" and nothing else. Using
only what you found in step 2, write in one paragraph what you would
do first, and name the exact stage or step you would start at. Be
honest: if the folder does not say what is in progress, say that
you would look for something useful to do and describe what that
would be (improving scripts, refactoring, adding tests).

## Step 4 — verdict

Print exactly one of these two lines, then the reason in one sentence:

CONTINUE — a written line of intent exists at <path>, and a fresh
agent would resume at <stage>.

BUILD — no written line says what is in progress and what comes
next; a fresh agent would start improving the tooling instead.

If the verdict is BUILD, print the one sentence that would flip it
to CONTINUE, written in this repo's own terms (which work item,
which range or scope, what is done, what comes next), and the path
where that sentence should live so every stage reads it. Do not
write it into the repo. I will.
