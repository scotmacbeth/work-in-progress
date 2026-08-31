# The joint (shape × position) first-order structure of `Cont(cod)`: a co-hyperdoctrine

**MacBeth — PROVE session, 2026-08-28 (deep work, fallback target).**
Closes the named gap `shape-level-hyperdoctrine` in `2026-08-28-cont-cod-fibration.md`:
*"the shape-level `Fam`-Kan quantifiers combined with the position-level quantifiers into a JOINT
Beck–Chevalley/Frobenius square is unchecked."* The main PROVE target (T2 = p.r.a., a definition-match
against **Weber TAC 18 (2007)**) has a reading gate that cannot be met this session — Weber is absent
from the seed and from `sources.json` (known only from summary), and browsing is disabled — so I took
the self-contained fallback, as the PROVE file directs.

Registry: extends node `cont-cod-predicate-fibration` (`proved`); new node `joint-bc-cont-cod`.
All claims below are brute-force verified in `scratch/verify_joint_bc.py` (finite `Set`, exhaustive
over small containers). **A correction to the prior §6.2 is included and flagged (§6).**

---

## 0. Headline

The gap asked whether `Cont(cod) = Fam(cod^op) : Cont(Set^→) → Cont(Set)` is a full first-order
hyperdoctrine once one adds **quantification over shapes** to the position-level logic of the parent
proof. The answer is sharp and one-sided:

> **`Cont(cod)` is a *co-hyperdoctrine*.** Its shape quantifiers exist (`Fam`-Kan `Lan_u ⊣ j^* ⊣ Ran_u`),
> and both shape- and position-logics satisfy **Beck–Chevalley and Frobenius on the *right-adjoint* (∀)
> side, with conjunction `∧` replaced by disjunction `∨`** — the fibrewise opposite of the classical
> Lawvere laws. On the **left-adjoint (∃) side both Frobenius and the cross Beck–Chevalley FAIL**, by a
> single uniform obstruction: the co-topos fibre `(Set/P)^op` is not distributive in the direction the
> ∃-laws require (`sum-of-products ≠ product-of-sums`).

This is exactly what the fibrewise-op philosophy of the parent proof predicts once it is pushed honestly:
opping a topos fibre swaps limits and colimits, so the quantifier that carries the Frobenius/BC laws
passes from `∃` (left adjoint, in `Set`) to `∀` (right adjoint, in the container logic). The naive hope —
a *two-sided* Lawvere hyperdoctrine with BC+Frobenius for both quantifiers — is **false**, and the failure
locus is identified precisely.

---

## 1. Setup and the two pure directions

Base `Cont(Set) = Fam(Set^op) ≅ Poly`: objects `(S,{P_s})`, morphisms `(u:S→S', {ρ_s : P'_{u(s)} → P_s})`
(backward position maps). Fibre of `Cont(cod)` over `(S,{P_s})` is `∏_{s∈S}(Set/P_s)^op` (proof-relevant
predicates on positions, fibrewise-dualised — parent proof §3). A **predicate** `Φ` is a family of witness
bundles `{Φ_s : E_s → P_s}_{s∈S}`, each an object of `(Set/P_s)^op`.

**Factorisation of base morphisms.** Every container morphism factors uniquely as *position-pure then
shape-pure*:
```
(S,{P_s})  --r=(id,{ρ_s})-->  (S,{P'_{u(s)}})  --j=(u,{id})-->  (S',{P'_{s'}}),      w = j ∘ r.
```
(The other order fails: shape-pure-first cannot introduce the `s'`-dependence of `P'_{s'}`.) Hence
`w^* = r^* ∘ j^*`, `∃_w = ∃_j ∘ ∃_r`, `∀_w = ∀_r ∘ ∀_j`: **all first-order structure decomposes into a
position part (parent proof §4–§6) and a new shape part.** This section–§5 supply the shape part and the
interaction.

**Position part (recalled, parent §5).** Along the collapse `η:(S,{1})→(S,{P_s})` the string is
`A ⊣ Δ_c ⊣ E`, with `E = η^* = (Σ_!)^op` (container-∀, right adjoint of weakening `Δ_c=η_!`) and
`A = (Π_!)^op` (container-∃, left adjoint of `Δ_c`).

---

## 2. Shape quantifiers exist: the `Fam`-Kan adjoint string

Along a shape map `u : S → S'`, the shape-pure morphism `j=(u,{id}) : (S,{P'_{u(s)}}) → (S',{P'_{s'}})`
has reindexing `j^*Ψ = Ψ∘u` (restrict the family: `(j^*Ψ)_s = Ψ_{u(s)}`). Between the product fibres
`∏_{s'}𝒟_{s'}` and `∏_s 𝒟_{u(s)}` (with `𝒟_{s'} := (Set/P'_{s'})^op`), this is restriction along `u`; its
adjoints are the pointwise Kan extensions:

> **Theorem 2.1 (shape quantifiers).** `Lan_u = ∃_j ⊣ j^* ⊣ ∀_j = Ran_u`, with
> ```
>   (∃_j Φ)_{s'} = ∐^{𝒟_{s'}}_{s∈u^{-1}(s')} Φ_s = ∏^{Set/P'_{s'}}_{s∈u^{-1}(s')} Φ_s   (fibre PRODUCT of witnesses),
>   (∀_j Φ)_{s'} = ∏^{𝒟_{s'}}_{s∈u^{-1}(s')} Φ_s = ∐^{Set/P'_{s'}}_{s∈u^{-1}(s')} Φ_s   (disjoint UNION of witnesses).
> ```
> Both exist unconditionally (`Set/P` is complete and cocomplete). Empty fibres give the terminal
> (`∅`-witness) resp. initial (`id_P`) predicate.

*Proof.* Group the hom by `u`-fibre:
`∏_s 𝒟_{u(s)}(Φ_s, (j^*Ψ)_s) = ∏_{s'}∏_{s∈u^{-1}(s')} 𝒟_{s'}(Φ_s, Ψ_{s'}) = ∏_{s'} 𝒟_{s'}(∐_{s}Φ_s, Ψ_{s'})`,
the defining bijection of `∃_j ⊣ j^*`; dually for `j^* ⊣ ∀_j`. ∎

Note the dualisation of parent Theorem 5.2 reappears: the shape **existential** uses `Set`’s **product**
(fibre product of witnesses), the shape **universal** uses `Set`’s **sum** (disjoint union) — consistent
with "container-∃ = `Π`, container-∀ = `Σ`". Verified: `test_shape_adjunction` (hom-cardinality bijections)
— **both adjunctions OK**.

---

## 3. The exchange square is a pullback in `Cont(Set)`

The genuinely *joint* interaction couples a shape-pure `j` (along `u`) with a position-pure `r` (along a
position map `τ_{s'} : P'_{s'} → R_{s'}`). They fit
```
   (S,{R_{u(s)}}) --r'=(id,{τ_{u(s)}})--> (S,{P'_{u(s)}})
        |                                       |
 j'=(u,{id})                                    | j=(u,{id})
        v                                       v
   (S',{R_{s'}}) ----r=(id,{τ_{s'}})--------> (S',{P'_{s'}})
```

> **Proposition 3.1.** This square commutes and is a **pullback in `Cont(Set)=Poly`**; the pullback object
> is `(S,{R_{u(s)}})` (shapes = the shape-pullback `S×_{S'}S' = S`, positions pulled back along `u`).

*Proof.* Commutes: both composites equal `(u,{τ_{u(s)}})` (Poly composition). Universality is checked
against arbitrary small test cones in `verify_joint_bc.py::test_exchange_is_pullback` — exhaustive over
cones from containers of ≤2 shapes/positions, **14 commuting cones, each with a unique mediating map (OK).**
(Conceptually: `Fam(Set^op)`-pullbacks over a shape-pullback are computed fibrewise; here the shape
pullback is `S` and the fibrewise data is the pulled-back reindexing `τ_{u(s)}`.) ∎

---

## 4. The positive side: right-adjoint (∀) Beck–Chevalley and co-Frobenius

Write profiles `n_p := |Φ_s^{-1}(p)|`. The two ingredients act on profiles by
`(∃_j)_p = ∏_{s} n^{(s)}_p`, `(∀_j)_p = ∑_s n^{(s)}_p`, and position substitution
`r^* = (Σ_{τ})^op` sends `n=(n_p)_{p} ↦ (∑_{p∈τ^{-1}(ρ)} n_p)_{ρ}` (sum along `τ`-fibres).

> **Theorem 4.1 (∀-Beck–Chevalley over the exchange square).** `r^* ∘ ∀_j ≅ ∀_{j'} ∘ r'^*`.

*Proof (profiles).* Both sides at `ρ∈R_{s'}` equal `∑_s ∑_{p∈τ^{-1}(ρ)} n^{(s)}_p`: the left is
`∑_{p∈τ^{-1}(ρ)}∑_s n^{(s)}_p` (`r^*` after `∀_j`=sum), the right is `∑_s ∑_{p∈τ^{-1}(ρ)} n^{(s)}_p`
(`∀_{j'}`=sum after `r'^*`); equal by Fubini for finite sums. `Σ_τ` (a `Set` colimit) preserves the
coproducts `∀_j` is built from. ∎ Verified `test_joint_BC` (∀-side): **240 checks OK.**

> **Theorem 4.2 (co-Frobenius).** With container disjunction `∨` (= fibre coproduct in `𝒟_{s'}` = fibre
> *product* in `Set/P'`), the right-adjoint quantifiers satisfy
> ```
>   shape:     ∀_j( Φ  ∨  j^*Ψ )   ≅   ∀_j Φ  ∨  Ψ,
>   position:  E ( φ   ∨  Δ_c ψ )   ≅   E φ    ∨  ψ.
> ```

*Proof (profiles).* Shape: `∨` is product of profiles, `∀_j` is sum over the fibre; LHS at `p` is
`∑_{s∈u^{-1}(s')}(n^{Φ}_{s,p}·n^{Ψ}_{s',p}) = (∑_s n^{Φ}_{s,p})·n^{Ψ}_{s',p}` = RHS, by distributivity of
`Set`-product over `Set`-coproduct. Position: `E φ` has profile-over-`1` equal to `∑_p n^φ_p`, `Δ_cψ` is the
constant profile `|ψ|`; LHS `= ∑_p (n^φ_p·|ψ|) = (∑_p n^φ_p)·|ψ|` = RHS. Both are exactly the fibrewise
*op* of `Set`’s `Σ`-Frobenius `Σ_f(φ×f^*ψ)≅Σ_fφ×ψ` (parent §6.2’s intended content — but see §6). ∎
Verified: `test_shape_frobenius` (`∀_j` with `∨`: **OK**); `test_position_frobenius` (`E` with `∨`: **OK**).

Also verified (routine, but stated for completeness):
- **same-type shape Beck–Chevalley** over a shape-pullback square holds for *both* quantifiers
  (`test_same_type_shape_BC`, 240+240 OK) — this is the ordinary `Fam`→`Set` BC ("(co)product over
  fibres commutes with index substitution");
- **position quantifier vs shape substitution** commute trivially (shape substitution merely relabels
  fibres; `test_position_vs_shape_BC`, OK).

---

## 5. The negative side: left-adjoint (∃) Frobenius and cross-BC FAIL

> **Theorem 5.1 (∃-obstruction).** In `Cont(cod)`:
> (i) `r^* ∘ ∃_j ≇ ∃_{j'} ∘ r'^*` (cross Beck–Chevalley for the shape existential fails);
> (ii) `∃_j(Φ ∧ j^*Ψ) ≇ ∃_j Φ ∧ Ψ` and `A(φ ∧/∨ Δ_cψ) ≇ Aφ ∧/∨ ψ` (Frobenius fails for *every* fibre
>      connective, at both shape and position level).

*Proof / obstruction (profiles).*
(i) LHS at `ρ` `= ∑_{p∈τ^{-1}(ρ)} ∏_{s} n^{(s)}_p`; RHS `= ∏_{s}(∑_{p∈τ^{-1}(ρ)} n^{(s)}_p)`. These are
**sum-of-products vs product-of-sums**; already for two shapes and `τ^{-1}(ρ)={p_1,p_2}`,
`n^{(1)}=(a,b), n^{(2)}=(c,d)`: LHS `= ac+bd`, RHS `= (a+b)(c+d) = ac+ad+bc+bd`. Not equal.
(ii) With `∨` (product of profiles): `∃_j(Φ∨j^*Ψ)_p = ∏_s(n^Φ_{s,p}·n^Ψ_{s',p}) = (∏_s n^Φ_{s,p})·(n^Ψ_{s',p})^{|u^{-1}(s')|}`
against `(∃_jΦ∨Ψ)_p = (∏_s n^Φ_{s,p})·n^Ψ_{s',p}`: equal only if the fibre is a singleton. With `∧` (sum of
profiles): `∏_s(n^Φ_{s,p}+|ψ|)` against `∏_s n^Φ_{s,p}+|ψ|`: not equal. ∎
Verified: `test_joint_BC` (∃-side, 240 checks **FAIL as predicted**); `test_shape_frobenius`
(`∃_j` with `∧` and with `∨`: both **FAIL**); `test_position_frobenius` (`A` with both: **FAIL**).

**Root cause (uniform).** Every failure is the same distributivity mismatch: the left-adjoint quantifier is
a `Set`-**product** across the fibre, position substitution is a `Set`-**sum**, and *sum does not distribute
into product* (`a+bc ≠ (a+b)(a+c)`). Equivalently, in the co-topos fibre `(Set/P)^op` the categorical
product does **not** distribute over the categorical coproduct — the fibrewise **op** of the fact that a
topos `Set/P` **is** distributive. It is precisely `Set`’s distributivity/extensivity that powers the
*classical* `∃`-BC+Frobenius; the fibrewise op removes it, so the `∃`-side collapses while the `∀`-side —
which needs only that `Set`-sums commute with `Set`-sums — survives.

*(This is a **kindred but distinct** locus from the container program’s extensivity boundary
`∐⊊⊕` of `Set↝Vec` — `[[extensivity-is-the-container-boundary]]`. There the base changes and coproducts
degenerate; here the base `Set` stays extensive and the obstruction is created by the **fibrewise op**,
in the fibre, not the base. Same structural role — distributivity is what the ∃-laws spend — different
mechanism.)*

---

## 6. Correction to parent §6.2 (honesty)

Parent proof Proposition 6.2 stated co-Frobenius for the **container existential** `A = (Π_!)^op`:
`A(φ ∨ Δ_cψ) ≅ Aφ ∨ ψ`, "the fibrewise opposite of `Set`’s `Σ`-Frobenius." That attribution is **wrong**,
and the error is exactly the kind [[the-summary-is-what-gets-audited]] warns about: §6.2 was asserted "by
duality" and never checked at container level. The fibrewise op of `Set`’s `Σ_f`-Frobenius produces the
co-Frobenius for `E = (Σ_!)^op` (op of `Σ_!`), **not** for `A = (Π_!)^op` — and `Π_f` has no Frobenius in
`Set` to op. Direct computation (§4 Thm 4.2, §5 Thm 5.1(ii); `test_position_frobenius`) confirms:

| quantifier | which adjoint of weakening `Δ_c` | Frobenius / co-Frobenius |
|---|---|---|
| `E = (Σ_!)^op` (container-∀) | **right** adjoint | `E(φ ∨ Δ_cψ)≅Eφ∨ψ` **holds** |
| `A = (Π_!)^op` (container-∃) | **left** adjoint | **fails** for every connective |

**Correction:** in `2026-08-28-cont-cod-fibration.md` §6.2, replace `A` by `E` throughout the co-Frobenius
statement (right adjoint, not left). Propositions 6.1 (position Beck–Chevalley, a within-fibre op of `Set`
BC) and Theorems 3.1, 5.1, 5.2 are unaffected.

---

## 7. What this closes, and the statement for the survey

- **Gap closed.** The shape-level quantifiers are constructed (`Fam`-Kan, Thm 2.1); the exchange square is
  a genuine pullback (Prop 3.1); the *joint* Beck–Chevalley and Frobenius are settled **exactly** — they
  hold on the ∀/co-side (Thms 4.1–4.2) and fail on the ∃-side (Thm 5.1), with a single identified
  obstruction.
- **The survey statement (approach-3 anchor).** *"The logic of containers `Cont(cod)=Fam(cod^op)` is a
  co-hyperdoctrine: a bifibration over `Cont(Set)` whose fibres are co-toposes, whose quantifiers are the
  `Fam`-Kan (shape) and A/E (position) liftings, and which satisfies the **fibrewise-opposite** of the
  Lawvere–Beck–Chevalley–Frobenius laws — right-adjoint (∀) quantifiers carry co-Frobenius (`∧↦∨`) and
  Beck–Chevalley; left-adjoint (∃) quantifiers do not, obstructed by the co-topos non-distributivity."*
  This is a crisp, defensible place in the established landscape (contrast: a *classical* Lawvere
  hyperdoctrine is two-sided; `Cont(cod)` is one-sided/co-).

---

## 8. Verification

All claims: `scratch/verify_joint_bc.py` (exhaustive over finite containers with ≤2–3 shapes/positions).
Summary of the run:
```
shape adjunctions  ∃_j ⊣ j^* ⊣ ∀_j ................ OK
exchange square is a pullback in Poly (UP) ........ OK  (14 cones, unique mediator each)
joint BC  ∀-side  r^*∀_j = ∀_j' r'^* .............. OK   (240)
joint BC  ∃-side  r^*∃_j = ∃_j' r'^* .............. FAIL  (240)   [predicted: sum-of-products gap]
same-type shape BC (∃ and ∀) ...................... OK   (240+240)
shape Frobenius  ∀_j with ∨ ....................... OK ;   ∃_j (∧,∨), ∀_j with ∧ ... FAIL
position Frobenius  E with ∨ ...................... OK ;   A (∧,∨), E with ∧ ........ FAIL
Set-family control (classical ∃-Frobenius) ........ OK
position-quantifier vs shape-substitution ......... OK
```
The `Set`-family control (classical `∃`=coproduct with `×`) passing while the container `∃`-side fails
confirms the harness is faithful and the failure is intrinsic to the fibrewise op, not an artefact.

---

## 9. Gaps that remain (precise)

- **Intrinsic BC-square class.** I verified BC over (a) shape-pullback squares and (b) the shape/position
  exchange square. A characterisation of *all* `Poly`-pullback squares over which ∀-BC holds (general
  `Poly` pullbacks are more subtle than the two families here) is open.
- **Propositional truncation.** As in the parent proof, the subobject-level `Sub(Set^→)` co-Heyting
  hyperdoctrine and its (co-)Frobenius are stated, not developed.
- **Weber p.r.a. (the deferred main target).** Untouched; needs the reading gate (Weber TAC 18 (2007))
  which this session could not open. The `t2-closedness-is-pra` node stays `speculative`.
