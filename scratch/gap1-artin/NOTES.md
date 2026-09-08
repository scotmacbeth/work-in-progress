# PROVE 2026-08-31 — Gap 1 / Artin gluing Gl((−)²)

## Opening move (before any computation): identify the object

`Gl(T) = (Set ↓ T)`, `T = (−)²`. An object is `(A, B, β : A → B²)`.
Rename: `B` = vertices, `A` = edges, `β = (source, target)`.
A morphism `(f,g)` with `β' f = g² β` is exactly `(s'(fa), t'(fa)) = (g(sa), g(ta))`.

> **`Gl((−)²)` IS THE CATEGORY OF DIRECTED MULTIGRAPHS**, i.e. the presheaf topos
> `Graph = [G^op, Set]`, `G = {V, E; s,t : V → E}`.

Consequences, immediately:
- It is a **presheaf topos**, hence **infinitary lextensive**.
- ⟹ the 2026-08-26 §4(v) claim "`Gl(T)` … **non-extensive**" is **WRONG**.
  The stated reason ("`T(B⊔B') ≠ TB ⊔ TB'`") confuses *`T` preserves coproducts* with
  *the glued category is extensive*. Extensivity of `(𝓕↓T)` needs only that colimits are
  componentwise and `T` preserves pullbacks — both hold.
- ⟹ **`Gl((−)²)` is not a Gap-1 candidate at all.** It sits on the extensive pole.

So the session's stated target evaporates in the first ten minutes. What survives is the
*question*: apply Lemma S to it anyway. Because now Lemma S is being applied to a
lextensive ccc with **connected unit** — the regime where Theorem B has nothing left to say.

## What the computation says (all verified, `presheaf.py` + `psh2.py`)

| base `C` | `= [D^op,Set]` | Lemma S | `π₀` mult. | admissible |
|---|---|---|---|---|
| `Set` | `D = 1` | ✓ | ✓ | ✓ |
| Sierpinski `Set^→` | `D = (0→1)` | ✓ 30/30 | ✓ | ✓ |
| `Idem`-sets | walking idempotent | ✓ 30/30 | ✓ | ✓ |
| **reflexive** graphs | `Δ_{≤1}` | ✓ 30/30 | ✓ | ✓ |
| **`Graph` = `Gl((−)²)`** | `V ⇉ E` | **✗** | **✗** | **✗** |
| `Z/2`-Set | `D = Z/2` | **✗** | **✗** | **✗** |

Smallest witness in `Graph`: `P = y(V)` (ONE vertex, no edges), `T = 2`.
`[y(V), Z]` = complete graph on `Z_V` **with all loops**; so `[y(V), 2·1]` has
**2 vertices and 4 edges**, while every copower `D·1` (= disjoint loops) has `#V = #E`.
`2 ≠ 4`. Lemma S fails. **`Gl((−)²)` is NOT `◁`-admissible.**

`Z/2`-Set is a **cardinality collision**: `|[y,2·1]| = 4 = |Δ4|`; only the *action* separates them.
The refinement+backtracking `iso_bt` catches it; a count would not. (Discipline #1 earned again.)

## The three things this turned into
1. `Gl((−)²) ≅ Graph` is a **presheaf topos** ⟹ lextensive. 08-26 §4(v) "non-extensive" is WRONG.
2. `Graph` has **connected unit** and **fails Lemma S** ⟹ Cor B″'s three-way equivalence is FALSE.
3. Lemma S is **SUFFICIENT** on the extensive pole (proof below), and equals
   "`π₀` preserves finite products" = **strong connectedness**. Gap 2 closes there.
