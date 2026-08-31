# The comonoid layer over a fibration — RESOLVED and SCOOPED (2026-07-14)

**For Neil / Robin.** Deep-work session on task C: *is "directed container = internal category" a
theorem about Π, or about composition?*

## Answer

**It is about composition, and this is settled, not open.** The conjecture `DirCont(q) ≃ Cat(B)` with
no Π is **true** (with one correction) and is **prior art in full** — chiefly **Shapiro–Spivak,
arXiv:2305.00167 (2023)**.

- **SS23 Thm 5.6:** ⊳-comonoids in `Poly_E` = internal categories with **exponentiable source**, for
  any finite-limit `E`. **Cor 5.12:** morphisms = internal cofunctors (Clarke, Def. 12). That is
  `DCont ≅ Cof` fibrationally.
- **SS23 Remark 3.16** is the exact answer to your question, in their words: `Poly_E` is a full
  subcategory of the *dependent lenses* (Spivak 1908.02202 Ex. 3.5) on **all** morphisms; only the
  **monoidal structure `◁`** needs exponentiability. So the *equivalence* needs only pullbacks; only
  `◁` needs **Π**.
- Roots: **Ahman–Chapman–Uustalu (LMCS 2014) §7** already *defines* directed polynomials in a
  category with pullbacks (they stipulate the source exponentiable in the *data* and never use it in
  the five laws — definitions only, no theorem); **Ahman–Uustalu 2016 §3.2** gives the Set-level
  observation.

**The correction to the conjecture:** it is `Cat_D(B)` (source a *display map*), not all of `Cat(B)`;
equality holds iff `q ≃ cod_B`. `C₁ = S.P` is a comprehension, so `dom` is display.

## Why this is worth your two minutes anyway

1. **It kills a stale "open gap."** `SUMMARY.md` had been asserting "nobody has done this
   fibrationally." Corrected. This is the **7th** reproof my full-PDF METHOD has caught — the pattern
   is stubborn and the guardrail is earning its keep.
2. **The one genuinely live target is the ∞-version:** **Kun Chen arXiv:2601.22968 Conjecture 7.2**,
   explicitly open — he has one direction of a Segal nerve and hasn't touched ∞-cofunctors. That is
   registry node `m6-infinity-dcont`. If we want novelty in this neighbourhood, it is there, and it is
   an ∞-category project, not a 1-category one.
3. **Two small expository things I'd keep for the book** (not theorems): (i) the `5+2=7` law
   accounting — the two internal-category axioms Ahman–Uustalu *don't* list are absorbed into the
   dependent typing of `o` and `⊕`, and every painful dependent cast in the Lean is externally just a
   pullback-mediation obligation discharged by an earlier law (D1 lets you state D4; D2 lets you state
   D5); (ii) a clean witness that `◁`-packaging is strictly lossy off LCC: `(ℚ,+)` as a one-object
   topological category in **Top** is a directed container whose source `ℚ→1` is *not* exponentiable
   (`ℚ` not core-compact), so it is not a `◁`-comonoid at all — an instance in a new base of SS23's
   own Example 5.10 (Conduché).

## Artifacts

- Write-up: `proofs/2026-07-14-comonoid-layer-over-fibration.md`
- Computation (two independent codings + monoid triangulation): `scratch/dircont_vs_cat.py`
- Registry: `proofs/registry/equivalence-chain.json` node `fibrational-comonoid-layer` (validated)
- SS23 read to verified-quote depth: `papers/ss23-2305.00167.pdf`, `sources.json` updated.

## Recommendation

Drop task C as a *research* target — the theory is Shapiro–Spivak's. Repoint at either (a) the
**∞-directed-container** conjecture (Chen 7.2), or (b) folding the settled 1-categorical story into the
book/grant as the clean "the equivalence is about composition, Π is only for the operad-of-composition
packaging" narrative, with SS23/ACU/AU/Clarke cited. I lean (a) for novelty, (b) for the grant.
