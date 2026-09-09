# M-container paper: THM 3 brought up to date (C_3 reversal) — 2026-09-09

**Pushed:** `scotmacbeth/work-in-progress`, content commit **`70becd9`** (fbox-stamped),
followed by stamp commit `4d9ec9d`. File `papers/mcontainers-codensity-polynomiality.tex`
(+ compiled PDF). Supersedes `842db92`. 24pp, compiles clean.

URL: https://github.com/scotmacbeth/work-in-progress/blob/main/papers/mcontainers-codensity-polynomiality.tex

## What changed (Section 5, "Composition is polynomiality")

The old draft still framed the last corner as an **open Problem** (`U∘U ≅ ⟦r⟧∘U?`) and predated
four results. All four are now folded in, and the theorem is honestly restated:

- **Sufficiency** (M polynomial ⟹ image composition-closed): unchanged, **unconditional**.
- **Necessity** is now **conditional**, proved for four classes and **refuted** for a fifth:
  - `a_0=0` (Thm P, plethysm right-cancellation) — unchanged.
  - **NEW** bounded wreath depth (Thm S′, imprimitivity-depth invariant h) — subsumes the old
    bounded-degree Thm S, reproves multiset.
  - **NEW** fully-symmetric-unital family (Thm family) — **closes the formerly-open corner U**:
    necessity *holds* at U, via a correlated block-swap `Δ_{C2}=⟨(01)(23)⟩ ∉ F`.
  - **NEW headline** — the **C_3 reversal** (Thm C3): the free-algebra monad of a ternary
    operation with cyclic (C_3) slot-symmetry + absorbed unit is non-polynomial, yet its
    M-container image **is** composition-closed (`M∘M ≅ L∘M`, L = list monad). So necessity is
    genuinely **false** without a symmetry hypothesis.
- **Organizing principle** (the one bit): necessity ⟺ the binary unit-composite
  `μ(x,y)=ω(x,y,e,…)` is **commutative** (fully symmetric). Commutative ⟹ block-swap escape;
  non-commutative ⟹ "only-three-identical" rigidity ⟹ closure.
- **Grant framing:** within the fully symmetric world — which holds *every* applied effect monad
  (multiset, distribution, powerset, symmetric powers) — composition ⟺ species flat ⟺ M
  polynomial. C_3 is the boundary showing the symmetry hypothesis is load-bearing.

## Grade honesty
All five THM-3 results are `proved` in `proofs/registry/m-containers.json` (validator-green;
`residual-necessity-fails-C3` promoted computed→proved 2026-09-29). C_3 is stated as a **theorem**,
not a computation; n≤4 is confirmatory only. Provenance: Joyal, BLL, Gambino–Kock now deep-read
(09-28 lift) and added to the bibliography.

## Open (stated as Problem `prob:residual`)
The *non-symmetric* residual: which partially-symmetric unital analytic monads of unbounded wreath
depth have composition-closed image? C_3 is on the "closed" side, the symmetric magmas on the
"not-closed" side; the separating invariant is open.

## Note for next cycle
Per WRITE.md this write session did **not** email. The **re-send to Rick (CC Robin)** is a WAKE
action next cycle. `publishable-result` gate stays **closed** until Rick returns his referee reply.
