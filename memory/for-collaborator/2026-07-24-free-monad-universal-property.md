# Free-monad universal property proved — Neil's Ch4 milestone 3 is now complete

**MacBeth → Neil (cc Robin) — 2026-07-24**

## Headline

The **one open gap** in Neil's Ch4 "Monads and Comonads" milestone-3 is closed. We now have a
container-coordinate proof that

> `U : Mon(Cont) → Cont` (forget the `◁`-monoid structure of a polynomial monad) has a **left
> adjoint** `F : X ↦ m_X`, the free-monad container, with unit `α_X : X ⇒ U(m_X)` the insertion of
> generators.

Everything else in milestone 3 was already done: the carrier `m_(S,P)=(S′,P′)` and its three
`◁`-monoid laws are Lean-verified (`Free.lean`, `Container.freeMonoid`, `Quot.sound`-only), and the
`(S′,P′)` formula matches Neil's on the nose. The missing piece — the *universal property* (the
grafting note's §6 gap #3) — is what this proof supplies.

Artifact: `proofs/2026-07-24-free-monad-universal-property.md`. Registry: node
`free-monad-universal-property` in `free-monad-grafting.json`, graded **proved** (validates).

## The one idea worth remembering

The universal property of the *free* monoid reduces, **by induction on the tree**, to the monoid
laws of the *target* monoid `M`:

- **base case (`t = lf`) = `M`'s unit law**;
- **inductive step (`t = nd s κ`) = `M`'s associativity**,

each used in *both* its forward (shape) and backward (position) component. No law of `M` is
re-proved — `M` is a given monoid and its laws are applied as morphism equations. This is the exact
mirror of the grafting note, where the free monoid's *own* laws reduced to grafting-associativity
(Lemma C/D). There the induction discharged `m`'s laws with tree combinatorics; here the same
induction discharges the *morphism* law using `M`'s laws.

Two small pleasures fell out:
- The **triangle `α;ĝ=g` uses `M`'s *right*-unit law** (both components), not the left — fitting,
  since `α` puts the generator at the root with leaf children, the right-unit configuration. The
  computational check independently reported this.
- **Uniqueness of the backward map is forced by the bijectivity of `split`** (Lemma A): any monoid
  morphism satisfying the triangle must, on positions, equal `cat_{α,w}` of the recursion — the
  same uniqueness that forced `μ♯` in the first place. So Lemma A does double duty (multiplication
  *and* uniqueness).

## The construction, briefly

`α₁ s = nd s (λp. lf)` (single node, all-leaf children); `α♯_s : leaves(α₁ s) ≅ P s`. Given
`M=(T◁Q,e_M,μ_M)` and `g:X⇒U(M)`, the induced `ĝ:m_X⇒M` is W-type recursion:
```
ĝ₁(lf)     = e_M₁(*),
ĝ₁(nd s κ) = μ_M₁( g₁ s, λq. ĝ₁(κ(g♯_s q)) ),      ĝ♯ mirrored through μ_M♯.
```
`ĝ` interprets a tree by folding: leaves ↦ unit of `M`, nodes ↦ `μ_M` of the generator `g(s)` with
the interpreted subtrees, threaded through `g♯` (which position of `g(s)` feeds which subtree).

## Part 2 (endofunctor corollary)

`⟦−⟧:(Cont,◁,I)→([Set,Set],∘,Id)` is strong monoidal (Lean-verified `⟦G◁F⟧=⟦G⟧∘⟦F⟧`) and fully
faithful (AAG representation theorem), so it preserves the free monoid: `⟦m_X⟧` has the free-monad
UP against every polynomial monad. Gambino–Kock 4.5 upgrades "polynomial" to "all monads" —
`⟦m_X⟧(A)=Σ_{t}(leaves(t)→A)=μY.(A+⟦X⟧Y)`, the free monad on the endofunctor `⟦X⟧`.

## Honesty / provenance

The **theorem is Gambino–Kock 4.5** (arXiv:0906.4931, deep-read) — prior art. The contribution is
the container-coordinate **proof** (α, ĝ by recursion, and the inductive discharge of morphism-law
/ triangle / uniqueness against a given `M`), the piece the grafting note left open. Part 1 (the
adjunction in `Cont`) is self-contained on the Lean-verified carrier + laws + elementary induction;
Part 2's "against all monads" rests on AAG + GK (flagged in §9). Verified computationally:
`scratch/free_monad_up_verify.py` — Writer(ℤ/3), Reader({0,1}, nontrivial backward), and a free
`m_Y` target; triangle + both MULT components + uniqueness, 306 exhaustive `(t,u)` pairs, negative
controls fire.

## Next

**LEAN target.** `ĝ₁` is a `PTree` recursor, `ĝ♯` the mirror; §4/§6 inductions become the two
`ContainerMorphism.ext_eq` obligations of "monoid morphism". This would make the free-monad
adjunction — carrier, laws, *and* universal property — end-to-end machine-checked, the first such.
Suggest queueing it after the cofree-comonad work (the other Ch4 half, currently paper+Python only).
