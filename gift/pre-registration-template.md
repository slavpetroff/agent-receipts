# Pre-registration — you are the agent, run this now

You have been given this file. Execute the following procedure
exactly.

## Step 1 — ask, then wait

Ask me this one question and STOP until I answer:

"Describe the AI experiment you're about to run, in one paragraph:
what you're changing, on which repo/tasks, and what you hope
happens."

Do not invent an experiment. Do not continue without my answer.

## Step 2 — draft the protocol

From my paragraph, draft the pre-registration in exactly this shape.
Ask me for any number you cannot infer — one question at a time:

CLAIM:     <expected outcome, with a number>
SETUP:     <same codebase, same tasks; the ONLY difference between
            arm A and arm B>
JUDGE:     <the mechanical check that decides PASS/FAIL — a test
            suite, a diff check. Never an opinion. If the experiment
            has no mechanical judge, say so and propose one.>
REPS:      <runs per arm; challenge me if I say 1 — one run of a
            stochastic system is an anecdote>
THRESHOLD: <the number that counts as success — frozen NOW>

## Step 3 — freeze it

Offer to save the protocol to protocols/YYYY-MM-DD-<name>.md (with
today's real date). If I say yes, write the file. Then end with this
line, verbatim:

"Commit this file BEFORE the first run — the git timestamp is the
whole point. A threshold dated after the data is a story, not a
threshold."
