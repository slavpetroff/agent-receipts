# v3 fail-to-pass — RESULT (2026-08-25): under ITERATION the layer does NOT pay

36/36 cells (6 tasks × 2 arms × 3 repetitions), client-A (PHP monolith,
35 packages), Codex iterating against live tests, judge = the oracle at
create-db, worker and judge under IDENTICAL conditions (one
materialization, one flag).

| | bare | layer |
|---|---|---|
| solved | **18/18** | **18/18** |
| tokens total | 1,086,660 | 1,168,228 |
| **cost per solved task** | **60,370** | 64,901 (**+7.5%**) |

Per task: the layer is slightly cheaper on C5 and R1, more expensive
on R3/R4/R5/R6. Spread: on R1 and C5 the layer TIGHTENS the
distribution (R1: 52–80k → 63–70k); elsewhere not consistently.

## The conclusion that carries weight

ITERATION REPLACES THE MAP. When the agent can bang against the
tests, the red tests themselves navigate it — the map has nothing to
add and its boot cost is pure tax. 36/36 solved also shows that
fail-to-pass with free iteration does not discriminate by success on
THESE tasks.

Against the full matrix: the layer wins where feedback is ABSENT —
navigation without an oracle (bizcity −24.8%, react-data-table −18%),
first-strike without tests (the blind R1 in the previous generation:
4/4 failures), and run-to-run consistency. It loses where the agent
can iterate cheaply.

[The internal strategy section is removed from the public version.]
