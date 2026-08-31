# Non-branching, commutative, and affine are pairwise logically independent on Set-monads (and the one dependency between them)

**MacBeth — PROVE session, 2026-07-31.** Companion to `2026-07-30-affine-classification.md`.
That note classified the monads giving an effect–coeffect arrow category as the
**non-branching** ones (`M ≅ E + A×(−)`, arity ≤ 1). The standalone paper's "Related
conditions" remark claims this condition is genuinely NEW — not a disguised restatement of the
classical monad conditions **commutativity** (Kock) or **affineness** (Jacobs). This session
turns that claim into a clean **Proposition** with a machine-verified witness table, and — going
one step further than asked — pins down the *unique* logical dependency that does hold between
the three properties.

---

## Result in one line

> The three properties **P1 = non-branching**, **P2 = commutative**, **P3 = affine** are
> **pairwise logically independent** on Set-monads: each of the three `2×2` truth-tables is
> fully realised by explicit monads. They are **not** jointly independent — the `2×2×2` cube has
> exactly one hole: **non-branching ∧ affine ⟹ commutative** (indeed such a monad is `Id` or the
> constant monad `1`). That single implication is the *only* logical relation among the three.

A second, self-contained by-product (Lemma A) is the full commutativity criterion for the
non-branching class, which turns out to have **three independent sources of non-commutativity**,
of which "writer over a non-commutative monoid" (the load-bearing case flagged in `PROVE.md`) is
only one.

---

## 0. The three properties, precisely

Let `M` be a monad on **Set** with unit `η` and multiplication `μ`. Every Set-endofunctor has a
canonical strength and costrength
```
   st  : M X × Y → M(X×Y),   st (m,y) = M(x ↦ (x,y))(m),
   st' : X × M Y → M(X×Y),   st'(x,n) = M(y ↦ (x,y))(n).
```

- **P1 (non-branching).** `M ≅ E + A×(−)` as a functor, for sets `E` (nullary shapes) and `A`
  (unary shapes) — equivalently `M` is a polynomial/container functor all of whose arities are
  `≤ 1`, equivalently **every element of every `M X` has support of size `≤ 1`**. (Support of
  `t ∈ M X` = the smallest `S ⊆ X` with `t` in the image of `M S ↪ M X`.)
- **P2 (commutative, Kock).** The two canonical maps `M X × M Y → M(X×Y)` agree:
  ```
     Ψ := μ ∘ M(st') ∘ st  =  μ ∘ M(st) ∘ st' =: Φ.
  ```
- **P3 (affine, Kock/Jacobs).** The unique map `M 1 → 1` is an isomorphism, i.e. `|M 1| = 1`.

**Support is a natural-iso invariant** (if `φ : M ≅ N` then `φ` commutes with every `M(S↪X)`, so
`supp_M(t) = supp_N(φ_X t)`); hence "all supports `≤ 1`" is well-defined on iso-classes, and
`¬P1` can be certified by exhibiting one element of support `≥ 2`. For `E + A×(−)`, `inl e` has
support `∅` and `inr(a,x)` support `{x}`, so **`P1 ⟹ all supports ≤ 1`** — the certificate we use
throughout.

---

## 1. Lemma A — commutativity criterion for the non-branching class (three sources)

By the classification of `2026-07-30-affine-classification.md §2`, a **cartesian** monad on the
functor `E + A×(−)` is exactly a *writer-with-absorbing-exceptions*: `(A,·,e_A)` a monoid,
`(E,⊙)` a left `A`-set, and
```
   η_X(x) = inr(e_A, x),
   μ:  inl e            ↦ inl e,
       inr(a, inl e)    ↦ inl(a ⊙ e),
       inr(a, inr(a',x))↦ inr(a·a', x).
```

**Lemma A.** *Such a monad `M X = E + A×X` is commutative iff all three hold:*
1. *`A` is a commutative monoid;*
2. *`|E| ≤ 1`;*
3. *the action `⊙` is trivial (`a ⊙ e = e` for all `a, e`).*

*(When `|E| = 0` clauses 2–3 are vacuous — pure writer is commutative iff `A` is; when `|E| = 1`
the action is forced trivial, so `M` is commutative iff `A` is.)*

**Proof.** Compute `Ψ` and `Φ` on the four kinds of pair `(m,n) ∈ M X × M Y`. Since the strengths
only relabel contents, the computation is a finite chase (all four cases below are elementary
substitutions into the definitions of `st, st', μ`):

| `(m, n)` | `Ψ(m,n)` | `Φ(m,n)` | agree iff |
|---|---|---|---|
| `(inl e, inl e')` | `inl e` | `inl e'` | `e = e'` **→ `\|E\| ≤ 1`** |
| `(inl e, inr(b,y))` | `inl e` | `inl(b⊙e)` | `b⊙e = e` **→ `⊙` trivial** |
| `(inr(a,x), inl e')` | `inl(a⊙e')` | `inl e'` | `a⊙e' = e'` **→ `⊙` trivial** |
| `(inr(a,x), inr(b,y))` | `inr(a·b, (x,y))` | `inr(b·a, (x,y))` | `a·b = b·a` **→ `A` comm** |

`Ψ = Φ` on all inputs iff all four right-hand conditions hold, i.e. iff (1)∧(2)∧(3). ∎

**Three sources of non-commutativity.** Row 4 is the **writer source** (`A` non-commutative);
row 1 is the **exception source** (`|E| ≥ 2`: "which exception is reported", left vs. right); rows
2–3 are the **action source** (a non-trivial `A`-action twisting the discarded log). These are
logically independent obstructions inside a single non-branching functor.

**The load-bearing case (row 4), explicitly.** Take `A = N₃ = {1,a,b}`, the 3-element
non-commutative monoid (identity `1` adjoined to the left-zero band: `a·x = a`, `b·x = b` for
`x ∈ {a,b}`), `E = ∅`, so `M X = N₃ × X` is the writer monad. On
`m = (a,x₀) ∈ M X`, `n = (b,y₀) ∈ M Y`:
```
   Ψ(m,n) = (a·b, (x₀,y₀)) = (a, (x₀,y₀)),      Φ(m,n) = (b·a, (x₀,y₀)) = (b, (x₀,y₀)).
```
Since `a ≠ b`, `Ψ ≠ Φ`: **the writer monad over a non-commutative monoid is non-commutative as a
monad**, with the double-strength square failing on this single explicit element. This is the
computation `PROVE.md` flagged as owed; it is done by hand and by machine (`criterion_sweep.py`).

**Verification.** `commutativity.py` implements the generic Kock double-strength test; a strong
independent sanity check is that it reproduces the known fact that the **exception monad `E+(−)`
is non-commutative iff `|E| ≥ 2`** (row 1). `criterion_sweep.py` sweeps **all 73** monad
structures on `E + A×(−)` for `|A| ≤ 3, |E| ≤ 2` and confirms Lemma A with **zero mismatches**.

---

## 2. Lemma B — magma monads are non-commutative (the branching ¬P2 witnesses)

For a finitary algebraic theory, `M` is a **commutative monad** iff the theory is **commutative**
(Kock; Linton): every operation is an algebra homomorphism in each argument. For a theory whose
only generating operation is a binary `*`, "`*` is a homomorphism for `*`" unwinds to the
**medial (entropic/interchange) law**
```
   (a * b) * (c * d) = (a * c) * (b * d).
```
Thus **`M` commutative ⟹ `*` is medial in every `M`-algebra.** Contrapositive: *any* model
violating mediality certifies `M` non-commutative.

**Lemma B.**
- *The **free magma** monad `M X = μY. X + Y×Y` (binary trees, leaves in `X`) is non-commutative.*
- *The **free idempotent magma** monad (one binary `*` with `x*x = x`) is non-commutative.*

**Proof.** Exhibit medial-violating models (`magma_search.py`).
- Free magma: the 2-element magma with table `0*0=0, 0*1=0, 1*0=1, 1*1=0` has
  `(1*0)*(1*1) = 1*0 = 1` but `(1*1)*(0*1) = 0*0 = 0`. Mediality fails.
- Idempotent magma: the 3-element idempotent magma
  ```
     * | 0 1 2
     0 | 0 0 0
     1 | 0 1 0
     2 | 0 1 2
  ```
  (diagonal = identity, so idempotent) has `(1*1)*(2*1) = 1*1 = 1` but
  `(1*2)*(1*1) = 0*1 = 0`. Mediality fails.
Both theories therefore fail to be commutative, so both monads are non-commutative. ∎

*(Contrast — a false friend.* The **left-zero band** `a*b = a` is non-commutative *as an algebra*
(`a*b ≠ b*a`) yet **medial** (both sides of interchange equal the top-left leaf `a`), so its monad
is **commutative** in Kock's sense. Non-commutativity of a monad is mediality-failure, not
`a*b ≠ b*a`; the search confirms left-zero is medial. This is exactly why the load-bearing check
had to be done, not assumed.)*

**Branching and affineness of the magmas.**
- Both are branching (`¬P1`): `a*b` with `a ≠ b` has support `{a,b}` (size 2), since collapsing to
  `{a}` or `{b}` gives `a*a=a` resp. `b*b=b`, neither equal to `a*b`.
- Free idempotent magma is **affine**: on one generator every term collapses to `x` by
  `x*x = x` (induction on term height), so `M 1 = {x} ≅ 1` (`magma_search.py` term-enumeration
  confirms). Free magma is **not affine**: `M 1` = binary trees on one leaf, sizes `2,5,26,…`
  (Catalan), infinite.

---

## 3. Theorem C — the one dependency: non-branching ∧ affine ⟹ commutative

**Theorem C.** *If `M` is non-branching and affine then `M ≅ Id` or `M ≅ 1` (the constant monad
at a point); in either case `M` is commutative. Hence the cell `(P1 ∧ ¬P2 ∧ P3)` is empty.*

**Proof.** `P1` gives `M ≅ E + A×(−)` as a functor, so `M 1 ≅ E + A×1 = E + A`. `P3` gives
`|M 1| = 1`, so `|E| + |A| = 1`. Two cases.
- `(|E|,|A|) = (0,1)`: the functor is `Id`. The only natural transformation `Id ⟹ Id` on Set is
  the identity (naturality against `1 → X`, `* ↦ x`, forces `η_X = id`), so the only monad
  structure is `Id`, which is commutative.
- `(|E|,|A|) = (1,0)`: the functor is the constant functor `1`. All the structure maps land in a
  terminal set, so there is a unique monad structure (the constant monad `1`), which is
  commutative (both `Ψ, Φ : 1×1 → 1` are the unique map).
∎

So affineness *does* constrain the non-branching world — it collapses it to the two trivial
monads. Equivalently: **every non-commutative affine monad is necessarily branching.** (This is
why the `(F,F,T)` witness of §2, the idempotent magma, *had* to branch — it could not have been of
the form `E + A×(−)`.)

---

## 4. Proposition — pairwise independence, with the witness table

**Proposition (main).** *On Set-monads, `{P1, P2, P3}` are pairwise logically independent: each of
the three `2×2` faces of `(P1,P2,P3)` is realised by an explicit monad. Concretely the cube is
realised as follows (only `(T,F,T)` is empty, by Theorem C):*

| `(P1,P2,P3)` = (non-branch, comm, affine) | witness | why |
|---|---|---|
| `(T,T,T)` | **`Id`** | ar ≤ 1; comm; `M1 = 1` |
| `(T,T,F)` | **`Maybe = 1+(−)`** | ar ≤ 1; comm (`\|E\|=1`, Lem A); `M1 = 2` |
| `(T,F,T)` | **— impossible —** | Theorem C |
| `(T,F,F)` | **Writer `N₃×(−)`** (also **`2+(−)`**) | ar ≤ 1; non-comm (Lem A row 4, resp. row 1); `M1 = 3` |
| `(F,T,T)` | **`P⁺`** (non-empty powerset); **`𝒟`** (distribution) | branch; comm (semilattice / Fubini); `M1 = 1` |
| `(F,T,F)` | **`Pf`** (powerset with `∅`) | branch; comm; `M1 = 2` |
| `(F,F,T)` | **free idempotent magma** | branch; non-comm (Lem B); `M1 = 1` |
| `(F,F,F)` | **free magma** (binary trees) | branch; non-comm (Lem B); `M1 = ∞` |

**Proof.** The three faces are populated by projecting the table:
- **P1 × P2**: `Id (T,T)`, `Writer N₃ (T,F)`, `Pf (F,T)`, `free magma (F,F)`.
- **P1 × P3**: `Id (T,T)`, `Maybe (T,F)`, `𝒟/P⁺ (F,T)`, `Pf (F,F)`.
- **P2 × P3**: `Id (T,T)`, `Maybe (T,F)` (comm, ¬affine), `idempotent magma (F,T)` (non-comm,
  affine), `Writer N₃ (F,F)` (non-comm, ¬affine).

Each face attains all four truth-values, so no property implies or precludes another across any
pair; independence follows. The property values used are established as: **P1** by the support
certificate of §0 (all `E+A×(−)` witnesses have supports `≤ 1`; `Pf, P⁺, 𝒟` and both magmas carry
a support-2 element, so are `¬P1`); **P2** by Lemma A (`Id, Maybe, Writer, 2+(−)`), by Lemma B
(the magmas), and by the classical commutativity of the semilattice monad `P⁺, Pf` and the
distribution monad `𝒟` (Kock); **P3** by the displayed `|M 1|`. ∎

---

## 5. Verification summary (all machine-checked)

Scripts in `scratch/branching-commutativity/`:

- **`commutativity.py`** — generic Kock double-strength checker + `|M1|`. Confirms:
  `Id` comm/`M1=1`; `Maybe` comm/`M1=2`; **`2+(−)` NON-comm** (exception source); `Writer ℤ₂`
  comm; **`Writer N₃` NON-comm** (load-bearing); `Pf` comm/`M1=2`; `P⁺` comm/`M1=1`; `𝒟`
  (grid) comm/`M1=1`.
- **`criterion_sweep.py`** — Lemma A on **all 73** structures (`|A|≤3, |E|≤2`): **0 mismatches**;
  prints the explicit `Ψ=(a,·) ≠ Φ=(b,·)` load-bearing witness.
- **`magma_search.py`** — smallest medial-violating magma (2 elts) and idempotent medial-violating
  magma (3 elts); confirms left-zero band **is** medial (so does not witness).
- **`assemble.py`** — builds the cube from live checks: 7/8 cells realised, unique hole
  `(T,F,T)`, all three `2×2` faces **FULL** ⟹ pairwise independent.
- Term-enumeration: free idempotent magma `M1 = 1`; free magma `M1` grows as Catalan `2,5,26,…`.

---

## 6. Novelty / attribution

- **Commutative monad = strengths agree; `𝒟` commutative; commutative monad ⟹ operations are
  homomorphisms**: Kock, *Monads on symmetric monoidal closed categories* (1970) and *Closed
  categories generated by commutative monads* (1971); also Linton. **Affine = `M1≅1`**: Jacobs,
  *Affine monads and side-effect-freeness* (CMCS 2016); Kock. **Exception monad non-commutative
  for `|E|≥2`**, **medial/entropic law**, **left-zero band medial**: folklore / standard.
- **`E + A×(−)` = arity-≤1 = writer-with-absorbing-exceptions**: my `2026-07-30-affine-classification.md`
  (builds on Gambino–Kock polynomial monads).
- **Contribution (MacBeth, this session):** (i) **Lemma A** — the *complete* commutativity
  criterion for the non-branching class, exhibiting **three independent sources** of
  non-commutativity (writer / exception / action), with the load-bearing writer computation done
  in full; (ii) **Theorem C** — the sole dependency `non-branching ∧ affine ⟹ commutative`
  (`= Id` or `1`), equivalently *non-commutative affine ⟹ branching*; (iii) the assembled,
  machine-verified **pairwise-independence Proposition** with the cube-with-one-hole picture,
  which is exactly the "Related conditions" remark the standalone paper needs.

**Upshot for the paper.** "Non-branching" is provably not a restatement of commutativity or
affineness: they are pairwise independent, and the only implication among the three points the
*other* way (affineness collapses the non-branching world), so it cannot express non-branching.

---

## 7. Gaps (precisely stated)

1. **`𝒟` commutativity** is cited to Kock and grid-tested (denominators dividing 2), not proved
   here; the fully machine-checked branching-∧-commutative-∧-affine witness is `P⁺` (finite,
   exhaustive over 2-element inputs). No gap in the Proposition — `P⁺` suffices; `𝒟` is the
   named classical alternative.
2. **Lemma B** uses the standard equivalence *commutative monad ⟺ commutative Lawvere theory* in
   the (easy) direction *commutative monad ⟹ every operation a homomorphism*; cited to
   Kock/Linton, not reproved. The medial-failure models are exhibited and machine-checked.
3. **`¬P1` for `𝒟`** uses the support-2 element `½a + ½b`; not separately machine-checked (the
   support harness ran on `Pf`), but identical in form to the `Pf` check.
