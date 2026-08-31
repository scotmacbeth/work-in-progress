# PROVE scratch — branching × commutativity × affine pairwise independence

**Started 2026-07-31.** Goal: prove P1 (non-branching), P2 (commutative), P3 (affine)
are **pairwise logically independent** on Set-monads. Deliverable: clean Proposition +
machine-verified witness table. Load-bearing owed computation: writer over a
non-commutative monoid is non-commutative *as a monad*.

## The three properties (precise)

- **P1 = non-branching**: `M ≅ E + A×(−)` as a functor (polynomial, all arities ≤ 1).
  `¬P1` = not of this form (e.g. genuinely branches: some element has support ≥ 2).
- **P2 = commutative** (Kock): the two canonical `MX × MY → M(X×Y)` (double strength)
  agree: `Ψ = μ∘M(st')∘st = μ∘M(st)∘st' = Φ`.
- **P3 = affine** (Kock/Jacobs): `M1 ≅ 1`.

## KEY STRUCTURAL DISCOVERY (sharper than PROVE.md asked)

The 2×2×2 cube of (P1,P2,P3) has **exactly one hole**: **(P1 ∧ ¬P2 ∧ P3) is impossible**
— *non-branching ∧ affine ⟹ commutative*. Proof: P1 ⟹ M1 = E+A. P3 ⟹ |E+A| = 1 ⟹
either (E=∅,|A|=1) ⟹ M = Id, or (|E|=1,A=∅) ⟹ M = constant-1 monad. Both commutative. ∎
So the three are **NOT jointly independent**, but **ARE pairwise independent** (all three
2×2 faces fully populated). That is the correct, honest, and sharper statement.

## The commutativity criterion for E+A×(−) (computed by hand — RICHER than expected)

Writer-with-absorbing-exceptions `M X = E + A×X`, `A` monoid, `E` a left `A`-set (`⊙`),
`η(x)=(e_A,x)`, `μ`: `inl e ↦ inl e`; `inr(a,inl e)↦inl(a⊙e)`; `inr(a,inr(a',x))↦inr(a·a',x)`.
Double strength Ψ vs Φ, four cases:
1. `(inl e, inl e')`: Ψ=`inl e`, Φ=`inl e'`  → equal ∀ iff **|E| ≤ 1** (left-vs-right exception!)
2. `(inl e, inr(b,y))`: Ψ=`inl e`, Φ=`inl(b⊙e)` → equal iff **action trivial** (`b⊙e=e`)
3. `(inr(a,x), inl e')`: Ψ=`inl(a⊙e')`, Φ=`inl e'` → same trivial-action condition
4. `(inr(a,x), inr(b,y))`: Ψ=`inr(a·b,·)`, Φ=`inr(b·a,·)` → equal iff **A commutative**

**Criterion.** `E+A×(−)` commutative ⟺ (A commutative) ∧ (|E|≤1) ∧ (⊙ trivial).
Three independent sources of non-commutativity:
- **writer source**: A non-commutative (case 4) — the one PROVE.md flags as load-bearing;
- **exception source**: |E|≥2 — "which exception wins", left vs right (case 1);
- **action source**: nontrivial A-action on E (cases 2,3).
(|E|=1 forces ⊙ trivial automatically; |E|=0 pure writer ⟺ A commutative.)

By-hand load-bearing check (case 4): 3-element non-comm monoid `N={1,a,b}`, `a·b=a`, `b·a=b`
(identity adjoined to left-zero band). Ψ((a,x),(b,y)) = (a·b,(x,y)) = (a,(x,y)); Φ = (b·a,·)=(b,·).
a≠b ⟹ **non-commutative**. ∎ (verify exhaustively in code.)

## Witness table (2×2×2 cube, one hole)

| cell (P1,P2,P3) | witness | notes |
|---|---|---|
| (T,T,T) | **Id** | ar≤1, comm, M1=1 |
| (T,T,F) | **Maybe** = 1+(−) | ar≤1, comm (|E|=1), M1=2 |
| (T,F,T) | **IMPOSSIBLE** | non-branching+affine ⟹ Id/const-1 ⟹ comm |
| (T,F,F) | **Writer A×(−)**, A 3-elt non-comm; also **2+(−)** exception | ar≤1, non-comm, M1=A/E |
| (F,T,T) | **𝒟** (distribution) / **P⁺** (non-empty powerset) | branch, comm, M1=1 |
| (F,T,F) | **Pf** (powerset with ∅) | branch, comm, M1=2 |
| (F,F,T) | **idempotent magma monad** (medial fails) | branch, non-comm, M1=1 |
| (F,F,F) | **free magma** (binary trees) | branch, non-comm, M1=∞ |

Note: any non-commutative affine monad is forced branching (contrapositive of the hole).

### Three 2×2 faces all fully populated ⟹ pairwise independent
- **P1×P2**: Id / Writer-noncomm / Pf / free-magma.
- **P1×P3**: Id / Maybe / 𝒟 / Pf.
- **P2×P3**: Id / Maybe(comm,¬aff) / idempotent-magma(noncomm,aff) / Writer-noncomm(noncomm,¬aff).

## Verification plan
1. Generic double-strength commutativity checker for finite Set-monads (obj,fmap,eta,mu).
2. Run on: Id, Maybe, Writer(A comm & non-comm), exception 2+(−), Pf, P⁺.
   Extract E+A×(−) criterion by sweeping (A,E,⊙). Confirm hand criterion.
3. Idempotent/free magma: find finite model where **medial law** (a*b)*(c*d)=(a*c)*(b*d)
   FAILS (idempotent case: also x*x=x) ⟹ monad non-commutative (Kock: comm monad ⟹ every
   op medial in every algebra). Confirm M1: free idempotent magma on 1 gen = {x} (affine);
   free magma on 1 gen = infinite (non-affine).
4. Affineness: |M1| for each.

## Citations (classical anchors, not reproved)
- Kock, *Monads on symmetric monoidal closed categories* / *Bilinearity...* (commutative = strengths agree; 𝒟 example; commutative ⟹ ops are homs / medial).
- Jacobs, *Affine monads* CMCS 2016 (affine = T1≅1; 𝒟, P⁺ affine).
- Power–Robinson 1997 (premonoidal/commutative).
- E+A×(−) classification = my 2026-07-30-affine-classification.md.
