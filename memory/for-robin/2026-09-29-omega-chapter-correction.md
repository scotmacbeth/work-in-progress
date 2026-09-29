# Skew-brace [Ω] chapter — corrective revision (WRITE 2026-09-29)

**File:** `papers/dossier/staging/app-skewbrace-omega.tex` (standalone build
`_standalone-omega.pdf`, 13 pp, compiles clean). Pushed to **work-in-progress
only** — NOT `\input` into `dossier.tex`, per WRITE.md and pending Neil's steer on
whether this is its own pillar chapter.

## Why the revision
The 2026-09-26 draft carried a **third theorem** claiming the internal residue
$[\nu]$ and the obstruction $[\Omega]$ are *independent coordinates*
($\mathrm{Ext}\cong R\times\Omega^0$). That was **refuted** — Rick's referee report
(2026-09-26) plus my from-scratch reproduction (2026-09-29). The argument was
circular: "read $\circ$ off from $+$ and $\lambda$" presupposes the very brace
whose existence is the question, and the *homogeneous* coupling being $\nu$-free
does not make *inhomogeneous* solvability $\nu$-free.

## What changed
- **Title**: dropped "independent of the internal residue".
- **Added an up-front correction box** in the intro putting the refutation on the record.
- **Theorem C** rewritten: independence → *residue-dependent solvability*. The new
  content is Rick's/my $o_\nu$: a group hom $o_\nu:H^2_+\to C^3/A(Z^2_\circ)$ with
  **$\operatorname{im}\varphi_+=\ker o_\nu$** [proved, trivial kernel, general $H$];
  the reverse inclusion *constructs* the cocycle (non-circular).
- **§2 setup**: fixed the block-triangularity overclaim. Admissibility of a residue
  is block-triangular; *solvability with that residue* is not. Flagged that $\nu$
  enters (c) twice for a non-trivial kernel (the $\nu\sigma(d)$ complement term).
- **New §5** (o_ν): operators $P,Q$, linchpin identity, main theorem, cross-validation
  ($\ker o_\nu=\operatorname{im}\varphi_+$ vs holomorph enumeration [computed]).
  Carries the surviving residue-invariance lemma and the "not a gauge-orbit product"
  negative (both still [proved]).
- **New §6** (explicit dependence): $|G|=8$ channel-1 ($\nu=1$ forces $[\beta]=0$,
  [proved]); $|G|=16$ three-way lock $4b\equiv2(\nu\sigma-1)\bmod 8$ [computed];
  torsor/no-basepoint for non-trivial kernel [computed]. The old $G_0/G_1$ corner is
  **reframed honestly**: it shows $[\Omega]$ is not a *function* of $[\nu]$ within one
  fibre — NOT independence (no $\sigma$ realises the full $[\nu]\times[\Omega]$ product).
- **§7 ledger**: refutation on the record; grades diffed against the registry.
- **Deleted**: old product theorem, split⊥residue corollary, "kernel non-triviality
  is orthogonal / ν never touches Ω" (that is exactly where the coupling bites), and
  the "one open step = residue surjectivity" (that was about the refuted product).

## Unchanged (KEEP)
Theorem A (identification, [Ω]=RY class, [peer-reviewed]) and Theorem B (bilinearity,
$W_4$ + heap-transport refutation, [proved]) — verbatim.

## Grades (matches registry `quiver-skew-brace-zs.json`)
A [peer-reviewed]; B [proved]; $o_\nu$ descent + $\operatorname{im}\varphi_+=\ker o_\nu$
[proved]; ker=im cross-val, $|G|=16$ lock, torsor [computed]; general-$H$/general-kernel
affine-torsor theorem **open**. Both citations (Ferri 2605.11903, Rathee–Yadav
2601.12371) at `deep-read` (citation_check footprint floor = deep-read).

## Still needs
1. **Neil's steer** (asked 2026-09-26, unanswered): own pillar chapter, or research
   thread feeding the ZS spine? Do not merge into the dossier until answered.
2. **Open proof target** for a PROVE session: general-$H$/general-kernel proof that
   $\operatorname{im}\varphi_+$ is an $o_\nu$-affine torsor with the offset identified
   intrinsically.
3. Once (2) settles and Neil steers, consider sending Rick the corrected chapter as a
   single pillar for review.
</content>
