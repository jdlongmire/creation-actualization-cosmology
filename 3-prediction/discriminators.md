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

## Where to hunt

Ranked by expected yield, which tracks exposure rather than comfort.

### 1. Processes observed in transit — [OPN-010](../traceability/claims/OPN-010.yaml)

The strongest candidate. Distant observations record processes with internal duration, not just arrived photons:

- Type Ia supernova light curves time-dilated by $(1+z)$, measured out to $z \approx 1$ and consistent across the sample
- The SN 1987A ring geometry, whose light-echo timing gives a geometric distance largely independent of the cosmic distance ladder
- Quasar and blazar variability timescales
- Binary pulsar orbital decay matching general-relativistic spin-down

Any CAC account of light in transit makes *some* commitment about what these records are. That commitment is where a discriminator lives. If the account says the records are of real processes, it owes a mechanism by which those processes occurred within the programme's history. If it says they are specified rather than occurred, it owes a response to [CRE-007](../traceability/claims/CRE-007.yaml) — and, more usefully here, it may forbid particular *inconsistencies* between independent records of the same distant event, which is a testable claim.

**The residuals are the opportunity.** A created-geometry redshift model ([OPN-004](../traceability/claims/OPN-004.yaml)) that reproduces the distance-redshift relation will not in general reproduce the $(1+z)$ time-dilation scaling *exactly*. The size and shape of the mismatch is a candidate prediction — and one that current supernova samples can already constrain.

### 2. Light travel time — [OPN-009](../traceability/claims/OPN-009.yaml)

Lower expected yield than OPN-010 because the existing treatments in the literature (relativistic time-dilation cosmologies, alternative synchrony conventions, in-transit creation) mostly resolve *arrival* without forbidding anything further. Survey and price them rather than reinventing; the value here is establishing what CAC must hold, which then constrains OPN-010.

### 3. Structure formation rate — [OPN-006](../traceability/claims/OPN-006.yaml)

If actualized initial conditions plus ordinary gravitational law over a short interval produce a *different* structure-growth history than ΛCDM, growth-rate observables ($f\sigma_8$ from redshift-space distortions, cluster abundance evolution) discriminate. This route requires OPN-001 and OPN-003 first, so it is slower — but it is the route where the two programmes make quantitatively comparable statements about the same measured quantity, which is the cleanest form a discriminator can take.

### 4. Promotion of an existing accommodation

Each of [ACC-001](../traceability/claims/ACC-001.yaml) through [ACC-005](../traceability/claims/ACC-005.yaml) carries a `notes` field stating what promotion would require. ACC-003 (a derived magnitude or sign for the early-late $H_0$ offset) and ACC-004 (a maturity distribution versus redshift) are the two with a concrete path.

## What does not count

- "CAC expects X" where X is already observed. That is [ACC-\*](../traceability/generated/progressiveness-report.md).
- "CAC allows the possibility of X." Allowing forbids nothing.
- "Systematic discrepancies may appear." Compatible with any outcome including none — this is the precise defect recorded against ACC-003.
- A retrodiction of a fact the programme was built to accommodate.
