# For Neil / Robin — Reader's proof-relevant monad liftings ARE small categories

**MacBeth, 2026-08-09 (prove).** Full proof: `proofs/2026-08-09-reader-liftings-are-categories.md`.
Registry: `reader-liftings-are-categories` (proved) in `effect-coeffect-arrows.json`.

## The one-sentence version
The proof-relevant monad liftings of **Reader** `y^E` to `Cont` are **not** the ∏/Σ/mix trio we
guessed — the full product ∏ is *excluded*, and the survivors are exactly **`E`-indexed families of
small categories**: a monad lifting of Reader = (`E`-indexed) polynomial comonad = small category,
one categorical level down. So the predicate-lifting story lands squarely on your DCont≅Cat spine.

## Why this matters for the grant (Path 2, Theory pillar)
We now have a second, independent route into "directed containers = categories": not from
comonoids in `(Cont,◁)`, but from **classifying the liftings of a fixed monad**. The Ahman–Bauer
`∏`-lifting `T_M` (the "obvious" proof-relevant one) *fails* to be a monad for Reader — and the
thing that *does* work is a small category per leaf, with composition as the multiplication. It is a
clean slogan for the taxonomy section: *"the proof-relevant ways to lift a reader effect are its
internal categories."*

## The result (precise)
Fibred proof-relevant **polynomial** monad liftings of `R=y^E` along the shape fibration
`p:Cont→Set` ≅ `E`-indexed families of small categories `(C_v)_{v∈E}`, via
```
   L(B) = ⊔_{v∈E} ⊔_{i∈Ob C_v} B_v^{ C_v(i,→) },   ε = identities,   δ = composition.
```
- **∏ excluded.** `L(B)=∏_v B_v` has one shape reading *two* leaves ("a cross-leaf object"); the
  multiplication δ needs, at each leaf-`v` position, an inner shape reading *only* `v`, and ∏ has
  none. So δ does not exist — matching `R` non-cartesian (your A/E flag, one level up).
- **Σ_U = discrete categories** on the leaves `U⊆E` (identities only) — the "linear" extreme.
- **Non-discrete liftings are real.** `L(B)=B_0×B_0` with the *swap* comultiplication is the
  one-object groupoid ℤ/2 — a genuine lifting that is neither ∏ nor Σ nor a leafwise mix. Products
  appear **within** a leaf (hom-sets of a category), never **across** (that is exactly ∏).
- **Analytic dies on the counit.** Symmetric/Bag aggregators have no natural unit ε, so *polynomial*
  is the boundary — the same polynomial-vs-analytic line as the Bag refutation, 7-for-7.

## How it connects to your A/E note (UID-94)
Your `A = All = ∏` is cartesian-only *as a bifunctor* (P1). Here `∏` fails to be a *monad lift of
Reader* for the same reason, read as a multiplication: `∏` has no canonical pushforward along
Reader's (non-cartesian) diagonal. The survivors replace "one product over all leaves" with "a
category structure per leaf," and the lift's μ is category composition seen through the fibrewise
op (the monad↔comonad twist). So: **A/E flag (object level) and the lifting classification (monad
level) are the same non-cartesianness, and what it leaves standing is `Cat`.**

## Honesty / what's open
- Proved for **polynomial** aggregators (the intended `Cont` setting); analytic excluded by the
  counit (Prop 5.1, symmetric/Bag). Removing the hypothesis entirely needs the lemma "every
  accessible Set-comonad with a counit is polynomial" — not claimed.
- **State and general `M` not done.** State is also a container monad keeping one distinguished token
  per surviving leaf, so the pure-shape forcing should transfer; I conjecture liftings of a general
  container monad `M` ↔ *categories fibred over `M`* (Reader = discrete `E` ⟹ plain `E`-indexed
  categories). **Neil — is "categories fibred over M" the framing you'd want for Ch7, and should I
  make State the next PROVE target?**
- Verified by two independent programs (monad-law enumeration vs category-axiom counting): they
  agree on every case (`[2]→4=#monoids(2)`, `[2,1]→6`, `∏→0`, impure→0).
