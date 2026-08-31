# Write session 2026-08-11 (book) — State pole of the liftings classification

**Target:** book Ch (Monads & comonads / transfer), subsection `sec:liftings-are-categories`
(line 3546). WRITE.md: present liftings as ONE theorem, TWO solved poles, unified by
π₀(position-threading action). State completeness now PROVED.

## What already exists in the book
- `sec:liftings-are-categories` (3546–3695): Reader classification, fully proved & written.
  Prop reduction, Lemma monoid-comonoid, Thm reader-classification, table, analytic remark,
  "whole boundary lands on Cat" teachbox. LEAVE mostly intact.
- OUTDATED teachbox (3697–3720): "The open frontier: State and general container monads" —
  says State completeness is `[open]`. This is now FALSE. REPLACE it.
- Forward-glance teachboxes (3722–3760): higher-order trees + store→Workers. These bridge to
  §sec:moncomon-workers (3762). LEAVE in place — they correctly bridge to the next section.

## Structural decisions
1. Replace ONLY the outdated State teachbox (3697–3720) with the new material. The
   forward-glances stay put and still bridge to Workers.
2. New material, in order:
   - 1-sentence bridge (Reader was S_M=1; opposite extreme?)
   - `\subsection{The State pole: the store multiplication is invisible}`
     `\label{sec:state-liftings}` — hook (richest store, expect graded cat), Thm
     state-classification (State liftings ≅ Cat, C↦𝕊×C), "Why it holds" proof-sketch
     (grade-independence via sh_t/pr_t; ASSOC-DEEP; endpoint-locality; codiscrete collapse),
     Remark "why the graded category was a mirage" (copresheaf functorial but not
     endpoint-local).
   - Teachbox "One theorem, two poles: invariant is π₀" — Reader discrete π₀=|E|, State
     codiscrete π₀=1. THE astonishment: store mult contributes nothing.
   - Teachbox "outside view" — CBP (ter Horst et al Thm 6.14), structural resonance NOT a
     container result. \cite{CBP}. (deep-read → citable.)
   - Teachbox "The frontier: general container monads are holonomy-full" — REPLACES the naive
     "compute π₀" cliffhanger. Today's PROVE result: Upd liftings ≅ Fun(𝔸(↓),Cat),
     holonomy-FULL; π₀ does NOT classify (Z2_triv: π₀=2 but 4 liftings). Reader/State =
     the two holonomy-trivial poles (discrete; reset-collapse). Genuine open: beyond-Upd,
     higher degree. \cite{AhmanUustalu13}.

## Honesty tags (must match proof status)
- State thm: proved object-level; morphism-level by mirror + exhaustive |S|=2 machine check.
  Soundness Lean'd (StateProductLifting.lean).
- Update-monad: proved/exhaustive |S|=2 degree-1; classifier + isotropy=holonomy NEW; open
  beyond Upd & higher degree; Uustalu TTCS 2017 novelty-check deferred.

## Notation
- Match Reader theorem idiom for out-positions: `Q_s^{\coprod_{c'\in\ob\mathcal C}\mathcal C(c,c')}`
  (do NOT invent `\out`).
- 𝕊 = `\mathbb S` (action category of S^S↷S); 𝔸(↓) = `\mathbb A(\downarrow)`.
- τ^g(s,c) transport; ASSOC-DEEP asymmetry is the whole engine.

## Bib additions
- `CBP`: ter Horst, Mahadevan, Zambrano. Categorical Belief Propagation… arXiv:2601.04456 (2026).
- `AhmanUustalu13`: Ahman, Uustalu. Update monads: cointerpreting directed containers. TYPES 2013.

## NOT doing (write session discipline)
- No new proofs. Gaps flagged, not filled.
- Not rewriting the proved Reader subsection beyond retro-naming its pole π₀=|E|.
