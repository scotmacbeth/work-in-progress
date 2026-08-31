# Workers type hierarchy — which of Cont's structures descend? (Neil's 07-30 Q)

**MacBeth — 2026-07-30 PROVE session.** Full write-up:
`proofs/2026-07-30-workers-type-hierarchy.md`. Registry:
`proofs/registry/workers-type-hierarchy.json` (**proved**, validates). Code:
`scratch/workers-type-hierarchy/` (all green; interchange 256 cases × 4 tensors).

## The question
Workers = `(Set,×)`-graded category `Workers_S(p,q)=Cont(ΔS⊗p,q)`. Do the four monoidal
structures (`◁,⊗,×,+`) and three closed structures descend?

## Answer — two frameworks, one fault line

**Two ways to tensor workers:**
- **(A) grade-multiplying (Para):** `S`-worker ⋆ `T`-worker → `S×T`-worker. This is *the* graded
  monoidal notion (tensor = graded functor, grades combine by `×`).
- **(B) shared register:** two `S`-workers → one `S`-worker on a shared state. = (A) + grade-diagonal
  + a **collapse `S×S→S`**.

**Framework A (the headline): all four descend.** `⊗` **strong** (PROVED — `⊙=ΔS⊗(−)` is a strong
monoidal functor `V×C→C`, since `ΔS⊗ΔT=Δ(S×T)`); `×` and `+` **oplax** (PROVED — cartesianness of
`(Set,×)`/`(Cont,×)`, resp. cocontinuity of `⊗` + functorial cartesian grade-projections); `◁`
**oplax** (COMPUTED — interchange verified 256 cases, pentagon unwritten). Interchange holds for all
four ⟹ the Para tensor is a genuine graded bifunctor every time.

**Framework B (the obstruction): the tensor splits.** `+` strict, `×` oplax-free, but **`⊗` and `◁`
require a monoid on the state `S`** — and none is natural (`S=∅` has no unit; the graded structure
must exist at every grade). PROVED for `⊗` via `Comon(Cont,⊗)≅Fam(Mon^op)`; COMPUTED for `◁`.

**The crown insight.** The collapse `S×S→S` needs a monoid **iff** the object-tensor puts the two
state-copies on the *same* position:
`+`,`×` **separate** operands' positions (fibre `Ba+Dc`) → free; `⊗`,`◁` **merge** them
(fibre `Ba×Dc`/nested) → monoid required.

**Closed structures — same fault line.** Workers is **`⊗`-closed**, internal hom `= [p,q]_⊗` of
`Cont` (PROVED: state curries *past* `⊗` because it sits beside the retained argument; counts
`256=256`, `65536=65536`). The `×`-exponential and `◁`-coclosure **do not descend** (state entangles
the curried argument; count witness `1296≠256`). Precise open test via `⊗`-closure:
`×`-closed ⟺ `([ΔS,q]_⊗)^p ∈ im[ΔS,−]_⊗`.

## For the grant / book
- **Book Ch4 (Monads & Comonads / Workers):** this is the natural §after the Workers construction —
  "which agent-algebra operations lift to stateful agents." Clean table (§4 of the proof). The
  `⊗` internal hom `[p,q]_⊗` is a genuine **stateful function type**.
- **Grant Impact:** the state mode's obstruction is now pinned — shared-state composition is
  obstruction-free for choice/product but demands the state be a **monoid** for parallel/pipelined
  composition. Slots into `connections/three-modes-of-composition.md`: directed=`[ω]∈H²`,
  state=**monoid-on-register**, effect–coeffect=branching `κ/λ`.

## Gaps (honest)
1. `◁` framework-A coherence: interchange only (pentagon unwritten).
2. `◁` framework-B "monoid suffices" converse: by analogy, not verified.
3. `×`/`◁` non-closure: base homs don't transport (proved); non-existence of *some* graded hom open.
4. Lean: A1 (`Φ^⊗` iso) + C1 (`⊗`-currying) are defeq-shaped, clean follow-ons to `StateComonad.lean`.

## Questions for Neil
- Book framing: present both frameworks (A grade-mult primary, B shared-register as the obstruction),
  or lead with the `⊗`-is-strong-and-closed headline and fold B into a remark?
- Worth a LEAN pass on A1+C1 now (short), or defer until the `◁` gaps close?
