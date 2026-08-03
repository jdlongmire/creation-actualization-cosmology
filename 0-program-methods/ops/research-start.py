#!/usr/bin/env python3
"""research-start — orientation briefing for a CAC research session.

Mirrors thinx's session-start and TRT's research-start: a fresh agent runs this and
gets everything needed to orient — VCS state, CI, traceability health, the
progressiveness ledger, the active PI, open problems, the appraisal verdict, and the
last session journal entry.

The progressiveness ledger is printed high in the briefing on purpose. It is the fact
about this programme most easily lost track of, and the one every session should be
oriented by.

Usage:  python3 0-program-methods/ops/research-start.py
Read-only. Never mutates the repo.
"""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run(cmd, **kw):
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=60, **kw)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except Exception as e:  # noqa: BLE001
        return 1, "", str(e)


def hdr(t):
    print("\n" + "=" * 68 + f"\n  {t}\n" + "=" * 68)


def main():
    print("=" * 68)
    print("  CAC research-start  |  orientation briefing")
    print("=" * 68)

    # --- Standing status ---
    hdr("[Standing status]")
    claims_json = ROOT / "traceability/generated/claims.json"
    if claims_json.exists():
        claims = json.loads(claims_json.read_text())
        preds = [c for c in claims.values() if c.get("role") == "prediction"]
        accs = [c for c in claims.values() if c.get("role") == "accommodation"]
        forbidding = [c for c in accs
                      if str(c.get("forbids") or "").strip().lower() not in
                      {"none", "nothing", "n/a", "-", ""}]
        print(f"  predictions: {len(preds)}   accommodations: {len(accs)} "
              f"({len(forbidding)} forbidding something)")
        if not preds and not forbidding:
            print("  >> UNAPPRAISED — zero novel content. The critical path is OPN-007")
            print("     (a discriminator). Belt work does not move this.")
    else:
        print("  (no generated claims.json — run traceability/scripts/build.py)")

    # --- VCS ---
    hdr("[VCS]")
    _, branch, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    _, porcelain, _ = run(["git", "status", "--porcelain"])
    clean = "clean" if not porcelain else f"{len(porcelain.splitlines())} uncommitted change(s)"
    print(f"  branch: {branch}   working tree: {clean}")
    _, ahead, _ = run(["git", "rev-list", "--count", "origin/main..HEAD"])
    _, behind, _ = run(["git", "rev-list", "--count", "HEAD..origin/main"])
    if ahead.isdigit() and int(ahead):
        print(f"  ! {ahead} commit(s) ahead of origin/main (unpushed)")
    if behind.isdigit() and int(behind):
        print(f"  ! {behind} commit(s) behind origin/main (pull)")
    _, log, _ = run(["git", "log", "-5", "--oneline"])
    print("  recent commits:")
    for ln in log.splitlines():
        print(f"    {ln}")

    # --- CI ---
    hdr("[CI]")
    rc, ci, _ = run(["gh", "run", "list", "--limit", "1",
                     "--json", "status,conclusion,displayTitle",
                     "--jq", r'.[0] | "\(.status)/\(.conclusion) — \(.displayTitle)"'])
    print(f"  latest: {ci if rc == 0 and ci else 'unknown (gh unavailable)'}")

    # --- Traceability ---
    hdr("[Traceability]")
    rc, out, err = run(["python3", "traceability/scripts/build.py"])
    for ln in (out.splitlines() + err.splitlines()):
        if any(k in ln for k in ("claims", "verified", "graph", "validation",
                                 "error", "progressiveness")):
            print(f"  {ln}")
    print(f"  build.py exit: {rc} ({'OK' if rc == 0 else 'FAILING'})")

    # --- Active PI ---
    hdr("[Active PI]")
    pis = sorted((ROOT / "0-program-methods/pi-planning").glob("PI-*.md"))
    if pis:
        latest = pis[-1]
        ms = latest.stem.replace("PI-0", "PI-")
        print(f"  plan: {latest.relative_to(ROOT)}")
        rc, issues, _ = run(["gh", "issue", "list", "--milestone", ms, "--state", "open",
                             "--json", "number,title", "--jq", r'.[] | "    #\(.number) \(.title)"'])
        print(f"  open issues on {ms}:")
        print(issues if rc == 0 and issues else "    (none / gh unavailable)")
    else:
        print("  no PI plan found")

    # --- Open problems ---
    hdr("[Open problems]")
    opn = sorted((ROOT / "traceability/claims").glob("OPN-*.yaml"))
    print(f"  registry: {len(opn)} OPN-* claims "
          "(see traceability/generated/open-problems.md)")
    print("  critical path: OPN-007 (discriminator)")
    print("  sharpest exposure: OPN-010 (processes observed in transit)")
    rc, active, _ = run(["gh", "issue", "list", "--label", "open-problem", "--state", "open",
                         "--json", "number,title", "--jq", r'.[] | "    #\(.number) \(.title)"'])
    print("  active (label:open-problem):")
    print(active if rc == 0 and active else "    (none / gh unavailable)")

    # --- Appraisal ---
    hdr("[Appraisal]")
    appraisal = ROOT / "3-prediction/appraisal.md"
    if appraisal.exists():
        for ln in appraisal.read_text().splitlines():
            if ln.strip().startswith("**") and any(k in ln for k in
                                                   ("nappraised", "rogressive", "egenerating")):
                print(f"  {ln.strip()}")
                break

    # --- Residuals ---
    hdr("[Residuals]")
    vs = ROOT / "references/verification-status.md"
    if vs.exists():
        rem = "Remaining" in vs.read_text()
        print(f"  references: "
              f"{'residual items remain (see verification-status.md)' if rem else 'all verified'}")

    # --- Last session journal ---
    hdr("[Last session]")
    sess = sorted(s for s in (ROOT / "0-program-methods/sessions").glob("*.md")
                  if s.name.lower() != "readme.md")
    if sess:
        last = sess[-1]
        print(f"  {last.relative_to(ROOT)}")
        grab = False
        for ln in last.read_text().splitlines():
            if ln.lower().startswith("## carry"):
                grab = True
            if grab:
                print(f"    {ln}")
    else:
        print("  (no session journal yet)")

    print("\n" + "=" * 68)
    print("  Ready. Read deeper as the task demands (ROADMAP, methodology, claims).")
    print("=" * 68)


if __name__ == "__main__":
    main()
