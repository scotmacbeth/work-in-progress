# Symmetry is the compositional fingerprint

**Claim (heuristic bridge, Path 3 core ↔ Path 5 applications):** the symmetry group of a composite
object is a fingerprint of *how it was assembled*. An **unexpected** symmetry certifies genuine
(irreducible) composition; a **broken expected** symmetry certifies a defective composition. Same
diagnostic principle, opposite sign.

## The two data points

**(A) THM 3 necessity — unexpected symmetry certifies genuine composition.** `[computed]`
The U-corner proof (`proofs/2026-09-07-U-corner-resolved-stabilizer.md`,
[[U-corner-closed-stabilizer-per-component]]) closes `U∘U ≇ ⟦r⟧∘U` by an `Aut(X)`-stabilizer invariant
read per species component. On the each-label-once component, a polynomial outer functor `⟦r⟧∘M` admits
only **block-fixing product** stabilizers `∏ Stab(u_β)` — rigid positions, "function fixed ⟺ pointwise
fixed," NO swap of parts. Genuine self-composition `U∘U` produces a **correlated swap**
`C_2 = ⟨(01)(23)⟩` (order 2, fixed-point-free, NOT a product) that no polynomial outer can match. The
*presence of a symmetry that shouldn't be there* is precisely what distinguishes true composition from a
polynomial fake. (Unit-free `n=8` witness `(S_2×S_2)≀S_2` in the free magma re-proves Theorem P the same
way.)

**(B) Catala tax-code #1095/#1096 — broken symmetry certifies a wiring bug.** `[agent-summary]`
(GitHub issues, `reading/2026-09-25.md`; diffs NOT deep-read — provenance flag.) The joint-return scope of
US tax §121 (home-sale gain exclusion) is *meant* to be parametric/symmetric in which spouse occupies
`person1` vs `person2`. The executable encoding silently breaks that symmetry at two structurally
independent wiring sites (lines 114–115 and 216–220 read `person1`-centric data). The *absence of a
symmetry that should be there* is the signature of the compositional defect — and because there are two
independent sites, the naive one-line fix does not restore it.

## Why this is one principle, not two coincidences

Both are instances of: **the automorphism structure of a composite is determined by its assembly, so
comparing the actual symmetry group against the symmetry the assembly *should* have is a decision
procedure for compositional correctness.**
- In (A) the "should" comes from the polynomial normal form (block-fixing products); the *surplus*
  symmetry is the certificate of irreducibility.
- In (B) the "should" comes from the intended parametricity of the scope; the *deficit* symmetry is the
  certificate of a bug.

This is the same move as the 09-05 stabilizer method that killed `𝕄` (`D_4 = S_2≀S_2` block-swap ∉ Young
orders) and eliminated `β` — symmetry as the invariant that no counting (cardinality) can see. Contrast
with the FUSION/IDENTIFICATION/COLLISION hygiene note: cardinality is a *lossy* invariant (COLLISION
mode); the stabilizer group is a *faithful* one. **Check the symmetry, not the count.**
[[fusion-versus-identification]]

## Grant / seed value
Bridges the deepest core-theory tool (THM 3 necessity via stabilizers) to the grant's Path 5 "economic
consequences" narrative: the *same* mathematical diagnostic — is the observed symmetry the one the
composition demands? — detects both irreducible functor composition and a real, open, money-relevant tax
-code wiring bug. If Catala #1095/#1096 becomes a `/expository` worked example, this is its thesis
sentence. Caveat: the bridge is currently a heuristic analogy, not a theorem — the Catala side is
`agent-summary` and would need the actual diffs read + the symmetry stated as a group action before any
claim leaves the container. [[U-corner-closed-stabilizer-per-component]],
[[two-invariants-of-the-effect-monad-codensity-and-polynomiality]]
