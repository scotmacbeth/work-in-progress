# Holonomy composition via the Zappa–Szép product — the state/directed cross-mode bridge

**MacBeth — PROVE session, 2026-08-12 (deep-work, cross-mode bridge).**
Companion to `2026-08-11-update-monad-liftings-holonomy-full.md` (the classification, proved) and
`2026-07-20-orchestration-reentrancy-obstruction-analytic.tex` (`[ω]=ε`, proved/Lean).

> **One line.** Composing two update monads that share a state set is a Zappa–Szép product on the
> position-threading monoid; the classifier of liftings composes cleanly by the ZS product of action
> categories **(a, proved)**; but the *isotropy* does **not** compose by the ZS product of factor
> isotropies **(b, REFUTED)** — the composite stabiliser is generically *larger*, so **orchestration
> synthesises holonomy that neither agent possesses** (emergent reentrancy, `S₃`-on-3-points witness);
> and in the aligned abelian case a degree-2 class `[ω]∈H²` obstructs the composite holonomy splitting
> as an *unentangled* product of the two factor holonomies **(c, proved, scoped)** — the stabiliser-level
> shadow of the orchestration reentrancy dichotomy `[ω]=ε`.

The honesty guardrails from `state/PROVE.md` both fired and both sharpened the result:
- **Degree mismatch is real** (§4): the factor holonomies are H¹-type data (representations); `[ω]` is
  an H² class deciding whether they assemble UNENTANGLED. Never an equality of the two.
- **Compute-first** (§2) *refuted* the conjectured isotropy law (b) before any proof, exactly as the
  guardrail demanded. The refutation is the discovery.

---

## 0. Setup and the internal-ZS reframing

Two update monads `Upd_{(S,P,↓)}`, `Upd_{(S,P',↓')}` share the state set `S` (Ahman–Uustalu 2013;
`Upd_{(S,Q,↓)}X = Σ_{f∈Q^S} X^S`, positions thread `s ↦ s↓f(s)`). A **distributive law**
`λ : Upd_{P'}∘Upd_{P} ⟹ Upd_{P}∘Upd_{P'}` is, by Ahman–Uustalu (*Distributive Laws of Directed
Containers*, TYPES 2013, published — "distributive-law based composition of directed containers
generalises the Zappa–Szép product of two monoids"; their matching-pair equations 11), a **matching
pair**: mutual actions `▷ : P'×P → P`, `◁ : P'×P → P'` making the carrier `P×P'` a monoid `Q = P⋈P'`,
the **Zappa–Szép product**, with

    (p,p')·(q,q') = ( p·(p'▷q) , (p'◁q)·q' ),      unit (o,o').

**The composite action on `S`.** Set `s ↓_⋈ (p,p') := (s↓p)↓'p'`. This is a `Q`-action iff, writing
`u:=s↓p` (which ranges over `S`),

    (★)   u ↓ (p'▷q) ↓' (p'◁q)  =  u ↓' p' ↓ q       for all u∈S, p'∈P', q∈P.

`(★)` is precisely the matched-pair compatibility on the state carrier — the ZS rewriting
`p'·q = (p'▷q)·(p'◁q)` transported through the action — which is exactly the naturality of `λ` restricted
to `S`. (Ahman–Uustalu's degenerate-`S` remark: when the position set does not depend on the state, `↓`
is a right monoid action on `S`; the composite directed container is again of this update type.)

> **Internal realisation.** When `Q = P⋈P'` is realised as an exact factorisation of a monoid/group
> `G = P·P'` (`P∩P'={e}`, every `g=pp'` uniquely) acting on `S`, then `s↓_⋈(p,p') = s·(pp') = s·g`, so
>
>     Stab_{P⋈P'}(s) ≅ Stab_G(s),   Stab_P(s) = Stab_G(s)∩P,   Stab_{P'}(s) = Stab_G(s)∩P'.
>
> This folds the update-monad isotropy question onto a classical one and drives §2–§3. Every internal
> exact factorisation is a ZS product and conversely (Brin; Ahman–Uustalu 2013), so no generality is
> lost for the finite witnesses.

---

## 1. Part (a): the classifier composes by the ZS product of action categories — **PROVED**

**Theorem (a).** The composite monad `Upd_{P}∘Upd_{P'}` is the update monad `Upd_{(S,Q,↓_⋈)}` for the ZS
product monoid `Q=P⋈P'` acting on `S` by `↓_⋈`. Hence its degree-1 proof-relevant polynomial monad
liftings are classified by

    liftings( Upd_{P}∘Upd_{P'} )   ≅   Fun( 𝔸(↓_⋈), Cat )   =   Fun( 𝔸(↓) ⋈ 𝔸(↓'), Cat ),

where `𝔸(↓)⋈𝔸(↓')` is the Zappa–Szép product of the two action categories: identity-on-objects `S`,
arrows `(p,p') : s → (s↓p)↓'p'`, composed by the matched-pair rewriting.

*Proof.* Three steps.

**(a1) Composite = update monad for `Q`.** By Ahman–Uustalu 2013 the DL `λ` is a matching pair with ZS
product monoid `Q=P⋈P'`; `(★)` (holding because `λ` was assumed) makes `↓_⋈` a right `Q`-action on `S`;
the DL-composition of the two update directed containers is the update directed container of `(S,Q,↓_⋈)`.

**(a2) Classification.** By the proved arc (`2026-08-11-update-monad-liftings-holonomy-full.md`,
Theorem "general update-monad classification": degree-1 proof-relevant polynomial monad liftings of any
`Upd_{(S,Q,↓)}` ≅ `Fun(𝔸(↓),Cat)`), applied to `(S,Q,↓_⋈)`:
`liftings ≅ Fun(𝔸(↓_⋈),Cat)`.

**(a3) `𝔸(↓_⋈) = 𝔸(↓)⋈𝔸(↓')`.** Compare the two categories directly.
- `𝔸(↓_⋈)`: objects `S`; one arrow `s --(p,p')--> s↓_⋈(p,p')=(s↓p)↓'p'` per `(p,p')∈Q`; composition =
  `Q`-multiplication (ZS product); identity `(o,o')`.
- `𝔸(↓)⋈𝔸(↓')` (ZS product of categories, `pairwise_zs_check.build_zs_product` on the one-object-per-
  state action categories): objects `S`; an arrow `s→u` is a composable pair
  `(α:s→t in 𝔸(↓), α':t→u in 𝔸(↓'))`, i.e. `α=p` (so `t=s↓p`) and `α'=p'` (so `u=t↓'p'=(s↓p)↓'p'`);
  thus arrows = pairs `(p,p')` with the same target; composition uses `λ` to slide an `𝔸(↓')`-arrow past
  an `𝔸(↓)`-arrow = the ZS multiplication on `Q`; identity `(o,o')`.

The two categories have equal objects, arrows, composition, and identities, so they are equal (iso,
identity-on-objects). ∎(a)

Thus the classifying object of the *composite* is built functorially from the two factor action
categories by the ZS product — the sense in which "the classifier is monoidal under composition."

---

## 2. Part (b): isotropy does **NOT** compose by the ZS product — **REFUTED**, replaced by (b')

Conjecture (b) (from `state/PROVE.md`): `Stab_{P⋈P'}(s) ≅ Stab_P(s) ⋈ Stab_{P'}(s)`. Guardrail 2 said:
finite-verify first; if it fails, reshape honestly. **It fails.**

**Theorem (b'), containment.** For every `s∈S`,

    Stab_P(s) ⋈ Stab_{P'}(s)   ⊆   Stab_{P⋈P'}(s) = End_{𝔸(↓_⋈)}(s) = { (p,p') : (s↓p)↓'p' = s },

as subsets of `Q ≅ P×P'`, where the left side is `{(a,a') : a∈Stab_P(s), a'∈Stab_{P'}(s)}`.

*Proof.* If `s↓a=s` and `s↓'a'=s` then `(s↓a)↓'a' = s↓'a' = s`, so `(a,a')∈Stab_Q(s)`. ∎

**Theorem (b'), properness — the refutation.** The inclusion is proper in general. Witness:
`G = S₃`, exact factorisation `P=A₃=⟨(123)⟩`, `P'=⟨(12)⟩` (machine-verified exact: every `g∈S₃` is
uniquely `p·p'`), natural action on `S={1,2,3}`. At `s=1`:

    Stab_G(1) = ⟨(23)⟩ ≅ C₂,     Stab_P(1) = A₃ ∩ Stab_G(1) = {e}   (no 3-cycle fixes a point),
                                  Stab_{P'}(1) = ⟨(12)⟩ ∩ Stab_G(1) = {e}   ((12) moves 1),

so `Stab_P(1) ⋈ Stab_{P'}(1) = {e} ⊊ C₂ = Stab_Q(1)`. **(b) is false.** ∎

**Exhaustive computational confirmation** (`general-M-liftings/zs_holonomy.py`): across all exact
factorisations of `S₃,S₄,A₄,D₄,ℤ/2×ℤ/2` (114 factorisations, 448 point-checks), the containment ⊆ held
in *every* case (an assertion that would abort on any violation never fired), and the inclusion was
**proper in 268/448 checks** — including the abelian ambient `ℤ/2×ℤ/2` via the diagonal factorisation
`⟨(01)(23)⟩·⟨(01)⟩` (8/32), so emergence is not a nonabelian artifact.

### 2.1 The discovery: orchestration synthesises holonomy

The nontrivial `(23)∈Stab_G(1)` factors as a length-2 word with **neither letter fixing `1`**: in the
`↓_⋈` convention (`P`-leg first), `(p,p') = ((123),(12))` fixes `1` because `1 ↓(123) = 2` and
`2 ↓'(12) = 1`, yet `(123)` moves `1↦2` and `(12)` moves `1↦2`.

> **Corollary (emergent holonomy).** Under (a), a composite lifting is a functor `F:𝔸(↓_⋈)→Cat`. Its
> **holonomy at `s`** is the restriction to the vertex monoid `Stab_Q(s)` — a representation of
> `Stab_Q(s)` on the fibre category `C_s`. The two *factor* holonomies are the restrictions of `F` along
> the wide inclusions `𝔸(↓)↪𝔸(↓_⋈)`, `𝔸(↓')↪𝔸(↓_⋈)`, i.e. representations of `Stab_P(s)`, `Stab_{P'}(s)`.
> At the `S₃` witness both factor holonomies are **trivial** (`Stab_P(1)=Stab_{P'}(1)=1`) while the
> composite holonomy is a genuine `C₂`-representation on `C_1`. **The composite carries holonomy absent
> from both factors** — a dispatch-and-return loop (out by `p`, back by `p'`) that is a nontrivial fibre
> automorphism though neither leg is a stabiliser. This is reentrancy created by orchestration, and it is
> exactly what (b)'s naive equality would have hidden.

This is a *better* theorem than the target: (b)-as-equality is the special **aligned** case
(`Stab_Q(s) = Stab_P(s)·Stab_{P'}(s)`), and its generic failure is the phenomenon the grant's
orchestration narrative actually wants — composition remembers more than the parts.

---

## 3. Part (c): `[ω]∈H²` obstructs *unentangled* splitting — **PROVED (aligned abelian scope)**

Guardrail 1 (degree gap) + `g-obstruction-is-h2-class` ("do not prove the nonabelian ZS case; scope to
the `ℤ/2` witnesses") fix the honest domain. Call `s` **aligned** if the containment (b') is an
equality, so `Stab_Q(s) = Stab_P(s) ⋈ Stab_{P'}(s)` is an internal exact factorisation of the vertex
group by its two factor isotropies. Write `A := Stab_P(s)`, `B := Stab_{P'}(s)`, `E := Stab_Q(s)`.

**Theorem (c').** Let `s` be aligned with `A,B` finite groups, `A` abelian and **normal** in `E`
(the semidirect/normal regime). Then:

1. `E` is an extension `1 → A → E → B → 1` with `B` acting on `A` by conjugation; rel that action its
   iso class is a Baues–Wirsching / group-cohomology class `[ω] ∈ H²(B;A)`.
2. If the conjugation action is trivial (e.g. `A` central, in particular the `ℤ/2` witness), then
   `[ω]=0  ⟺  E ≅ A×B` (**direct product**).
3. Under (a) each composite lifting `F:𝔸(↓_⋈)→Cat` has holonomy at `s` a representation `ρ` of `E` on
   the fibre `C_s`, restricting to the two factor holonomies `ρ_A=ρ|_A`, `ρ_B=ρ|_B`. Call `ρ`
   **unentangled** if `ρ(A)`, `ρ(B)` commute in `Aut(C_s)` (equivalently `ρ` factors through `A×B` — the
   independent/commuting combination `ρ_A⊠ρ_B` of the two agents' holonomies). Then, for trivial action:

   > **`[ω]=0` ⟺ `E≅A×B` ⟺ *every* composite holonomy is unentangled; `[ω]≠0` ⟺ `E` is non-direct (e.g.
   > `ℤ/4`) ⟺ there is a composite holonomy (already the regular one, `ρ=`left mult of `E` on itself) that
   > is entangled.** So `[ω]∈H²(B;A)` is the obstruction to the composite holonomy splitting as an
   > unentangled product of the two factor holonomies: `[ω]=0` puts the two agents' holonomies on
   > independent commuting registers of the fibre; `[ω]≠0` means orchestration **entangles** them.

*Proof.* (1) Standard: an extension of `B` by an abelian normal `A` with a fixed `B`-action is
classified up to equivalence by `H²(B;A)` (Eilenberg–Mac Lane; the Baues–Wirsching abelian case cited in
`g-obstruction-is-h2-class`). (2) For trivial action, `[ω]=0` gives the split *and* central extension,
which for abelian `A` is `A×B`; conversely `A×B` has `[ω]=0`. (3) If `E≅A×B` then every hom
`ρ:E→Aut(C_s)` restricts to `ρ_A,ρ_B` with commuting images (`Hom_{Grp}(A×B,H)≅{(f,g):[f(A),g(B)]=1}`),
so every composite holonomy is unentangled. If `E` is non-direct (`[ω]≠0`, trivial action), take `ρ=` the
regular representation of `E` on itself: `ρ(A),ρ(B)` are left-multiplications, which commute iff `ab=ba`
for all `a∈A,b∈B` iff `E=A×B` — false — so this composite holonomy is entangled. The equivalences chain
through (2). ∎(c')

**Degree honesty, explicit.** `ρ_A,ρ_B` are H¹-type data (representations = functors `BG→Cat`). Whether
they assemble into an unentangled joint representation is decided by the degree-2 class `[ω]∈H²(B;A)`
(plus the H¹-level action datum). `[ω]` is *not* equal to either holonomy; it is the second-order datum
governing their compatibility. This is the promised clean resolution of the degree gap: an H² class
governs whether an H¹ datum factors — never an equality of the two.

**Witness (compute-verified, `zs_holonomy.py` test 3).** `A=B=ℤ/2`, action trivial
(`Aut(ℤ/2)=1`), `H²(ℤ/2;ℤ/2)≅ℤ/2 = {0,ε}`:

| `[ω]` | `E = Stab_Q(s)` | factor holonomies | composite holonomy |
|---|---|---|---|
| `0` | `ℤ/2 × ℤ/2` (a,b commute) | two `ℤ/2` reps | **unentangled** `ρ_A⊠ρ_B` (commuting) |
| `ε` | `ℤ/4` (cyclic, non-split) | two `ℤ/2` reps | **entangled** order-4 automorphism; no splitting |

This is the **stabiliser-level shadow** of the orchestration reentrancy dichotomy
`[ω(K_ε)]=ε∈H²(Sk_C;𝒟)≅𝔽₂` (`orchestration-is-zappa-szep-weld`,
`lean-reentrancy-omega-equals-epsilon`, proved/Lean). **Distinct sites** — the reentrancy `[ω]` lives on
the *handoff category* `Sk_C`, this one on the *point-stabiliser* `B` — and I do **not** claim they are
the same cohomology class (that would repeat the fusion-category conflation error,
`cohomological-obstruction-family` correction). What is shown here: the *same* `ℤ/2` dichotomy, same
generator, arising intrinsically inside the update-monad isotropy from the *same* ZS-composition data.

---

## 4. Status ledger (honesty)

**Proved / exhaustively verified (this file):**
- (a) composite = `Upd_{P⋈P'}`; liftings ≅ `Fun(𝔸(↓)⋈𝔸(↓'),Cat)` — rigorous, on the proved 08-11
  classification + Ahman–Uustalu 2013 (published) ZS-composition + the elementary `𝔸(↓_⋈)=𝔸(↓)⋈𝔸(↓')`.
- (b') containment ⊆ (rigorous, one line) + properness (`S₃`/3-points, rigorous; exhaustive sweep
  448 checks, 268 proper, ⊆ never violated) ⟹ **(b) as stated is FALSE**.
- Emergent-holonomy corollary — rigorous given (a)+(b').
- (c') aligned-abelian `[ω]∈H²(B;A)` obstruction to unentangled splitting (rigorous via classical
  extension theory) + `ℤ/2` witness (compute-verified) welded to the reentrancy `[ω]=ε`.

**Gaps / scope (honest):**
1. **Degree-1, proof-relevant polynomial liftings** — inherited from the 08-11 arc (and the Reader/State
   proofs). Higher-degree/branching liftings not treated. This *generalises* their scope, not narrows.
2. **(c') scope: aligned + abelian + normal `A`.** The general (non-aligned) `s` has composite isotropy
   strictly larger than any ZS product of factor stabilisers (§2.1) — there the invariant is the full
   vertex monoid of `𝔸(↓_⋈)`, not a single H² class; and the nonabelian ZS obstruction is deliberately
   out of scope (`g-obstruction-is-h2-class`). The `ℤ/2` case is the clean, load-bearing witness.
3. **Two distinct `[ω]` sites** (handoff vs stabiliser) — related by the same ZS data and dichotomy, but
   NOT identified as one class. A future task: is the stabiliser `[ω]` the restriction of the handoff
   `[ω]` along `B·Stab → Sk_C`? Conjectural; not claimed.
4. **Internal-vs-external ZS.** §2–§3 witnesses use internal exact factorisations `G=PP'`; every ZS
   product is one and conversely, but the finite sweeps are internal. The abstract (a) is external and
   general.

**Cited (proved/published):** update-monad liftings ≅ `Fun(𝔸(↓),Cat)` (`2026-08-11-...`, proved);
Reader/State poles (proved); Ahman–Uustalu, *Distributive Laws of Directed Containers*, TYPES 2013
(published) — DL = matching pair = ZS product of monoids; Ahman–Uustalu, *Update Monads*, TYPES 2013;
reentrancy `[ω]=ε` (`orchestration-zs`, proved; `lean-reentrancy-omega-equals-epsilon`, Lean); H²
extension classification — Eilenberg–Mac Lane / Baues–Wirsching JPAA 38 (1985) (cited, not reproved).

## 5. Grant framing
The three proved composition modes now genuinely **weld**: the state/isotropy mode (holonomy) and the
directed/Zappa–Szép mode (`[ω]`) meet on the *same* ZS product, and the meeting reveals that composing
two coeffectful agents (i) classifies by the ZS product of their behaviour categories (a), (ii) can
create reentrant holonomy neither agent has (b'), and (iii) is unentangled precisely when a degree-2
class vanishes (c'). "Unprotected orchestration synthesises holonomy; a cohomology class certifies when
the composite is a clean product of the parts" is a one-sentence Impact anchor with a theorem under it.
