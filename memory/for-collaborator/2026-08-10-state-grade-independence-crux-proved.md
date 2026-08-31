# State-liftings completeness: the grade-independence CRUX is proved (08-10 pt II)

**For Neil / Robin.** Follow-up to this morning's `state-liftings-holonomy-free` (which had
completeness OPEN). The crux sub-lemma that `state/PROVE.md` flagged — **grade-independence** —
is now **proved** (|S|=2, polynomial). Proof file:
`proofs/2026-08-10-state-liftings-grade-independence.md`.

## What was open
Post-purity a State lifting is a family `(A_t)_{t∈S^S}` of aggregators, `A_t(Q)=∐_{j∈J_t}
Q_{ρ(j)}^{Out(j)}`. Completeness (`State liftings ≅ Cat`, `C↦𝕊×C`) needed, first, that the
family is **grade-independent**: `A_t ≅ A_{id}` for all `t`. I had verified `𝕊×C` works and
refuted nontrivial holonomy *computationally*, but grade-independence itself was unproved and
the free-δ enumeration is combinatorially walled (10¹² candidates).

## The proof (one good idea)
Two rigorous pieces:
1. **`(P1)` `A_{id}` = an `S`-indexed family of small categories.** At grade `id` the threading
   is trivial (`s↦id(s)=s`), so the `(id,(id))`-restricted structure is *literally* the Reader
   comultiplication/counit with `E:=S`, and the State monad laws specialise to Reader's. By my
   08-09 Reader theorem, `A_{id}≅∐_s∐_{c∈Ob C̃_s}Q_s^{out(c)}`. **State's `A_id` is Reader-with-E=S.**
2. **`(★)` `δ_out` is functorial** — literally the outermost-object component of the
   associativity law `μTμ=μμT`:
   `δ_out^{(T,τ)} = δ_out^{(T,t)} ∘ δ_out^{(σ',ρ)}` (threaded factorizations).
   Then define `sh_t=δ_out^{(id,(t))}: J_t^s→J_id^s` (left-unit shadow) and
   `pr_t=δ_out^{(t,(t'_s))}` with `thread=id` (a σ=id lift). Feeding a carefully chosen 3-fold
   datum into `(★)` collapses one side to the **right-unit** factorization `(t,(id))`, whose
   `δ_out=id`. Result: **`pr_t∘sh_t=id` and `sh_t∘pr_t=id`** — the object sets `J_t^s` are
   grade-independent, all equal to `Ob C̃_s`.

So the "grades" of the store monoid `S^S` are a mirage: the left-unit shadows every grade-`t`
object down to a grade-`id` object, and associativity (read on the top object) makes the lift
back its inverse.

## Verification
- `(★)` verified directly on `Σ` and `𝕊×ℤ/2` (32768 instances each), and shown to **track
  associativity** (corrupting δ to break assoc breaks `(★)` in lockstep — disagreements 0).
- `sh_t/pr_t` confirmed inverse bijections + **degree-preserving** on `𝕊×C` for
  `C=ℤ/2,ℤ/3,`walking-arrow`,disc_3`.
- Grade-dependent-*profile* refutation hunt: no survivor found (free-δ walled, but every
  checkable candidate collapses to grade-independent).

## What's still open (honest)
Completeness now reduces to a **single** residual lemma: **holonomy-triviality** —
source-independence (`C̃_0≅C̃_1=:C`) and trivial `𝕊`-transport. The companion file refutes
every nontrivial transport *computationally*; a grade-independent abstract proof (transport =
functor `𝕊→Aut(C̃)`, forced trivial by the `σ≠t_s∘T` mismatch on untouched states; `𝕊`
connected ⟹ one `C`) is the last step. Also: the out-degree/position half of §3.2 is the
position-level mirror of `(★)`, verified but not written in full backward-map detail.

Registry `effect-coeffect-arrows.json`: added **proved** node `state-grade-independence`
(premises `state-P1-Aid-is-S-indexed-cat`, `state-delta-out-functoriality-star`, both proved);
degree-preservation carried as a `computed` **attempt** (not a premise, so it doesn't cap the
proved result). Completeness node stays **speculative**. Validator green.

**Grant angle:** this tightens Path 2 (DCont≅Cat spine) — the predicate/monad-lifting story
for *both* Reader and State now provably lands in `Cat`, one categorical level down, and the
State case shows the store-monoid grading **collapses** to `π_0` rather than enriching. Good
"the anticipated finer object is in truth the coarser `Cat`" narrative beat.
