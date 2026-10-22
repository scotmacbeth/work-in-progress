# Covering note for Rick — NEW unit: topos-uniform Day convolution (held for WAKE delivery)

**To:** Rick (grandparick20@gmail.com) · **CC:** Robin (always)
**From:** MacBeth
**Status:** held for WAKE to email (WRITE sessions commit but cannot send mail).
**Thread:** NEW review request, independent of the normalization-defect/triangulation thread.

## What this is

A fresh, self-contained grant unit — the strongest available *theory* bullet for the Kodamai
AI-Mathematician grant. It states and proves that the equivalence chain
`containers ≃ directed containers ≃ polynomial comonoids ≃ Cat` carries its **monoidal** content
uniformly across **every Grothendieck topos**, not just `Set`.

- **File (tex):** https://github.com/scotmacbeth/work-in-progress/blob/main/expository/2026-10-22-day-convolution-topos-uniform.tex
- **File (pdf):** https://github.com/scotmacbeth/work-in-progress/blob/main/expository/2026-10-22-day-convolution-topos-uniform.pdf
- **Content commit:** `b553b27` (stamped on page 1; stamp commit `50edcd6`).
- **Lean witness:** https://github.com/scotmacbeth/work-in-progress/blob/main/lean/2026-10-21-day-convolution-graph.lean

## The two theorems (and who owns which)

- **Theorem 1.1 (ours, proved).** For internal categories `C, D` in a Grothendieck topos `E`, with
  `◁`-comonoids `c, d` in `Poly(E)`, the Dirichlet/Day tensor `c ⊗ d` represents the product internal
  category `C × D` **on the nose** — componentwise objects, morphisms, identities, composition. Proof
  in three steps: underlying object (finite limits), interchanger distributor `(★)` (= the LCCC
  composition-distributivity law of Gambino–Kock, *not* a separate extensivity axiom), structure
  trace. No well-pointedness, no extensivity, no disjointness of coproducts are used.
- **Theorem 1.2 (NOT ours — a corollary of a published theorem).** Under the internal equivalence
  `Comon(Poly(E),◁,y) ≃ Cat(E)`, `⊗` computes the categorical product. This rests on the *full*
  internal equivalence (incl. essential surjectivity) of **Shapiro–Spivak, arXiv:2305.00167,
  Thm 5.6 + Cor 5.12**. I say so explicitly in the footnote and in Remark 4.1 — I am not claiming it.

## What I'd most like you to check

1. **The division of labour in §3.** My central honesty claim is that the non-pointwise content of
   `◁` is absorbed entirely into the comonoid↔category dictionary, leaving only componentwise finite
   limits, so the identification is genuinely *on the nose* (no coherence iso to chase). Does Step 3's
   structure trace actually discharge this, or have I smuggled a pointwise assumption?
2. **The `(★)` = Gambino–Kock claim (§3 Step 2, and Table in §5).** I assert the only load-bearing
   coherence is `Σ(A×B) ≅ (ΣA)×(ΣB)`, and that this *is* the LCCC law GK use to compose polynomials —
   hence "LCCC suffices", sharper than the folklore "LCCC + extensive". Is that attribution right, or
   is there a hidden extensivity/universality-of-coproducts step?
3. **Honest scope (§7).** I state the theorems over Grothendieck toposes and flag "any LCCC carrying
   GK-polynomials" as the open maximal reach; I deliberately do **not** assert an "LCCC+extensive ⟹
   Grothendieck topos" converse (not Giraud's shape). Is this the right place to draw the line?

## Provenance I want to flag (per our citation protocol)

- Niu–Spivak Prop 3.79 (Dirichlet = Day convolution) is **theirs**, cited as such — not original, and
  I make no strict-monoidal claim about the extension functor (a prior correction on that is logged).
- Lucyshyn-Wright 2502.18557 is cited only for the *parallel* enriched-side signal that Day-convolution
  **closure** is special to `Set`-like bases and does not transport to a general base `V`. Its full
  read corrected an earlier over-framing; I have **not** attributed any specific "retreat to `V̂`"
  construction to it, and I note it is about enrichment, not polynomial comonoids.
- Przybyłek 1401.1172 is **not** cited (only agent-summary provenance; below the paper floor).

Candidate for `publishable-result` after one pass from you.
