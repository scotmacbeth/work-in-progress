# LEAN 2026-08-14 — The Disjointness Lemma, formalised in full generality

**File:** `lean/Containers/Containers/Disjointness.lean` (root-wired, `lake build`
green, 55 jobs, 0 warnings). Sorry-free; `#print axioms` = `[propext]` only.

**Registry:** node `disjointness-lemma` in `holonomy-composition-zs-bridge.json`
promoted `proved → lean-verified`; `lean` field =
`Containers.Disjointness.disjointness`.

## What is machine-checked

**Lemma 1 (Disjointness).** For an internal exact factorisation `G = P·Q`
(subgroups `P, Q` with `P ∩ Q = {e}` and every `g` factoring as `p·q`) and
**every** `g ∈ G`,
```
        P ∩ g Q g⁻¹ = {e}.
```

This is the general group-theoretic backbone of the emergent-holonomy
meeting-points theorem (`proofs/2026-08-13-emergent-holonomy-meeting-points.md`,
Lemma 1 + Cor 1.1): it forces every `(A,B)`-double coset in `U = Stab_G(s)` to
have uniform size `|A|·|B|`, so `h(s) = |U|/(|A|·|B|) = #(A\U/B)` is an honest
positive integer.

**Key point for the grant story:** the *witness* was already Lean'd
(`EmergentHolonomy.lean`, `S₃`). This is the FIRST **general** step of the whole
bridge to be machine-checked — arbitrary group, no finiteness, no action, no
fixed point. That is exactly the "one genuinely general, Mathlib-friendly step"
LEAN.md flagged.

## How it is encoded (and why Mathlib-free)

The whole `Containers` project deliberately carries no Mathlib dependency (there
is no Mathlib on the machine; `EmergentHolonomy.lean` hand-rolls `S₃`). So I
hand-rolled:

- `class Group` — `Mul`/`One`/`Inv` + assoc/one/inv-cancel laws.
- `structure Subgroup` — a `mem : G → Prop` predicate closed under `1, *, ⁻¹`.

Derived group lemmas (`inv_mul_cancel_left`, `mul_inv_cancel_left`,
`mul_inv_rev`, `inv_eq_of_mul_eq_one_left`), all `@[simp]`.

The two crux calculations:
- `conj_pivot : p⁻¹ * ((p*q)*z*(p*q)⁻¹) * p = q*z*q⁻¹` — pure group word, closes
  by `simp only [mul_inv_rev, mul_assoc, inv_mul_cancel_left, inv_mul_cancel,
  mul_one]` (right-associate + cancel adjacent inverse pairs).
- `pivot_recover : p * (p⁻¹ * a * p) * p⁻¹ = a`.

`disjointness` then observes the pivot `p⁻¹·a·p` lies in `P` (closure) and,
via `conj_pivot`, in `Q`; trivial intersection ⟹ pivot `= 1`; `pivot_recover`
⟹ `a = 1`. `disjointness_iff` packages the clean `P ∩ gQg⁻¹ = {e}` set form.

## Note for a Mathlib port (future)

The natural Mathlib version replaces `Group`/`Subgroup` by `Subgroup G` /
`IsComplement (P : Set G) Q` and derives Cor 1.1's double-coset size from
`Mathlib.GroupTheory.DoubleCoset` (`Doset`). The mathematical content is
identical — this hand-rolled proof transfers line-for-line once the group API is
Mathlib's. It is general enough to be a Mathlib contribution (pure finite/any
group theory, no container content).

## Gotcha logged

`set … with …` is a **Mathlib tactic** — unavailable in a Mathlib-free project.
It parsed as "unknown tactic". Rewrote using explicit `p⁻¹ * a * p` throughout.
(Same class of trap as any Mathlib-only tactic in this repo: `decide` is fine —
it is core — but `group`, `set`, `omega`-heavy chains, `ring` are not.)
