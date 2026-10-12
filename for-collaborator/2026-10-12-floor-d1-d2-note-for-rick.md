# Covering note for Rick — the floor correction (D1 vs D2)

**To:** Rick · **CC:** Robin (always) · **Re:** your M1 (band-boundary review,
`proofs/reviews/2026-10-12-band-boundary-review.pdf`)

Rick — your M1 lands, and it repairs into something cleaner than the thing it broke. The note is

- **PDF/TeX:** `papers/inventory-floor-d1-vs-d2.{pdf,tex}` (6pp, compiles clean, no warnings)
- **Proof file:** `proofs/2026-10-12-inventory-floor-d1-d2-dichotomy.md`
- **Lean witness:** `lean/2026-10-12-floor-d1-separation-s3.lean`
- **GitHub:** https://github.com/scotmacbeth/work-in-progress/blob/main/papers/inventory-floor-d1-vs-d2.pdf
  (content commit `f19cfcb`)

## What your counterexample was telling us

The naive floor corollary *strict global inventory ⟺ β=0 ∧ [𝔤]=0* was **false**, exactly as your
`B(ℤ)/S₃` recomputation showed. The fix is not a patch — it is that the word "strict" was hiding a
choice, and the two honest choices live **one cohomological degree apart**:

1. **(D2, Thm 1.1):** retain the 2-cell (coherence) datum — ask `ᾱ` to *lift* to a strict `K`-valued
   functor. Exists ⟺ `[𝔤] = ᾱ*[⋆] = 0 ∈ H²(N(C); Z(K))`. — **proved** (this cycle;
   Lemma 3.1 is the Eilenberg–Mac Lane / Brown IV.3 central-extension criterion, carried).
2. **(D1, naive, Thm 1.2):** drop the datum — ask `ᾱ` to be *trivialised* to the identity. Exists ⟺
   `o_{D1} = 0 ∈ H¹(C; Inn K)/im H⁰(C; Out K)` — a **degree-one** obstruction with coefficients in
   `Inn K`, **not** `[𝔤]`. — **proved**.
3. **D1 ⟹ D2, strictly** (Prop 5.2): the gap `o_{D1}≠0=[𝔤]` is exactly the centreless/fungible regime
   where `Z(K)` is too small to carry a class while `ᾱ` is still a nontrivial inner transport.
4. **Separation (§6):** `C=B(ℤ)`, `K=S₃`, `α=c_{(0 1)}`: `β=0 ∧ [𝔤]=0` (D2 holds, lift `T(n)=σⁿ`) yet
   `o_{D1}≠0` (no gauge conjugates `σ` to `e`). Your witness, now proved in both directions with the
   `o_{D1}` location made explicit.

The slogan, if you want one line for the handout: *name the extension, and its kernel names both the
coefficient group and the degree.* Dropping the coherence datum costs one degree and swaps the
coefficient from the centre `Z(K)` (degree 2) up to `Inn K` (degree 1). Keeping those two coefficient
groups distinct **is** the repair.

## Grades (honest, please check them)

- Floor dichotomy (D1⟺o_{D1}, D2⟺[𝔤], D1⟹D2, separation): **proved** — landed in this heartbeat's
  prove cycle, no gaps flagged.
- S₃ finite/decidable core: **lean-verified** (`floor_separation`: `Z(S₃)=1`, `|Aut S₃|=6` so
  `Out=1` by brute force over all 720 carrier perms, `σ²=e` D2 lift, and `∀μ μσμ⁻¹≠e`). Kernel axioms
  `[propext]`/`Quot.sound` only — no `native_decide`, no `sorryAx`, no added axioms.
- Band-triviality criterion (`β=0 ⟹ ᾱ` exists): cited at **computed** (band-boundary clause-(a),
  which you demoted this cycle — I did not re-inflate it).
- Gerbe-class construction `[𝔤]=ᾱ*[⋆]`: cited to the capstone / thm-A (**proved**, your review).

## What I explicitly did *not* do

- I did **not** claim the re-promotion of `band-boundary`. The note says in the Upshot that this is a
  separate registry judgement, deferred to a later wake. If you think the repair is grounds to
  re-promote, say so and I'll flag it.
- Scope is the band-trivial stratum `β=0` only — exactly the stratum your M1 concerned. The
  nontrivial-band / `T²`-coupled frontier stays in the capstone.

## Things to attack

- **§4 Prop 4.2 (D2 end):** the gauge-invariance reconciliation `τ*[⋆]=(ĥ_c|_Z)_*[𝔤]` — I claim the
  global `ĥ_c∈Aut K` preserves `(⋆)` and the induced coefficient automorphism fixes `0`. Is the
  decomposition `μ(x)=ĥ_c·j(x)` per-component airtight when `C` is disconnected?
- **§5 Prop 5.1 (D1 end):** the `Out K`-action on `H¹(C; Inn K)` is vanishing-neutral but can be
  nontrivial (D₄ swaps the two reflection classes). Is the quotient the right home for `o_{D1}`, or
  would you state it as a bare `[ᾱ]∈H¹` with the coordinate-change caveat as a remark?
- **The degree claim itself:** is "dropping the 2-cell datum costs exactly one cohomological degree"
  a fair slogan, or does it over-compress the `Z → Inn K` coefficient shift that rides along with it?

**Not emailed yet** — write sessions commit but cannot send; this note is queued for the next WAKE to
deliver (standing "WAKE delivers undelivered covering notes" feedback). Content commit `f19cfcb`.

— MacBeth
