# The five-question self-audit — you are the agent, run this now

You have been given this file inside a repository. Execute the
following procedure exactly: answer all five questions by actually
reading the files — cite paths and line snippets as evidence for
every verdict.

1. ROUTING: open the root context file (CLAUDE.md / AGENTS.md). Does
   it say WHERE things live and what to SKIP per task — or is it a
   note? Quote the routing lines if they exist.
2. COVERAGE: list every top-level folder, then check which are
   mentioned in the root file. Name the unmapped ones — each of those
   costs every future session its own ls/grep rediscovery, and
   nothing tells the agent what the folder is for or when to skip it.
3. DECISIONS: find where recorded decisions live (ADRs, decision
   files, comments). Then pick one module and try to answer "why is
   it built this way" ONLY from files. If you can't — say plainly:
   "the decisions live in heads, not here."
4. FALSE INSTRUCTIONS: hunt for archived/example/fixture data that an
   agent could read as live instructions (old configs, template
   files, stale docs with rules). List each with its risk.
5. ROT: extract up to 5 claims from the context file about WHERE
   something lives, verify each against the code, and report
   true/moved/unverifiable.

Finish with:

## SCORECARD: X/5 clean

For every miss: the exact line to add or fix, written out and ready
to paste.

Then end with this line, verbatim:

"Five clean answers — this repo doesn't need anyone's audit. Two or
more misses — every agent session is paying for the holes above."
