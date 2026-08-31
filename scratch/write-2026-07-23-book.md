# Write session 2026-07-23 (book) — Chapter "Monads and Comonads"

## Task (from WRITE.md)
Promote & expand book §7.1 (free monad + cofree comonad, lines 1810–1892 of
`books/category-of-containers.tex`) into a full chapter "Monads and Comonads", per
Neil's 07-23 three-milestone spec.

## Placement decision
Insert new chapter **immediately after Ch5 (Comonoids: DCont ≅ Cat), before Ch6 (Zappa–Szép)**.
Rationale: WRITE.md + Neil — "belongs right AFTER the comonoid/DCont chapter"; the cofree
comonad IS a directed container, so it lands back on Ch5's equivalence chain — narrative
continuation. Renumbers ZS→7, Phase-2→8 (all refs by label, auto-resolve).
Gut the free/cofree §7.1 out of the Phase-2 chapter, leave the derivative stub + a pointer.

## M1 (initial algebras / accessibility) placement
Neil wants M1 in a **Preliminaries chapter**, not the new chapter. Book has NO prelim chapter yet.
Compromise: open the new chapter with a TIGHT preliminaries section "The tools we borrow"
(initial algebras μF, final coalgebras νF, accessibility, the T_F/D_F formulas) framed as
borrowed machinery, cited (Adámek; AAG). **Question for Neil** (put in email/scratch): relocate
to a real Preliminaries chapter when you fix global structure? For now self-contained.

## Provenance discipline (honesty)
- Free-monad **construction + ◁-monoid laws**: construction = prior art (Gambino–Kock 0906.4931
  [deep-read]; AAG 2005 W-types). Explicit container-coord ◁-monoid laws = MacBeth, Lean-checked
  `Free.lean` (zero sorry, Quot.sound-only, NOT committed to repo tree → footnote per Preface
  convention, tag [MacBeth]).
- Free-monad **Lemma (universal property)**: theorem = Gambino–Kock Thm 4.5 (prior art). Container-
  coordinate proof = MacBeth (proofs/2026-07-24-free-monad-universal-property.md, graded `proved`).
  Partial Lean: `FreeUniversal.lean` = triangle + unit + object-uniqueness machine-checked; MULT-hom
  law + backward-uniqueness NOT yet Lean. Tag [Cited: G–K 4.5] + footnote grading the coord proof.
- Cofree comonad + laws: **STRIP novelty tag** (was [MacBeth] on thm:cofree-dircont l.1873).
  Cofree side = **Niu–Spivak 2312.00990 Prop 8.18/8.33/Thm 8.45 [deep-read] PRIOR ART**. Directions
  = ALL nodes/vertices (book text already correct: P^∞ = finite paths from root = nodes). Proof
  object (explicit o/↓/⊕ in D1–D5 form + small-case verification) = MacBeth.
- Cofree **Lean**: `Cofree.lean` BLOCKED — core Lean 4, no PFunctor.M / no coinduction (M-type).
  Note in-progress, pending Mathlib (Robin infra). NO Lean tag for cofree.

## Citation floor
All new cites at deep-read: G–K 0906.4931, Niu–Spivak 2312.00990, AU 1604.01187, ACU14 (classical).
Do NOT add new citations to 2405.13157 (SS2405, agent-summary — pre-existing debt, DCont chapter only).
Run `citation_check.py --report footprint` on the file before finishing.

## Chapter promise (ONE sentence)
Every container has a free monad (its language of terms) and a cofree comonad (its space of
behaviours); both are again containers with computable shape/position data; the free monad is the
universal monad on the container, and the cofree comonad is a *directed container* — a small
category, the subtree category — so behaviour lands back on the equivalence chain.

## Section arc
1. Hook (signature → language vs behaviour) + promise + landscape (two adjunctions).
2. The tools we borrow: μF, νF, accessibility, T_F=μY.(X+FY), D_F=νY.(X×FY). [cited, tight]
3. W-types and their duals: W S P = μY.(S,P); exist in Set; dual ν(S,P) via connected-limit
   preservation (REUSE Ch3 thm:char); inductive-families remark.
4. The free monad of a container: m_(S,P)=(S',P'); trees & leaves; grafting monoid; cite Free.lean.
   Example: Maybe, binary.
5. The free-monad Lemma: F ⊣ U; α, ĝ; ⟦−⟧ strong monoidal + ff ⟹ ⟦m_X⟧ = free monad on ⟦X⟧.
   Fold in PROVE result. G–K 4.5 anchor.
6. The cofree comonad; cofree = cofree directed container. Niu–Spivak. Subtree category. Link Ch5.
7. Connections: syntax/behaviour pair; grant; open (cofree Lean blocked; the comonad-→-category
   specialness).

## Draft-book revision lenses to run after: promise&arc / examples&diagrams / reader / cut.

## STATUS — COMPLETE (2026-07-23)
Chapter drafted, revised, compiles clean (48pp, exit 0, 0 new overfull, no undefined/dup refs).
Revision fixes made: landscape adjunction display X→C consistency + correct cofree side
`Comon(D,C^∞)≅Cont(UD,C)`; "largest comonad it dominates"→"mapping to it"; Barr cite honesty
(free-monad only, cofree dual); free-monoid prov tag softened to `[MacBeth]`+footnote (no bare
"machine-checked" in main text, per Preface); Phase-2 chapter range fix. Citation footprint run:
floor `agent-summary` = pre-existing 2405.13157 only; my cites (G–K 0906.4931, NS 2312.00990) deep-read.
Deliverables: PROGRESSIVE_DISCLOSURE updated; collaborator note
`memory/for-collaborator/2026-07-23-monads-comonads-chapter.md`; memory node
`book-ch6-monads-comonads-drafted`. NO email/PR (write-session rule + book off-GitHub).
Also compacted MEMORY.md index 20.1KB→15.8KB (hook-triggered).
