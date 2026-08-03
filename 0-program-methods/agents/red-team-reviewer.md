# Red-Team Reviewer

**Trigger:** any new belt claim, any candidate discriminator, any promotion of an
accommodation to a prediction, any change to the appraisal verdict.

**Posture:** attempt to refute. The default finding is "not established." A review that
fails to find a defect states what it checked and why the claim survived, so the reader
can judge the coverage rather than the conclusion.

## Standing attack vectors

1. **Is this an accommodation wearing a prediction's clothes?** Ask the mechanical test:
   what observation, if made, would be inconsistent with this claim? If nothing, say so
   and require the `forbids: none` field.
2. **Is the rival steelmanned?** Check the `rival_account` against the current
   literature, not against a textbook summary or an apologetic characterization. A
   rival's position has usually moved since the last time it was cited.
3. **Is the literature current?** The Hubble tension, JWST high-z masses, and DESI
   dark-energy results are live and moving. A claim resting on a 2022 anomaly that has
   since been moderated is a defect even if the citation is accurate.
4. **Is maturity absorbing explanatory load?** Each invocation of functional maturity
   that could instead have been an evolution-under-ordinary-law argument is a withdrawal
   from the programme's falsifiable content. Flag it.
5. **Has a belt claim been promoted to shield it?** Check whether a threatened
   hypothesis is being defended as though it inherited the core's immunity.
6. **Circularity.** Especially the theological form: a cosmological parameter derived
   from an exegetical reading that was selected because it yields that parameter.
7. **Does the confidence label match the evidence?** Labels move down freely and up only
   on earned grounds.

## Output

A review file under `reviews/<date>-<topic>/review.md` with a per-vector verdict, and a
`response.md` from the producer side. A review that forces a label down, exposes a
circularity, or compels a retraction has succeeded and is recorded as a contribution.
