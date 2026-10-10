# Corrected Crown Stage 2 note, for Rick (CC Neil) — 2026-10-10

**Status:** QUEUED for WAKE delivery (WRITE has no email tool). Email to Rick
(grandparick20@gmail.com), CC Robin (langer.robin@gmail.com). Content commit **4e7264d**, pushed to
`github.com/scotmacbeth/work-in-progress` (`papers/crown-stage2-unfolding-vs-descent.{tex,pdf}`,
11 pp, recompiles clean). Supersedes the version you reviewed (commit 4136ecf / re-stamped 8972231).

Rick — your report was exactly right: all three defects trace to one mistake, that I made the
encoding functor covariant and then patched the variance by hand with a nearest-ancestor retraction
`ρ_f`, which does not compute preimage. The rewrite makes the single structural change you prescribed
— **the encoding functor is now contravariant** — and everything falls out. Proof file:
`proofs/2026-10-10-crown-stage2-repair.md` (in the repo). Item by item:

- **M1 (Def 6 / Prop 7(2) / Prop 8).** `Ψ'` is now `Ψ':𝒯^op→Cont`, `Ψ'(f)=(id₁,j)` with `j` the node
  injection carried **backward**; the opcartesian leg is then `j⁻¹`, as wanted. The result is stated
  as an **isomorphism of indexed posets** `𝒯^op→Pos`, `T↦(2^{nodes T},⊆)`, `f↦j⁻¹`; in total-category
  terms ℙ is the **opfibration part** of `Ψ'*Cont(cod)` over `𝒯^op`, fibrewise-opposed. The ill-typed
  "as fibrations over 𝒯" is gone, and the word **conditional** has left the abstract, Thm 1(1) and the
  scope section. New Remark records why `ρ_f` was wrong (your V-tree counterexample: `Σ_{ρf}{b}={r}≠∅`).
  Stage 1 is now presented with the same contravariant convention `Φ:𝒫^op→Cont`, inclusion backward
  (so the `[m]→[n]` collapse issue you flagged cannot arise).
- **M2 / §1 ((∗) without Jakl–Reggio).** Rem 9 and Open Problem 1 are replaced by your **six-line
  proof** of the cartesian lift inside the coloured category 𝒜 (new Lemma: cartesian ⟺ R=j⁻¹R′ ⟺
  pathwise; preimage for every T). **The Jakl–Reggio dependence is deleted.** The paper is now cited
  correctly (T. Jakl, L. Reggio, arXiv:2603.21841, CMCS 2026) with an explicit note that it is **not
  used** — the earlier ref wrongly listed "Abramsky, Reggio" and no arXiv id.
- **M3 (Ψ not a functor).** New §4 states the **no-go as a theorem**: the object assignment
  `T↦(br(T),{chain_b})` extends to no functor `𝒯→Cont` nor `𝒯^op→Cont` covering the embeddings —
  contravariant fails on existence (a branch of T′ restricts to a non-branch prefix), covariant fails
  on functoriality (your sibling-swap σ forces a fixed-point-free map where functoriality needs a
  fixed point). So clause 2 is now explicitly about the **object** assignment Ψ, and the genuine
  branch relation is a **span** `R_f` (left-total, not functional) — which is *why* `Fam=Σ` can't
  realize it and recovery is descent.
- **M4 (ceiling refuted).** The k≥2 "beyond Cont(cod)" claim is **withdrawn**. New Prop: `Ψ'_k(T)=
  (1,{nodes(T)^k})` with backward map `j^k` **reproduces the k-ary fibre exactly** (the M1 argument
  verbatim). Only the trivial "unary Ψ' is blind to k-ary" survives. One shape per relation symbol for
  a signature (coproduct over symbols is the *correct* coproduct); EF-style ⇒ positions = comparable
  k-tuples, and the old `2^{n^k}` count is corrected.
- **Should-fix.** Lemma 12 presented as a one-line observation; the descent object is named an
  **equalizer** (one variance, not "coequalizer/descent equalizer"); the cover is for the **Alexandrov
  topology of down-sets** (named); Open Problem 3 restated as descent along the **span** R_f, since Ψ
  is not a functor.

Clause 2's objectwise over-count `2^{Σ(λ−1)}` is untouched (it compares fibres over single objects,
and is lean-verified separately). Registry: `crown-stage2-multishape-branch-extension` re-promoted to
**proved** (positive half), new proved child `crown-stage2-psi-no-functorial-action`, ceiling node
corrected to the trivial statement.

**Not yet re-reviewed** — you saw only the false version. Circulating as WIP; I'd welcome a check of
the contravariant indexed-poset statement and the no-go before it moves toward publishable.

— MacBeth
