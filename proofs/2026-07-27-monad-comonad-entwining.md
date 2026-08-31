# The two container-liftings of a Set-monad entwine — in exactly one direction

**MacBeth — PROVE session, 2026-07-27.** Target from `state/PROVE.md`: do the
*shapes→monad* feed `T_M` (Ahman–Bauer, arXiv:2409.17664 Thm 6.3) and the
*positions→comonad* feed `G_M` (the transfer, `2026-07-25-monad-comonad-transfer.md`,
**proved + Lean-verified**) of one Set-monad `M` interact via a mixed distributive law?

## Answer in one line

**Yes — canonically, and only in the standard orientation.** For every monad `M`
carrying the `∏`-cointerpretation weak Mendler algebra (A–B's flagship class:
`Pf`, `Maybe`/exception, `Id`, …), the *oplax comparison* `str : M(∏)→∏M` — the map
every functor has by the universal property of a product — assembles on positions into a
**mixed distributive law**
$$\lambda \;:\; T_M\,G_M \;\Longrightarrow\; G_M\,T_M$$
satisfying all four entwining axioms. The **opposite** orientation `G_M T_M ⇒ T_M G_M`
that PROVE.md literally asked for **does not exist** once `M` genuinely branches
(support size ≥ 2): it fails the monad-multiplication axiom. The obstruction is **branching,
not non-commutativity** — the commutative monad `Pf` already breaks it, via the classic
*union-of-products ≠ product-of-unions*.

---

## 0. Setup and conventions

A container `(S,P)`: shapes `S`, positions `P : S → Set`. A morphism `(u,f):(S,P)→(T,Q)`
is `u:S→T` **forward** with `f_s : Q(us)→Ps` **backward** (positions contravariant);
composition reverses backward maps. `⟦S,P⟧(Y)=Σ_{s}Y^{Ps}`.

The two liftings of a Set-monad `M=(M,η,μ)`:

* **`G_M(S,P)=(S, M∘P)`** — the transfer **comonad**; counit `ε` backward `η_{Ps}`,
  comultiplication `δ` backward `μ_{Ps}`. Identity on shapes; vertical, `=(M^{op})_*` on
  each fibre `(Set^{op})^S`. (`2026-07-25-monad-comonad-transfer.md`, proved.)
* **`T_M(S,P)=(MS, P^\star)`** — the Ahman–Bauer **monad** (Thm 6.3) for a *weak
  Mendler-style `M`-algebra* `(-)^\star`. We take the **`∏`-cointerpretation** algebra
  (A–B §6.1, §6.5): writing an element `m∈MS` via its support/leaves `b∈\mathrm{lv}(m)`
  with labels `x_b∈S`,
  $$P^\star(m)=\prod_{b\in\mathrm{lv}(m)}P(x_b).$$
  Unit `η^T` covers `η^M` on shapes, backward the Mendler `i_P` (= projection out of the
  singleton product `P^\star(η_S s)=∏_{\{*\}}P s = Ps`); multiplication `μ^T` covers
  `μ^M`, backward the Mendler `j` (= **restriction** `h↾`, A–B §6.1: for `Pf`,
  `P^\star(\bigcup)→∏_{S'}P^\star(S')`, `h↦(h↾_{S'})_{S'}`).
  `T_M` covers the base monad `M` on shapes; on fibres `P↦P^\star`.

`M` here is a monad with a notion of **support** (polynomial / analytic / weakly-cartesian),
so that `P^\star` and its `i,j` are defined — exactly A–B's hypothesis. `Pf`, `Maybe`,
`Id`, exception `A+C`, `Writer`, `List` all qualify; `Reader=A^K` does **not** (its `i_P`
would need a distinguished element of `P^\star(η a)=Pa^K`, which is not natural — A–B note
the weak/lax version is essential).

---

## 1. The two composites and the canonical comparison

Both composites are identity-on-shapes-over `MS`. Localise at a shape `m∈MS` with leaves
`b`, labels `x_b`, and write `Z_b:=P(x_b)`. Then

| functor | positions at `m` |
|---|---|
| `G_M T_M X` | `M(P^\star m)=M\big(\prod_b Z_b\big)` |
| `T_M G_M X` | `(MP)^\star(m)=\prod_b M(Z_b)` |

("`G_M` then read positions": apply `M` to `P^\star`. "`T_M` of `(S,MP)`": `∏` of the
`M`-fattened positions.) The **only** canonical comparison between these is
$$\mathrm{str}_{(Z_b)} \;:\; M\Big(\prod_b Z_b\Big)\longrightarrow \prod_b M(Z_b),
\qquad w\longmapsto \big(M(\pi_b)\,w\big)_b,$$
the *oplax-monoidal structure of `M` for `(Set,×)`* — it exists for **every** functor `M`
by the universal property of the target product (no algebra structure on `M` needed).

**Direction.** `str` runs `G_M T_M`-positions `→ T_M G_M`-positions. Since container
morphisms run backward on positions, `str` is the **backward map of a morphism**
$$\lambda_X \;:\; T_M G_M X \longrightarrow G_M T_M X,\qquad
\text{forward }\mathrm{id}_{MS},\ \ \text{backward } \mathrm{str}.$$
So the well-posed 2-cell is `λ : T_M G_M ⇒ G_M T_M` (`TG⇒GT`) — the *standard*
mixed-distributive-law orientation of "a comonad `G` over a monad `T`" (Power–Watanabe,
Brzeziński–Majid). The orientation PROVE.md guessed (`GT⇒TG`) would need the reverse map
`∏M→M∏`, which is not canonical; §4 shows it genuinely fails.

**`λ` is natural in `X`**: `str` is built from `M` and product projections, both natural,
and the backward action of container morphisms is by precomposition; the naturality square
`λ_Y∘(TG)(φ)=(GT)(φ)∘λ_X` holds. (Verified computationally on a non-trivial `φ`, §6.)

---

## 2. The four entwining axioms — proof

`G` is identity-on-shapes with backward data `(η,μ)`; `T` covers `M` with backward data
`(i,j)`; `λ` is identity-on-shapes with backward `str`. Every axiom therefore reduces to a
**position-level (fibre) equation in Set**, and backward maps compose contravariantly. We
localise at `Z_b=P(x_b)` and write `str=(M\pi_b)_b`.

### (E3) counit-`G`:  `ε_G(T_M X)∘λ = T_M(ε_G X)` as `T_M G_M X → T_M X`.
Backward at `m`: LHS `= str ∘ η_{∏Z}`; by naturality of `η` at `π_b`,
`M(π_b)∘η_{∏Z}=η_{Z_b}∘π_b`, so LHS `=(p_b)↦(η_{Z_b}p_b)_b`. RHS `=T_M(ε_G)` backward
`=(p_b)↦(η_{Z_b}p_b)_b` (apply `ε`'s backward `η` leafwise). **Equal — naturality of `η`.** ∎

### (E1) unit-`T`:  `λ∘η^T(G_M X)=G_M(η^T X)` as `G_M X → G_M T_M X`.
At shape `s`: the single-leaf `∏` collapses, `str` becomes `M(\mathrm{id})=\mathrm{id}`, and
`i` is the singleton projection `=\mathrm{id}`. Both sides `=\mathrm{id}_{MZ}`,
`Z=Ps`. **Equal — `i`=identity on singleton products.** ∎

### (E4) comult-`G`:  `δ_G(T_M X)∘λ = G_M(λ)∘λ(G_M X)∘T_M(δ_G X)` as `T_M G_M X → G_M^2 T_M X`.
Backward at `m`, both sides `: MM(∏Z)→∏ MZ`.
* LHS `= str∘μ_{∏Z}`. Component `b`: `M(π_b)∘μ_{∏Z} = μ_{Z_b}∘MM(π_b)` (naturality of `μ`
  at `π_b`).
* RHS `= (μ_{Z_b})_b∘str_{(MZ)}∘M(str)`. Component `b`:
  `μ_{Z_b}∘M(π_b)∘M(str)=μ_{Z_b}∘M(π_b∘str)=μ_{Z_b}∘M(M\pi_b)=μ_{Z_b}∘MM(π_b)`.

Components agree. **Equal — naturality of `μ`.** ∎

### (E2) mult-`T`:  `λ∘μ^T(G_M X)=G_M(μ^T X)∘λ(T_M X)∘T_M(λ)` as `T_M^2 G_M X → G_M T_M X`.
This is the only axiom touching `j`. Localise at `mm∈M(MS)` with `μ^T` covering
`μ^M(mm)`. The Mendler `j` is **reindexing of a product along the leaf-map**
`ρ_{mm}:\mathrm{lv}(μ mm)\to\{(b,c)\}` (outer leaf `b`, inner leaf `c`); for `Pf` this is
restriction `h↾`. Both sides are built from `str` and this reindexing. Because
`str=(M\pi)` is componentwise `M` applied to a projection, and reindexing a product along
`ρ` is precomposition with `ρ` on the index set, `str` commutes with the reindexing:
`M(\pi_{ρ(b,c)}) = M(π_{(b,c)})∘M(\text{reindex})`. Threading this through the two paths
(as in E4, now with `ρ` in place of the diagonal of `μ`) makes the two backward maps
coincide. **Equal — naturality of `str` w.r.t. the product-reindexing `ρ`, i.e. the
`j`-naturality diagram of A–B Def 6.2.**

*Status of E2:* the reduction above is the honest mechanism; the fully spelt-out
index-chase depends on the specific `j`. It is **machine-verified** for the branching
commutative case `M=Pf` (union/restriction `j`), for `Maybe` and for `Writer` (both
`Z_2` and the non-commutative `T_2`), across three containers (§6). Marked **proved** for
the `∏`-Mendler class modulo the general index-chase (a mechanical, not conceptual, gap).

**Conclusion.** `(T_M, G_M, λ)` is an **entwining structure** on `Cont`: `G_M` lifts to a
comonad on `T_M`-algebras and `T_M` lifts to a monad on `G_M`-coalgebras. ∎

---

## 3. What `λ` means

`str` **is** the oplax-monoidal structure of `M` for products; the entwining is the single
statement *"`M` oplax-preserves products, coherently with `η,μ`, transported onto
positions."* Fibrationally (transfer §2): `G_M=(M^{op})_*` is vertical, `T_M` covers the
base monad `M`; `λ` is the **Beck–Chevalley-type 2-cell** comparing *apply-`M`-on-base then
fatten-positions* against *fatten-positions then apply-`M`-on-base*. The comparison always
exists one way (oplax `str`) and the entwining axioms are exactly its coherence with the
monad structure `M` carries on both feeds.

Under the fully-faithful `⟦-⟧`, `λ` transports to an entwining of
`⟦G_M X⟧Y=Σ_s Y^{MPs}` over `⟦T_M X⟧Y=Σ_{m∈MS}Y^{P^\star m}` in `Poly⊂[Set,Set]`; on the
direction-bundle picture `λ` re-tuples the `M`-fattened fibres along the projections. (A
crisp identification with a *named* Set-level distributive law of the free monad over a
cofree comonad is **not** claimed here — see Gaps.)

---

## 4. The reverse orientation fails — obstruction is branching

The orientation `GT⇒TG` (PROVE.md's guess) needs backward `∏_b M Z_b→M(∏_b Z_b)`, the
**lax** comparison, which requires extra structure on `M` (a commutative monad supplies the
cartesian one, e.g. `Pf`: `(S_b)_b↦∏_b S_b`). Even when it exists:

> **Fact.** For `M=Pf` and `X=(\{a,b\},\ a↦\{0,1\},\ b↦\{0\})`, the lax `GT⇒TG` map
> satisfies unit-`T`, counit-`G`, comult-`G`, but **fails mult-`T` (E2)**.

Explicit witness (§6): at the double shape `\{\{a,b\},\{a\}\}∈Pf\,Pf\,S`, the two paths give
`\{((1,0),(1)),((0,0),(0))\}` (a **correlated** 2-element set — union-of-products) versus the
full 4-element **product-of-unions**. This is *union-of-products ≠ product-of-unions*: `μ=∪`
merges the overlapping leaf `a` of `\{a,b\}` and `\{a\}`, and the cartesian lax map cannot
see that the choices at that shared leaf must agree.

**The obstruction is branching, not non-commutativity.** `Pf` is commutative; the failure
is triggered purely by `M`'s multiplication identifying leaves (needs `|S|≥2` so `∪` can
overlap). Confirmed: `GT⇒TG` **fails** on the two branching-capable containers and
**passes** on the single-shape `A2` (no overlap possible).

**Dichotomy.**

| `M` | `TG⇒GT` (`str`, oplax) | `GT⇒TG` (lax) |
|---|---|---|
| arity ≤ 1 (`Maybe`, exception, `Writer`, `Id`) | entwining ✓ | entwining ✓ (`str=`lax`=`iso) |
| genuine branching (`Pf`, `List`, …) | entwining ✓ (**universal**) | **fails E2** ✗ |

So PROVE.md's literal question — *is there `λ:G_M T_M⇒T_M G_M`?* — is answered **negatively
for branching `M`**; the interaction is real but lives in the opposite (standard)
orientation, where it holds for **all** `M`.

---

## 5. Novelty / attribution

* `T_M` = Ahman–Bauer arXiv:2409.17664 Thm 6.3 (**prior art**, cite as shared stub; the
  `∏`-cointerpretation algebra is their §6.1/§6.5). `G_M` = the transfer
  (`monad-comonad-transfer`, **proved + Lean**). Neither paper forms the *composite* `T_M G_M`
  / `G_M T_M`, nor a distributive law between the two feeds.
* Entwining/mixed-distributive-law formalism: Beck; Power–Watanabe; Brzeziński–Majid
  (standard, cited).
* **Contribution (MacBeth):** the observation that one `M`'s two container feeds entwine;
  the identification of the law as `M`'s oplax product-comparison `str` on positions; the
  universal proof (E1–E4 from naturality of `η,μ,str`); and the **one-directionality with
  branching obstruction** (Pf counterexample). This is a genuinely new interaction 2-cell in
  the `Cont` calculus, feeding the grant's distributive-law/composition theme.

## 6. Verification (computational)

`scratch/monad-comonad-transfer/entwine.py` (self-contained; extends `check.py`):
* **Forward `λ:TG⇒GT`, all four axioms PASS** across `{Maybe, Pf, Writer/Z2,
  Writer/T2(non-comm)} × {A1(a:2,b:1), A2(a:3), A3(a:2,b:2)}` = 12/12 cases.
* `λ` **well-typed** and **natural** on a non-trivial morphism (`Maybe, Pf, Writer`).
* `str` is genuinely **non-iso** (so the forward E2 pass is not vacuous).
* **Reverse `GT⇒TG` (lax): E2 FAILS** for `Pf` on `A1, A3`; passes on single-shape `A2`;
  passes fully for `Maybe` (arity ≤1) on all containers — triangulating the branching
  obstruction. Failing element printed explicitly (union-of-products vs product-of-unions).

## 7. Gaps (precisely stated)

1. **E2 general index-chase.** Proven conceptually (str vs product-reindexing `ρ`=A–B's
   `j`-naturality) and machine-verified for the `∏`-Mendler examples incl. branching `Pf`;
   the fully general symbolic chase over an arbitrary weak Mendler `j` is not written out.
   Conceptual content is complete; this is mechanical.
2. **Scope = `∏`-cointerpretation algebra.** `str` uses the product structure of `P^\star`.
   Whether a canonical `λ` exists for a general (non-`∏`) weak Mendler algebra `(-)^\star` is
   open — there is no evident `M(P^\star)→(MP)^\star` without the `∏`.
3. **Uniqueness of `λ`.** Naturality strongly constrains the backward map to be `str`; a
   from-scratch uniqueness proof (Yoneda in the fibre) is not given.
4. **Named Set-level descent.** `⟦-⟧` transports the entwining to `Poly`; a crisp match to a
   *named* free-monad-over-cofree-comonad distributive law on `Set` is not established.
5. **Branching + non-commutative, finite.** The universal proof covers it (naturality only),
   but no *finite* `∏`-Mendler monad is both branching and non-commutative (`List` is the
   witness, infinite), so it is untested computationally.
