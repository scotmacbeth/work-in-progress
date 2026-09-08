# Artin gluing `Gl((−)²)` is `◁`-INADMISSIBLE — connectedness is not sufficient
### The Gap-1 candidate I owned is (a) extensive, not Gap-1 at all, and (b) inadmissible; the obstruction is Weichsel's theorem on the graph tensor product

**MacBeth — 2026-08-31 (PROVE session).**
Target of the session (`state/PROVE.md`): test `◁`-admissibility of the Artin gluing
`Gl(T) = (Set ↓ T)`, `T = (−)²`, the one Gap-1 probe I already owned
(`proofs/2026-08-26-copowers-gap-writer-monad.md` §4v). Predecessor for the machinery:
`proofs/2026-08-30-admissibility-and-the-connectedness-converse.md` (**Lemma S**, Theorems A/B/D).
Companion code: `scratch/2026-08-31-gluing-admissibility-lemmaS.py`,
`scratch/2026-08-31-gluing-extensivity.py`, `scratch/2026-08-31-gluing-exp-construct.py` — all green.

---

## EXECUTIVE SUMMARY

**Verdict.** `Gl((−)²)` is **`◁`-inadmissible**. It is therefore **not** a witness that Theorem B is
non-sharp — the hope recorded in `PROVE.md`. But the *reason* is new and sharper than the hoped-for
outcome, and it corrects a recorded misclassification.

**Three results.**

**(1) `Gl((−)²)` is an (infinitary lextensive) topos — the "non-extensive" label was an error.**
`T = (−)²` is right adjoint to `2×(−)`, hence preserves *all* limits; Artin gluing of a lex functor
between toposes is a topos (MacLane–Moerdijk A2.1). So `Gl((−)²)` is a Grothendieck topos:
cartesian closed, cocomplete, **infinitary extensive**. The parenthetical "non-extensive" in
`2026-08-26` §4v is false; its `(A)∧(C)` computation stands and is in fact an instance of that
file's own Theorem 3.1. **Consequence: `Gl((−)²)` is not in Gap 1 (it has `⊗ = ×` and *is*
extensive). Gap 1 remains empty of known inhabitants.** (§1, verified: disjointness + universality
on 377 random diagrams, `gluing-extensivity.py`.)

**(2) On this base, admissibility reduces to a multiplicativity that FAILS.** Objects of `Gl((−)²)`
are **graphs** (`B` = vertices, `A` = directed edges, `β : A → B²` = endpoints); the categorical
product is the **tensor (Kronecker) product of graphs**; the terminal `1_C` is a single looped
vertex; the copower `T·1_C = (T,T,\mathrm{diag})`. The components functor
`π₀ ⊣ (−)·1_C` sends a graph to its set of connected components. I prove (Prop 3.1):

> Over a cocomplete cartesian-closed base with a components functor `π₀ ⊣ (−)·1_C` preserving the
> terminal object, **Lemma S holds ⟺ `π₀` preserves finite products**; and `T = 2` already detects
> failure.

**(3) `π₀` is not multiplicative — Weichsel's theorem — so `Gl((−)²)` fails Lemma S.** The tensor
product of two connected **bipartite** graphs has **two** components (Weichsel 1962). Take
`K :=` the edge `•—•` (`π₀ K = 1`, bipartite). Then `π₀(K×K) = 2 ≠ 1 = π₀K·π₀K`. Concretely the
internal hom is **computed explicitly**:

> `[K,\ 2·1_C]\ ≅\ 2·1_C\ ⊔\ K` — two looped vertices (`2` points) **plus a bald edge**.

That stray edge-component carries no point, so `[K,2·1_C]` is **not** a copower of `1_C`; Lemma S
(necessary for admissibility, `proved`) fails at `P = K`, `T = 2`. **Hence `Fam(Gl((−)²)^op)` is not
closed under `◁`.** (§4, Theorem G, verified three independent ways.)

**The corollary that matters most (§5).**

> **Connectedness of the unit is necessary but NOT sufficient for `◁`-admissibility.**

`Gl((−)²)` has a **connected** unit (its *points* functor `C(I,−) = β^{-1}(Δ)` preserves coproducts —
the `2026-08-26` `(A)∧(C)` result) yet is **inadmissible**. This is the first base separating the two
conditions, and it does so on the *extensive pole*, where Theorem B gives `admissible ⟹ connected`.
So the extensive pole splits:

| base | extensive | unit connected | Lemma S | `◁`-admissible | obstruction |
|---|---|---|---|---|---|
| `Set`, connected topos | ✓ | ✓ | ✓ | **yes** | — |
| `Set×Set` | ✓ | ✗ (Thm B) | ✗ | **no** | disconnected unit |
| **`Gl((−)²)`** | ✓ | **✓** | **✗** | **no** | **`π₀` not multiplicative (Weichsel)** |
| `Set_*` | ✗ | ✗ | — | **no** (Thm A) | polynomial degree `a=−4` |

`Gl((−)²)` is the **third inadmissible base**, and the only one that is admissible-obstructed with a
*connected unit*. The mechanism — the components functor failing to preserve products — is disjoint
from the two already on the table (disconnected unit; polynomial degree).

---

## 0. Setup: `Gl(T)` is a category of graphs

`Gl(T) := (Set ↓ T)` for `T = (−)² : Set → Set`. Objects `(A,B,β)` with `A,B ∈ Set` and
`β : A → B² = B×B`. A morphism `(A,B,β) → (A',B',β')` is a pair `(f:A→A',\ g:B→B')` with
`β'∘f = (g×g)∘β`, i.e. `β'(f(a)) = (g(β(a)_0),\ g(β(a)_1))` for all `a`.

**Read this as graphs.** `B` is a vertex set, each `a∈A` is a *directed edge* with endpoints
`β(a) = (β(a)_0,β(a)_1)`, and a morphism is a graph homomorphism `(g` on vertices, `f` on edges,
compatibly`)`. The undirected/connectivity structure is what `π₀` below sees.

**Structure (all standard for a comma category `(Id ↓ T)` with `T` lex; verified in code).**
- **Terminal** `1_C = (1,1,\,!)` — one vertex with a loop. It is the `×`-unit `I` (CCC).
- **Products** are componentwise: `(A,B,β)×(A',B',β') = (A×A',\ B×B',\ β×β')`, using `T` lex so
  `T(B×B') ≅ TB×TB'`. As graphs this is the **tensor (categorical/Kronecker) product**: vertex set
  `B×B'`, an edge `(a,a')` for each pair of edges, joining `(β(a)_0,β'(a')_0)—(β(a)_1,β'(a')_1)`.
- **Coproducts** are componentwise: `(A⊔A',\ B⊔B',\ [β,β'])` — disjoint union of graphs.
- **Copower of the terminal** `T·1_C = ∐_{t∈T} 1_C = (T,T,\mathrm{diag})` — `T` looped vertices,
  one per `t`.
- **Points** `C(I,X) = C(1_C,(A,B,β)) = β^{-1}(Δ_B) = \{a : β(a)_0 = β(a)_1\}` — the *loops*.
- `[0_C,X] ≅ 1_C` and `[Q,1_C] ≅ 1_C` (predecessor Lemma 1.0).

---

## 1. `Gl((−)²)` is a topos, hence extensive (correcting `2026-08-26` §4v)

**Proposition 1.1.** `Gl((−)²)` is a Grothendieck topos; in particular it is cartesian closed,
cocomplete, and **infinitary lextensive**.

*Proof.* `T = (−)² = \mathrm{Set}(2,−)` is right adjoint to `2×(−)` (since
`\mathrm{Set}(2×X,Y) = \mathrm{Set}(X,Y²)`), hence preserves all limits; it is finitary, hence
accessible. Artin gluing of an accessible left-exact functor between Grothendieck toposes is a
Grothendieck topos (MacLane–Moerdijk, *Sheaves in Geometry and Logic*, A2.1.12; Carboni–Johnstone,
"Connected limits, familial representability and Artin glueing", TAC 1995). Every Grothendieck topos
is infinitary extensive. ∎ *(`peer-reviewed` for the gluing theorem; `computed` sanity check below.)*

**Verification (`gluing-extensivity.py`).** Coproduct injections disjoint (pullback `= 0_C`): `0`
failures in `200` random pairs. Universality (`Z ≅ h^*X ⊔ h^*Y` for `h:Z→X⊔Y`): `0` count-mismatches
in `377` random diagrams. Consistent with extensivity.

**Correction.** The claim in `2026-08-26` §4v that `Gl((−)²)` is "non-extensive because
`T(B⊔B') ≠ TB⊔TB'`" conflates *`T` not preserving coproducts* with *`Gl(T)` not being extensive*.
The latter is false. The file's actual computation there — that `Gl((−)²)` satisfies `(A)` and `(C)`,
i.e. its unit is connected — is correct and is subsumed by that same file's Theorem 3.1 (extensive
⟹ `(A)⟺(C)`). **The correction changes nothing downstream except the classification of this base:
it belongs to the extensive pole.**

---

## 2. Two functors on `Gl((−)²)` that must not be confused

The base carries two `Set`-valued functors, and the whole point is that they come apart.

- **Points** `U = C(I,−) : X ↦ β^{-1}(Δ_B)` (the loops). This preserves coproducts (loops do not
  cross components), so **the unit is connected** — the `2026-08-26` `(A)∧(C)` result.
- **Components** `π₀ : X ↦ B/⟨\text{edge relation}⟩`, the connected components of the graph. It is
  **left adjoint** to `(−)·1_C : \mathrm{Set} → Gl`, `T ↦ (T,T,\mathrm{diag})`:

**Lemma 2.1.** `Hom_{Gl}(X,\ T·1_C) = \mathrm{Set}(π₀X,\ T) = T^{π₀X}`, naturally in `X` and `T`.

*Proof.* A morphism `X = (A,B,β) → (T,T,\mathrm{diag})` is `(f:A→T,\ g:B→T)` with
`(f(a),f(a)) = (g(β(a)_0),\ g(β(a)_1))`, i.e. `f(a) = g(β(a)_0) = g(β(a)_1)`. So the data is exactly a
`g:B→T` that is **constant on every edge** (coequalizes the edge relation), i.e. a map
`π₀X = B/⟨\text{edges}⟩ → T`, with `f` then determined. ∎ *(`proved`; `Hom(X,2·1_C)=2^{π₀X}`
verified for `X ∈ \{1_C,K,\vec K,K×K,K⊔K\}` in `gluing-admissibility-lemmaS.py`.)*

`U` preserves **coproducts** (⟹ connected unit); `π₀` is what Lemma S will interrogate for
preservation of **products**. Different functor, different (co)limit. **This is the crux of why
connectedness and admissibility separate here.**

---

## 3. The reduction: Lemma S ⟺ `π₀` preserves finite products

**Lemma S** (predecessor §2, `proved`, *necessary* for admissibility). If `C` is `◁`-admissible then
for every `P∈C` and every small `T`, the internal hom `[P,\ T·1_C]` is a copower of `1_C`.

**Proposition 3.1.** Let `C` be cocomplete cartesian closed with a components functor
`π₀ ⊣ (−)·1_C`. Consider the statement `S(P,T)`: "`[P,T·1_C]` is a copower of `1_C`".
1. If `π₀` preserves the binary product `(−)×P`, then `S(P,T)` holds for all `T`, with
   `[P,T·1_C] ≅ (T^{π₀P})·1_C`.
2. Conversely, if `π₀` preserves the terminal object and `S(P,T)` holds for all `T`, then the
   canonical comparison `π₀(X×P) → π₀X × π₀P` is a bijection for all `X` (`π₀` preserves `(−)×P`).
   `T = 2` alone suffices to detect failure.

*Proof.* `[P,T·1_C]` represents `X ↦ Hom(X×P,\ T·1_C) = \mathrm{Set}(π₀(X×P),\ T)` (exponential
adjunction + Lemma 2.1).
(1) If `π₀(X×P) ≅ π₀X×π₀P` canonically, this is
`\mathrm{Set}(π₀X×π₀P,T) = \mathrm{Set}(π₀X,\ T^{π₀P}) = Hom(X,\ (T^{π₀P})·1_C)`, so by Yoneda
`[P,T·1_C] ≅ (T^{π₀P})·1_C`, a copower of `1_C`.
(2) Suppose `[P,T·1_C] ≅ E·1_C`. Evaluate the representable at `X=1_C`: using `1_C×P ≅ P` and
`π₀(1_C) ≅ 1`, `E = Hom(1_C,\ [P,T·1_C]) = \mathrm{Set}(π₀P,T) = T^{π₀P}`. So
`\mathrm{Set}(π₀(X×P),T) ≅ \mathrm{Set}(π₀X×π₀P,\ T)` naturally in `X`, for every `T`. Since `2` is a
cogenerator of `Set`, a natural iso of `\mathrm{Set}(−,2)`-values along the canonical comparison
forces that comparison to be a bijection. ∎ *(`proved`.)*

**Corollary 3.2.** For `Gl((−)²)` (where `π₀(1_C) = 1`), **Lemma S ⟺ `π₀` preserves finite products.**

This is precisely the "teeth" the predecessor predicted for Lemma S between the `Set` and `Vec`
degeneracies: over `Set` every object is discrete (`π₀ = \mathrm{Id}`, trivially multiplicative,
Lemma S vacuous); over `Gl` the components functor is genuine and multiplicativity is a real,
falsifiable demand.

---

## 4. The refutation: Weichsel's theorem kills multiplicativity

**Weichsel's theorem** (1962). The tensor product `G×H` of two connected graphs is connected iff at
least one of `G,H` is non-bipartite; if both are connected and bipartite, `G×H` has exactly **two**
components.

Let `K` be the single undirected edge: `B = \{0,1\}`, `A = \{e_1,e_2\}`, `β(e_1)=(0,1)`,
`β(e_2)=(1,0)`. `K` is connected and bipartite, `π₀K = 1`.

**Theorem G.** `Gl((−)²)` is not `◁`-admissible. Explicitly, Lemma S fails at `P = K`, `T = 2`.

*Proof.* By Weichsel (both factors connected bipartite), `π₀(K×K) = 2`. By Prop 3.1(1)'s forced
value, if `[K,2·1_C]` were a copower of `1_C` it would be `(2^{π₀K})·1_C = 2·1_C`, with
`Hom(K,2·1_C) = \mathrm{Set}(π₀K,2) = 2`. But
`Hom(K,\ [K,2·1_C]) = Hom(K×K,\ 2·1_C) = \mathrm{Set}(π₀(K×K),\ 2) = 2^2 = 4 ≠ 2`. So
`[K,2·1_C] ≇ 2·1_C`; as `X=1_C` forces the copower rank to be `2`, `[K,2·1_C]` is a copower of `1_C`
for no rank. Lemma S fails, and by its contrapositive `Gl((−)²)` is not `◁`-admissible. ∎

**The obstruction, made fully explicit (`gluing-exp-construct.py`).** Searching all finite
`Gl`-objects with `|B| ≤ 4`, `|A| ≤ 4` for one whose representable matches `X ↦ Hom(X×K,2·1_C)` on a
discriminating six-object family returns a unique iso class, and it is

> `[K,\ 2·1_C]\ ≅\ 2·1_C\ ⊔\ K`  —  vertices `\{0,1,2,3\}`, loops at `0,1`, edge `2—3`.

Two looped vertices give the `2` points (`= E` forced); the extra **bald edge** `\{2,3\}` is a
component with **no loop**, i.e. a `π₀`-component carrying no point. A copower `E·1_C` is "all
diagonal" — every component is a looped point — so the bald edge is exactly the summand obstructing
Lemma S. It is the image, under `[K,−]`, of the diagonal-avoiding second component of `K×K` that
Weichsel produces. *(Match verified on `9` further test objects; failure persists at `T=3`: `9≠3`.)*

**Why the polynomial calculus breaks here, structurally.** `⟦(\{∗\},K)⟧⟦(2,(0_C,0_C))⟧ = [K,\,2·1_C]`
is a single "monomial-with-external-shape" `X↦X^{K}` composed with the constant `2·1_C`; the composite
is `2·1_C ⊔ K`, which needs shape set of size `3` *but with one shape whose position object `K` is
not `1_C`* — so it is genuinely a `Fam(Gl^op)` object, yet it is **not** the copower of `1_C` that
`⟦p◁q⟧(1_C)` would force. Internal (Gambino–Kock) polynomials in the topos `Gl` *are* closed under
composition; the **external-shape** functors `∐_{s∈S}X^{P_s}` of `Fam(Gl^op)` are not. Theorem G is
exactly the gap between external and internal shape, localized to a base where it bites.

---

## 5. Corollaries

**Corollary 5.1 (connected ⟹̸ admissible).** The unit of `Gl((−)²)` is connected (§2) but the base is
inadmissible (Theorem G). So **unit-connectedness is necessary (Theorem B, extensive pole) but not
sufficient for `◁`-admissibility.** `Gl((−)²)` is the first base exhibiting the separation, and it
does so *on the extensive pole itself*. This answers the predecessor's Gap 2 ("is Lemma S
sufficient?") in the strong negative direction: not only can "Lemma S + extensivity" fail to give
admissibility — **Lemma S itself can fail on a connected-unit extensive base.**

**Corollary 5.2 (Gap 1 correction, the session's stated target).** The `PROVE.md` premise that
`Gl((−)²)` is a *non-extensive* Gap-1 candidate is refuted: it is an extensive topos (Prop 1.1), so
it lives on the extensive pole, not in Gap 1. And it is inadmissible (Theorem G), so it is **not** a
witness that Theorem B is non-sharp. **Registry node `open-middle-region` stays `speculative`/open:
this candidate is disqualified, but no proof that Gap 1 is empty is obtained — only that its one
named probe is not in it.**

**Corollary 5.3 (third inadmissible base; trichotomy table enriched).** With `Set×Set` (disconnected
unit) and `Set_*` (polynomial degree), `Gl((−)²)` is the **third** inadmissible base, via a **third**
mechanism — non-multiplicativity of the components functor. The extensive pole is therefore not a
uniform "admissible" region: it splits into `{Set, connected toposes with π₀ multiplicative}`
(admissible) and `{Set×Set, Gl((−)²)}` (inadmissible), the split being exactly whether `π₀`
preserves products (Cor 3.2). Theorem B's implication `admissible ⟹ connected` is intact and
one-directional; its converse `connected ⟹ admissible` is **false**, witnessed here.

---

## 6. Verification ledger

| script | checks | result |
|---|---|---|
| `gluing-admissibility-lemmaS.py` | `π₀(K×K)=2≠1`; `Hom(X,2·1_C)=2^{π₀X}` (5 objs); Lemma S test `4≠2`; no rank `E` works on 4-obj family | all green |
| `gluing-extensivity.py` | disjointness (200 diagrams), universality (377 diagrams) | 0 failures |
| `gluing-exp-construct.py` | explicit `[K,2·1_C]≅2·1_C⊔K` (unique iso class, `|B|≤4`); it is not `(E,E,diag)` | confirmed |
| `/tmp/confirm.py` | `[K,2·1_C]≅2·1_C⊔K` on 9 objs; failure at `T=3` (`9≠3`) | confirmed |

All `computed`. The topos/extensivity input to Prop 1.1 is `peer-reviewed` (Carboni–Johnstone;
MacLane–Moerdijk). Lemma S, Theorem B, Lemma 1.0 are `proved` (cited, predecessor).

---

## 7. Gaps, precisely stated

1. **Gap 1 is disqualified-of-this-candidate, not proved empty.** I have shown the *one* probe I
   owned is not in Gap 1 (it is extensive) and is inadmissible anyway. Whether a genuinely
   non-extensive, non-collapse, `◁`-admissible base exists is **still open**. The `2026-08-26` census
   ruling out `Vec/R-Mod/CMon/Set_*/Rel/quantales` via `(A)` remains the state of the art.
2. **Prop 3.1(2) uses `π₀(1_C) ≅ 1`** (π₀ preserves the terminal). This holds for `Gl((−)²)`
   (`π₀(1_C)=1`, computed) so Cor 3.2 is unconditional there; the *general* iff needs that mild
   hypothesis, stated explicitly. The `⟸` direction (positive criterion) is hypothesis-free.
3. **Task (3) of `PROVE.md` — idempotent splitting / dropping cartesianness from Theorem B — not
   attempted.** Orthogonal to this result; the step `I_i⊗I_j ≅ 0` off the cartesian case is
   recorded as an untested lead. (Note: product categories `C₁×C₂` give `I_i⊗I_j=0` for free; a
   separator needs a *non-extensive* unit splitting, which I did not construct.)
4. **Novelty.** Weichsel's theorem is classical (H. Weichsel, "The Kronecker product of graphs",
   Proc. AMS 13 (1962) 47–52). The **application** — that container `◁`-admissibility of the
   Artin-gluing base `Gl((−)²)` is controlled by, and defeated by, graph-tensor connectivity — is
   mine (`computed`+`proved` this session). The reduction Prop 3.1 (Lemma S ⟺ `π₀`-multiplicativity)
   is mine. The `Gl` extensivity correction is a bookkeeping fix to my own `2026-08-26` file.
   Not gated against the literature beyond the gluing theorem; flag before any external claim.

---

## 8. Grant framing

The predecessor said substitution of processes lives "only at two extremes — set-like or linear."
This session sharpens the set-like side: **being set-like enough for a connected unit is not enough.**
The resource base must have a components functor that is *multiplicative* — it must not create
components under pairing. `Gl((−)²)` is the cautionary base: a perfectly good cartesian-closed topos,
connected unit, where pairing two connected resources can *disconnect* them (Weichsel), and precisely
there the plug-in calculus `◁` does not exist. For a design principle:

> A compositional substitution calculus needs its resource base's **connected-components** to be
> multiplicative under pairing. A base where two connected resources can combine into a disconnected
> one — a "tensor-like" rather than "cartesian-like" notion of joint resource — admits no external
> substitution operation, even when it is a topos with a connected unit.

This is predictive and checkable: it tells a system designer to test `π₀(X×Y) =? π₀X×π₀Y` on the
intended resource category *before* attempting to build a composition operator.
