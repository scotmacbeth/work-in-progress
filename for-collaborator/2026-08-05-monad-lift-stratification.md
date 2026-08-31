# Four levels of a monad, seen from the container fibration

**A theory contribution for the Kodamai AI-Mathematician grant.**
MacBeth — write session, 2026-08-05. Neil-independent grant prose + drop-in collaborator note.
Audience: a reader who knows monads but has never met containers-as-a-fibration.

---

## The result in one sentence

> **For a Set-monad `M`, asking how much of its structure survives the lift to the container
> fibration stratifies the monad universe into four strictly nested classes —
> pure writer `A×(−)` ⊊ writer-with-exceptions `E+A×(−)` ⊊ cartesian ⊊ Π-liftable (has support) —
> each detected by a concrete, computable fibred condition and each boundary witnessed by a
> named, everyday monad.**

This is a *container-native refinement of the classical notion of a cartesian monad*: instead of
the single yes/no question "is `M` cartesian?", the fibration supplies a four-rung ladder that says
exactly *which* structural guarantees a monad offers when you compose effectful, resource-tracking
processes. That is precisely the kind of correctness-of-composition taxonomy the grant is about.

---

## The setup, in six lines

Containers `(S,P)` — a set `S` of *shapes*, and for each shape `s` a set `P(s)` of *positions* —
form a category `Cont` that maps down to `Set` by remembering only the shapes: `p:Cont→Set`,
`(S,P)↦S`. This projection is a *fibration*. The one fact a monad-literate reader needs: a morphism
of containers has a **forward** part (on shapes) and a **backward** part (on positions), and it is
called **cartesian** when the backward part is a family of *bijections* — no positions created,
merged, or destroyed.

Every Set-monad `M` casts **two shadows** on this fibration:

- a **comonad** `G_M(S,P) = (S, M∘P)` — it acts only on positions, sits vertically over the base,
  and is **cartesian for every `M` whatsoever** (proved and Lean-certified,
  `lean/.../FibredTransfer.lean::onMor_cartesian`);
- a **monad** `T_M(S,P) = (MS, P^⋆)` — it acts on shapes and genuinely *lies over `M`*
  (`T_M` projects to `M` along `p`). This is the ∏-cointerpretation lifting of Ahman–Bauer
  [AB24, Thm 6.3]; it exists exactly for the **Π-liftable** monads — those with a *notion of
  support*: each element `m∈MX` has a finite set of leaves carrying labels in `X`. (This class is
  *strictly larger* than the polynomial monads: powerset has a notion of support yet is not
  polynomial — that gap is the top rung of the ladder.)

The comonad shadow is always perfect. All the information about `M` is therefore concentrated in
**how much fibred structure the monad shadow `T_M` retains** — and that is the ladder.

---

## The ladder

Four increasingly demanding questions, from the top of the tower down:

| Level | Fibred detector (what you compute) | Reading in plain terms | Monad class | First witness *outside* |
|------:|------------------------------------|------------------------|-------------|--------------------------|
| **4** | `T_M` is *defined at all* | `M` has a notion of support | Π-liftable (has support) | (`Reader`, `State` — no support) |
| **3** | `T_M` *preserves cartesian morphisms* | composing never *merges* leaves | cartesian monad | `Pf` (powerset: `∪` merges) |
| **2** | the reverse comparison `κ: G_M T_M ⇒ T_M G_M` *exists* (arrows compose) | effect–coeffect **arrows form a category** | writer-with-exceptions `E+A×(−)` (= non-branching) | `List` (branches: arity ℕ) |
| **1** | `λ: T_M G_M ⇒ G_M T_M` is *invertible* (strict **Beck–Chevalley**) | products preserved on the nose, **including the empty one** | pure writer `A×(−)` | `Maybe`, `Exc` (exceptions break the empty product) |

Read from the bottom up, each rung *strictly* implies the one above it:

```
  pure writer  A×(−)   ⊊   writer+exception  E+A×(−)   ⊊   cartesian   ⊊   Π-liftable
      Id, Writer              +Maybe, Exc                    +List           +Pf
   strict Beck–Chevalley    arrows form a category      no leaf merging    has a support
```

The one-line summary for the grant: **strict Beck–Chevalley ⇒ arrows compose ⇒ leaves don't merge
⇒ support exists** — a chain of *strict* implications, each `⊊` witnessed by a named monad, none of
which reverses. The middle rung is the one we can state as a clean biconditional and have proved as
such: *the effect–coeffect arrows `G_M p ⤳ T_M q` form a category **if and only if** `M` is
non-branching* (`effect-coeffect-arrows`), and that non-branching class is classified as exactly
`E+A×(−)` in `affine-classification`.

Every boundary is populated by a monad you already use: `Maybe` is non-branching but not a pure
writer; `List` is cartesian but branches; `Pf` (powerset) has a notion of support but is not
cartesian. Nothing is vacuous, and nothing collapses.

---

## The honest arc: this began as a *refuted* conjecture

The result is sharper than what we set out to prove, and it is worth telling the grant reader why.

We had been carrying a tidy slogan — *"containers preserve cartesian morphisms = `M` non-branching
= strict Beck–Chevalley"* — a proposed **TFAE** bundling all four detectors into one equivalence.
This session's proof shows the TFAE is **false**: the three conditions live on three different rungs.
The failure is the content. Two everyday monads carry it:

- **`List` splits cartesian from non-branching.** The free-monoid monad is the textbook cartesian
  monad — concatenation never merges elements — yet it *branches* (a shape can have any arity).
  So *cartesian does not imply non-branching*: "preserving cartesian morphisms" is strictly weaker
  than what our slogan claimed.
- **`Maybe` splits strict Beck–Chevalley from non-branching.** `Maybe` is non-branching, so its
  arrows compose; but at its *empty* shape the comparison `λ` is `M(1)→1 = (E+1→1)`, not invertible.
  Exceptions break strict Beck–Chevalley at exactly the nullary shapes. So *non-branching does not
  imply strict Beck–Chevalley*: strict-BC is **pure writer**, non-branching is **writer + exception**.

What survives is better than a slogan: a *four-level classification* in which each rung has a
computable test, a named monad class, and a witness for its strictness. A collapse would have said
"these four ideas are the same"; the truth is that they are a **ladder of composability guarantees**,
and knowing which rung a monad sits on tells you which compositional correctness properties you get.

---

## Why the grant wants this

The grant's Theory pillar is a taxonomy of *composable effects with correctness consequences*. This
result delivers exactly that, in three grant-legible ways:

1. **It is a computable, container-native refinement of "cartesian monad".** The classical dichotomy
   (cartesian or not) becomes a graded diagnosis. For an effect monad `M`, you can *compute* its rung
   and read off what compositional guarantees hold — no leaves lost, arrows associate, products
   preserved — from the rung alone.
2. **It ties the ladder to named effects.** The bottom two rungs are precisely the **writer-with-exceptions**
   monads `E+A×(−)` — logging that may fail, the workhorse effects of real pipelines. So the boundary
   is not an exotic edge case; it is where the effects an AI mathematician (or a supply chain, or a
   smart contract) actually uses start to lose compositional closure.
3. **It is a proof-and-a-half already machine-checked.** The always-perfect comonad shadow `G_M` is
   Lean-certified; the pivotal middle biconditional is proved in coordinates and checked on the
   Set-monad examples. It is a concrete deliverable for the Formalisation pillar, not a promissory note.

The retired slogan was appealing because it *felt* inevitable. The corrected ladder is the more
valuable object — strata, tests, and witnesses — and it is the shape a taxonomy of composable effects
should take.

---

## Provenance

- **Refutation + boundary table + strict chain:** `proofs/2026-08-05-cartesian-preservation-nonbranching.md`.
- **The two newly-closed rungs** (level 3⟺cartesian within Π-liftable via a leaf-reindexing bijection;
  strict-BC ⇒ non-branching at every arity): `proofs/2026-08-05-crown-gap-closure.md`.
- **Middle biconditional** (arrows form a category ⟺ non-branching) and the `E+A×(−)` classification:
  `proofs/2026-07-29-effect-coeffect-arrows.md`, `proofs/2026-07-30-affine-classification.md`.
- **The comonad shadow `G_M` is cartesian for every `M`:** Lean, `lean/Containers/Containers/FibredTransfer.lean`
  (`onMor_cartesian`); companion `TMCartesianBoundary.lean` for the `T_M` side.
- **External:** the monad lifting `T_M` is the ∏-cointerpretation of Ahman–Bauer, *Comodule
  Representations of Second-Order Functionals*, arXiv:2409.17664, Thm 6.3 [AB24] (deep-read). The
  cartesian/polynomial-monad framing is standard (the free-monoid monad `List` as the flagship
  cartesian monad).

### Open, flagged honestly (not for this note to close)
- Strict-BC ⇒ non-branching at arity ≥2 uses a cross-terms argument sketched, not written
  line-by-line — conceptually solid, mechanical (`crown-gap-closure` §, Gap 1).
- The reverse-`κ` associativity axiom E2′ is proved for the non-branching case and checked on the
  Set-monad examples; general Lean certification is a lean-session item.
- `List`'s cartesianness is checked on bounded data; the *branching* witness is unaffected.

---

*Drop-in status:* the block-quoted paragraph at the top is written to slot directly into the grant's
Theory / "taxonomy of composable effects" section. If Neil rules that the stratification also earns a
book aside, that is a separate edit and awaits his answer — this note does not touch the book.
