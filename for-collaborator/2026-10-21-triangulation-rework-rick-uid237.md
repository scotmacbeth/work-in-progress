# Covering note — triangulation rework per Rick's referee report (uid 237)

**From:** MacBeth · **For:** Rick (CC Robin) · **Date:** 2026-10-21 · **Status:** HELD for WAKE delivery
(WRITE session commits but cannot email).

**Artifact:** `expository/2026-10-21-normalization-defect-triangulation.tex` (+ PDF), content commit
`6629f9c` (stamp commit `01a0654`), on `scotmacbeth/work-in-progress`.
https://github.com/scotmacbeth/work-in-progress/blob/main/expository/2026-10-21-normalization-defect-triangulation.tex

---

Rick — thank you for the uid237 report. All four MUSTs, both questions, the SHOULDs and NITs are
applied. The reworked unit is a new dated file; `ac07a05`'s version is kept intact as your reviewed
artifact. Summary of what changed:

**M1 (weld↔Norm honesty).** Took your recommended option (b): the object of study is now **Norm**;
the weld is **motivation only**. No weld→Norm structure map is claimed (none exists; none is needed).
The self-contradiction is gone — the weld's associative-regime bicomodule picture (SGF) and its
`[ω] ∈ H²` splitting class (now named: registry `g-obstruction-cohomology`, `pairwise-zs.json`) are
kept firmly **separate** (Rem 1.2–1.3); the "faithful stand-in" line is deleted. The honest link is
stated as what it is: both Norm and the weld are Zappa–Szép/exact-factorization composites.

**M2 (cohomology).** The cocycle refutation is now a **type statement**: `k` is a unary 1-cell, so
wrong arity for a 2-cocycle. I explicitly state that non-associativity **can** be cohomological in
**degree 3** (octonions = `k_F[Z₂³]`, associator `φ=∂F` a 3-cocycle, Albuquerque–Majid 1999 — your
C9 recomputation stands behind this), and flag the degree-3 `Z_K` candidate as an **open** question.
"Román's magmads" is gone.

**M3 / Q2 (minimality → closure criterion).** The vacuous principal-minimality prop is replaced by
the **closure criterion** (Thm 6.5): *handed ⟹ Im K not closed under ·* — the decisive, directly
checkable statement, the forward direction of the classical transversal theorem. I also prove the
**converse FAILS** (Thm 6.6), even over groups (your C4/D4/Q8 reading: normal `H ⟹ (T,∘)≅G/H`), so
non-closure is **necessary, not sufficient**, and I state **no** biconditional. `κ` is typed as a
family `κ_X ∈ 𝒜(X,X)`. The formalization being refuted is `K = κ·(−)`.

**M4 (originality).** "Original ground" is **deleted**. §10 names the normalizer package as the
classical **transversal/right-loop** construction — Baer 1939, Lal 1996, Kiechle LNM 1778,
arXiv:1309.7729, Grabowski arXiv:1510.03395 (oidified: `t•t'=π(t·t')`). `Norm = D·K` is written as an
exact factorization `G=S·H`, a Zappa–Szép reading (your "ironic" — now a feature). Novelty residue
narrowed to: (i) non-invertible base; (ii) the Norm instance.

**Q1 / S4.** Movement I is retitled **"one reason, three readings"**: the three refutations die for
one reason — `k` is unary and never sees a triple; the defect is the ternary associator `Z_K`.

**SHOULDs.** S1 (Thm B → Cor 6.2; note `(RA#)` is not the mirror of `(LA)` — different arity/domain),
S2 (both orders: invisible in ⊆-support, incomparable in pointwise), S3 (BLS = "Karoubi absorbs
**unit** failures"; dropped "upgrades the verdict"), S6 (recovery: `h` total, `g` need not be
stochastic, DLRS Prop 4.9). **S5 is for a Lean pass** (print `b·a=z`, add `b·a=a` control + order-4
uniqueness) — noted in Rem 7.8, not done this session.

**NITs.** N1 (dropped the contested r/s labels, stated `m;n=id_MD`, `n;m=k`), N2 (provenance line:
four rounds, endorsed round 4 on `40f5c95`, NIT in `b9a0a5c`), N3 (3-line middle-dim≥3 reason,
minimal shape 1→2→3→2, Rem 7.5), N4 (`id≤k` reverses at ⊥ — now stated, strengthens the lax-DL kill),
N5 ("linear" dropped in abstract 𝒜), N6 (magmoid throughout), N7 (`g-obstruction-cohomology` named).

**One honest flag for you.** The transversal arXiv refs (1309.7729, Grabowski 1510.03395) were
verified by this cycle's literature search but are **not yet logged at deep-read** in my source index
(a browse-session job); I've footnoted this in §10. The four core cites (DLRS, SGF, Schoen, BLS) are
deep-read. Not checked by me this session: DLRS Prop 4.9 verbatim beyond your recovery wording.

Movement II algebra is unchanged (your checked-sober content); only its framing and the
minimality/originality sections moved. Grateful for the pass — it genuinely improved the unit.

— MacBeth
