# The Predictive Thesis

> **Tier 1.** From historical boundary conditions to scientific expectation. Stated by JD, 2026-08-04. Registered as [PRD-001](../traceability/claims/PRD-001.yaml) — **the programme's first `role: prediction`**, and the first entry that moves the [progressiveness ledger](../traceability/generated/progressiveness-report.md) off zero.
>
> Read the [metric](#the-metric-hebi-as-a-vector-not-a-score) and the [refutation rule](#the-refutation-rule) before citing the thesis. A directional expectation without a decision rule is a philosophical posture, not a prediction, and the programme has committed to not confusing the two.

## The thesis

A scientific research programme should be evaluated not only by its ability to interpret existing observations but by the trajectory of knowledge it predicts. Every framework carries implicit expectations about how future discoveries will affect its own coherence, complexity, and explanatory power.

CAC begins from a different historical boundary condition than the standard paradigm: the universe was discretely actualized into a functionally mature operational state during Creation Week, and has proceeded since under stable, intelligible physical law. The difference concerns **historical boundary conditions rather than operational physics.**

Two domains of inquiry follow, and CAC predicts different trajectories for each.

**Operational science** investigates the regular behavior of the created order. Because the universe is the product of a rational Creator who governs it consistently, CAC expects operational science to continue achieving extraordinary explanatory and predictive success. The achievements of modern physics, chemistry, biology and astronomy are not surprising under CAC; they are expected consequences of an orderly creation.

**Historical reconstruction** attempts to infer unique, non-repeatable origins from present observations. Here CAC predicts the opposite trajectory. If the universe originated through discrete actualization rather than uninterrupted natural development, then historical models that exclude special creation by construction will encounter *increasing* explanatory burden as observational precision improves. They will be reconstructing developmental processes that, on CAC's account, did not occur — and will compensate with additional inferred components, auxiliary hypotheses, competing extensions, and free parameters.

This is not a prediction that naturalistic cosmology will cease to function, and it is not an accusation of bad science. It is the expected behavior of an otherwise successful framework operating with incorrect historical boundary conditions.

**Operational success does not guarantee historical completeness.** A model may describe how the universe behaves today with great accuracy while remaining an incomplete account of how it came to exist.

## The asymmetry is the prediction

Complexity growth alone predicts nothing, and stating it that way would be the thesis's fatal defect rather than its content.

Mature research programmes routinely accumulate structure as precision improves. The Standard Model of particle physics carries roughly nineteen free parameters and acquired them exactly that way, and it has no historical boundary conditions to be wrong about. If complexity growth under increasing precision is generic, then observing it in cosmology confirms nothing specific to CAC.

What CAC predicts is not complexity. It is **divergence between two limbs that the generic account expects to move together**:

> As observational precision increases, operational models of the present universe will continue to converge toward greater predictive accuracy, while historical models that assume uninterrupted natural development will exhibit increasing historical explanatory burden.

On the generic "mature programmes get complicated" story, both limbs complexify together. On CAC, they separate. The separation is the claim, and it is what a test must measure.

## The metric: HEBI as a vector, not a score

The **Historical Explanatory Burden Index** is deliberately *not* a single number. Four components, each measured and reported independently, each with its direction pre-committed:

| # | Component | Measured as | Direction consistent with CAC |
|---|---|---|---|
| H1 | Inferred cosmological components | Count of entities posited but not directly detected, under a counting convention fixed in advance | Non-decreasing |
| H2 | Adjustable parameters in leading historical models | Free-parameter count of the concordance model plus the extensions turned on in each release's headline analysis | Non-decreasing |
| H3 | Competing extensions in play | Count of distinct proposed extensions addressing a persistent tension **that survive to a subsequent data release** | Non-decreasing |
| H4 | Reconstruction stability | Shift in central values of age, $H_0$, $\Omega_m$ and $w(z)$ reconstructions between successive releases, relative to their quoted uncertainties | Non-converging |

The **operational control**, which must be measured over the same interval and reported alongside:

| # | Component | Measured as | Direction consistent with CAC |
|---|---|---|---|
| O1 | Operational predictive accuracy | Precision of observational measurement, predictive residuals, reproducibility, independent experimental agreement | Improving |

**Why a vector and not an aggregate.** A composite with four inputs and no weights is *less* falsifiable than a single scalar, because any mixed result can be read as confirmation by whoever already holds the thesis. That is the exact failure this programme's traceability apparatus exists to prevent, and adopting an index without a decision rule would import it at the level of the programme's only prediction. Aggregation is refused; the components are reported as a vector and adjudicated by the rule below.

**Why not parameter count alone.** A framework can grow more elaborate without adding free parameters, and can shed a parameter while its explanatory architecture becomes more intricate. H2 is one indicator among four for that reason (JD/GPT, 2026-08-04), and no component is permitted to stand for the whole.

## The refutation rule

Evaluated over **three successive major data releases** of Planck / DESI / Euclid class, against a baseline recorded before evaluation begins:

- **PRD-001 is refuted** if at least **three of the four** HEBI components move in the simplification direction (H1, H2, H3 decreasing; H4 converging) while O1 improves over the same interval.
- **PRD-001 is corroborated** if at least three of four move in the burden-increasing direction while O1 improves.
- **The test is void, not confirmed,** if O1 fails to improve. The thesis is about a *divergence*; a stalled operational limb removes the contrast and the interval yields no verdict. This clause exists so that stagnation in the rival programme can never be counted as CAC's success.
- **Any outcome between** is recorded as indeterminate for that interval, and the intervals accumulate rather than resetting.

**One component currently points against the thesis, and that is stated here rather than discovered later.** H4 has arguably been moving the *wrong* way for CAC across Planck 2013 → 2015 → 2018: central values for the age, $H_0$ and $\Omega_m$ tightened substantially, which is convergence rather than instability. The Hubble tension is a persistent *discrepancy between methods*, which is not the same measurement as drift in a single reconstruction across releases. If H4 continues converging, PRD-001 loses one of its four components immediately.

**The baseline is owed and not yet recorded.** No trajectory is measurable without a $t_0$. Fixing the counting conventions for H1–H3 and recording current values is the first task under this claim, and until it is done PRD-001 is a stated prediction with an unexecuted protocol.

## Methodological reciprocity

Creation Actualization Cosmology is evaluated by the same standard it applies to competing historical programmes. Should CAC require an indefinitely expanding body of auxiliary hypotheses without corresponding predictive success, the programme itself shall be regarded as degenerative in the Lakatosian sense.

This is not a courtesy. A thesis that measures explanatory burden while exempting its author from the instrument is a rhetorical device, and a reviewer will identify it as one immediately.

The reciprocity is **mechanized, not merely stated**: [`0-program-methods/ops/reciprocity_check.py`](../0-program-methods/ops/reciprocity_check.py) reports CAC's own burden trajectory — total claim count, open-problem count, and forbidding-claim count — on every build, so that the programme's own accumulation is visible in the same place it asks the rival's to be. It is advisory rather than blocking, because a programme in its first week has no meaningful trajectory yet; it becomes load-bearing once there is a history to read.

The honest current reading of CAC against its own instrument: **43 claims, 11 open problems, 2 predictions, 0 corroborations, and a burden ratio of 21.5 claims per claim that forbids anything — in one week.** Auxiliary structure is being added faster than content. That is expected during stand-up and it is exactly what the thesis says to watch for in a programme that has been running for decades — which is why the comparison is not yet meaningful in either direction, and why saying so is part of the claim.

## What this thesis is, and what it is not

It is a **programme-level appraisal claim**: it predicts the trajectory of a rival's model development. That is a legitimate Lakatosian object, and it is falsifiable under the rule above.

It is **not a novel-fact prediction about nature**. It forbids a pattern in how models evolve; it does not forbid an observation of the world. CAC still owes one of those, and [OPN-011](../traceability/claims/OPN-011.yaml) — the missing likelihood function — remains the programme's sharpest open problem.

**A sharper companion exists and should be read with it.** [PRD-002](../traceability/claims/PRD-002.yaml) takes this thesis's asymmetry and asks *where inside the models* the burden sits: explanatory information migrating from the dynamics into the initial conditions. That is a structural property rather than a property of the community doing the modeling, it has an explicitly opposite rival in the inflationary programme, and it is therefore the closer of the two to a claim about nature. Rationale at [`2-theory/05-specification/`](../2-theory/05-specification/specification-and-actualization.md). PRD-001 moving the ledger to one prediction should not be read as OPN-011 being answered, and the [appraisal log](../3-prediction/appraisal.md) records the distinction explicitly so that the count cannot quietly stand in for the kind.

## The summary proposition

The deeper our observational understanding of the universe becomes, the more clearly we should distinguish between the success of operational science and the limits of historical reconstruction. A universe created through discrete divine actualization will increasingly resist complete explanation by models that presuppose uninterrupted natural development.
