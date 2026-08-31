# Bare ⊗-comonoids in Poly = families of monoids (answers Niu–Spivak Ch9 Q5, Poly/⊗ slice)

**MacBeth — 2026-07-17, PROVE deep-work session.**
Full write-up: `proofs/2026-07-17-bare-dirichlet-comonoid.md`. Registry:
`proofs/registry/bare-dirichlet-comonoid.json` (proved, validates). Verification:
`scratch/bare-comonoid/verify.py`.

## The result

Drop *all* directed-container / `◁` structure and ask only: which containers are comonoids for the
**Dirichlet (parallel) tensor** `(Cont, ⊗, y)`, `(p⊗q)[s,t] = p[s]×q[t]`?

**Answer: exactly the containers with a monoid on every direction set** — `c = Σ_{s∈S} y^{M_s}`, each
`M_s` an arbitrary monoid. A "family of monoids" / "set of monoids." The comultiplication is *forced*:
diagonal `s↦(s,s)` on shapes (because `×` on Set is cartesian), and on directions it *is* a binary
operation `m_s : c[s]×c[s]→c[s]`; counitality = unitality, coassociativity = associativity. No
cocommutativity (a comonoid need not be cocommutative — verified: the comonoid count equals the
*unfiltered* monoid count on order-3 fibres, non-commutative ones included).

Categorically, mirroring `Cont ≅ Fam(Set^op)`:
```
    Comon(Cont, ⊗, y)  ≅  Fam(Mon^op),        cocommutative ones  ≅  Fam(CMon^op).
```
Morphisms are: forward reindex on shapes + a *backward monoid homomorphism* per fibre.

## Why it matters / where it sits

- It **answers the Poly/⊗-comonoid slice of Niu–Spivak Ch. 9 Question 5** (verbatim: "characterize …
  the ⊗-(co)monoids in Poly, Cat♯, Mod … or create a theory of them") — which is *open* in the book.
- It **completes the comonoid trilogy** over a fixed carrier `c`:
  | structure | is |
  |---|---|
  | ◁-comonoid | small category (Ahman–Uustalu) |
  | ⊗-comonoid (this) | family of **monoids** |
  | double (◁ & ⊗) | set of **commutative** monoids (`comparitor-double-comonoid`, Eckmann–Hilton) |
  The bare ⊗ layer is strictly larger than the double layer — all monoids, arbitrary shapes — exactly
  the "strictly larger and cleaner" the PROVE brief predicted. The gap between the two *is* the
  Eckmann–Hilton commutativity that the ◁ side adds.
- **Grant use:** the "collective semantics — agents aggregate contributions, distribute returns"
  reading Niu–Spivak attach to ⊗-*monoids* (Rmk 3.78) has a clean dual on the comonoid side: a bare
  ⊗-comonoid is a shape-indexed family of monoids of directions, i.e. *per-state action monoids with
  no cross-state coupling* — the un-directed substrate onto which a category (◁) or a duoidal
  interchange later imposes coupling. Good "before/after" picture for the four-monoidal chapter.

## Honesty note (please cross-check the correction)

While running the honesty gate I re-read the full Niu–Spivak PDF and found that my own earlier note
`proofs/2026-07-15-comparitor-double-comonoid.md` §7 wrote "Spivak owns … the ⊗-comonoid
classification ('sets of monoids')." **That attribution is wrong.** The book classifies neither
⊗-comonoids nor ⊗-monoids in Poly: Q5 is open, and Rmk 3.78 leaves ⊗-*monoids* to "future work."
§8.2.4 "Parallel product comonoids" (Prop 8.79) is `⊗`-on-`Cat♯` (the double ingredient), *not* a bare
classification — its title is a false friend. I've corrected the registry node
`comparitor-comonoid-nogo` and flagged it in the write-up. The double-comonoid *theorem* itself
(= sets of commutative monoids) is unaffected; only the novelty-attribution line was loose.

## Next moves I'd suggest

1. **Lean.** The forward direction (monoid-on-fibres ⟹ ⊗-comonoid) is a natural companion to the
   already-verified `M3b`/comonoid-converse and `seqProdDistrib` work. The `⊗` bifunctor and its
   morphism action are the only new infrastructure; the laws are `rfl`-adjacent given a `Monoid`
   instance per fibre. Candidate LEAN target for the next lean session.
2. **Book.** One paragraph in the four-monoidal chapter: the three-layer table above is a genuinely
   nice "one astonishment" — *the same carrier is a category, a family of monoids, or (when both) a
   family of commutative monoids, depending only on which tensor you comultiply against.*
3. **Cat♯ and Mod slices of Q5** remain open (⊗-comonoids in `Cat♯` = double comonoids = done;
   but ×-comonoids in Poly/Cat♯/Mod, and everything in Mod, are untouched). Possible future PROVE.
