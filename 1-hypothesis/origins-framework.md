# The Origins Framework

> **Tier 1.** The parent framework from which CAC's five axioms are the *cosmological specialization*. Stated by JD, 2026-08-03. The [position paper](paper/CAC-v0.1.md) opens at the cosmological level; this file states the level above it, because several of the paper's commitments are consequences of these five points rather than independent posits.

## The five points

1. **The Bible is the material authoritative source of truth.**

2. **God creates or produces systems functionally mature** — Adam and Eve, the wine at Cana, miraculous healings that skip the normal biological processes.

3. **Given 1 and 2, it is reasonable to reject the hypothesis of deep time as necessary.**

4. **Systems that appear "old" are the result of a set of naturalistic Bayesian priors that do not take into account 1 and 2.**

5. **Divine intervention is by definition the exception and not the rule** — methodological designism is a reasonable normative operational model.

## How CAC specializes it

| Origins point | CAC realization | Claim |
|---|---|---|
| 1 | Genesis records genuine historical events | [CRE-001](../traceability/claims/CRE-001.yaml) |
| 2 | Functional maturity of the created order; extended to cosmology | [CRE-003](../traceability/claims/CRE-003.yaml), [CRE-006](../traceability/claims/CRE-006.yaml) |
| 2 | Operational completeness is not deception | [CRE-007](../traceability/claims/CRE-007.yaml) |
| 3 | Deep time is not necessary — a modal claim, not a denial | [CRE-008](../traceability/claims/CRE-008.yaml) |
| 4 | Apparent age is prior-dependent | [EPI-001](../traceability/claims/EPI-001.yaml) |
| 5 | Stable intelligible law after Creation Week; methodological designism | [CRE-005](../traceability/claims/CRE-005.yaml), [EPI-002](../traceability/claims/EPI-002.yaml) |
| 1–5 + Day Four | Discrete actualization of the observable heavens | [CRE-002](../traceability/claims/CRE-002.yaml), [CRE-004](../traceability/claims/CRE-004.yaml) |

## Three things the framework does that the position paper did not

**It generalizes the maturity pattern beyond creation.** The paper's instances are Adam and the fruit trees, both inside Creation Week, which leaves maturity looking like a special feature of the creation event. Point 2's further instances — the wine at Cana, healings that skip the normal biological process — are *post*-creation acts, and they establish that functional maturity is characteristic of divine action as such.

This matters directly for [CRE-007](../traceability/claims/CRE-007.yaml). The stand-up audit recorded that the paper's "operational completeness is not deception" was **asserted rather than argued**. Point 2 supplies the argument: the Cana wine had chemical properties a chemist would date to years of fermentation, and nobody at the wedding was deceived, because the artifact's purpose was never to testify to its own history. Deception requires an intent to induce false belief, and a functional artifact produced for a stated function makes no claim about its provenance. The charge does not attach.

**It states the modal claim correctly.** Point 3 rejects deep time as *necessary*, not as false. That is a weaker and much more defensible claim than the position paper implies, and the programme should hold it at that strength. What is denied is the entailment from the observational corpus to deep time; what is not asserted is that the corpus is inconsistent with it.

**It states the inference problem in the right currency.** Point 4 is the sharpest of the five. "This system appears old" is not an observation; it is a posterior, computed under a likelihood and a prior. The prior in standard practice assigns effectively zero weight to discrete actualization, so the posterior concentrates on deep time regardless of what the data are. Change the prior and the posterior moves. This is straightforwardly correct as an epistemology of the inference, and it is the correct reply to a large class of "but it *looks* old" objections.

## The reservation the programme must carry — there is no likelihood function

Point 4's argument is stated in Bayesian terms, so hold it to Bayesian standards.

$$P(H \mid E) \propto P(E \mid H)\, P(H)$$

Point 4 correctly observes that $P(H_{\mathrm{CAC}})$ is set near zero by standard practice, and that this drives the result. But the shift it recommends cannot actually be *computed*, because **CAC has not specified $P(E \mid H_{\mathrm{CAC}})$.** The programme currently has no likelihood function: no statement of what a discretely actualized cosmos should be expected to look like, in what respects, with what distribution.

Two consequences follow, and they are the programme's central problem rather than a side issue.

**The argument cannot be run, only asserted.** Without a likelihood, "the appearance of age is prior-dependent" is a correct observation about *someone else's* inference that does not yet license any inference of its own. It neutralizes an objection; it does not produce a claim.

**Without a likelihood, nothing is forbidden.** Any observation whatever can be absorbed by "your priors generated that inference." That is the unfalsifiability charge in its strongest form, and it is exactly why the [progressiveness ledger](../traceability/generated/progressiveness-report.md) reads zero. The absence is registered as [OPN-011](../traceability/claims/OPN-011.yaml), which is now the programme's sharpest open problem and the direct precondition of [OPN-007](../traceability/claims/OPN-007.yaml).

The framework is not damaged by this. A likelihood is exactly the kind of thing a research programme is *for* producing, and point 4 identifies precisely where to build it. But until it exists, point 4 is a defensive result, and the programme should describe it as one.

## Point 5 is where the programme gets its teeth

Methodological designism holds that intervention is the exception and law is the norm. Its defensive use is obvious — it blocks the charge that CAC licenses arbitrary miracle-invocation. Its *constructive* use is more important and is currently unexploited.

If law is the norm, then everything after Creation Week is ordinary physics operating on an actualized initial configuration. That is a substantive, constrained, and **falsifiable** claim, and it does not depend on relitigating the appearance of age. Ordinary law acting on a specified initial state over a short interval either does or does not reproduce what is observed, and the answer is computable in principle.

This is where the discriminator hunt should concentrate. See [`../3-prediction/discriminators.md`](../3-prediction/discriminators.md) and [OPN-006](../traceability/claims/OPN-006.yaml).

Point 5 also carries a discipline the programme must self-impose: **if intervention is the exception, then invoking it is costly.** Every appeal to actualization to explain a structure that ordinary law could have produced is a withdrawal from the programme's falsifiable content, and point 5 is the reason that is a violation of CAC's own commitments rather than merely a strategic error. This is the [degeneration watch-point](../2-theory/open-problems.md).
