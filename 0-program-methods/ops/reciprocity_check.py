#!/usr/bin/env python3
"""Reciprocity check — CAC measured by its own instrument.

PRD-001 predicts that a historical programme with wrong boundary conditions will
accumulate explanatory burden as precision improves. Methodological reciprocity means
CAC submits to the same measure, and a thesis that measures the rival while exempting
its author is a rhetorical device rather than a claim.

This reports CAC's own burden vector — the analogue of HEBI H1-H3 — on every build:
total claims, open problems, and how much of the registry forbids anything. It is
ADVISORY and always exits 0. A programme in its first week has no meaningful trajectory,
and a gate that fails during stand-up teaches you to ignore it. What makes it useful is
that the number is printed in the same place the programme asks the rival's to be.

Run by CI and by research-wrap.py.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDS_NOTHING = {"none", "nothing", "n/a", "-", ""}

# Burden per unit of content. Above this, the programme is adding auxiliary structure
# faster than it is adding anything that could be wrong. Advisory only.
BURDEN_RATIO_WATCH = 20.0


def main() -> int:
    claims = json.loads((ROOT / "traceability/generated/claims.json").read_text())

    total = len(claims)
    opens = [c for c in claims.values() if c.get("role") == "open"]
    preds = [c for c in claims.values() if c.get("role") == "prediction"]
    forbidding_acc = [c for c in claims.values()
                      if c.get("role") == "accommodation"
                      and str(c.get("forbids") or "").strip().lower() not in FORBIDS_NOTHING]
    content = len(preds) + len(forbidding_acc)

    print("CAC measured by its own instrument (PRD-001 methodological reciprocity)")
    print(f"  claims total ............ {total}")
    print(f"  open problems ........... {len(opens)}")
    print(f"  predictions ............. {len(preds)}")
    print(f"  forbidding accommodations {len(forbidding_acc)}")

    if content == 0:
        print("  burden ratio ............ undefined (0 claims forbid anything)")
        print("  ADVISORY: the programme currently accumulates structure and forbids "
              "nothing. Under its own thesis this is the signature it attributes to a "
              "framework with wrong boundary conditions. Stand-up is a legitimate "
              "excuse; it expires.")
        return 0

    ratio = total / content
    print(f"  burden ratio ............ {ratio:.1f} claims per forbidding claim")
    if ratio > BURDEN_RATIO_WATCH:
        print(f"  ADVISORY: above the {BURDEN_RATIO_WATCH:.0f} watch line. Auxiliary "
              "structure is outgrowing content. Not a failure; a reading the programme "
              "asked to have taken.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
