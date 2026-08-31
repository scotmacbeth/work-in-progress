# Polynomiality = provenance-tracking = coherence

> ⚠️ 2026-07-22 UPDATE: the "closure is vacuous / free" reading this note leaned toward is
> **REFUTED** — [[vacuity-false-collapse-tensor]] gives a monoidal counterexample (collapse tensor,
> `R_2` non-poly). The slogan below survives as *intuition* for WHY the polynomial (closed) tensors
> track provenance, but it does NOT force every monoidal ⋆ to be polynomial: the collapse tensor is
> coherent yet non-polynomial (it *shrinks* rather than adding a phantom). The precise locator is now
> the η-cartesian dichotomy (Lemma D ∧ ¬★'), see `proofs/2026-07-22-vacuity-resolved-collapse-tensor.md`.

**Grade:** connection resting on a *proved* toolkit; the vacuity *conjecture* it fed is now
**disproved** (2026-07-22). Anchored in `proofs/2026-07-21-closure-condition-vacuity.md`,
`proofs/2026-07-22-vacuity-resolved-collapse-tensor.md`, and registry
`closed-day-structures.condition-vacuity` (now **proved: NO**).

## The one-sentence insight

A functor `Set → Set` is **polynomial** iff it records, for each output element, *which input
elements that output uses* (its fibre exponent). This "provenance" is exactly what monoidal
**coherence** (associator naturality + interchange) forces a Day-convolution tensor to carry. So:

> **The closure side-condition looks vacuous because coherence and polynomiality are the same
> discipline seen from two directions.** A tensor that fails to be left-closed would have to lose
> provenance somewhere — but every way of losing provenance breaks a monoidal axiom.

## Why this bridges seed paths

- **Path 3 (monoidal structures on Cont):** `(Cont, ⊙_⋆)` left-closed ⟺ `R_B := (−)⋆B` polynomial
  ∀B (proved 2026-07-15, `2026-07-15-uniform-closure-day-tensors.md`). Question of the day: is that
  condition ever *false*? → reduces to "every monoidal `(Set,⋆)` preserves connected limits in each
  variable."
- **Path 1 (container theory):** polynomial ⟺ preserves connected limits ⟺ preserves wide pullbacks
  ⟺ `Σ_i(−)^{A_i}` (Carboni–Johnstone; Gambino–Kock 0906.4931 §1.18). The exponent `A_i` **is** the
  provenance.
- **Coherence theory:** the bridge. Each attempted non-polynomial tensor is killed by a *different*
  monoidal axiom.

## The evidence table (each candidate dies by a different axiom)

| candidate `A⋆B` | how it loses provenance | axiom that kills it |
|---|---|---|
| `max(\|A\|,\|B\|)` | rank-collapsing "pinch" `\|1⋆1\|=1` | **bifunctoriality / interchange** (vs a retract) |
| support `A⊔B⊔[both≠∅]` | separator point `•` forgets which leaves it splits | **associator naturality** (empty-slot fill `∅→1`) |
| `Sym²(A)×B`-type extra | super-linear growth degree `d²≠d` | **associativity** (via `R_B∘R_C≅R_{C⋆B}`) |
| any with unit `1` | "extra" `E` vanishes at terminal | `E(1)=∅⟹E=∅` (retract-only gap, §2) |

The `∨_S` family survives precisely because its normal form keeps a term
`Π_{i∈K}X_i × S^{|K|-1}` for **every** subset `K` of leaves — each extra element records its
provenance, and that provenance is the exponent making it polynomial.

## Reusable tool banked (proved)

**Retraction lemma (§1.3).** For any monoidal `⋆` on `Set`, using `i₀,i₁:1⇉2`, `t:2→1` with
`t∘iₖ=id`: any `(u,v)∈(1⋆B)²` with `(i₀⋆B)u=(i₁⋆B)v` in `2⋆B` already has `u=v` (apply `t⋆B`). This
gives the **injective half** of two-point-pullback preservation *for free, in full generality*. The
open core is the surjective half: "agreement ⟹ independence of the first slot."

## What is NOT yet proved (honesty)

- **Vacuity Conjecture** is a *conjecture*, not a theorem. The positive statement "associativity +
  naturality force `R_B` to preserve all connected limits" is open; only the injective half is done.
- **Unit-terminal ⟹ `⋆=×`** has one coherence gap: the natural idempotent `μ∘⟨π,π'⟩` splits as a
  *retract*, not obviously a subfunctor; clean closure route = **Fox's theorem** (needs `δ=μ∘Δ`
  coassociative + monoidal, i.e. `μ:(Set,×)→(Set,⋆)` a monoidal nat. transf. — unverified).

## Grant / downstream use

- If the conjecture holds, the 2026-07-15 biconditional's side-condition is **automatic** — every
  convolutional tensor on `Cont` is left-closed, and Neil's "were we just lucky with ⊗/×?" (UID-71)
  is answered NO structurally, not by coincidence. Handedness (§4) becomes unobservable for Day tensors.
- The `⋉/⋊` non-closure (proved 2026-07-20, [[ltimes-rtimes-are-dialectica]]) is consistent: `⋉/⋊`
  are **non-convolutional**, outside the Day family, so the vacuity claim never touches them. The two
  results together say: *inside* Day, closure is free; the only non-closed tensors on `Cont` live
  *outside* Day (Dialectica line). Clean dichotomy for the book/grant.

## Related

[[monoidal-structures-on-cont]] · [[ltimes-rtimes-are-dialectica]] · [[census-framing-preferred]] ·
[[contravariance-is-the-fibrewise-op]]
