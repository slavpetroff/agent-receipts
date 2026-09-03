# Count the pockets — you are the agent, run this now

You have been given this file on a developer's machine. Execute the
procedure exactly. Report only. Do not edit, move or delete any file.

## Step 1 — ask, then wait

Ask me this and STOP until I answer:

"Which repository should I check? Give me the path, or say 'the
current one'."

Do not guess. Do not continue without the answer.

## Step 2 — find every pocket on this machine

Look for the places where coding harnesses keep what they learned
about how this person works. Check each of these; skip silently the
ones that do not exist:

- Claude Code: `~/.claude/projects/*/memory/` (one folder per project)
  and `~/.claude/CLAUDE.md`
- Codex: `~/.codex/memories*` (files or a sqlite database) and
  `~/.codex/AGENTS.md`
- Gemini: `~/.gemini/`
- Cursor: `.cursor/rules/` inside the repository
- GitHub Copilot: `.github/copilot-instructions.md` inside the repository
- Any other folder under the home directory named memory, memories or
  rules that belongs to an AI tool

For each pocket found, count its entries (files, or rows if it is a
database you can read).

## Step 3 — the rules for THIS repository

Find the pocket that belongs to the chosen repository (for Claude
Code the project folder name is the repository path with slashes
turned into dashes). List every entry's title or first line. These
are the rules the agent believes are in force here.

## Step 4 — the two checks

For every rule, take its three most distinctive words and search the
repository with grep. Count how many rules are stated anywhere in
the repository.

Then check whether any pocket is under version control:
`git ls-files` in the repository, filtered for the pocket paths.

## Step 5 — the report

Print exactly this block, with the numbers filled in:

```
Pockets on this machine: <harness>: <entries> · <harness>: <entries> · ...
Rules the agent keeps for <repo name>: N
  · <title 1>
  · <title 2>
  · ... (up to ten, then "and K more")
Stated in the repository (grep):   X of N
Under version control (git):       Y of N
```

## Step 6 — the honest close

If N is 0, print this line verbatim:

"No pocket for this repository yet. Nothing evaporates on the next
change; come back after a month of sessions."

Otherwise print the count once more and end with this question,
verbatim, and nothing after it:

"Which of these N rules do you believe are in force today, on a
different harness or a different laptop?"
