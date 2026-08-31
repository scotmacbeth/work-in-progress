# Book Ch7: the crown identity `T^Σ_M = M ◁ −` is now written into the fibration section

**MacBeth — WRITE session, 2026-08-09.** For Neil / Robin.

## What I did

Folded the 08-08 crown result — **the Σ-container lifting is left composition by `M`** — into the
book, `books/category-of-containers.tex`. It is a **new subsection** `\subsection{Which monads lift:
the Σ-lifting is M◁(−)}` (`\label{sec:sigma-is-comp}`) inside the fibration section
`sec:moncomon-fibration` of Chapter `ch:moncomon`, placed as the culminating subsection right after
the "comonadic because contravariant" caution remark and before the two forward-glance teachboxes.

It compiles clean (77 pp, 0 undefined refs, 0 new citations). Source of the maths:
`proofs/2026-08-08-sigma-monad-is-triangle-monoid.md`.

## The four beats

1. **Prop `prop:sigma-is-comp`** — `T^Σ_M C = M ◁ C`, an equality of endofunctors, with
   `η^Σ = η_M ◁ −`, `μ^Σ = μ_M ◁ −`. I do the shape/position match in the open (shapes `= MS`,
   positions `= ∐_{b∈lv(m)} P(x_b)`) because it *explains* the definition of `T^Σ` rather than merely
   confirming it. **Lean-verified**: `SigmaLift.lean`, `sigmaLift_eq_seq` closes `M.sigmaLift C = M◁C`
   by `rfl` (definitional; sorry-free, axiom-free).
2. **Cor `cor:sigma-monad`** — `T^Σ_M` is a monad ⟺ `M` is a `◁`-monoid (container monad) ⟺ `⟦M⟧` is
   a Set-monad with polynomial structure maps. One-line proof via `Cont ≃ Poly ↪ [Set,Set]` fully
   faithful strong monoidal: "`A⊗−` is a monad ⟺ `A` is a monoid". The mysterious "canonical section"
   `σ` of the 08-07 proof **is** `μ_M`'s backward position map; (U1),(U2),(A) are the `◁`-monoid laws
   read on positions. So the whole 08-07 Reader/State computation is now *an instance of a theorem* —
   Reader = diagonal comonoid on `E`, State = store monad.
3. **Thm `thm:bag-refutes`** — `reverse-total ⟹ Σ-monad` is **FALSE**. Bag is reverse-total in the
   strongest way (`μ = ⊎` is a leaf-bijection, `σ = id`) yet `T^Σ_Bag` is not even a functor on
   `Cont`, because Bag ∉ Cont (fails the connected pullback `A→1←B`; `|Bag(2×2)|₂ = 10 ≠ 9`;
   `{(0,0),(1,1)}` and `{(0,1),(1,0)}` collide). Discriminator: **polynomial, not merely analytic** —
   `reverse-total : ◁-monoid :: analytic : polynomial :: forgets-provenance : tracks-provenance`.
4. **Teachbox: both legs, clean criteria** — `∏ = T_M` lifts ⟺ `M` cartesian; `∐ = T^Σ = M◁−` lifts ⟺
   `M` a `◁`-monoid. Independent axes (List both; Reader/State are `◁`-monoids but non-cartesian, so
   carry `∐` and not `∏`). With the honest caveat that the strict object-level identity is a different
   *layer* from Orestis's oplax `Λ P ∘ join ⊆ Λ(Λ P)` — that oplax `⊆` is the base-monad-join
   interaction, which degrades from the strict law exactly at the `T_M`-cartesian boundary.

## I also closed an open flag

The big 2×2-grading teachbox earlier in the same section had an **"Open:"** provenance note asking
whether `reverse-total ⟹ Σ-monad`. I rewrote it to **"Resolved" (false)**, forward-referencing
`cor:sigma-monad` / `thm:bag-refutes`. The *other* open question there — exhaustiveness of the parity
dichotomy (is every data-valued lifting of Reader/State `∏`, `∐`, or a mixture?) — I left flagged
open, because it is.

## Ch7 lead-ordering — your call, Neil

Per your steer I wrote the identity so it **stands as a theorem regardless** of whether Ch7 ends up
*leading* with it. Right now it sits as the culminating subsection of the fibration section, which
reads well: the grading table poses "which monads, and why do the sections cohere?", and this
subsection answers both. If you'd rather the chapter *open* with `T^Σ_M = M◁−` and present the 08-07
Reader/State work as the special case, that's a re-order I can do in a follow-up write session — say
the word.

## Honesty / open

- The module-coherence 2-cells (pentagon/triangle) for the `A`-action are still only object-level —
  flagged in the earlier predicate-liftings section, unchanged here.
- `code/citation_check.py` is still absent at the documented path; I introduced no new bibitems (all
  four cites — NiuSpivak23, AhmanBauer24, HermidaJacobs98, OrestisAgda — are pre-existing deep-read
  sources), so the footprint is unchanged.
