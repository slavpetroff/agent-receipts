#!/usr/bin/env python3
"""layers_check.py — структурният ICM валидатор (v1, 2026-08-26).

Проверява ТРИСЛОЙНАТА ICM архитектура (workspace-blueprint канона)
+ нашите шимове и persistence добавката. Отделен от icm_check.py
(R1-R9 проверяват граматиката НА файловете; това проверява СЛОЕВЕТЕ).

Правила:
  L1  root CLAUDE.md е КАРТА: съществува, ≤200 реда, носи дърво
      (``` фенс) и naming/placement секции, НЕ носи закони
      (STOP/ЗАКОН заглавия = 0).
  L2  root CONTEXT.md е РУТЕР: съществува, ≤90 реда, носи routing
      таблица (≥3 реда с ≥3 колони, една от които What-else/You'll
      Also Need по смисъл).
  L3  всеки workspace (top-level папка извън exclusions) има CONTEXT.md.
  SHIM root AGENTS.md съществува, реферира CLAUDE.md И CONTEXT.md,
      ≤15 реда; workspace AGENTS.md (ако има) реферира своя CONTEXT.md.
  SPINE (persistence добавката; --require-spine) docs/spine.md
      съществува И root CONTEXT.md го реферира.
  SKILLS (мек, warn) рутерът вплита поне един скил (`/име` или
      'skill' в таблицата).

Изход: PASS/FAIL по правило + exit 0/1. Детерминистичен, офлайн.
Употреба: python3 tools/icm/layers_check.py --repo . [--exclude X]...
          [--require-spine]
"""
import argparse
import re
import sys
from pathlib import Path

DEFAULT_EXCLUDES = {
    ".git", ".agents", ".worktrees", ".claude", ".playwright-mcp",
    ".serena", ".codegraph", "os", "node_modules", "__pycache__",
    ".venv", ".orpheus",
}


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def check(repo: Path, extra_excludes: list[str], require_spine: bool):
    ex = DEFAULT_EXCLUDES | set(extra_excludes)
    results: list[tuple[str, bool, str]] = []

    def add(rule: str, ok: bool, msg: str):
        results.append((rule, ok, msg))

    # L1 — the map
    cm = repo / "CLAUDE.md"
    s = read(cm)
    lines = s.splitlines()
    if not s:
        add("L1", False, "root CLAUDE.md липсва")
    else:
        ok_len = len(lines) <= 200
        ok_tree = "```" in s
        ok_nam = bool(re.search(r"(?i)(naming|конвенц|placement|именув)", s))
        law_hits = len(re.findall(r"(?im)^#+.*(STOP|ЗАКОН|LAW)\b", s))
        ok_nolaw = law_hits == 0
        add("L1", ok_len and ok_tree and ok_nam and ok_nolaw,
            f"CLAUDE.md: {len(lines)} реда (≤200:{ok_len}) · дърво:{ok_tree} · "
            f"naming:{ok_nam} · закони в картата:{law_hits} (трябва 0)")

    # L2 — the router
    cx = repo / "CONTEXT.md"
    s = read(cx)
    if not s:
        add("L2", False, "root CONTEXT.md ЛИПСВА — рутерният слой не съществува")
    else:
        rows = [l for l in s.splitlines() if l.strip().startswith("|")
                and l.count("|") >= 4 and "---" not in l]
        ok_tab = len(rows) >= 4  # header + ≥3 data rows
        ok_len = len(s.splitlines()) <= 90
        add("L2", ok_tab and ok_len,
            f"CONTEXT.md: {len(s.splitlines())} реда (≤90:{ok_len}) · "
            f"routing редове с ≥3 колони: {max(0, len(rows)-1)} (≥3:{ok_tab})")

    # L3 — workspace entry points
    # gitignored dirs are runtime, not workspaces (blago install, 26.08)
    import subprocess
    def _ignored(d: Path) -> bool:
        try:
            r = subprocess.run(["git", "-C", str(repo), "check-ignore", "-q",
                                str(d.relative_to(repo))], capture_output=True)
            return r.returncode == 0
        except OSError:
            return False
    missing = []
    workspaces = []
    for d in sorted(repo.iterdir()):
        if not d.is_dir() or d.name in ex or d.name.startswith("."):
            continue
        if d.is_symlink() or _ignored(d):
            continue
        workspaces.append(d.name)
        if not (d / "CONTEXT.md").exists():
            missing.append(d.name)
    add("L3", not missing,
        f"workspaces: {len(workspaces)} · без CONTEXT.md: {missing or 'нула'}")

    # SHIM — cross-vendor entry
    am = repo / "AGENTS.md"
    s = read(am)
    if not s:
        add("SHIM", False, "root AGENTS.md липсва (кросвендорният шим)")
    else:
        ok_refs = "CLAUDE.md" in s and "CONTEXT.md" in s
        ok_len = len(s.splitlines()) <= 15
        add("SHIM", ok_refs and ok_len,
            f"AGENTS.md: {len(s.splitlines())} реда (≤15:{ok_len}) · "
            f"сочи карта+рутер:{ok_refs}")
    ws_shim_bad = []
    for w in workspaces:
        wa = repo / w / "AGENTS.md"
        if wa.exists():
            t = read(wa)
            if "CONTEXT.md" not in t or len(t.splitlines()) > 15:
                ws_shim_bad.append(w)
    add("SHIM-WS", not ws_shim_bad,
        f"workspace AGENTS.md шимове несинхронни/дебели: {ws_shim_bad or 'нула'}")

    # SPINE — persistence add-on
    if require_spine:
        sp = repo / "docs" / "spine.md"
        cx_s = read(cx)
        ok_sp = sp.exists() and "spine" in cx_s.lower()
        add("SPINE", ok_sp,
            f"docs/spine.md:{sp.exists()} · рутерът го реферира:"
            f"{'spine' in cx_s.lower()}")

    # SKILLS — woven into routing (warn-only)
    cx_s = read(cx)
    ok_sk = bool(re.search(r"(?i)(скил|skill|/[a-z][a-z-]{2,})", cx_s))
    add("SKILLS(warn)", ok_sk, "рутерът вплита скилове" if ok_sk
        else "рутерът не споменава нито един скил (warn)")

    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument("--require-spine", action="store_true")
    a = ap.parse_args()
    res = check(Path(a.repo).resolve(), a.exclude, a.require_spine)
    hard_fail = False
    for rule, ok, msg in res:
        tag = "PASS" if ok else ("WARN" if "warn" in rule.lower() else "FAIL")
        if tag == "FAIL":
            hard_fail = True
        print(f"[{tag}] {rule}: {msg}")
    print("\nПРИСЪДА:", "ЗЕЛЕНО — трислойната структура е налична"
          if not hard_fail else "ЧЕРВЕНО — ICM слоевете липсват/слети")
    sys.exit(1 if hard_fail else 0)


if __name__ == "__main__":
    main()
