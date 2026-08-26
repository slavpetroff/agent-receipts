# Protocol: decision-recall dose probe v1 (self-test 1)

2026-08-26 · PRE-REGISTERED before the run. Phenomenon:
decision-recall of a fresh agent through OUR OWN workspaces (we are
our own first client).

## Design

- **Domains:** 3 of our businesses/"departments".
- **Wave 1 (canon):** one extractor agent per domain reads the
  decision records and living plan and returns 3 pairs of {question,
  canonical answer, file} — REAL decisions, not trivia. Questions are
  phrased the way a new team member would ask.
- **Wave 2 (the probe):** one FRESH agent per question (9 total), cwd
  = the domain root, instruction: "follow the repo's context layer
  and answer; cite the file". The fresh agent never sees the
  canonical answer or which file holds it.
- **Verdict (fixed now):** PASS = the decision's key assertion is
  present + the source found · PARTIAL = right direction, a key
  constraint missed · FAIL = wrong/invented/not found. Headline
  number: PASS / total. PARTIAL counts as non-PASS.
- Judge: me, against the canon pairs; verdicts written line by line
  in the report (hand-checkable).

## Declared limits

- n=9 is small — this is a DOSE PROBE, not a benchmark; reported as
  such.
- No bare arm: the phenomenon is "does the layer route a fresh agent
  to the decided thing", not "layer vs no layer" (that is a different
  protocol).
- Extractor and probe are different agents; no contamination through
  shared context — wave 2 receives only the question.
- The result is reported regardless of outcome (failure included).
