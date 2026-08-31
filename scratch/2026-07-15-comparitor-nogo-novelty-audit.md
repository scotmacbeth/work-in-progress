# Novelty audit — the comparitor no-go (2026-07-15)

**Verdict: PARTIALLY-KNOWN. Delta = only the "descends ⟹ degenerate" direction for directed
containers.** The comparitor, its invertibility boundary (= exactly the degenerate class), and the
⊗-comonoid classification are all Spivak's. Position any write-up as "Eq. (33) on the diagonal, plus
the converse" — NOT a fresh no-go.

## The single most dangerous citation — READ IN FULL FIRST
Spivak, *Reference: Categorical Structures on Poly*, **arXiv:2202.00534**, specifically
**Eq. (32)–(33)** + the **⊗-comonoid classification** (paragraph at/after Eq. (212)–(215)) +
**footnote 16**. Local: `/home/agent/git/ghani-containers/pdf/spivak-poly/Spivak_Reference-Categorical-Structures-on-Poly_2022.pdf`.

## What is Spivak's (cite, do not claim)
- **Comparitor `Indep : p⊗q → p◁q`** = 2202.00534 Eq. (32); = Niu–Spivak Ex. 6.85 `o_{p,q}`
  ("inclusion of order-independent positions of p◁q").
- **Eq. (33): `Indep_{p,q}` iso iff `p` linear (Ay) or `q` representable (y^A).**
  On the diagonal `p=q=c`: `Indep_{c,c}` iso iff `c = Ay` or `c = y^A` — **exactly the degenerate
  class.** So (degenerate ⟹ descends) is an immediate corollary; the boundary is already written down.
- **⊗-comonoids classified** (after Eq. (212), line ~3195): the (⊗)-comonoids `(p,ε,δ)` are
  **"sets of monoids"** — for each position `I:p(1)`, the fibre `p[I]` carries a monoid structure.
  ⚠️ **This is NOT the degenerate class.** Any polynomial whose every fibre is a monoid qualifies.
  ⟹ **The degeneracy in my claim CANNOT come from being a ⊗-comonoid. It must come from the
  DESCENT / double-comonoid compatibility** (the SAME carrier being a ◁-comonoid AND a ⊗-comonoid,
  compatibly, in the duoidal sense).
- **Footnote 16** (line ~2444): "the only (⊗)- or (⊳)-comonoids in **Poly_cart** are linear (Ay)."
  A genuine no-go — but restricted to the **cartesian-map subcategory**, so NOT my statement.
- **Duoidal framework** = Aguiar–Mahajan "double comonoids" in a 2-monoidal (duoidal) category.
  No off-the-shelf A–M theorem collapses double comonoids to a degenerate class. (In fact
  Niu–Spivak Prop. 8.79 / 2202.00534 line ~3344: `⊗` lifts to `◁`-comonoids as the cartesian
  product of categories — the general slogan runs the OTHER way.)

## What is left for MacBeth (the delta)
Only the **"only if" direction, specialized to directed containers**:
> descent of a ◁-comonoid's comultiplication through `Indep` forces the carrier onto the Eq.-(33)
> boundary (either `Indep` iso here, or a direct fibre argument: a category whose composition is
> order-independent is discrete-or-one-object).

A short, honest computation — one lemma away from published results. Clean statement:
**"Double comonoids in the duoidal `(Poly, ◁, ⊗)` are exactly the degenerate polynomials."**

## ⚠️ FIRST THING THE PROVE SESSION MUST DO — fix the definition of "descends"
The audit flags this as the crux. "Descends" is a priori WEAKER than "Indep is iso":
- iso ⟹ descent trivially (easy direction).
- but δ:c→c◁c could in principle factor through the order-independent IMAGE of `Indep` without
  `Indep` being invertible.
So pin down: does "descends" mean **(a)** δ factors through `Indep`, or **(b)** the full
Aguiar–Mahajan double-comonoid axioms hold? The theorem statement changes with the answer. Compute
the smallest non-degenerate directed container (2 shapes, or the walking arrow category `• → •`) and
check by hand whether its δ factors through `Indep` — that single example likely settles truth AND
the right definition.
