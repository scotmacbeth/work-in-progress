/-!
# The re-entrancy obstruction `[ω] = ε` as finite 𝔽₂ linear algebra

This file machine-checks the finite-linear-algebra core of the grant-Impact
orchestration theorem (MacBeth,
`proofs/2026-07-20-orchestration-reentrancy-obstruction-analytic.tex`; registry
`orchestration-zs.json`).

**Context.** Supervisor–worker agent orchestration is modelled as a Zappa–Szép
product `C ⋈ D`. Whether the product exists (equivalently, whether the closing
condition `(G)` holds) is governed by a degree-2 obstruction class
`[ω(K_ε)] ∈ H²(Sk_C; 𝒟)`, where the parameter `ε` is the *token-mutation bit*
(`s₂ ∘ p = q · τ^ε`). The analytic proof reduces the categorical obstruction, by
an explicit orbit/cochain computation, to a tiny complex over 𝔽₂:

* `C¹ ≅ 𝔽₂²` (coordinates `h([p]), h([q])`),
* `C² ≅ 𝔽₂²` (coordinates `ω([s],[p]), ω([s₂],[p])`),
* `C³ = 0`, so `Z² = C²`;
* the coboundary `δ¹ h = (h[p]−h[q], h[p]−h[q])`, hence
  `B² = im δ¹ = {(t,t)} = ⟨(1,1)⟩` is the diagonal, and
* `H²(Sk_C; 𝒟) = 𝔽₂²/⟨(1,1)⟩ ≅ 𝔽₂` via `(a,b) ↦ b − a`.

The defect 2-cocycle of the natural transversal is `ω_T = (0, ε)`, so its class
is `[ω(K_ε)] = ε · (generator)`, i.e. `[ω] = 0 ⟺ ε = 0 ⟺ K_ε = C ⋈ D exists`.

**What this file checks.** The *finite class computation* only — not the
reduction of the categorical obstruction to this complex (that stays the paper's
`proved` step). We transcribe the complex directly rather than re-derive it:
see the `.tex` §"Normalized cochain complex" / §"The obstruction class equals the
token-mutation bit" for the numbers (`C² ≅ 𝔽₂²`, `d¹ =` diagonal, `ω_T=(0,ε)`).

**Model.** 𝔽₂ is `Bool` with `false = 0`, `true = 1`, `xor = + = −` (the additive
group of the two-element field). Everything is finite, so the substantive facts
close by `decide`. This keeps the file in the project's pure-core-Lean style
(no Mathlib), matching `Containers/Basic.lean`, `Containers/ZappaSzep.lean`.

Two equivalent sharp statements of "`[ω] = ε`" are proved:

* `omega_inB2_iff_zero` — membership form: `ω_T(ε) ∈ B² ⟺ ε = 0`
  (`[ω]=0 ⟺ ε=0`, avoiding quotients entirely);
* `phi_omega` — class form: the gauge-invariant class map `φ` sends `ω_T(ε)` to
  `ε` exactly, together with `phi_ker_eq_inB2` (`ker φ = B²`, so `φ` descends to
  the iso `H² ≅ 𝔽₂`) and `phi_surjective`.
-/

namespace Containers

namespace Reentrancy

/-- The two-element field 𝔽₂, modelled as `Bool`: `false = 0`, `true = 1`,
addition/subtraction is `xor`. -/
abbrev Z2 := Bool

/-- The 2-cochains `C² ≅ 𝔽₂²`. The two coordinates are the worker-outcome
defects `ω([s],[p])` and `ω([s₂],[p])`. -/
abbrev C2 := Z2 × Z2

/-- The coboundary `δ¹`, precomposed with the parametrisation `t = h[p] − h[q]`
of its (one-dimensional) source: `δ¹ h = (h[p]−h[q], h[p]−h[q])`, so its image is
exactly `{(t,t)}`, the diagonal. This `d1` is that image map. -/
def d1 (t : Z2) : C2 := (t, t)

/-- Membership in the coboundary subgroup `B² = im δ¹ = ⟨(1,1)⟩` (the diagonal). -/
def InB2 (x : C2) : Prop := ∃ t : Z2, d1 t = x

/-- The defect 2-cocycle `ω_T` of the natural transversal `T = {p,q,s,s₂}`, as a
function of the token-mutation bit `ε`: `ω_T = (ω([s],[p]), ω([s₂],[p])) = (0, ε)`
(the paper's Main theorem: `s∘p = q` gives `0`, and `s₂∘p = q·τ^ε` gives `ε`). -/
def omega (ε : Z2) : C2 := (false, ε)

/-- The gauge-invariant class map `φ : C² → 𝔽₂`, `(a,b) ↦ b − a = xor a b`.
Its kernel is the diagonal `B²`, so it descends to the iso `H² ≅ 𝔽₂`; it reads
off the class `[ω]`. -/
def phi (x : C2) : Z2 := xor x.1 x.2

/-! ### The class map kills coboundaries and detects `B²` exactly -/

/-- `φ` vanishes on the coboundary subgroup: `φ(δ¹ h) = 0`. -/
@[simp] theorem phi_d1 (t : Z2) : phi (d1 t) = false := by
  cases t <;> rfl

/-- `ker φ = B²`: the class map vanishes on `x` iff `x` is a coboundary. This is
the statement that `φ` descends to an *injective* map `H² = C²/B² → 𝔽₂`. -/
theorem phi_ker_eq_inB2 (x : C2) : phi x = false ↔ InB2 x := by
  obtain ⟨a, b⟩ := x
  constructor
  · intro h
    cases a <;> cases b <;> first | exact ⟨false, rfl⟩ | exact ⟨true, rfl⟩ | simp_all [phi]
  · rintro ⟨t, ht⟩
    cases t <;> simp_all [d1, phi]

/-- `φ` is surjective, so the induced `H² → 𝔽₂` is onto: `H²` is (at least) all
of `𝔽₂`. Together with `phi_ker_eq_inB2` this is the iso `H² ≅ 𝔽₂`. -/
theorem phi_surjective (y : Z2) : ∃ x : C2, phi x = y := by
  cases y
  · exact ⟨(false, false), rfl⟩
  · exact ⟨(false, true), rfl⟩

/-! ### The main theorem: `[ω(K_ε)] = ε` -/

/-- **Class form of `[ω] = ε`.** The gauge-invariant class of the defect cocycle
`ω_T(ε) = (0, ε)` is exactly the token-mutation bit `ε`. -/
@[simp] theorem phi_omega (ε : Z2) : phi (omega ε) = ε := by
  cases ε <;> rfl

/-- **Membership form of `[ω] = 0 ⟺ ε = 0`.** The defect cocycle is a coboundary
(its class is trivial) iff the token-mutation bit vanishes — iff the Zappa–Szép
product `K_ε = C ⋈ D` exists. -/
theorem omega_inB2_iff_zero (ε : Z2) : InB2 (omega ε) ↔ ε = false := by
  rw [← phi_ker_eq_inB2, phi_omega]

/-- Corollary chaining both forms: the class of `ω_T(ε)` is `0` iff `ε = 0`. -/
theorem omega_class_zero_iff (ε : Z2) : phi (omega ε) = false ↔ ε = false := by
  rw [phi_omega]

/-- Sanity: the two workers *do* differ when `ε = 1` — the class is nonzero, the
Zappa–Szép product does **not** exist (protected re-entrancy fails). -/
example : phi (omega true) = true := rfl

/-- Sanity: at `ε = 0` the class is trivial and the product exists. -/
example : InB2 (omega false) := ⟨false, rfl⟩

end Reentrancy

end Containers
