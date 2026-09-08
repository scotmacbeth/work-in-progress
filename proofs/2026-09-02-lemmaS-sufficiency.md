# The external distributive law is sufficient for `◁`-admissibility; and on the extensive pole it is EQUIVALENT to `π₀`-multiplicativity

### PRIMARY TARGET of `state/PROVE.md` resolved: Lemma S (external form) *is* sufficient — with the exact scope pinned

**MacBeth — 2026-09-02 (PROVE session).**
Predecessors (all `proved`): `proofs/2026-09-01-gap1-setxvec-proved.md` (Prop 6.1 absorptive
characterization; the two-source analysis); `proofs/2026-08-30-admissibility-and-the-connectedness-converse.md`
(Theorem B, Lemma S *necessity*, Theorem D); `proofs/2026-08-31-gluing-inadmissible-pi0.md`
(Lemma S ⟺ `π₀`-multiplicativity over an extensive CCC; `Gl((−)²)` inadmissible with connected unit).
Companion code: `scratch/verify_distributive.py` (FinSet brute force, both formulas natural isos,
0 failures). Registry: `proofs/registry/left-adjoint-over-vec.json`, node `conj-absorptive-dichotomy`
(this file resolves the *tractable* sub-question, promotes a new node `lemmaS-sufficiency` to `proved`).

---

## EXECUTIVE SUMMARY

The `PROVE.md` primary target asked: **is Lemma S sufficient for admissibility?** The answer turns
on a distinction the target already flagged — *external* vs *internal* distributivity — and is:

**YES, the EXTERNAL distributive law (D) is sufficient (Theorem 1), and on the extensive
cartesian-closed pole it is moreover EQUIVALENT to Lemma S in its weak (copower) form, hence to
`π₀`-multiplicativity (Theorem 2). Consequently, on that pole,**

> **`Fam(C^op)` is `◁`-admissible ⟺ `π₀` preserves finite products.**

This is a *complete* characterization of admissibility on the extensive pole, and it **unifies the
two obstructions** the census had listed as distinct mechanisms (`Set×Set`: "disconnected unit";
`Gl((−)²)`: "`π₀` non-multiplicative") into the single criterion of `π₀`-multiplicativity.

**Why this is not a triviality (the tension I had to respect).** `Gl((−)²)` is a *topos* — extensive
cartesian closed — yet **inadmissible** (predecessor). The *internal* (Gambino–Kock) distributive
law holds in **every** topos, so it CANNOT be what admissibility needs. Admissibility is governed by
the **external** law: shape ranges over the hom-**set** `C(P,T·1_C)` and the positions decompose `P`
by an **external** coproduct. External = internal **iff** the shape object `[P,T·1_C]` is a copower
of `1_C` (a discrete object) — exactly Lemma S. In `Gl`, `[K,2·1_C] = 2·1_C ⊔ K` carries a stray
bald edge, so external ⊋ internal, (D) fails, inadmissible. The sufficiency proof lives precisely in
that gap, exactly as `PROVE.md` predicted.

**Scope, stated honestly.** This resolves the RIGID/extensive half — the "tractable half first" the
target named. The FLEXIBLE pole (`Vec_fd`; non-cartesian, `1_C≅0_C`) is admissible by a *different*
sufficient condition (every object copower-tiny). The full absorptive **dichotomy** (Conj 6.2 — that
rigid + flexible + their tensors exhaust absorptivity) is **not** settled here; §5 states precisely
what remains.

---

## 0. Setting and the two forms of Lemma S

`C` closed symmetric monoidal, cocomplete, locally small. `[−,−]` internal hom, `⊗` tensor, `I` unit,
`0_C` initial, `1_C` terminal. For a set `T`, the copower `T·A := ∐_{t∈T} A`. `Fam(C^op)`: objects
`p=(S,(P_s)_{s∈S})`; extension `⟦p⟧(X)=∐_{s∈S}[P_s,X]`. **`Fam(C^op)` is `◁`-admissible** iff it is
closed under `◁`, iff (Prop 6.1, predecessor `proved`) **every object `P∈C` is absorptive**:
`X ↦ [P,⟦q⟧(X)]` lies in the image of `⟦−⟧` (is an *extension*) for every `q∈Fam(C^op)`.

**Definition (extensive-preimage decomposition).** In an infinitary-extensive category, a map
`c: P → T·1_C` induces `P ≅ ∐_{t∈T} P^c_t`, where `P^c_t` is the pullback of `c` along the `t`-th
coproduct injection `1_C → T·1_C`. (Coproducts in an extensive category are disjoint and universal;
this is the content of `C/(∐_t A_t) ≃ ∏_t C/A_t`.)

**Lemma S — weak form (S-weak).** For every `P` and every set `T`, `[P, T·1_C]` is a copower of
`1_C`. *(Equivalently — predecessor `2026-08-31` Cor 3.2, over an extensive CCC — `π₀ ⊣ (−)·1_C`
preserves finite products.)*

**Lemma S — external distributive law (D).** For every `P`, every set `T`, every family
`(Y_t)_{t∈T}`, the canonical comparison
> `κ : ∐_{c ∈ C(P,\,T·1_C)} ∏_{t∈T} [P^c_t, Y_t] \xrightarrow{\ ≅\ } [P, ∐_{t∈T} Y_t]`,   natural in `(Y_t)`,

is an isomorphism. (Well-posed once the `P^c_t` exist, e.g. `C` extensive.) `κ` sends, on the `c`-th
summand, a tuple `(g_t: P^c_t → Y_t)_t` to the map `P ≅ ∐_t P^c_t \xrightarrow{∐ g_t} ∐_t Y_t`.

**(D) ⟹ (S-weak)** is immediate (put `Y_t=1_C`: `[P,T·1_C] ≅ ∐_c ∏_t 1_C = C(P,T·1_C)·1_C`). The
substance is the reverse and the sufficiency.

---

## 1. Theorem 1 — the external distributive law is sufficient for admissibility

**Theorem 1.** Let `C` be an **infinitary-extensive closed symmetric monoidal** cocomplete category
satisfying **(D)**. Then every object of `C` is absorptive; hence `Fam(C^op)` is `◁`-admissible.

*Proof.* Fix `P∈C` and `q=(T,(Q_t)_{t∈T})∈Fam(C^op)`. Put `Y_t := [Q_t, X]`, functorial in `X`.
Then, naturally in `X`:
```
[P, ⟦q⟧X] = [P, ∐_{t∈T} [Q_t,X]]
          ≅ ∐_{c ∈ C(P,T·1_C)} ∏_{t∈T} [P^c_t, [Q_t,X]]        (D), natural in (Y_t) hence in X
          ≅ ∐_{c}              ∏_{t∈T} [P^c_t ⊗ Q_t, X]          tensor–hom [A,[B,X]]≅[A⊗B,X], nat. in X
          ≅ ∐_{c}              [∐_{t∈T} (P^c_t ⊗ Q_t), X].        [−,X] sends ∐ to ∏, nat. in X
```
Define `r := (S_r, (R_c)_{c∈S_r})` with `S_r := C(P, T·1_C)` and `R_c := ∐_{t∈T} (P^c_t ⊗ Q_t)`.
`S_r` is a set (local smallness); each `R_c ∈ C` (cocomplete + `⊗`); nothing depends on `X`. The
display is a natural isomorphism `[P, ⟦q⟧(−)] ≅ ⟦r⟧`. Thus `X ↦ [P,⟦q⟧X]` is an extension: `P` is
absorptive.

`P, q` arbitrary ⟹ every object absorptive ⟹ (Prop 6.1) `Fam(C^op)` is `◁`-admissible. ∎

**Remark (the composite `◁`).** For general `p=(S,(P_s))`, running the above per `s`,
`⟦p⟧⟦q⟧X = ∐_s [P_s,⟦q⟧X] ≅ ∐_s ⟦r_s⟧X = ⟦∐_s r_s⟧X`. So `p◁q = ∐_s r_s`, with total shape
`∐_{s∈S} C(P_s, T·1_C)`. This *constructs* the container `◁` explicitly from (D).

**Each step is a theorem, not a hope.** Tensor–hom is the closed structure; `∏_t[Z_t,X]≅[∐_t Z_t,X]`
is the universal property of the coproduct; both natural in `X`. Only (D) is a hypothesis. There is
no gap. (FinSet instance of the whole display: `scratch/verify_distributive.py` Task 2 — 200 random
cardinality checks + 50 naturality-square checks, **0 failures**.)

---

## 2. Theorem 2 — on the extensive CCC pole, (D) ⟺ Lemma S (weak)

Now add cartesian closure: `⊗ = ×`, `I = 1_C` terminal, `[P,−] ⊣ (−)×P`. So `C` is an
**infinitary-extensive cartesian closed** category (every Grothendieck topos qualifies).

I use three consequences of infinitary extensivity + CCC, all standard:
- **(U) Universality.** A map `W → ∐_{i∈I} B_i` is *the same data* as a decomposition
  `W ≅ ∐_{i∈I} W_i` together with maps `(W_i → B_i)_i`; hence
  `C(W, ∐_i B_i) ≅ ∐_{\{W≅∐_i W_i\}} ∏_i C(W_i, B_i)`. *(Definition of extensivity; NB this FAILS in
  additive categories — a map into `⊕` need not split the source — which is why the flexible pole is
  outside Theorem 2.)*
- **(P) Partitions.** Specializing `B_i = 1_C`: `C(W, I·1_C) ≅ \{` `I`-indexed decompositions
  `W ≅ ∐_{i∈I} W_i` `\}` (maps into a copower of the terminal = clopen `I`-partitions of `W`).
- **(Dist) Distributivity.** `(−)×P` is a left adjoint, so preserves `∐`: `W × ∐_i B_i ≅ ∐_i(W×B_i)`.

**Theorem 2.** For `C` infinitary-extensive cartesian closed: **(D) ⟺ (S-weak).**

*Proof.* (⟹) is §0. For (⟸), assume `[P,T·1_C] ≅ E·1_C`, `E := C(P,T·1_C)`, for all `P,T`. Fix
`P,T,(Y_t)`. I show `[P,∐_t Y_t] ≅ ∐_{c∈E} ∏_t [P^c_t,Y_t]` by comparing representables `C(X,−)`,
naturally in `X`.

*The right-hand side.* With `W_c := ∏_{t}[P^c_t,Y_t]`:
```
C(X, ∐_{c∈E} W_c) ≅ ∐_{φ:\,X≅∐_{c∈E} X_c} ∏_{c∈E} C(X_c, W_c)              (U), E-decomps of X
                  = ∐_{φ}              ∏_{c∈E} ∏_{t∈T} C(X_c, [P^c_t, Y_t])
                  = ∐_{φ}              ∏_{c∈E} ∏_{t∈T} C(X_c × P^c_t, Y_t).  CCC adjunction
```

*The left-hand side.*
```
C(X, [P, ∐_t Y_t]) ≅ C(X × P, ∐_t Y_t)                                     CCC
                   ≅ ∐_{ψ:\,X×P ≅ ∐_t Z_t} ∏_{t} C(Z_t, Y_t).             (U), T-decomps of X×P
```

*The shape indices biject: `\{ψ\} ≅ \{φ\}`.*
```
\{X×P ≅ ∐_t Z_t\} = C(X×P, T·1_C)          (P)
                  ≅ C(X, [P,T·1_C])         CCC
                  = C(X, E·1_C)             S-weak
                  = \{X ≅ ∐_{c∈E} X_c\}.    (P)
```
a natural bijection `ψ ↔ φ`.

*The fibres match under `ψ↔φ`.* Trace the decomposition `ψ` that `φ` names. The map
`X×P → T·1_C` corresponding to `φ` restricts, on `X_c × P` (`c∈E=C(P,T·1_C)`), to
`X_c×P \xrightarrow{pr} P \xrightarrow{c} T·1_C` (constant in the `X_c` coordinate, because `φ|_{X_c}`
hits precisely the `c`-summand of `E·1_C`). Since `c` decomposes `P ≅ ∐_t P^c_t`, (Dist) gives
`X_c×P ≅ ∐_t (X_c×P^c_t)`, so this map decomposes `X_c×P` as `∐_t X_c×P^c_t`. Summing over `c` and
using `X = ∐_c X_c`:
```
X×P ≅ ∐_{c∈E}(X_c×P) ≅ ∐_{c}∐_{t}(X_c×P^c_t) ≅ ∐_{t}( ∐_{c∈E} X_c×P^c_t ),   so  Z_t = ∐_{c∈E} X_c × P^c_t.
```
Therefore
```
∏_{t} C(Z_t, Y_t) = ∏_t C(∐_c X_c×P^c_t, Y_t) = ∏_t ∏_{c∈E} C(X_c×P^c_t, Y_t) = ∏_{c∈E}∏_t C(X_c×P^c_t, Y_t),
```
the last two by "hom out of `∐` = `∏`" and reindexing. This is exactly the RHS fibre over `φ=ψ`.

Hence both sides equal `∐_{φ:X≅∐_{c∈E}X_c} ∏_{c∈E}∏_{t∈T} C(X_c×P^c_t, Y_t)`, naturally in `X` and
`(Y_t)`. By Yoneda `[P,∐_t Y_t] ≅ ∐_{c∈E}∏_t[P^c_t,Y_t]`, which is (D). ∎

**The one load-bearing use of S-weak.** It is the single step `C(X,[P,T·1_C]) = C(X, E·1_C)` turning
the internal shape *object* `[P,T·1_C]` into an external *partition* of `X` indexed by the *set* `E`.
Without it the shape stays internal (the topos always has the *internal* law) and the coproduct
`∐_{c∈E}` on the right cannot be formed over a set. This is exactly the internal/external seam, and
exactly what `Gl` violates. (FinSet, where `π₀=Id` and S-weak is trivial, confirms (D) is a genuine
natural bijection — Task 1, 200 instances, forward map = extensive tagging, full round-trip, 0
failures.)

---

## 3. The characterization, and the unification of obstructions

Assemble: Prop 6.1 (`Adm ⟺ every object absorptive`, proved), Lemma S *necessity*
(`Adm ⟹ S-weak`, predecessor `2026-08-30` §2, proved — re-derived self-containedly in the footnote¹),
Theorem 2 (`S-weak ⟹ (D)`), Theorem 1 (`(D) ⟹ Adm`).

**Corollary 3.1 (extensive-pole characterization).** For `C` an infinitary-extensive cartesian
closed category,
> `Fam(C^op)` is `◁`-admissible ⟺ (S-weak) ⟺ [when `π₀ ⊣ (−)·1_C` exists] `π₀` preserves finite products.

**Corollary 3.2 (the two obstructions are one).** On the extensive pole, `π₀`-multiplicativity is the
*single* criterion. The census had two rows with two "mechanisms":

| base | extensive CCC | admissible | prior "mechanism" | via Cor 3.1 |
|---|---|---|---|---|
| `Set`, connected topos, FinSet | ✓ | **yes** | — | `π₀` mult (`π₀=Id`) |
| `Set × Set` | ✓ | no | disconnected unit | `π₀` **non-mult** |
| `Gl((−)²)` | ✓ | no | `π₀` non-mult (Weichsel) | `π₀` **non-mult** |

For `Set×Set`: `π₀ =` (left adjoint to the diagonal `T↦(T,T)`) `= (X_1,X_2)↦X_1⊔X_2`, and
`π₀((X_1,X_2)×(Y_1,Y_2)) = X_1Y_1 ⊔ X_2Y_2 ≠ (X_1⊔X_2)×(Y_1⊔Y_2) = π₀(X)×π₀(Y)`. So the
"disconnected unit" obstruction **is** `π₀`-non-multiplicativity; there was never a second mechanism
on the extensive pole. (And `π₀`-mult ⟹ connected unit follows from Cor 3.1 + Theorem B; the
converse fails — `Gl` — so connected-unit is *strictly weaker* than admissibility, as the predecessor
found.)

¹ *Self-contained necessity.* If `P` is absorptive, take `q=(T,(0_C)_t)`; `⟦q⟧X = ∐_t[0_C,X] =
∐_t 1_C = T·1_C`, constant in `X`. So `X↦[P,T·1_C]=∐_s[R_s,X]` is a *constant* extension, forcing
each `[R_s,X]≅1_C` for all `X`, i.e. `R_s≅0_C` (in an extensive CCC, `[R,X]≅1 ∀X` ⟹ `W×R≅0 ∀W` ⟹
`R≅0`). Hence `[P,T·1_C]=∐_s 1_C`, a copower of `1_C`. ∎

---

## 4. Verification ledger

| script / source | checks | result |
|---|---|---|
| `scratch/verify_distributive.py` Task 1 | (D) as a **bijection** in FinSet: forward = extensive tagging `c(p)=` summand of `g(p)`; image = RHS, injective, both round-trips id; 200 instances (`|P|,|T|,|Y_t|≤4`) | **0** card. mism., **0** bij. failures |
| `scratch/verify_distributive.py` Task 2 | admissibility formula `[P,⟦q⟧X]≅∐_c[∐_t P^c_t×Q_t,X]`: cardinality (200) + **naturality square** in `X` on every element (50) | **0** mism., **0** iso/nat. failures |
| predecessor `2026-08-31` | `Gl`: `π₀(K×K)=2≠1` (Weichsel), `[K,2·1_C]=2·1_C⊔K` not a copower ⟹ (D) fails ⟹ inadmissible | consistent with Cor 3.1 (`⟸` contrapositive) |
| this file §3 | `Set×Set`: `π₀` non-mult computed by hand | consistent |

FinSet realizes the *positive* side of Cor 3.1 (S-weak holds ⟹ (D) holds ⟹ admissible); `Gl` realizes
the *negative* side (S-weak fails ⟹ (D) fails ⟹ inadmissible). Together they bracket Theorem 2.

---

## 5. What is proved, and the gaps that remain (precise)

**Proved this session.**
- **Theorem 1** (extensive closed-monoidal + (D) ⟹ admissible). `proved`.
- **Theorem 2** ((D) ⟺ S-weak on extensive CCC). `proved`.
- **Corollary 3.1** (admissible ⟺ `π₀`-multiplicative on the extensive pole). `proved`.
- **Corollary 3.2** (the "disconnected unit" and "`π₀` non-mult" obstructions coincide). `proved`.

**Answer to the PRIMARY TARGET.** *Yes* — the external Lemma S (D) is sufficient (Theorem 1); on the
extensive pole it is equivalent to the weak/copower Lemma S and to `π₀`-multiplicativity (Theorem 2),
which therefore *characterizes* admissibility there. The gap the target located ("external vs internal
distributivity") is where the proof lives (§2, the load-bearing step).

**Correction to a predecessor overreach.** The gluing file's Corollary 5.1 wrote that this "answers
Gap 2 (is Lemma S sufficient?) in the strong negative direction: *not only can 'Lemma S + extensivity'
fail to give admissibility* — Lemma S itself can fail on a connected-unit extensive base." The second
half (Lemma S *can fail*, witnessed by `Gl`) is correct and proved. **The first, parenthetical clause
is an overreach and is now shown FALSE:** on the extensive CCC pole, Lemma S (weak) *does* give
admissibility (Theorem 2 + Theorem 1). There is no base where Lemma S holds yet admissibility fails on
this pole — `Gl` is not such a base (it *fails* Lemma S, `π₀(K×K)=2`). What Gap 2 actually resolves to
is the clean *equivalence* of Corollary 3.1, not a negative. (The registry node
`connected-not-sufficient-for-admissible` states only the correct half — "Lemma S itself fails on a
connected-unit extensive base" — so only the prose parenthetical needs the fix; recorded here.)

**Gaps / scope, honestly.**
1. **Flexible pole not covered.** Theorem 2 needs extensivity (property (U) fails in additive `C`).
   `Vec_fd` is admissible via *copower-tiny*, a genuinely different sufficient condition; there is no
   `π₀` there (`1_C≅0`). Theorem 1 does not apply either (its (D) presupposes `1_C`-copowers with
   content). So "sufficiency of Lemma S" is a statement about the **rigid** pole only.
2. **The absorptive dichotomy (Conj 6.2) is NOT settled.** I have shown each pole's mechanism is
   *sufficient* for its objects' absorptivity; I have **not** shown these two are the *only* sources,
   nor that a mixed base decomposes. In particular Theorem 1 gives a *clean sufficient* condition for
   the rigid contribution but says nothing about an object that is absorptive by a *mixed* mechanism
   on a base that is neither extensive nor additive-fg — the exact locus (predecessor Gap 1: additive
   non-fg; or `γ`-non-injective non-additive) where an irreducible inhabitant could still hide.
3. **`π₀`-mult ⟹ connected unit** is obtained only *through* Theorem B (via Cor 3.1). A direct
   diagram proof would give an independent, sharper route to Theorem B on the extensive pole — a
   worthwhile follow-up, not attempted.

---

## 6. Grant framing

The predecessor's design slogan was: *a compositional substitution calculus needs its resource base's
connected components to be multiplicative under pairing.* This session upgrades that from a **necessary
warning** to a **complete design test on the cartesian side**:

> For a cartesian (extensive, cartesian-closed) resource base, the external plug-in calculus `◁`
> **exists if and only if** the connected-components functor `π₀` preserves finite products — a single,
> decidable condition (`π₀(X×Y) ≅ π₀X × π₀Y`), which simultaneously rules out product-of-worlds bases
> (`Set×Set`) and tensor-connectivity bases (graphs, `Gl`). No separate "connected unit" check is
> needed: it is subsumed.

For the AI-Mathematician grant this is the extensive-pole endpoint of the `◁`-admissibility programme:
a *characterization*, not just bounds, with the two poles (rigid `= π₀`-multiplicative; flexible `=`
all-copower-tiny) now each carrying a clean sufficient criterion, and the residual open problem
(irreducible mixed inhabitant / Conj 6.2) sharply isolated to the non-extensive-non-additive-fg locus.
