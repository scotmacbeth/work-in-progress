# The emergent-holonomy count is cohomological — and it lives in degree 0

**MacBeth — PROVE session, 2026-08-20 (deep-work).**
Proves the Mackey/Eckmann–Shapiro/Nakaoka decomposition (★) for `Ext` between permutation
modules, identifies its degree-0 part with the emergent-holonomy meeting count
`h(s) = |A\U/B|` of `2026-08-13-emergent-holonomy-meeting-points.md`, and — the sharp,
slightly counter-intuitive payoff — shows that in the emergent-holonomy setting the **entire
higher `Ext` tower vanishes identically**, so the holonomy invariant is cohomological *but
concentrated in `Ext⁰`*. This resolves the Rick collaboration: his `Ext²`/higher-class bet
was structurally void, and now we can say exactly why.

> **One line.** `Extⁿ_{kG}(k[G/A],k[G/B]) ≅ ⊕_{g∈A\G/B} Hⁿ(A∩gBg⁻¹;k)`. In degree 0 this is
> the double-coset count `|A\G/B|`; specialised to `U=Stab_G(s)` with `A,B` the factor
> isotropies of an exact factorisation, **every** intersection `A∩uBu⁻¹` is trivial (Lemma 1),
> so `Ext⁰ = h(s)` and `Ext^{≥1} = 0`. The emergent holonomy is the *rank of `Ext⁰`*, not a
> higher class.

---

## 0. Setup and conventions

`G` a finite group; `A, B ≤ G` subgroups; `k` a field of characteristic `p` (interesting case
`p | |G|`). All modules are **left** modules. Write
```
    Ind_H^G W = kG ⊗_{kH} W,     Res_H Y = Y viewed over kH,     M = k[G/A] = Ind_A^G k,   N = k[G/B] = Ind_B^G k.
```
`k[G/H]` is the permutation module on the left cosets `G/H`; as a `kG`-module it is
`Ind_H^G k`. For `H ≤ G` write `Hⁿ(H;k) = Ext^n_{kH}(k,k)` (group cohomology, trivial
coefficients). For `g ∈ G` write `^gB = gBg⁻¹`.

We freely use three classical facts, each stated with its one-line justification; the
references are Benson, *Representations and Cohomology I* (§2.8 Eckmann–Shapiro, §3.3 Mackey)
and Brown, *Cohomology of Groups* III.5–III.6. **(★) itself is classical (Nakaoka 1960s).**
The contribution of this note is §3–§4: the holonomy dictionary and the degree-0 concentration.

---

## 1. The three classical ingredients

### (I) Eckmann–Shapiro
For `H ≤ G`, any `kH`-module `W`, any `kG`-module `Y`:
```
    Ext^n_{kG}(Ind_H^G W, Y) ≅ Ext^n_{kH}(W, Res_H Y),      n ≥ 0.     (Shapiro)
```
*Justification.* `kG` is free as a right `kH`-module (`G = ⊔_i g_i H` gives
`kG = ⊕_i g_i·kH`), so `Ind_H^G = kG⊗_{kH}(-)` is exact; and it sends free `kH`-modules to
free `kG`-modules (`Ind_H^G kH = kG`), hence preserves projectives. `Ind_H^G ⊣ Res_H` with
counit/unit the usual Frobenius maps. Thus for a projective resolution `P_• → W` over `kH`,
`Ind P_• → Ind W` is a projective resolution over `kG`, and the adjunction gives a natural
isomorphism of complexes `Hom_{kG}(Ind P_•, Y) ≅ Hom_{kH}(P_•, Res_H Y)`; take cohomology. ∎

Specialising `H=A`, `W=k`, `Y=N`:
```
    Ext^n_{kG}(k[G/A], N) ≅ Ext^n_{kA}(k, Res_A N) = Hⁿ(A; Res_A N).      (I·)
```

### (II) Mackey decomposition
As `kA`-modules,
```
    Res_A^G Ind_B^G k ≅ ⊕_{g ∈ A\G/B} Ind_{A∩^gB}^A k,      (Mackey)
```
the sum over a set of representatives `g` of the double cosets `A\G/B`.
*Justification.* `G = ⊔_{AgB} AgB` and `AgB ≅ A ×_{A∩^gB} gB` as `(A,B)`-sets, so the
permutation `A`-set `Res_A(G/B) = ⊔_{g} A/(A∩^gB)`; linearise. (General Mackey has a twist
`Res(^g W)`; for `W=k` trivial the twist is trivial.) ∎

Because `Hⁿ(A;−)` commutes with finite direct sums of coefficient modules, (I·) and (II) give
```
    Ext^n_{kG}(k[G/A], k[G/B]) ≅ ⊕_{g ∈ A\G/B} Hⁿ(A; Ind_{A∩^gB}^A k).      (I·II)
```

### (III) Shapiro for cohomology (coinduction form)
For `H ≤ A`: `Hⁿ(A; Ind_H^A k) ≅ Hⁿ(H; k)`.
*Justification.* For finite index `Ind_H^A ≅ Coind_H^A` (both `= k[A/H]` as the underlying
space, canonically isomorphic when `[A:H]<∞`). `Coind_H^A` is *right* adjoint to `Res_H`, and
`Res_H` is exact and preserves projectives (`kA` is free over `kH`), so the derived adjunction
gives `Ext^n_{kA}(k, Coind_H^A k) ≅ Ext^n_{kH}(Res_H k, k) = Ext^n_{kH}(k,k) = Hⁿ(H;k)`.
Hence `Hⁿ(A; Ind_H^A k) = Ext^n_{kA}(k, Ind_H^A k) ≅ Hⁿ(H;k)`. ∎

### The theorem
Substituting (III) into (I·II):

> **Theorem 1 (★).** For a finite group `G`, subgroups `A,B ≤ G`, and any field `k`,
> ```
>     Extⁿ_{kG}(k[G/A], k[G/B]) ≅ ⊕_{g ∈ A\G/B} Hⁿ(A ∩ gBg⁻¹; k),      n ≥ 0,
> ```
> naturally in `n`, the sum over any set of representatives of the double cosets `A\G/B`.
> (Different representatives of one double coset give conjugate — hence cohomologically
> isomorphic — intersection subgroups, so the right side is well defined.) ∎

**Status: proved-as-assembled.** Every step is a cited classical lemma; the assembly is the
Mackey formula for `Ext` of permutation modules (Nakaoka; Benson I §3). Verified numerically
on 17 cases (§2). The *novel* content is §3–§4.

---

## 2. Computational verification (guardrail — done FIRST)

Engine `scratch/ext-mackey-general/` (own exact `F_p` linear algebra; no CAS). It computes
each side **independently**: the left side by a genuine minimal free resolution of `k[G/A]`
over `kG` followed by `H^n Hom_{kG}(F_•, k[G/B])`; the right side by Mackey double cosets with
each `H^*(A∩gBg⁻¹;k)` obtained from its own `kH`-resolution. **All 17 cases agree**, and
`dim Ext⁰ = |A\G/B|` in every case (this also pins the Mackey convention `A∩gBg⁻¹`, not
`gAg⁻¹∩B`).

| case | `p` | LHS = RHS `Ext^{0..}` | note |
|---|---|---|---|
| `V₄, A=⟨a⟩,B=⟨b⟩` | 2 | `[1,0,0,0]` | transverse, 1 dcoset |
| `V₄, A=B=⟨a⟩` | 2 | `[2,2,2,2]` | 2 dcosets, both `∩=ℤ/2` |
| `S₃, A=B=⟨(12)⟩` | 2 | `[2,1,1,1]` | **mixed tower** (`∩ = ℤ/2` and `{e}`) |
| `A₄, A=B=V₄` | 2 | `[3,6,9,12]` | 3 dcosets, each `∩=V₄`, `Hⁿ(V₄)=n+1` |
| `D₄, A=B=⟨refl⟩` | 2 | `[3,2,2,2]` | non-abelian 2-group |
| `D₄, A=B=Z(D₄)` | 2 | `[4,4,4,4]` | central, 4 dcosets |
| `S₄, A=B=⟨(12)⟩` | 2 | `[7,2,2,2]` | 7 dcosets |
| `ℤ/3, A=B=G` | 3 | `[1,1,1,1]` | odd `p`, periodic |
| `ℤ/3, A=B={e}` | 3 | `[3,0,0,0]` | regular |
| **holonomy W1** `S₃=A₃·⟨(12)⟩, U=⟨(23)⟩, A=B={e}` | 2 | `[2,0,0,0]` | `Ext⁰=h=2` |
| **holonomy W2** `S₄=A₄·⟨(12)⟩, U=S₃, A=A₃, B={e}` | 2 | `[2,0,0,0]` | `h=2>1`, tower `≡0` |

(Plus 6 further cases in `driver.py`/`driver2.py`.) The `A₄`/`V₄` row is the strongest single
check: the direct `kG` resolution has Betti numbers `[1,2,3,4,5]` and independently reproduces
the elementary-abelian tower `[3,6,9,12]`.

---

## 3. The dictionary: `h(s) = dim Ext⁰`

Recall the emergent-holonomy setup (`2026-08-13-emergent-holonomy-meeting-points.md`): an exact
factorisation `G = P·P'` (a Zappa–Szép product, `P∩P'={e}`, `|P||P'|=|G|`) acts on a set `S`;
fix `s∈S` and set
```
    U := Stab_G(s),   A := Stab_P(s) = U∩P,   B := Stab_{P'}(s) = U∩P'.
```
Theorem 6 / Corollary 7 there prove `h(s) := |A\U/B| = |U|/(|A||B|) = |(P·s)∩(P'·s)|`, the
number of crossing points of the two factor orbits, with `h(s)=1 ⟺` alignment.

Apply **Theorem 1 with `G` replaced by `U`** (a finite group; `A,B ≤ U`). In degree 0,
`H⁰(H;k) = k` for every `H`, so:

> **Corollary 2 (degree 0 = the meeting count).**
> ```
>     dim_k Ext⁰_{kU}(k[U/A], k[U/B]) = dim_k Hom_{kU}(k[U/A],k[U/B]) = |A\U/B| = h(s).
> ```
> The double-coset invariant Rick wanted `Ext` to see **is** `Ext` — in degree 0.

*Proof.* By Theorem 1 over `U`, `Ext⁰ = ⊕_{u∈A\U/B} H⁰(A∩uBu⁻¹;k) = ⊕_{u∈A\U/B} k`, of
dimension `|A\U/B|`. The middle equality is `Ext⁰ = Hom`; the last is Corollary 7. ∎

Directly: `Hom_{kU}(k[U/A],N) = (Res_A N)^A = k^{A\U/B}` (the `A`-fixed points of the
permutation module `k[U/B]` are spanned by the `A`-orbit sums on `U/B`, i.e. the double
cosets) — the same count, no resolution needed.

---

## 4. The higher tower vanishes in the holonomy setting — so holonomy is a degree-0 invariant

Here is the payoff, and it corrects the initial framing ("the higher tower detects
alignment").

> **Lemma 3 (exact-factorisation transversality; = Lemma 1 of the meeting-points proof).**
> For an exact factorisation `G=P·P'` and every `g∈G`, `P ∩ gP'g⁻¹ = {e}`.

*(3-line proof reproduced there; uses only `P∩P'={e}` and unique factorisation `g=pp'`.)*

> **Theorem 4 (holonomy is concentrated in degree 0).** In the emergent-holonomy setting
> (`A=U∩P ⊆ P`, `B=U∩P' ⊆ P'`), **for every `u∈U`** the intersection `A∩uBu⁻¹` is trivial.
> Consequently, over `U`,
> ```
>     Extⁿ_{kU}(k[U/A], k[U/B]) ≅ ⊕_{u∈A\U/B} Hⁿ({e};k) = { k^{h(s)}  (n=0),   0  (n≥1). }
> ```
> The emergent-holonomy invariant `h(s)` is the rank of `Ext⁰`; the entire higher `Ext`
> tower is identically zero, independently of `p` and of alignment.

*Proof.* `A ⊆ P` and `uBu⁻¹ ⊆ uP'u⁻¹`, so `A∩uBu⁻¹ ⊆ P∩uP'u⁻¹ = {e}` by Lemma 3 (applicable
since `u∈U⊆G`). Then every Mackey summand in Theorem 1 (over `U`) is `Hⁿ({e};k) = [n=0]·k`.
Sum over the `h(s)` double cosets. ∎

**Reading — and the honest correction.**
- The holonomy count is **cohomological**, but it is a *degree-0 rank*, `h(s) = dim Ext⁰`, not
  a higher cohomology class. There is no `[ω]∈H²` shadow of `h` in this `Ext`-tower, and no
  higher class at all: the tower is `[h,0,0,0,…]`.
- Alignment is read off degree 0: aligned `⟺ h(s)=1 ⟺ Ext⁰` is **1-dimensional**. Misaligned
  `⟺ h(s)>1 ⟺ Ext⁰` has rank `>1`. Computation **W2** exhibits `h=2>1` (misaligned) with the
  higher tower still `≡0` — so the higher tower demonstrably does *not* detect alignment. The
  entire alignment content is the rank of `Ext⁰`.
- **This is exactly why Rick's `Ext²`-shifted-class bet was structurally doomed** (see memory
  `rick-v4-ext-vanishes-transverse`, `scratch/rick-v4-ext2/`): in any exact-factorisation
  holonomy setting Lemma 3 forces `Res_A N` free over `kA`, killing `Ext^{≥1}` — there is no
  `Ext²` for a class to live in. His hypothesis was right in degree 0 (`h = dim Ext⁰`) and
  void in every higher degree.

**Where the higher tower *does* live.** For **general** `A,B ≤ G` *not* drawn from an exact
factorisation, `Ext^{≥1}` can be nonzero: Theorem 1 gives it as `⊕_g H^{≥1}(A∩gBg⁻¹;k)`,
supported on the double cosets with `p | |A∩gBg⁻¹|` (if `p∤|H|`, Maschke ⟹ `H^{≥1}(H;k)=0`).
The `S₃` (`[2,1,1,1]`), `D₄`, `A₄` (`[3,6,9,12]`), `S₄` rows of §2 are exactly these surviving
towers. But that is a **different phenomenon** — `p`-divisible subgroup *overlap* between two
arbitrary subgroups — not emergent holonomy, which by Lemma 3 always sits in the transverse
locus. The two must not be conflated.

> **Corollary 5 (twist-stability).** For any 1-dimensional `kG`-module (character) `L`,
> `Extⁿ_{kG}(k[G/A], k[G/B]⊗L) ≅ ⊕_{g} Hⁿ(A∩gBg⁻¹; Res_{A∩gBg⁻¹} L)`. In the holonomy setting
> every `A∩uBu⁻¹={e}`, so `Res L = k` and the tower is **unchanged** by any twist. (Over `F₂`
> there is no nontrivial character at all: `F₂*={1}`.) This is why Rick's orientation-line
> twist is a no-op.

*Proof.* Mackey with coefficients: `Res_A(N⊗L) = ⊕_g Ind_{A∩^gB}^A Res_{A∩^gB}(^g L)`, then
Shapiro; `^gL=L` since `L` is 1-dimensional (`G` acts by a character, invariant under
conjugation). In the holonomy setting each intersection is `{e}` so `Res L` is `k`. ∎

---

## 5. Status ledger (honesty)

**Proved-as-assembled (classical), verified 17 cases:**
- **Theorem 1 (★)** — Mackey/Eckmann–Shapiro decomposition of `Ext` between permutation
  modules. Not novel (Nakaoka 1960s; Benson I §3). Provided in coordinates with each step
  cited. Numerically confirmed both sides agree on 17 groups incl. `A₄, D₄, S₄`, and
  `dim Ext⁰=|A\G/B|` throughout.

**Contribution (the delta):**
- **Corollary 2** — `h(s) = dim Ext⁰_{kU}(k[U/A],k[U/B])`. Combines Theorem 1 (deg 0) with the
  proved meeting-points identity `h=|A\U/B|` (`2026-08-13`, `proved`).
- **Theorem 4** — in the holonomy setting the higher `Ext` tower **vanishes identically**
  (Lemma-3 transversality), so `h` is a degree-0 rank invariant, *not* a higher class. This
  **corrects** the working hypothesis "higher tower detects alignment": witness **W2** shows
  `h>1` with zero higher tower. It also gives the structural reason Rick's higher-class bet
  fails (`rick-v4-ext-vanishes-transverse`).
- **Corollary 5** — twist-stability, with the holonomy case a corollary of Theorem 4.

**Scope / not claimed:**
1. `G` finite throughout (`U=Stab_G(s)` is finite). Theorem 1's iso is natural in `n`; the
   `dim` statements are finite.
2. The *general* higher tower `⊕_g H^{≥1}(A∩gBg⁻¹;k)` (non-holonomy `A,B`) is real and can be
   large (§2), but is a distinct invariant (`p`-divisible overlap), explicitly **not**
   emergent holonomy.
3. No `H²`-class for `h` is claimed or exists in this tower; consistent with
   `two-omega-sites-not-isotropy-restriction` (`proved`) and `rick-v4-ext-vanishes-transverse`
   (`computed`).

**Route.** Per the PROVE guardrail: the mathematics of (★) is entirely classical, so the (★)
write-up is an **`/expository`** deliverable; the *contribution* worth a standalone claim is
the two-line dictionary + degree-0 concentration (Cor 2, Thm 4). Registry node
`emergent-holonomy-is-ext-tower` at `proved` with the classical backbone flagged
`proved-as-assembled` and the delta being the holonomy identification.

**Grant framing.** Emergent holonomy of unprotected orchestration now has a *representation-
theoretic* signature: `h(s) = dim_k Hom_{kU}(k[U/A], k[U/B])`, the rank of the space of
`U`-equivariant maps between the two factor-orbit permutation modules — computable by a single
`Hom` (or double-coset count), with the guarantee (Theorem 4) that no higher `Ext` obstruction
can hide the invariant. Detection is degree 0; there is nothing deeper to audit.
