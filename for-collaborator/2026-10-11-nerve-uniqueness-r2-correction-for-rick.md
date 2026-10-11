# Covering note to Rick — nerve note (A1/A2/A3) + uniqueness note (B1/B2)

**To:** Rick · **CC:** Robin Langer · **From:** MacBeth
**Re:** your round-2 report of 2026-10-11 on Note A (nerve-level-two) and Note B (uniqueness)
**Status:** QUEUED for WAKE delivery. Do not re-send if already delivered.

## Note A (`papers/composition-is-a-nerve-level-two-datum.tex`) — A1, A2, A3 landed
All three must-fixes are addressed; no theorem statement changed (content commit to be stamped;
supersedes `6089268`).

- **A1 (splitting derivation, three repairs).** (a) Remark 13 no longer names Theorem 12's base-magma
  equation: the cocycle condition dω=0 is now stated as associativity of the *twisted composition over
  the already-associative base S*, distinct from Theorem 12 (a base-associativity failure, over which
  d∘d≠0 and no class exists) — both N₃-predicates on different objects. (b) I added the (L) qualifier:
  [ω]=0 ⟺ (G), and splitting = (L)∧(G), so [ω] decides splitting only under the standing (L) (the intro
  and Rem 13 both now say this). (c) The opening "whether a candidate matched pair closes … is governed
  by [ω]" now reads "whether an *associative* candidate splits", with the matched-pair/cocycle condition
  named as what supplies associativity. I also added the EM-is-semidirect / general-matched-pair-is-[12]
  clarification (A4) and switched d²ω → dω.
- **A2 (what [ω] is a class of).** New Remark (rem:whatomega): [ω]∈H²(S;D) is a class of the base S
  classifying an extension D ↣ E_ω ↠ S, and it is E_ω that splits; a base presented as C⋈D has [ω]=0,
  while the rigid-twist witness has S=B(Z/2), D=Z/2, E_ω=B(Z/4). I disambiguated D (the vertex-group
  natural coefficient system) from the wide subcategory 𝒟.
- **A3 (level convention).** Remark 8 (rem:coefftest) now attaches "coefficient-free" to the *datum*
  a·a=1 (nerve level N₂ for every ring), and states the *detecting class* sits at N₂ over F₂ and N₃ over
  Z, consistent with the nerve-level = degree+1 convention. The §7 reliance is corrected in the same way.

I understand the **weld nodes stay demoted** on this version — they reach checked-sober only once A1 is
in the text (now done), and proved only once ref [12] is attached; the (G)⟺[ω]=0 identification stays
"read" pending [12]. I am not re-promoting them.

## Note B (`papers/container-derivative-uniqueness.tex`) — B1, B2 landed
The two 30-second edits are in, and I mention the Prop. 12 restatement in the p.1 header (your B4 point):

- **B1.** The §1 "Finiteness is not load-bearing" paragraph now says N·y is *abstractly* solid; the Cantor
  pairing supplies an *abstract* isomorphism M⊗M≅M, **not** a vertical lift ℓ_M (so no contradiction with
  Def. 4 / Thm 13). "abstract" added at the three flagged spots.
- **B2.** §1 now reads "This note proves there cannot, **among representable (Weil base-change) structures
  on the linear layer**."

Per your disposition I will confirm the peer-reviewed status of the uniqueness grades (Thm 22 / Thms
11,18 / "N·y carries no tangent structure") only after B1/B2 land and you have seen them — not on the
strength of this note alone.

Gratefully, MacBeth
