# Note for Robin — vec-admissibility preprint, WRITE #2 revision (2026-09-21)

**File:** `papers/vec-admissibility-not-zfc.tex` (now 12pp, compiles clean two-pass, citation floor
`deep-read`). This is a **revision**, not a new paper and not a publishable promotion — the headline is
unchanged: *container-admissibility of `Vec` is not provable in ZFC* (proved via the CH refutation).

## What changed and why

The PROVE #3 session that ran just before this WRITE (`proofs/2026-09-21-gapS-osofsky-jensen-product-pd.md`)
did **not** close the residual — but it produced a clean **proved ZFC reframing** that was worth folding
in, and WRITE.md's second ask (fold in the HT deep-read; soften the independence lean) is now done.

1. **§4 rebuilt around projective dimension.** The residual is now stated as a single homological
   invariant: **`Conj 6.2 ⟺ pd_S(M) = 0`**. The mechanism is pretty: the cokernel of `M` inside the free
   module `Φ ≅ S` is `∏_ℕ N₀`, the countable product of a projective-dimension-one *seed*
   `N₀ = ∏_ℕ E / ⊕_ℕ E ≅ S/I` (the scalar Baer–Specker quotient, cyclic because the field beats `ℤ`). So
   admissibility of `Vec` is literally an instance of the Osofsky–Jensen problem: *does a product of pd-1
   modules raise projective dimension?* Added proved-ZFC bounds `1 ≤ pd_S(M) ≤ d+1`
   (`d = min{n : 2^{ℵ0} ≤ ℵ_n}`), and a refined necessary condition (if `M` is projective the
   decomposition has rank *exactly* `ℵ1` in `MA + 2^{ℵ0}=ℵ2`).

2. **Honesty flag you should know about.** The tempting sharpening `pd_S(M) ≤ d`, hence `= 1` under CH,
   needs Osofsky's exact global-dimension value `gl.dim S = d+1`. I have that only as a **recollection,
   not a source-verified fact**, so it lives in a clearly-marked Remark and *no proved claim depends on
   it*. **This is the one thing to verify in a future browse session** (Osofsky, *Homological dimension
   and the continuum hypothesis*, Trans. AMS 132 (1968); her 1973 CBMS notes). If it checks out, `pd_S(M)`
   under CH is pinned to 1; if not, the ZFC-clean bound gives only `pd ∈ {1,2}`.

3. **§5 (residual) is now genuinely two-sided.** The earlier draft leaned independent on the grounds that
   "both obstructions vanish in the residual window." PROVE #3 self-corrected that: refuting
   `ℵ2`-projectivity is a size-`ℵ1` phenomenon at `ω1`, which a continuum *collapse* `2^{ℵ0}=2^{ℵ1}` does
   not obviously protect. So I now present **FALSE-in-ZFC and INDEPENDENT as both live**, weigh the two
   intuitions honestly, and keep only an *evidential* lean to independence (collapse-threshold is
   forcing-arrangeable; `pd=0` is Whitehead-shaped; the large dual removes the `ℤ^ℕ`-style absolute
   obstruction). Not a proof either way.

4. **HT citation debt cleared.** Herbera–Trlifaj arXiv:0910.4277 is now `deep-read` in `sources.json`
   (you registered it / the verification agent read it at source — artifact
   `proofs/reviews/2026-09-21-HT-0910.4277-ex68-deepread.md`). §5 now cites Thm 2.9(i), Ex 6.8, Cor 7.3 as
   *verified*. The paper's two external load-bearing sources (HT + Trlifaj's Dual Baer Criterion) are both
   deep-read; `citation_check --report footprint` shows floor = `deep-read`.

## What still needs work (not this session — flagged for the right phase)

- **BROWSE/verify:** Osofsky's `gl.dim End_k(E) = 1 + d` (point 2 above). This is the single unverified
  citation and it would sharpen §4.
- **PROVE:** the actual open problem, Question 4.13 — compute `pd_S(M)` as a function of the continuum;
  can it be 0 when `2^{ℵ0}=2^{ℵ1}`? PROVE.md recommends attacking the commutative shadow
  `∏_r(k^ω/k^{(ω)})` over `k^ω` first.
- **Not publishable yet:** per WRITE.md, no publishable push until the headline is upgraded on a
  proved+Rick-reviewed result. This is a WIP revision.

Direct-read the tex/PDF from the projects volume, or from the work-in-progress repo (I've synced it there).
— MacBeth
