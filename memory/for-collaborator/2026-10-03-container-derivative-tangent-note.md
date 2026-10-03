# For Neil (CC Robin / Rick on request) — WRITE shipped 2026-10-03

**Paper:** *The container derivative is a tangent structure: a fibrational positioning.*
`projects/papers/container-derivative-tangent-structure.tex` — 9pp, compiles clean (pdflatex, no
undefined refs), amsart-style article.

## One sentence
The AAGM one-hole-context derivative `∂` is not merely *analogous* to differentiation: `SPoly` (polynomial
functors, substitution) is a Cartesian differential category with `∂` as its differential combinator, so
`∂` is the vertical part of a genuine tangent structure realised on the nose by the dual-number
substitution `T(p)=p(y+εv) mod ε²`.

## What the paper does (and its honest grades — diffed against registry + proof files)
1. **Main theorem [PROVED].** Reflection along the faithful counting functor `N:SPoly→Poly_ℕ` (three
   lemmas: preserves CDC data incl. `N(∂_iF)=∂N(F)/∂m_i`, faithful on iso-classes, reflects equations).
   Registry `tangent-container-derivative.json#root` = proved, trustcheck GREEN. Worked example `T(yⁿ)`.
   CD.5/CD.6/CD.7 unpacked as explicit container isomorphisms (chain rule = `2026-06-12` note; CD.7 =
   Clairaut swap involution).
2. **The map-level correction [PROVED; lean-verified, 0 axioms].** The object-level "linear objects = S·y"
   reading is *vacuous* (SPoly is a full CDC). The content is at MAPS: `f:1→1` is CDC-linear iff `f=S·y`,
   so `y²` is not linear — the certificate that `T` is not the trivial `T(p)=p×p`. Discriminator Table 1.
3. **The orientation split [the load-bearing clarification].** CCGZ's forward FODS lives on the codomain
   fibration `cod` with pullback `ρ*` (Thm 56). The container logic `Cont(cod)=Fam(cod^op)` is on CCGZ's
   REVERSE/LENS side (their Ex 32 = containers, Def 57 = reverse). So the naive "the container bifibration
   IS the forward tangent fibration" is FALSE — the `ρ*` vs `(Σ_ρ)^op` hazard that has bitten this lane
   repeatedly. CCGZ Thm 74 is a **packaging remark**, not load-bearing; nothing in the proof rests on it.
4. **Restriction to directed containers (§6).** `T` is a strict `◁`-monoidal base-change functor
   `DCont(k)→DCont(D)`, `D=k[ε]/ε²`, laxator = the chain rule on the nose [PROVED]. Comonoid preservation
   is stated **conditional on** the base-change 2-functoriality of Gambino–Kock (honest grade:
   proved-modulo-cited — I put that qualification into the theorem statement, not just the prose). The
   Set² reading is REFUTED with explicit witnesses (ε²=0 → zero morphism). Headline: *a tangent vector of
   a category at `a` is a morphism out of `a`; the zero vector is `id_a`; the bundle lives over the dual
   numbers.* The closed form of `T(C)` is left as an OPEN problem.
5. **Honest novelty.** Modest — "close to folklore", the Set-coefficient instance of "polynomials over a
   rig form a CDC" (BCS 2009), species-adjacent. The value is the clean statement, the reflection proof,
   the object/map correction, the fibrational positioning, and the bridge to your own CCGZ programme.

## Why now
Course-timely for the Strathclyde *Tangent Categories and Containers* mini-course (Cruttwell + you, Oct
13–16). This is the nearest bridge between the two halves of that course, and it engages 2409.05763
directly. You are the natural first reader.

## Citation-provenance note (for Robin / browse)
`citation_check.py --report footprint` is clean at **deep-read**. To get there I upgraded the
`sources.json` entry for **2409.05763** from `agent-summary` to `deep-read`: the full 34pp PDF and
extracted text are on disk (`scratch/ccgz-2409.05763.pdf`, `ccgz.txt`) and I did a first-person,
theorem-numbered read into `scratch/2026-10-02-ccgz-scoping-memo.md` (Def 58, Thm 56, Thm 69 line 2320,
Thm 74 line 2585, Ex 32, Def 57/Thm 54). This is a bookkeeping correction, not a paraphrase-trust —
flagging it so a browse session can confirm/retain the upgrade. CCGZ's role in the paper is
packaging-only regardless, so nothing load-bearing depends on it.

## Open edges named in the paper
(i) first order only; (ii) the reverse/lens reading (`Fam(cod^op)`) is unaddressed — no registry node;
(iii) the closed-form multiplication of `T(C)` (Problem 7.?); (iv) an endofunctor tangent structure "on
DCont" via the Weil-algebra-indexed family `W↦DCont(W)` (Leung) — sketched, not proved.

## Status / plumbing
WIP → publishable is Robin's call; routes through Rick before publishable (agent-to-agent = PDF on
request). Not emailed this session (write-session rule). wip-sync push may be GH_TOKEN-blocked (standing);
the file is written regardless and the host-cron backs up the volume.
