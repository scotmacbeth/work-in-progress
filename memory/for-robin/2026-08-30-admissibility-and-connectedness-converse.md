# For Neil / Robin — Gap 3 closed, and the §9bis dichotomy refuted
**2026-08-30, third PROVE of the day.**
Proof: `proofs/2026-08-30-admissibility-and-the-connectedness-converse.md`.
Registry: `left-adjoint-over-vec` → subtree `gap3-converse` (validates `proved`).
Code: `scratch/connectedness-converse/verify.py` (5 blocks, green).

## The one-paragraph version
This morning's session proved: *`C(I,−)` preserves coproducts ⟹ `(−)◁q` has a left adjoint for
every `q`*, over any closed symmetric monoidal cocomplete base. It left open whether connectedness
is **necessary**. It is — on both poles where the question can be asked — and the reason it cannot
be asked anywhere else is *the same connectedness condition*. Along the way the base `Set_*`
(pointed sets under smash) refutes the dichotomy I floated this morning.

## Four results

**A. `Set_*` refutes the §9bis dichotomy.** I conjectured that `◁` exists on `Fam(C^op)`
essentially only when `1_C` is a generator (the `Set` pole) or `1_C ≅ 0_C` (the linear pole).
`Set_*` has a **zero object** — so it looks like the linear pole — but `◁` does not exist there.
Take `p = ⟨S^0∨S^0⟩` and `q = ({1,2},(S^0,S^0))`, so `⟦p⟧⟦q⟧X = (X∨X)^2`. Matching
`|⋁_d[N_d,X]| = 1 + Σ_d((m+1)^{n_d}−1)` against `(2m+1)^2` as polynomials in `m := |X|−1` forces
four summands with `|N_d| = 3` and **minus four** with `|N_d| = 2`. `Set_*` sits on neither pole:
`S^0` is tiny but `S^0∨S^0` is not, so no collapse; and the wedge is not disjoint, so no
extensivity. **`1_C ≅ 0_C` is a symptom of the linear pole, not a characterisation of it.**

**B. On the extensive pole, admissibility FORCES connectedness.** If `C` is nontrivial, infinitary
lextensive and cartesian closed, and `Fam(C^op)` is closed under `◁`, then `1 = I` is connected —
so by this morning's Theorem 1 the left adjoint exists for every `q`. **One cannot even pose a
counterexample there.** The mechanism is the one that killed `Set×Set`, now in its proper
generality: `Fam(C^op)` gives an object **one external shape set**, and when `1 ≅ A ⊔ B` splits
`C ≃ C/A × C/B`, the object `[A, T·1] = (T·1_1, 1_2)` demands the two counts `|T|` and `1` at once.
The small lemma that does the work is pretty and may well be folklore: *in a lextensive category,
`1 ≅ 1 ⊔ Z` implies `Z ≅ 0`* — because `θι_1 : 1 → 1` is a map into the terminal object hence the
identity, disjointness makes the pullback of the two legs initial, and the pullback of `id_1` along
anything is that thing.

**C. On the collapse pole the unit is always disconnected.** If every object is copower-tiny (the
hypothesis under which `◁ = ⊗`), then `I` is not connected. The proof is a two-step chase and uses
**no cardinality argument** — deliberately, because over `Vec/𝔽₂` at dimension `(1,1)` both sides of
`γ` have four elements and a counting check passes. That is the second session running where the
smallest case is a cardinality collision. Build the map.

**D. Why the converse cannot be a statement about `C` alone.** When `I` is connected, `⟦−⟧` is full
and faithful (T1), hence injective on objects up to iso, so `p◁q` is *determined* by
`⟦p◁q⟧ ≅ ⟦p⟧⟦q⟧` and "has a left adjoint" is a property of `C`. When `I` is disconnected it is not:
over `Vec_fd`, `({∗},k^2)` and `({1,2},k)` present the same functor `X ↦ X⊕X` and are not
isomorphic. **Theorem 1's hypothesis is simultaneously what makes its converse true and what makes
its converse meaningful.** This is also why the standing caveat "`◁ := ⊗` is a definition, not a
deduction" can never be discharged over `Vec` — and it tells us which of this morning's two
necessity proofs to trust: the binary-product one (robust to re-choosing `◁`), not the terminal-
object one.

## What I would want a second pair of eyes on
1. **Novelty.** Lemmas E1/E2 (terminal rigidity in extensive categories) smell like folklore —
   Carboni–Lack–Walters is the place to look. I claim no priority for them; I do not know about
   Theorem B.
2. **Scope of Theorem B.** It is a theorem about **my** `Fam(C^op)`, with one *external* shape set.
   Dorta–Jarvis–Niu `2305.05655` work with an indexed formulation; if their shape data is indexed
   per component then `Set×Set` is fine for them and Theorem B says something about my convention
   rather than about generalized polynomials. **I have not read them closely enough to say.** This
   is now the single most important thing on my browse list.
3. **The middle region.** A separator for the converse would have to be `◁`-admissible,
   non-collapse, and closed symmetric monoidal with `⊗ ≠ ×`. I have no example and no proof that
   none exists. Lead: `I ≅ I_1 ⊔ I_2` gives `X ≅ (X⊗I_1) ⊔ (X⊗I_2)` for all `X` — an idempotent
   splitting shape. If one shows `I_i ⊗ I_j ≅ 0` for `i ≠ j`, Theorem B runs without cartesianness.

## The sentence for the grant
*A composition calculus for processes needs its resource base to be set-like or linear. On a
set-like base the external shape data is visible inside `C` as a copower of the terminal object,
`Fam(C^op)` embeds in `[C,C]`, substitution is canonical, and the slot-reindexing left adjoint
always exists. On a linear base none of the three holds — and each failure is the same arithmetic
fact, that `C(I,−)` does not preserve coproducts. In between, on a "pointed" resource base where
every type has a distinguished trivial inhabitant but resources do not add, substitution does not
exist at all.*
