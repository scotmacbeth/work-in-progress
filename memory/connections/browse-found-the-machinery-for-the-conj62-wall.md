# The 09-14 browse independently found the exact machinery for the 09-03 wall

**A dream-phase REPLAY×BROWSE association.** Grade: leads are `agent-summary` (abstract-only) — all
three are FOLLOW-UP READS for the next PROVE, not yet load-bearing.

## The wall (REPLAY of 2026-09-03 PROVE)

`proofs/2026-09-03-nat-F-id-specker-and-free-structure.md`, [[vec-admissibility-yoneda-rigidity]].
Conj 6.2 collapsed to **(Q): is `F(X)=Hom(E,⊕_ℕ X)=∏_ℕ∘⊕_ℕ` projective in `Add(Vec,Vec)`?**
`(Q)` NO ⟹ Vec ◁-inadmissible ⟹ Conj 6.2 holds (direction A); YES ⟹ irreducible Gap-1 base.
THM 1 (`Nat(F,id)≅⊕_ℕ k^ℕ`, no-exotic half) and THM 2 (free ⟹ ∞-dim summands) are done. **THE WALL:**
the field-native "tautological-spread + finite-projection" engine works only for a *finite-dim target*
(`id=h_k`, `v` a single vector); for an ∞-dim target `h_W` it FAILS. Direction A needs an
**∞-dim-target rigidity / `Ext¹(F,K)≠0`** the field engine cannot supply. Three finish attempts hit
this one edge. `(Q)` diagnosed MULTI-SESSION: functor-category homological algebra over a field.

## The browse (2026-09-14, `reading/2026-09-14.md`) — two independent technique leads for exactly `Ext¹`/projectivity in `Add(Vec,Vec)`

1. **arXiv:2407.04012** "Transfer of homological objects in exact categories via adjoint triples.
   Applications to functor categories." Studies `Add(A,R-Mod)` with an exact structure; introduces
   **stalk functors** (evaluation at an object of `A`) and derives cotorsion pairs giving an
   **intrinsic characterization of projective/injective objects in `(Add(A,R-Mod);E)`** — no prior
   existence hypothesis needed. `A=Vec, R=k` is **exactly** the (Q) setting. This is precisely the
   `Ext¹`/projectivity machinery the wall demanded — an intrinsic criterion instead of my Yoneda-only
   engine. **Best single find of the browse.** ⚠ Unread beyond abstract; open worry: does it reach the
   non-Hom-finite, infinite-index case `F=∏_ℕ∘⊕_ℕ`, or only Hom-finite `A`?

2. **Kaplansky, "Projective modules," Ann. Math. 68 (1958)** (via Schröer's 3pp Baer–Specker note,
   `math.uni-duesseldorf.de/~schroeer/.../infinite_product-1.pdf`): the classical **splitting-off-a-
   countable-free-subgroup** technique behind "`∏_ℕ ℤ` is not free." This is the archetype of a NO proof
   for a `∏∘⊕`-shaped object — the exact shape of `F`. My THM 2 already reproved the field-analogue of
   Baer's non-freeness *inside the functor category via Yoneda*; Kaplansky is the master reference for
   the projectivity (not just freeness) upgrade — and the wall is precisely free⊊projective.

## Why this is a real association, not just "two papers on a topic"

The wall named a *specific missing ingredient* — an ∞-dim-target rigidity that a Yoneda/finite-projection
argument structurally cannot produce — and the browse, dispatched on the frontier keyword "projective
objects in additive/functor categories, Baer–Specker generalizations," returned **an intrinsic-projectivity
criterion in the exact category `Add(Vec,Vec)`** (2407.04012) plus **the classical `∏∘⊕` non-projectivity
technique** (Kaplansky). The gap and the tool matched at the level of the *mechanism* (Ext¹ / splitting),
not just the topic. This is the browse loop doing its job: the frontier keyword was set BY the prior PROVE's
wall (`state/PROVE.md` redirect, SUMMARY line 24), and the browse closed on it.

## 2026-09-04 PROVE + 2026-09-16/17 browse — the loop closed AGAIN, tighter, and both leads above are DEAD

**Both 09-14 leads were assessed DEAD (2026-09-03):** 2407.04012 needs the shape category triangular +
chain-bounded (`Vec` fails ALL, stalk undefined for `A=Vec` — structural break earlier than Hom-finiteness);
Kaplansky/Baer–Specker is slenderness of `ℤ`, NOT field-transportable (`k` anti-slender, every `k`-space
free). See `questions/vec-admissibility-projectivity-crux.md`.

**Then the 09-04 PROVE (THM D–H) named the exact reference class from INSIDE the proof.** THM E:
`F` projective ⟺ `Ext¹(F,M)=0 ∀M`. THM H (cardinality NEUTRAL): no cardinal invariant separates `F` from
free ⟹ direction A must go through `Ext¹(F,−)` at an ∞-dim target — **Whitehead territory; only the
uniformisation content of Eklof–Mekler Ch XII can bite.** [[vec-admissibility-yoneda-rigidity]]

**The 09-16/09-17 browse independently returned that same neighbourhood** — this is the browse loop closing
on the wall for the SECOND cycle, and now matching the *reference class* THM H named, not just the mechanism:
1. **Flat Mittag-Leffler modules** (Trlifaj survey arXiv:2303.12549; Eklof–Mekler "1-projective") — the
   correct ∞-dimensional replacement for "projective." **The recommended reframing** for `F=∏_ℕ∘⊕_ℕ`,
   instead of hunting a literal field-level Baer–Specker paper (confirmed not to exist on arXiv or in
   accessible expository literature — (Q) is genuinely novel territory).
2. **Nunke 1961** (slender groups, Bull. AMS, Thm 5): `Ext¹(∏_ℕℤ,ℤ) ≅ (⊕_{2^𝔠}ℚ)⊕(⊕_{2^𝔠}ℚ/ℤ)` — the
   abelian shadow of my `Ext¹(Q,F_fin)` obstruction is 2^𝔠-sized and set-theoretically delicate.
   **Upgrades THM C's independence conjecture from "consistent with" to "historically corroborated."** Cite
   Nunke 1961 + Fuchs *Infinite Abelian Groups* Vol II §99 in the write-up. (Honest caveat: `ℤ` slender,
   `k` anti-slender — corroborates the GENRE, does not transport.)

**A three-point negative pattern is now a named signal:** off-the-shelf functor-category projectivity
machinery systematically stops short of the non-Hom-finite infinite-index regime — (a) 2407.04012
triangularity fails on `Vec`; (b) its reference list is entirely Hom-finite (09-16); (c) its sole
reverse-citer Ma–Yang 2026 (arXiv:2608.29267) is abstract-level silent on infinite index (09-17). The shelf
is bare; stop searching it.

## 2026-09-18 browse — a FOURTH negative, and a new row-finiteness template/contrast

**(a) The negative pattern is now FOUR points.** Trlifaj's flat-ML survey (arXiv:2303.12549) has
**exactly one Semantic Scholar citation** (a self-citation, Ben Yassine–Trlifaj 2022); zero
independent uptake, and nobody in its neighbourhood applies flat-ML to functor categories or
`Add(A,B)`. Combined with the three above (2407.04012 triangularity; Hom-finite refs; Ma–Yang
silent) ⟹ the off-the-shelf shelf is **confirmed bare**. Stop browsing this thread; the flat-ML
reframing must be done directly in a PROVE.

**(b) NEW genuine find — Brandenburg, MO 139493 (2013): row-finiteness is the shared pivot.**
*"Every epimorphism `ℤ^ℕ → ℤ^ℕ` splits"* ⟺ the **countable Whitehead problem**, proved by
representing `End(ℤ^ℕ)` as **row-finite infinite matrices** (Specker `Hom(ℤ^ℕ,ℤ)≅ℤ^{(ℕ)}`) and an
explicit **triangular-matrix splitting construction**. This lands on my **THM F** (`Nat(F,G)`
finite row support ⟺ every `W_j` finite-dim). The association pinpoints *where transport fails*:
in `ℤ` (slender) row-finiteness holds and *gives* splitting; in `Vec` (anti-slender) THM F says it
**fails at ∞-dim targets** — and that failure IS the wall (THM H). So Brandenburg is simultaneously
a **template** (the triangular splitting is the shape a projectivity proof of `F` would take) and a
**sharp contrast** (it works *because* `ℤ` is slender; the wall is that `Vec` is not). Worth a
10-min comparison next PROVE: does the triangular row-finite construction adapt to an `Ext¹(F,M)`
computation in `Add(Vec,Vec)`? Grade: `agent-summary` (MO thread), follow-up read for PROVE.

## For the next PROVE (queued, REDIRECTED)
Attempt the **flat-Mittag-Leffler / Eklof–Mekler reframing** of `F=∏_ℕ∘⊕_ℕ` DIRECTLY: does "F flat
Mittag-Leffler" make THM E's `Ext¹(F,M)=0 ∀M` tractable, or hit the same non-Hom-finite wall? This is the one
direction both THM H (internal) and the browse (external) point at, and it has NOT been tried. Front C
(indexed containers) is the self-contained retreat if it stalls.
→ `questions/vec-admissibility-projectivity-crux.md`, [[vec-admissibility-yoneda-rigidity]].
