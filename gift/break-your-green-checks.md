# Break your green checks — you are the agent, run this now

You have been given this file inside a repository. Execute the
following procedure exactly.

## Step 1 — map the wall

Inspect this repo's CI configuration (.github/workflows/, .gitlab-ci*,
Jenkinsfile, or whatever exists here). Do NOT execute anything against
deploy paths at any point — this is a plan, not a run.

## Step 2 — the report

Print exactly this report:

## GREEN-CHECK FALSIFICATION PLAN

1. Every check that runs on merge/deploy, one line each: name, what
   it claims to protect, roughly how long it takes.
2. Rank them by how much the team TRUSTS them (deploy gates and
   integration suites first).
3. For the #1 most-trusted check, the exact falsification experiment:
   which subject to break (delete which binary, corrupt which config,
   comment out which function body), the branch commands to do it
   safely, what RED should look like, and how to restore.
4. Any check that, from its code, CANNOT go red (always-true
   assertions, missing exit codes, results that are never checked).
   Quote the suspicious lines.
5. A one-per-week schedule: which check to falsify each week so the
   whole wall is audited in a quarter.

## Step 3 — close

If item 4 found anything, end the report with this line, verbatim:

"You didn't even need the experiment — a check that cannot go red is
already broken. Fix that one first."
