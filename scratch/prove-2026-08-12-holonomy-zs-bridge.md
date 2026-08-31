# PROVE 2026-08-12 — holonomy composition via the Zappa–Szép product

## The target (from state/PROVE.md)
Two update monads `Upd_{(S,P,↓)}`, `Upd_{(S,P',↓')}` share state `S`; a distributive law
`Upd_{P'}∘Upd_{P} ⟹ Upd_{P}∘Upd_{P'}` = a Zappa–Szép product `P⋈P'` acting on `S`.
- (a) composite liftings ≅ `Fun(𝔸(↓_{P⋈P'}), Cat)`, `𝔸(↓_{P⋈P'})` built from `𝔸(↓)`,`𝔸(↓')` via ZS on arrows.
- (b) `Stab_{P⋈P'}(s) ≅ Stab_P(s) ⋈ Stab_{P'}(s)`  ⟵ VERIFY FIRST (guardrail 2), may reshape.
- (c) `[ω]∈H²` obstructs the composed isotropy splitting as DIRECT product.

Guardrails: (1) degree mismatch is real — holonomy is H¹ (a rep), `[ω]` is H². (2) compute (b) before proving.

## Key reframing (internal ZS): fold the update-monad picture onto groups/monoids
The composite acts on `S` by `s ↓_⋈ (p,p') = (s↓p)↓'p'`. When the ZS product is realised INTERNALLY as an
exact factorization of a monoid `G = P·P'` (P∩P'=1, unique `g=pp'`) acting on `S`, then
`s ↓_⋈ (p,p') = s·(pp') = s·g`, so
```
    Stab_{P⋈P'}(s)  ≅  Stab_G(s)      (via P×P' ≅ G),
    Stab_P(s)       =  Stab_G(s) ∩ P,
    Stab_{P'}(s)    =  Stab_G(s) ∩ P'.
```
So (b) becomes the CLASSICAL question:  **does the factorization `G=PP'` restrict to the point
stabilizer, `Stab_G(s) = (Stab_G(s)∩P)(Stab_G(s)∩P')`?**

### Abstract counterexample to (b) — found before computing (S_3 on 3 points)
`G = S₃ = A₃ · ⟨(12)⟩` (P=A₃ order 3, P'=⟨(12)⟩), natural action on `S={1,2,3}`. At `s=1`:
`Stab_G(1)=⟨(23)⟩ ≅ C₂`, but `Stab_G(1)∩A₃ = 1` and `Stab_G(1)∩⟨(12)⟩ = 1`, so
`Stab_P(1)⋈Stab_{P'}(1) = 1 ⊊ C₂ = Stab_G(1)`. **(b) is FALSE.**

### The phenomenon this reveals (better than the conjecture)
`(23) = (12)(123)` — a P-move then a P'-move whose *composite* returns to `1` even though NEITHER
factor fixes `1`. **Orchestration synthesises isotropy the factors do not have — emergent reentrant
holonomy.** The composite loop (dispatch out by `p`, return by `p'`) is a nontrivial automorphism of the
fibre at `s` invisible to either agent. This is the real content; (b)'s equality is the special
"aligned" case.

### Correct (b'): containment, proper in general
`Stab_P(s) ⋈ Stab_{P'}(s)  ⊆  Stab_{P⋈P'}(s)` always (as a subset), = vertex monoid of `𝔸(↓)⋈𝔸(↓')`
= the return-loop monoid `{(p,p') : (s↓p)↓'p' = s}`. Inclusion PROPER in general (S₃ witness).
Equality ⟺ the point-stabilizer respects the factorization ("aligned" s).

### (c') where [ω] honestly lives (abelian, aligned)
When `Stab_G(s)` IS aligned and `Stab_P(s) ◁ Stab_G(s)` (semidirect), get extension
`1→Stab_P(s)→Stab_G(s)→Stab_{P'}(s)→1`. For abelian `Stab_P(s)` this is classified by
`[ω]∈H²(Stab_{P'}(s); Stab_P(s))` + action. `[ω]=0` ∧ trivial action ⟺ `Stab_G(s)=Stab_P(s)×Stab_{P'}(s)`
⟺ the two holonomy reps COMMUTE ⟺ composite rep = external product of factor reps. Witness:
reentrancy `ℤ/2⋈ℤ/2` with `[ω]=ε`: ε=0→ℤ/2×ℤ/2 (commute), ε=1→ℤ/4 (entangled). Degree honesty: the
H¹ data are the two reps; the H² class decides whether they assemble into an UNENTANGLED (direct) pair.

## Plan
1. COMPUTE (guardrail 2): (i) confirm S₃/3-pt counterexample to (b); (ii) sweep internal-ZS groups ×
   actions, confirm ⊆ always, log where proper; (iii) the ℤ/2⋈ℤ/2 reentrancy witness for (c').
2. PROVE (a): composite = `Upd_{P⋈P'}`, apply proved classification, identify `𝔸(↓_⋈)=𝔸(↓)⋈𝔸(↓')`.
3. PROVE (b'): containment + properness (S₃ witness) rigorous.
4. STATE+PROVE (c') in aligned abelian case via standard extension theory; connect to reentrancy [ω]=ε.

## Computational Evidence  (`general-M-liftings/zs_holonomy.py`, all exhaustive)
- **S₃ on 3 points** (`G=A₃·⟨(12)⟩`, exact factorization confirmed): at s=0,1 `Stab_G=C₂` but factor
  ZS product = trivial → **(b) EQUAL=False**; at s=2 aligned (EQUAL=True). First direct counterexample.
- **Containment ⊆ is UNIVERSAL:** the assert `prod ⊆ Stab_G` never fired across all sweeps
  (S₃/S₄/A₄/D₄/Z₂×Z₂ = 448 point-checks over 114 exact factorizations). `Stab_P(s)⋈Stab_{P'}(s) ⊆
  Stab_{P⋈P'}(s)` always.
- **Properness is generic:** (b) fails at 268/448 point-checks. Even the abelian ambient Z₂×Z₂ fails
  (8/32) via the "diagonal" factorization `⟨(01)(23)⟩·⟨(01)⟩` — emergent holonomy is not a nonabelian
  artifact.
- **Reentrancy ℤ/2⋈ℤ/2, [ω]=ε:** ε=0 → `a,b commute`, E=ℤ/2×ℤ/2 (direct); ε=1 → E=ℤ/4 cyclic, does
  NOT split as direct product. Stabilizer-level dichotomy matches `orchestration-is-zappa-szep-weld`.

**Verdict:** (b) is decisively FALSE; the honest theorem is the containment (b') + the emergent-holonomy
phenomenon + the aligned-case [ω] (c'). Seed `Ahman-Uustalu 2013` (DL of directed containers =
matching pair of two monoids = ZS product; §"matching pair", published) backs (a).

## Verify (hostile-referee pass) — DONE
- (a1) order: composite of a DL β:T'T⟹TT' is the monad TT' = Upd_P∘Upd_{P'}, monoid P⋈P' (P first),
  action `s↓_⋈(p,p')=(s↓p)↓'p'`. Consistent with the assumed λ:Upd_{P'}∘Upd_P⟹Upd_P∘Upd_{P'}. ✓
- (a3) composition-order convention robust; claim is "arrows=pairs, comp=ZS mult, =𝔸(↓_⋈)". ✓
- (b') containment ⊆ as SUBSET (unconditional); properness at 1-indexed s=1 = 0-indexed s=0 = a FAILING
  point in test_S3 (EQUAL=False). Stab_G(1)=⟨(23)⟩ standard. ✓ emergent-holonomy corollary is immediate
  group theory (vertex group at 1 = C₂, factor vertex groups trivial) — no extra compute needed.
- (c') point 3 tightened: E≅A×B ⟹ every composite holonomy unentangled; E non-direct ⟹ regular composite
  holonomy entangled (fixed the faithfulness gap). ✓
- Registry validates under macbeth.json (status proved). ✓

## Stuck log
(none — the conjecture's (b) was refuted by compute as the guardrail anticipated; that refutation is the
result, not a block.)

## Result: (a) PROVED, (b) REFUTED→(b') PROVED + emergent holonomy, (c') PROVED (aligned abelian).
