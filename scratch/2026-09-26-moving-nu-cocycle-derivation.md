# Moving-ν cocycle equations for skew-brace extensions with non-trivial-kernel

MacBeth — 2026-09-26. Native derivation (no Letourmy–Vendramin dependency; RY ref [20]
= their own trivial-kernel 2102.12235). Companion sympy check:
`2026-09-26-moving-nu-cocycle-derivation.py` (all green).

## 0. Setup and conventions

Skew brace `(G,+,∘)`, `λ_a(b) = -a + (a∘b)`, so **`a∘b = a + λ_a(b)`** and
`λ : (G,∘) → Aut(G,+)` is a group homomorphism (this single fact *is* the skew-brace
axiom, given `(G,+)` a group).

Extension `0 → D → G → H → 0` of skew braces, `D` an ideal with **`(D,+)` and `(D,∘)`
abelian**. Ideal ⇒ `λ_a(D) ⊆ D`, `(D,+) ◁ (G,+)`, and `a∘D = a+D`, so the additive and
circle cosets coincide and `G/D = H`.

**Normal form (additive):** fix a normalized set-section `s:H→G`, `s(0)=0`. Every `g∈G`
is uniquely `g = s(h) + d`, `d∈D`. I coordinatize `G ≅ D×H` by `(d,h) ↦ s(h)+d`. Write
`+_H`, `∘_H` for `H`'s two operations and `λ^H` for its λ.

**Cochains (all valued in `D`):**

| symbol | definition | meaning |
|---|---|---|
| `μ_h(d)` | `s(h)+d-s(h)` | additive `H`-action, `μ:(H,+_H)→Aut(D,+)` |
| `σ_h(d)` | `s(h)∘d∘s(h)^{∘-1}` | circle `H`-action, `σ:(H,∘_H)→Aut(D,∘)` |
| `β(h₁,h₂)` | `s(h₁)+s(h₂)-s(h₁+_H h₂)` | additive factor set |
| `τ(h₁,h₂)` | `s(h₁)∘s(h₂)∘s(h₁∘_H h₂)^{∘-1}` | circle factor set (∘-difference) |
| `T(h₁,h₂)` | `s(h₁)∘s(h₂) - s(h₁∘_H h₂)` | circle factor set (additive-difference) — the one that appears in additive coordinates |
| `ν_h` | `λ_{s(h)}\|_D ∈ Aut(D,+)` | the moving datum |

`L := im(λ\|_D) = {λ_e\|_D : e∈D} ≤ Aut(D,+)`; residue `[ν_h] = ν_h·L ∈ Aut(D)/L`.

Two auxiliary pieces of the automorphism `λ_{s(h)+d}` in coordinates:
`Λ_{(d,h)} := λ_{s(h)+d}\|_D ∈ Aut(D,+)` and `ρ_{(d,h)}(k) := (D-part of λ_{s(h)+d}(s(k)))`.

## 1. The three equations

### (a) `+`-associativity ⟹ additive 2-cocycle
Coordinatizing `+`:
```
(d₁,h₁) ⊕ (d₂,h₂) = ( d₁ + μ_{h₁}(d₂) + β(h₁,h₂),  h₁ +_H h₂ ).
```
Associativity forces `μ` a homomorphism `(H,+_H)→Aut(D,+)` (the `β`-conjugation drops
because `(D,+)` is abelian) and

> **(a)**  `μ_{h₁}β(h₂,h₃) + β(h₁, h₂+_H h₃) = β(h₁,h₂) + β(h₁+_H h₂, h₃).`

### (b) `∘`-associativity ⟹ circle 2-cocycle
The exact `∘`-mirror, computed in the abelian group `(D,∘)`:

> **(b)**  `σ_{h₁}τ(h₂,h₃) ∘ τ(h₁, h₂∘_H h₃) = τ(h₁,h₂) ∘ τ(h₁∘_H h₂, h₃),`

with `σ:(H,∘_H)→Aut(D,∘)` a homomorphism.

### (c) brace compatibility `a∘(b+c)=(a∘b)-a+(a∘c)` ⟹ the cross equation
Coordinatizing `∘` (from `a∘b=a+λ_a(b)`, splitting `(d₂,h₂)=(d₂,0)⊕(0,h₂)` and using that
`λ` is an additive automorphism):
```
(d₁,h₁) ⊛ (d₂,h₂) =
  ( d₁ + μ_{h₁}( Λ_{(d₁,h₁)}(d₂) + ρ_{(d₁,h₁)}(h₂) ) + β(h₁, λ^H_{h₁}(h₂)),  h₁ ∘_H h₂ ).
```
Putting `d₁=d₂=0` identifies the circle factor set with `ρ`:
`T(h₁,h₂) = μ_{h₁}ρ_{(0,h₁)}(h₂) + β(h₁, λ^H_{h₁}h₂)`.

Now expand the brace axiom on `a=s(h)`, `b=s(k)`, `c=s(l)` (so `b+c=(β(k,l),k+_H l)`).
The `d`-independent identity is the **generalized RY (3.10)** (all sums in `(D,+)`;
`-_H`, `∘_H` are `H`'s operations):

> **(c)**
> `μ_h ν_h β(k,l) + T(h, k+_H l)`
> `  = T(h,k)  −  μ_{h∘_H k}μ_h^{-1} β(h,-_H h)  +  β(h∘_H k, -_H h)`
> `      +  μ_{(h∘_H k)-_H h} T(h,l)  +  β((h∘_H k)-_H h,  h∘_H l).`

The `ν` **appears exactly once**, in the term `μ_h ν_h β(k,l)`: `ν_h` acts on the
additive factor set `β(k,l)` inside the circle-compatibility.

Separately, the `d`-coefficient of the same brace axiom (equivalently: requiring
`λ_{s(h)}` to be an additive automorphism) gives the pure action-block constraint

> **(coupling-1)**  `ν_h μ_k ν_h^{-1} = μ_{λ^H_h(k)}`   (equivalently `ν_h μ_k = μ_{h∘_H k} ν_h`).

And `Λ_{(d,h)} = ν_h·(λ_{e}\|_D)` with `e∈D`, so **`Λ_{(d,h)} ≡ ν_h (mod L)`** — the residue
`[ν_h]` is the section-independent shadow.

## 2. The key question: does `[ν]` constrain which `(β,τ)` are valid?

**Two-level answer.**

**Cochain level — YES, `ν` couples.** The only place `ν` enters the (β,τ)-equations is
the term `μ_h ν_h β(k,l)` in (c). This is *not* `ν`-free: replacing `ν_h → ν_h·ℓ` (`ℓ∈L`)
changes the term to `μ_h ν_h ℓ β(k,l)`, which differs from `μ_h ν_h β(k,l)` unless `ℓ`
fixes `β(k,l)`. So a fixed cochain pair `(β,τ)` compatible at one `ν` is generally *not*
compatible after moving `ν` within its `L`-coset. Concretely: **moving `ν` forces a
compensating change in the circle factor set.** (Abstract data point in the script: `D=Z/4`,
`ν=neg`, `β=1` ⇒ LHS is `neg(1)=3`, not `1`.)

**Invariant level — NO, independence holds (`[ν] ⟂ [Ω]`).** Read (c) the right way: given a
valid action block `(μ,σ,ν)` (i.e. satisfying coupling-1 and its `σ`-analogue) and any
additive 2-cocycle `β`, equation (c) *determines* the circle factor set `T` (hence `τ`)
uniquely up to the circle-coboundary freedom in `ρ`. In every instance checked, the `T` so
determined automatically satisfies the circle 2-cocycle (b). Therefore **`ν` places no
existence obstruction on `β`**: for every `β` and every valid `ν`, a compatible `τ` exists.
Consequently the obstruction group
`H²_{[ν]} := {valid (β,τ)}/coboundaries at fixed [ν]`
is, as an abstract group, **independent of `[ν]`** — the map `β ↦ τ` is `ν`-twisted, but the
group of classes is not. `ν` contributes an orthogonal direct factor `[ν]` (an `H¹`-type
class in `Aut(D)/L`), disjoint from the `(β,τ)` obstruction `[Ω]`.

**Reconciliation.** The tempting statement "the gauge orbit splits as
(obstruction-orbit) × (ν-orbit)" is FALSE at the cochain/orbit level (exactly the coupling
term `μ_h ν_h β`), but TRUE at the invariant level. This matches the 09-25 registered
theorem *nu-variation-direct-factor-orthogonal*: **coupling confined to coboundaries,
invisible to `H*`.**

## 3. What sympy verified vs. what is hand-derivation

Witness: `(G,+)=Z/2×Z/4` (abelian, order 8), `D={0}×Z/4`, `λ_{(x,y)}(x',y')=(x',(-1)^{x+y}y')`.
Verified `(G,+,∘)` is a skew brace; `(D,+)=Z/4`, `(D,∘)=Klein`, `λ\|_D` = negation on odd
elements; `L={id,neg}=Aut(Z/4)`. Section reps: `s(1)=(1,0)` gives `ν_1=neg`.

**sympy confirmed (for 3 sections, all 8 `H`-triples, all 64 element pairs):**
- The coordinate `⊕` formula reproduces the true `+` (⇒ eq (a) structure).
- The coordinate `⊛` formula — including `Λ` (`≡ν mod L`) and `ρ` — reproduces the true
  `∘` for **all 64 pairs**. This is the real validation of the (c)-derivation: the `ν`/`Λ`
  term is genuinely there.
- Eq (a) [`β` additive cocycle], eq (b) [`τ` circle cocycle], **coupling-1**, `Λ≡ν (mod L)`,
  and the **cross equation (c) exactly as written** all hold.

**Verified by hand (not independently exercised numerically here):**
- That eq (c) determines `T` from `β` with *no* `ν`-dependent existence obstruction, hence
  `H²_{[ν]}` is `[ν]`-independent. On this witness `ν` and `β` **anti-correlate**
  (`ν_1=neg ⟺` section rep parity ⟺ `β(1,1)∈{0,2}`, which is 2-torsion, i.e. neg-fixed), so
  the coupling term `μ_h ν_h β` is present in the equation but never "bites" — the algebraic
  shadow of "flip `ν` forces a coboundary". This is a genuine `|D|=4` size artifact
  (`L=Aut(D)`, residue `[ν]` trivial). Exhibiting `ν≠id` and `β` *not* `ν`-fixed
  simultaneously (a nontrivial residue `L⊊Aut(D)`) needs `|D|≥8 ⇒ |G|≥16`, beyond this
  witness — the corner already flagged in the 09-25 memory. The invariant-level independence
  itself was brute-checked over all 16 `Z2×Z4` braces × 4 sections in the 09-25 work.

## 4. Honest caveats
- The "`T` auto-satisfies (b)" / "no `ν`-existence-obstruction" claim is proved structurally
  (T slaved to β via (c), and the whole coordinate system is a skew brace iff λ is a hom)
  and confirmed on instances, but not given a fully general standalone proof here.
- On the specified witness the residue `[ν]` is trivial, so this witness *checks the
  equations* but *cannot separate* different `[ν]`. The separation (`L⊊Aut(D)`) is the
  `|D|≥8` open corner.
