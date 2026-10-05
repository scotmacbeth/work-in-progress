# Ambient-category correction shipped across the tangent arc (Rick F1/F4/F5)

**MacBeth — 2026-10-05 (write session)**

Robin — the systematic correction Rick's referee report asked for is done and pushed. This is a
**scope/framing fix, not a refutation**: the mathematics (the Weil-model rank arithmetic, the
Lean-certified collapse) is unchanged. What changed is the *name of the tangent functor* and the
*category it lives in*.

## The one-sentence version
We were writing the container tangent functor as `T=(−)◁D` in the full substitution category
`(Poly,◁,y)` and claiming it *is* the dual-number substitution. It isn't: full `◁` has no `ε²=0`
truncation (`y²◁(2y)=4y²≠3y²`), and on full Poly the uniqueness result collapses to `{id}`. The honest
functor is **base change by the Weil algebra** `W=ℕ[ε]/ε²`, `T=(−)⊗W`, on finite-rank ℕ-modules. `◁`
and `⊗W` agree **only on the linear layer** `S·y` — which is exactly where the rank count `1+2n` lives,
so the classification survives intact. The `ε²=0` truncation is what lets `n=1` (the derivative)
survive alongside `n=0`; drop it and only the trivial structure remains. That is Rick's finding, and
he was right.

## What I changed, document by document
1. **`papers/container-derivative-uniqueness.tex`** (primary, 12→13pp). Abstract, intro + Theorem 1,
   Definitions (infinitesimal object = augmented square-zero ℕ-algebra `D`; `T=(−)⊗D` base change),
   a new **Convention remark** pinning `⊗` vs `◁`, §3 recast as the *three-tensor coincidence*
   (`⊗D=◁=⊗_Dir` on the linear layer — this is now the linchpin that bridges "Weil base change" and
   "container derivative"), §6 converse relabelled (functor-level identities → `⊗`; object-level
   computations stay `◁`, legitimate because everything in the converse is linear and the two functors
   literally coincide there), §7 Theorem, §8 comparison table + caption, conclusion.
   - **F4 demoted.** `ℕ·y` is a solid *part* (true, kept) but was never shown to be a genuine tangent
     *structure*, so I do **not** claim uniqueness fails over all of Poly — only that the rank
     *rigidity* needs finiteness. New Remark `rem:part-not-structure` states the open question honestly.
   - **F5.** The `D=y⊕M` splitting and the linearity of `M` need pointedness (0 initial = 1 terminal),
     which base change over ℕ provides and full Poly does not; stated in the ℕ-algebra setting.
2. **`papers/container-cartan-boundary.tex`** (8pp). Relabelled `T=(−)◁D → T=(−)⊗W`; fixed the false
   `T(p)=p◁D=p(y+εv) mod ε²` to base change with the linear-layer caveat. The no-negation / no-scalar-
   ring-object argument is about the additive bundle's free-ℕ-module fibres — untouched and still valid.
3. **`papers/container-derivative-tangent-structure.tex`** (existence note): **already honest.** It uses
   `◁_𝔻 = substitution after base change along k→𝔻` and a Remark that explicitly explains why base
   change, not free substitution, is the right composition. No false claim present — no edit needed.
   (WRITE.md had flagged it as suspect; on inspection it was already correct.)
4. **Far-side note** (`proofs/2026-10-06-virtual-container-cartan.md`): still a proof `.md`, no paper
   yet, so nothing to relabel. When it becomes a paper, same fix with `W_ℤ=ℤ[ε]/ε²`.

## Verification
- Both papers compile clean with `pdflatex` (13pp / 8pp).
- `citation_check.py --report footprint`: provenance floor **deep-read** on both.
- No document now asserts `(−)◁D = dual-number substitution`; Theorem 1 is true as stated.

## Still owed (not for a write session)
- **CCGZ 2409.05763 convention.** WRITE.md wanted a deep-read to pin `⊗W` against CCGZ §1–4. `sources.json`
  already marks it deep-read and the correction rests on the standard Weil base-change framing (which the
  proof file `tangent-restricts-to-dcont` already states), so the fix is sound — but a browse/prove session
  should confirm the exact convention matches CCGZ's Weil-algebra-action presentation (Leung).
- **Route the corrected uniqueness note back to Rick** through the path once you're happy with it.

Strathclyde (Oct 13–16) is the reason correctness here was non-negotiable; this is the Theory-pillar lead
and it is now true as taught. — M
