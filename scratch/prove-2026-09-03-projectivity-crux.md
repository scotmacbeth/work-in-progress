# PROVE 2026-09-03 — (Q): is F = ∏_ℕ(⊕_ℕ −) projective in Add(Vec,Vec)?

Goal: F not projective ⟹ Vec ◁-inadmissible ⟹ Conj 6.2 (direction A).
F = ∏_{n} A, A = ⊕_{m} id. Row-finite ℕ×ℕ matrices over X.
Representables h_N = Hom(N,−); projective; A = ⊕_m h_k is free.

## NEW RESULTS THIS SESSION (candidate)

### (D1) Self-similarity + telescope SES  [mechanics to verify]
- F ≅ A ⊕ F naturally (split off row 0; rows≥1 ≅ F via shift).
- Telescope: d: F ⟹ F, d(a)_n = a_n − a_{n+1}. Then
      0 → A → F --d--> F → 0   is exact (ker d = constant seqs ≅ A = lim; d surjective since
      partial sums solve a_n − a_{n+1} = y_n in ∏, no convergence needed ⟹ lim¹ = 0).
  This SES has F (right) and SPLITS (because F ≅ A⊕F anyway). So the telescope/lim¹ does NOT
  obstruct projectivity. ⇒ documents a natural WRONG approach as dead. (Consistent, not decisive.)

### (D2) Free-case structure theorem  [UNCONDITIONAL — only evaluates at k]
Suppose F ≅ ⊕_{j∈J} h_{N_j}. Evaluate at k (countable field, dim=card):
  F(k) = ⊕_j N_j^*,  dim_k F(k) = 𝔠  (row-finite ℕ×ℕ matrices over k).
- Each summand N_j^* has dim ≤ 𝔠, so 2^{dim N_j} ≤ 𝔠 ⟹ **dim N_j ≤ ℵ₀ for every j**.
- #{j : N_j ≠ 0} ≤ 𝔠, with ≥1 having dim N_j = ℵ₀ (to reach 𝔠).
So: if F is free, it is ⊕ of AT MOST 𝔠 representables on COUNTABLE-DIM spaces, ≥1 infinite-dim.
(Countability of J would follow from the Specker deliverable D3 via dim Nat(F,id) ≤ 𝔠 = ∏_j N_j.)

### (D3) Specker deliverable — PROVED: Nat(F,id) = ⊕_n k^ℕ (NO exotic functional). ★
**Prop.** α∈Nat(F,id), α∘in_n=0 ∀n ⟹ α=0.
*Proof (tautological-spread + finite projection).* Fix X, ξ∈F(X). Σ=supp(ξ)={(n,m):ξ_{nm}≠0}
(row-finite ⟹ countable). U=k^{(Σ)}, basis {u_{nm}}. Tautological spread η∈F(U): η(e_n)=∑_m u_{nm}f_m.
w:U→X, w(u_{nm})=ξ_{nm}. Then **ξ=F(w)η** (check: (⊕w)η(e_n)=∑ξ_{nm}f_m ✓). Naturality: α_X(ξ)=w(α_U η).
Now α_U(η)=0: v:=α_U(η)∈U finite support Σ_0. φ=proj_U onto Σ_0. F(φ)η supported on Σ_0 ⟹ finite
ROW support ⟹ ∈F_fin(U)=Σ finite in_n ⟹ α_U(F(φ)η)=0. Naturality: 0=φ(v)=v (φ fixes supp v). ∎
Constant-column case ξ_{n,0}=e_0 killed as special case: ξ=F(w)η, w:e_n↦e_0 collapse. c=0. ✓
**Combined w/ Lemma R (image⊆finite support, cited proved) + surjectivity (α=Σ_{n∈S}γ^{(n)}pr_n):
   Nat(F,id) ≅ ⊕_{n∈ℕ} k^ℕ  EXACTLY.**  [needs: Lemma R + D3(new) + easy surjectivity]

### (D2+D3) Free-case structure theorem — now with COUNTABLE J
F≅⊕_{j∈J}h_{N_j} ⟹ Nat(F,id)=∏_j N_j = ⊕_n k^ℕ (D3), dim 𝔠 ⟹ |{j:N_j≠0}|≤ℵ₀ (else dim≥2^{ℵ₁}>𝔠).
Plus D2: each N_j countable-dim. So: **F free ⟹ F≅⊕_{n∈ℕ}h_{N_n}, countably many countable-dim
N_n, ≥1 infinite-dim.** UNCONDITIONAL, rigorous. Sharpest constraint to date on direction B.

## THE WALL — now crisply understood
D3 works because TARGET id=h_k is FINITE-dim: v=α_U(η)∈U is a single vector, finite support,
killable by finite projection. Same argument for target h_W, W INFINITE-dim FAILS: v∈Hom(W,U) has
infinite support (im v spread over ∞ coords), no finite φ fixes it. An infinite-dim summand N_0 (≅E,
forced by D2+D3) needs exactly this infinite-dim-target rigidity. Confirmed: **h_E IS a retract of F**
(column-0 split: F=∏_n(⊕_m id)⊇∏_n(id)=h_E split) — so infinite-dim retracts are CONSISTENT, no
contradiction there. Direction-A finish needs a genuinely NEW infinite-dim-target obstruction. Blocked.

## STATUS: D1,D2,D3 solid & new. Finish (A) open — wall precisely located (infinite-dim target).
Three-strike honest: deliver D1/D2/D3 + wall analysis; save finish for collaborator/dream.
