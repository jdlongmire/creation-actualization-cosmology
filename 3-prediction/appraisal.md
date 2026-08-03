# Programme Appraisal (Progressive vs Degenerating)

> The Lakatosian self-audit. A research programme is **progressive** if it predicts novel facts and some corroborate; **degenerating** if it only accommodates facts post hoc. This file is the standing answer to: *which is CAC, right now?*
>
> The mechanical counterpart is the generated [progressiveness report](../traceability/generated/progressiveness-report.md), regenerated on every build.

## Current verdict (CAC v0.1)

**Unappraised — and, more precisely, with zero novel content.**

CAC is a research programme in the literal Lakatosian sense: it has an articulated [hard core](../1-hypothesis/hard-core.md), an articulated positive heuristic (the [ROADMAP](../0-program-methods/ROADMAP.md)), and a stated intention to become testable ([position paper §9](../1-hypothesis/paper/CAC-v0.1.md)). It has **no prediction**, and therefore nothing that could yet corroborate or refute.

The ledger at stand-up:

| Category | Count |
|---|---|
| Predictions (`role: prediction`) | **0** |
| Accommodations (`role: accommodation`) | 5 |
| — of which forbid something | **0** |
| Open problems | 10 |

All five of the position paper's §5 reinterpretations — low initial entropy, redshift, the Hubble tension, JWST early structure, the dark sector — are accommodations of facts that were known before the claims were made. On Lakatos's criterion they contribute **nothing** to progressiveness however coherent they are. This is not a criticism of §5; it is what §5 is. The paper says so itself in §8 and §9, and the [methodology](../0-program-methods/METHODOLOGY.md) makes it structural so it cannot quietly stop being said.

**One wording correction is carried into v0.2.** §5 uses "CAC predicts" twice — in the Hubble tension and JWST paragraphs. Neither is a prediction in the Popperian sense: both are compatible with any observed outcome including none. Per [research-practices #1](../0-program-methods/research-practices.md), the wording is recorded here as a correction rather than silently kept, because "predicts" doing accommodation's work is the exact slippage the programme is most at risk of.

## What would move the needle to *progressive*

One claim that forbids an observation ΛCDM permits, or permits one ΛCDM forbids, stated with its evaluation protocol **in advance** — then corroborated.

| Candidate route | Source | Gate |
|---|---|---|
| A created-geometry redshift model reproducing $(1+z)$ supernova light-curve time dilation, with a residual signature LCDM does not predict | [OPN-004](../traceability/claims/OPN-004.yaml), [OPN-010](../traceability/claims/OPN-010.yaml) | OPN-002 mechanism |
| A stated maturity-versus-redshift distribution differing from the LCDM expectation, testable against a defined JWST sample | [ACC-004](../traceability/claims/ACC-004.yaml) promotion | Requires a quantitative maturity measure |
| A derived magnitude or sign for the early-late $H_0$ offset | [ACC-003](../traceability/claims/ACC-003.yaml) promotion | OPN-001, OPN-004 |

The most likely source of a real discriminator is [OPN-010](../traceability/claims/OPN-010.yaml) — processes observed in transit. It is where the programme is most exposed, and exposure and discriminating power are the same property seen from opposite ends.

A *theoretically* progressive step (stating something that forbids an observation) precedes an *empirically* progressive one (the observation goes the programme's way). CAC has taken neither.

## What would mark *degeneration* — to be recorded as plainly as success

- **Accommodation accumulation.** A sixth, seventh, eighth §5-style reinterpretation while the prediction count stays at zero. The [progressiveness report](../traceability/generated/progressiveness-report.md) will show it adding nothing, and that showing is the point.
- **Maturity absorbing the explanatory load.** Every unexplained structure being resolved by "it was created that way." [OPN-006](../traceability/claims/OPN-006.yaml) is the named watch-point: if large-scale structure must be *specified* rather than *grown*, the maturity principle has become unfalsifiable in practice.
- **Belt promotion.** Defending a threatened exegetical or physical hypothesis by treating it as though it inherited the core's immunity. [HER-002](../traceability/claims/HER-002.yaml) and [HER-003](../traceability/claims/HER-003.yaml) are in the belt precisely so this is visible when attempted.
- **Riding a moving literature.** Continuing to cite the strong form of the JWST anomaly, or a Hubble tension that systematics have closed, after the literature has moved. [ACC-004](../traceability/claims/ACC-004.yaml) already carries this warning.
- **Rounding the status up.** Describing the programme as anything other than unappraised, anywhere, before this log says otherwise.
- **Silence on OPN-009 / OPN-010.** A programme that never states its position on light in transit has chosen unfalsifiability by omission.

## Log

| Date | Event | Effect on appraisal |
|---|---|---|
| 2026-08-03 | Programme stood up. Position paper v0.1 landed; hard core enumerated (7 claims); belt seeded (7 hypotheses, 5 accommodations, 2 imports); 10 open problems registered; progressiveness ledger mechanized in the traceability build | **Unappraised (baseline).** 0 predictions, 5 accommodations, 0 forbidding anything |
| 2026-08-03 | **OPN-008 opened** — TRT's belt cosmology (ADCE) develops *continuous* actualization over cosmic time and is not obviously compatible with CAC's discrete boundary condition. Found by reading ADCE directly rather than the §7 summary. Three dispositions priced in [`relation-to-trt.md`](../1-hypothesis/relation-to-trt.md); none chosen | No change to verdict. Registers a known conflict *before* belt work is built on the assumption of compatibility — a progressive move in the housekeeping sense, not in the content sense |
| 2026-08-03 | **OPN-009 and OPN-010 opened** — light travel time, and processes observed in transit. Neither is named in the position paper | No change to verdict. Both are load-bearing objections; OPN-010 additionally bears on [CRE-007](../traceability/claims/CRE-007.yaml)'s deception disclaimer, which is asserted in the paper but not yet argued |
