# Pending — awaiting explicit authorization

The CI workflow for this repository is staged here rather than installed. Installing it
writes to a harness-floor protected surface (morals.md hard-stops: *Modify CI/CD
pipelines*), which requires JD's explicit per-edit authorization.

## To install

With JD's explicit go-ahead for this specific edit:

```bash
python3 <thinx>/means/scripts/set-override-marker.py --reason "install CAC CI workflow"
# then copy ci.yml into the workflows directory and commit
```

## What it gates

| Job | Check |
|---|---|
| `traceability` | Claim schema valid, dependency graph acyclic, generated reports fresh |
| `honest-status` | The appraisal log's verdict matches the progressiveness ledger |
| `accommodation-hygiene` | Every `role: accommodation` claim states `forbids` and `rival_account` |
| `math-lint` | No `\operatorname` in committed math (GitHub's renderer rejects it) |

`honest-status` is the one worth having. It is a machine check that the programme has not
started describing itself as further along than its own registry supports — the failure
mode a programme of this kind is most likely to reach for, and the one least likely to be
noticed from inside.

Both checked scripts (`../honest_status_check.py`, `../accommodation_hygiene_check.py`)
are already installed and are run locally by `research-wrap.py`, so the gate is live at
the session boundary even before CI is installed. Installing CI moves it from
self-discipline to enforcement.
