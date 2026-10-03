# Write scratch — "Toward a uniqueness theorem for the container derivative"

Date 2026-10-03. Follow-on to the 10-03 existence note
(`papers/container-derivative-tangent-structure.tex`). Positioning/roadmap note, 7–9pp.

## Phase 1 — The one sentence

> Among representable first-order tangent structures on **finite-support** polynomial
> functors, the AAGM container derivative is the only nontrivial one — because the
> solid-idempotent condition `|S|²=|S|` has only `{0,1}` as finite solutions — and this
> finiteness is sharp: at infinite support `ℕ·y` is a third solid structure.

## Honesty ceiling (from WRITE.md + registry)

- Root graded **computed**. Legs: rank-rigidity classification = **proved** (mine,
  airtight, Lean-certified arithmetic core, propext-only). Representability of ∂ =
  **proved** (via base-change result). Correspondence-CONVERSE (tangent ⟹ solid) =
  **ported** from L–L Thm 4.8, NOT reproved rig-internally. THE GAP.
- So the clean, airtight deliverable is: **classification of finite solid infinitesimal
  parts = {0, y}**. The uniqueness theorem is CONDITIONAL on the ported converse.
- Do NOT inflate. The abstract must say: we classify solid infinitesimal parts, establish
  representability, and REDUCE uniqueness to one ported step stated as an open problem.
- Qualified ceiling: "among representable first-order tangent structures on finite-support
  polynomials" — and representability of ∂ IS established, so that qualifier is earned.

## Phase 2 — Skeleton

1. Introduction — existence recalled; from existence to uniqueness; L–L template; what we
   prove (classification) vs what we reduce (uniqueness via converse); finiteness is sharp.
2. Preliminaries — containers, ◁, y; infinitesimal object + augmentation; D=y⊕M;
   representable tangent bundle T=(−)◁D; linear containers S·y. (Only what's used.)
3. The bundle and solid tensors coincide on the linear layer (Lemma 0). The linchpin.
4. Rank rigidity: freeness automatic over ℕ (Lemma 1); solid ⟹ |S|²=|S| (Lemma 2);
   finite ⟹ {0,1} (Theorem 1). PROVED. Lean oracle.
5. Finiteness is sharp: ℕ·y solid (Prop 2). The honest obstruction.
6. From solid parts to tangent structures: the correspondence (★), forward verified on
   primitives + Whitney-sum corroboration; the CONVERSE as the central open problem.
   Conditional uniqueness theorem.
7. Comparison with Lanfranchi–Lemay (table) + significance / Strathclyde.
8. Conclusion — what's proved, the one gap, routes to close it.

## Structural decisions

- Lead with the PROVED classification as the headline deliverable; frame uniqueness as the
  target we reduce to one step. This keeps the honest grading visible in the architecture.
- State the conditional uniqueness as a clearly-labelled "Theorem (conditional on (★c))"
  so no reader mistakes it for unconditional.
- Reuse macros from existence note (\SPoly, \Poly, \lhd via \lhd, \N, \DD, \sem).
- Infinitesimal part M=S·y linearity: FORCED by additive-bundle axiom, not assumed — say so.
- Table: L–L (PID, ring) vs this note (rig ℕ, cardinality rank) — the "cleaner than L–L"
  point (freeness automatic, no PID).

## Citations (all deep-read, verified in sources.json)

AAGM2003, BCS2009, CockettCruttwell2014, AhmanUustalu2016, GambinoKock2013, CCGZ2024,
LanfranchiLemay2025 (2505.09080). Existence note cited as MacBethTangent (internal).
Ikonicoff–Lanfranchi–Lemay operad paper: NOT in sources at deep-read → prose footnote only,
NO bibitem.

## Open problems to state precisely

(O1) The correspondence-converse: a representable first-order tangent structure T=(−)◁D on
     finite-support Poly forces its infinitesimal part M solid. (L–L vertical-lift
     universality, Thm 4.8, ported.) THE gap.
(O2) "Finite support ⟺ coexponentiable in (Poly,◁)" — Niefield analogue, intrinsic hypothesis.
(O3) Higher order / iterated tangents (Weil algebras ℕ[ε]/εᵏ, k≥3) — out of scope.
