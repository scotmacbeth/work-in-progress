# Topic: The Equivalence Chain (Containers ≃ Directed Containers ≃ Comonads ≃ Small Categories)

## Directed container, precise (repo notation)
A container `S ◁ P` (shapes S, positions P(s)) with:
- root `o : ∏_s P(s)`
- sub-shape `↓ : ∏_s (P(s) → S)`, written `s↓p`
- shift `⊕ : ∏_s ∏_{p∈P(s)} (P(s↓p) → P(s))`, written `p⊕q`
Laws:
- D1: `s↓o(s) = s`
- D2: `o(s)⊕q = q`
- D3: `p⊕o(s↓p) = p`
- D4: `s↓(p⊕q) = (s↓p)↓q`
- D5: `(p⊕q)⊕q' = p⊕(q⊕q')`

## The dictionary (proved at object level in directed-categories.tex)
| directed container | small category |
|---|---|
| shape s | object s |
| position p∈P(s) | morphism p: s → s↓p (out of s) |
| s↓p | codomain of p |
| root o(s) | identity id_s |
| shift p⊕q | composite q∘p (ORDER REVERSED) |
D1↔cod(id)=s, D2/D3↔unit laws, D4↔composition well-typed, D5↔associativity.
Corollary: |S|=1 ⟺ monoid; thin ⟺ preorder.

## The comonad (computed; this was a repo gap)
On D = ⟦S◁P⟧, DX = Σ_s X^{P(s)}:
- ε(s,v) = v(o(s))
- δ(s,v) = (s, λp.(s↓p, λq. v(p⊕q)))
Comonad laws ⟺ directed-container laws, exactly:
- left counit ε∘δ=id  ⟺  D1 (then) D2
- right counit Dε∘δ=id  ⟺  D3
- coassoc Dδ∘δ = δ_D∘δ  ⟺  D4 (shapes agree) + D5 (values agree)
Converse forced by full-faithfulness of ⟦−⟧.

## Worked atoms
- Poset **2** = {0→1}: S={0,1}, P(0)={id₀,u}, P(1)={id₁}; |D1|=3 morphisms. Full shift table verified.
- Monoid **ℤ/3**: one shape, P(⋆)=ℤ/3, ⊕ = +, comonad DX = X^3 (array/shift comonad).
These are the two generators: many-objects (poset/cat) + endo-loops (monoid).

## Morphism level: DCont ≅ Cof (NOT Cat) — RESOLVED 2026-06-09
The roadmap's "morphisms ↔ functors" was a **broken assumption**. The container
map `(f, f♯)` is *contravariant* on positions (`f♯_s : P'(fs)→P(s)`), opposite to
a functor. The correct theorem (proven + verified on 36 pairs):
**DCont ≅ Cof** (small categories + **cofunctors**). Morphism conditions (M0,M1,M2)
= cofunctor laws (C0,C1,C2). *Covariant* positions would give functors — but that
isn't a container morphism. In Poly: comonoid morphisms in (Poly,◁) = cofunctors.
→ proof `projects/proofs/2026-06-09-dcont-morphisms.tex`; cofunctors are
update-lenses, see [[cofunctors-are-update-lenses]].
**Verification count: 17 (not 20)** of 36 pairs have `#functors ≠ #cofunctors`
(corrected in the write cycle; `dcont_morphisms_check.py`). Put cofunctor is
`A⇸B / D_A→D_B`.

## The Poly-language home: Cat#
DCont ≅ Cof IS **Cat#** = ◁-comonoids with cofunctor morphisms (Libkind–Spivak
arXiv:2404.16321 "Pattern Runs on Matter"; Shapiro–Spivak arXiv:2405.13157). The
Poly community arrived at this object independently; nobody has published the
*explicit categorical proof* — that's the arXiv-note novelty. Position DCont ≅ Cof
as "the morphism structure of Cat#." (READ 2405.13157 before finalizing the note.)

## Status (current)
- directed-categories.tex (object dictionary, computed) → PR (RaggedR).
- 2026-06-09-dcont-morphisms.tex (DCont ≅ Cof, morphism level). **Needs back-port**
  of write-cycle fixes: count 17, Put direction `A⇸B`.
- `papers/dcont-cof.tex` (7pp publication note) → PR #1 (scotmacbeth fork).
- Lean M1 (representation theorem) proved → `lean/Containers/Basic.lean`.
- Lean M2 (forward: D1–D5 ⇒ comonad laws) proved → `Containers/Directed.lean`.
  Converse + bijection = **M2b (deferred)**.
- **Lean M4 (DCont ≅ Cof) DONE** → `Containers/Cofunctor.lean`, zero sorry, **zero
  axioms**, identity-on-objects iso of categories. Cof is a strict category.

Links: [[open-threads]] · [[cofunctors-are-update-lenses]] ·
[[two-atoms-zappa-szep-decomposition]] · [[duplicate-is-futures-with-provenance]]
