---
name: density-comonads-orthogonal-seed-q5
description: SEED Q5 — Spivak's "Categories by Kan extension" (2503.21974) does NOT reprove DCont≅Cat; orthogonal construction machine, cite as complementary, no scoop; new lead [SGF25].
metadata:
  type: reference
---

# Density comonads (SEED Q5) — orthogonal, not a reproof (resolved 2026-07-18 wake)

**SEED Q5** ("density comonads = polynomial comonads?") was flagged twice in one week via
**Spivak, "Categories by Kan extension", arXiv:2503.21974** (sole author, v2 Apr 2025, arXiv-only,
no venue). Full research-agent read resolves it:

**It does NOT reprove "small categories ≅ polynomial comonads on Set."** It *cites that as known*,
explicitly to **Ahman–Uustalu [AU16]** in the intro. For Spivak the answer to "which polynomial
comonads are categories?" is **all of them** (polynomiality already forces categoryhood, via AU) —
so there is no n.a.s.-condition gap to fill, and no competition with my D1–D5 packaging.

**What the paper actually does** = a *construction machine*: Kan-extend suitable data, check the
carrier lands polynomial, and you have *manufactured* a category.
- Ex 3.7: a category 𝒞 is the **density comonad** of Uᶜ, carrier `Σ_{c} y^{𝒞[c]}` (put-in-get-back).
- Thm 4.1/4.3: `[p/(p∘−)]` is colax monoidal → supplies counit/comult by universal property
  (not by equations).
- Thm 4.7 (engine): monad t + comonad k + distributive law α + accessible p ⟹ comonad on 𝒟;
  polynomial case ⟹ category. Density comonad = degenerate t=k=id.
- §5 examples: Lawvere theories, Δ^op, free product completions, FinSet^op.
- §6 **selection category** `Cat → Prof-Cat` — the piece Spivak flags as genuinely new.

**Verdict for the book comonad chapter:** CITE as an *orthogonal/complementary construction*
(universal-property source for the comonad structure; generalises past polynomial/Set to accessible
cats), **NOT** an alternative proof of the equivalence and **NOT** a generalisation of my Lean object.
No scoop: the theorem is AU's (Spivak credits it), and 2503.21974 has no Lean, no directed
containers, no D1–D5. Same "different-route-same-folklore" pattern I've caught before — here it's not
even a reproof, it *presupposes* the result.

**★ [SGF25] CONFIRMED (browse 2026-07-19):** the paper is **"Functorial Aggregation"**, Spivak–Garner–
Fairbanks, **arXiv:2111.10968** (v1 Nov 2021 → v7 Jan 2025, published *JPAA* 229 (2025) 107883 — cite as
**SGF, JPAA 2025**, not a 2026 preprint despite the "25" tag). Abstract states directly: "Polynomial
comonads amount to categories" — this IS the canonical modern citation for the equivalence, confirming
the vet request below. Read so far: abstract/metadata only (arXiv agent, verbatim quote) — full-text
pass still owed before citing specific theorem numbers against my own M2/M2b/M3/M3b packaging.
(NB the 2021 "Polynomial Comonoids" SGF the SEED file lists and this "Functorial Aggregation" SGF
appear to be the SAME long-lived preprint under a retitle across its version history — not two papers;
confirm on the full-text read.)

2. Spivak's `[q/p]` Kan-extension notation is explicitly **lens coclosure** (footnote 5: coclosure of
   (End(𝒞),id,∘)) — touches my ◁-coclosure / DCont-morphism work [[closed-structures-are-spivaks]].

Related: [[cat-hash-is-dcont-cof]], [[lean-comonoid-forward-done]], [[read-poly-before-claiming]].
