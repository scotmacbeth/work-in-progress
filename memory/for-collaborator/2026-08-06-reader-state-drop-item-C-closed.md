# Item (C) closed: the Reader/State leaf-drop is uniform in size

**MacBeth, 2026-08-06 deep-work session.** Short note for Robin / Neil / whoever runs the next
LEAN or WRITE pass.

## TL;DR

The PROVE.md census ("Reader/State are ∏-Mendler non-cartesian, witnessing `cartesian ⊊ ∏-Mendler`)
was already **refuted** earlier today (`proofs/2026-08-06-state-reader-ladder-census.md`, registry
node `state-reader-outside-pi-mendler` = proved, Lean-verified finite core). This session I did **not**
re-litigate the refutation — I re-verified its crux (Lemma 1, the Yoneda reindexing criterion) and
then **closed the one gap it flagged**: PROVE.md item (C), the *fully general* symbolic drop.

## What was loose, and what's now nailed

The proof file (§2, §6) proved the drop for small cases + "mechanism", and:
- mis-stated the Reader bound as "possible once `|X|` is **large enough**";
- left the general State case as "**mechanical**", computed only at `S=3`.

Both are now **proved for all `|E|,|S|≥2` at the minimal `|X|≥2`**:

1. **Uniform witness.** Constant diagonal + one fresh off-diagonal:
   `G(e)(e)=0 ∀e`, `G(0)(1)=1`. Then `μG` (the diagonal) is **all-`0`-labelled**, but the inner
   token `(0,1)` has label `1`. By Lemma 1 (a natural mult-laxator `j` exists iff there is a total
   label-preserving `κ_μ:I(mm)→lv(μ mm)`), `κ_μ` is **not total** ⟹ no `j` ⟹ Reader ∉ ∏-Mendler.
   Only two ingredients: an off-diagonal *position* (`|E|≥2`) and a *fresh label* (`|X|≥2`). No "large
   `X`".

2. **State = Reader, made precise.** Take the outer shape `h=id`. Then State's multiplication
   `μ(mm)(s₀)=F(s₀)(h(s₀))=F(s₀)(s₀)` is **literally Reader's diagonal** `μG(e)=G(e)(e)` on the
   `X`-labels. The uniform witness ports verbatim. State's `S^S`-many shapes (its *branching*) are
   **irrelevant** to the drop — the single identity shape already breaks totality. So Reader and State
   are **one mechanism** (diagonal leaf-drop), differing only in shape-multiplicity — sharpening the
   old slogan "they differ only in branching."

3. **Lemma 1 independently re-derived.** `∏_L ev_{a_L}=Hom(⊔_L y_{a_L},−)`; then
   `Nat(Hom(⊔_L y_{a_L},−),Hom(y_b,−)) ≅ (⊔_L y_{a_L})(b) = ⊔_L[a_L=b]`. Each output coordinate is a
   matching input, or the whole hom-set is empty. The direction (`I(mm)→lv(μ mm)`, many→few) is
   **forced** by "μ^T is a backward container map (target→source)" — this is exactly the variance the
   original compute pass slipped on.

Exhaustive no-total-`κ_μ` confirmation: `scratch/pi-mendler-boundary/general_drop.py` (`|E|,|S|∈2..8`).

## Provenance / registry

- Patched `proofs/2026-08-06-state-reader-ladder-census.md` §2 (Reader tightened, State rewritten),
  §5 (verification), §6 (gap → CLOSED).
- Registry `effect-coeffect-arrows.json`: added child `reader-state-drop-general-uniform` = **proved**
  under `state-reader-outside-pi-mendler`; `trustcheck` green.

## Flag for the next wake

`state/PROVE.md` still contains the **pre-refutation** framing (asks to upgrade the false census to
proved). It is **stale** — the question is settled (refuted + item C closed). Wake should retire or
rewrite it. Natural next targets if anyone wants to push: (i) Lean the general uniform witness (the
current Lean cert is a single finite `S=Bool` datum — the uniform-`|X|=2`-all-sizes statement is a
clean `∀ n≥2` Lean lemma); (ii) the **converse** half of the trichotomy characterisation
("`κ_μ` total + labels rigid ⟹ full ∏-Mendler monad") — asserted in §3, currently leaning on A–B
Thm 6.3 for coherence; worth a standalone write-up for the book's boundary chapter.
