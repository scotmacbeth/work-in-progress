# For Rick — your Ext hypothesis was right (in degree 0) and structurally void above it

**MacBeth, 2026-08-20 deep-work.** Full proof: `proofs/2026-08-20-emergent-holonomy-is-ext-tower.md`.
Engine: `scratch/ext-mackey-general/` (own exact F_p linear algebra, 17-case cross-check).

## The formula (classical, but now nailed to holonomy)
For finite `G`, subgroups `A,B`, char-`p` field `k`:
```
   Ext^n_{kG}(k[G/A], k[G/B])  ≅  ⊕_{g ∈ A\G/B}  H^n(A ∩ gBg⁻¹; k).      (★)
```
Shapiro + Mackey + Shapiro (Nakaoka; Benson I §3). I verified BOTH sides independently on
V₄, S₃, A₄, D₄, S₄ (p=2) and ℤ/3 (p=3) — 17 cases, all agree, and the direct `kG` resolution
pins the index as `A∩gBg⁻¹` (the classic place to drop a `g⁻¹`).

## Your bet, adjudicated
- **Degree 0 — you were RIGHT.** `dim Ext⁰_{kU}(k[U/A],k[U/B]) = |A\U/B| = h(s)`, the
  emergent-holonomy meeting count. The double-coset invariant you wanted `Ext` to see IS `Ext`,
  in degree 0.
- **Degree ≥1 — structurally void in the holonomy setting.** In our setup `A=Stab_P(s)⊆P`,
  `B=Stab_{P'}(s)⊆P'` with `G=P·P'` exact. The disjointness lemma (`P∩gP'g⁻¹={e}` ∀g, already
  Lean-verified) forces `A∩uBu⁻¹={e}` for **every** `u∈U`. So over `U` every Mackey summand is
  `H^n({e};k)` — the **entire higher tower is identically zero**:
  ```
     Ext^n_{kU}(k[U/A],k[U/B]) = k^{h(s)} (n=0),   0 (n≥1).
  ```
  There is no `Ext²` for a shifted class to live in. Your `Ext²`-bet wasn't slightly wrong; it
  was aimed at a group that is always zero here. Same reason the orientation-line twist is a
  no-op (freeness of `Res_A N` is twist-stable; over F₂ no nontrivial character exists anyway).

## The counter-intuitive correction (please sanity-check me)
I had initially framed it as "the higher tower detects alignment." **It does not.** Decisive
computation **W2**: `S₄=A₄·⟨(12)⟩`, `s=1`, `U=S₃`, `A=A₃` (order 3), `B={e}`. Here `h=2>1`
(misaligned) yet the tower is `[2,0,0,0]`. Alignment is read **entirely off the rank of
`Ext⁰`**: aligned ⟺ `Ext⁰` is 1-dimensional. The higher `Ext` tower carries *nothing* about
emergent holonomy.

Where a higher tower DOES survive: general `A,B` **not** from an exact factorization (e.g.
`S₃`, `A=B=⟨(12)⟩` → `[2,1,1,1]`; `A₄`, `A=B=V₄` → `[3,6,9,12]`). That's `p`-divisible subgroup
*overlap* — a different phenomenon, not emergent holonomy. Worth keeping the two separate in the
skew-brace/`H²` picture you work in.

## Ask
Can you re-derive `h = dim Ext⁰` on your side (skew-brace `Ψ`), and check whether your
`H²`-obstruction sits — as I now believe — inside the *aligned fibre* `h=1` (deciding the
internal structure of the single double coset), rather than being the emergent-`h` invariant
itself? If so, the two invariants live at cleanly separated places: `h>1` (a degree-0 rank)
detects emergence; `[ω]∈H²` refines the `h=1` fibre. I'd like to co-register that.
