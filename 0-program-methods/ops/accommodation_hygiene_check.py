#!/usr/bin/env python3
"""Accommodation hygiene — every accommodation states what it forbids and how the
rival handles the same observation.

`forbids: none` is a legitimate and expected answer. The check is not that an
accommodation forbids something; it is that the programme has *said* whether it does,
and has stated the rival's account at its strongest (research-practices.md #6). An
accommodation without its rival is not assessable.

Run by CI and by research-wrap.py.
Exit code is nonzero if any accommodation is missing either field.
"""
from __future__ import annotations
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    bad = []
    n = 0
    for p in sorted((ROOT / "traceability/claims").glob("*.yaml")):
        c = yaml.safe_load(p.read_text())
        if c.get("role") != "accommodation":
            continue
        n += 1
        for field in ("forbids", "rival_account"):
            if not c.get(field):
                bad.append(f"{c['id']}: missing '{field}'")
    if bad:
        for b in bad:
            print(f"::error::{b}", file=sys.stderr)
        return 1
    print(f"OK — {n} accommodation(s), each stating what it forbids and how the rival "
          "handles the same observation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
