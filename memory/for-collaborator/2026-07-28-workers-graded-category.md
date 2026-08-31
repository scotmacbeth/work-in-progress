# The category of Workers, graded by (Set,×) — for Neil (Ch4)

**MacBeth, 2026-07-28.** Delivered on your 07-27 steer. Full proof:
`proofs/2026-07-28-delta-state-object-and-workers.md`. Registry: `state-object-delta.json` (valid, proved).
Code: `scratch/state-object-delta/` (exhaustive finite checks, all green).

## What I proved

**T1.** `ΔS = (S, s↦S)` is exactly the **codiscrete category** on `S` under DCont≅Cat, with the forced
directed structure `o_s=s`, `s↓p=p`, `p⊕p'=p'` (⊕ = second projection). D1–D5 verified. Its extension is
the **store/costate comonad** `⟦ΔS⟧X = S × X^S` (Uustalu–Vene) — counit `(s,v)↦v(s)`, comult
`(s,v)↦(s,λp.(p,v))`.

**T2.** `⟦ΔS⟧ = S × Reader_S(−)`: the **reader** `X^S` is the position fibre (read-only shadow); the
`S ×` factor is the current state + writeback. That writeback is exactly your "*there is something more to
be said*."

**T3 (the target).** A **Worker** `p→q` with state `S` is a container morphism `ΔS ⊗ p → q` (Dirichlet
tensor). The key fact is **`ΔS ⊗ ΔT = Δ(S×T)` strictly** (and `Δ1 = y`), so Worker composition

  `(ΔS⊗p→q)` then `(ΔT⊗q→r)`  ⟼  `w'∘(ΔT⊗w) : Δ(S×T)⊗p → r`

**multiplies the context to `S×T`** — precisely your prediction. This makes **Workers a category graded by
`(Set,×)`** (identity grade `1`, composition grade `×`, coherence = `(Set,×)`'s associator/unitors),
equivalently the **coKleisli category of the graded comonad `S ↦ ΔS⊗−`**. Associativity and unitality are
proved in coordinates and verified exhaustively (512 + 1369 associativity triples; unit laws; 400×256
valid composites).

**Why ⊗ and not ×.** The Dirichlet tensor is forced: under the product tensor `ΔS × ΔT` has fibres of
size `|S|+|T| ≠ |S×T|`, so the state would *not* multiply. Only the positions-multiply tensor works.

**Para (your item on "S might change").** Collapsing the grade gives
`Para(p,q) = Σ_{S:Set} Cont(ΔS⊗p, q)` with parameters (states) tensoring on composition — Gavranović's
Para construction of the `(Set,×)`-action `S·p = ΔS⊗p`.

## The two honest gaps (identifications, not the mathematics)

1. **Para exactness.** `Δ` is functorial only on *bijections* (a bare `h:S→S'` gives no canonical
   `ΔS→ΔS'`). So I have a *literal* Para over `Core(Set)` and a *graded* reading over all `(Set,×)`.
   Whether it's a strict `(Set,×)`-actegory Para needs a check against Gavranović's axioms — I graded that
   **computed**, not proved. Worth a look: is there a variance convention that makes it a genuine
   actegory, or is Core(Set) the honest home?
2. **Graded-comonad packaging** vs the Fujii–Katsumata–Melliès definition — short, unwritten.

## For the book / grant

This is the *state* axis of compositional correctness (context multiplies), complementary to the
Zappa–Szép `[ω]∈H²` axis (directed composition). Workers = stateful agents with context; the Para reading
plugs directly into categorical cybernetics / lenses. Natural **LEAN** next step: Lemma 3.1
(`ΔS⊗ΔT=Δ(S×T)`) and the composite are defeq-shaped — should mirror `MonadComonadTransfer.lean`.

Questions for you: (a) do you want Workers stated as a graded category or via the Para collapse in Ch4?
(b) Is Core(Set) an acceptable home for the Para statement, or should I chase the strict actegory?
