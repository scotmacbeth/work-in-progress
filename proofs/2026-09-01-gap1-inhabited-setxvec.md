# Gap 1 is inhabited: `Set × Vec_fd` is ◁-admissible, non-collapse, non-cartesian

**Date:** 2026-09-01. **Grade: `computed`** (scoping agent `scratch/2026-09-01-gap1-hunt.py`
+ MacBeth hand-verification of the crux, below). **NOT yet `proved`** — a full PROVE pass owes:
associativity/coherence of the constructed `◁`, the summability boundary made precise, and the
irreducibility question. Registry: `open-middle-region` in `left-adjoint-over-vec.json`.

## Statement
The base `C = Set × Vec_fd` (product of categories; symmetric monoidal under the componentwise
tensor `⊗ = (×_Set, ⊗_k)`; closed, cocomplete) is a **Gap-1 inhabitant**:
- **◁-admissible** (`Fam(C^op)` closed under composition product `◁`) — on the fd-position locus,
  i.e. the same standard under which the programme already calls `Vec_fd` admissible;
- **non-collapse**: `(A,V)` is copower-tiny iff `A` tiny in Set (`|A|≤1`) AND `V` tiny in `Vec_fd`;
  positions with `|A|≥2` are not tiny, so not every object is tiny;
- **non-cartesian**: `⊗_k ≠ ⊕` (the product in `Vec` is the biproduct), so `⊗ ≠ ×`.

**Consequence: Theorem B is NOT SHARP.** Its conclusion (admissibility ⟹ unit connected) fails on
`Set × Vec_fd`: the unit is `(1, k)`, and `C(I,−) = Set(1,−) × Vec(k,−)` does not preserve
coproducts (the `Vec` factor sends `⊕` to the underlying product, not the coproduct of sets). So the
base is **admissible with a disconnected unit** — which the extensive pole forbids. The extensive
pole is therefore a **sufficient** condition for the one-bit rigidity, not a **characterisation**.

## The crux, hand-verified (why `Set×Vec` is admissible while `Set×Set` is NOT)
Extension over the closed base `C`: for `p = (S, (A_s, V_s)_s)`,
`⟦p⟧(X,Y) = ∐_{s} [ (A_s,V_s), (X,Y) ] = ( ⊔_s X^{A_s},  ⊕_s [V_s, Y]_k )`
(coproduct in `Set×Vec` is componentwise `(⊔, ⊕)`; internal hom is componentwise `(X^A, [V,Y]_k)`).

Compose with `q = (T, (B_t, W_t)_t)`:
- **Set component** = `⊔_s (⊔_t X^{B_t})^{A_s} = ∐_{s,\,f:A_s→T} X^{Σ_{a∈A_s} B_{f(a)}}`
  (Set distributivity). This is representable and its **shape set `∐_s T^{A_s}` is FORCED** — `Set` is
  full/faithful/extensive, so `⟦−⟧` is injective on objects there and the shape set is determined.
- **Vec component** = `⊕_s [V_s, ⊕_t [W_t, Y]] = ⊕_s ⊕_t [V_s, [W_t,Y]] = ⊕_{s,t} [V_s⊗W_t, Y]`
  (`V_s` fd ⟹ `[V_s,−]` preserves `⊕`; then hom–tensor adjunction `[V,[W,Y]] = [V⊗W,Y]`).

For a single container `r = (D, (C_d, U_d)_d)` to present this composite, its Set-positions and
Vec-positions share **one** index set `D`. Take `D = ∐_s T^{A_s}` (the forced Set shape set), with
`C_{(s,f)} = Σ_a B_{f(a)}` (forced). For the Vec-positions, use **biproduct collapse**: in `Vec`,
`⊕_i [U_i,Y] = [⊕_i U_i, Y]`, so the entire Vec sum fits in **one** slot —
pick any `d_0∈D`, set `U_{d_0} = ⊕_{s,t} V_s⊗W_t` and `U_d = 0` otherwise
(`[0,Y] = 0` contributes nothing to `⊕`). Then
`⊕_{d∈D}[U_d,Y] = [U_{d_0},Y] = ⊕_{s,t}[V_s⊗W_t,Y]` — matches. ∎(crux)

**Contrast with `Set×Set` (Prop 9.1, inadmissible):** there BOTH factors are full/rigid, so BOTH
force their own shape sets `∐_s T^{A_s}` and `∐_s T^{A'_s}`, which differ when `A_s ≠ A'_s`, and
neither can absorb the other — no single `D` works. The operative dichotomy is **rigid
(fully-faithful) vs flexible (collapse, non-full) factors**, NOT cartesianness and NOT `I₁⊗I₂≅0`.

## Why the emptiness lead is dead (Task B)
The recorded lead — "if `I ≅ I_1⊔I_2` in closed monoidal `C` and `I_1⊗I_2≅0`, Theorem B runs
verbatim without cartesianness" — is **broken regardless of `I_1⊗I_2`**. Theorem B's contradiction
also runs through **Lemma E2**, which needs a **nonzero terminal on both factors**; a collapse factor
has `1_C ≅ 0`, so `1 = E·1` degenerates to `0 = 0`, vacuous — the obstruction evaporates. And
`Set×Vec` has `I_1⊗I_2 = 0` anyway (its split unit `(1,k) = (1,0)⊔(0,k)`, cross term `(0,0)=0`) yet
is admissible + disconnected. So `I_1⊗I_2≅0` is neither the obstruction nor a separator.

Separately (Task B, abstract): `I_1⊗I_2≅0` is **not forced** by unit-splitting alone — it needs
extensivity (`B→I` through both injections ⟹ `B→0` ⟹ `B=0`) or additivity (`e_1e_2 = 0`). No
counterexample constructed; Day-convolution bases have indecomposable unit (no split). Open in the
abstract but not the crux.

## Caveats (honest)
1. **Reducible.** `Set×Vec_fd` is a **product** base. It settles the *named* Gap-1 hole but the
   sharper question is whether an **irreducible** (non-product) Gap-1 inhabitant exists. The `rigid ×
   flexible` mechanism suggests looking at bases that are *internally* a mix — e.g. a recollement, or
   modules over a ring with both a field quotient and a nontrivial nilpotent/idempotent structure.
2. **Summability boundary.** The Vec absorption uses `⊕_i[U_i,Y]=[⊕U_i,Y]` with `U_i` fd; if
   `⊕_{s,t}V_s⊗W_t` is infinite-dimensional it leaves `Vec_fd` — the same T2/left-adjoint summability
   boundary. So the clean statement is over `Vec_fd` with the finiteness proviso; full `Vec` inherits
   its own non-admissibility. State the locus precisely in any write-up.
3. **Grade.** `computed`. Crux hand-verified (natural isos, not cardinality). Full `◁`
   construction + coherence + the summability statement need a PROVE pass before `proved`.
