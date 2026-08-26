# Field test v2 — RESULT: FAILS even under the breadth rule

2026-08-25 · 5 broad repos · 5 installs (PASS 5/5 first try, incl.
preservation) + 60 A/B Codex runs · thresholds from the protocol.

| repo | verdict/forecast | correct org→inst | tokens Δ |
|---|---|---|---|
| bizcity-twin-ai (PHP, 37 layers) | sick / ≥25% | 5/6 → 6/6 | **−24.8%** — a hair under the bar, with +1 correct |
| librefang — CONTROL | healthy-routed / <10% | 6/6 → 6/6 | **−5.2%** ✓ control called it AGAIN |
| MoviePilot (64 plugins) | sick / ≥25% | 6/6 → 6/6 | **+22.1%** ✗✗ worse |
| kyo (Scala, 20+ modules) | sick / ≥25% | 6/6 → 5/6 | −12.0% ✗ and −1 correct |
| dimos | sick / ≥25% | 6/6 → 6/6 | +3.6% ✗ |

Threshold: ≥3 of 4 sick repos at ≥25%. Achieved: 0 (bizcity at −24.8
is CLOSEST, but a bar is a bar). VERDICT: FAILS.

Judge correction, disclosed: the primary count gave bizcity org 0/6 —
a judge defect (the repo dirties 14 files by itself and "exactly one
file edited" exploded). Re-judged excluding the constant noise (files
appearing in ≥5 of 6 diffs). Codex had been hitting the targets.

## What THIRTEEN repos now say

Big wins appear only in the COMBINATION: broad + no/bloated layer +
NON-OBVIOUS names (client-A −38% and fail→pass; client-B −25/−32%;
bizcity −25%). Otherwise: thin wins (kyo −12), zeros (dimos, java),
or harm (MoviePilot +22 — a plugin collection with obvious names;
the mini-repos +13/+21; our-product-repo +14 on top of a healthy
layer). The controls called it BOTH times (java −0.3%, librefang
−5.2%) — the qualifier is reliable for "healthy", unreliable for
"how sick".

The honest epistemic bottom line: a static scan does NOT predict
effect size. A per-codebase number can only come from a measured
trial on that codebase — never from a promised percentage.
[An internal go-to-market paragraph is removed from the public
version; the epistemic conclusion above is kept in full.]

## The installer grew, indisputably

v1: 2/5 with content losses → gate + preservation → v2: 5/5 clean on
first try. Delivery without our hands is stable. The problem is not
delivery — it is PREDICTING the effect.
