# Prove notebook — ΔS, the reader/store, and the category of Workers (2026-07-28)

## Objects and conventions

- **Container** `p = (A, B)`: shapes `A : Set`, positions `B : A → Set`. Extension `⟦p⟧X = Σ_{a:A} X^{B a}`.
- **Morphism** `p → q=(C,D)`: forward `f : A → C`, backward `f♯ : ∀a. D(f a) → B a`. Composition: forward
  composes forward, backward composes in reverse.
- **Dirichlet tensor** (PINNED: Niu–Spivak 2312.00990 Def 3.65; my note dirichlet-is-day-convolution):
  `p ⊗ q = (A×C, (a,c) ↦ B a × D c)`. Unit `y = (1, *↦1)`. Extension `⟦p⊗q⟧X = Σ_{a,c} X^{Ba×Dc}` (Day of ×).
- **⊗-internal hom** (Niu–Spivak Ex 4.78 / eq 4.75): `[q,r] = Π_{j∈C} r ◦ (D j · y)`.
- **ΔS** `= (S, s↦S)`: shapes `S`, EVERY fibre `= S`. So `⟦ΔS⟧X = Σ_{s:S} X^S = S × X^S`.

## KEY OBSERVATIONS (to verify)

1. **T1.** `ΔS` = codiscrete (indiscrete) category on `S` under `DCont≅Cat`. Directed-container structure
   forced: `o_s = s`, `s↓p = p`, `p⊕p' = p'` (⊕ = 2nd projection). Check D1–D5.
   `⟦ΔS⟧ = S×(−)^S = Store_S` (store/costate comonad, Uustalu–Vene). Counit `(s,v)↦v(s)`; comult
   `(s,v)↦(s, λp.(p,v))`.

2. **T2.** `⟦ΔS ⊗ p⟧X = Σ_{s,a} X^{S×Ba}`. At `p=y`: recovers `Store_S`. Reader `(−)^S` = the fibre functor.

3. **T3 (main).** `ΔS ⊗ ΔT = Δ(S×T)` STRICTLY; `Δ1 = y`. A **Worker** `p→q` with state `S` = container
   morphism `w : ΔS ⊗ p → q`. Composition: `w:ΔS⊗p→q`, `w':ΔT⊗q→r` compose to
   `w'∘(ΔT⊗w) : Δ(T×S)⊗p → r` — **state multiplies**. Category **graded by (Set,×)**. Identity grade `1`.
   coKleisli of the `(Set,×)`-graded comonad `S↦ΔS⊗−`. S-varying version = **Para** of that action
   (over Core(Set) — Δ functorial on bijections only). Gavranović Para (cite).

## Explicit Worker (coordinates)

`w : ΔS⊗p → q`, `ΔS⊗p = (S×A, (s,a)↦S×Ba)`, `q=(C,D)`:
- forward `f : S×A → C`
- backward splits: `f♯₁(s,a): D(f(s,a))→S` (new state), `f♯₂(s,a): D(f(s,a))→Ba` (position back-map).

Composite of `w` and `w':ΔT⊗q→r=(E,G)` (`g:T×C→E`, `g♯₁:...→T`, `g♯₂:...→D`):
`w'' : Δ(T×S)⊗p → r`
- forward `((t,s),a) ↦ g(t, f(s,a))`
- backward at `((t,s),a)`, `d':G(e)` where `e=g(t,f(s,a))`:
  - state ∈ T×S: `( g♯₁(t,f(s,a),d'), f♯₁(s,a, g♯₂(t,f(s,a),d')) )`
  - position ∈ Ba: `f♯₂(s,a, g♯₂(t,f(s,a),d'))`

State reads T×S (relabel S×T by symmetry). Convention: reading order gives state S×T.

## VERIFICATION RESULTS (verify.py + run_tests.py + stress.py) — ALL PASS
- D1–D5 for ΔS: OK for |S|=1,2,3.
- Comonad laws (store comonad) OK for S={a,b}, X={0,1},{0,1,2}.
- ΔS⊗ΔT = Δ(S×T) strict; Δ1=y. Profiles match.
- Worker composites: all 32 valid container morphisms (tiny), 400×256 valid (multi-shape).
- Unit laws: hold up to unitor (16 workers).
- Associativity: 512 triples (tiny) + 1369 triples (multi-shape) all equal up to ×-associator.

## To verify computationally
- [ ] D1–D5 for ΔS with o_s=s, s↓p=p, p⊕p'=p'. (S={a,b}, S={a,b,c})
- [ ] Comonad laws for the induced comonad = store comonad on finite X.
- [ ] ΔS⊗ΔT = Δ(S×T) as containers (shape + fibres).
- [ ] Worker composite is a valid container morphism ΔS⊗p→q → ... → Δ(T×S)⊗p→r.
- [ ] Associativity of Worker composition (3 workers, both bracketings equal up to ×-associator).
- [ ] Unit laws (id_p grade 1, both sides up to unitor).
