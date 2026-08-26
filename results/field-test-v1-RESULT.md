# Field test v1 — RESULT: FAILS its own pre-registered criteria

Date: 2026-08-25 · 5 external repos · 5 installs + 60 A/B runs, all
Codex · mechanical verdict · criteria fixed BEFORE repo selection.

## The numbers

| repo | verdict/forecast | correct org→inst | tokens Δ |
|---|---|---|---|
| egglog (Rust, 2605 commits) | sick / ≥25% | 5/6 → 5/6 | **−3.2%** ✗ |
| react-data-table (TS, 1017) | sick / ≥25% | 6/6 → 6/6 | **−18.1%** ✗ (under the bar) |
| java_8_recipes (Java, 486) | HEALTHY / <10% | 5/6 → 4/6 | **−0.3%** ✓ CONTROL CALLED IT |
| sqlite-vector (C, 230) | sick / ≥25% | 6/6 → 6/6 | **+13.0%** ✗✗ WORSE |
| dpi-detector (Py, 166) | sick / ≥25% | 6/6 → 6/6 | **+20.6%** ✗✗ WORSE |

Registered threshold: ≥3 of the sick repos at ≥25%. Achieved: **0 of 4.**
VERDICT: FAILS.

## What survived

- T2 (installer without us in the loop): **5/5 PASS** with content
  preservation — incl. Codex fixing its own two losses after the new
  gate check. The delivery machine works.
- T4 (healthy control): java_8_recipes −0.3% — the qualifier called
  the healthy repo correctly. No false positive on HEALTHY.
- The gate grew: defect #10 (dropped content) caught and plugged.

## Why it failed — the sharpened law from EIGHT repos

The effect correlates with STRUCTURAL BREADTH, not with layer presence:

| repo | packages/areas | effect |
|---|---|---|
| client-A (PHP monolith, 35 packages) | 35 packages | −38% per delivered change, fail→pass |
| client-B (web platform) | multi-app monorepo | −25…−32% |
| react-data-table | monorepo (apps+src) | −18% |
| our-product-repo | 14 crates, ALREADY routed | +14% (restructuring hurts) |
| egglog | 1 crate + helpers | −3% |
| java_8_recipes | flat | −0.3% |
| sqlite-vector | effectively 1 C file | +13% (the map costs more than the territory) |
| dpi-detector | 4 files | +21% |

ROUTING PAYS WHERE THERE IS SOMETHING TO ROUTE. Under ~10 areas the
layer is pure tax: a small repo is swept in seconds and the map only
adds reading. Qualifier v1 confused "no layer" with "sick" — sickness
also requires SCALE.

## What changes

1. Qualifier v2: sick = (no/thin/bloated layer) AND (breadth ≥ ~10
   areas / multi-package structure). Under v2, sqlite-vector and
   dpi-detector are rejected at intake — as is our-product-repo.
2. The test measured outside the population where the effect lives:
   the field five, picked by stars, are small OSS libraries — not
   team-scale multi-package codebases. That is a lesson about the
   selection rule, not an excuse: the rule carried no breadth.
3. Before any client use: a second field test ONLY on
   breadth-qualified repos (≥10 areas). Only if THAT passes does the
   number get shown to a buyer.

## Limits of the test itself

6 tasks/repo · one-line navigation tasks · one vendor (Codex) · the
small-repo tasks are trivial by construction (everything is one grep
away) — which is exactly the mechanism of the sharpened law.
