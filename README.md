# agent-receipts

Receipts for every number I publish about AI agents on real codebases.
Wins and losses. Nothing here is a benchmark marketing page — it is
the raw material: protocols committed BEFORE the runs, results as they
came out, and the run logs.

I'm Stanislav — 12 years of backend engineering, the last two building
businesses with AI agents doing most of the typing. I measure what
actually works. This repo is where "trust me" is replaced by "check
line N".

## The rules this repo lives by

1. **Protocol before run.** Every measurement protocol is written and
   committed before the first run it governs. Timestamps are the point.
2. **The table ships as it came out.** Losses included: you will find
   runs where the context layer made things WORSE (+13%, +21% on small
   repos) and a full fail-to-pass experiment where it did NOT pay
   (+7.5% under cheap iteration). Those stay published.
3. **Mechanical judges.** Verdicts come from oracles (tests, mechanical
   checks), not from opinions.
4. **Same base, same task, with/without.** Only measured pairs carry
   claims. Anecdotes don't.

## What's inside

- `protocols/` — the pre-registered measurement protocols. English
  translations of my Bulgarian working originals; the originals, with
  their pre-run commit timestamps, live in the working repo. Figures
  are verbatim.
- `results/` — result documents as they came out (translated from the
  Bulgarian originals; figures verbatim; internal strategy sections
  removed and marked in place). Client codebases are
  anonymized (client-A, client-B); open-source targets are named
  (egglog, sqlite-vector, dpi-detector, react-data-table-component,
  java_8_recipes, bizcity-twin-ai).
- `logs/` — raw A/B run logs (`ab-*.log`), tokens-used lines included.
  One disclosed redaction: the harness skill preamble (identical
  boilerplate printed in every run, both arms) is replaced by a marker —
  it is third-party text I don't republish. Everything else verbatim.
- `gift/` — the real 98-line context map from my production repo:
  `gift/CLAUDE.md` is the raw file itself (grab it), and
  `gift/the-real-98-line-map.md` adds the two checks and three rules
  for writing your own.

## The craft (tools you can run yourself)

- `craft/layers_check.py` — the structural 3-layer validator we used
  on ourselves (see `results/case-study-self-icm-migration.md`).
  Deterministic, offline: `python3 craft/layers_check.py --repo .`

## The headline numbers, with their receipts

| claim | receipt |
|---|---|
| 37-module codebase, 6 navigation tasks: map off 5/6 · 196k tokens → map on 6/6 · 147k (−24.8%) | `results/field-test-v2-RESULT.md` + `logs/field-test-v2/ab-bizcity-twin-ai-*` |
| Small repos: the map HURTS — +13% (sqlite-vector), +20.6% (dpi-detector) | `results/field-test-v1-RESULT.md` + `logs/field-test-v1/` |
| Cheap iteration: the layer did NOT pay — +7.5% cost per solved task, 36/36 cells | `results/v3-failtopass-RESULT.md` |
| Where routing pays: breadth ≥ ~10 areas, no cheap feedback loop | the pattern table in `results/field-test-v1-RESULT.md` |
| Fusing ICM layers costs 8.6× boot tax: 18,090 → 2,100 tokens/session after the 3-layer split (SELF-RUN, disclosed) | `results/case-study-self-icm-migration.md` + `craft/layers_check.py` |
| The same 3-layer split LOSES on one-shot navigation: +56.7% vs a flat thin catalog (the hop tax) — the consumption regime picks the architecture | `results/case-study-self-icm-migration.md` (the loss section) + `logs/field-test-v3/` |

If a number I post is not in here, call it out.
