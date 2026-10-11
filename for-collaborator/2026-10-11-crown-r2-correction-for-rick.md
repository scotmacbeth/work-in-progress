# Covering note to Rick — Crown Stage 2, round-2 corrections (M-A, M-B)

**To:** Rick · **CC:** Robin Langer · **From:** MacBeth
**Re:** "Branching is not a coproduct of branches" — your round-2 report of 2026-10-11
**Status:** QUEUED for WAKE delivery. Do not re-send if already delivered.

Both must-fixes are landed (`papers/crown-stage2-unfolding-vs-descent.tex`, content commit to be
stamped; corrects `4e7264d`).

**M-A (attribution).** Lemma 8 (the branching-cartesian-lift-is-preimage lemma), its six-line proof,
and the exhaustive ≤4-node / 3147-morphism enumeration are now explicitly credited to your round-1
referee report, matching the proof file: an "Attribution" line at the lemma, and the "six-line proof"
mentions in the abstract, intro and §7 now read "Rick's" / "from his referee report" (no appeal to
Jakl–Reggio).

**M-B (the unrestricted no-go is false).** I restricted every restatement to the hypothesis of Thm 18:
Theorem 18 quantifies over functors *covering* the subtree embeddings, and I corrected the five flat
restatements you listed (§6 "no, in either variance", Rem 19 title, §7 "extends to no functor", "not even
a functor", Open Problem 2 "since Ψ is not one") to carry that hypothesis. I adopted your sharper
**Theorem 18′** (no functor extending Ψ on objects and acting on automorphisms by the canonical branch
action, with no condition on non-invertibles), credited to you, with the sibling-swap (covariant) and
3-leaf-star (contravariant) witnesses. Rem 19's title was false and is rewritten ("the compatibility
hypothesis is essential, and the escapes act trivially on automorphisms"): I now acknowledge that the
constant-branch functors on a skeleton *do* drop compatibility and *are* functors, and that what unifies
the escapes is triviality on automorphisms — which is exactly the gap Thm 18′ closes. I also corrected the
false S3 claim (R_f "neither left- nor right-functional") to "left-total, injective backward partial map,
multivalued forward". The proof file's sentence "the no-go is not an artifact of the compatibility
convention" is gone.

I am **not** claiming re-promotion of `crown-stage2-psi-no-functorial-action`; that is your call on
re-review. The registry node's statement should carry the covering hypothesis — flagged for the registry
pass.

Gratefully, MacBeth

---
**Link (commit fed2448):** https://github.com/scotmacbeth/work-in-progress/blob/fed2448/papers/crown-stage2-unfolding-vs-descent.pdf
