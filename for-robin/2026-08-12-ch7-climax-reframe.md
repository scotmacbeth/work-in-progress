# Ch7 climax reframe — liftings ≅ Fun(𝔸(↓),Cat) is now the punchline

**Write session, 2026-08-12.** File: `projects/books/category-of-containers.tex` (87pp, compiles
clean, 0 undefined refs). No email this session — write-session rule.

## What changed and why

The Ch7 classification section had, since the 08-11 write, its best result buried. The general
theorem — **degree-1 polynomial monad liftings of an update monad `Upd_{(S,P,↓)}` are classified by
`Fun(𝔸(↓), Cat)`, and the classification is holonomy-FULL** — sat at the end as a hedged "humbling
frontier" teachbox, *after* the π₀ two-poles box had already been presented as the answer. That
inverted the actual weight of the mathematics: π₀ does **not** classify; it merely happens to at the
two poles because each is degenerate in its own way.

So I reframed the arc as a genuine reversal (motto: fair is foul):

1. Reader liftings ARE small categories (kept).
2. State's store multiplication is INVISIBLE, π₀=1 (kept).
3. **The two-poles box now ends by making the "π₀ classifies" conjecture explicit** — the reader is
   led to commit to the wrong guess.
4. **New climactic subsection** `The general law: holonomy, and the two poles as its degeneracies`
   (`sec:update-liftings-holonomy`):
   - Definition of the update monad, the position-threading action `↓:P↷S`, and the action category
     `𝔸(↓)` (objects `S`, arrow `s→s↓p` per `p`).
   - The deepest-object associativity law `ρ_{s,p⊕q}=ρ_{s↓p,q}∘ρ_{s,p}` shown to *be* functoriality
     of the transport on `𝔸(↓)` — the transport isn't extra structure, it IS the functor.
   - **Theorem** `liftings ≅ Fun(𝔸(↓),Cat)`, with a book-level "why it holds."
   - **Worked example** ℤ/2 acting trivially: π₀=2 (like a two-leaf Reader) but **four** non-isomorphic
     liftings — one ℤ/2 of holonomy per orbit. The count was an illusion.
   - Teachbox **"trivial two ways"**: Reader is holonomy-free because `𝔸(↓)` is *discrete* (nothing to
     transport along); State because its overwrite monoid has *reset* elements forcing endpoint-locality
     and codiscrete collapse (transport *erased*, not absent). π₀ classifies iff every component is
     holonomy-trivial. (A free ℤ/2 action is a third road to the cliff.)
   - Closing teachbox **"the holonomy is a group representation"**: the isotropy action is a rep of
     `Stab(s)` on the fibre category — a second-order compositional datum, the exact sibling of the
     `[ω]∈H²` reentrancy class from the Zappa–Szép chapter. Grant line: orchestrating a threading agent
     with nontrivial isotropy composes a group representation into the whole; Reader/State are the agents
     whose rep is trivial. *Composition remembers a group.*

## Honesty / flags

- One **correctness slip I caught and fixed** while writing: my first draft of the theorem said
  "Reader and State are the cases where every functor is constant up to iso." False for Reader — a
  functor out of a *discrete* category is an arbitrary family, not constant. Reworded to "trivial
  isotropy ⟹ the datum degenerates to a π₀-indexed family of *plain* categories (arbitrary for Reader,
  single for State)." The teachbox already used "component-wise holonomy-trivial" correctly.
- The `[open]` flags are kept honest: degree-1 only, `|S|=2` machine-verified (argument uniform),
  beyond-Upd and higher object-degree still open, Uustalu TTCS 2017 novelty-check still owed.
- Citations: `AU16` and `CBP` are deep-read (verified in sources.json). `AhmanUustalu13` is the seed
  PDF `Ahman-Uustalu_Update-Monads-Cointerpreting-Directed-Containers_2014.pdf`, cited only for the
  standard `Upd` definition; the bibitem data is accurate. WRITE.md pointed at
  `memory/code/citation_check.py` — that script is not present in this environment, so I verified
  provenance by hand instead. Worth restoring the script or noting where it lives.

## For a next session (not this one)

- LEAN: `HolonomyWitness.lean` already machine-checks the refutation (per MEMORY.md 08-12). If it isn't
  cited in this teachbox yet, a lean/write pass could add `\prov{... Lean-verified: HolonomyWitness.lean}`
  to `Example ex:z2-holonomy`.
- The 08-12 PROVE result (holonomy composition = ZS bridge, `2026-08-12-holonomy-composition-zs-bridge.md`)
  gives the *composite* classifier `Fun(𝔸(↓)⋈𝔸(↓'),Cat)` — a natural sequel section welding this Ch7
  climax to the Zappa–Szép chapter. Not written yet.
