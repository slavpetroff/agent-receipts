# Weigh your context backpack — you are the agent, run this now

You have been given this file inside a repository. Execute the
following procedure exactly. Report only — don't edit anything.

## Step 1 — ask, then wait

Ask me these two questions and STOP until I answer both:

"Two numbers for the bill: roughly how many agent sessions does your
team run per day (all people combined), and how many people are on
the team?"

Do not guess these numbers. Do not continue without my answer.

## Step 2 — weigh and price

1. Find every context file that auto-loads in this repo: the root
   CLAUDE.md / AGENTS.md plus the per-folder ones an agent hits when
   it enters those folders. List them with sizes in bytes.
2. Compute the boot weight: total bytes ÷ 4 ≈ tokens loaded on EVERY
   session before any work happens.
3. Price it with my numbers:
   tokens × sessions/day × 22 days × $3/M = monthly boot bill.
   Print the formula with the real values filled in.
4. Read the files line by line and list the 10 heaviest offenders:
   lines that restate what a linter already enforces, describe what
   filenames already say ("utils has utilities"), or that nobody
   would miss. Quote each with its file.
5. Verdict on the scale: under ~5k tokens = fine · 5-15k = every line
   must earn its place · over 15k = paying rent on prose.

## Step 3 — close

If this repo is small (under ~10 modules), end with this line,
verbatim:

"An empty backpack is correct here — under ~10 modules a map costs
more than it saves. Don't add one because a post told you to."
