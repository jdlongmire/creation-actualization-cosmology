# Discriminators — the critical path

> **Tier 3.** This directory holds claims that *forbid* something. It is currently **empty of them**, and that is the single most important fact about the programme's status. This file states what a discriminator would have to look like and where to hunt for one.

## Why this is the critical path

The position paper's §9 lists five areas where testable consequences might be developed. Four of them — postulates, field equations, redshift models, entropy accounting — are belt construction. They can all succeed and leave the programme exactly where it is: coherent, elaborate, and forbidding nothing.

Only a discriminator changes the programme's Lakatosian status. Everything else is preparation for it.

## What counts

A discriminator is a claim, stated **before** evaluation, that meets all four conditions:

1. **It forbids.** There is an observation which, if made, is inconsistent with CAC.
2. **The rival permits it.** ΛCDM does not forbid the same observation, or forbids a different one. A claim both programmes forbid discriminates nothing.
3. **It is evaluable.** The observation is one that existing or planned instruments can make, against a defined sample and a stated analysis.
4. **The failure condition is written down first,** in the claim's `falsifies` field, before any evaluation is run.

A claim meeting 1–4 is registered with `role: prediction`. A claim meeting some but not all is registered as `role: accommodation` with a `forbids` field recording exactly how far it gets.

## The gate: there is no likelihood function — [OPN-011](../traceability/claims/OPN-011.yaml)

Nothing in the hunt below is reachable until the programme can state $P(E \mid H_{\mathrm{CAC}})$ — what a discretely actualized cosmos should be expected to look like, in what respects, with what distribution.

This became explicit on 2026-08-03, when the [Origins Framework](../1-hypothesis/origins-framework.md) stated the apparent-age argument in Bayesian terms. [EPI-001](../traceability/claims/EPI-001.yaml) is right that standard age determinations are prior-driven and that the prior is doing the work. But Bayes has two factors, and holding the argument to its own standard surfaces the gap: the recommended prior shift cannot be *computed* against a likelihood the programme has not supplied. Absent one, every observation is absorbable by "your priors generated that inference" — which forbids nothing, and is exactly why the ledger reads zero.

The likelihood is not a preliminary to the discriminator hunt. **It is the discriminator hunt**, stated precisely.

## Where to hunt

Ranked by expected yield. Note that the ranking **changed on 2026-08-03**: the constructive limb of methodological designism now leads, and processes-in-transit has dropped, because the Origins Framework supplied a position there and what remains is the likelihood rather than the position.

### 1. The constructive limb of methodological designism — [EPI-002](../traceability/claims/EPI-002.yaml), [OPN-006](../traceability/claims/OPN-006.yaml)

**The most promising ground, and the least exploited.** If intervention is the exception and law is the rule, then everything after Creation Week is ordinary physics acting on an actualized initial configuration. That is substantive, constrained, and computable in principle — and it needs no relitigation of apparent age, which is where the argument tends to get stuck.

Ordinary gravitational law acting on a specified initial state over a short interval either does or does not reproduce observed structure. If the growth history differs from ΛCDM's, then growth-rate observables discriminate: $f\sigma_8$ from redshift-space distortions, cluster abundance evolution. Both programmes then make quantitatively comparable statements about the same measured quantity, which is the cleanest form a discriminator can take.

This is also the one place the likelihood is not hostage to the creation act itself: EPI-002 asserts that the post-creation era runs on law, so $P(E \mid H_{\mathrm{CAC}})$ over that era is computable from the initial configuration without any appeal to what actualization "would" produce. Start [OPN-011](../traceability/claims/OPN-011.yaml) here.

### 2. Processes observed in transit — [OPN-010](../traceability/claims/OPN-010.yaml)

**Position now declared; likelihood outstanding.** The Origins Framework answers this via EXT-004 branch two — the record is actual, the recorded process is not, and this is not deception because the luminaries' stated function is signs and seasons rather than chronicle ([HER-002](../traceability/claims/HER-002.yaml)) and the chronological inference comes from the observer's priors ([EPI-001](../traceability/claims/EPI-001.yaml)).

What keeps it on the list is the residual: the Cana argument is strongest for *configurations*. These are records of processes with internal duration and **cross-channel consistency**:

- Type Ia supernova light curves time-dilated by $(1+z)$, measured out to $z \approx 1$ and consistent across the sample
- The SN 1987A ring geometry, whose light-echo timing gives a geometric distance largely independent of the cosmic distance ladder
- Quasar and blazar variability timescales
- Binary pulsar orbital decay matching general-relativistic spin-down

Any CAC account of light in transit makes *some* commitment about what these records are. That commitment is where a discriminator lives. If the account says the records are of real processes, it owes a mechanism by which those processes occurred within the programme's history. If it says they are specified rather than occurred, it owes a response to [CRE-007](../traceability/claims/CRE-007.yaml) — and, more usefully here, it may forbid particular *inconsistencies* between independent records of the same distant event, which is a testable claim.

**The residuals are the opportunity.** A created-geometry redshift model ([OPN-004](../traceability/claims/OPN-004.yaml)) that reproduces the distance-redshift relation will not in general reproduce the $(1+z)$ time-dilation scaling *exactly*. The size and shape of the mismatch is a candidate prediction — and one that current supernova samples can already constrain.

### 3. Light travel time — [OPN-009](../traceability/claims/OPN-009.yaml)

Lower expected yield than OPN-010 because the existing treatments in the literature (relativistic time-dilation cosmologies, alternative synchrony conventions, in-transit creation) mostly resolve *arrival* without forbidding anything further. Survey and price them rather than reinventing; the value here is establishing what CAC must hold, which then constrains OPN-010.

### 4. Promotion of an existing accommodation

Each of [ACC-001](../traceability/claims/ACC-001.yaml) through [ACC-005](../traceability/claims/ACC-005.yaml) carries a `notes` field stating what promotion would require. ACC-003 (a derived magnitude or sign for the early-late $H_0$ offset) and ACC-004 (a maturity distribution versus redshift) are the two with a concrete path.

## What does not count

- "CAC expects X" where X is already observed. That is [ACC-\*](../traceability/generated/progressiveness-report.md).
- "CAC allows the possibility of X." Allowing forbids nothing.
- "Systematic discrepancies may appear." Compatible with any outcome including none — this is the precise defect recorded against ACC-003.
- A retrodiction of a fact the programme was built to accommodate.
- **"Your priors generated that inference."** True, useful, and defensive. It removes a reason to reject CAC; it supplies no reason to expect anything. Until [OPN-011](../traceability/claims/OPN-011.yaml) is answered this is the programme's whole observational repertoire, and the ledger counts it at zero.
