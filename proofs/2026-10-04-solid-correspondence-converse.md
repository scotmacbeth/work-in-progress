# A rig-internal proof of the solid-correspondence converse

**MacBeth (Kodamai / Ghani group) — 2026-10-04**

**Upgrades** `tangent-uniqueness-spoly.json#solid-correspondence-converse` and hence
the root `#root` from `computed` → `proved`. Closes the one gap flagged in
`proofs/2026-10-03-tangent-uniqueness-spoly.md` §4, §6 (Problem 6.3 of
`papers/container-derivative-uniqueness.tex`).

---

## 0. The statement, and what was missing

Let `T = (−)◁D` be a **representable first-order tangent structure** on the
category `SPoly` of finite-support polynomial functors, in the based (dual-number)
sense of the proved base-change result `proofs/2026-10-03-tangent-restricts-to-dcont.md`
(`T` is base change along the rig map `ℕ → ℕ[ε]/ε²`, strict `◁`-monoidal). Write

> `D = y ⊕ M`,  `M = S·y` a **linear** container, `|S| = n` finite.

(Linearity of `M` is forced by the additive-bundle axiom — companion note §2 — and is
not re-litigated here; it is orthogonal to the gap.)

> **Theorem (converse — now proved).** The tangent-category axioms force `n² = n`;
> hence (finite `n`) `n ∈ {0,1}`, i.e. `M ∈ {0, y}` and `T ∈ {Id, ∂}`.

The companion note proved every other leg. The **only** thing standing between
`computed` and `proved` was: derive `n²=n` *rig-internally*, i.e. without the
subtraction / additive inverses that Lanfranchi–Lemay (arXiv:2505.09080, Thm 4.8)
use over a commutative **ring**. That is what follows. The engine is the
**universality of the vertical lift**, and the one new idea is that the relevant
*vertical bundle* is a **coproduct** of surviving summands (so ranks **add**, never
subtract), because `SPoly` is extensive.

Throughout, `◁` is substitution with unit `y` (`y◁E = E = E◁y`); a linear container
`k·y` has extension `X ↦ k×X`, and (Lemma 1 of the companion note) the shape-count
`k` is a complete isomorphism invariant of a linear/finite-support container.

---

## 1. `◁` preserves pullbacks on both sides

> **Lemma A.** For every `D ∈ SPoly`, the functor `(−)◁D : SPoly → SPoly` preserves
> pullbacks; and for every polynomial `A`, the functor `A◁(−)` preserves pullbacks.

*Proof.* Pullbacks in `SPoly` are computed pointwise. For `(−)◁D`: if
`F = G ×_H K` pointwise, then for all `X`,
`(F◁D)(X) = F(D(X)) = G(D(X)) ×_{H(D(X))} K(D(X)) = (G◁D ×_{H◁D} K◁D)(X)`.
So `F◁D = G◁D ×_{H◁D} K◁D`. For `A◁(−)`: `(A◁E)(X) = A(E(X))`, and a polynomial
functor `A` preserves connected limits (Gambino–Kock, *Polynomial functors and
polynomial monads*, Prop. 1.9); a pullback is a connected limit, so `A` preserves the
pointwise pullback `E₁(X) ×_{E₀(X)} E₂(X)`. Hence `A◁(−)` preserves pullbacks. ∎

**Consequence (the tangent data are all `◁`-functors).** The projection, zero,
pullback-powers, pushforward and vertical bundle of `T = (−)◁D` are again right
`◁`-tensorings, by the tangentoid structure maps on `D`:

- `p = (−)◁p̂`,  `p̂ : D → y` the augmentation (`ε ↦ 0`, kills `M`), `z = (−)◁ẑ`,
  `ẑ : y → D` the zero, `p̂∘ẑ = id_y`.
- **`T₂ = (−)◁D₂`**, `D₂ := D ×_y D`:
  `T₂(A) = TA ×_A TA = A◁D ×_{A◁y} A◁D = A◁(D ×_y D)` by Lemma A (`A◁(−)` preserves
  the pullback), naturally in `A`.
- **`Tp = (−)◁ĝ`**, `ĝ := p̂◁D : D◁D → D`: indeed
  `T(p_A) = (A◁p̂)◁D = A◁(p̂◁D)`.
- The **vertical bundle** `V :=` pullback of `Tp : T² → T` along `0 : Id → T`
  satisfies **`V = (−)◁P'`**, `P' :=` pullback of `ĝ` along `ẑ`, by Lemma A
  applied pointwise (`V(A) = A◁P'`).

All of `D`, `D₂`, `D◁D`, `P'` are objects of `SPoly`; `y` is one of them.

---

## 2. The three counts (direct coproducts — no subtraction)

Work in the based/graded setting (ε-grading mod ε² per copy of `D`; across copies the
mixed term survives — this is exactly the Weil-algebra model
`k[ε^A_1..ε^A_n, ε^B_1..ε^B_n]/(\text{within-copy products})`, the ground truth for a
representable tangent structure, delivered by the base-change equivalence).

**(i) `D◁D`.** Since `M` is linear, `M(X) = S×X`, so
`(D◁D)(X) = D(D(X)) = X ⊕ M(X) ⊕ M(X) ⊕ M(M(X))`, a coproduct of four pieces:

| summand | source | rank |
|---|---|---|
| `y` | base | `1` |
| `ε_in = M` | inner copy's `M` | `n` |
| `ε_out = M` | outer copy's `M` | `n` |
| `M◁M = (S×S)·y` | mixed (both `M`) | `n²` |

so `D◁D = y ⊕ M ⊕ M ⊕ (M◁M)`, rank `(1+n)² = 1+2n+n²`.

**(ii) `P'` (the vertical bundle fibre).** `ĝ = p̂◁D` applies `p̂` (`ε ↦ 0`) to the
*outer* copy: it kills `ε_out` and `M◁M` (both carry an outer-`M` factor) and sends
`y ↦ y`, `ε_in ↦ M ⊂ D`. The zero `ẑ : y → D` has image the `y`-summand. Hence

> `P' = ĝ⁻¹(\mathrm{im}\,ẑ) = \{\,ε_in\text{-component} = 0\,\}
>      = y ⊕ ε_out ⊕ (M◁M)`,

**a coproduct of the surviving summands.** This is the crux: in the extensive
category `SPoly` the pullback is literally the sub-coproduct where the `ε_in` leg
vanishes, so its rank is the **sum** `1 + n + n²` — computed by addition, never as
`\mathrm{rank}(D◁D) − \mathrm{rank}(\mathrm{im})`. (Lanfranchi–Lemay compute the
analogous fibre over a ring by a short exact sequence, i.e. by subtraction; that is
the step that fails over the rig `ℕ`, and it is exactly the step we have replaced.)

**(iii) `D₂ = D ×_y D`.** Two tangent directions sharing the base, with **no** mixed
term (a fibre product creates no products of the two infinitesimals):
`D₂ = y ⊕ M ⊕ M`, rank `1 + 2n`.

Both `P' = (1+n+n²)·y` and `D₂ = (1+2n)·y` are **linear** (a coproduct `y ⊕ (\text{free})`
is again `(1+\cdots)·y`), so Lemma 1 of the companion note applies to them.

*(Computational verification: `scratch/verify_universality_counts.py` enumerates the
based bases for `n = 0..5`, confirming `rank(D₂) = 1+2n`, `rank(P') = 1+n+n²` with
`P'` a direct coproduct, and that `D₂ ≅ P' ⟺ n²=n`.)*

---

## 3. Universality forces `n² = n`

> **Universality of the vertical lift** (Cockett–Cruttwell 2014, Def. 2.3 [v.l.]):
> the square
> ```
>          v
>   T₂  --------→  T²
>   |              |
> p∘π₀             | Tp
>   ↓              ↓
>   A   --------→  TA
>          0_A
> ```
> is a pullback, with the comparison `v : T₂ → T²` built from the vertical lift `ℓ`.

Being a pullback with corner `T₂`, the axiom asserts precisely that
**`T₂ ≅ V`** (the pullback of `Tp` along `0_A`), as endofunctors, naturally in `A`.

By §1, `T₂ = (−)◁D₂` and `V = (−)◁P'`. Evaluate the functor-isomorphism at the object
`y ∈ SPoly` and use `y◁E = E`:

> `D₂ ≅ P'`  in `SPoly`.

Both are linear; by Lemma 1 (shape-count is a complete iso-invariant),

> `1 + 2n = 1 + n + n²`.

Now use only that `ℕ` is a **cancellative** rig with no zero divisors — **no
subtraction, no additive inverses**:

- additive cancellation of `1`, then of `n`: `1+2n = 1+n+n² ⟹ 2n = n+n² ⟹ n = n²`;
- so `n² = n`; for `n ≥ 1`, multiplicative cancellation gives `n·n = n·1 ⟹ n = 1`;
  and `n = 0` satisfies `0² = 0`.

Hence **`n ∈ {0, 1}`**. ∎

`n = 0`: `M = 0`, `T = Id`. `n = 1`: `M = y`, `T = ∂` (AAGM dual-number). Combined with
the companion note's forward direction (both are realised) and representability, this
proves: **`∂` is the unique nontrivial representable first-order tangent structure on
finite-support polynomial functors — unconditionally.**

---

## 4. Why this is rig-internal (the one new idea)

| step | Lanfranchi–Lemay (ring) | here (rig `ℕ`) |
|---|---|---|
| vertical bundle fibre `P'` | submodule, rank via SES `⟹ rank = rank(T²) − rank(im)` (**subtraction**) | explicit **coproduct** `y ⊕ ε_out ⊕ M◁M`, rank **adds** (extensivity) |
| extract rigidity | solid map `μ:M⊗M→M` iso `⟹ r²=r` | rank equation `1+2n=1+n+n²` directly from `D₂≅P'` |
| finish `r²=r ⟹ r∈{0,1}` | integral domain | ℕ **cancellative**, no zero divisors (not subtraction) |

The subtraction that blocked a literal port lived in computing the vertical-bundle
fibre by exactness. In `SPoly` that fibre is a *direct coproduct of the surviving
summands*, so its rank is a **sum**. Everything downstream is additive/multiplicative
cancellation in `ℕ`. The derivation never forms a difference of ranks, never inverts
an element, and never builds the solid map `μ` explicitly.

---

## 5. Verification and sanity

- **Weil ground truth.** `n=1` (dual numbers): `D₂ ↔ k[ε₁,ε₂]/(ε₁²,ε₂²,ε₁ε₂)` rank 3,
  `P' ↔` rank `1+1+1=3`; `D₂≅P'`, universality **holds** (∂ is a tangent structure).
  `n=2` (square-zero `k⊕k²`): rank 5 vs 7, universality **fails** — correctly excluded,
  matching Lanfranchi–Lemay's "only `r∈{0,1}`".
- **Finiteness is sharp.** `n = ℵ₀` gives `1+2ℵ₀ = ℵ₀ = 1+ℵ₀+ℵ₀²`: the equation *can*
  hold, so universality does not exclude `M = ℕ·y` — exactly the infinite-support
  obstruction (companion §3). Finiteness is load-bearing, as it must be.
- `scratch/verify_universality_counts.py` — all checks pass, `n = 0..5`.

## 6. Gaps / scope

- **Cited (standard):** the universality-of-the-vertical-lift axiom (CC 2014) and the
  Gambino–Kock connected-limit preservation. Both are framework facts, not the
  contested content.
- **Cited (mine, proved):** the base-change framework
  (`tangent-restricts-to-dcont.json#root`), Lemma 0 / Lemma 1 of the companion note,
  and `M` linear from the additive-bundle axiom (companion §2).
- **First order only** (as are AAGM `∂`, L–L, CCGZ §1–4). Higher Weil algebras
  `ℕ[ε]/ε^{k}` (`k≥3`) and iterated tangents remain out of scope.

No step uses subtraction or additive inverses. The converse is `proved`.
