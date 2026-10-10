# The band boundary of the supply-chain inventory gerbe

**MacBeth — deep-work prove session, 2026-10-10.**

**Status: PROVED** (clauses (a), (b)) **+ witnessed** (clause (c): nontrivial-band witness,
computed then proved). This removes the *trivial-band scope hypothesis* of the 2026-10-08 inventory
gerbe theorem (`proofs/2026-10-08-supply-chain-inventory-gerbe.md`, root **proved**) by settling the
*band* question — the program's first genuinely **nonabelian** content.

Builds on: `supply-chain-inventory-gerbe-h2` [proved] (Thm A/B/C, Prop D; the transport `ρ`, the
reduced nerve, the centre coefficients `Z(Aut F)`). Cited standard theory: Giraud (*Cohomologie non
abélienne*, III — the three-stage band factorization), Breen (bitorsors), and the classical
automorphism-group arithmetic of `S_n` (Rotman, *An Introduction to the Theory of Groups*, 4th ed.,
Thms 7.5–7.7: `S_n` is complete for `n ≠ 2, 6`, and `Out(S_6) = ℤ/2`).

Computational corroboration: `scratch/band_boundary_verify.py`, `scratch/clause_a_D4_check.py`
(and the S₆ witness, below).

---

## 0. Where this sits — the three Giraud strata

Giraud's classical theorem factors `G`-gerbe classification over a base `X` (for us `X = N(C)`, the
nerve of the supply-chain category `C`, with structure group `G := Aut F`) in **three strata**:

| stratum | datum | invariant | lives in |
|---|---|---|---|
| 1 (unbanded) | the gerbe's structure 2-group cocycle | `π₀(G\text{-Gerbe}) ≅ H¹(X; \mathrm{AUT}(G))` | nonabelian `H¹`, autom.-2-group coeffs |
| **2 (band)** | the **outer** transport `ρ := q∘α` | `β := [ρ] ∈ H¹(X; \mathrm{Out}\,G)` | **nonabelian `H¹`, `Out G` coeffs** |
| 3 (fixed band) | the centre cocycle | `[𝔤] ∈ H²(X; Z(G))_β` (twisted by `β`) | abelian `H²`, `Z(G)` coeffs |

The 2026-10-08 theorem computed stratum 3 **in the special case `β = 0` (trivial band)**: there
`[𝔤] ∈ H²(N(C); Z(Aut F))` with untwisted coefficients, and a strict global inventory exists iff
`[𝔤]=0` (Thm A). That result carried the honest scope hedge *"we trivialize the band."* **This note
settles stratum 2**: it gives the band-triviality criterion (a), shows fungible stock is invisible to
it (b), and exhibits a nonvacuous band (c). Stratum 2 is **prior to and independent of** stratum 3 and
is the first place genuinely nonabelian ( `Out G` nonabelian / inner-vs-outer ) data appears.

**Conventions.** For a group `Q` (constant coefficients) write `H¹(N(C); Q)` for nonabelian degree-1
cohomology over the nerve: a **cocycle** is a functor `C → BQ`, i.e. a map `γ: \mathrm{Mor}\,C → Q`
with `γ(gf)=γ(g)γ(f)`, `γ(\mathrm{id})=e`; two cocycles are **cohomologous** iff related by an
object-relabeling `λ: \mathrm{Ob}\,C → Q`, `γ'(f\colon x→y)=λ(y)\,γ(f)\,λ(x)^{-1}`. Then
`H¹(N(C);Q) := Z¹/{\sim}`, pointed by the trivial cocycle `γ≡e`; `[γ]=0` means `γ ∼ e`. (For `Q`
abelian this is ordinary simplicial `H¹` of `N(C)`; for `Q` nonabelian it is a pointed set.)

---

## 1. Setup: the transport, the band, and the two structure groups

Let `C` be a small category (directed container: objects = nodes, morphisms = logistics operations),
`N(C)` its nerve, `F` the inventory fibre, `G := Aut F` the relabelling group. Local inventory
trivializations are the local objects of an `Aut F`-gerbe over `N(C)`; comparing charts across a
morphism `f: x→y` transports the structure group by an **automorphism** of `G`. Collecting these:

> the **transport** `α: \mathrm{Mor}\,C → \mathrm{Aut}(G)`, functorial up to inner automorphism.

(Strictly: the gerbe presents a pseudofunctor `C → \mathrm{Aut}(G)\text{-}\mathbf{Tors}`; since `C` is a
1-category the 1-cells are the `α_f ∈ \mathrm{Aut}(G)` and the 2-cell coherence data — the stratum-3
datum — is valued in `Z(G)`. The only fact we need now is that `α_{gf}` and `α_g α_f` agree **modulo
inner automorphisms of `G`**, because re-trivializing a chart conjugates the transport.)

Recall the inner/outer sequence of `G`:

> `1 → Z(G) → G \xrightarrow{\;\mathrm{conj}\;} \mathrm{Aut}(G) \xrightarrow{\;q\;} \mathrm{Out}(G) → 1,`
> with `\mathrm{Inn}(G) = \mathrm{im(conj)} = \ker q ≅ G/Z(G)`.   (★)

**Definition (band).** The **band** (lien) of the gerbe is the composite outer transport

> `ρ := q ∘ α : \mathrm{Mor}\,C → \mathrm{Out}(G).`

**Lemma 0 (the band is always a strict cocycle).** `ρ` is a genuine functor `C → B(\mathrm{Out}\,G)`,
i.e. `ρ(gf)=ρ(g)ρ(f)` and `ρ(\mathrm{id})=e`, so `[ρ] ∈ H¹(N(C); \mathrm{Out}\,G)` is well-defined —
regardless of the up-to-inner slack in `α`.

*Proof.* By the setup `α_{gf} = \iota · α_g α_f` for some inner `\iota ∈ \mathrm{Inn}(G) = \ker q`.
Apply `q`: `ρ(gf) = q(α_{gf}) = q(\iota)\,q(α_g)q(α_f) = q(α_g)q(α_f) = ρ(g)ρ(f)`, since
`q(\iota)=e`. Normalization `ρ(\mathrm{id})=e` is immediate. The inner slack dies in `Out`, so `ρ`
depends only on `α \bmod \mathrm{Inn}`. ∎

So the band is the **outer-automorphism-valued transport**; its class `β := [ρ]` is the stratum-2
invariant. "Band trivial" (the 10-08 hypothesis) means **`β = 0`**.

---

## 2. Clause (a): the band-triviality criterion

> **Theorem (a).** `β = 0 ∈ H¹(N(C); \mathrm{Out}\,G)` **iff** the transport `α` is, up to an
> `\mathrm{Out}\,G`-relabeling of objects, valued in inner automorphisms — precisely: iff there is a
> cocycle `α̃ : C → B(\mathrm{Aut}\,G)`, cohomologous to `α` via an `\mathrm{Aut}\,G`-valued object
> relabeling, with `α̃(f) ∈ \mathrm{Inn}(G)` for every morphism `f`.
>
> In particular, **if `α` already lands in `\mathrm{Inn}(G)`** (the transport is pointwise inner) then
> `β=0`; this is the literal "trivial band," and the theorem says `β=0` is exactly its
> gauge-invariant closure.

*Proof.*

(⇐) Suppose `α̃ = μ·α` with `μ: \mathrm{Ob}\,C → \mathrm{Aut}\,G` and `α̃(f) ∈ \mathrm{Inn}\,G=\ker q`
for all `f`. Set `λ := q∘μ : \mathrm{Ob}\,C → \mathrm{Out}\,G`. For `f: x→y`,
`ρ(f) = q(α(f)) = q\big(μ(y)^{-1} α̃(f) μ(x)\big) = λ(y)^{-1}\,q(α̃(f))\,λ(x) = λ(y)^{-1}λ(x),`
since `q(α̃(f))=e`. The relabeling `λ` then trivializes `ρ`:
`λ(y)\,ρ(f)\,λ(x)^{-1} = λ(y)λ(y)^{-1}λ(x)λ(x)^{-1} = e`, so `ρ ∼ e`, i.e. `β = [ρ] = 0`. ✓

(⇒) Suppose `β = 0`: there is `λ: \mathrm{Ob}\,C → \mathrm{Out}\,G` with `ρ(f) = λ(y)^{-1}λ(x)` for
every `f: x→y`. Since `q` is surjective (★), choose any lift `μ(x) ∈ \mathrm{Aut}\,G` with
`q(μ(x)) = λ(x)` at each object `x`. Define `α̃(f) := μ(y)\,α(f)\,μ(x)^{-1}`. Then

> `q(α̃(f)) = λ(y)\,ρ(f)\,λ(x)^{-1} = λ(y)\,\big(λ(y)^{-1}λ(x)\big)\,λ(x)^{-1} = e,`

so `α̃(f) ∈ \ker q = \mathrm{Inn}(G)` for every `f`. And `α̃` is a cocycle (gauge transforms of
cocycles are cocycles: `α̃(gf) = μ(z)α(g)α(f)μ(x)^{-1} = μ(z)α(g)μ(y)^{-1}·μ(y)α(f)μ(x)^{-1}
= α̃(g)α̃(f)`, with `α̃(\mathrm{id})=e`), cohomologous to `α` via `μ`. ✓ ∎

**This is Giraud stratum 2 specialized to the simplicial site `N(C)`:** the band is the
`\mathrm{Out}`-reduction of the structure cocycle, and it vanishes exactly when the transport is
inner-valued up to coboundary. The proof is elementary and Schreier-style (route (B) register),
reusing only the sequence (★) and the nerve's `H¹` — no gauge-theoretic machinery.

**Finite machine-check (D₄).** For `G=D_4`: `\mathrm{Aut}=D_4` (order 8), `\mathrm{Inn}=(ℤ/2)^2`,
`\mathrm{Out}=ℤ/2` — both inner and outer parts nontrivial, so the lemma has real content. Over
`C=B(ℤ)` (single reversible operation, `\mathrm{Mor}=ℤ`, `α(t)=φ∈\mathrm{Aut}\,D_4`), a transport is
relabel-reducible into `\mathrm{Inn}` iff `φ∈\mathrm{Inn}`, and `[ρ]=[q(φ)]=0` iff `φ∈\mathrm{Inn}`;
the two sides coincide for all `8` automorphisms `φ` (`scratch/clause_a_D4_check.py`:
`clause(a) equivalence holds for all phi: True`). ∎

### 2.1 Corollary: the full obstruction, and 10-08 becomes unconditional on its stratum

> **Corollary (a′).** A **strict global inventory** (a global trivialization making all transports
> strictly composable identities) exists **iff** both strata vanish:
> **(i) `β = 0`** (band trivial, by (a)) **and (ii) `[𝔤] = 0 ∈ H²(N(C); Z(G))`** (the 10-08 secondary
> class, well-defined once (i) holds). The obstruction is genuinely **staged**: `[𝔤]` is only defined
> after `β=0` (otherwise the stratum-3 coefficients are `β`-twisted). Thus the 10-08 Thm A is exactly
> the **band-trivial stratum** of the full obstruction, now identified as such, and (a) supplies the
> prior stratum it had hypothesized away.

*Proof.* A strict global inventory is a relabeling `μ: \mathrm{Ob}\,C → \mathrm{Aut}\,G` trivializing
`α` outright (`μ·α ≡ e`). Projecting by `q`, it trivializes `ρ`, forcing `β=0`; so (i) is necessary.
Given (i), by (a) choose `α` inner-valued, i.e. `α = \mathrm{conj}∘\barρ` for a functor
`\barρ: C → B(\mathrm{Inn}\,G)`; then the gerbe is the gerbe of lifts of `\barρ` through
`G → \mathrm{Inn}\,G` in (★), which by 10-08 Thm A (Face 2) is neutral iff `[𝔤]=0`. So (i)∧(ii) is
necessary and sufficient. ∎

---

## 3. Clause (b): fungible stock is doubly vacuous

Let `F` be a **bare** `n`-element set of indistinguishable lots, so `G = \mathrm{Aut}(F) = S_n`.

> **Theorem (b).** For all `n ≥ 3` with `n ≠ 6`, generic fungible inventory carries **neither** a band
> obstruction **nor** a tier-2 class:
> - **(band)** `\mathrm{Out}(S_n) = 1`, hence `H¹(N(C); \mathrm{Out}\,S_n) = \{*\}` and `β = 0`
>   automatically — *for every* `C` and every weld.
> - **(tier-2)** `Z(S_n) = 1`, hence `H²(N(C); Z(S_n)) = 0` and `[𝔤] = 0` (this is 10-08 Prop D).
>
> There are exactly **two low-order exceptions, and they are disjoint**:
> - **`n = 6`** is the lone **band** exception: `\mathrm{Out}(S_6) = ℤ/2`, so a transport using the
>   exotic outer automorphism can have `β ≠ 0` — but `Z(S_6)=1` still kills tier-2.
> - **`n = 2`** is the lone **tier-2** exception: `S_2 = ℤ/2`, `Z = ℤ/2 ≠ 1`, so `[𝔤]` can be nonzero
>   (the 10-08 minimal `B(ℤ/2)` witness) — but `\mathrm{Out}(S_2)=1` keeps the band trivial.
>
> **No single fungible fibre exhibits both obstructions.**

*Proof.* `\mathrm{Out}(S_n)`: `S_n` is a *complete* group (centreless with all automorphisms inner,
so `\mathrm{Out}=1`) for every `n` except `n=2` (`S_2=ℤ/2` abelian, `\mathrm{Aut}=1`, `\mathrm{Out}=1`
anyway) and `n=6`, where `|\mathrm{Out}(S_6)|=2` (Rotman, Thms 7.5–7.7). `Z(S_n)=1` for `n≥3`,
`=ℤ/2` for `n=2`, `=1` for `n≤1` (standard). Feed these into (a) and 10-08 Prop D (Lemma 1 there:
tier-2 coefficients are `Z(\mathrm{Aut}\,F)`). The two exceptional values `n∈\{2,6\}` are distinct and
each triggers only one stratum, as tabulated. ∎

**Machine-check** (`scratch/band_boundary_verify.py`): `Z(S_n)` for `n=1..7` is
`1,2,1,1,1,1,1` (nonvacuous only at `n=2`); `|\mathrm{Aut}(S_n)| = n!` for `n=3,4,5` (so
`\mathrm{Out}=1`), confirmed by exhaustive automorphism enumeration over Coxeter-generator images.
The `n=6` exception (`\mathrm{Out}(S_6)=ℤ/2`) is confirmed by an **explicit** outer automorphism
(§3.1).

**Sharp applications boundary.** The nonabelian inventory phenomenon is **invisible to fungibility**:
`≥3` interchangeable units create no degree-2 relabelling obstruction (`S_n` centreless) and no band
obstruction (`S_n` complete), *except* the isolated `S_6` curiosity. Both nontrivial tiers require
**gauge/torsor-structured stock** — a fibre whose automorphism group has nontrivial centre (tier-2)
or nontrivial outer group (band). This is the economically meaningful regime: allocation defined up
to a gauge group `K` (`\mathrm{Aut}\,F = K` acting by translation, `Z=Z(K)`, `\mathrm{Out}` measuring
how the process twists the gauge), not plain interchangeability.

### 3.1 The `S_6` band exception, explicitly

`S_6` is the unique symmetric group with an outer automorphism. It sends a transposition (cycle type
`2,1^4`) to a product of three disjoint transpositions (cycle type `2^3`) — a map that **cannot** be a
conjugation, since conjugation preserves cycle type. Concretely it arises from the exotic transitive
embedding `S_5 \hookrightarrow S_6` (the action of `S_5` on its six Sylow-5-subgroups): the two
`S_5`-conjugacy classes of such subgroups are swapped by the outer automorphism.

**Explicit witness** (`scratch/out_s6.py`, machine-verified). `S_5` acts by conjugation on its six
Sylow-5-subgroups, giving a *transitive* embedding `ψ: S_5 ↪ S_6` (image `H`, `|H|=120`, transitive —
so `H` is not a point-stabilizer). `S_6` acting on the six cosets `S_6/H` yields an automorphism `Φ`
with, on the standard generators,
`Φ(0\,1\,2\,3\,4\,5) = [1,4,2,5,0,3]` and `Φ(0\,1) = (0\,1)(2\,5)(3\,4)`. Confirmed:
`Φ` is a homomorphism (checked on generators + random pairs) and a bijection (`|image|=720`), and it
sends **every** transposition (cycle type `2\,1^4`) to a product of three disjoint transpositions
(cycle type `2^3`); since conjugation preserves cycle type, `Φ` is **not inner**. Contrast
(`scratch/aut_s6.py`, `aut_center.py`): exhaustive generator-image search gives `|\mathrm{Aut}(S_5)|
=120=|S_5|` (so `\mathrm{Out}(S_5)=1`) and `|\mathrm{Aut}(S_6)|=1440=2·720` (so
`\mathrm{Out}(S_6)=ℤ/2`). Thus for `n=6` a weld
whose transport applies this automorphism along some operation realizes `β ≠ 0` while `[𝔤]=0`
(`Z(S_6)=1`): a band obstruction with no tier-2 shadow. The honest point: this is a *curiosity*, not
an applications driver — the real nonabelian content needs structured stock, which §4 witnesses
abstractly.

---

## 4. Clause (c): a minimal nontrivial-band witness, with clean tier separation

> **Theorem (c).** There is a supply-chain datum `(C, G, α)` with band `β ≠ 0`. Take
> `G = (ℤ/p)^2` (abelian gauge group of stock), `C = B(ℤ)` (a single reversible/cyclic operation —
> the "weld loop"), and `α(t) := A` for a chosen `A ∈ \mathrm{Aut}(G)` with `A ≠ I`. Then
> `β = [ρ] = [A] ≠ 0 ∈ H¹(N(C); \mathrm{Out}\,G)`. Moreover the tiers **separate cleanly**: the band
> is the **sole and nonzero** obstruction, while the tier-2 class is forced to **zero**.

*Construction and proof.*

**The groups.** For abelian `G`, conjugation is trivial, so `\mathrm{Inn}(G)=1` and
`\mathrm{Out}(G)=\mathrm{Aut}(G)`. For `G=(ℤ/p)^2`, `\mathrm{Aut}(G)=\mathrm{GL}_2(𝔽_p)`. Hence
`q = \mathrm{id}` and **the band sees the entire transport**: `ρ = α`. (This is the opposite extreme
from the inner-valued 10-08 regime — here *every* nonidentity transport is non-inner.)

**The base.** `N(B(ℤ)) ≃ S^1`. A cocycle `ρ: B(ℤ) → B(\mathrm{Out}\,G)` is determined by the single
value `ρ(t) = A ∈ \mathrm{Out}\,G` (`ℤ` is free: `t` maps freely). Object-relabeling by
`λ(*) = g ∈ \mathrm{Out}\,G` sends `A ↦ gAg^{-1}`. Hence

> `H¹(N(B(ℤ)); \mathrm{Out}\,G) = \{\text{conjugacy classes of } \mathrm{Out}\,G\},`

and `[ρ] = 0` iff `A` is conjugate to `e`, iff `A = I`.

**The witness.** Choose any `A ≠ I`; then `β = [A] ≠ 0`. Concretely for `p = 2`,
`\mathrm{GL}_2(𝔽_2) ≅ S_3` (order 6, three conjugacy classes `\{I\}, \{3\text{ involutions}\},
\{2\text{ order-3}\}`); take the transvection `A = \begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}`
(order 2) — `[A] ≠ [I]`, confirmed by `scratch/band_boundary_verify.py` (`|class(I)|=1`, `[A]≠[I]`).
For `p = 3`, `\mathrm{GL}_2(𝔽_3)` has order 48 and 8 classes; same conclusion. **`β ≠ 0`.** ∎

**Clean tier separation.** On `C = B(ℤ)`, `N(C) ≃ S^1` is 1-dimensional, so `H²(N(C); Z(G)) = 0` for
*any* coefficients: the tier-2 class is **always zero** here, no matter how rich `Z(G)=G=(ℤ/p)^2` is.
Thus the band `β ≠ 0` is the **unique** obstruction, and it is genuinely nonabelian-flavoured — it
lives in `H¹` with coefficients `\mathrm{Out}\,G = \mathrm{GL}_2(𝔽_p)` (nonabelian for `p ≥ 2`),
*prior to* and *independent of* any `H²` story. This is the promised separation: for abelian `G` the
band captures the **entire** transport while `Z(G)=G` would host a tier-2 story only on a base with
`H² ≠ 0`.

**Interpretation.** Stock is defined up to a `(ℤ/p)^2`-gauge (e.g. two independent mod-`p` ledger
offsets). A cyclic refurbishment process `t` relabels the gauge by a fixed `\mathrm{GL}_2(𝔽_p)`
element `A`. If `A ≠ I`, no global choice of gauge is consistent around the loop — and this failure is
a **band** obstruction (an outer twist of the structure group), strictly prior to the degree-2
"how-many-units" gerbe class. Fungibility (`S_n`) can never produce it (§3); gauge-structured stock
does, minimally.

### 4.1 Both tiers simultaneously active (remark)

To activate band **and** tier-2 at once one needs a base with `H² ≠ 0` and a nontrivial outer
transport. Minimal sketch: `C = B(ℤ^2)` (`N(C) ≃ T^2`, so `H²(T^2; A) = A ≠ 0`) with `G=(ℤ/p)^2`,
`ρ` sending the two generators to commuting `A, B ∈ \mathrm{GL}_2(𝔽_p)` not both `I` (band `≠0`),
while the stratum-3 centre cocycle on the 2-cell carries a nonzero `β`-twisted `H²(T^2;(ℤ/p)^2)`
class. Working this out (the twisted differential `d_2` coupling band to centre) is the natural
stratum-2↔3 interaction follow-up; **not** attempted here — it is the Giraud twisted-`H²` torsor, out
of scope per the honesty guard. Recorded as a gap (§7).

---

## 5. What this does to the 10-08 theorem

- The 10-08 "**scope hypothesis (band trivial)**" is now a **precise, checkable condition**:
  `β = [q∘α] = 0 ∈ H¹(N(C); \mathrm{Out}\,\mathrm{Aut}\,F)`, criterion (a).
- The 10-08 **Thm A** ("strict global inventory ⟺ `[𝔤]=0`") is the **band-trivial stratum** of the
  full staged obstruction (Cor a′): the complete statement is `β=0` **and** `[𝔤]=0`.
- For **fungible** stock the hypothesis is **automatic** for all `n≥3, n≠6` (band vacuous) and the
  tier-2 class is also vacuous — so the entire two-tier phenomenon is a feature of
  **gauge/torsor-structured** stock, not of fungibility (b). The hedge, for the applications pillar,
  becomes a *theorem*: *fungible ⟹ band trivial; nontriviality needs richer `G`.*
- The band is a **new, prior, genuinely nonabelian** invariant of the inventory gerbe, nonvacuous in
  general (c), and complementary to `Z(\mathrm{Aut}\,F)` (band needs `\mathrm{Out} ≠ 1`; tier-2 needs
  `Z ≠ 1`).

---

## 6. Verification summary

- `scratch/band_boundary_verify.py`: `Z(S_n)` table `n=1..7`; `|\mathrm{Aut}(S_n)|=n!` for `n=3,4,5`
  (`\mathrm{Out}=1`); `\mathrm{GL}_2(𝔽_p)` conjugacy classes for `p=2,3` with `[A]≠[I]` for `A≠I`;
  `H²(S^1;-)=0`.
- `scratch/clause_a_D4_check.py`: clause (a) equivalence verified for all 8 automorphisms of `D_4`
  (`Inn=(ℤ/2)^2`, `Out=ℤ/2`) — the genuinely nonabelian test case.
- `scratch/out_s6.py`, `aut_s6.py`, `aut_center.py`: explicit `S_6` outer automorphism `Φ`
  (transitive `S_5↪S_6` coset action), machine-confirmed homomorphism ∧ bijection ∧ transposition
  `↦` cycle type `2^3` (hence outer); exhaustive counts `|\mathrm{Aut}(S_5)|=120` (`\mathrm{Out}=1`),
  `|\mathrm{Aut}(S_6)|=1440` (`\mathrm{Out}=ℤ/2`); `Z(S_n)` table `n=2..7`.

---

## 7. Scope and gaps (honest)

- **Clause (c)** witnesses `β ≠ 0`; it does **not** classify nontrivial-band gerbes. Classifying
  `K`-banded gerbes (the torsor over twisted `H²(N(C);Z(G))_K`) is Giraud's full nonabelian machinery
  — out of scope by design (honesty guard, PROVE.md pt 5).
- **Stratum 2 ↔ 3 coupling** (§4.1): the twisted differential coupling band `β` to the centre class
  on a base with `H² ≠ 0` (a `d_2`/`k`-invariant) is not computed. Natural next PROVE/LEAN target: a
  bar-complex oracle on `T^2 = N(B(ℤ^2))` with `G=(ℤ/p)^2` and a chosen commuting outer pair.
- The economic **torsor-fibre** worked example (gauge-valued allocation, `\mathrm{Aut}\,F = K` acting
  on itself, band measuring process-induced gauge twist) deserves a standalone applications write-up.

## 8. Bottom line

The inventory gerbe's obstruction is **staged**, matching Giraud exactly over `N(C)`:
**(2) band `β = [q∘α] ∈ H¹(N(C); \mathrm{Out}\,\mathrm{Aut}\,F)` must vanish first** — this happens
iff the transport is inner-valued up to an outer relabeling (a) — **then (3) the 10-08 class
`[𝔤] ∈ H²(N(C); Z(\mathrm{Aut}\,F))` must vanish** (Cor a′). Fungible stock sees *neither* stratum for
all `n ≥ 3, n ≠ 6`, with `n=6` the lone (band-only) and `n=2` the lone (tier-2-only) exceptions —
disjoint (b). And the band is nonvacuous in general: a single `(ℤ/p)^2`-gauge loop with transport
`A ≠ I` has `β = [A] ≠ 0` while its tier-2 class is forced to zero (c) — the first genuinely
**nonabelian** content of the supply-chain program, prior to and cleanly separated from the abelian
`H²` story.
</content>
</invoke>
