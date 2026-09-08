# For Neil / Robin — (Q) is now a single homological question, and cardinality is provably neutral

**2026-09-04 PROVE.** File: `proofs/2026-09-04-Q-homological-reduction-and-target-dimension-dichotomy.md`.
Registry `left-adjoint-over-vec.json` node `conj-absorptive-dichotomy` (5 new `proved` children, validates).

## The one-line state of (Q)
Recall (Q): is `F(X)=Hom(E,E⊗X)` = row-finite ℕ×ℕ matrices a coproduct of representables in
`Add(Vec,Vec)`? YES ⟹ Vec `◁`-admissible (new Gap-1 base); NO ⟹ Conj 6.2 (absorptive dichotomy) holds.
**Still open** — but this session pins it to a single homological question and closes off *both* classical
routes to deciding it, in ZFC.

## What's new (all ZFC, all `proved`)
1. **Explicit projective presentation (Thm D).** `⊕_{η∈F(E)} h_E ↠ F` — a coproduct of 𝔠 copies of the
   representable `h_E`, surjecting onto `F` (every matrix factors through a countable-dim space). `F` is
   *not* cyclic. This is the resolution we needed to even talk about `Ext¹(F,−)`.
2. **The Ext reduction (Thm E).** From `0→F_fin→F→Q→0` (with `F_fin` projective):
   `0→coker(ρ_M)→Ext¹(Q,M)→Ext¹(F,M)→0` for all `M`. So **`F` projective ⟺ `Ext¹(F,M)=0 ∀M`** — the
   whole problem is now "is `Ext¹(F,−)` identically zero?". Cor B (last session's non-splitting) is
   *exactly* `coker(ρ_{F_fin})≠0` — a statement about the *left* term, silent on `Ext¹(F,F_fin)` where
   projectivity actually lives. That was the subtle gap in reading Cor B as "close to done."
3. **Target-dimension dichotomy (Thm F).** `Nat(F,G)` has **finite row support ⟺ `G` is built from
   finite-dimensional representables**. For such `G`, `Nat(F,G)=⊕_n Nat(A,G)`. For infinite-dim targets
   it fails — explicit witness `r∈Nat(F,h_E)` (read column 0) with `r∘in_n≠0` for all `n`. This turns
   the predecessor's heuristic "wall" (rigidity dies at infinite-dim targets) into a theorem.
4. **The Specker cokernel (Cor G).** For finite-dim-representable `G`, `coker(ρ_G)` is the **reduced
   product** `∏_n Nat(A,G)/⊕_n Nat(A,G)` — nonzero. So `Ext¹(Q,A)≠0`, `Ext¹(Q,id)≠0` (new, sharper than
   Cor B). The Baer/Specker "product-mod-coproduct" object now lives *inside* functor-category `Ext` as a
   concrete subobject; (Q) YES ⟺ `Ext¹(Q,G)` is *nothing but* this Specker cokernel, for every `G`.
5. **Cardinality is neutral (Thm H).** The `id`-dual has **no blow-up**: `Nat(h_N,id)=N` (Yoneda), versus
   `Hom_ℤ(ℤ^{(κ)},ℤ)=ℤ^κ` of size `2^κ` that powers `ℤ`-Baer–Specker. Under the forced free shape
   `⊕_n h_{N_n}` (Cor C1), every dimension invariant of `F` agrees with the free one (all `𝔠`). **No
   cardinal invariant can separate `F` from a free functor.** Combined with Theorem A (all single-target
   rigidities vanish on `Q`): *both* classical decision routes — rigidity and cardinality — are now
   theorems saying they cannot decide (Q). What's left is genuinely `Ext¹(F,−)` at an
   infinite-dimensional target: Whitehead territory.

## Why this matters for the grant / the independence bet
The predecessor *conjectured* independence because "the cardinal engine is unavailable over a field."
Thm H makes that a **theorem** (Lemma H0 is the precise reason: representables over a field are
duality-reflexive, no `2^{dim}` jump). So the independence bet is no longer a hunch — it is the only
remaining possibility given that the two classical routes are provably closed. The clean grant headline
crystallising: *compositional `◁`-admissibility over an infinite-dimensional linear base is decided by a
functor-category Whitehead problem — the splitting of `Ext¹(Q,F_fin)` — not by any cardinal or rigidity
invariant.*

## The honest hard core (next cycle)
Decide `Ext¹(F,M)=0?` at an infinite-dim `M` (e.g. `M=h_E` or `F_fin`), via the syzygy functor
`K=ker(P₀→F)` of Thm D: `Ext¹(F,M)=coker[∏_{F(E)}M(E)→Nat(K,M)]`. Direction A = a natural cocycle
`K→M` not extending to `P₀`; direction B = a Whitehead-type uniformisation extending them all (likely
needs `¬(2^{ℵ0}<2^{ℵ1})` + transfinite recursion). **Literature gate still open** and now genuinely
load-bearing: Eklof–Mekler *Almost Free Modules* Ch. XII, transported to functor categories; Shelah on
Whitehead. Thm H tells us *which* half of that literature can bite: only the uniformisation content, not
the slenderness/cardinality content.

— MacBeth
