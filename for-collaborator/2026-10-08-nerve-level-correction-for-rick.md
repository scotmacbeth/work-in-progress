# Covering note — corrected note, re-review requested

**To:** Rick (grandparick20@gmail.com), cc Robin
**From:** MacBeth
**Re:** your referee report UID 209 on *"Composition is a degree-two datum"* (ae9d67a)
**Date:** 2026-10-08
**Status of this note:** DRAFT covering note — the covering **email** is queued (this was a
write-session; email is out of scope here). Send on next wake/comms pass.

Rick — thank you. The central refutation was exactly right and the fix is clean. The headline was
off by one, and the cure is to grade by **nerve level**, not cohomological degree.

## What changed

New file (supersedes, does not delete, ae9d67a):
- `papers/composition-is-a-nerve-level-two-datum.{tex,pdf}`
- content commit **242c7ea** (stamped), pushed to `scotmacbeth/work-in-progress` at **da7ebd3**.
- consumes the new proof `proofs/2026-10-08-nerve-level-tower.md` (registry
  `composition-nerve-level`, proved) for the regrade lemma, the strict floor separation, the
  2-coskeletal collapse, and the assembly separation.

**The one conceptual fix.** A class carries two simplicial indices: an n-cochain is a function on
N_n, but its cocycle condition d^n c = 0 is tested on N_{n+1}. Hence
`cohomological degree = (nerve level of the cocycle condition) − 1` (Lemma 1). δ lives on composable
PAIRS = N₂ — read already by an H¹ cocycle condition. So composition is first seen at **degree one**,
not two; the weld [ω]∈H² reads N₃ = associativity.

**The honest ladder** (your recommendation, adopted verbatim):
- DETECTION: two rungs only — N₁ (U-blind, degree 0) ⊊ N₂ (composition-sensitive). Strict and proved
  (Z/2 vs {1,e} at H¹ over 𝔽₂; your script's (1,1,1) vs (1,0,0)).
- Within N₂: [θ_R]∈H¹ and [ω]∈H² are two **independent** anchors, differing in coefficients and
  condition-level, not in whether they see composition.
- N₂⊊N₃ is a **condition-level / assembly** fact (associativity), NOT a truncation separation of
  fixed categories — a category IS its tr₂ nerve (Thm, 2-coskeletal collapse).
- OPEN, flagged: does cohomological *degree* stratify *detection* above the floor? No as naively
  stated (degree-1 counterexample); the honest grade is nerve level.

## Your correction list — disposition

All 5 errors, 9 wording, 7 minor addressed. Highlights:
- **E1** headline/slogan/§7 regraded by nerve level. "No invariant below degree two can detect
  composition" is gone; replaced with the two-index story and the OPEN question.
- **E4** Lanfranchi Thm 4.20 quoted with "given a group object" restored; Def 4.18 attributed to
  Cruttwell–Ikonicoff–Lemay–Van Der Linden; the port flagged as ours.
- **E2/E3** the two false "cannot" claims replaced (invariance under changing δ on fixed p;
  class-level argument via the two witnesses: 0 ↦ nonzero is impossible).
- **W3** promoted from footnote to the central Lemma 1 (regrade).
- **W4** "different degrees ⇒ independence" removed; transgression/Bockstein acknowledged;
  independence is the content of the witnesses.
- **W7** Aut(a) restated as the non-abelian H¹ class of the (faithful) regular representation,
  vanishing iff Aut(a)=1 — not an "H² class".
- **W9** "first clean instance" withdrawn; Kirchhoff/HodgeRank/Ghrist cited for the mechanism; the
  stylized-transport caveat added.
- **M1–M7** sign, torsor/H¹(S;A), cochain renamed τ_f, surjectivity fix in Thm (δ-translation),
  BN not BZ, W = Z[ε]/ε² fixed, rigid-twist category defined.

**Flag for you:** the HodgeRank (Jiang–Lim–Yao–Ye, Math. Program. 2011) and Ghrist (*Elementary
Applied Topology*, 2014) pointers come from your report, not my own deep-read; I've cited them for
the internal/Strathclyde note but they want independent verification before any external version.

Re-review welcome. This is the version Neil should use for the mini-course (Oct 13–16).
— MacBeth
