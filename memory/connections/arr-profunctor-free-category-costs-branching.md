# The profunctor is free; the category is what branching costs

**Claim (the honest synthesis of the whole effect–coeffect arc, and now the book
Ch4 spine).** For *every* monad `M` on a container, the effect–coeffect arrows

> `Arr_M(p,q) := Cont(G_M p, T_M q)`

assemble into a **profunctor** `Cont^op × Cont → Set` — no hypothesis on `M`. This is
immediate from the functoriality of the two feeds (`G_M` the transfer comonad, `T_M` the
Ahman–Bauer effect monad). The arrows always *exist as data*. What branching costs is not
the arrows but their **composition**: the biKleisli composite runs through the compositor
`κ:G_MT_M ⇒ T_MG_M`, and `κ` coheres (E1′–E4′) **iff `M` is non-branching**. So:

- **profunctor face** — always there (all `M`), pure functoriality;
- **bialgebra/Plotkin–Turi face** `λ:T_MG_M ⇒ G_MT_M` — **exists** always (all `M`);
- **arrow/Freyd face** `κ:G_MT_M ⇒ T_MG_M` — **non-branching only** (arity ≤ 1 ⟺ `M ≅ E+A×(−)`).

One entwined structure; branching is the wall between "profunctor with underlying arrows"
and "profunctor whose arrows compose into a category."

**⚠️ 08-05 CORRECTION — "three faces" undercounts; it is a 4-RUNG LADDER.** The crown TFAE
refutation ([[fibration-stratifies-monad-zoo]], [[crown-tfae-strict-chain]]) showed "`λ`
*exists*" (all `M`) ≠ "`λ` *invertible*." `λ`-invertibility (strict Beck–Chevalley) is a
strictly *narrower* rung than `κ`-composition: it holds only for **pure writer `A×(−)`**
(Maybe splits it — non-branching but nullary `str:(1+1)→1` not iso). So the honest count is
four rungs: `λ`-inv (pure writer) ⊊ `κ`-composes (non-branching `E+A×(−)`) ⊊ `T_M` cartesian
(`M` cartesian) ⊊ profunctor exists (∏-Mendler). The fibration is what makes the rungs visible.

## Why this is the right frame (not just a slogan)

It makes the branching obstruction **structural, not a failure**: nothing is missing when
`M` branches — you still have a perfectly good profunctor of arrows — you simply cannot
*compose* them coherently. This is the same content as
[[branching-obstruction-is-atkeys-index]] read the categorical way: Atkey's *closed indexed*
Freyd category is the profunctor-with-a-second-input; the *genuine* (non-indexed) Freyd
category is the profunctor that composes. Non-branching = index-collapse = "the composition
coheres." The profunctor statement is the object-level shadow of Atkey's index.

## Provenance / status (2026-08-04)

- The math was already all in `projects/books/category-of-containers.tex` (transfer `thm:*`,
  entwining `thm:entwine`, arrows `thm:arrows` = category ⟺ non-branching ⟺ `E+A×(−)`).
  The **08-04 write session** added `def:arrowprof` (the profunctor, for every `M`) as the
  Ch4 closing movement, with the "profunctor free / category costs branching" astonishment
  as a teachbox, and rewired the "three modes" paragraph + `thm:arrows` + the two-faces bullet
  to *reference* it. Book compiles, 66pp, 0 undefined refs, **no new citations** (no provenance
  debt). Placement/exposition, not new math. `for-robin/2026-08-04-arr-profunctor-in-book.md`.
- **08-04 prove** hardened the wall itself: the branching non-associativity is now proved at
  the **full `Cont`-morphism** level (`M=Pf`/`A₁`; the composite bracketings differ at one
  leaf), not merely fibrewise ⟹ "category ⟺ non-branching" is an **iff at full-morphism level**.
  → [[branching-full-morphism-lift]] (registry `branching-full-morphism-lift` = proved).
- **08-04 lean** machine-checked the classification bijection `T_M` monad ⟺ monoid on `E⊔A`
  (`E` left-zero ideal), certifying the `E+A×(−)` boundary in Lean.
  → [[lean-affine-classification-done]].

## The primary citable source (closes a paper-polish thread since 07-31)

**Power–Thielecke, "Closed Freyd- and κ-Categories", ICALP 1999** (deep-read 08-04 via CiteSeerX)
is now the citable primary source for "closed indexed Freyd category" — the vocabulary Atkey's
index-collapse framing borrows. It gives four equivalent presentations of λc-models incl. the
**closed Freyd category** `J:C→K` and the **closed κ-category** `H:C^op→Cat` (generic maps +
indexed right adjoint).

**⚠️ Load-bearing false-friend, must go in the book verbatim:** Power–Thielecke's letter **κ**
is *Hasegawa's stack-passing κ-calculus* (push/apply/mkthunk), historically UNRELATED to
MacBeth's compositor **κ:GT⇒TG**. Same symbol, different 1990s PL lineage. And the
agent-orchestration "Plumbing" post (Baez/Waites, Azimuth 2026-03-11) attributes its
"don't-care-don't-write" convention to the *same* Hasegawa κ-calculus — a three-way name
collision (Power–Thielecke κ / Hasegawa κ-calculus / Plumbing κ) all distinct from the
compositor κ. Disambiguate explicitly wherever both appear.

Links: [[branching-obstruction-is-atkeys-index]] · [[two-feeds-entwine-one-direction]] ·
[[effect-coeffect-arrows-first-strength]] · [[three-modes-of-composition]] ·
[[affine-classification-writer-exceptions]] · [[branching-full-morphism-lift]]
