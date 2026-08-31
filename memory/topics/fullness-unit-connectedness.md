# T1 flagship: container extension full-faithful ⟺ monoidal unit CONNECTED (not extensivity)

**PROVED 2026-08-25** — `proofs/2026-08-25-fullness-unit-connectedness.md`, registry
`fullness-unit-connectedness.json` (validates, proved). Answers Neil's #1 (email UID 120).

## The theorem

For closed symmetric monoidal `C` with small coproducts, the container extension
`⟦−⟧ : Fam(C^op) → C-enriched-[C,C]`, `⟦S,P⟧ = ∐_s [P_s,-]`, acts on homs by `∏_s` of the
canonical comparison
`γ : ∐^{Set}_t C(I,X_t) → C(I, ∐^C_t X_t)` (`X_t=[Q_t,P_s]`). Hence:

- **⟦−⟧ fully faithful ⟺ the monoidal unit `I` is CONNECTED**, i.e. `C(I,-):C→Set` preserves
  small coproducts (γ a bijection). Sufficiency general; necessity via the **copower test**
  `T·C(I,Z) → C(I,T·Z)` (source `({s},Z)`, target `(T,(I))`), tight when a cogenerator
  `[-,Z₀]` is essentially surjective.
- **faithful ⟺ coproduct injections are `I`-disjoint** (γ injective); **full ⟺ γ surjective**.

Method: enriched co-Yoneda `Nat(h_P,G)≅G(P)` + `Nat(∐_s F_s,G)=∏_s Nat(F_s,G)`. Set-level, no
completeness needed.

## Two HONEST CORRECTIONS to the PROVE.md brief

1. **NOT extensivity.** `Set×Set` is (l)extensive yet `⟦−⟧` is NOT full — its unit `(1,1)` is
   disconnected (`C((1,1),(X,Y)+(X',Y'))=(X+X')×(Y+Y') ≠ X×Y+X'×Y'`). Witness: source
   `({s},(1,1))`, target `({t₁,t₂},((1,1),(1,1)))` → **2 container morphisms but 4 natural
   transformations**. Extensivity is neither necessary nor sufficient; **unit-connectedness**
   is the invariant. Verified `F_3`/finite.
2. **"faithful always" is FALSE.** Over `Vec`, `(f,0)` and `(f',0)` (distinct shape-maps, zero
   positions) both give the **zero** nat transf ⟹ `⟦−⟧` not faithful. Only "faithful on the
   non-zero part," as the Vec file already said. Faithfulness = `I`-disjointness of injections.

## The three poles

- **Set** (`I=1` connected): full-faithful = classical AAG; my Cor 3.1 *names its hidden
  hypothesis* — AAG works because `1` is connected, not (directly) because Set is extensive.
- **Vec** (`I=k`, `C(k,-)`=forgetful, ⊕ not preserved): neither full nor faithful; the `∐⊊⊕`
  crux of [[vec-biproduct-collapse-proved]] is one instance.
- **Set×Set** (extensive, unit disconnected): not full — the counterexample that kills the
  conjecture.

## Why folklore said "extensivity" (the real story)

Two theorems fused at `C=Set`: (a) full-faithfulness of the FIXED extension `⟦−⟧` = governed
by **unit-connectedness of the enrichment base**; (b) Diers reconstruction `S=π₀(el F)` from an
abstract familially-representable functor = governed by **extensivity of the CODOMAIN Set**. At
`C=Set` base=codomain so both read "extensivity." Off Set they separate.

**Also (Rem 3.5): does NOT contradict Gambino–Kock.** GK polynomials are the *fully internal*
construction (shapes internal, slice categories); its representation theorem holds over LCCC
bases like Set×Set. My `Fam(C^op)` is the *mixed* construction (external shape-set, internal
positions) — the external `∐_t` of internal homs is what a disconnected unit fails to preserve.
The two constructions agree only when the base is Set; that divergence IS the content.

## Corollaries
- **T3 (change of base = change of enrichment): PROVED.** Lax monoidal `F:Set→C` sends
  Set-containers to `Fam(C^op)`; full-faithful iff target unit connected. Free-vec `F1=k` not
  connected ⟹ linearizing strictly loses naturality = `∐⊊⊕`. Vec-enrichment = the invariant
  view (confirms Neil).
- **T2 (closedness): CONJECTURED, gaps.** (a) Day/Dirichlet `⊗` closed via pointwise Day right
  adjoint when `C` complete — adjunction shape only, bookkeeping unverified. (b) `◁`-coclosure
  via `Lan` preserving corepresentables — break located at `⊗≠×`, no general criterion.

## Open gap
Whether "`C(I,-)` preserves copowers" (the necessity I proved) always upgrades to "preserves
all coproducts" for a monoidal unit, in EVERY closed `C` (holds for all named bases). See
[[extensivity-is-container-boundary]], [[vec-containers-new-front]].

Grant: this is the general theorem Neil asked for, flagship-ready, with the conjecture fixed.
Feeds the unification-note WRITE (Vec-attention = worked instance).


## SECOND OCCURRENCE of the same condition (2026-08-30)

`γ : ∐^{Set}_d C(I,X_d) → C(I,∐^C_d X_d)` does more than decide fullness. It also decides the
**`◁`-coclosure**: if `I` is connected then `F_q = Fam(⟦q⟧^op) ⊣ (−)◁q` for **every** `q`, over any
closed symmetric monoidal cocomplete base — proof = `γ` twice plus tensor–hom, four lines, no
distributivity and no choice of presentation for `◁`
(`proofs/2026-08-30-left-adjoint-over-vec.md` Thm 1, `proved`; topic [[left-adjoint-over-vec]]).

> **T1 (fullness of `⟦−⟧`) and the existence of the left adjoint to `(−)◁q` are the SAME LEMMA
> applied twice.** One condition, two theorems.

The three poles transfer verbatim: `Set` ✓, `Set×Set` ✗ (lextensive but disconnected unit — so
extensivity is not the invariant on the left either), `Vec` ✗.
Honest correction #2 of this file (**`⟦−⟧` not faithful over `Vec`: distinct shape maps with zero
positions give the same natural transformation**) is *load-bearing* there: it is why
`⟦p◁q⟧=⟦p⟧⟦q⟧` fails to pin down `p◁q`, and why `◁ := ⊗` on the collapse locus has to be carried
as a **definition**.
