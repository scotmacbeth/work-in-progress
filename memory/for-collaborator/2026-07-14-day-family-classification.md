# For Neil / Robin — the Day family on Poly is now classified

**2026-07-14. Deep-work session. Result: three theorems, all proved.**
Full write-up: `proofs/2026-07-14-day-family-classification.md`.

## The one-sentence version

**The categorical product is the unique pointwise monoidal structure on containers** — and
that is not a fact about Day convolution, it is a fact about `Cont`. Day convolution is
merely the telescope through which one can *see* it.

## What I actually proved

**Theorem A (classification).** The Day construction is an **equivalence**
```
   { monoidal structures on Set }  ≃  { "convolutional" monoidal structures on Cont }
```
where *convolutional* means the tensor (D1) preserves coproducts in each variable and (D2)
sends representables to representables. The whole literature — Niu–Spivak Prop. 3.79,
Spivak's *Reference* — states only the **existence** direction ("for any monoidal structure
on `Set` there **is** one on `Poly`"). Nobody states a converse. The mechanism is one line:

> **`Cont` is the free coproduct completion of `Set^op`.** A container *is* a family of
> sets. So a tensor satisfying (D1) is *determined* by its restriction to representables,
> and (D2) says that restriction lands in `Set^op`.

Everything else is bookkeeping. (Also: the unit's representability is a *consequence* of
(D1)+(D2), not an assumption — Lemma 3.2.)

**Theorem B⁺ (uniqueness).** Any monoidal structure on `Cont` is pointwise iff it *is* the
cartesian one. No Day hypothesis needed: pointwise-ness forces (D1) and (D2), so Theorem A
applies and the classification does the rest. There is also an **effective test** (B′): when
the unit is initial, there is a canonical `κ : A + B → A ⋆ B`, and the tensor is pointwise
iff `κ` is a bijection.

**Corollary (the sharp form).** `Cont` carries a **proper class** of pairwise non-isomorphic
convolutional monoidal structures — Spivak's `▷_S`, from `A ∨_S B = A + A×S×B + B`
— **all of which share the product's unit** (the terminal object `1 = y^∅`). Exactly one,
`S = ∅`, is the product. So the product is singled out by *none* of the cheap invariants:
not the unit, not symmetry, not coproduct-preservation, not semicartesianness. Only `κ`
separates them. This is the answer to "is the Day family actually large?" — it is large *in
a way that defeats every invariant except the right one*.

**Theorem C (what the comparitor is).** The map `p ⊗ q → p ◁ q` is the **counit of a
coreflection**:
```
   p ⊗ −  =  Lan_J ( (p ◁ −) ∘ J )        J : Set^op ↪ Cont the representable embedding
```
i.e. `p ⊗ −` is the **terminal coproduct-preserving approximation** to `p ◁ −`. `◁` satisfies
(D2) exactly, and (D1) only in the *left* variable; its restriction to representables is
`(A,B) ↦ A × B` — **the same restriction as `⊗`**. So `⊗` is the Day-ification of `◁`, and
the comparitor is the universal map. This is the precise sense of "`⊗` is `◁` with the
dependency switched off".

## Where I was wrong, and it matters

**The map `dirToSeq` is not mine. It is prior art six times over.** I ran a full novelty
audit of the seed first (thank god). It is the duoidal *comparitor* (Shapiro–Spivak eq. 5),
*Indep* (Spivak *Reference* eq. 32), the lens `o_{p,q}` (Niu–Spivak Ex. 6.85, Prop. 6.87),
Spivak–Garner–Fairbanks Prop. 7.10. Its lax monoidality is Niu–Spivak Ex. 6.85. Its
invertibility for linear `p` / representable `q` is Spivak eq. (33). The registry node
`dirichlet-is-uniform-fragment-of-seq` carried a **NOVELTY UNAUDITED** flag; it is now
resolved, and the honest verdict is *not new*. I emailed you this as a conjecture-of-novelty
earlier today — **please disregard that claim.**

What *is* new is the **universal property**. In the literature the comparitor is always
*derived* by plugging `y` into the duoidal interchanger. Nobody says what it **is**. Theorem
C says what it is, and two of the three known facts about it fall out as corollaries (it
exists — it's a counit; it's invertible on representables — counits of `Lan` along a fully
faithful functor are).

**And the old dead end is now explained.** `dirichlet-strict-monoidal` (the "⟦–⟧ is strict
monoidal for `⊗`" category error) was not a bookkeeping slip. Corollary 4.5: `⟦–⟧` is strong
monoidal into the *pointwise* product iff the tensor **is** the cartesian one. There was no
version of that claim that could have been true.

## Two things I'd flag

1. **Prop. 5.2** (coherence of `∨_S`) is a normal-form argument — the `n`-fold tensor is
   `⊔_{∅≠K⊆[n]} (Π_{i∈K} X_i) × S^{|K|−1}`, increasing subsequences with `S`-separators;
   every bracketing maps canonically onto it, so any two composites of associators agree
   (Mac Lane's coherence-by-normal-form), pentagon included.

   **This was not pedantry, and the reason is worth your attention.** Spivak merely *asserts*
   `∨_S` is monoidal (Reference eq. 9, credited to Garner; it's Haskell's `These`), and
   Niu–Spivak Ex. 3.82 asks the reader to check only **associativity-as-a-bijection**. A
   **negative control** in the verification run constructed the *label-swapping* variant `α'`
   of the associator: it is a natural bijection, and it **is associative** — and it **fails
   the pentagon** (16/243 cases; you need `|S| ≥ 2` to see it at all). So associativity does
   not suffice, and the cited sources do not actually establish what they assert. Cor. 5.5
   depends on this, so it had to be proved. **I'd like it in Lean.**

   Relatedly: **I do *not* claim `∨_S` is symmetric.** There's an evident candidate braiding,
   and Spivak's `⊙` is stated for symmetric structures — but I never checked the hexagon, and
   a braiding has to re-match the `S`-separators, which is *exactly* where the negative
   control shows coherence can fail. Nothing needs symmetry, so I dropped the claim rather
   than assume it.

2. **One open gap, not load-bearing (Question 5.6).** Theorem B assumes the pointwise iso is
   natural in `p, q`. If one only assumes it exists for each `p, q` (natural in `X` alone),
   I get `A ⋆ B ≅ A + B` as bare bijections and `I = ∅`, but I cannot show `κ` is bijective.
   *Is there a monoidal `(⋆, ∅)` on `Set` with `A ⋆ B ≅ A + B` for all `A,B` but `⋆ ≇ +` as a
   bifunctor?* I believe not; I have no proof. Nothing depends on it.

## Why this matters for the grant

This is the "four monoidal structures" chapter's spine, and it upgrades it from a *list* to a
*classification*. It says how Neil's four structures relate rather than merely enumerating
them:

* `×` and `⊗` are the two Day tensors (of `+` and `×` on `Set`).
* `+` is not Day, and fails for a triviality: **every Day tensor annihilates `0`** (shapes
  multiply, `S × ∅ = ∅`), and the coproduct never does.
* `◁` is the **near miss** — (D2) exactly, (D1) in one variable — and `⊗` is precisely its
  Day-ification, with the comparitor as counit.
* Among the *proper class* of Day tensors, exactly one is pointwise.

**Next:** `/lean` targets, in order of value — (i) Theorem B′ and the `κ` test, (ii) Prop. 5.2
coherence of `∨_S`, (iii) Theorem C's coreflection. Registry updated and validating;
`day-family-classification` and children all `proved`.
