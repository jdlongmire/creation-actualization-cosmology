# Research Practices

Disciplines the programme commits to beyond the [Popper/Lakatos methodology](METHODOLOGY.md). These are the *how-we-work* norms that keep the programme honest as it scales.

## 1. Accommodation vs prediction — the standing demarcation

A reinterpretation of an *already-known* fact is an **accommodation**; a claim that forbids something is a candidate **prediction**. Every result is tagged as one, in prose and in its traceability claim (`role: accommodation` or `role: prediction`). Presenting an accommodation as a prediction is this programme's canonical degenerating move and is rejected in review.

The test is mechanical: *what observation, if made, would be inconsistent with this claim?* If the answer is "none," it is an accommodation. The claim's `forbids` field records the answer, including when the answer is `none`.

## 2. Preregistration

State the prediction *and its failure condition* **before** evaluating it. No result is reported without the refutation condition having been fixed in advance. This forecloses exactly the post-hoc accommodation that marks a degenerating programme, and the programme is at elevated risk of it because its §5 material is retrospective by construction.

## 3. Confidence labelling

Every claim carries a label — **HIGH · MEDIUM · LOW · UNCERTAIN** in prose; the traceability enum `established / argued / conjectured / open`. Labels move *down* freely on evidence and *up* only on earned grounds. An inflated label is a review-blocking defect.

## 4. Exegetical discipline

Exegetical claims sit in the [belt](../2-theory/00-exegesis/), not the core, and are held to the same standards as physical ones:

- **Primary text first.** Hebrew text and lexical evidence before English translations, and translations before commentary.
- **Name the competing readings.** A Day Four reading is stated alongside the framework, analogical-day, and functional-ontology alternatives, with the grounds for preferring it and the cost of being wrong.
- **Say what the reading forbids.** An exegetical commitment with no consequence for what may be observed is coherence work, and is logged as such.
- **Do not smuggle the core.** "Genesis is history" (core) does not by itself settle *which* historical reading is correct; treating a preferred reading as though it inherited the core's immunity is the belt-promotion failure the [methodology](METHODOLOGY.md) names.

## 5. Primary-source discipline (scientific citations)

Cite primaries, not secondary characterizations, and especially not secondary characterizations from apologetic or anti-apologetic sources on either side. Use "as cited in" when primary access is unavailable, and flag for verification. Verification state is tracked per reference in [`../references/verification-status.md`](../references/verification-status.md); no downstream work builds on an unverified citation.

This bites hardest on §5's tension claims. The Hubble tension, JWST high-redshift masses, and DESI dark-energy results are **live, moving literatures** with active reanalyses — the position paper already concedes as much for JWST ("many initial claims have since been moderated"). Any use of a tension as support carries the current state of that literature, not the state at which it was most convenient.

## 6. Steelman the standard model

The programme's claim is that ΛCDM's *historical boundary condition* is wrong, not that ΛCDM is incompetent. Every accommodation must state how standard cosmology addresses the same observation, at its strongest, before stating CAC's alternative. An accommodation that is impressive only against a weak version of the rival is worth nothing.

## 7. Reproducibility

Computational results ship with their code (`3-prediction/<test>/code/`) and a stated environment. A result that cannot be reproduced is not a result. The traceability `formal_artifacts` field links each claim to its computational artifact with a status.

## 8. Circularity audit

Mandatory for derivations and any parameter claimed as "derived." Trace the dependency graph (must be acyclic — enforced by CI), audit definitions for self-reference, confirm no "derived" value was fitted to the outcome it explains. Watch specifically for the theological form: deriving a cosmological parameter from an exegetical reading that was itself selected because it yields that parameter.

## 9. Adversarial review is a contribution

A review that forces a confidence label down, exposes a circularity, or compels a retraction is *successful*, and is archived in [`../reviews/`](../reviews/) with a response. Reviews are sought from readers who reject the hard core, because a review from someone who shares it cannot test the belt independently.

## 10. Honest status at all times

The [appraisal log](../3-prediction/appraisal.md) records standingly whether the programme is progressive, degenerating, or unappraised. The status is never rounded up, and never rounded up in a summary, abstract, talk, or post that circulates ahead of the log.

## 11. GitHub-safe LaTeX

Math must render on GitHub and in strict KaTeX viewers, not only in a local engine.

- **Operator names:** `\mathrm{Name}`, never `\operatorname{Name}` (rejected by GitHub's renderer). Enforced by CI.
- **Absolute values in inline math inside tables:** `\lvert … \rvert`, not bare `|` — kramdown reads `|` as a table delimiter.
- **No** `\def`, `\newcommand`, `\gdef`, `\let`, `\href`, `\label`, `\tag` in committed math.

## 12. Attribution

Provenance on any artifact is the single line `Human-Curated, AI-Enabled (HCAE)`. No model or vendor byline, no model-signed confidence rating.
