#!/usr/bin/env python3
"""CAC traceability build.

Loads traceability/claims/*.yaml, validates them, checks the dependency graph is
acyclic (the circularity discipline), and emits generated reports: claims.json,
coverage-report.md, dependency-graph.{mmd,json}, risk-report.md, open-problems.md,
progressiveness-report.md.

Adapted from the TRT build with one substantive addition: the Lakatosian
progressiveness ledger. Accommodations (post-hoc handling of already-known facts)
are counted separately from predictions, and an accommodation that forbids nothing
is reported as non-progressive. See 0-program-methods/METHODOLOGY.md, Divergence 2.

Usage:  python3 traceability/scripts/build.py
Exit code is nonzero if validation fails (suitable for CI).
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CLAIMS_DIR = ROOT / "traceability" / "claims"
GEN_DIR = ROOT / "traceability" / "generated"

ID_PREFIXES = {"CRE", "HER", "PHY", "ACC", "PRD", "OPN", "EXT"}
REQUIRED = ["id", "name", "statement", "tier", "role", "proof_status", "epistemic_status"]
ROLES = {"primitive", "bridge", "derived", "imported", "accommodation", "prediction", "open"}
PROOF_ORDER = ["verified", "imported", "axiomatized", "prose_only", "open"]
EPI_ORDER = ["established", "argued", "conjectured", "open"]
TIER_NAME = {0: "strategy", 1: "hypothesis (hard core)", 2: "theory (belt)", 3: "prediction"}

# An accommodation whose `forbids` is one of these forbids nothing, and so
# contributes nothing to progressiveness. Recorded, not hidden.
FORBIDS_NOTHING = {"none", "nothing", "n/a", "-", ""}


def cell(s) -> str:
    """Escape a value for use inside a markdown table cell."""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def load_claims() -> dict:
    claims = {}
    for p in sorted(CLAIMS_DIR.glob("*.yaml")):
        with p.open() as f:
            c = yaml.safe_load(f)
        c["_file"] = p.name
        claims[c["id"]] = c
    return claims


def forbids_something(c: dict) -> bool:
    return str(c.get("forbids") or "").strip().lower() not in FORBIDS_NOTHING


def validate(claims: dict) -> list[str]:
    errs = []
    for cid, c in claims.items():
        for field in REQUIRED:
            if field not in c or c[field] in (None, ""):
                errs.append(f"{cid}: missing required field '{field}'")
        if cid.split("-")[0] not in ID_PREFIXES:
            errs.append(f"{cid}: unknown id prefix")
        if c.get("role") not in ROLES:
            errs.append(f"{cid}: unknown role '{c.get('role')}'")
        # predictions must state a Popperian refutation condition
        if c.get("role") == "prediction" and not c.get("falsifies"):
            errs.append(f"{cid}: role=prediction but no 'falsifies' (Popperian) field")
        # accommodations must state what they forbid, even when the answer is "none"
        if c.get("role") == "accommodation":
            if not c.get("forbids"):
                errs.append(f"{cid}: role=accommodation but no 'forbids' field "
                            "(state what it rules out, or the literal string 'none')")
            if not c.get("rival_account"):
                errs.append(f"{cid}: role=accommodation but no 'rival_account' field "
                            "(state how standard cosmology handles the same observation)")
        # dangling dependency refs
        for dep in c.get("depends_on") or []:
            ref = dep.get("claim_id")
            if ref not in claims:
                errs.append(f"{cid}: depends_on dangling ref '{ref}'")
        # computational artifact files must exist
        for art in (c.get("formal_artifacts") or {}).get("computation", []):
            if not (ROOT / art["notebook"]).exists():
                errs.append(f"{cid}: computation artifact missing: {art['notebook']}")
    return errs


def find_cycles(claims: dict) -> list[list[str]]:
    """DFS cycle detection over depends_on edges (must be acyclic)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {cid: WHITE for cid in claims}
    cycles, stack = [], []

    def dfs(u):
        color[u] = GRAY
        stack.append(u)
        for dep in claims[u].get("depends_on") or []:
            v = dep.get("claim_id")
            if v not in claims:
                continue
            if color[v] == GRAY:
                cycles.append(stack[stack.index(v):] + [v])
            elif color[v] == WHITE:
                dfs(v)
        stack.pop()
        color[u] = BLACK

    for cid in claims:
        if color[cid] == WHITE:
            dfs(cid)
    return cycles


def counts(claims: dict, key: str, order: list[str] | None = None) -> list[tuple[str, int]]:
    tally: dict = {}
    for c in claims.values():
        tally[c.get(key)] = tally.get(c.get(key), 0) + 1
    return sorted(tally.items(),
                  key=lambda kv: (order.index(kv[0]) if order and kv[0] in order else 99, str(kv[0])))


def write_claims_json(claims: dict):
    out = {cid: {k: v for k, v in c.items() if k != "_file"} for cid, c in claims.items()}
    (GEN_DIR / "claims.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")


def write_coverage(claims: dict):
    lines = ["# Coverage Report", "",
             "*Generated by `traceability/scripts/build.py` — do not edit by hand.*", "",
             f"**Total claims: {len(claims)}**", ""]
    for title, key, order in [("By tier", "tier", None), ("By role", "role", None),
                              ("By proof status", "proof_status", PROOF_ORDER),
                              ("By epistemic status", "epistemic_status", EPI_ORDER)]:
        lines += [f"## {title}", ""]
        for k, n in counts(claims, key, order):
            label = f"{k} — {TIER_NAME[k]}" if key == "tier" else str(k)
            lines.append(f"- **{label}**: {n}")
        lines.append("")
    lines += ["## All claims", "", "| ID | Tier | Role | Proof | Epistemic | Name |",
              "|---|---|---|---|---|---|"]
    for cid in sorted(claims):
        c = claims[cid]
        lines.append(f"| {cid} | {c['tier']} | {c['role']} | {c['proof_status']} | "
                     f"{c['epistemic_status']} | {cell(c['name'])} |")
    lines.append("")
    (GEN_DIR / "coverage-report.md").write_text("\n".join(lines))


def write_depgraph(claims: dict):
    edges = []
    for cid, c in claims.items():
        for dep in c.get("depends_on") or []:
            edges.append({"from": cid, "to": dep.get("claim_id"), "type": dep.get("dependency_type")})
    (GEN_DIR / "dependency-graph.json").write_text(
        json.dumps({"nodes": sorted(claims), "edges": edges}, indent=2) + "\n")
    mmd = ["graph TD"]
    for cid in sorted(claims):
        c = claims[cid]
        mmd.append(f'  {cid}["{cid}<br/>{c["role"]}/{c["proof_status"]}"]')
    for e in edges:
        mmd.append(f'  {e["from"]} --> {e["to"]}')
    (GEN_DIR / "dependency-graph.mmd").write_text("\n".join(mmd) + "\n")


def write_risk(claims: dict):
    lines = ["# Risk Report", "",
             "*Generated — failure conditions and Popperian refutation conditions.*", "",
             "## Predictions (`falsifies`)", "", "| ID | Name | Refuted if |", "|---|---|---|"]
    preds = sorted(c for c in claims if claims[c].get("role") == "prediction")
    if preds:
        for cid in preds:
            c = claims[cid]
            lines.append(f"| {cid} | {cell(c['name'])} | {cell(c.get('falsifies') or '')} |")
    else:
        lines.append("| — | *(no predictions stated)* | — |")
    lines += ["", "## All failure conditions (`risk_if_false`)", "",
              "| ID | Tier | Risk if false |", "|---|---|---|"]
    for cid in sorted(claims):
        c = claims[cid]
        r = cell(c.get("risk_if_false") or "")
        if r:
            lines.append(f"| {cid} | {c['tier']} | {r} |")
    lines.append("")
    (GEN_DIR / "risk-report.md").write_text("\n".join(lines))


def write_open_problems(claims: dict):
    """Generated view of the OPN-* claims, which are the canonical registry."""
    opn = sorted(c for c in claims if claims[c].get("role") == "open")
    lines = ["# Open Problems (generated)", "",
             "*Generated by `traceability/scripts/build.py` from the `OPN-*` claims — "
             "do not edit by hand.*", "",
             "The `OPN-*` traceability claims are the **canonical registry** of open problems. "
             "GitHub **Issues** track the *active subset* — filter `label:open-problem`. "
             "Each such issue carries `Tracks: OPN-id`.", "",
             "| ID | Tier | Confidence | Problem | Depends on |", "|---|---|---|---|---|"]
    for cid in opn:
        c = claims[cid]
        deps = ", ".join(d.get("claim_id", "") for d in (c.get("depends_on") or [])) or "—"
        lines.append(f"| {cid} | {c['tier']} | {c['epistemic_status']} | {cell(c['name'])} | {deps} |")
    lines += ["", "## Statements & failure conditions", ""]
    for cid in opn:
        c = claims[cid]
        lines += [f"### {cid} — {c['name']}", "", cell(c.get("statement") or "")]
        if c.get("risk_if_false"):
            lines += ["", f"*Risk if false:* {cell(c['risk_if_false'])}"]
        lines.append("")
    (GEN_DIR / "open-problems.md").write_text("\n".join(lines) + "\n")


def write_progressiveness(claims: dict):
    """The Lakatosian ledger — the report the programme is least comfortable with.

    Accommodation of a known fact contributes nothing to progressiveness however
    elegant it is. Printing the ratio on every build is the cheapest defence
    against mistaking accumulated accommodation for advance.
    """
    accs = sorted(c for c in claims if claims[c].get("role") == "accommodation")
    preds = sorted(c for c in claims if claims[c].get("role") == "prediction")
    acc_forbidding = [c for c in accs if forbids_something(claims[c])]
    novel = len(preds) + len(acc_forbidding)

    if not preds and not acc_forbidding:
        verdict = ("**UNAPPRAISED — no novel content.** Every claim currently either belongs to "
                   "the hard core, supports it, or accommodates an already-known fact. On "
                   "Lakatos's criterion the programme has not yet begun to be progressive, and "
                   "no accumulation of further accommodation will change that.")
    elif not preds:
        verdict = (f"**UNAPPRAISED — {len(acc_forbidding)} accommodation(s) forbid something and "
                   "are candidates for promotion to `role: prediction`.** Promote them: an "
                   "accommodation that forbids something is a prediction that has not been "
                   "written down as one.")
    else:
        verdict = (f"**{len(preds)} prediction(s) stated.** Progressive status still requires that "
                   "a *novel* fact be predicted and corroborated — see the appraisal log for "
                   "which, if any, have been.")

    lines = ["# Progressiveness Report (generated)", "",
             "*Generated by `traceability/scripts/build.py` — do not edit by hand.*", "",
             "> Lakatos: a programme is **progressive** if it predicts novel facts and some "
             "corroborate; **degenerating** if it only accommodates facts post hoc. This report "
             "separates the two so the programme cannot confuse them. See "
             "[METHODOLOGY.md](../../0-program-methods/METHODOLOGY.md) Divergence 2.", "",
             "## Ledger", "",
             "| Category | Count |", "|---|---|",
             f"| Predictions (`role: prediction`, carry `falsifies`) | **{len(preds)}** |",
             f"| Accommodations (`role: accommodation`) | {len(accs)} |",
             f"| — of which forbid something | {len(acc_forbidding)} |",
             f"| — of which forbid nothing (non-progressive) | {len(accs) - len(acc_forbidding)} |",
             f"| **Novel-content claims** (predictions + forbidding accommodations) | **{novel}** |",
             "", "## Verdict", "", verdict, "",
             "## Accommodations in detail", "",
             "| ID | Name | Forbids | Rival account |", "|---|---|---|---|"]
    for cid in accs:
        c = claims[cid]
        f = c.get("forbids") or ""
        mark = "" if forbids_something(c) else " *(non-progressive)*"
        lines.append(f"| {cid} | {cell(c['name'])} | {cell(f)}{mark} | {cell(c.get('rival_account') or '—')} |")
    lines.append("")
    (GEN_DIR / "progressiveness-report.md").write_text("\n".join(lines))
    return len(preds), len(accs), len(acc_forbidding)


def main() -> int:
    GEN_DIR.mkdir(parents=True, exist_ok=True)
    claims = load_claims()
    errs = validate(claims)
    cycles = find_cycles(claims)
    for cyc in cycles:
        errs.append(f"CIRCULARITY: dependency cycle {' -> '.join(cyc)}")

    write_claims_json(claims)
    write_coverage(claims)
    write_depgraph(claims)
    write_risk(claims)
    write_open_problems(claims)
    n_pred, n_acc, n_acc_forbid = write_progressiveness(claims)

    n_open = sum(1 for c in claims.values() if c.get("role") == "open")
    print(f"loaded {len(claims)} claims ({n_open} open problems); "
          f"generated 6 reports in {GEN_DIR.relative_to(ROOT)}/")
    verified = sum(1 for c in claims.values() if c["proof_status"] == "verified")
    print(f"  proof_status=verified: {verified}/{len(claims)}")
    print(f"  progressiveness: {n_pred} prediction(s), {n_acc} accommodation(s) "
          f"({n_acc_forbid} forbidding something)")
    print(f"  dependency graph: {'ACYCLIC' if not cycles else 'HAS CYCLES'}")
    if errs:
        print(f"\n{len(errs)} validation error(s):", file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("validation: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
