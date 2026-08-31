# Write session 2026-07-21 — Ch "Algebraic structure on Cont": closing the structures

## Target
`books/category-of-containers.tex`, chapter `ch:algebra`. Insert a new
`\section{Closing the structures}` (label `sec:closed`) BETWEEN "The monoidal
menagerie" and "Monoids and comonoids for the four structures" (`sec:comonoid-table`,
the chapter closer per Neil 07-21).

## Edits
1. DELETE placeholder `\begin{Definition}[Closed structures]\label{def:closed}` block
   (superseded; it only cites Spivak21 = 2111.10968 which is `abstract`-grade — must
   not be load-bearing). Keep the free-monad-deferral paragraph as menagerie closer.
2. INSERT the new section after that paragraph.

## Section arc (book voice, compute-first)
Promise: by the end you can decide, for any of these tensors, whether it is closed —
and see that **closure on containers = polynomiality on sets, read through ⟦–⟧**.
Hook + Neil's warning: internal hom is a right Kan ext, need not be a container; the
honest question is *when there is one*.

1. **Dirichlet closure, as a hom of morphisms** (compute the transpose by hand).
   Held p, target q, adjunction (−⊗p) ⊣ [p,−].
   `[p,q] = (Cont(p,q),  f ↦ Σ_{i∈S_p} q[f₁ i])`. Shapes = morphisms; a position = a
   p-shape + a q-position over the delegated shape. PRIOR ART: NS Ex 4.78 eq (4.79);
   Spivak 2202.00534 Eq (44) "Dirichlet closure". Ours = mechanisation DirichletClosed.lean.
2. **Astonishment: same hom = product of composites.**
   `[p,q] ≅ Π_{i∈S_p} q ◁ (p[i]·y)`,  `⟦[p,q]⟧R = Π_{i∈S_p} ⟦q⟧(R × p[i])`.
   Collapse Cont(p,q)=Π_iΣ_t p[i]^{q[t]} by ΠΣ≅ΣΠ. Machine-checked: DirichletHomPi.lean
   (`ihomPiIso`, axiom-free, 07-21). [MacBeth, Lean-verified].
3. **General theorem (the one new bit).** Day tensor ⊙_⋆ of monoidal (⋆,I) on Set.
   Left-closed ⟺ (−)⋆B polynomial ∀B. Then `[p,q]_⋆ = Π_i q◁(p[i]⋆y)`,
   `⟦[p,q]_⋆⟧R = Π_i ⟦q⟧(R⋆p[i])`. Necessity ONE LINE: evaluate at [y^B,y]_⋆ → (−)⋆B
   (co-Yoneda). Sufficiency sketch: co-Yoneda + hom-out-of-⊔ + Poly closed under ◁, ∏.
   HANDEDNESS: formula `R⋆p[i]` (left slot) ↔ condition `(−)⋆B` polynomial (left slot).
   [MacBeth, proved]. Three instances (×,⊗,▷_S) = prior art (Spivak 2202.00534 Eqs 38–40).
4. **Is the condition ever violated? (honest open).** vacuity ⟺ every monoidal Set
   preserves connected limits per variable. NOT resolved; 3 candidates killed.
   Moral (book-worthy): polynomiality = provenance-tracking = coherence. Cautionary
   example = SUPPORT TENSOR (bifunctor+pentagon+triangle pass, yet NO natural associator
   — separator point can't record provenance). [Open].
5. **The other three, briefly.** ×: cartesian closed, exp Π_s q(−+p[s]) = uniform formula
   at ⋆=+ (× = Day-of-+); NOT locally cartesian closed (contrast). NS Thm 5.31; ALS in prose.
   ◁: not left-closed, has right coclosure (Meyers; Spivak Eqs 68–69 / NS Prop 6.57);
   naming clash remark.
6. **Beyond the census (forward pointer).** ⋉/⋊ (Dialectica, DJN 2305.05655) non-convolutional:
   ⋉ not closed, ⋊ directed-left-closed. Boundary of the Day census. Full treatment deferred.

## Citations (all deep-read+ or in-book, none load-bearing on abstract-grade)
- NiuSpivak23 (2312.00990) deep-read — Ex 4.78, Thm 5.31, Prop 6.57.
- SpivakRef 2202.00534 verified-quote — Eqs (6),(38)-(40),(44),(68)-(69). NEW bibitem needed.
- DJN 2305.05655 deep-read — ⋉/⋊. Already in bib.
- CJ, GK in-book bib — polynomial ⟺ connected limits.
- Spivak21 (2111.10968) is `abstract` — DO NOT add new load-bearing cites; drop from closed section.
- ALS (Altenkirch–Levy–Staton): not in sources.json; PROSE attribution only, formula cited to NS Thm 5.31.

## Honesty ledger
No originality for the 3 concrete closures. Morphism form = Spivak/NS. Π-form = repackaging
(but the identity itself + its Lean proof are ours). NEW = uniform biconditional + necessity
reduction. Vacuity = honest open. Keep grade-language out of prose, attributions in.
