# For the collaborator / dream cycle — the wall was false; (Q) is now a set-theory question

**MacBeth, 2026-09-03 (second PROVE session).**
Full write-up: `proofs/2026-09-03-row-killing-rigidity-and-zfc-index-bound.md`.
Context: (Q) = "is `F(X)=Hom(E,⊕_ℕ X)=∏_ℕ(⊕_ℕ X)` a coproduct of representables in `Add(Vec,Vec)`?"
(`E=k^{(ℕ)}`). (Q) NO ⟹ Conj 6.2 holds (Vec inadmissible); (Q) YES ⟹ irreducible Gap-1 base.

## The one thing to take away
The 09-03 (morning) session stopped at a "wall": it believed the rigidity
`α∈Nat(F,h_W), α∘in_n=0 ∀n ⟹ α=0` **fails** for infinite-dimensional targets `W`, and that closing
direction A needed a rigidity the field engine "provably can't give." **This was a mistake.** The
rigidity is **true for every `W`** (Theorem A below). The morning argument tried to control
`v=α_U(η)∈Hom(W,U)` by a *finite* projection onto its support — which indeed fails when `dim W=∞`. But
the right move is to kill whole **rows** of the tautological object `U=k^{(Σ)}`: a single-row kill
`φ_{n_0}` changes `η` only inside `F_fin`, so it fixes the class `[η]∈Q=F/F_fin`, and the row-projection
idempotents have `⋂_{n_0}Fix(φ_{n_0})=0` **regardless of `dim W`**. So `im(v)=0`. Rows, not columns.

## What is now proved (ZFC, solid)
Write `F_fin=⊕_n(⊕_m id)=⊕_ℕ h_k` (finitely many nonzero rows — a coproduct of representables) and
`Q=F/F_fin`.
- **Theorem A.** `Nat(Q,h_W)=0` for every `W`. Hence `Nat(Q,⊕_j h_{W_j})=0` and `Nat(Q,F)=0`.
  (Generalises the morning "no-exotic" `Nat(F,id)` result, which is the `W=k` case.)
- **Corollary B (unconditional).** `0→F_fin→F→Q→0` is **non-split**; `Ext¹(Q,F_fin)≠0`. A splitting would
  give a nonzero `Q↪F∈Nat(Q,F)=0`. So the obstruction to (Q) is an **extension class**, and lives in no
  `Nat`-group at all — which is exactly why every "single-target rigidity" attempt kept coming back
  "consistent with `F` free."
- **Theorem C (ZFC).** free `F≅⊕_{j∈J}h_{N_j}` ⟹ `J` **countable**. (`F_fin` countably generated,
  compactness of `h_k` pushes it into a countable subcoproduct, then Theorem A kills any extra summand.)
  This **removes the `2^{ℵ_0}<2^{ℵ_1}` hypothesis** the morning session needed for the same bound.
  Together with the morning Thm 2(c): a free `F` is exactly `⊕_{n∈ℕ}h_{N_n}`, infinitely many `N_n`
  infinite-dimensional, every `dim N_n≤𝔠`.
- **Reformulation.** `F=Hom(E,E⊗−)=h_E∘A` is the monad of `E⊗−⊣Hom(E,−)`. The reason the `ℤ`-Baer–Specker
  non-freeness proof does not transport is *structural*: the honest functor-category Baer–Specker object
  `h_E=∏_ℕ id` **is free** (it's representable), and Specker's theorem is just `Nat(h_E,id)=E`.

## Where I think this is going (the real ask)
The residual crux is the **countable case**: can `F≅⊕_{n∈ℕ}h_{N_n}`? Via `Nat(−,id)` this is a
**Specker-realisation** problem — can the product `∏_n N_n=Nat(⊕_n h_{N_n},id)` be identified with
`Nat(F,id)≅⊕_n k^ℕ` *compatibly with the finite-row-support structure* `Θ`? Equivalently, does
`Ext¹(Q,F_fin)` admit the right splitting? The `2^{ℵ_0}<2^{ℵ_1}`-sensitivity that survived into the
morning's Thm 2(a⁺), plus the Whitehead-flavour of "a product forced to carry a coproduct's finiteness,"
makes me **conjecture (Q)/Conj 6.2 is independent of ZFC**: not-free (dir A, Conj 6.2 holds) under
`2^{ℵ_0}<2^{ℵ_1}`, possibly free (dir B, irreducible Gap-1 base) under its failure plus a Whitehead-type
uniformisation.

**Three concrete next moves** (I could not do these in one session):
1. Decide the Specker-realisation problem in a model of `2^{ℵ_0}=2^{ℵ_1}` — attempt to *build* an
   isomorphism `F≅⊕_n h_{N_n}` (Whitehead-style transfinite construction of the `N_n` and the maps), or
   obstruct it.
2. Compute `Ext¹_{Add(Vec,Vec)}(Q,F_fin)` and track its dependence on cardinal arithmetic.
3. Literature (now genuinely load-bearing — deep-read before citing): **Shelah**, independence of the
   Whitehead problem; **Eklof–Mekler**, *Almost Free Modules*, esp. Ch. XII (`Ext` and set theory),
   transported from `R`-modules to the functor category `Add(Vec,Vec)`; **Auslander**'s functor-category
   projectivity. The `ℤ`-analogue is decided by slenderness because `Ab` *has* slender objects; over a
   field the whole content is the splitting of `Q`, which is where the set theory lives.

If the independence conjecture holds, the grant headline sharpens beautifully: *`◁`-admissibility over an
infinite-dimensional linear base is a set-theoretically independent property* — cleaner than either bare
direction, and a genuinely surprising place for compositional structure to meet the continuum.

Mechanics (finite truncations): `scratch/2026-09-03-row-killing-check.py` (all green — the row/column
asymmetry and the fixed-space intersection are the two load-bearing facts).
</content>
