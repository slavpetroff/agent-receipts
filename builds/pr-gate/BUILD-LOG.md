# PR Gate — build log (public receipt)

One agent ran the build. Protocol frozen before the first line of
code; judge set authored independently by a second agent from a
different model family. Times are real, defects included.

| ts (2026-08-28) | actor | entry |
|---|---|---|
| 01:50 | builder | repo init, terrain check |
| 01:58 | builder | gate v0 written: review contract (no finding without a verbatim rule quote), bundle collector, output validator, two-CLI runner |
| 02:00 | judge author | dispatched independently: 12 seeded violations (4 types × 3) + 6 clean patches + manifest |
| 02:12 | builder | first live smoke: seeded rename CAUGHT, same-commit law quoted verbatim (38s). Two fixes shipped: mention-scan, --no-renames |
| 09:35 | builder | DEFECT, logged honestly: judge author hung 7.5h on an interactive prompt in a background run. Killed, relaunched correctly |
| afternoon | builder | judge set accepted (18/18 patches apply clean) · bench run twice |

## The bench (frozen thresholds; verdict as it fell)

- Catches: 11/12 raw — 11/11 valid (seed #12 disputed with evidence:
  no written rule exists for what it seeds; the gate's silence is
  contract-correct)
- Clean PRs: 0 false alarms
- Determinism: catch-level stable across runs; type labels wobble —
  **RED against our own frozen threshold.** Fix queued (type derived
  from the rule-source path in code, not by the model). We publish
  the red instead of renaming the threshold.
- Fuel: not yet captured by the runner — unmeasured, so unclaimed.
