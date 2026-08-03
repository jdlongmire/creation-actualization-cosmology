# GitHub Workflow

Agile-DevOps mechanics for the programme. The methodology decides *what* counts as
progress; this file decides *how* work is tracked.

## The unit of iteration is a problemshift

An iteration is not a time-box filled with tasks. It is **one attempt to resolve one
open problem**, with its success and failure conditions stated before it starts. It
closes when the problem is decided — either way. A recorded refutation closes an
iteration successfully.

## Mapping

| Concept | GitHub |
|---|---|
| Programme increment (PI) | **Milestone** (`PI-1`, `PI-2`, ...), planned in [`pi-planning/`](pi-planning/) |
| Open problem, active subset | **Issue** with `label:open-problem`, carrying `Tracks: OPN-id` in the body |
| Falsifiability tier | **Label** `tier-0` … `tier-3` |
| Claim role | **Label** `hard-core`, `belt`, `accommodation`, `prediction` |
| A change to the programme | **PR**, judged by the [change-legitimacy criterion](METHODOLOGY.md) |
| Validation | **Actions** — traceability build, acyclic gate, fresh reports, math-lint |

The `OPN-*` claims are the canonical open-problem registry; issues track only what is
actively being worked. An issue without a `Tracks:` line is a task, not a problem.

## PR expectations

- Claim files updated alongside prose, `build.py` run, generated reports committed.
- The PR body states which category of the change-legitimacy criterion the change falls
  under. "Progressive because it records a refutation" is a complete and good answer.
- A PR that adds an accommodation states its `forbids` and `rival_account` in the body,
  not only in the YAML, so review can see them without opening the file.

## Labels that carry meaning

- `open-problem` — the active subset of the OPN registry
- `critical-path` — reserved for work on [OPN-007](../traceability/claims/OPN-007.yaml)
- `degeneration-watch` — flags a change that risks reducing falsifiable content; requires
  an explicit note in the appraisal log whether or not the change is merged
- `red-team` — adversarial review, archived under [`../reviews/`](../reviews/)

## Session lifecycle

```bash
python3 0-program-methods/ops/research-start.py    # orient
python3 0-program-methods/ops/research-wrap.py     # gate, then append a session journal entry
```

`research-wrap.py` is a pass/fail gate. Do not claim a session done if any check FAILs.
Its **honest-status check** compares the appraisal log against the generated ledger, so
the programme cannot describe itself as further along than the registry supports.
