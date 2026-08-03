#!/usr/bin/env python3
"""research-wrap — end-of-session hygiene gate for the CAC research repo.

Mirrors thinx's session-wrap: a pass/fail gate run at the session transition. Don't
claim a session done if any check FAILs.

Beyond the usual repo housekeeping this gate carries one programme-specific check:
the **honest-status check**. It re-derives the progressiveness ledger from the claim
registry and compares it against what the appraisal log says, so the programme cannot
drift into describing itself as further along than the ledger supports.

Usage:  python3 0-program-methods/ops/research-wrap.py
Exit code is nonzero if any gate check FAILs.
"""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDS_NOTHING = {"none", "nothing", "n/a", "-", ""}
results = []  # (level, label, detail)


def run(cmd, shell=False):
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=120, shell=shell)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except Exception as e:  # noqa: BLE001
        return 1, "", str(e)


def add(level, label, detail=""):
    results.append((level, label, detail))


def main():
    print("=" * 68)
    print("  CAC research-wrap  |  session hygiene gate")
    print("=" * 68)

    # 1. Working tree clean
    _, porc, _ = run(["git", "status", "--porcelain"])
    if porc:
        add("FAIL", "uncommitted changes",
            f"{len(porc.splitlines())} file(s) — commit before wrapping:\n    "
            + "\n    ".join(porc.splitlines()[:20]))
    else:
        add("PASS", "working tree clean")

    # 2. Unpushed commits
    _, ahead, _ = run(["git", "rev-list", "--count", "origin/main..HEAD"])
    if ahead.isdigit() and int(ahead):
        add("WARN", "unpushed commits", f"{ahead} commit(s) ahead of origin/main — push if intended")
    else:
        add("PASS", "synced with origin/main")

    # 3. Traceability: build passes + generated fresh
    rc, out, err = run(["python3", "traceability/scripts/build.py"])
    blob = out + err
    if rc == 0 and "ACYCLIC" in blob and "validation: OK" in blob:
        add("PASS", "traceability", "validation OK, dependency graph acyclic")
    else:
        add("FAIL", "traceability", f"build.py exit {rc}")
    _, gen_dirty, _ = run(["git", "status", "--porcelain", "traceability/generated"])
    if gen_dirty:
        add("FAIL", "generated reports stale",
            "build.py changed traceability/generated — commit the refresh")
    else:
        add("PASS", "generated reports fresh")

    # 4. Honest-status check — the ledger vs what the appraisal claims
    claims_json = ROOT / "traceability/generated/claims.json"
    appraisal = ROOT / "3-prediction/appraisal.md"
    if claims_json.exists() and appraisal.exists():
        claims = json.loads(claims_json.read_text())
        n_pred = sum(1 for c in claims.values() if c.get("role") == "prediction")
        n_forbid = sum(1 for c in claims.values()
                       if c.get("role") == "accommodation"
                       and str(c.get("forbids") or "").strip().lower() not in FORBIDS_NOTHING)
        text = appraisal.read_text()
        says_unappraised = "Unappraised" in text or "UNAPPRAISED" in text
        novel = n_pred + n_forbid
        if novel == 0 and not says_unappraised:
            add("FAIL", "honest status",
                "ledger shows 0 novel-content claims but the appraisal log does not say "
                "unappraised — the status has been rounded up")
        elif novel > 0 and says_unappraised:
            add("WARN", "honest status",
                f"{novel} novel-content claim(s) exist but the appraisal still reads "
                "unappraised — update the log and its verdict")
        else:
            add("PASS", "honest status",
                f"appraisal consistent with the ledger ({n_pred} prediction(s), "
                f"{n_forbid} forbidding accommodation(s))")
    else:
        add("WARN", "honest status", "claims.json or appraisal.md missing")

    # 5. Accommodation hygiene — every ACC must price its rival
    if claims_json.exists():
        claims = json.loads(claims_json.read_text())
        thin = [cid for cid, c in claims.items()
                if c.get("role") == "accommodation" and not c.get("rival_account")]
        if thin:
            add("FAIL", "accommodation hygiene",
                "missing rival_account: " + ", ".join(sorted(thin)))
        else:
            add("PASS", "accommodation hygiene", "every accommodation prices its rival")

    # 6. GitHub-safe LaTeX (math-lint)
    rc, hits, _ = run(r"grep -rn '\operatorname' --include='*.md' . | grep -v '`' || true",
                      shell=True)
    if hits.strip():
        add("FAIL", "math-lint (\\operatorname)",
            "use \\mathrm:\n    " + "\n    ".join(hits.splitlines()[:10]))
    else:
        add("PASS", "math-lint", "no \\operatorname in committed math")

    # --- Session journal reminder ---
    _, recent, _ = run("git log -1 --since='12 hours ago' --name-only --pretty=format: "
                       "-- 0-program-methods/sessions || true", shell=True)
    if recent.strip():
        add("PASS", "session journal", "entry touched recently")
    else:
        add("WARN", "session journal",
            "append a session entry to 0-program-methods/sessions/ before wrapping")

    # --- Report ---
    print()
    icon = {"PASS": "+", "WARN": "!", "FAIL": "x", "INFO": "."}
    for level, label, detail in results:
        print(f"  [{icon[level]}] {level:4} {label}" + (f" — {detail}" if detail else ""))

    fails = [r for r in results if r[0] == "FAIL"]
    warns = [r for r in results if r[0] == "WARN"]
    print("\n" + "=" * 68)
    if fails:
        print(f"  RESULT: FAIL — {len(fails)} blocking issue(s), {len(warns)} warning(s). Not wrapped.")
        print("=" * 68)
        return 1
    print(f"  RESULT: PASS — {len(warns)} warning(s). Safe to wrap.")
    print("  Then: append the session journal + update the appraisal log as needed.")
    print("=" * 68)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
