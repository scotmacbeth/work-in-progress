# For collaborator — 2026-09-03: Nat(F,id) computed, free case pinned, the exact remaining wall

**Context.** (Q) — the crux of Conjecture 6.2 (absorptive dichotomy): is
`F(X) = Hom(E, ⊕_ℕ X) = ∏_ℕ(⊕_ℕ X)` a coproduct of representables (equivalently, is it projective) in
`Add(Vec,Vec)`? `E = k^{(ℕ)}`. NO ⟹ Vec ◁-inadmissible ⟹ Conj 6.2 holds (direction A). Full write-up:
`proofs/2026-09-03-nat-F-id-specker-and-free-structure.md`.

## What is now PROVED (solid, new)

1. **`Nat(F, id) ≅ ⊕_{n∈ℕ} k^ℕ` exactly** (the flagged guaranteed deliverable). The nontrivial half —
   *no exotic functionals*: `α∘in_n = 0 ∀n ⟹ α = 0` — has a clean **field-native** proof that needs
   neither ℤ-divisibility (absent over a field) nor Baer–Specker slenderness (false for `Vec`):
   *tautological-spread + finite projection*. Given `ξ ∈ F(X)`, write `ξ = F(w)(η)` with
   `η ∈ F(U)`, `U = k^{(supp ξ)}` the free space on `ξ`'s support and `w(u_{nm}) = ξ_{nm}`; then
   `α_U(η) = 0` because `v := α_U(η) ∈ U` is a **single vector of finite support** `Σ_0`, and the
   projection `φ` onto `Σ_0` sends `F(φ)η` into finite-**row**-support (killed by `α∘in_n = 0`) while
   naturality forces `φ(v) = v`. The whole argument is one use of naturality against a finite-rank
   projection.

2. **Free-case structure theorem.** If `F ≅ ⊕_j h_{N_j}` then **(c) [ZFC] infinitely many `N_j` are
   infinite-dimensional** — this *directly excludes* the old "Case A (all `N_j` finite-dim)", via `F`
   not preserving infinite coproducts — and every `dim N_j`, `|J|` is `≤ 𝔠`. Under `2^{ℵ_0} < 2^{ℵ_1}`
   (holds under GCH; **independent of ZFC**) this sharpens to *countably many `N_j`, each of countable
   dimension*. **Honest caveat:** the "countable" refinement genuinely uses that fragment of cardinal
   arithmetic (it can fail: `2^{ℵ_0}=2^{ℵ_1}` is consistent); the ZFC-safe part (c) is all the wall
   below needs.

3. **Self-similarity / telescope is a dead approach (documented).** `F ≅ A⊕F ≅ h_E⊕F`; the telescope
   `0→A→F→F→0` is exact and **splits** (`lim¹` of the constant tower vanishes). No obstruction there.

## The wall — where direction A actually stops (the ask)

Result 1's engine works for the target `id = h_k` **only because `k` is finite-dimensional**: `v` is a
single vector, hence finite-support, hence killed by a finite projection. The *same statement for a
target `h_W` with `W` infinite-dimensional is false* (`v ∈ Hom(W,U)` has infinite support). By result
2(c) a free `F` **must** contain an infinite-dimensional representable summand `h_{N_0}` — and indeed
**`h_E` genuinely *is* a retract of `F`** (the column-`0` split `F ≅ h_E ⊕ F`), so infinite-dim
retracts are *consistent*, not contradictory. Three independent finish attempts (dimension/dual-size;
the `h_E`-retract; the target-`A` rigidity, where `pr_0 ∈ Nat(F, ⊕_m id)` has infinite output-support)
all collapse onto this one edge.

**Precise open sub-problem.** Supply a rigidity for an **infinite-dimensional target**, or equivalently
compute `Ext¹_{Add(Vec,Vec)}(F, K) ≠ 0` for `K = ker(⊕_{n∈ℕ} h_{N_n} ↠ F)` under the result-2 shape;
or refute that the infinite-`n`-support elements of `F` (e.g. `ζ ∈ F(k)`, or the diagonal
`σ_{n,0}=e_n ∈ F(E)`) can be *naturally* factored through a coproduct of representables. The ℤ-analogue
in `Add(Ab,Ab)` closes via Baer–Specker precisely because `Ab` *has* slender objects; the field
obstruction lives one level up. **Literature still gated (deep-read needed):** Auslander functor
categories; Eklof–Mekler cotorsion / almost-free reworked over a field; slenderness in functor
categories.

Mechanics all green: `scratch/2026-09-03-mechanics-check.py`.
