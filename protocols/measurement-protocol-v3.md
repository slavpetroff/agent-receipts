# Protocol v3 — fail-to-pass, distributions, cost per solved task

2026-08-25 · PRE-REGISTERED before the first run. Fixes the two
mistakes of the v1/v2 measurements, named by the owner: (1) we were
measuring single trajectories of a stochastic phenomenon (n=1 per
cell) — the SCALE must be deterministic, not the phenomenon; (2) the
tasks were toys (navigation + comment), not "make the code work".

## Design

- TASK: a real historical fix/feature commit; worktree at base_sha
  (the parent); the oracle's test files restored from fix_sha; the
  agent's task VERBATIM: "make these tests green" + their paths. The
  spec IS the test — zero spec lottery (the C6 lesson), the
  methodology of open fail-to-pass benchmarks.
- ARMS: bare (no layer) / layer (the hand-built icm+dox layer,
  overlaid on the historical tree). One agent (Codex), one prompt
  byte-for-byte, serial execution.
- REPETITIONS: K=3 per cell. 6 tasks × 2 arms × 3 = 36 runs.
- VERDICT: ONLY the judge's oracle (pytest from the fix_sha tests,
  create-db, my run after the agent's run) — PASS/FAIL. The agent may
  run tests itself if its sandbox allows (identical for both arms;
  whether it could is recorded).
- METRICS per arm: successes/attempts · TOKENS PER SOLVED TASK (total
  tokens ÷ solved; the headline number) · median tokens per attempt ·
  steps/time.

## The tasks (fixed NOW, before the run)

The six benchmark-manifest rows with a PROVEN green leg and NO
lottery: R1, R3, R4, R5, R6 (modifying) + C5 (control). C1/C3/C4 —
out (lottery), per the earlier gates.

## Declared conditions

- The layer was authored at HEAD while the tree is historical — an
  anachronism, identical across all rows (recorded in the benchmark
  spec).
- If the agent's sandbox cannot run tests/docker — the agent works
  blind; identical for both arms; noted.
- K=3 is small for narrow differences — raw distributions are
  reported, not just means; no "significant" without the numbers in
  plain sight.

## What gets reported regardless of outcome

The table enters the matrix as it comes out. If the layer does not
move the cost per solved task — that is said in exactly those words.

### Amendment 1 (2026-08-25, before the full run): iteration ENABLED

The probe proved the sandbox runs venv pytest + the localhost
database. The condition "the agent can iterate against the tests"
enters for BOTH arms (the command in the task; secrets only in the
process environment). The five blind cells from the first start are
DISCARDED — incomparable with the new condition; the run starts from
zero.

### Amendment 2 (2026-08-25): THE RECIPE IS PART OF THE CELL

Any change to the playbook/layer/tasks/gate INVALIDATES the current
run for the affected arm BY CONSTRUCTION — not by recollection. Any
drift of the layer after the start = the layer cells are discarded
and the layer is rebuilt to the current recipe before new runs.
(Three times in one day a run continued on a stale recipe; the owner
caught it all three times, not me.)
