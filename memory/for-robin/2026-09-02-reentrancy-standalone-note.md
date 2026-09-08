# Standalone Lean-verified re-entrancy note — pushed to wip

**Date:** 2026-09-02 (write session)
**File:** `papers/reentrancy-machine-checked-obstruction.{tex,pdf}` (7 pp, compiles clean)
**Repo:** `scotmacbeth/work-in-progress`, branch `main`, commit **`733b76b`** (supersedes `e6aaa75`)
**URL:** https://github.com/scotmacbeth/work-in-progress/blob/main/papers/reentrancy-machine-checked-obstruction.pdf

## What it is
The standalone note Rick recommended: split the **Lean-verified** ZS re-entrancy result out on its
own, with the machine check as the load-bearing artifact. It is NOT a re-write of the admissibility
paper (still out to Rick, untouched) and NOT a duplicate of `containers-for-orchestration.tex`.

## The one inversion that justifies a separate note
- `containers-for-orchestration.tex`: proves `[ω]=ε` **analytically**; Lean is a corollary cross-check.
- **this note**: the Lean file `Reentrancy.lean` (sorry-free, no Mathlib) is the deliverable. The note
  quotes its actual theorems verbatim — `phi_omega : phi (omega ε) = ε` and
  `omega_inB2_iff_zero : InB2 (omega ε) ↔ ε = false` — and draws the verification boundary explicitly:
  Lean certifies the **finite 𝔽₂ class computation** (complex → `[ω]=ε`); the **reduction** of the
  categorical obstruction to that complex stays cited pen-and-paper (`analytic` note, Prop 3.1).

## Honesty ledger (all per WRITE.md binding constraints)
- ZS-from-distributive-laws = **Ahman–Uustalu 2013** (Progress in Informatics 10, DOI
  10.2201/NIIPI.2013.10.2); they build no obstruction theory — `[ω]∈H²` is the clean delta.
- The total/partial "lens" is **demoted to one paragraph** (§5): named as Gerstenhaber
  absolute-vs-classified (Annals 79, 1964); the H¹ degree prediction is **retired**; no novelty claimed.
- Citation footprint floor = **deep-read** (`citation_check.py --report footprint`). No unsourced
  numbers: ℤ/2, `[ω]=ε`, `ω_T=(0,ε)`, `C²≅𝔽₂²` all trace to `Reentrancy.lean` + the analytic `.tex`.

## Status / next
- Not ready for `publishable-result` until Rick reviews (§4.2). No wip-push email per protocol §3.5.
- Open Lean target flagged in §5: formalise the **first mile** — orbit category, freeness (L),
  defect = (0,ε) — currently the pen-and-paper input.
