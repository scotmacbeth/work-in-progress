# PROVED: Workers ⊗-grading is a retract of BHM ▷-grading (+ the grading-compatibility story)

**MacBeth, 2026-08-29 (PROVE session).** For Neil / Robin.
Full theorem: `proofs/2026-08-29-workers-retract-of-bhm-grading.md`.
Registry: `proofs/registry/workers-retract-of-bhm-grading.json` (validates, `proved`).
Code (verified n≤3): `.claude/scratch/verify_retract.py`, `verify_p3.py`.

## One line
On the store family `ΔS = S·y^S`, the Workers grading (Dirichlet `⊗`,
`ΔS⊗ΔT = Δ(S×T)`) is a **canonical non-trivial retract** of the BHM grading
(composition `▷`, `ΔS▷ΔT`) — *not* equal, *not* a fibre — and the store
comonad's comultiplication is exactly the extra structure `▷` carries that `⊗`
collapses.

## What's proved
Let `A = ΔS⊗ΔT = Δ(S×T)` (shapes & positions `S×T`), `B = ΔS▷ΔT` (shapes
`S×T^S`, positions `S×T`). At `|S|=|T|=2`: `A = 4y⁴`, `B = 8y⁴`.

1. **Retract (P2).** Section `σ:A→B`, `(s,t)↦(s,const_t)`; retraction `r:B→A`,
   `(s,g)↦(s,g(s))` (self-evaluation). Both identity-on-positions. **`r∘σ = id_A`**
   as genuine Poly morphisms (the variance is the point: backward maps compose in
   reverse, both identities); `σ∘r ≠ id_B`. The idempotent `e=σr` collapses each
   branch map `g` to the constant at its self-evaluation `g(s)`.

2. **Coherence (P3a,b).** `σ` satisfies the **oplax** associativity hexagon
   (both composites land on the fully-constant shape `(s,const_t,const_u)`); `r`
   satisfies the **lax** hexagon ("self-evaluation is associative":
   `(s,g,k) ↦ (s,(g(s),k(s,g(s))))`). Both unit-coherent; `σ,r` natural under
   bijections.

3. **The collapse (P3c) — "`⊗` is the diagonal of `▷`".** With `d:S→S×S` the
   diagonal, **`r ∘ δ = Δ(d)`** (π₂ version), where `δ:ΔS→ΔS▷ΔS` is the store
   comultiplication. So `δ` is a **lift of the ⊗-diagonal along the retraction
   `r`**. The off-diagonal data — the non-constant branch maps `g` that `▷`
   produces and `e=σr` discards — is precisely the failure of `▷` to be the
   `⊗`-diagonal.

4. **Impossibility (P3d).** `σ∘Δ(d) = e∘δ =: δ'` (branch `const_s`) is
   **coassociative but not counital** (right counit law fails) ⟹ `δ'` is **not a
   comonad**. Hence the naïve "oplax functor sends the diagonal comonoid to a
   comonad" recipe cannot produce the store comonad. **Verdict:** `Δ` is oplax
   (`σ`) and lax (`r`) into `(Poly,▷)` **only on the core groupoid `(Set_≅,×)`**;
   on the full cartesian `(Set,×)` it is neither a genuine (op)lax monoidal
   functor (the store comonad is *internal*, not transported along `σ`).

## Why it matters for the grant
Two composition disciplines on the *same* carrier `ΔS`, now explicitly related:
- **⊗ (Workers):** state *entanglement* — two workers' states combine into
  `Δ(S×T)`.
- **▷ (BHM):** state *nesting* / store-of-store — `ΔS▷ΔT`.
They are distinct products; the retract `(σ,r)` is the exact bridge, and the
store comonad is the measure of what nesting sees that entanglement collapses.
This sharpens (does not subsume) BHM ACT 2026 and the Snoc-Trees free-ℕ grading:
**one graded line, three genuinely different products.**

## Honest scope / open threads
- General proofs complete; computation covers `n≤3` (hexagons to `(2,3,2)`).
  These are natural-in-bijections polynomial identities, so small `n` is
  conclusive for the qualitative claims.
- The "`σ` is the essentially unique natural bifunctorial comparison" step
  (used to say *no* comparison reproduces the store comonad) is argued from the
  type/naturality constraint; a fully formal enumeration of natural
  transformations `Δ(-×-) ⇒ Δ(-)▷Δ(-)` is left as a `computed`-level remark —
  not load-bearing for the impossibility.
- **Lean target?** The retract `r∘σ=id` and `r∘δ=Δ(d)` are clean, finite,
  defeq-flavoured — good candidates to sit next to `lean-lemma31-comonad-level`.
  Flagging for a possible LEAN.md.
