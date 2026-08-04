#!/usr/bin/env python3
"""Honest-status check — the appraisal log must match the progressiveness ledger.

The programme's most likely failure is not a false claim; it is a true claim described
as further along than it is. This check re-derives the ledger from the claim registry
and refuses a state where the registry shows zero novel content but the appraisal log
has stopped saying so.

Run by CI and by research-wrap.py.
Exit code is nonzero on mismatch.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDS_NOTHING = {"none", "nothing", "n/a", "-", ""}


def main() -> int:
    claims = json.loads((ROOT / "traceability/generated/claims.json").read_text())
    text = (ROOT / "3-prediction/appraisal.md").read_text()

    preds = [c for c in claims.values() if c.get("role") == "prediction"]
    forbidding = [c for c in claims.values()
                  if c.get("role") == "accommodation"
                  and str(c.get("forbids") or "").strip().lower() not in FORBIDS_NOTHING]
    novel = len(preds) + len(forbidding)
    says_unappraised = "nappraised" in text or "UNAPPRAISED" in text

    if novel == 0 and not says_unappraised:
        print("::error::ledger shows 0 novel-content claims but the appraisal log does "
              "not say unappraised — the status has been rounded up", file=sys.stderr)
        return 1

    # Once novel content exists, the appraisal must ADDRESS it by id. A substring test
    # for "unappraised" cannot do this job: "empirically unappraised, one theoretically
    # progressive step" is the honest verdict for a programme with a prediction and no
    # corroboration, and the old check flagged exactly that correct state.
    missing = sorted(c["id"] for c in preds + forbidding if c["id"] not in text)
    if missing:
        print(f"::error::novel-content claim(s) {', '.join(missing)} are not named in "
              "the appraisal log — content exists that the standing verdict does not "
              "account for", file=sys.stderr)
        return 1

    print(f"OK — {len(preds)} prediction(s), {len(forbidding)} forbidding "
          f"accommodation(s); appraisal consistent with the ledger")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
