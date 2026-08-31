# Workers closure column, completed: ×-closed (conjecture flipped), ◁ genuinely obstructed

**Date:** 2026-08-21 (PROVE session)
**Status:** proved (× and ◁), computationally verified.
**Prior:** `workers-type-hierarchy.json` had × ("×-exponential obstructed for the candidate
hom only") and ◁ ("obstruction identified, open") as standing gaps. This closes both — and
the × answer is the **opposite** of the prior conjecture.

## Setup

Containers `Cont`: objects `p=(S_p, P_p:S_p→Set)`, extension `⟦p⟧X=Σ_{s}X^{P_p(s)}`; container
morphisms = all natural transformations of extensions. Cont is:
- **⊗-closed** (Dirichlet tensor `p⊗q=(S_p×S_q,(s,t)↦P_p(s)×P_q(t))`), hom `[p,q]_⊗`
  (Niu–Spivak Ex. 4.78 / Eq. 4.79; machine-checked in `DirichletClosed.lean`);
- **cartesian closed** (product `p×q=(S_p×S_q,(s,t)↦P_p(s)+P_q(t))`, `⟦p×q⟧=⟦p⟧×⟦q⟧`),
  exponential `q^p` (Altenkirch–Levy–Staton, CiE 2010; Niu–Spivak Thm 5.31).

Two closed structures are instances of the **uniform closure formula** for a Day-convolution
tensor `⊙_⋆` (⋆ a monoidal structure on Set) — proved (both directions, with the polynomiality
criterion) in my `proofs/2026-07-15-uniform-closure-day-tensors.md`:
> `[p,q]_⋆ = ∏_{s_p} q ◁ (P_p(s_p) ⋆ y)`, i.e. `⟦[p,q]_⋆⟧A = ∏_{s_p} ⟦q⟧(A ⋆ P_p(s_p))`.
`⋆=×` gives `⊗` (Dirichlet), `⋆=+` gives `×` (cartesian): `⟦q^p⟧A=∏_{s_p}⟦q⟧(A+P_p(s_p))`.

**Workers** (state object `ΔS=(S, s↦S)`, the codiscrete category): the `(Set,×)`-graded
category `Workers_S(a,q) := Cont(ΔS⊗a, q)`. Fix a grade S throughout. "Workers is ⊙-closed"
means the graded monoidal product ⊙ (=Cont's ×, resp. ◁) has an internal hom:
`Workers_S(a⊙p, q) ≅ Workers_S(a, E)` naturally in a, for some container E.

Two lemmas do all the work.

**Lemma L1 (state-lift = ⊗-hom out of ΔS).** For any container r,
`⟦[ΔS,r]_⊗⟧X = (⟦r⟧(S×X))^S`.
*Proof.* `[ΔS,r]_⊗` has shape set `Cont(ΔS,r)` and, at a morphism `φ=(u:S→S_r, (f_s))`,
position set `Σ_{s∈S}P_r(u s)`. So
`⟦[ΔS,r]_⊗⟧X = Σ_{u:S→S_r} Σ_{(f_s)∈∏_s S^{P_r(u s)}} X^{Σ_s P_r(u s)}
            = Σ_{u:S→S_r} ∏_{s∈S}(S×X)^{P_r(u s)}
            = ∏_{s∈S} (Σ_{s_r∈S_r}(S×X)^{P_r(s_r)}) = (⟦r⟧(S×X))^S.`  ∎
(This is the uniform formula at ⋆=×, p=ΔS: `⟦[ΔS,r]_⊗⟧A=∏_{s∈S}⟦r⟧(A×S)=⟦r⟧(A×S)^S`.)

**Lemma L2 (hom out of a ◁-image).** `Cont(c,R)=∏_{s_c∈S_c} ⟦R⟧(P_c(s_c))`.
*Proof.* A morphism `c→R` is, per shape `s_c`, a shape `s_R` and a backward map
`P_R(s_R)→P_c(s_c)`; so `Cont(c,R)=∏_{s_c}Σ_{s_R}P_c(s_c)^{P_R(s_R)}=∏_{s_c}⟦R⟧(P_c(s_c))`. ∎

---

## Theorem 1 (×). Workers is ×-closed. Internal hom
> `[p⇒q]_× = ∏_{s_p∈S_p} q ◁ (y ⊕ c_{S×P_p(s_p)})`,  i.e.
> `⟦[p⇒q]_×⟧Y = ∏_{s_p} ⟦q⟧(Y + S×P_p(s_p))`,
where `c_K=(K,k↦∅)` (constant K) and `y⊕c_K` is the container with `⟦y⊕c_K⟧Z=Z+K`.

**Proof.** Write `R:=[ΔS,q]_⊗`. Naturally in a:
```
Workers_S(a×p, q) = Cont(ΔS⊗(a×p), q)
                  = Cont((a×p)⊗ΔS, q)          [⊗ symmetric]
                  ≅ Cont(a×p, [ΔS,q]_⊗) = Cont(a×p, R)   [⊗-closure of Cont]
                  ≅ Cont(a, R^p)                [Cont cartesian closed]
```
and `Workers_S(a,E) = Cont(ΔS⊗a, E) ≅ Cont(a, [ΔS,E]_⊗)`. By Yoneda, Workers is ×-closed with
hom E iff `R^p ≅ [ΔS,E]_⊗`. We exhibit E. Using L2's companion (uniform formula, ⋆=+) and L1:
```
⟦R^p⟧X = ∏_{s_p} ⟦R⟧(X+P_p(s_p)) = ∏_{s_p} (⟦q⟧(S×(X+P_p(s_p))))^S
        = ∏_{s_p} (⟦q⟧(S×X + S×P_p(s_p)))^S.
```
Define E by `⟦E⟧Y := ∏_{s_p}⟦q⟧(Y + S×P_p(s_p))` — a container (finite/arbitrary products and
composites `q◁(y⊕c_K)` of containers are containers). Then by L1,
```
⟦[ΔS,E]_⊗⟧X = (⟦E⟧(S×X))^S = (∏_{s_p}⟦q⟧(S×X + S×P_p(s_p)))^S
            = ∏_{s_p}(⟦q⟧(S×X + S×P_p(s_p)))^S            [(∏_i B_i)^S = ∏_i B_i^S]
            = ⟦R^p⟧X.
```
So `R^p ≅ [ΔS,E]_⊗` (extension is faithful), hence `[p⇒q]_× = E`. ∎

**Reading.** The state entangles the curried argument — `P_p(s_p) ↦ S×P_p(s_p)` — exactly the
"entanglement" the prior work identified. But the entanglement is **representable**: `[p⇒q]_×` is
Cont's cartesian exponential with each argument fibre inflated by `S`. Contrast the ⊗-hom
`[p,q]_⊗ = ∏_{s_p}q◁(P_p(s_p)×y)` (`⟦⟧A=∏_{s_p}⟦q⟧(A×P_p(s_p))`), where state curries **past**.

**Boundary checks.** `|S|=1`: `E=∏_{s_p}q◁(y⊕c_{P_p(s_p)})=q^p` — grade 1 = plain Cont, ✓.
`p=1` (terminal, one shape, no positions): `E=q◁(y⊕c_∅)=q◁y=q`, i.e. `[1⇒q]_×=q`, ✓.

**Uniform mechanism.** For any Day-convolution tensor `⊙_⋆` on Cont with Cont `⊙_⋆`-closed, the
same chain gives: Workers is `⊙_⋆`-closed iff `S×(A⋆K)` is a functor of `Y:=S×A` (for each
constant K). `⋆=+`: `Y+S×K` ✓ (× distributes over +). `⋆=×`: `Y×K` ✓ (× associative). Hence
**both** native tensors close, for one structural reason.

---

## Theorem 2 (◁). Workers is not ◁-closed (whenever p has ≥2 shapes, |S|≥2, q non-constant).
The obstruction is **inherited from Cont**: `(−)◁p` has no right adjoint in Cont, because the
would-be internal hom is a **non-polynomial** functor.

**Proof.** By L1's ⊗-step, `Workers_S(a◁p,q) ≅ Cont(a◁p, R)`, `R=[ΔS,q]_⊗`. If this presheaf in
a were representable by a container H, then evaluating at `C_A:=(1, *↦A)` (one shape, A
positions) forces `⟦H⟧(A)=Cont(C_A◁p, R)`. Now `C_A◁p` has shapes `γ:A→S_p` and positions
`Σ_{i∈A}P_p(γ i)`, so by L2
```
⟦H⟧(A) = Cont(C_A◁p, R) = ∏_{γ:A→S_p} ⟦R⟧(Σ_{i∈A}P_p(γ i)) =: T_R(A).
```
So representability requires `T_R` to be polynomial. It is not. Take p with ≥2 shapes, each with
≥1 position, and any R with `|⟦R⟧(1)|≥2`. For `A=[n]` the product ranges over `|S_p|^n ≥ 2^n`
functions γ, and each `Σ_{i∈[n]}P_p(γ i)` has ≥ n ≥ 1 elements, so each factor is `≥|⟦R⟧(1)|≥2`.
Hence `|T_R([n])| ≥ 2^{2^n}` — **double-exponential**. But every container H satisfies
`|⟦H⟧(1)| = #S_H` and, if that is finite, `|⟦H⟧(n)| = Σ_{s}n^{|P_H(s)|} ≤ (#S_H)·n^{K}`
(polynomial in n); if `#S_H` is infinite then `|⟦H⟧(1)|=∞`. Since `|T_R(1)|` is finite yet
`|T_R(n)|` grows faster than any `c·n^K`, no such H exists. So the presheaf is not representable
in Cont; a fortiori Workers has no ◁-internal-hom. ∎

**Sharpest witness (Cont, no state).** Already `R=y` (Id) gives `T_R(A)=A^{S_p^A}`; for
`p=(2 shapes, 1 position)`, `|T_R([n])| = n^{2^n} = 0,1,16,6561,4294967296,…`. If this were a
container, `|T_R(1)|=1` forces a single shape of arity `k` with `2^k=16`, i.e. `k=4`, predicting
`|T_R(3)|=3^4=81 ≠ 6561`. Contradiction. **Cont itself is not ◁-closed.**

**Clarification vs. prior narrative.** The obstruction is *not* a state effect: it appears at
`S=1` already. It reflects that `Poly`/`Cont` carries a ◁-**co**closure (a *left* adjoint,
Niu–Spivak §6 / Meyers) but **no** ◁-closure (right adjoint to `−◁p`). Where the prior note said
"state spreads over the nested positions," the precise statement is: the nesting `a◁p` makes the
representing functor's shape-count grow like `S_p^A` (double-exponentially), leaving `Cont`.
Single-shape p is exactly the escape hatch: then `T_R(A)=⟦R⟧(|P_p|·A)=⟦R◁(|P_p|·y)⟧A` is
polynomial, so `−◁p` does have a right adjoint (and Workers ◁-closure reduces to the `×`-style
membership test, which succeeds).

---

## Verification (computational)

`scratch/workers-type-hierarchy/` (all green):
- `xclosed_resolve.py`: L1, L2 objectwise (n=1..3); **`R^p ≅ [ΔS,E]_⊗`** via equal fibre-multiset
  AND equal extension counts, for `|S|=2` and 4 pairs (p,q); direct closedness
  `|Work(a×p,q)| = |Work(a,E)|` for several a (16=16, 576=576, 25=25, 225=225, 64=64, 0=0);
  control: `E ≠ q^p` (fibre-multiset differs) — reconciles the old naive 1296≠256 mismatch.
- `lhd_cardinality.py`: `t_n=|T_R([n])|` = `[0,1,16,6561,4294967296]` (R=Id) and
  `[0,16,65536,2821109907456]` (R=[ΔS,q], q=Id, |S|=2); single-shape p gives `[0,2,4,6,8]` (=2·y,
  polynomial ✓).

## Gaps
None in Theorems 1–2. Open extensions (not part of this task):
- The `p◁(−)` side (right adjoint to post-composition by p) — a different adjunction; not needed
  for the graded-monoidal ◁-closedness (which is `(−)◁p`).
- Whether the uniform `⊙_⋆`-closure criterion `S×(A⋆K)=G(S×A)` characterizes *exactly* which Day
  tensors descend closed to Workers (both native ones do; is there a Day tensor that fails?).
