# Revision scratch — containers-for-orchestration.tex (2026-07-20 write session)

Task: honesty-and-framing surgery per ~/state/WRITE.md. NOT new math.

## Provenance audit (from memory/reading/sources.json, field `extraction`)
- 2604.01303 Aberlé — **deep-read** ✓ (cite prominently)
- 1604.01187 Ahman–Uustalu "Directed Containers as Categories" — deep-read ✓, title CORRECT in bibitem
- 2312.00990 Niu–Spivak — deep-read ✓
- 2202.00534 Spivak Reference — verified-quote ✓
- 2607.15091 Comonads as Spaces — deep-read ✓
- 2606.01663 / 2605.11204 / 2605.01879 sheaf-MAS trio — all deep-read ✓
- 1512.03250 Pirashvili — deep-read ✓
- **2605.12239 ArchAgents (Banu) — agent-summary ✗ BELOW FLOOR. Do NOT cite as reference.**
- **2607.04240 "Biological Motifs for Agentic Control" (Banu) — deep-read ✓.** Same author,
  same programme (operad + wiring-diagram algebra, promoters-as-lenses); PDF read in full,
  EXPLICITLY checked for ZS/distributive-laws/semidirect — NONE. This is the citable anchor
  for the "parallel operad-assembly axis, orthogonal to our sequential C⋈D" differentiator.
- rw (Rosebrugh–Wood JPAA 175, 2002), bw (Baues–Wirsching JPAA 38, 1985) — classical journal,
  no arXiv ID, standard refs (come through gobstr note).

DECISION on ArchAgents: WRITE.md item 3 names 2605.12239, but it sits at agent-summary. Anchor
the differentiator on the DEEP-READ companion 2607.04240 (carries the exact load-bearing fact:
operad/wiring-diagram composition, no distributive laws). Name Banu's programme; do not add the
agent-summary bibitem. Flag in handoff: a future browse-session deep-read of ArchAgents would let
us name it directly.

## Grade of the delta: PROVED (registry orchestration-zs.json status=proved, closed 2026-07-20)
- PROVED (analytic): the dichotomy on the token family K_ε — C⋈D exists iff ε=0; [ω(K_ε)]=ε·gen
  in H²(Sk_C;𝒟)≅Z/2. Source: proofs/2026-07-20-orchestration-reentrancy-obstruction-analytic.tex.
- COMPUTED context (keep, mark as such): the two extra table regimes (independent product; S₃ dihedral).
- NOT claimed: named production framework literally = K_ε (that's the validation ask).

## Structural edits
1. **Aberlé prominent + reframe.** New intro subsection "Prior art: the mechanism" (by p.2) stating
   poly=interface, free-monad-Kleisli=implementation composed along wiring diagrams (Thm 3.1),
   dependent-poly=spec/Hoare (Thm 5.3), strict-monoidal π:Spec→Int (Def 7.1) — ALL Aberlé; our
   theorem-proving & orchestration rows are a DOMAIN REINTERPRETATION; he flags tactics as future work.
   Trim the soft dictionary remark accordingly; upgrade the dictionary provenance column.
2. **§4 rewrite to the analytic proof.** Parametrize by ε; [ω(K_ε)]=ε·gen uniformly. Demote the
   rigid-twist iso + brute-force SFS to independent cross-checks (not load-bearing). Grade PROVED.
   Keep 4-regime table; mark independent/S₃ rows computed.
3. **ArchAgents differentiator** → one sentence in §5 (degree axis / related work), cite 2607.04240.
4. **Intro "result"/abstract**: dichotomy is proved; add Aberlé to the prior-art clause.

## Compile: pdflatex ×2 (amsart), no errors. Run footprint-style check on cited IDs afterward.

## DONE (session close)
All edits applied; pdflatex ×2 clean, 10pp (was 8pp). No undefined refs/citations.
citation_check footprint → floor deep-read. Removed Proposition prop:bug (folded into
parametrized Theorem thm:h2). Handoff note: memory/for-robin/2026-07-20-orchestration-note-revised.md.
PROGRESSIVE_DISCLOSURE.md entry updated (computed→proved, Aberlé reframing).
Delivery: projects volume (not a git repo; no email this session per WRITE rules).
