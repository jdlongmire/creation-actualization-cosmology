# Creation Actualization Cosmology (CAC)

An alternative cosmological research programme founded on a different historical boundary condition: that the universe was **discretely actualized into functional maturity** during Creation Week, and has operated under stable physical law since.

CAC does not seek to repair ΛCDM. It replaces its historical boundary conditions.

**Status: CAC v0.1 — a position paper and a programme scaffold, not a cosmological model.** The programme's own [appraisal](3-prediction/appraisal.md) records it as **unappraised, with zero novel content**: 0 predictions, 5 accommodations, none of which forbids anything. That verdict is generated on every build, not asserted, and it is the honest starting point rather than a defect to be managed.

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

## The five axioms

1. The biblical creation narrative records genuine historical events.
2. Creation is an act of divine actualization rather than the culmination of prior natural processes.
3. Creation necessarily possesses functional maturity.
4. Day Four represents the actualization of the observable heavens into their operational state from Earth's historical perspective.
5. Following Creation Week, the universe operates under stable, intelligible physical laws.

Full statement in the [position paper §2](1-hypothesis/paper/CAC-v0.1.md); enumerated as immune commitments in [`hard-core.md`](1-hypothesis/hard-core.md).

## What is and is not claimed

CAC is a candidate research programme, not a completed physical theory and not a quantitative rival to ΛCDM. Its hard core is held immune **by methodological decision** and rests on exegetical and theological grounds — it is not offered as a scientific claim, and the repository says so rather than blurring the point. What must earn scientific standing is the belt and, above all, the predictions.

There are currently no predictions. The programme's scientific value depends entirely on whether it develops one. See [`3-prediction/discriminators.md`](3-prediction/discriminators.md) for what would count and where the search is concentrated.

## The accommodation ledger

Position paper §5 reinterprets five standing cosmological tensions. Every one is an accommodation of an **already-known** fact, and on Lakatos's criterion accommodations contribute nothing to progressiveness however elegant they are.

The traceability build enforces the distinction mechanically: accommodations carry a required `forbids` field (the answer `none` is legitimate and expected), a required `rival_account` field stating how standard cosmology handles the same observation at its strongest, and are counted separately from predictions in a [generated progressiveness report](traceability/generated/progressiveness-report.md).

The mechanism is deliberately unflattering. §5 is the most rhetorically attractive part of the paper and the least scientifically load-bearing, and making that visible on every build is the cheapest available defence against the failure this programme is most exposed to.

## The two problems the paper does not name

Registered at stand-up because a young-cosmos programme that does not confront them is not being read seriously:

- **[OPN-009](traceability/claims/OPN-009.yaml) — light travel time.** What accounts for light presently arriving from cosmological distances.
- **[OPN-010](traceability/claims/OPN-010.yaml) — processes observed in transit.** $(1+z)$ supernova light-curve time dilation, the SN 1987A ring geometry, quasar variability, binary pulsar spin-down. Sharper than OPN-009, less often addressed, and bearing directly on the paper's claim that operational completeness does not entail deception.

OPN-010 is flagged as the most promising place to look for the programme's first discriminator, on the reasoning that maximum exposure and maximum discriminating power are the same property.

## Relation to Triadic Reality Theory

CAC imports TRT's ontology — $\chi \equiv \mathcal{A}(I \mid L)$ — as the setting in which "actualization" is a primitive act rather than a limit of natural process.

It does **not** import TRT's belt-level cosmology. TRT's [ADCE](https://github.com/jdlongmire/triadic-reality-theory/blob/main/2-theory/04-cosmology/adce.md) note develops a *continuous* accumulation of realized causal history over cosmic time, which is not obviously compatible with CAC's discrete boundary condition. The conflict is registered as [OPN-008](traceability/claims/OPN-008.yaml) and priced in [`relation-to-trt.md`](1-hypothesis/relation-to-trt.md) rather than smoothed over.

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
