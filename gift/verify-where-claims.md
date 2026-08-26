# Verify your WHERE-claims — you are the agent, run this now

You have been given this file inside a repository. Execute the
following procedure exactly. Do not edit any file — report only.

1. Read every CLAUDE.md / AGENTS.md file in this repo.
2. Extract every sentence that claims WHERE something lives ("auth is
   handled in X", "config lives in Y", "Z is done in module W").
3. For each claim, open the named place and decide: is it the OWNER
   of that behavior, or just a CALLER of the real owner? Follow the
   code one level down if needed.
4. Print the table:
   | claim | verdict (TRUE / CALLER-NOT-OWNER / MOVED / UNVERIFIABLE) | evidence (path:line) |
5. For every non-TRUE row: write the corrected sentence, ready to
   paste into the context file.
6. End with a date-stamp line for the top of the context file, and
   the one number that matters, printed as its own line:

"N of this map's WHERE-claims were wrong. A confident map that lies
is worse than no map — agents don't double-check it."
