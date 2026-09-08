# For Neil — QPF as the collapse-locus tool, and a dilator flag (2026-09-12)

Two formalisation-angle items from this week's browse, both grant-relevant, both honestly scoped.

## 1. QPF is the missing Lean tool for the collapse-locus objects (a real bridge, worth pursuing)

The admissibility program keeps producing, at the collapse/flexible pole, objects where the extension
functor `⟦−⟧` is **not injective on objects** — over `Vec_fd`, `({∗},k²)` and `({1,2},k)` present the same
functor `X↦X⊕X` and are not isomorphic (this is Theorem D from the connectedness-converse proof). I have
been carrying this for a month as a *caveat*: "`◁ := ⊗` on the collapse locus is a choice of presentation,
not a deduction."

The browse this week deep-read **Avigad–Carneiro–Hudon, "Data Types as Quotients of Polynomial Functors"
(ITP 2019, `10.4230/LIPIcs.ITP.2019.6`)** — the ancestor of Mathlib's `Data.QPF.Multivariate`. A QPF is a
functor `F` with a polynomial functor `P` and a **split surjection** `abs : P ⟹ F`. That is *exactly* the
type-theoretic form of `⟦−⟧`-non-injectivity: the collapse-locus "container" is a **quotient/retract of a
polynomial functor**, i.e. a QPF, not a literal polynomial functor. `abs`/`repr` names the retraction; the
"choice" Theorem D isolates is the datum QPF quotients away.

**Why this matters for the grant's formalisation deliverable:** it turns a caveat into a Lean-ready
construction. The concrete next step is a `/lean` pass — take one collapse-locus container we already have
and check whether the QPF `Wequiv`/`Mcongr` machinery quotients it cleanly. Live Lean 4 package:
`github.com/alexkeizer/QpfTypes` (work-in-progress, not yet Mathlib-integrated). Full write-up in
`connections/qpf-is-the-tool-for-collapse-loci.md`.

I am fairly confident of this one — the match is a shared *universal property* (quotient of the
representable data), not a shared number or symbol, so it is not one of the collision traps I have been
burned by.

## 2. A dilator flag — outside my competence, flagging rather than chasing

On the leanprover Zulip ("Ordinal notations and QPF", 2026-01-19, still unanswered) someone builds a
QPF-based ordinal-notation system below ε₀ and **speculates that a QPF might essentially be a Girard
dilator (or a "ptyx"), or a restricted version of one.** If true, this would tie the
polynomial-functor / container program to proof-theoretic ordinal analysis — a bridge nobody has drawn,
and one that lands on the grant's named formalisation angle.

**I cannot evaluate this** — dilator theory is not in my store, and I will not pretend otherwise. Flagging
it because it is cheap to note and squarely grant-shaped; if it is worth an hour of someone who knows
dilators (or a pointer from you), that hour is well spent. If not, no loss.

*(Both items are also in tomorrow's daily email to you; this note is the durable version with the
locators.)*
</content>
