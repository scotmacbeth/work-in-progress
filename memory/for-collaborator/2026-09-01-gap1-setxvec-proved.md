# For collaborator — Gap 1 inhabitant `Set×Vec_fd` PROVED; dual-numbers refuted; a per-object axis

**MacBeth, 2026-09-01 (PROVE).** Full proof: `proofs/2026-09-01-gap1-setxvec-proved.md`.
Verification: `scratch/2026-09-01-gap1-verify.py` (all PASS, 0 mismatches). Registry:
`open-middle-region` in `left-adjoint-over-vec.json`, promoted `computed → proved`.

## What is now `proved`

**`Set × Vec_fd` is `◁`-admissible on the finite-vec-support locus.** I built the composition
container `r = p◁q` explicitly (shape `D = ∐_s T^{A_s}`, set-positions `∐_a B_{f(a)}`, vector data
concentrated at one slot `U_{d_0} = ⊕_{s,t}V_s⊗W_t`) and an **explicit natural isomorphism**
`Θ = (Θ_set, Θ_vec) : ⟦p◁q⟧ ⟹ ⟦p⟧∘⟦q⟧`. The Set component is the classical container-composition
bijection (with explicit inverse); the Vec component is a composite of four natural isos that comes
out, concretely, a **coordinate permutation matrix**. Naturality is checked on both components. This
is a *built map*, not a cardinality match — the discipline that burned us twice this month (the
`4=4` collisions) is satisfied: computationally `Θ_vec` is a full-rank permutation, `Θ_set` a
verified bijection with round-tripping inverse, on asymmetric and zero-position cases.

Consequences: `Set×Vec_fd` is admissible + **non-collapse** (`(A,V)` tiny iff `|A|≤1`) +
**non-cartesian** (`⊗_k≠⊕`) + **disconnected unit** — a genuine Gap-1 inhabitant. So **Theorem B is
not sharp**: admissibility does *not* imply unit-connectedness in general; Theorem B's
lextensive-cartesian hypotheses are essential (not droppable).

**The locus is the summability boundary, stated exactly.** `⟦p⟧` is an endofunctor of `Set×Vec_fd`
iff `{s : V_s ≠ 0}` is finite (finite vec-support); `S` and the set-positions `A_s` stay arbitrary.
This locus is closed under `◁`. Outside it, `⟦p⟧` leaves `Vec_fd`; and over *full* `Vec`, non-fd
positions are not copower-tiny and the absorption fails — that is the predecessor's Gap 1, still open.

**Coherence, honestly.** There is **no canonical** monoidal structure on `Fam((Set×Vec_fd)^op)`: the
construction picks a slot `d_0 ∈ ∐_s T^{A_s}`, and there is no natural such choice. A *non-canonical*
monoidal structure exists (concentrate via the Set associator). The obstruction to canonicity is
exactly the non-faithfulness of `⟦−⟧` on the Vec factor — Theorem D in the wild. The canonical monoid
lives in the image `⟦𝒫⟧ ⊆ [C,C]` under functor composition.

## The correction Neil/Robin should note: the dual-numbers probe is REFUTED

The brief proposed `k[ε]/ε²`-modules as the cleanest *irreducible* Gap-1 probe (dualizable free
modules vs non-dualizable `k` = an "internal rigid/flexible mix"). **This is wrong, and instructively
so.** The programme's axis is **copower-tiny** (`[P,−]` preserves coproducts), which is **not**
dualizability. General lemma (any ring): a finitely generated `P` has `Hom_R(P,−)` preserving
coproducts (any `P → ⊕M_i` factors through a finite subsum). So over an Artinian ring **every** fg
module is copower-tiny — including `k = R/εR`, whose `Hom_R(k,−) = ker(ε)` preserves `⊕` even though
`k` is not projective/dualizable. Hence `fg-R-Mod` (any commutative Noetherian `R`) is a **collapse
base**, structurally identical to `Vec_fd = fg-k-Mod`, `◁=⊗_R`, disconnected unit — **the collapse
pole, never Gap 1**. This single lemma kills the *entire* "modules over a mixed ring" candidate
family: dual numbers, `k[x]`, `ℤ`, recollements/pullbacks of module categories. Verified numerically
(0 mismatches; `k` copower-tiny = YES, `k` projective = NO).

## The structural takeaway (toward Neil's #1 `◁`-generality question)

**Admissibility is a per-object property:** `Fam(C^op)` is `◁`-admissible **⟺ every object of `C` is
absorptive** (`X ↦ [P,⟦q⟧X]` is an extension for every `q`). Two sources of absorptivity —
**copower-tiny** (flexible/additive) and **distributive** (rigid/extensive). Gap 1 lives at their
**seam**: additive-fg bases are all-tiny (collapse); extensive non-collapse bases have their unit
connected forced (Theorem B); so a non-collapse *disconnected* base must run both mechanisms. The
product `Set×Vec_fd` does exactly that, by *factoring* rigid and flexible.

So the sharp question "is there an **irreducible** (non-product) Gap-1 inhabitant?" is now pinned
between two identified open doors:
- **additive & non-fg** — needs a genuinely non-copower-tiny (infinite-dim) object; the absorption
  then requires infinite direct sums — this **is** the predecessor's Gap 1 (`Fam(Vec^op)`, infinite
  `T`, infinite-dim positions), open;
- **non-additive & disconnected** — disconnected by non-injectivity of `γ`; the only base I know is
  `Set_*`, which is *inadmissible* (Theorem A). Conjecture: every `γ`-non-injective closed base is
  inadmissible.

**Conjecture 6.2 (decomposition, speculative but sharp):** every absorptive object is a tensor of a
copower-tiny part and a distributive part; hence every *nice* Gap-1 inhabitant decomposes as
rigid-extensive × flexible-additive, and **no irreducible inhabitant exists among nice bases**. If
true this replaces cartesianness and idempotent-splitting as *the* classifying axis — a one-statement
answer across all three poles + Gap 1. That is the natural next PROVE target, and it wants a novelty
gate against Carboni–Lack–Walters and DJN `2305.05655` first.

## Grant framing
Theory section: "process substitution `◁` exists on a resource base exactly when every resource is
either *flexible* (copower-tiny — the additive/linear mode, absorbing structure into a tensor) or
*rigid* (distributive — the set-like mode, forcing branching shape). A base carrying a compositional
plug-in calculus is a controlled mixture of the two; the cleanest mixtures are products of a
set-like and a linear resource model." Predictive, and it says which semantic bases can carry the
calculus *before* one is built.
