# Scoping note — `theorem-general-stabilizer-necessity`

**MacBeth — 2026-09-07 (scoping only; NOT a proof attempt).**
Target: decide whether the correlated-swap stabilizer mechanism that closed the `U`-corner
(`proofs/2026-09-07-U-corner-resolved-stabilizer.md`) generalises to give THM 3 necessity —
*`M`-containers compose ⟹ `M` polynomial* — **uniformly for every non-flat analytic monad**,
retiring the plethysm engine (Theorem P, `2026-09-06-lemmaN`) and the degree engine (Theorem S).

Sources cited by line: `U` = `2026-09-07-U-corner-resolved-stabilizer.md`;
`P` = `2026-09-06-lemmaN-plethysm-cancellation.md`; `R0` = `2026-09-05-lemmaN-retract-and-beta.md`.

---

## (a) PRECISE STATEMENT

**Non-flat analytic monad.** `M = Ã`, `Ã(X)=Σ_{n≥0} A[n]×_{S_n}X^n`, `A[n]` finite `S_n`-sets
(`P` §0). `M` polynomial ⟺ `A` flat ⟺ every `S_n`-action on `A[n]` is free (`P` (J2), (C2)).
**Non-flat** = some non-identity `σ∈S_k` (`k≥1`) fixes some `t∈A[k]`. Equivalently `Z_A` has a
monomial `p_λ`, `λ≠(1^n)` (`P` (C2)); equivalently `Ã` does not preserve wide pullbacks
(`R0` §0, (J2)).

**Single-`M`-element stabilizers.** On the each-label-once species component `[m]` (`U` §1, `U` Rmk
lines 79–87), for `u∈M[β]` with content exactly the block `β⊆[m]`, `Stab_{M[β]}(u)⊆Sym(β)`.

**`𝒫_M` (block-fixing products).** `𝒫_M[m] := { ∏_{β∈π} Stab_{M[β]}(u_β) : π ⊢ [m],\ u_β∈M[β] }`,
up to `S_m`-conjugacy (`U` §1 Meta-theorem lines 55–67; `U` §5 line 192). The Meta-theorem
(`U` lines 55–72, one-line proof "a function is fixed iff fixed pointwise") states: **every**
point-stabilizer occurring in `(⟦r⟧∘M)[m]`, for `⟦r⟧` polynomial, lies in `𝒫_M[m]`. No two parts
are ever permuted.

**Correlated swap / the conjecture.**
> **Conjecture (general stabilizer necessity).** For every non-flat analytic monad `M`, there exist
> `m` and a point `w∈(M∘M)[m]` (each label once) whose stabilizer `Stab(w)∉𝒫_M[m]`. Hence
> (`U` Cor. lines 74–76) `M∘M≇⟦r⟧∘M` for all polynomial `⟦r⟧`, so `M`-containers do not compose.

**"Escape `𝒫_M`" made group-theoretic (proposed sharpening).** Use the finest support-splitting
(`P` Lemma S1, lines 158–170): every `K` factors uniquely as a direct product `∏_t K_t^*` of
**support-indecomposable** factors, and the degree-multiset `{|C_t^*|}` is a conjugacy invariant.
Since a block-fixing product `∏_β Stab(u_β)` is *already* a support-splitting, its indecomposable
factors are exactly `⋃_β {indecomposable factors of Stab_{M}(u_β)}`. Define

> **`𝒬_M := {support-indecomposable factors (as abstract permutation groups, with degree) of
> single-`M`-element stabilizers `Stab_{M[k]}(u)`, over all `k`, all `u∈M[k]`}`.**

Then `H∈𝒫_M ⟹` every indecomposable factor of `H` lies in `𝒬_M`. **Sound escape criterion:**
> `(M∘M)[m]` realises a stabilizer with a support-indecomposable factor `∉ 𝒬_M ⟹ that stabilizer
> `∉ 𝒫_M ⟹` `M`-containers don't compose.

This is *exactly* how both proven witnesses work: `⟨(01)(23)⟩` is support-indecomposable of degree
4, order 2, and no single-`U`-structure of degree 4 has such a factor (only `D_4` order 8, or a
support-*decomposable* caterpillar transposition) — `U` §3; and `(S_2×S_2)≀S_2` (order 32,
support-indecomposable) is not among the single-8-leaf-tree factor orders `{8,128}` — `U` lines
170–176. The whole general theorem reduces to: **non-flat `M ⟹ M∘M` realises an indecomposable
stabilizer factor outside `𝒬_M`.**

---

## (b) WHAT THE `U`-PROOF USED: unit-specific vs. generic

**Generic (survives for all `M`):**
1. The Meta-theorem and Corollary (`U` §1) — hold for *any* endofunctor `M` (`U` lines 55–56, 188).
2. Lemma E, the per-component stabilizer invariant (`U` §0 lines 41–47; `R0` §4.1). Convergence-free,
   `a_0`-agnostic — the reason it reaches `a_0=1` where plethysm (Theorem P) diverges (`U` §0
   lines 30–38).
3. The escape shape: **swap two equal composite blocks**; a polynomial outer layer is rigid on
   parts (`U` §1), so `M∘M`'s block-swap is the "irreducibly second-order symmetry" it cannot
   forge (`U` lines 136–139, 203–208).

**Unit-specific (the load-bearing step that does NOT obviously generalise):**
The construction of a **rigid block**. In `U`, `W_L=μ(V_0,μ(V_2,E'))` is rigid (trivial stabiliser)
*because* the inner unit `E'` is a content-free peg of a shape distinct from a leaf, breaking the
last cherry symmetry (`U` lines 110–115, 162–165, 18–20). This is decisive: with symmetric cherries
`μ(V_0,V_2)` the composite `w` has stabiliser `S_2≀S_2=D_4∈𝒫_U` (a *single*-`U`-element stabiliser),
which does **not** escape (`U` §4 lines 162–165). Escape needs the swap group to be *anomalously
small at its degree* (order 2 at degree 4), and only a rigid block delivers that.

**Sharp diagnosis.** No pure-leaf commutative binary tree over distinct labels is rigid: the bottom
cherry `μ(V_i,V_j)` is always fixed by the relabelling transposition `(ij)` (commutativity +
relabelling). Rigidity in `U` *requires* a shape-distinct nullary peg — i.e. `a_0>0`. The peg `E'`
is literally the `A[0]` constant. **So the `U` route is really the `a_0>0` route**, and the constant
`c_0∈M∅` (guaranteed by `a_0>0`) is the general form of the peg.

**Does non-flatness alone give a rigid block to swap? No — not directly.** Every monad has singletons
`A[1]≠∅` (`P` (C3)), which are rigid but size 1; swapping two singletons yields a bare transposition,
which is in `𝒬_M` whenever `M` has any degree-2 symmetric structure — it does **not** escape. Escape
needs a rigid block of **size ≥ 2**, and non-flatness per se does not supply one. Two sources do:
(i) `a_0>0` (constant peg, the `U` mechanism), or (ii) a size-degree/order mismatch that makes even a
*non-rigid* swapped block escape (the unit-free `n=8` route, `U` lines 170–176; = `P` Lemma S2
block-linking, lines 184–193).

---

## (c) INDUCTION / STRATEGY

**Recommended split (honest, and matches what is already proved):**

- **`a_0=0`:** *already closed uniformly and cleanly by plethysm right-cancellation* (Theorem P,
  `P` §2, lines 112–145) — no bound on degree or wreath depth. The stabiliser method reproves this
  (unit-free `n=8`, `U` lines 170–176) but offers **no advantage**. **Do not re-derive `a_0=0` by
  stabilisers.**

- **`a_0>0` (the genuine target; where plethysm diverges, `U` lines 32–36):** generalise the `U`
  constant-peg construction. Fix the constant `c_0∈M∅`. Non-flatness gives an outer `T∈M[k]` and
  `σ≠id∈Stab_{M[k]}(T)` with a cycle `(i_1…i_c)`, `c≥2`. Build `w∈(M∘M)[m]`:
  1. **Rigidify.** For each cycle-slot fill with the *same* rigid composite block `u` of size `e≥2`,
     built from distinct singletons + the peg `c_0` (as `W_L=μ(V_0,μ(V_2,E'))` in `U`).
  2. **Kill spurious symmetry.** Fill all non-cycle slots of `T` with pairwise-distinct rigid
     fillers (or `c_0`) so the only surviving symmetry of `w` is generated by `σ`'s action on the
     `c` equal blocks.
  3. **Read the factor.** `Stab(w)` then has a support-indecomposable factor `F ≅ C_c` (or `⟨σ⟩`
     restricted) acting *block-regularly* on `c·e` points (each block rigid ⟹ no intra-block
     freedom).

  **Key Lemma to prove (the crux):**
  > For suitable choice of `(T,σ,u,e,c)`, the block-regular factor `F` (degree `c·e`, order dividing
  > `|σ|`, `e≥2`) is **not** a support-indecomposable factor of any single-`M`-element stabiliser —
  > i.e. `F∉𝒬_M`.

  For `U`, `c=e=2`, `F=C_2` degree 4: proved (`U` §3). The general Key Lemma is the whole content.

- **Uniform alternative (if a single statement is demanded):** phrase everything through `𝒬_M` and
  the escape criterion of (a); prove "non-flat `⟹` some `(M∘M)`-factor `∉𝒬_M`" by the constant-peg
  construction for `a_0>0` and the degree/order-mismatch (Lemma S2 iterated) for `a_0=0`. This is
  "uniform" only in *statement*; the proof is still two-regime.

---

## (d) WHERE IT LIKELY BREAKS — the crux

**The Key Lemma of (c) is where everything is at risk.** Producing a swap factor `F` is generic;
proving `F∉𝒬_M` is not. Failure modes, hardest first:

1. **"Stabiliser-flat but non-flat" monads.** Suppose `M` is non-flat yet its single-structure
   stabilisers are so rich that *every* correlated-swap wreath `M∘M` can build already occurs as a
   support-indecomposable factor of one `M`-structure. Then `𝒬_{M∘M-on-components} ⊆ 𝒬_M` and the
   mechanism **fails** even if THM 3 necessity is still true (via some other obstruction). Concrete
   worry: an unbounded-degree `a_0>0` monad whose own branching realises block-regular `C_c` factors
   at *all* degrees `c·e`. I could not rule this out on paper. This is the genuine open crux.

2. **Unbounded degree defeats the degree route.** Lemma S2's escape (`P` §3.2–3.3) hinges on the
   swapped factor exceeding `e_max` (`P` lines 195–205). For unbounded-degree `M` there is no
   `e_max`, so route B is unavailable — one is forced onto the rigidity/order route (1), which is
   exactly the unproven Key Lemma.

3. **No usable outer swap.** Non-flatness gives *some* `σ≠id`, but its cycles might be long
   (`c>2` only) or entangled with the rest of `T` so that "isolate a `c`-cycle and rigidify the
   complement" (step 2) is obstructed — e.g. if every non-free `T` has `σ` acting without any
   invariant slot-subset one can rigidify independently. Plausibly always circumventable, but not
   obviously.

4. **Rigid block of size ≥2 may not exist without `a_0>0`.** Confirmed for `U` (b). For `a_0=0`
   this forces route B; if route B is also blocked (unbounded degree, `a_0=0`), only plethysm
   (Theorem P) saves it — which is why I recommend *keeping* Theorem P rather than retiring it.

**Candidate counterexample family to probe:** a finitary analytic **`a_0>0`, unbounded-degree,
unbounded-wreath-depth** monad other than `U` — the corner `2026-09-06` conjectured vacuous but which
`conjecture-V-refuted` shows is **inhabited** (`U` and relatives). Build the free commutative
**unital** magma variants with extra symmetric operations, or the free algebra for a signature with a
constant + a symmetric binary op + a symmetric ternary op, and test whether the constant-peg swap
still escapes, or whether the richer single-structure stabilisers now *contain* the swap factor. If
one such `M` is stabiliser-flat, the uniform mechanism is **false** (though THM 3 may survive).

---

## (e) IS THE GENERAL THEOREM TRUE? — honest assessment

Two distinct claims must be separated:

- **THM 3 necessity itself** ("non-flat analytic `M ⟹` containers don't compose"): **likely-true.**
  Proved for `a_0=0` unconditionally (plethysm cancellation, `P` §2, unbounded everything), for
  bounded degree (`P` §3), for the symmetric-power/`𝕄` class (`R0` §4), and now for the canonical
  `a_0>0`-unbounded inhabitant `U` (`U` §4). No counterexample monad is known in any regime. The
  balance of evidence strongly favours truth.

- **The uniform *mechanism*** ("the correlated swap escapes `𝒫_M` on some species component, for
  *every* non-flat analytic `M`"): **genuinely-open, leaning cautiously true, with a real risk of a
  stabiliser-flat residue.** The mechanism is proven only at two points (`U` `n=4`; free magma
  `n=8`) plus the `𝕄`/symmetric-power class. The Key Lemma (`F∉𝒬_M`) has no uniform proof and I can
  construct no barrier *and* no proof — the honest status is **open**. The hardest obstruction is
  failure mode (d.1): an unbounded-degree `a_0>0` monad rich enough to already contain its own
  self-composite swap factors.

**Recommendation for PROVE.md.** Do **not** aim to retire Theorem P — it is the clean, complete
`a_0=0` argument and the stabiliser method has no edge there. Scope the PROVE target as the **`a_0>0`
Key Lemma**: *for every non-flat analytic monad with `M∅≠∅`, the constant-peg correlated-swap block
`F` (block-regular `C_c`, `e≥2`) lies outside `𝒬_M`.* Attack it via the `𝒬_M`/support-indecomposable
reformulation of (a). First deliverable: settle failure mode (d.1) — either prove "block-regular
`C_c` with `e≥2` is never a single-`M`-structure factor for `a_0>0` finitary analytic `M`" (which
would essentially close the theorem), or exhibit a stabiliser-flat non-flat `M` (which refutes the
uniform mechanism and forces a hybrid). That binary is the crux and the right next computation
(small-case search over signatures with a constant + symmetric ops, `|X|≤6`).

**Rank: THM 3 necessity — likely-true. Uniform correlated-swap mechanism — genuinely-open.**
