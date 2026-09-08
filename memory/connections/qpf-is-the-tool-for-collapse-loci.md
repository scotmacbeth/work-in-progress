# QPF `abs`/`repr` is the formalisation tool for the collapse/identification loci

**Found:** 2026-09-12 (dream), joining the 09-10/09-11 browse deep-read of Avigad–Carneiro–Hudon to
Theorem D + [[fusion-versus-identification]] (IDENTIFICATION mode).
**Status:** `demonstrated` (pattern), 2026-09-02 `/lean`. The abs/repr retraction is machine-checked
sorry-free in core Lean 4 on the smallest genuine collapse locus — the two-leaf bag
`Bag₂ X = (X×X)/swap = Sym²X` — with the quotiented symmetry being the *proved* leaf-swap obstruction
([[effect-coeffect-arrows-first-strength]]). See `lean/Containers/Containers/QpfCollapse.lean` and
`for-collaborator/2026-09-02-lean-qpf-collapse.md`. STILL open: whether a *specific* `Vec_fd`/Gap-1
collapse-locus container quotients cleanly via ACH's `Wequiv`/`Mcongr` — the pattern is demonstrated,
the specific `Vec` identification is not yet. Both endpoints individually solid: Theorem D is `proved`
(registry `left-adjoint-over-vec`, subtree `gap3-converse`); the QPF source is **deep-read**.
**DOI correction:** ACH is `10.4230/LIPIcs.ITP.2019.6` (LIPIcs 141, pp. 6:1–6:19), NOT `.17`.

## The two things being connected

**Endpoint A — my Front-A boundary phenomenon (proved).** When the monoidal unit `I` is *disconnected*,
T1 fails: `⟦−⟧ : Fam(C^op) → C-[C,C]` is **not injective on objects**. Over `Vec_fd`, `({∗},k²)` and
`({1,2},k)` both present `X ↦ X⊕X` and are **not** isomorphic. So on the collapse pole the "container"
is *not* the functor — several non-isomorphic containers present the same functor, and "`◁ := ⊗`" is a
**choice of presentation**, not a deduction (Theorem D; the caveat carried verbatim on four proof files).
This is the IDENTIFICATION mode of [[fusion-versus-identification]]: *no change of base helps, because the
question has stopped referring; you must fix a presentation by fiat.*

**Endpoint B — Quotients of Polynomial Functors (Avigad–Carneiro–Hudon, ITP 2019).**
DOI `10.4230/LIPIcs.ITP.2019.6` (LIPIcs vol. 141, pp. 6:1–6:19 — **note: a 09-11 "correction" to `.17`
was itself wrong (`.17` is an unrelated Forster–Kunze paper), fixed back to `.6` on 09-12; deep-read
pp. 1–10/19**). A **QPF** is a functor `F` equipped with a
polynomial functor `P = A ▷ B` (their container notation) and a **split surjective** natural
transformation `abs : P ⟹ F` (with `repr`, `abs_repr`, `abs_map`). Motivation: polynomial functors (=
containers) are closed under composition and (co)initial (co)algebras but **NOT under quotients**
(`finset`/`multiset` are Isabelle BNFs but not polynomial functors, by cardinality). The QPF typeclass is
a **retraction of a container onto the functor it presents**; `Wequiv` (initial-algebra) / `Mcongr`
(final-coalgebra) are the quotient relations. Direct ancestor of Mathlib's `Data.QPF.Multivariate`; live
Lean 4 successor `github.com/alexkeizer/QpfTypes` (WIP, not Mathlib-integrated).

## ★ The connection

> **`abs : P ⟹ F` split surjective is the type-theoretic form of "`⟦−⟧` is non-injective on objects".**
> The collapse-locus objects that my `Fam(C^op)` generality program keeps producing — where several
> containers present one functor — are **exactly QPFs**: functors that are quotients/retracts of a
> polynomial functor, not literal polynomial functors themselves.

So the standing IDENTIFICATION caveat has a **constructive dual**. "Work with the functor, not the naive
container, because the container is a choice" is, on the Lean side, precisely *"work in the QPF typeclass:
`abs`/`repr` names the retraction, and the choice is quotiented away."* The non-injectivity of `⟦−⟧` —
recorded for a month as a *caveat* on the Vec/collapse results — is here a **feature with an existing
formalisation pattern**. First time the T1-failure has an upside rather than a warning label.

## Why it is a genuine seed connection, not a collision

Guard against the very failure this file's cousin ([[fusion-versus-identification]], COLLISION) warns of:
*name the invariant, ask what functor it is a shadow of.* Here the match is not a shared number or symbol
— it is a shared **universal property**: both `abs`-split-surjectivity and `⟦−⟧`-non-injectivity say the
functor is a *quotient of the representable data*, and the retraction (`abs`/`repr`) is the same datum as
the "choice of presentation" Theorem D isolates. The map matches, not just the count. (Contrast the DJN
`◁` symbol collision, same file §"FOURTH COLLISION": there the *operation* differed under a shared symbol.
Here the operation — retract a container onto its extension — is the same on both sides.)

## What this buys

1. **A Path-6 deliverable with a Front-A motivation.** The grant's formalisation angle wants Lean
   artifacts that are *motivated by the theory*, not toy. "Formalise the collapse-locus containers as
   QPFs" is exactly that: it is the Lean realisation of Theorem D's identification phenomenon.
2. **A concrete `/lean` next step.** Take a specific collapse-locus container already built (e.g. the
   `Vec_fd` `◁=⊗` objects, or a Gap-1 `Set×Vec_fd` position) and check whether `Wequiv`/`Mcongr` quotient
   it cleanly. If yes → the connection is demonstrated, not just asserted. If the quotient is awkward, the
   awkwardness *is* information about how the collapse differs from finset/multiset.
3. **It sharpens the audit target from [[fusion-versus-identification]].** The results "at identification
   risk" (Vec-comonoid/algebroid, linear-attention `⊙` — they name *containers* over `Vec`) are exactly
   the ones that should be **restated as QPFs / their extensions** rather than as containers. The QPF
   framing is the honest object; the container framing is the choice.

## Honest scope

- The correspondence is at the level of *shape* (both say "quotient of a polynomial functor"); no theorem
  is claimed that a specific collapse container **is** a QPF in Mathlib's precise sense until the `/lean`
  check runs. `speculative` until then.
- Avigad–Carneiro–Hudon read pp. 1–10/19 only; the weak-pullback §5, data-type package §6, and future
  work §7 are unread. Any technical claim from those sections needs the rest of the paper.
- Adjacent, **not** claimed here: the QPF ↔ Girard **dilator/ptyx** speculation (leanprover Zulip,
  "Ordinal notations and QPF", 2026-01-19, unanswered) — outside my territory, flagged to Neil in
  `for-collaborator/2026-09-12-qpf-tool-and-dilator-bridge.md`, not evaluated.

Related: [[fusion-versus-identification]], [[fullness-unit-connectedness]],
[[lemmas-sufficient-extensive-pole-pi0]], [[gap1-inhabited-setxvec-rigid-flexible]],
[[the-summary-is-what-gets-audited]], [[contravariance-is-fibrewise-op]].
</content>
