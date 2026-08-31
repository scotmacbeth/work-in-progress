# PROVE — Classification of left-closed convolutional tensors on Cont

MacBeth, 2026-07-23. Deep-work session. Target set by state/PROVE.md (2026-07-22).

## The theorem to establish

Let `(Set, ⋆, I)` be a **monoidal** structure such that `R_B := (−)⋆B : Set → Set` is
**polynomial** (preserves connected limits / familially representable) for every set `B`.
(Equivalently, by the 2026-07-15 biconditional, the Day tensor `⊙_⋆` on `Cont≅Fam(Set^op)`
is left-closed.) **Classify all such `⋆`.**

**Conjecture (from PROVE.md).** Exactly:
- (a) `I=1` and `⋆ ≅ ×` (→ Dirichlet `⊗` on Cont), or
- (b) `I=∅` and `⋆ ≅ ∨_S` for some set `S`, where `A ∨_S B := A + A×S×B + B`
      (→ `▷_S` on Cont; `∨_∅ = +` → product `×` on Cont).

Collapse tensor (2026-07-22) is the minimal witness that NOT every monoidal `⋆` qualifies
(its `R_2` is non-poly), so this is a genuine restriction.

Reference facts:
- `∨_S B = A + A×S×B + B`, unit ∅, monoidal, prior art (Spivak); `∨_∅ ≅ +`.
  [2026-07-14-day-family-classification.md §5.]
- Polynomial functor `F:Set→Set` ⟺ `F ≅ Σ_{i∈I} y^{A_i}` ⟺ preserves connected limits
  (Carboni–Johnstone). `F(1)=I` (index set), arities `A_i` recoverable.

## Plan
1. COMPUTE: cardinality-level discovery — classify symmetric assoc. unital polynomial ops
   `f:ℕ×ℕ→ℕ`. Expect shortlist {xy (unit1)} ∪ {x+y+sxy (unit0)}.
2. Prove `I ∈ {∅, 1}`.
3. Case I=1 ⟹ ⋆≅×.
4. Case I=∅ ⟹ ⋆≅∨_S. (crux: naturality+assoc force A⋆B = A+B+A×S×B)
5. Consider non-symmetric / one-sided (left-closed only).

---

## Computational Evidence
DONE. `cardinality-classification.py` (SymPy deg 2–4 + brute force): symmetric assoc unital
polynomial ops on ℕ = **`x+y+s·xy` (unit 0, s≥0 free)** and **`xy` (unit 1)** ONLY. No unit≥2
solution (confirms Lemma 1). NO single-variable degree-≥2 term ever survives (confirms Key Lemma's
finite content). `verify_reconstruction.py`: ×, ∨_S (S≤3) — unit, assoc/`R_B∘R_C=R_{C⋆B}`, affine
form, symmetry identity, `D_{B⋆C}=D_B·D_C`, `D_∅=1` all PASS. `hostile_affine_check.py`: degree-2
candidate `b+x+x²b` fails associativity (deg_x 4 vs 2) — no monoidal structure. Final write-up:
`proofs/2026-07-23-closed-convolutional-tensors-classification.md`.

---

## STRUCTURE OF THE PROOF (developed 2026-07-23)

Standing hypothesis (H): `(Set,⋆,I)` symmetric monoidal, `R_B:=(−)⋆B` polynomial ∀B.
Polynomial ⟹ `X⋆B ≅ Σ_{u∈1⋆B} X^{A_{B,u}}` naturally in X; index set `1⋆B=R_B(1)`,
arity `A_{B,u}` a set. Recover arity: fibre of `R_B(2)→R_B(1)` over u is `2^{A_{B,u}}`.

### Lemma 1 (Unit is small): under (H), |I| ≤ 1, i.e. I∈{∅,1}.
Proof. `R_1=R_B|_{B=1}` polynomial: `R_1(X)=X⋆1=Σ_{k∈K}X^{M_k}`, K=1⋆1.
Right unit: `R_I=(−)⋆I≅Id` ⟹ `1⋆I=1`; symmetry ⟹ `I⋆1≅1⋆I=1`, so `R_1(I)=I⋆1=1`.
Thus `Σ_{k∈K}I^{M_k}=1`. If |I|≥2, every `I^{M_k}≥1`, so the sum =1 forces |K|=1 and the
single `I^{M_{k₀}}=1` ⟹ M_{k₀}=∅. Hence `R_1(X)=X^∅=1` constant: `X⋆1=1 ∀X`. In particular
`1⋆∅=∅⋆1=1`, so `R_∅(1)=1⋆∅=1`: `R_∅` has one index, `X⋆∅=X^A` (A:=A_{∅,*}). Then
`∅⋆I=I^A`, but right unit at object ∅ gives `∅⋆I≅∅`, so `I^A=∅` ⟹ |I|=0, contradicting |I|≥2. ∎
[General, uses symmetry + polynomiality of R_1,R_∅ only. Does NOT need arities≤1.]

### Prop 2 (Degree multiplicativity). d(B):=sup_u|A_{B,u}|. Associativity gives
`R_B∘R_C ≅ R_{C⋆B}` (from (X⋆C)⋆B≅X⋆(C⋆B)). Composition-of-polynomials arity formula:
`(R_B∘R_C)` has index `Σ_{b∈1⋆B}(1⋆C)^{A_{B,b}}`, arity at (b,φ)= `Σ_{i∈A_{B,b}}A_{C,φ(i)}`.
⟹ `d(C⋆B)=d(C)·d(B)` (cardinal product), for d≥1. [d is a monoid hom (Set,⋆)→(Card,·).]

### KEY LEMMA (crux): under (H), every arity |A_{B,u}| ≤ 1.
  Equivalently each R_B is AFFINE: `X⋆B ≅ C_B + D_B×X`.
Proof (bounded-arity case). Let κ=sup_B d(B). If 2≤κ<∞: pick B,b with |A_{B,b}|=κ. By Prop 2,
d(B⋆B)=κ² > κ (finite κ≥2), contradicting κ=global sup. So κ≤1. ∎ (finite-arity)
  ⚠️ GAP: infinite arities. Prop-2 growth fails (κ²=κ for infinite κ). See §Gap.

### Reconstruction (given Key Lemma).
Write `X⋆B=C_B+D_B×X` (C_B=arity-0 indices, D_B=arity-1 indices; functors of B).
• I=1: `X⋆1=X`⟹C_1=∅,D_1=1; symmetry+`1⋆∅=∅⋆1=R_1(∅)=∅`⟹`X⋆∅=∅`⟹C_B=∅⋆B=∅; and
  C_B+D_B=1⋆B=B⟹D_B=B. So `X⋆B=B×X` = **×**.
• I=∅: `R_B(∅)=∅⋆B=B`⟹C_B=B (natural). Symmetry `B+D_B×X ≅ X+D_X×B`: LHS affine in X ⟹ RHS
  affine in X ⟹ D_X affine ⟹ `D_X=D_∅+S×X`. `D_∅`: X=∅ gives `B≅D_∅×B`⟹D_∅=1. So `D_X=1+S×X`,
  `X⋆B=B+(1+S×B)X=X+B+S×X×B` = **∨_S**. (S := linear coeff of the strong-monoidal
  functor D:(Set,⋆,∅)→(Set,×,1), D_B=1+S×B; assoc independently forces D_{B⋆C}≅D_B×D_C.)

### CLASSIFICATION THEOREM (under Key Lemma).
(H) ⟹  ⋆≅× (I=1) or ⋆≅∨_S for a unique set S (I=∅).  Conversely both satisfy (H).
Corresponds on Cont to: **Dirichlet ⊗**, and the **▷_S family** (▷_∅ = product ×).

### §Gap (the ONE remaining gap): exclude INFINITE arities.
Need: no `|A_{B,u}|` infinite. Growth argument (Prop 2) cannot see it (κ²=κ). Likely killed by
associator naturality (cf. support/Sym² deaths, 2026-07-21) but no clean general argument yet.
Status: Classification proved for bounded/finitary ⋆; infinite-arity exclusion = conjecture.

