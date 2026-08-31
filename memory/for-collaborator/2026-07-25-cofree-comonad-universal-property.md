# Cofree comonad universal property — container-coordinate proof (2026-07-25)

**For:** Neil, Robin. **File:** `proofs/2026-07-25-cofree-comonad-universal-property.md`.
**Registry:** `proofs/registry/cofree-comonad.json` (status: proved, validates).

## One-line
Proved, in container coordinates, the **couniversal property of the cofree comonad** `𝔠_p` on a
container `p` — the exact dual of the free-monad UP I proved 2026-07-24. Together they give both
halves of the Ch. 4 "Monads and Comonads" adjunction story: `F ⊣ U` (free monad) and `U ⊣ 𝔠`
(cofree comonad), both spelled out in coordinates that Niu–Spivak / Spivak state only abstractly.

## What is new vs. cited
- **Cited (prior art):** the construction and the theorem — Niu–Spivak Prop 8.18/8.33/Thm 8.45;
  Spivak 2202.00534 Eq. (244)–(249). I direct-read (244)–(249) this session (lines 3801–3853) to
  discharge the "verify the recipe before it's load-bearing" flag: carrier = M-type of `p`-trees,
  positions = **vertices** (all finite rooted paths), fixed point `𝔠_p≅(p◁𝔠_p)×y`, `U⊣𝔠`.
- **New (my contribution):** the coordinate proof — the counit `ε_p` (read-root), the induced
  comonoid morphism `ĝ` by corecursion, and the discharge of (a) `ĝ` is a comonoid morphism, (b) the
  triangle `ε_p∘U(ĝ)=g`, (c) uniqueness — each against a *given* comonoid `D`.

## The structural punchline (worth a sentence in the grant/book)
The couniversal property **reduces to the five directed-container laws D1–D5 of the source `D`**,
split cleanly:
- forward (shape) components ← D1 (base), D4 (step);
- backward (position) components ← D2 (base), D5 (step);
- triangle ← D3.

And the free↔cofree duality is exactly **W-type/M-type on shapes, leaves/vertices on positions**.
The one asymmetry: the shape layer goes from induction (free) to **coinduction** (cofree, via
finality of `tree_p`), but the *position* layer stays **finite induction on both sides** — because
positions are vertices = finite rooted paths. This is precisely why getting "positions = vertices,
not leaves" right (an error I'd made and corrected) matters: leaves are not closed under the
path-prefix `⊕` the backward proof runs on, so the dual proof would not even typecheck with leaves.

## Extension corollary
`⟦𝔠_p⟧(A) = Σ_{t}(vtx(t)→A) ≅ νZ.(A×⟦p⟧Z)` — the cofree comonad on `⟦p⟧` (labels at every vertex).
Two independent justifications: the direct vertex count, and `⟦−⟧` preserving the ω^op (connected)
cofree tower (strong monoidal + connected-limit preservation, Ch. 3).

## Verification
`scratch/cofree_up_verify.py` — concrete non-degenerate `D` (walking-arrow category `X→Y`), `p`,
nontrivial `g`; corecursion, triangle, Lemma U, Lemma S, the comonoid-morphism law assembled a
second independent way via the `◁`-on-morphisms formulas, counit compat, and uniqueness-backward,
all to path length 4; three negative controls fire. RESULTS: see §8.1 of the proof file.

## Honest gaps
1. Construction + theorem are prior art (cited, not claimed).
2. **Finality** (existence of `ĝ₁` and uniqueness-forward) is the one genuinely coinductive
   ingredient — cited (Lambek/Barr/Spivak (249)). Everything else is finite induction.
3. **Not yet Lean:** `ĝ₁`/finality need M-types/coinduction, absent from Lean 4 core — the infra
   block noted in PROVE.md. But the entire **backward/position layer** (Lemmas U, S, triangle,
   uniqueness-backward) is finite induction and *is* portable now: a natural partial LEAN target
   dual to `FreeUniversal.lean`. **Question for Neil:** do we want to pursue M-types in Mathlib
   (`PFunctor.M` exists and matches the tower — I cross-checked) to close the shape layer, or keep
   the cofree LEAN scoped to the portable backward half for now?

## Where it feeds
Ch. 4 "Monads and Comonads" — the cofree section's couniversal-property statement (WRITE target).
Grant: completes the comonad/coalgebra half of the compositional-correctness story (applications =
directed containers = comonads; cofree = the universal behaviour/interaction tree).
