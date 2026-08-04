# Creation Actualization Cosmology (CAC)

[![CI](https://github.com/jdlongmire/creation-actualization-cosmology/actions/workflows/ci.yml/badge.svg)](https://github.com/jdlongmire/creation-actualization-cosmology/actions/workflows/ci.yml)

An alternative cosmological research programme founded on a different historical boundary condition: that the universe was **discretely actualized into functional maturity** during Creation Week, and has operated under stable physical law since.

CAC does not seek to repair ΛCDM. It replaces its historical boundary conditions.

**Status: CAC v0.1 — a position paper and a programme scaffold, not a cosmological model.** The programme's own [appraisal](3-prediction/appraisal.md) records it as **empirically unappraised, with one theoretically progressive step taken**: 1 prediction ([PRD-001](traceability/claims/PRD-001.yaml), protocol unexecuted), 5 accommodations, none of which forbids anything, and **0 novel-fact predictions about nature**. PRD-001 forbids a pattern in how a rival's models evolve, which is a legitimate Lakatosian object and a weaker species than the programme still owes. The ledger is generated on every build, not asserted, and it is the honest starting point rather than a defect to be managed.

---

## How this repository is structured

The layout is a **[Lakatosian research programme](0-program-methods/METHODOLOGY.md)** governed by a **Popperian** standard, adopting the ladder used by [Triadic Reality Theory](https://github.com/jdlongmire/triadic-reality-theory). The tiers form a *falsifiability gradient* — each more exposed to refutation than the one above — and the programme's work is to push claims *down* the ladder.

| Tier | Role | Contents |
|---|---|---|
| **[0-program-methods/](0-program-methods/)** | How the programme is run (governs the ladder) | [VSOK](0-program-methods/vsok.md) · [METHODOLOGY](0-program-methods/METHODOLOGY.md) · [ROADMAP](0-program-methods/ROADMAP.md) (the positive heuristic) · [research practices](0-program-methods/research-practices.md) · [GitHub workflow](0-program-methods/github-workflow.md) |
| **[1-hypothesis/](1-hypothesis/)** | **Hard core** — immune by *decision*, and said so | [hard-core.md](1-hypothesis/hard-core.md) · [the position paper](1-hypothesis/paper/CAC-v0.1.md) · [relation to TRT](1-hypothesis/relation-to-trt.md) |
| **[2-theory/](2-theory/)** | **Protective belt** — the adjustable work | [exegesis](2-theory/00-exegesis/) · [actualization](2-theory/01-actualization/) · [metric & redshift](2-theory/02-metric/) · [entropy](2-theory/03-entropy/) · [dark sector](2-theory/04-dark-sector/) · [open problems](2-theory/open-problems.md) |
| **[3-prediction/](3-prediction/)** | **Severe tests** — claims that forbid something | [discriminators](3-prediction/discriminators.md) *(currently empty — this is the critical path)* · [appraisal](3-prediction/appraisal.md) |

Supporting: **[traceability/](traceability/)** (claim ↔ dependency ↔ prose audit), **[references/](references/)**, **[reviews/](reviews/)**.

## The Origins Framework

CAC's five axioms are the *cosmological specialization* of a seven-point origins framework stated at [`1-hypothesis/origins-framework.md`](1-hypothesis/origins-framework.md) (**v0.2**): the Bible as material authoritative source; God producing systems functionally mature (Adam and Eve, the wine at Cana, healings that skip the normal biological process); deep time therefore not *necessary*; apparent age as the output of naturalistic Bayesian priors rather than an observation; contingency requiring a non-contingent, logical, informational and actualizable source; methodological designism, since special intervention is by definition the exception; and a set of standing anomalies that a uniformly naturalistic cosmos would not be expected to produce.

Points 4 and 6 do the most work here. Point 4 is correct as epistemology and is the right reply to a large class of "but it *looks* old" objections — the inference is theory-laden and the prior is carrying it. Point 6 is where the programme becomes testable: if law is the rule, the post-creation era is ordinary physics on an actualized initial configuration, which is falsifiable without relitigating apparent age.

**Point 7 is stated in the framework and deliberately not registered as claims.** Registering the ten anomalies as they stand would take the ledger from 5 accommodations and 0 predictions to 15 and 0, since each accommodates an already-known fact; and the argument form — surprises exist, therefore not naturalism — is a likelihood ratio whose second factor is exactly what [OPN-011](traceability/claims/OPN-011.yaml) says the programme has never supplied. The form that *would* run is the claim that the residuals are **directionally biased**, that systems are observed systematically more mature and intact than gradualist expectation permits and never systematically less. That version forbids something, and it is registered as a route at OPN-011 rather than banked as content.

## The five axioms

1. The biblical creation narrative records genuine historical events.
2. Creation is an act of divine actualization rather than the culmination of prior natural processes.
3. Creation necessarily possesses functional maturity.
4. Day Four represents the actualization of the observable heavens into their operational state from Earth's historical perspective.
5. Following Creation Week, the universe operates under stable, intelligible physical laws.

Full statement in the [position paper §2](1-hypothesis/paper/CAC-v0.1.md); enumerated as immune commitments in [`hard-core.md`](1-hypothesis/hard-core.md).

## What is and is not claimed

CAC is a candidate research programme, not a completed physical theory and not a quantitative rival to ΛCDM. Its hard core is held immune **by methodological decision** and rests on exegetical and theological grounds — it is not offered as a scientific claim, and the repository says so rather than blurring the point. What must earn scientific standing is the belt and, above all, the predictions.

There is currently **one** prediction — [PRD-001](traceability/claims/PRD-001.yaml), stated in [`1-hypothesis/predictive-thesis.md`](1-hypothesis/predictive-thesis.md) — and it is a prediction about the *trajectory of a rival's model development*, not about nature. There are **no novel-fact predictions**, and [OPN-011](traceability/claims/OPN-011.yaml) says why: **the programme has no likelihood function.** It has not specified $P(E \mid H_{\mathrm{CAC}})$ — what a discretely actualized cosmos should be expected to look like, in what respects, with what distribution. This was surfaced by holding the framework's own Bayesian argument to its own standard: point 4 correctly identifies that the *prior* is doing the work in standard age determinations, but a prior shift cannot be computed against a likelihood nobody has written down. Until one exists, any observation is absorbable by "your priors generated that inference," which forbids nothing.

The programme's scientific value depends entirely on closing that gap. See [`3-prediction/discriminators.md`](3-prediction/discriminators.md) for what would count and where the search is concentrated.

## The predictive thesis — PRD-001

[`1-hypothesis/predictive-thesis.md`](1-hypothesis/predictive-thesis.md). CAC's difference from the standard paradigm is one of **historical boundary conditions, not operational physics**, and two trajectories follow from that. Operational science, investigating the regular behavior of a consistently governed order, should keep converging. Historical reconstruction, inferring unique origins under an assumption of uninterrupted natural development, should accumulate explanatory burden as precision improves.

**The asymmetry is the prediction, not the complexity.** Mature programmes generically accumulate structure — the Standard Model carries ~19 free parameters and has no historical boundary conditions to be wrong about — so complexity growth alone discriminates nothing. What CAC forbids is the two limbs moving together.

Burden is measured by the **Historical Explanatory Burden Index**, deliberately a *vector* rather than a score: inferred components, adjustable parameters, surviving competing extensions, and reconstruction stability, each reported separately with its direction fixed in advance, adjudicated by a majority rule over three successive Planck/DESI/Euclid-class releases. A composite with four inputs and no weights would be *less* falsifiable than a single scalar, since any mixed outcome reads as confirmation to whoever holds the thesis; a single scalar invites Goodhart. The vector plus decision rule is the resolution of both.

Two disciplines ship with it. **The test is void, not confirmed, if operational accuracy stops improving** — stagnation in the rival programme can never be counted as CAC's success. And **methodological reciprocity**: CAC is evaluated by the same instrument, mechanized at [`0-program-methods/ops/reciprocity_check.py`](0-program-methods/ops/reciprocity_check.py), which currently reports 41 claims per claim that forbids anything. That reading is unflattering and it is printed on every build for the same reason the accommodation ledger is.

## The accommodation ledger

Position paper §5 reinterprets five standing cosmological tensions. Every one is an accommodation of an **already-known** fact, and on Lakatos's criterion accommodations contribute nothing to progressiveness however elegant they are.

The traceability build enforces the distinction mechanically: accommodations carry a required `forbids` field (the answer `none` is legitimate and expected), a required `rival_account` field stating how standard cosmology handles the same observation at its strongest, and are counted separately from predictions in a [generated progressiveness report](traceability/generated/progressiveness-report.md).

The mechanism is deliberately unflattering. §5 is the most rhetorically attractive part of the paper and the least scientifically load-bearing, and making that visible on every build is the cheapest available defence against the failure this programme is most exposed to.

## The two problems the paper does not name — now answered

Registered at stand-up because a young-cosmos programme that does not confront them is not being read seriously:

- **[OPN-009](traceability/claims/OPN-009.yaml) — light travel time.** What accounts for light presently arriving from cosmological distances.
- **[OPN-010](traceability/claims/OPN-010.yaml) — processes observed in transit.** $(1+z)$ supernova light-curve time dilation, the SN 1987A ring geometry, quasar variability, binary pulsar spin-down. Sharper than OPN-009, less often addressed, and bearing directly on the paper's claim that operational completeness does not entail deception.

**Both were answered on 2026-08-03** by the Origins Framework, taking the branch on which the record is actual and the recorded process is not — defensible because the luminaries' stated function is signs and seasons rather than chronicle, and because the chronological inference is supplied by the observer's priors rather than asserted by the artifact. [CRE-007](traceability/claims/CRE-007.yaml) is correspondingly upgraded from *asserted* to *argued*.

What remains is not a position but a **likelihood** ([OPN-011](traceability/claims/OPN-011.yaml)), which is why the discriminator hunt has moved off these two and onto the constructive limb of methodological designism.

## Relation to Triadic Reality Theory

CAC imports TRT's ontology — $\chi \equiv \mathcal{A}(I \mid L)$ — as the setting in which "actualization" is a primitive act rather than a limit of natural process.

It does **not** import TRT's belt-level cosmology. [OPN-008](traceability/claims/OPN-008.yaml) asked whether CAC's discrete actualization and TRT's [ADCE](https://github.com/jdlongmire/triadic-reality-theory/blob/main/2-theory/04-cosmology/adce.md) — which develops a *continuous* accumulation of realized causal history — can both be developments of the same ontology. **Dispositioned 2026-08-03, sharpened 2026-08-04: compatible cores, composable belts.**

The two hard cores share no proposition on which they could disagree. TRT's constrains the form and status of the actual and fixes no content, occasion or duration for any particular actualization; CAC's makes historical and content claims about one actualization event. The temporal profile of actualization is a parameter TRT's core leaves free, established by TRT's own registered refutation of ADCE's forcing hypothesis. **TRT's core is silent on duration** — where a timeline appears on the TRT side it belongs to ADCE's belt, which develops inside the standard expansion history. "ADCE works within the conventional timeline" is accurate; "TRT requires deep time" is not.

ADCE chooses rate; CAC chooses act; and on ADCE's rate-shaped bridge laws those **compose** rather than compete, since a mature initial stock is invisible to a scale-free growth law ([EXT-005](traceability/claims/EXT-005.yaml)). The one stock-shaped quantity in the neighbourhood is everpresent $\Lambda \sim \pm\hbar/\sqrt{V_4}$, ADCE's declared rival, and it is where the composition stops being free — registered as [OPN-012](traceability/claims/OPN-012.yaml), which is also the programme's first computable discriminator lead.

**The disposition costs CAC its grounding argument, and the repository carries the cost rather than banking the result.** An ontology that does not entail continuity does not entail discreteness either, so the position paper's "naturally derives from TRT" is *wrong*, not merely unsupported, and becomes "adopts the ontology of" in v0.2. What the import supplies is a formal home for actualization-as-act, plus one real constraint: TRT's four-tier engine forbids leaving the status of a distant record's process undeclared ([EXT-004](traceability/claims/EXT-004.yaml)), which narrows the option space at OPN-010. Full argument in [`relation-to-trt.md`](1-hypothesis/relation-to-trt.md).

## Working in this repository

```bash
python3 0-program-methods/ops/research-start.py    # orientation briefing
python3 traceability/scripts/build.py              # validate claims, regenerate reports
python3 0-program-methods/ops/research-wrap.py     # end-of-session hygiene gate
```

Contribution rules and the progressive/degenerating criterion: [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Citation

See [`CITATION.cff`](CITATION.cff).

## License

Prose and documents: **CC BY 4.0**. Code: **Apache 2.0**.

---

*Human-Curated, AI-Enabled (HCAE)*
