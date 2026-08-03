# Methodology — Popper, Lakatos, and the Falsifiability Ladder

This repository is structured as a **Lakatosian research programme** and governed by a **Popperian** standard of demarcation. The directory layout is not filing; it is the methodology made structural. This file states the apparatus, how each tier realizes it, and the two places where CAC's situation differs from a conventional physics programme.

The apparatus is adopted from the [Triadic Reality Theory](https://github.com/jdlongmire/triadic-reality-theory) programme, which uses the same ladder. Where CAC diverges, it says so.

---

## The two standards

**Popper** (*The Logic of Scientific Discovery*, 1959; *Conjectures and Refutations*, 1963). Demarcation by **falsifiability**: a claim is scientific iff it *forbids* something — exposes itself to a risky test that could refute it. Progress is bold conjecture met by severe attempted refutation. There is no verification, only corroboration and falsification. Ad hoc moves that *reduce* falsifiability are illegitimate (the "conventionalist twist").

**Lakatos** (*The Methodology of Scientific Research Programmes*, 1970). The unit of appraisal is not a lone theory but a **programme** with three parts:

- a **hard core** of fundamental commitments, held immune by the *negative heuristic*;
- a **protective belt** of auxiliary hypotheses that take the brunt of refutation;
- a **positive heuristic**: an articulated plan for developing the refutable variants.

A programme is **progressive** if it predicts *novel facts* and some corroborate; **degenerating** if it only accommodates facts post hoc.

---

## The tier mapping

The tiers form a **falsifiability gradient** — each more exposed to refutation than the one above. The programme's work is to push claims *down* the ladder.

| Tier | Lakatos/Popper role | Holds |
|---|---|---|
| **[0-program-methods](.)** | The frame that *governs* the ladder (not on it) | [VSOK](vsok.md), this methodology, the [ROADMAP](ROADMAP.md) (= the **positive heuristic**), [research practices](research-practices.md), [GitHub workflow](github-workflow.md) |
| **[1-hypothesis](../1-hypothesis/)** | **Hard core** + negative heuristic | The five axioms, functional maturity as a cosmological principle, the [position paper](../1-hypothesis/paper/CAC-v0.1.md) |
| **[2-theory](../2-theory/)** | **Protective belt** + execution of the positive heuristic | Exegesis, actualization mechanism, metric/redshift, entropy, dark sector, [open problems](../2-theory/open-problems.md) |
| **[3-prediction](../3-prediction/)** | **Popperian severe test** + progressive/degenerating appraisal | Claims that *forbid* something, their test protocols, the [appraisal log](../3-prediction/appraisal.md) |

The two transitions name the programme's governing tasks:

- **1 → 2** — turn a core commitment into an adjustable, formalizable hypothesis. Currently almost all of CAC's work.
- **2 → 3** — produce a claim that forbids an observation ΛCDM permits, or permits one ΛCDM forbids. **CAC has not yet made this transition once.** See the [appraisal](../3-prediction/appraisal.md).

---

## Divergence 1 — the core is immune by *decision*, not by necessity

TRT claims a stronger-than-orthodox warrant for its core: the denial of *L₃* is self-refuting, so the immunity is earned. **CAC claims no such thing.** Its core rests on the historical reliability of a text and on theological commitments about the creative act, argued on exegetical and theological grounds. That is orthodox Lakatos — immunity by methodological decision.

Stating this is not a concession extracted under pressure; it is the condition of the programme being honest. A core held by decision while *claiming* necessity is precisely the conventionalist twist. See [`../1-hypothesis/hard-core.md`](../1-hypothesis/hard-core.md).

---

## Divergence 2 — accommodation is tracked as a first-class, non-progressive category

Position paper §5 reinterprets five standing cosmological tensions: low initial entropy, redshift, the Hubble tension, JWST early structure, and the dark sector. Every one of these is an **accommodation of an already-known fact**, not a prediction of a novel one. On Lakatos's criterion, accommodations contribute **nothing** to progressiveness however elegant they are, and a programme that accumulates them while producing no novel content is the textbook picture of degeneration.

CAC therefore gives accommodation its own claim role (`role: accommodation`) rather than letting it blur into `prediction`. The traceability build enforces the distinction:

- an `accommodation` claim must carry a **`forbids`** field;
- if it forbids nothing, the build records it as **non-progressive** and it is excluded from the progressiveness count;
- a `prediction` claim must carry a **`falsifies`** field, as in TRT;
- the generated [progressiveness report](../traceability/generated/progressiveness-report.md) prints the ratio, so the programme cannot mistake accumulated accommodation for advance.

**The mechanism is deliberately unflattering to the programme.** Section 5 is the most rhetorically attractive part of the position paper and the least scientifically load-bearing. Making that visible in a generated report, on every build, is the cheapest available defence against the failure mode this programme is most exposed to.

An accommodation is not worthless. It is how a programme demonstrates *coherence* — that its architecture handles the known corpus without special pleading. It simply is not evidence, and the ledger keeps the two apart.

---

## The change-legitimacy criterion (governs contributions)

- **Progressive (accept):** adds novel content that forbids something; sharpens an existing test; formalizes a prose-only claim; converts an accommodation into a prediction by finding what it forbids; or **records a refutation** — a decided conjecture, success *or* failure, is a progressive resolution.
- **Degenerating (decline):** ad hoc accommodation that reduces falsifiability; inflating a confidence label; removing a failure condition; promoting a belt hypothesis into the core to shield it; presenting *accommodation* as *prediction*, or *interpretation* as *derivation*.

The accommodation-vs-prediction line is this programme's demarcation self-test, as interpretation-vs-derivation is TRT's.

---

## The machine-checkable form

The [`traceability/`](../traceability/) layer is this methodology rendered auditable. Every claim carries a `role`, a `proof_status`, an `epistemic_status`, an acyclic `depends_on` graph (the circularity discipline), a `risk_if_false`, and — by role — a `falsifies` or `forbids` field. The generated coverage, risk, open-problem and progressiveness reports are the programme's standing self-appraisal, regenerated in CI.

Confidence labels: **HIGH · MEDIUM · LOW · UNCERTAIN** in prose; schema enum `established / argued / conjectured / open` in traceability.
