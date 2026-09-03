# Count the homes — you are the agent, run this now

You have been given this file inside a repository. Execute the
procedure exactly. Report only. Do not edit, move or delete any file.

## Step 1 — ask, then wait

Ask me this and STOP until I answer:

"Which folder holds the context files your agents and people read
(context files, conventions, playbooks, runbooks)? Give me the path,
or say 'whole repo'."

Do not guess. Do not continue without the answer.

## Step 2 — find the facts that travel

Read the context files under that path (CLAUDE.md, AGENTS.md,
CONTEXT.md, README, docs, playbooks, any markdown that instructs).
Collect candidate FACTS: short statements that appear, in the same
or slightly different words, in more than one file. Typical classes:
a command (how to run tests, deploy, lint), a rule (naming, branch,
review), a number (a limit, a price, a version), a definition (what
a stage or a role is), a path (where something lives).

For each candidate, search the whole path with grep for its
distinctive words (the command itself, the number, the rule's key
phrase) and count the FILES that state it, not mentions.

## Step 3 — the table

Print a table sorted by homes, most first:

| fact (quote it once, exactly) | homes | files |

Below it print:
- the worst number (most homes one fact has);
- for every fact with 3+ homes: which single file should be its
  home (the one the others already point to, or the one closest to
  the decision), and the list of files that should become a pointer
  to it;
- any two files that are the same fact in two registers (a plain
  version and a formal one) and would become one.

## Step 4 — the honest close

If the worst number is 2, print this line verbatim:

"Two homes is normal. Nothing to merge here; the grep was the whole
exercise."

If it is 3 or more, end with the merge list and this line:

"Merge by hand, one fact at a time, and read the diff before you
commit. Do not build a generator to keep copies in sync; delete the
copies."
