# Covering note for Rick — container-derivative U+E, second-pass revisions applied

**To:** Rick (grandparick20@gmail.com) · **CC:** Robin (langer.robin@gmail.com)
**Re:** Your second-pass review, UID 210 (2026-10-08) · **Requesting:** final re-review
**Repo:** github.com/scotmacbeth/work-in-progress
**Content commit (stamped on p.1 of the uniqueness PDF):** `75603ad` · **pushed HEAD:** `e558743`
**PDFs:** `papers/container-derivative-uniqueness.pdf`, `papers/container-derivative-tangent-structure.pdf`

> **NOTE TO SELF (MacBeth):** written during a WRITE session (email disabled). Send this to Rick,
> PDFs attached, on the next wake/routing pass. CC Robin. Correct hash is `75603ad` (not the earlier
> `19e272d`/`19e372d`).

---

Rick —

All six items from your second-pass report are addressed. No mathematics changed; this was
self-containment + honesty, as you asked.

**R1 — Thm 13 (rank-free exclusion) now proved in full in the note.** The `\cite{MacBethFlip}`
deferral is gone (that note is unpushed; the argument is now inline and the citation + bib entry
removed). The proof is the five-step chain, with your two flagged sub-steps made explicit:
  - **(0)** the lift lands in the mixed part, `δ(M) ⊆ M⊗M` — from the two verticality conditions and
    `ker(p⊗id) ∩ ker(id⊗p) = M⊗M`;
  - **(1)** `ℓ_M` is an isomorphism — read off the universal comparison `v = id ⊕ ℓ_M`, so
    universality *produces* solidity rather than assuming it;
  - then (2) a free-module iso permutes bases → `β = (β₁,β₂): K → K×K` a bijection; (3) `cℓ=ℓ` +
    `ℓ_M` surjective force `γ = id` on the mixed part (this is the correction to your step (iii):
    `c` is *derived* to be id-on-mixed, not assumed to be the swap); (4) lift-coassociativity then
    collapses to strict coassociativity of `ℓ_M`; (5) a coassociative basis-bijection is the diagonal,
    surjective onto `K×K` iff `|K| ≤ 1`. No step uses finiteness. I also kept the independent
    representable (`◁`-monoidal) route as a remark — it closes `κ ≤ 1` without [lc.2].

**R2 — Thm 17 (converse): `ℓ_M` iso now exhibited, not asserted.** `M = 0`: `ℓ_M = 0: 0 → 0`.
`M = y = ⟨ε⟩`: `M⊗M` is free of rank 1 on `ε⊗ε`, and `ℓ_M: ε ↦ ε⊗ε` is a bijection of one-element
bases.

**O1 — overclaim dropped.** Title and headline now read "the only nontrivial representable
first-order tangent structure on the linear layer `Lin(SPoly)`"; the "in `Poly`" phrasing is gone, and
the sequel paragraph is scoped the same way.

**O2 — "extensive category of ℕ-modules" removed** (you're right — the zero module kills
extensivity). Every occurrence is restated as the fact actually used: free ℕ-modules are closed under
direct sum and rank is additive over it (`rank(A⊕B) = rank A + rank B`), with no subtraction; and `P'`
is the direct sum of the surviving summands because `ĝ`, `ẑ` respect the decomposition.

**O3 — directed-container sketch demoted in the Existence note.** It is out of the abstract and the
introduction headline (both now say "proposition-sketch", with the comonoid-preservation step flagged
as computed-not-proved). §7 already carried the sketch label.

**Protocol — commit hash on p.1.** The uniqueness PDF now prints "Built from commit `75603ad`"
directly under the title. Apologies again for the earlier `19e272d`/`19e372d` typo in the covering
email.

Grateful for a final look when you have a moment — this is the reference I plan to hand Neil for the
Strathclyde mini-course (Oct 13–16).

— MacBeth
