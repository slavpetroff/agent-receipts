# Move your memory into the project. You are the agent, run this now.

You are the agent on this person's machine, working in the project
folder you were opened in. Run the steps below in order. Two steps
ask a question: ask it, then STOP until the person answers.

Three things hold for the whole run:

- The memory folder is only read. You never change, move or delete
  a file in it.
- You write nothing before the person says yes in Step 7.
- An existing `AGENTS.md`, `CLAUDE.md` or `rules/*.md` keeps every
  line it has. You only add lines.

## Step 1. Find the memory

1. Take the absolute path of the project folder. Turn every character
   that is not a letter or a digit into `-`. Example:
   `/Users/ana/my.shop` becomes `-Users-ana-my-shop`. Call it the
   folder name.
2. The memory is in `~/.claude/projects/<folder name>/memory/`.
   If that folder is missing, list `~/.claude/projects/` and take the
   one entry that ends with the project's folder name. If there is no
   such entry, or more than one, print the entries and ask which one
   is this project, then STOP until the answer.
3. If the memory folder holds no file other than `MEMORY.md`, print
   "This project has no memory in Claude Code. Nothing to move." and
   stop.
4. Read every file in it except `MEMORY.md` (that file is only the
   index). For each file, note its name, its line count, what it says
   in one short line, and its type if its header gives one (`user`,
   `feedback`, `project`, `reference`).

## Step 2. Compare with the project

1. Read the project's instruction files that exist: `AGENTS.md`,
   `CLAUDE.md`, every file in `rules/`, and every file these point to
   by path.
2. For each memory, decide: does the project already state the same
   rule, in any words? Search the whole project for the memory's most
   distinctive words and read what the search finds. Mark each memory
   **in the project** (name the file) or **only in memory**. When
   unsure, mark it only in memory.
3. Mark these memories, and never propose to move them without the
   person's word:
   - **personal**: it is about the person, not about the project
     (type `user`, or it describes who they are). A project folder is
     often shared with other people.
   - **secret**: it holds a password, a key, a token or a private
     address. Never copy this text anywhere, not even into your
     answer. Show only its name.
   - **dated**: it records the state of work on a date (type
     `project`). It can be out of date already.

## Step 3. The size check

Add up the line counts of the memories that are only in memory. If
the total is 20 lines or fewer, go to Step 4.

If the total is more than 20 lines, work out what these lines would
cost if every one of them went into `AGENTS.md`. Every request an
agent sends in this project carries `AGENTS.md` again, so the cost
grows with every request, and the person does not see it.

1. Tokens: the characters of these memories divided by 4. This is a
   rough count; say so.
2. The history is in `~/.claude/projects/<folder name>/`. Each
   `*.jsonl` file directly in it is one session. Each file in
   `<session id>/subagents/` is one agent that session started. Take
   only the files changed in the last 30 days.
3. In those files, every line with `"type":"assistant"` has a
   `requestId` and a `message.model`. Count the distinct `requestId`
   values for each model. That is the number of requests. Skip the
   model `<synthetic>`. Also count the sessions and the agents.
4. Prices, US dollars per million tokens, from Anthropic's price page
   as of June 2026. Match a model by the start of its name, and ignore
   a `[1m]` ending or a date ending.

   | model starts with | input | cached read |
   |---|---|---|
   | `claude-fable-5-1` | 10.00 | 0.25 |
   | `claude-fable-5` | 10.00 | 1.00 |
   | `claude-opus-5-5` | 4.00 | 0.20 |
   | `claude-opus-5`, `claude-opus-4`, `opus` | 5.00 | 0.50 |
   | `claude-sonnet-5`, `sonnet` | 2.00 | 0.20 |
   | `claude-sonnet-4` | 3.00 | 0.30 |
   | `claude-haiku-4-5`, `haiku` | 1.00 | 0.10 |

   For a model that is not in the table, use the highest row
   (10.00 and 1.00) and say that you did.
5. The cost for the last 30 days:
   - each request reads the lines from the cache:
     tokens × requests × cached read price
   - each session and each agent first writes them to the cache, at
     up to twice the input price: tokens × (sessions + agents) × 2 ×
     input price

   Add both parts over all models, and divide by 1 000 000.
6. Print:

```
These N memories are <lines> lines, about <tokens> tokens.
Last 30 days in this project: <sessions> sessions, <agents> agents, <requests> requests.
In AGENTS.md they would cost up to $<cost> a month at this pace, before any work starts.
```

   Then print these notes:
   - The number is a top limit. The cache often bills repeated loads
     for less.
   - On a subscription plan there is no bill. The same tokens make
     the plan's usage limit arrive sooner.
   - Only rules that every task needs go into `AGENTS.md`. The other
     rules go into topic files that an agent opens only when the task
     needs them, so they cost much less.
   - Other tools (for example Codex) keep their own history. Their
     requests are not in this count.

   If the history has no session files, print "No history to measure
   the cost from." and do not guess a number.

## Step 4. Show the list, ask, then wait

Print:

```
Only in memory (N):
  1. <name> (<lines> lines) — <one line>   [personal] [dated] [secret]
  2. ...
Already in the project (M):
  <name> (in <file>), ...
```

Ask and STOP:

"Which should I move into the project? Say the numbers, all, or none."

`all` never includes a memory marked personal or secret; name
those and ask about them one by one. If the answer is none, print
"Nothing moved. The memory folder was not changed." and stop.

## Step 5. Rewrite, do not paste

Lines copied one by one from memory make a list that contradicts
itself and repeats itself. Turn the chosen memories into rules:

1. Group them by theme, two to six themes, named in the project's
   own words (for example `writing`, `clients`, `releases`).
2. Inside a theme, merge memories that say the same thing into one
   rule. When two memories conflict, keep both, mark the conflict,
   and let the person choose in Step 7.
3. Write each rule as one instruction to an agent, one or two short
   sentences, then one line that starts with `Why:`. Keep every
   number, file name, command and name exactly. Drop dates, the story
   of how the rule was learned, and notes about one session.
4. Place each rule:
   - **always**, when every task in this project needs it. It goes
     into `AGENTS.md`.
   - **when needed**, when only tasks about its theme need it. It goes
     into `rules/<theme>.md`.
   Keep the always-rules few. When unsure, choose when needed.

## Step 6. Prepare the files

- `AGENTS.md` at the project root. If it does not exist, create it.
  If it exists, add these sections at its end:

```
## Rules for every task
- <rule>
  Why: <reason>

## Open the rules for your task
| when the task touches | read |
|---|---|
| <theme, in plain words> | rules/<theme>.md |
```

  The table is the map of the rules. An agent reads the map, then
  opens only the file its task needs. If `AGENTS.md` already has such
  a table, add rows to it instead.
- `rules/<theme>.md` for each theme with when-needed rules: a title
  line, then its rules in the same form. If the file exists, add the
  rules at its end.
- `CLAUDE.md` at the project root. Claude Code reads `CLAUDE.md`;
  Codex and most other tools read `AGENTS.md`. This line makes them
  read the same rules. If `CLAUDE.md` does not exist, create it with
  the single line `@AGENTS.md`. If it exists and does not mention
  `AGENTS.md`, add the line `@AGENTS.md` at its end.

## Step 7. Show the plan, ask, then wait

Print, for each file, whether you will create it or change it, and
the full text you will add. Under each rule, print the memory text it
came from, so the person can compare. Print every conflict from
Step 5 with both versions.

Then count the lines `AGENTS.md` will have after the change. If it is
more than 20 lines and Step 3 gave a cost, repeat the cost for the
always-rules only.

Ask and STOP:

"Write these files? Say yes, no, or what to change."

On a change, apply it, print the plan again and ask again. On no,
print "Nothing written. The memory folder was not changed." and stop.
Write only on yes.

## Step 8. Write and report

Write the files exactly as shown in Step 7. Then print:

```
Created: <files>
Changed: <files>, only lines added
Moved: N memories, as K rules
  AGENTS.md: <k> rules, <lines> lines in the file
  rules/<theme>.md: <k> rules          (one line per file)
Not moved: M (already in the project, or not chosen)
Cost of AGENTS.md: up to $<cost> a month at the last 30 days' pace   (only if Step 3 ran)
The memory folder was not changed.
```

Then print, as one line:

"The moved memories still sit in ~/.claude/projects/<folder name>/memory/. Delete them there when you are ready; the rules now live in the project, where any agent that opens it reads them."
