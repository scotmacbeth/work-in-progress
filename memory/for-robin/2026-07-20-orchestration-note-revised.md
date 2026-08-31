# Revised: containers-for-orchestration.tex (Aberlé reframing)

**File:** `projects/papers/containers-for-orchestration.tex` (+ `.pdf`, 10pp, compiles clean, amsart).
**Session:** write, 2026-07-20. Revision forced by the 2026-07-21 Aberlé deep-read (arXiv:2604.01303).

## What this is
The grant-Impact note now sits *honestly on top of* Aberlé's framework instead of implicitly
re-claiming its mechanism. The surviving delta — composing two shared-resource orchestrations =
a Zappa–Szép product `C⋈D`, obstructed by `[ω]∈H²(Sk_C;𝒟)`, re-entrancy = nonzero gen ℤ/2 — is
now the clear spine, and it is graded **proved** (the registry promoted `orchestration-zs`
computed→proved on 2026-07-20; the note follows the analytic proof).

## Changes made
1. **Aberlé, prominent + specific.** New intro subsection "Prior art: the interface/implementation
   mechanism" (lands on p.2): poly=interface, free-monad-Kleisli=implementation composed along
   wiring diagrams (Thm 3.1), dependent-poly=spec/Hoare (Thm 5.3), strict-monoidal π:Spec→Int
   (Def 7.1) — all attributed to Aberlé. Added *implementation* and *specification* rows to the
   dictionary table crediting him; sequential row now credits him for the free-monad implementation
   structure (Lean grafting-laws remain our machine-checked addition). Abstract acknowledges the
   mechanism. Our theorem-proving / orchestration rows are framed as *domain reinterpretation*.
2. **§4 rewritten to the analytic proof.** Parametrized family `K_ε`; single Theorem 4.1
   `[ω(K_ε)]=ε·gen`, so `C⋈D` exists iff ε=0. Enumeration (#SFS) and the rigid-twist isomorphism
   are demoted to independent cross-checks (a remark), not load-bearing. The two extra table
   regimes (independent product, S₃) are explicitly marked **computed illustration**, not part of
   the proved dichotomy. "Status, honestly" and the abstract updated accordingly.
3. **Banu differentiator** added in §5 (degree axis): operad/wiring-diagram parallel skill-assembly,
   no distributive laws — orthogonal to our sequential two-party interleaving.
4. Bibitems added: `analytic` (the 07-20 proof note), `banu`. AhmanUustalu title confirmed correct
   ("Directed Containers as Categories", 1604.01187).

## One decision you should know about (honesty)
WRITE.md item 3 named **ArchAgents, arXiv:2605.12239** for the differentiator, but that entry is
only `agent-summary` in sources.json — below the citable floor for a paper. I anchored the
differentiator on the **deep-read companion, arXiv:2607.04240** ("Biological Motifs for Agentic
Control", same author, same programme), which was read in full and *explicitly verified* to contain
no distributive-law / Zappa–Szép structure — exactly the load-bearing fact. So the differentiator
stands on deep-read ground and I did **not** add the agent-summary bibitem.
→ *If you want ArchAgents named directly, a future browse session should deep-read 2605.12239;
then we can cite it too.*

## Provenance
`citation_check.py --report footprint` → **floor: deep-read** (all cited arXiv IDs deep-read or
better; verified-quote for the Poly Reference). Clean.

## Still open (not this session's job)
- The "real deployed framework literally = K_ε" claim remains a *computed* reading (the validation
  ask): needs one concrete orchestration framework exhibited as a directed container + an explicit λ.
- Open direction flagged in §6: comonads generalise both DCont and cellular sheaves (Fairbanks–
  Carlson–Spivak, "Comonads as Spaces", 2607.15091) → possible single comonadic invariant unifying
  the H²(handoff) and H⁰/H¹(communication-graph) pictures. Held at deep-read; worth a prove session.
