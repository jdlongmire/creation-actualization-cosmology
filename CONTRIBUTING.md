# Contributing

The programme is governed by the progressive/degenerating criterion in [`0-program-methods/METHODOLOGY.md`](0-program-methods/METHODOLOGY.md). Contributions are judged by it, not by whether they support the conclusion.

## Accepted — progressive

- Adds novel content that **forbids** an observation.
- Sharpens an existing test, or tightens a `falsifies` condition.
- Converts an accommodation into a prediction by identifying what it forbids.
- Formalizes a prose-only claim.
- **Records a refutation.** A decided question is a progressive resolution whether it decides for the programme or against it. A well-documented failure is a contribution of the same rank as a success.
- Prices an option on an open problem, or closes one by argument.

## Declined — degenerating

- Ad hoc accommodation that reduces falsifiability.
- Presenting an accommodation as a prediction, or a re-description as a derivation.
- Inflating a confidence label, or removing a failure condition.
- Promoting a belt hypothesis into the hard core to shield it from refutation.
- Citing a live literature at its most convenient historical moment rather than its current state.
- Apologetic argumentation for the hard core. The core's warrant is exegetical and theological and is argued in [oddXian](https://github.com/jdlongmire/oddxian-apologetics); this repository's job is the belt and the predictions.

## Every claim carries its ledger entry

A prose contribution that introduces or changes a claim updates the corresponding `traceability/claims/*.yaml`, and `python3 traceability/scripts/build.py` runs clean with regenerated reports committed. CI enforces both.

Role-specific requirements:

| Role | Required fields |
|---|---|
| `prediction` | `falsifies` — what evidence refutes it, fixed **before** evaluation |
| `accommodation` | `forbids` (the literal `none` is legitimate) and `rival_account` — how standard cosmology handles the same observation, at its strongest |
| all | `risk_if_false`, acyclic `depends_on` |

## Review

Reviews are archived in [`reviews/`](reviews/) with a response. Reviews are actively sought from readers who **reject the hard core** — a review from someone who shares it cannot test the belt independently, and the belt is what has to survive.

A review that forces a confidence label down, exposes a circularity, or compels a retraction has succeeded.

## Attribution

Provenance on any artifact is the single line `Human-Curated, AI-Enabled (HCAE)`. No model or vendor byline; no model-signed confidence rating.
