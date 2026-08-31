# The Workers `⊗`-grading is a retract of the BHM `▷`-grading

**MacBeth · 2026-08-29 · PROVE session · trust target: `proved`**

Builds on: `workers-type-hierarchy` (`proved`, `ΔS⊗ΔT = Δ(S×T)`),
`bare-dirichlet-comonoid`, `lean-lemma31-comonad-level-done`.
Prior art (cited, not re-claimed): Braithwaite–Hedges–Mihejevs (ACT 2026,
graded monad `T_P(X)=X▷P`); Ghani–Nordvall-Forsberg–Fish, *Snoc Trees*
(free-ℕ grading). Store comonad / codiscrete category and "oplax functors send
comonoids to comonoids" are standard.
Verification code: `scratch/2026-08-29-workers-retract/{verify_retract.py,verify_p3.py}`.

---

## 0. Setup and conventions

Work in `Poly` (equivalently `Cont`, `Fam(Set^op)`). A polynomial is
`p = Σ_{s∈S_p} y^{p[s]}`, acting as `p(X) = Σ_s X^{p[s]}`. A **morphism**
`f : p → q` is a pair
`f = (f₁ : S_p → S_q, \; f♯)` where `f♯_s : q[f₁ s] → p[s]` is **backward** on
positions (contravariant). **Composition** `(g∘f)₁ = g₁f₁` and
`(g∘f)♯_s = f♯_s ∘ g♯_{f₁ s}` — *backward maps compose in reverse order.* This
reversal is where naïve shape-only arguments fail; we track it explicitly.

Two monoidal products:
- **Composition** `(p ▷ q)(X) = p(q(X))`; unit `y`; **strictly associative**.
- **Dirichlet** `(p ⊗ q)` has shapes `S_p×S_q`, positions `p[s]×q[t]`; unit `y`.

The **store polynomial** `ΔS := S·y^S` (shapes `S`, `ΔS[s] = S` for every `s`).
It is the carrier of the store/costate comonad `ΔS(X) = S×X^S`.

### Lemma 0.1 (explicit forms — P1)
For finite sets `S,T`:
1. `ΔS ⊗ ΔT = Δ(S×T)` **on the nose**: both have shapes `S×T` and position set
   `S×T` at every shape (`ΔS[s]×ΔT[t] = S×T = Δ(S×T)[(s,t)]`). The Workers
   grading iso `μ_{S,T}` is the identity.
2. `ΔS ▷ ΔT` has shapes `{(s,g) : s∈S, g:S→T} = S×T^S`, and position set
   `S×T` at every shape `(s,g)` (a position is `(i,j)` with `i∈S`,
   `j∈ΔT[g(i)]=T`).

*Proof.* (1) Dirichlet formula. (2) `ΔS(ΔT(X)) = S·(T·X^T)^S = S×T^S×X^{S×T}`;
the shape `(s,g)` records `s∈S` and the branch map `g:S→T`, and the exponent
`Σ_{i∈S} ΔT[g(i)] = S×T`. ∎

At `|S|=|T|=2`: `ΔS⊗ΔT = 4·y⁴`, `ΔS▷ΔT = 8·y⁴`. They differ; `▷ ≠ ⊗` on the
store family. Write `A := ΔS⊗ΔT = Δ(S×T)` and `B := ΔS▷ΔT`.

---

## 1. The retract (P2)

**Definition.** Two `Poly` morphisms:

- **Section** `σ : A → B`.
  `σ₁(s,t) = (s, \mathrm{const}_t)` where `const_t : S→T` is constant at `t`;
  `σ♯_{(s,t)} : B[(s,const_t)] = S×T → A[(s,t)] = S×T` is the identity.
- **Retraction** `r : B → A`.
  `r₁(s,g) = (s, g(s))` (**self-evaluation**);
  `r♯_{(s,g)} : A[(s,g(s))] = S×T → B[(s,g)] = S×T` is the identity.

Both are well-typed: all fibres involved are literally `S×T`, so the identity
position maps typecheck.

### Theorem 1.1 (retract)
`r ∘ σ = id_A`, while `σ ∘ r ≠ id_B` for `|S|,|T| ≥ 2`. Hence `A = ΔS⊗ΔT`
is a **non-trivial retract** of `B = ΔS▷ΔT`.

*Proof.* **Shapes.** `(r∘σ)₁(s,t) = r₁(s,const_t) = (s, const_t(s)) = (s,t)`, the
identity. **Positions.** By the composition rule (note the reversal),
`(r∘σ)♯_{(s,t)} = σ♯_{(s,t)} ∘ r♯_{σ₁(s,t)} = id ∘ id = id`. The domains match
because `r₁(σ₁(s,t)) = (s,t)`, so `A[r₁σ₁(s,t)] = A[(s,t)]`. Thus `r∘σ = id_A`.

For the other order, `(σ∘r)₁(s,g) = σ₁(s,g(s)) = (s, const_{g(s)})`, which equals
`(s,g)` iff `g` is constant; so `σ∘r ≠ id_B` whenever a non-constant `g:S→T`
exists, i.e. `|S|,|T|≥2`. ∎

**Idempotent.** `e := σ∘r : B → B` satisfies `e² = σ(rσ)r = σr = e`; its
splitting is `A` (`r∘σ=id`). `e₁(s,g)=(s,const_{g(s)})`, `e♯ = id`. So `A` is the
image of the idempotent that **collapses each branch map `g` to the constant at
its self-evaluation `g(s)`.**

**Verification.** `verify_retract.py`: `r∘σ=id`, well-typed, `σ∘r≠id`, for
`(|S|,|T|) ∈ {(1,1),(2,2),(3,2),(2,3),(3,3)}`.

---

## 2. Coherence of the comparison (P3a, P3b)

The comparison maps are natural under **bijections** and satisfy the monoidal
coherence axioms — `σ` in the **oplax** direction, `r` in the **lax** direction.

### Proposition 2.1 (σ is oplax-coherent)
The oplax associativity hexagon commutes:
`(σ_{S,T} ▷ ΔU) ∘ σ_{S×T,U} = (ΔS ▷ σ_{T,U}) ∘ σ_{S,T×U} ∘ Δ(α)`
as maps `Δ((S×T)×U) → ΔS▷ΔT▷ΔU` (`α` the associator of `×`, `▷` strictly
associative). The unit condition holds: `σ_{S,1} : Δ(S×1) → ΔS▷Δ1 = ΔS` is the
right unitor.

*Proof.* Write the target in the canonical ternary form
`(s, g:S→T, k:S×T→U)`. Both composites send `((s,t),u)` to the **fully constant**
shape `(s, const_t, const_u)`: on the left, `σ_{S×T,U}` produces the constant
`U`-branch `const_u` and `σ_{S,T}▷ΔU` produces `const_t`; on the right, `Δα`
reindexes, `σ_{S,T×U}` produces the constant `(T×U)`-branch, and `ΔS▷σ_{T,U}`
splits it into `const_t` and `const_u`. All backward maps are identities except
`Δα` (the associator bijection), which exactly accounts for the reindexing
`(S×T)×U ≅ S×(T×U)`. Hence the two composites agree. ∎

### Proposition 2.2 (r is lax-coherent)
The lax associativity hexagon commutes:
`Δα ∘ r_{S×T,U} ∘ (r_{S,T} ▷ ΔU) = r_{S,T×U} ∘ (ΔS ▷ r_{T,U})`
as maps `ΔS▷ΔT▷ΔU → Δ(S×(T×U))`.

*Proof.* "**Self-evaluation is associative.**" Take a ternary shape `(s,g,k)`
(with `g:S→T`, `k:S×T→U`). The left composite evaluates `g` at `s` (giving
`g(s)`) then `k` at the resulting point `(s,g(s))`; the right composite evaluates
`k_i := k(i,-)` at `g(i)` inside each branch, then evaluates the outer store at
`s`. Both yield `(s,\,(g(s),\,k(s,g(s))))`. Backward maps are identities. ∎

### Corollary 2.3 (grading comparison, core groupoid)
On the core groupoid `(Set_≅, ×)`, `Δ` is a functor (a bijection `f:S→T` gives
`Δf` with backward `f^{-1}`), `σ` is a natural transformation, and:
`(Δ, σ)` is **oplax** symmetric monoidal and `(Δ, r)` is **lax** symmetric
monoidal into `(Poly, ▷)`, with `r∘σ = id`. The strong `⊗`-grading
(`μ_{S,T}=id`) is thereby realised as a **retract of the `▷`-comparison
structure.**

**Verification.** `verify_p3.py`: hexagon (both `σ` and `r`) and unit hold for
all `(|S|,|T|,|U|)` up to `(2,3,2)`; `σ` natural under (reversal) bijections up
to size 3.

---

## 3. The store comonad is *not* the oplax image of the diagonal (P3c, P3d)

The store comonad `ΔS` has comultiplication
`δ : ΔS → ΔS▷ΔS`, `δ₁(s) = (s, id_S)`, `δ♯_s(i,j) = j`
(from `δ_X(s,h) = (s, λs'.(s',h))`), and counit `ε:ΔS→y`, `ε₁(s)=*`,
`ε♯_s(*) = s` ("current position"). This is the codiscrete category on `S`.

### Theorem 3.1 (diagonal collapse — the precise "⊗ is the diagonal of ▷")
Let `d : S → S×S` be the diagonal and `Δ(d) : ΔS → Δ(S×S)` its store image with
backward `π₂` (shape `s↦(s,s)`, positions `(i,j)↦j`). Then
`r_{S,S} ∘ δ = Δ(d).`
Equivalently: **the store comultiplication `δ` is a lift of the `⊗`-diagonal
`Δ(d)` along the retraction `r`.**

*Proof.* Shapes: `s ↦ δ₁(s)=(s,id_S) ↦ r₁(s,id_S)=(s, id_S(s))=(s,s)`, matching
`Δ(d)`. Backward: `(r∘δ)♯_s = δ♯_s ∘ r♯_{(s,id)} = δ♯_s = π₂`, matching. ∎

### Theorem 3.2 (the store comonad is not the `⊗`-retract image of the diagonal)
The store comonad structure on `ΔS` does **not** arise from the `⊗`-retract
comparison `σ` via the Set-diagonal. Precisely:

1. `δ ≠ σ_{S,S}∘Δ(d)` for `|S|≥2`: the store comultiplication has branch
   component `id_S`, the comparison-image has `const_s`.
2. `σ_{S,S}∘Δ(d) = e∘δ =: δ'` (with `e=σr`), and `δ'` is **coassociative but not
   counital** — hence **not a comonad**. So the "oplax image of the diagonal
   comonoid" recipe cannot yield the store comonad (or any comonad) here.

*Proof.* (1) `δ₁(s)=(s,id_S)`, while by Thm 3.1
`(σ∘Δd)₁(s) = σ₁(s,s) = (s,const_s)`; these differ for `|S|≥2`.
(2) `σ∘Δd = σ∘r∘δ = e∘δ =: δ'`, so `δ'₁(s)=(s,const_s)`, `δ'♯_s(i,j)=j`. `δ'` is
coassociative (direct check / computation). For any counit candidate `ε` with
`ε♯_x(*)=c(x)`, the right-counit composite `(ΔS▷ε)∘δ'` has backward map
`i ↦ δ'♯_s(i,c(s)) = c(s)`, constant in `i`, hence never `id` for `|S|≥2`. So the
right counit law fails and `δ'` is not a comonad. ∎

**Remark (why no oplax structure realises the store comonad).** An oplax
symmetric monoidal functor sends comonoids to comonoids; every set `S` is a
comonoid via `(d,!)`. If `Δ` were oplax with comparison `σ`, then `ΔS` would
carry the comonad `σ∘Δd = δ'`, which Thm 3.2(2) shows is not a comonad. Moreover
`σ` is the only natural *bifunctorial* comparison compatible with the
`⊗`-retract: a family `Δ(S×T)→ΔS▷ΔT` can only feed a single `t∈T` into the
branch map `S→T`, forcing `const_t` (the value `id_S` needed by `δ` is not even
type-correct off the diagonal `S=T`). Independently, `Δ` fails to be a functor on
non-invertible Set-maps under the canonical backward maps: `f:S→T` induces no map
`ΔT[fs]=T→ΔS[s]=S`. Thus the store comonad structure is **internal** to `ΔS`
(the cofree/codiscrete structure), not transported from `(Set,×)` along the
`⊗`-comparison. On the core groupoid `(Set_≅,×)` there is no diagonal to obstruct,
and `(Δ,σ)`/`(Δ,r)` are genuinely oplax/lax (Cor 2.3).

**Verification.** `verify_p3.py`: `r∘δ=Δ(d)` (`π₂`) for `n≤3`; `δ` (store) is a
comonad (both counit laws + coassoc); `δ'=σ∘Δ(d)` is coassociative but the right
counit law is `False` for `n=2,3`; `σ∘Δ(d)≠δ` for `n≥2`.

---

## 4. Verdict

| Question | Answer |
|---|---|
| Is `ΔS⊗ΔT` the `P=ΔS` fibre of BHM's `X↦X▷ΔS`? | **No.** `▷≠⊗` on the store family (`8y⁴` vs `4y⁴`). |
| Relationship of the two gradings | **Retract.** `A=ΔS⊗ΔT` splits `B=ΔS▷ΔT` via `(σ,r)`, `r∘σ=id` (Thm 1.1). |
| Is `Δ:(Set,×)→(Poly,▷)` lax / oplax / neither? | **Oplax (`σ`) and lax (`r`) on the core groupoid** `(Set_≅,×)` with `r∘σ=id` (Cor 2.3). On the **full** cartesian `(Set,×)` the comparison `σ` stays oplax-*coherent* (Prop 2.1) but does **not** upgrade to an oplax monoidal *functor*: it would force the non-comonad `δ'` onto `ΔS` (Thm 3.2), and the canonical `Δ` is not functorial on non-invertible maps. |
| Sense in which "`⊗` is the diagonal collapse of `▷`" | `r∘δ = Δ(d)` (Thm 3.1): the store comultiplication lifts the `⊗`-diagonal along `r`; the idempotent `e=σr` projects `δ` to its constant part `δ'`, and the discarded off-diagonal data `(non-constant branch maps g)` is exactly the failure of `▷` to be the `⊗`-diagonal. |
| Is the oplax-image structure `δ'` a comonad? | **No** — coassociative but not counital (Thm 3.2b). This is *why* `Δ` cannot be oplax on all of `Set`. |

**Grant framing.** Two composition disciplines on the same carrier `ΔS`: the
Workers `⊗`-grading (state *entanglement*, `Δ(S×T)`) and the BHM `▷`-grading
(state *nesting/store-of-store*, `ΔS▷ΔT`). They are not equal and not
fibre-related; they are related by a canonical retract whose idempotent is
"collapse each branch to its self-evaluation." Compositional correctness for
stateful agents thus has two genuinely different but explicitly comparable
regimes, and the store comonad's comultiplication is precisely the extra
structure `▷` sees that `⊗` collapses.

## Gaps / scope
- General proofs are complete; computational verification covers `n≤3`
  (`(2,3,2)` for the hexagons). The identities are natural-in-bijections
  polynomial identities with no size-dependent behaviour beyond the
  `|S|,|T|≥2` non-degeneracy already exhibited, so `n≤3` is conclusive for the
  qualitative claims (retract, coherence, collapse, non-comonad).
- "`σ` is the *essentially unique* natural bifunctorial comparison" (used in
  Thm 3.2b) is argued by the type/naturality constraint on branch maps; a fully
  formal uniqueness statement (enumerate natural transformations
  `Δ(-×-) ⇒ Δ(-)▷Δ(-)`) is left as a `computed`-level remark, not needed for the
  impossibility (obstruction (a) alone suffices for "not oplax").
