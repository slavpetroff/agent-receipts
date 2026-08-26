# Case study: we audited our own context layer against the ICM canon — and failed

**Disclaimer, up front: this is a SELF-RUN case study.** Same operator,
same repo, no external client. We publish it because the method is the
point — and because the numbers were measured the same way we measure
everything else: validator committed before the fix, verdicts
mechanical, receipts below. Treat it as a worked example, not as
third-party proof.

## The setup

Our own business repo carried a context layer we had built and sold
by. A structural audit against the ICM 3-layer canon (map / router /
workspace entry points) found the layers FUSED: one always-loaded
182-line root file carrying map + router + laws + strategy, zero
router files anywhere, no per-workspace entry points.

Worse: our own checkers passed it green — they had been calibrated on
our deviation. The judge couldn't go red.

## The method (TDD on a context layer)

1. Wrote a structural validator (`craft/layers_check.py` — in this
   repo, run it on your own repo) and committed it BEFORE any fix.
2. Ran it: **6 FAIL** — the red proof of the gap.
3. Migrated: pure map (59 lines) · router file · entry points in all
   7 workspaces with input/output handoffs · thin cross-vendor shims ·
   the decided-things file loaded on demand instead of always.
4. Ran it again: **7/7 PASS.**

## The numbers

| metric | before | after |
|---|---|---|
| Always-loaded boot tax | ~18,090 tokens/session | **2,100 tokens (÷8.6)** |
| Structural validator | 6 FAIL | 7/7 PASS |
| Decision-recall (fresh agent, own decisions) | 8/9 | preserved — probe PASSED via the new layers, including catching a stale premise in the question itself |

The boot number alone: at 10 agent sessions/day per engineer, the
fused layer was charging ~160k tokens/day/engineer before any work
happened. The funnel fixed that by construction, not by discipline.

## The installer run on two more of our repos (same day)

The rearmed installer + gate migrated two more of our own repos
(branch-only, content preserved, validator green on both):

| repo | validator | auto-loaded context (before → after) |
|---|---|---|
| business repo A (3 workspaces) | 7/7 PASS | 1,255 → 1,043 tokens (1.2×) |
| business repo B (6 workspaces, 22 task routes) | 7/7 PASS | 11,158 → 8,259 tokens (1.4×) |

The honest pattern — and it matches our navigation matrix: **the
benefit scales with how fused and fat the root was.** Our worst
offender (everything in one always-loaded file) gained 8.6×; a repo
that was already reasonably split gained 1.2×. If your root context
file is thin and routes properly, this migration buys you structure,
not tokens — and we'd tell you that before you pay for anything.

## The loss that came with it (published the same day)

We then measured the SAME 3-layer split on one-shot navigation runs
(same 6 tasks, same agent, same judge as our earlier A/B):

| arm | correct | tokens |
|---|---|---|
| flat thin catalog (v1) | 6/6 | 147,467 |
| fat catalog (v2) | 6/6 | 174k |
| **3-layer split (v3)** | 6/6 | **231,032 (+56.7% vs v1)** |

The mechanism, visible in the logs: the hop tax. A one-shot agent
swallows a flat 95-line catalog in one read; the 3-layer split makes
it pay shim → map → router → workspace on every task.

We then tried to rescue the split with a discipline arm (v3.1): the
SAME structure plus one hard rule in every router file — "read ONLY
the files this table names, then stop reading". Result: 6/6 correct,
231k → 190,970 tokens (overhead 1.33× → 1.10×; the structure itself
costs only ~1.5% over flat). It recovered HALF the gap — and still
FAILED our pre-registered threshold by 970 tokens (0.5%). Thresholds
are frozen before runs precisely so a near-miss stays a miss. One
honest correction from this arm: our earlier "wandering evidence"
list came from a regex over log MENTIONS, not actual reads — the
real gain is shorter trajectories, and we've corrected the record.

**So the two-regime law, measured — and it survived a rescue
attempt:** always-loaded interactive
sessions → the 3-layer split wins (8.6× boot cut). One-shot batch
runs → the flat thin catalog wins (+56.7% against the split). The
architecture must match how your agents actually consume the layer —
and anyone selling you one shape for both regimes hasn't measured.

## The honest limits

- Self-run: the operator who built the layer also fixed it.
- One repo (three more are being migrated through the installer now —
  their numbers will be appended here as they land).
- Boot-tax pricing depends on your model's input price; recompute
  with yours.

## Run it on yourself

`python3 craft/layers_check.py --repo /path/to/your/repo`
— deterministic, offline, exits red or green. If it's red, the fix
is the same one we did: split the map from the router, give every
workspace an entry point, make everything else load on demand.
