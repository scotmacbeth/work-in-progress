# Linear containers over Vec: the biproduct collapse (PROVE, 2026-08-18)

**For Robin / Neil / Rick.** First rigorous result on the new front Neil steered
(2026-08-15): containers with a **vector-space answer object**, i.e. over
`Fam(Vec^op)`. Proof file: `proofs/2026-08-18-linear-containers-vec.md`. Registry:
`proofs/registry/linear-containers-vec.json` (validated, `proved`).

## The setup in one line
`LinCont := Fam(Vec^op)`: shapes `S∈Set`, positions `P_s∈Vec_k`. Extension
`⟦S,P⟧ W = ⊕_{s∈S} Vec(P_s, W) : Vec → Vec` — a direct sum of "additive
representables" `h_{P_s} = Vec(P_s,-)`, with `h_k = Id`.

## The headline (Part 1 — PROVED)
Base-change `Set ↝ Vec` turns the coproduct/product distinction into a
**biproduct**, and the container's shape data goes from *free* to *hidden*:

- **Terminal recovery dies.** `Vec`'s terminal object is `0`, so `⟦S,P⟧(0)=0`.
  The Set slogan `F(1)=S` has NO analog — you cannot read the shapes off anywhere.
- **Finite collapse.** For finite `S` and finite-dim positions, `⟦S,P⟧ ≅ Id^N`
  with `N = Σ_s dim P_s = dim(⊕_s P_s)`. A finite linear container is classified
  by the **single number `N`**; the shape partition is invisible. `End(Id)=k` is a
  field, so Krull–Schmidt makes `Id^N` the unique indecomposable decomposition —
  `N` is recovered, nothing else. (`({∗},k²)` and `({∗,∗},(k,k))` both give `W²`.)

## The crux (Part 2 — PROVED as a negative-with-remedy)
This is the load-bearing contribution and the answer to the neighbour pass's
warning that "Vec is not extensive." Two computations:

    Nat(⟦S,P⟧, ⟦T,Q⟧) = ∏_s ⊕_t Vec(Q_t, P_s)        (natural transformations)
    Fam(Vec^op)-hom   = ∏_s ∐_t Vec(Q_t, P_s)        (container morphisms)

The extension `⟦−⟧` sends a container morphism to the natural transformation
supported at the single shape `f(s)` — i.e. the induced map on homs is the
inclusion **`∐_t ↪ ⊕_t`**. So `⟦−⟧` is **NOT full**: natural transformations may
take linear combinations across shapes; container morphisms (bound to one `f(s)`)
cannot.

**The punchline.** Over `Set` the *same* hom formula holds, but there the
coproduct in the formula IS the disjoint union (`⊕_t = ∐_t`), so container-hom
`= Nat` and `⟦−⟧` is fully faithful — the classical Diers/familial-representability
theorem. **The one symbol that changes under `Set ↝ Vec` is `∐ ⊊ ⊕`, and that IS
the failure of extensivity.** Object-collapse (Σ → biproduct) and morphism-collapse
(∐ → ⊕) are the *same* phenomenon. That unification is what I think is new — every
individual ingredient is owned (strict polynomial functors own the objects; Diers
owns familial representability; Mitchell owns "algebroid"), but nobody assembled
them or named the collapse.

## Part 3 (COMPUTED — a third collapse, and a caution for the grant)
Finite-dim composition is clean: `(S,P) ◁ (T,Q) = (S×T, (P_s⊗Q_t))`, unit
`({∗},k)` — shapes multiply, positions tensor. **Not** the Set dependent sum
`∐_s T^{P_s}`: linearity kills the dependency (a linear map into `⊕` is a sum of
components, not a choice of branch). Consequence: a `◁`-comonoid collapses to a
**family of `k`-algebras** (one shape ⟹ a single `k`-algebra, à la Mitchell), NOT
a full algebroid — the off-diagonal homs a genuine `k`-linear category needs are
unreachable. So the tempting crown analog `◁`-comonoid `≅` algebroid is **false in
the finite-dim case**; getting real algebroids needs a different (lax/bimodule)
composition. Worth knowing before we write it into the grant.

## Gaps (honest)
1. General representation theorem for infinite `S` / infinite-dim positions — the
   intrinsic characterization of `⟦−⟧`'s image and recovery up to biproduct
   ambiguity is open past the finite case (Diers extensivity is the obstruction).
2. Prop 4.2's comonoid-law check is a sketch (banked `computed`, not `proved`);
   and whether a lax composition recovers algebroids is open.

## Why it matters for the grant
This is a genuine "check what the terminal object is" astonishment that reframes
the whole container programme under base change — exactly the kind of structural
surprise the grant's theory pillar wants, and it comes with a precise diagnosis
(non-extensivity) rather than a vague "it's different over Vec." **Rick** — this
touches your obstruction-theoretic instincts: the fullness gap is a genuine
cokernel (`⊕/∐`); is there an Ext-flavoured reading of it? Would value your eye.
