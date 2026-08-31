# The two [ω] sites are irreducibly distinct: isotropy-restriction refutation and the alignment–splitting collapse

**MacBeth — PROVE session, 2026-08-14 (deep work, one problem).**
Closes gap #3 of `2026-08-12-holonomy-composition-zs-bridge.md` (§4) and the book teachbox
`§sec:emergent-holonomy`. Companion to that bridge (peer-reviewed via Rick, 2026-08-14) and to
`2026-07-20-orchestration-reentrancy-obstruction-analytic.tex` (`[ω]=ε`, proved/Lean).

> **One line.** The handoff class `[ω_h]∈H²_BW(Sk_C;𝒟)` and the stabiliser class
> `[ω_st]∈H²(B;A)` rhyme (both `≅𝔽₂`, same generator `ε`, same ZS bit) but are **not** related by
> the standard isotropy-restriction map: `Sk_C` is automorphism-rigid, so isotropy restriction is
> the **zero map** and kills `[ω_h]` (Part 1). More: the *geometric* stabiliser class is **forced to
> zero** in the only regime where it is even well-typed — aligned + normal ⟹ split (Part 1.5), so the
> `ℤ/4` witness of the bridge is not realised by any internal exact factorisation. And **no** comparison
> functor `F:𝔸(↓_⋈)→Sk_C` can rescue the identification: for every `F`, `i_s*F*[ω_h]=0` (Part 2). The
> two sites are irreducibly distinct; the rhyme is that both are images of the *same* `ε` under two
> **incomparable** structure maps out of category cohomology (off-diagonal/nerve vs isotropy).

---

## 0. The two sites (recalled precisely)

**Site H (handoff).** `Sk_C` = the orbit category of the reentrancy witness
(`2026-07-20-…-analytic.tex`, §4): objects `Sup, Wk, Rt`; non-identity generators
`[p]:Sup→Wk`, `[q]:Sup→Rt`, `[s],[s₂]:Wk⇉Rt`; composites `[s]∗[p]=[q]=[s₂]∗[p]`. The natural
system `𝒟` has `𝒟(Sup)=ℤ/2`, `𝒟(Wk)=𝒟(Rt)=0`, all restriction maps zero. The normalised
Baues–Wirsching complex is `C¹≅(ℤ/2)²` (coords `[p],[q]`), `C²≅(ℤ/2)²` (coords `([s],[p]),([s₂],[p])`),
`C³=0`; `B²=⟨(1,1)⟩` (diagonal), so
```
        H²_BW(Sk_C;𝒟) = (ℤ/2)²/⟨(1,1)⟩ ≅ ℤ/2,   [ω_h] = [(0,ε)],   ε = the token-mutation bit.
```
The generator is supported on the length-2 chain `([s₂],[p])` — a `Sup→Rt` path through **three
distinct objects**.

**Site S (stabiliser).** An internal exact factorisation `G=P·P'` (Zappa–Szép product `Q=P⋈P'`) acts
on `S`; at a state `s` put `E:=Stab_G(s)`, `A:=Stab_P(s)=E∩P`, `B:=Stab_{P'}(s)=E∩P'`. When `A` is
abelian and normal and `s` is *aligned* (`E=A·B`), the bridge §3 reads off an extension
`1→A→E→B→1` and a class `[ω_st]∈H²(B;A)`, with witness `A=B=ℤ/2`: `[ω_st]=0⟺E≅ℤ/2×ℤ/2`,
`[ω_st]=ε⟺E≅ℤ/4`.

Both are `𝔽₂` with generator `ε`, and both come from the *same* ZS-composition data. The temptation
(gap #3) is to declare them one class seen twice. We refute this three ways.

---

## 1. Part 1 — Isotropy restriction is the zero map (naive identification FALSE)

For a small category `𝒞`, a natural system `𝒟`, and an object `x`, the inclusion of the automorphism
group `i_x : B\,Aut_𝒞(x) ↪ 𝒞` induces the **isotropy-restriction** homomorphism
```
        i_x* : H^n_BW(𝒞;𝒟) → H^n(Aut_𝒞(x); 𝒟(x))      (group cohomology),
```
the standard, well-typed bridge between category cohomology and group cohomology (Baues–Wirsching
1985). This is the *only* natural map of the shape the naive identification needs.

**Definition.** `𝒞` is **automorphism-rigid** if `Aut_𝒞(x)={id_x}` for every object `x`.

**Lemma 1.1.** `Sk_C` is automorphism-rigid.
*Proof.* The only endomorphisms of `Sup, Wk, Rt` in `Sk_C` are the identities: the topology
`Sup→Wk⇉Rt` is acyclic and the sole would-be loop, the token `τ`, was pushed into the coefficient
`𝒟(Sup)=ℤ/2`, not into an arrow of `Sk_C`. (Machine-checked: `comp1_bw_isotropy.py` lists no
non-identity endomorphism at any object.) ∎

**Theorem 1.2 (isotropy-blindness).** If `𝒞` is automorphism-rigid then for every `n≥1`, every
natural system `𝒟`, and every object `x`, the map `i_x*` is zero — indeed its codomain is `0`.
Consequently every class in `H^n_BW(𝒞;𝒟)`, whether or not it vanishes, restricts to `0` on every
isotropy group. At the cochain level: for `n=2` the restriction of any 2-cochain to `x` is supported
on chains of endomorphisms of `x`; there are none of length `≥1` besides identities, so the restricted
cochain is identically `0`.
*Proof.* `Aut(x)={id_x}` is the trivial group, and `H^n(1;M)=0` for all `n≥1` and any module `M`.
So `i_x*` has target `0`. The cochain statement is the same fact one categorical level down: the
normalised BW `n`-cochain restricted to `B\,Aut(x)` is a function on `n`-tuples of non-identity
automorphisms of `x`, an empty index set. ∎

**Corollary 1.3 (Part 1, the refutation).** For every object `x∈Sk_C`, `i_x*[ω_h]=0`. Since the
stabiliser class `[ω_st]∈H²(B;A)` is (in its nonzero instance) a *nontrivial* single-group extension
class, and `Sk_C` has **no** object whose automorphism group is the nontrivial `B`, the statement
"`[ω_st]` is the isotropy-restriction of `[ω_h]`" is **false**: the right-hand side is `0` at every
object, and there is no object at which the type `H²(B;A)` with `B` nontrivial even occurs.
*Proof.* Lemma 1.1 + Theorem 1.2. Computationally: `ω_T=(0,ε)` is supported on `([s₂],[p])` and
`([s],[p])`, neither a loop; its restriction to loops at any object is `0`. ∎

This is the exact deliverable of `state/PROVE.md` Part 1, and it is stronger than "kills the
generator": isotropy restriction from `Sk_C` is *structurally* zero, so no BW class on `Sk_C` — the
handoff class or any other — is visible to isotropy. The handoff class lives in the **off-diagonal /
nerve** part of `H²_BW` (chains through distinct objects); the stabiliser class is **pure isotropy**
(a loop class). These are orthogonal, and `i_x*` is exactly the projection onto the part that `Sk_C`
does not have.

---

## 2. Part 1.5 — The alignment–splitting collapse (a scope-correction of bridge §3)

The refutation above is a *site* mismatch. Part 1.5 is sharper and internal to Site S: the geometric
stabiliser class is **identically zero wherever it is well-typed**, so the nonzero `ε`-witness of the
bridge is not realised by the ZS point-stabiliser geometry at all.

Throughout, `G=P·P'` is an internal exact factorisation, `E=Stab_G(s)`, `A=E∩P`, `B=E∩P'`.

**Lemma 2.1 (trivial intersection).** `A∩B=1`.
*Proof.* `A∩B = E∩P∩P' ⊆ P∩P' = {e}`, the defining property of an exact factorisation. ∎

**Lemma 2.2 (aligned + normal ⟹ split).** If `s` is aligned (`E=A·B`) and `A◁E`, then `E=A⋊B` is a
**split** extension of `B` by `A`; hence `[ω_st]=0∈H²(B;A)` — for *every* action of `B` on `A`,
trivial or not.
*Proof.* `B=E∩P'` is a subgroup of `E`. Aligned gives `A·B=E`; Lemma 2.1 gives `A∩B=1`. With `A`
normal, `A·B=E` and `A∩B=1` are exactly the recognition conditions for an internal semidirect product
`E=A⋊B`: `B` is a subgroup complement to `A`, i.e. a group-theoretic section of `E↠E/A≅B`. A section
is precisely a splitting, so the extension class is `0`. ∎

**Lemma 2.3 (the `ℤ/4` witness is geometrically impossible).** There is no internal exact
factorisation with `(A,B,E)≅(ℤ/2,ℤ/2,ℤ/4)`.
*Proof.* Suppose `|A|=|B|=2`. By Lemma 2.1 `A∩B=1`, so `A,B` are **distinct** order-2 subgroups; let
`a,b` be their involutions, `a≠b`. If moreover `E≅ℤ/4`, then `E` has a **unique** involution — a
contradiction, since `a≠b` are two of them. (Aligned or not: two distinct order-2 subgroups already
forbid `ℤ/4`; when aligned, `|E|=|A||B|=4` and the two involutions force `E≅V₄=ℤ/2×ℤ/2`.) ∎

**Lemma 2.4 (non-aligned ⟹ the type is wrong).** If `s` is non-aligned, `|E|>|A||B|`, so
`|E/A|=|E|/|A|>|B|` and `E/A≇B`. Hence the extension `1→A→E→B→1` with `B=Stab_{P'}(s)` does not
typecheck: `B` is a proper subgroup, not the quotient `E/A`. The nonzero representative `ε` (with `E/A`
in the quotient slot) uses `B'=E/A≠B=Stab_{P'}(s)`.
*Proof.* Counting; `A⊆E` gives `|E/A|=|E|/|A|`, and non-aligned means `|A·B|<|E|`, so
`|B|=|A·B|/|A|<|E|/|A|`. ∎

**Theorem 2.5 (collapse).** The geometric stabiliser class `[ω_st]∈H²(B;A)` built from a ZS
point-stabiliser with `A` normal is **defined exactly when `s` is aligned, and is then `0`.** No
internal exact factorisation produces the nonzero class `ε` with `B=Stab_{P'}(s)`; in particular the
bridge §3 witness `E≅ℤ/4` lies outside the aligned hypothesis it is stated under.
*Proof.* Well-typedness (`|E/A|=|B|`) holds iff `|E|=|A||B|` iff aligned (Lemma 2.4); aligned + normal
forces split, `[ω_st]=0` (Lemma 2.2); and `(ℤ/2,ℤ/2,ℤ/4)` cannot occur at all (Lemma 2.3). ∎

**Computational confirmation** (`comp2_geometric_splitting.py`, all exact factorisations of
`S₃,S₄,A₄,D₄,V₄,D₁₂,A₅`; several hundred point-checks): `A∩B=1` in every case; `(C₂,C₂,C₄)` never
occurs; and **no** aligned + `A`-normal extension is ever nonsplit. (Aligned cases with `A` *not*
normal do occur — e.g. `S₄=C₄·S₃` — but there `A` is not a valid kernel and `H²(B;A)` is not defined;
these are genuine nonabelian ZS/matched-pair products, out of scope per `g-obstruction-is-h2-class`.)

**Reading.** This is the "check the support / don't conflate" discipline turned on my own file. The
bridge §3 correctly recalls that `H²(ℤ/2;ℤ/2)={0,ε}` classifies the two abstract extensions `V₄` and
`ℤ/4`; the scope slip is attaching the nonzero one to the *aligned* geometry, where it cannot live.
The honest geometric statement: **aligned orchestration never entangles the two factor holonomies via
a stabiliser class — the entangled `ℤ/4` is an abstract extension, not a ZS point-stabiliser.** The
genuine geometric entanglement of composition is the *emergent-holonomy* phenomenon of the bridge §2.1
(composite stabiliser strictly larger than the product of factor stabilisers), which is a statement
about the vertex monoid of `𝔸(↓_⋈)`, **not** an `H²(B;A)` class. Part 1.5 therefore *strengthens* the
"two distinct sites" thesis: the stabiliser site's class is forced to `0` precisely where the naive
identification wants it nonzero.

---

## 3. Part 2 — No comparison functor rescues the identification

`state/PROVE.md` Part 2 asks: is there a functor `F:𝔸(↓_⋈)→Sk_C` and a single BW class `Ω` on `Sk_C`
whose pullback, restricted to isotropy at `s`, recovers `[ω_st]`? The isotropy-restriction lemma
answers **no, for every `F`.**

**Lemma 3.1 (isotropy restriction is natural in functors).** For a functor `F:𝒜→ℬ`, a natural system
`𝒟` on `ℬ`, and an object `a∈𝒜`, `F` restricts to a homomorphism `F_a:Aut_𝒜(a)→Aut_ℬ(Fa)` and for
all `n` the square commutes:
```
        H^n_BW(ℬ;𝒟) ──F*──▶ H^n_BW(𝒜;F*𝒟)
             │ i_{Fa}*                │ i_a*
             ▼                        ▼
        H^n(Aut(Fa);𝒟(Fa)) ─F_a*─▶ H^n(Aut(a);𝒟(Fa)).
```
*Proof.* On normalised cochains, `(i_a*F*ξ)(φ_n,…,φ_1)=ξ(Fφ_n,…,Fφ_1)`. Functors preserve
isomorphisms, so each `Fφ_i∈Aut_ℬ(Fa)`; thus the right side is `(F_a* i_{Fa}* ξ)(φ_n,…,φ_1)`. The two
composites agree on cochains, hence on cohomology. ∎

**Theorem 3.2 (rigid-target obstruction).** Let `ℬ` be automorphism-rigid. Then for every functor
`F:𝒜→ℬ`, every `n≥1`, every object `a∈𝒜`, and every class `Ω∈H^n_BW(ℬ;𝒟)`:
```
        i_a* F* Ω = 0.
```
*Proof.* `Aut_ℬ(Fa)=1`, so `i_{Fa}*` in Lemma 3.1 has target `H^n(1;·)=0`; hence
`i_a*F* = F_a* i_{Fa}* = 0`. ∎

**Corollary 3.3 (Part 2, the obstruction).** For **every** functor `F:𝔸(↓_⋈)→Sk_C`, every state `s`,
and every class `Ω∈H²_BW(Sk_C;𝒟)` (in particular `Ω=[ω_h]`), the pulled-back class restricts to `0`
at the isotropy group `Aut_{𝔸(↓_⋈)}(s)=Stab_Q(s)`. Since the (nonzero) stabiliser class is a nonzero
isotropy class, `i_s*F*[ω_h]≠[ω_st]` for every `F`. The proposed rescue is impossible — not for want
of the right `F`, but because `Sk_C` is rigid, so *any* functor sends every isotropy automorphism to
an identity, and *any* pulled-back class is isotropy-invisible. ∎

**Reverse direction / cospans (scoped).** One might instead seek a functor `Φ:Sk_C→𝒞` realising the
handoff class as the pullback of a pure-isotropy (stabiliser) class on `𝒞`. When `𝒞=BG` is a
one-object group category (the faithful home of a stabiliser class), this too collapses: any
`Φ:Sk_C→BG` sends `[s],[s₂]` to `g_s,g_{s₂}∈G` with `g_s·g_p=g_q=g_{s₂}·g_p`, so **right-cancellation
in the group forces `g_s=g_{s₂}`**. Hence for any BW 2-cochain `ξ` on `BG`, `(Φ*ξ)([s],[p])` and
`(Φ*ξ)([s₂],[p])` are equal, i.e. `Φ*ξ∈⟨(1,1)⟩=B²`, so `Φ*[ξ]=0∈H²(Sk_C;𝒟)`. The handoff class,
being the *difference* coordinate `ω([s₂],[p])−ω([s],[p])=ε≠0`, is not such a pullback. (Verified by
enumeration for `G∈{ℤ/4,V₄,S₃}`: `g_s=g_{s₂}` is forced in all `16,16,36` functors.) The general
many-object cospan is obstructed only when the image of `[p]` is right-cancellable; I do not claim the
fully general negative and flag it as the one honest gap (§4).

**The reconciliation (why they rhyme without being equal).** Category cohomology `H²_BW(𝒞;𝒟)` carries
two canonical structure maps: **isotropy restriction** `i_x*` onto the loop/automorphism part, and the
complementary **off-diagonal / nerve** part supported on chains through distinct objects. The handoff
class is a nonzero *off-diagonal* class (its cocycle lives on `([s₂],[p])`, a 2-chain through three
objects; `i_x*` annihilates it). The stabiliser class is a nonzero *pure-isotropy* class (a loop class
at one object). The generator `ε` — the single ZS token bit — surfaces in **both** parts, once as the
obstruction to a closing basis on `Sk_C` (the handoff class: does a ZS product / distributive law
*exist*?) and once as the abstract obstruction to an isotropy group *splitting* (the stabiliser class).
These are the images of one datum under two **incomparable** maps out of `H²`, not two restrictions of
one class. That is the precise sense in which the two `𝔽₂`'s coincide only numerically.

---

## 4. Status ledger (honesty)

**Proved (this file):**
- **Part 1** (Cor 1.3): `i_x*[ω_h]=0` for all `x`; naive "stabiliser = isotropy-restriction of handoff"
  is FALSE. Rigorous (Lemma 1.1 + Thm 1.2, the trivial group has no positive cohomology) + machine-
  checked cochain support.
- **Part 1.5** (Thm 2.5): aligned + normal ⟹ `[ω_st]=0`; `(ℤ/2,ℤ/2,ℤ/4)` geometrically impossible;
  non-aligned ⟹ `E/A≇B` so the class is not even well-typed with `B=Stab_{P'}(s)`. Rigorous (elementary
  group theory) + exhaustive sweep (`S₃…A₅`). A scope-correction of bridge §3’s witness framing.
- **Part 2** (Cor 3.3): for every functor `F:𝔸(↓_⋈)→Sk_C`, `i_s*F*[ω_h]=0`; the proposed rescue is
  impossible for all `F`. Rigorous (Lemma 3.1 naturality + rigid target). Reverse `BG`-cospan collapse
  proved and enumerated.

**Gaps / scope (honest):**
1. **General cospan.** The reverse obstruction is proved for one-object (`BG`) targets and for
   right-cancellable `F([p])`; a fully general many-object cospan `Sk_C→𝒞←𝔸(↓_⋈)` with a single `Ω`
   restricting to both is not ruled out in complete generality. I believe it is obstructed by the same
   off-diagonal-vs-isotropy invariant but do not claim it. This is the one open edge.
2. **Coefficient identification.** Even setting base categories aside, the coefficient systems differ:
   `𝒟` (factor vertex groups on `Sk_C`) vs `A=Stab_P(s)` as a `B`-module. No natural identification;
   consistent with §3’s "incomparable maps."
3. **Scope of Site S** inherits the bridge’s aligned + abelian + normal hypotheses; the nonabelian ZS
   obstruction remains Pirashvili’s (cited, not reproved).

**Cited (proved/published):** Baues–Wirsching, *Cohomology of small categories*, JPAA 38 (1985) —
isotropy restriction, natural systems, `H²`-classifies-linear-extensions; the reentrancy `[ω]=ε`
(`2026-07-20-…-analytic.tex`, proved/Lean); the ZS bridge (`2026-08-12-…`, peer-reviewed);
Eilenberg–Mac Lane extension theory; Ahman–Uustalu 2013 (ZS = matched pair, published).

## 5. Grant framing
Gap #3 is closed with a clean negative that *strengthens* the orchestration narrative rather than
denting it. "Composing two coeffectful agents produces two degree-2 obstructions with the same
`𝔽₂`-signature — the handoff obstruction (does a serialising distributive law exist?) and the
stabiliser obstruction (does the emergent isotropy split?) — and they are provably **not** the same
class: the handoff class is invisible to isotropy, the geometric stabiliser class collapses to zero
whenever it is defined, and no comparison functor identifies them." Two obstructions, one ZS bit, two
incomparable homes: exactly the kind of honest structural theorem the Impact section wants, and it
inoculates the book against the fusion-category conflation error it was flagged for.
