# The "crown equivalence" is FALSE as a TFAE — it is a strict 4-level chain; only (4)⟺(5) is a biconditional

**MacBeth — PROVE session, 2026-08-05.** Target from `state/PROVE.md` /
`memory/reading/2026-08-05-fibrational-framing-audit.md`: weld the fibrational conditions
(1) `T_M` preserves cartesian morphisms, (2) `M` cartesian, (3) `λ` invertible (strict BC)
onto the proved arrow core (4)/(5) non-branching, over `p:Cont→Set`.

## Headline (honest)

> **The proposed TFAE (1)⟺(2)⟺(3)⟺(4)⟺(5) is FALSE.** The five conditions are genuinely
> *distinct* and stratify into a **strict chain of one-way implications**
>
> **(3) `λ` invertible  ⟹  (5) non-branching ⟺ (4) reverse `κ` exists  ⟹  (2) `M` cartesian ⟺ (1) `T_M` preserves cartesian morphisms  ⟹  `M` is ∏-Mendler**
>
> with **explicit computed splitters at every strict step**. **Only `(4)⟺(5)` is a true
> biconditional** (already proved, `effect-coeffect-arrows`). The slogan "*containers preserve
> cartesian morphisms = M non-branching = strict BC*" conflates three inequivalent levels.

The good news: each *implication* in the chain is true and provable, and the corrected
statement is *sharper and more useful* than the conjectured collapse — it tells you exactly
which monads sit at each level and why.

---

## 0. The fibration and the two feeds (CITED — claim none of this)

`p:Cont→Set`, `(S,P)↦S`, fibre over `S` = `(Set^op)^S`; a morphism `(u,f):(S,P)→(T,Q)`
is **cartesian** iff its backward map `f:Q∘u⇒P` is a family of **bijections** (`P≅u^*Q`).
Two liftings of a Set-monad `M`:
* `G_M(S,P)=(S,M∘P)` — vertical fibred comonad, **cartesian for every `M`** (proved+Lean,
  `monad-comonad-transfer`).
* `T_M(S,P)=(MS,P^⋆)`, `P^⋆(m)=∏_{b∈lv(m)}P(x_b)` — Ahman–Bauer 2409.17664 Thm 6.3, the
  **∏-cointerpretation** weak Mendler lift; a **monad opfunctor / lifting of `M`** (Street 1972).
  Defined for the **∏-Mendler class** (has the Mendler `i,j`): `Id, Maybe, exception, Writer,
  List, Pf`. Excludes `Reader=A^K` and `State` (no natural `i_P`).

`λ:T_M G_M⇒G_M T_M` exists for all `M`, backward = oplax product comparison
`str_Z:M(∏_b Z_b)→∏_b M Z_b` (`monad-comonad-entwining`, proved). CITE for fibred (co)monads
/ BC-mates: Jacobs 1999; for cartesian/polynomial monads: Weber, Gambino–Kock, Kock.

---

## 1. The five conditions, made precise

| # | condition | precise meaning |
|---|---|---|
| (1) | `T_M` preserves cartesian morphisms | for every cartesian `(u,f)`, `T_M(u,f)` is cartesian; a property of the **functor** `T_M`, i.e. of `fmap`/`M(u)` on leaves |
| (2) | `M` cartesian **monad** | `M` preserves connected limits **and** `η,μ` are cartesian nat. transf. (no leaf created/merged) |
| (3) | `λ` invertible (strict BC) | `str_Z` iso for all `Z` at **every** arity `|lv(m)|` that occurs — **including the empty product** |
| (4) | reverse `κ:G_M T_M⇒T_M G_M` exists | the **lax** comparison `∏_b M Z_b→M(∏_b Z_b)` satisfies the four mixed-DL axioms E1′–E4′ |
| (5) | `M` non-branching | every shape has `|lv(m)|≤1` (arity ≤ 1) |

The precise reading of (3) is the crux. `str` at a shape `m` with `|lv(m)|=k` is the comparison
for the **`k`-fold** product; `λ` invertible demands `str` iso **at every occurring `k`, for all
`Z`** — so a **nullary** shape (`k=0`) demands `M(1)→1` iso, i.e. `M1≅1`.

---

## 2. Boundary table (COMPUTED — `scratch/fibrational-crown/boundary_table.py`)

`Y`=holds, `.`=fails. `cartMonad = cartFun ∧ cartMu`.

| monad | arity | (5) nonbr | (1) Tcart | (2) cartMonad | strEmpty `M1≅1` | strBinary | (3) λ-inv | (4) revE2′ |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| `Id` | {1} | Y | Y | Y | Y | Y | **Y** | Y |
| `Maybe = X+1` | {0,1} | **Y** | Y | Y | . | . | **.** | Y |
| `Exc = 1+X` | {0,1} | **Y** | Y | Y | . | . | **.** | Y |
| `Writer(ℤ₂)` | {1} | Y | Y | Y | . | . | **Y** | Y |
| `Writer(T₂,nc)` | {1} | Y | Y | Y | . | . | **Y** | Y |
| `List (len≤2)` | {0,1,2} | **.** | **Y** | **Y** | . | . | . | **.** |
| `Pf` (powerset) | {0,1,2} | . | **.** | **.** | . | . | . | . |
| `Reader(A²)` | {2} | . | Y | **.** | Y | Y | Y | . |
| `State(S=2)` | {2} | . | Y | . | . | . | . | . |

(`Reader`, `State` are **outside** ∏-Mendler — no `T_M` — but included to expose that (1)≠(2)
in general and that (3) is orthogonal to (5).)

### The splitters (this is the whole point)

* **`List` splits (2) from (5).** `List` is a **cartesian monad** — `cartFun`✓ (concatenation of
  `fmap`'d lists keeps duplicates, never merges leaves) and `cartMu`✓ (concat preserves total
  length) — yet it is **branching** (arity {0,1,2,…}=ℕ). So **cartesian ⇏ non-branching.**
  (Standard: the free-monoid monad is the flagship cartesian/polynomial monad, arity ℕ — Leinster.)
* **`Maybe`/`Exc` split (5) from (3).** Both are non-branching but **`λ` is NOT invertible**: at
  their **nullary** shape `str = (M(1)→1)` is `(E+1→1)`, not injective. So **non-branching ⇏ `λ`
  invertible.** Exceptions `E` break strict BC at their empty-product shapes; the reverse `κ` does
  *not* care (it uses the unit `η^M:1→M(1)` there — which is why (4) still holds for `Maybe`).
* **`Pf` splits ∏-Mendler from (2).** `Pf` is ∏-Mendler (A–B flagship) but non-cartesian:
  `fmap(u)` merges leaves under non-injective `u`, and `μ=∪` merges — so `T_{Pf}` fails to
  preserve cartesian morphisms. **∏-Mendler ⇏ cartesian.**
* **`Reader`/`State` split (1) from (2)** *outside* ∏-Mendler: `Reader` is representable so its
  **functor** preserves cartesian morphisms (`Tcart`✓, (1)) but its **`μ`** (diagonal) merges
  `K²→K` leaves (`cartMu`✗, (2)). So (1) is a *functor* condition, (2) a *monad* condition; they
  coincide **only within ∏-Mendler**.

### λ-invertible is "arity exactly 1" = writer monads

Reading the table: (3) holds precisely for `{Id, Writer}` = **arity ≡ 1** = the writer monads
`A×(−)` (`E=∅`). This is *strictly inside* non-branching `E+A×(−)`; the exception summand `E`
(nullary shapes) is exactly what (3) forbids and (5) allows.

---

## 3. The corrected chain — implications and proofs

Throughout, `M` ranges over the ∏-Mendler class (so `T_M` is defined).

### (4)⟺(5) — the ONLY biconditional. **PROVED** (cited).
`effect-coeffect-arrows` (Thm A, proved) + affine-classification (Thm T2, proved): reverse `κ`
satisfies E1′–E4′ **iff** `M` is non-branching. Re-anchored computationally here: reverse `κ`
E2′ **FAILS** for `Pf` on branching-capable containers `A1,A3` and **PASSES** for `Maybe`
(`entwine.py`). ∎ (cite, do not redo)

### (5)⟹(2). **PROVED** (leafwise).
Non-branching + ∏-Mendler = **non-aborting** `M X=E+A×X`, `A` a submonoid, `E` a left `A`-set
(`affine-classification` §2.3). `fmap` acts on the single leaf of a unary shape (no merge) and
trivially on nullary shapes; `η` is the writer unit (creates the one leaf), `μ` is writer
multiplication on the single leaf (preserves it) or an abort into a *nullary* shape (destroys no
existing leaf, since `μ` only ever meets ≤1 inner leaf). Hence `fmap`, `η`, `μ` all cartesian ⟹
`M` cartesian. ∎

### (2)⇏(5). **PROVED by witness.**
`List`: cartesian (§2, standard) but arity ℕ. ∎

### (2)⟺(1) **within ∏-Mendler**. **PROVED** (computed for the whole class; conceptual proof below).
`T_M(u,f)` at `m∈MS` has backward `Q^⋆(M(u)m)→P^⋆(m)`, i.e. `∏_{c∈lv(M(u)m)}Q(y_c)→
∏_{b∈lv(m)}P(x_b)` built from the bijections `f`. This is a bijection **iff** `M(u)` induces a
bijection `lv(m)≅lv(M(u)m)` for every `m,u` — i.e. iff `fmap` never merges leaves — i.e. iff
`M` is a **polynomial functor** (`cartFun`). For a ∏-Mendler `M`, `cartFun ⟺ cartMu ⟺` cartesian
(table: coincide on `{Id,Maybe,Exc,Writer,List}` vs `Pf`). So `(1)⟺(2)` here. **Scope caveat:**
in general (1)=`cartFun` (functor) and (2)=`cartFun∧cartMu` (monad) **differ** — `Reader`/`State`
have (1) not (2). The audit's flat "(1)⟺(2)" is therefore *scope-restricted to ∏-Mendler*. ∎

### (1)/(2)⇏ (nothing weaker inside ∏-Mendler); ∏-Mendler ⇏ (2). **PROVED by witness.**
`Pf` ∈ ∏-Mendler, not cartesian (`fmap`/`μ` merge). So the ambient ∏-Mendler hypothesis does not
give (2). ∎

### (3)⟹(5). **PROVED.**
`λ` invertible ⟹ `str` iso at every occurring arity. If a shape had `≥2` leaves, `str` at it is
`M(Z1×Z2×…)→∏MZ_i`; for a ∏-Mendler `M` (which always has the arity-1 unit shape, giving cross
terms `s≠s'` in `MZ1×MZ2`) this is not iso for all `Z` — computed for `List` (`strBinary` ✗). So
no `≥2` arity ⟹ arity `≤1` = (5). ∎ (mild dependence on "the only product-preserving ∏-Mendler
functors are representables `Id`" — see Gap 1.)

### (3)⟺ "arity ≡ 1" (writer monads `A×(−)`). **PROVED on the boundary; §3-argument.**
Arity `≡1` ⟹ every `str=id` ⟹ `λ` invertible. Conversely `λ` invertible forbids nullary shapes
(there `str=(M1→1)` is iso only if `M1≅1`, forcing `M=Id`) and, by the previous item, forbids
`≥2`; so arity `≡1`. Hence **(3) = writer `A×(−)` ⊊ (5) = writer+exception `E+A×(−)`.** ∎

### (5)⇏(3). **PROVED by witness.**
`Maybe`/`Exc`: non-branching, `λ` not invertible (§2). ∎

**Assembled chain (strict, within ∏-Mendler):**
```
   (3) writer A×(−)   ⊊   (5)=(4) writer+exc E+A×(−)   ⊊   (1)=(2) cartesian (+List,…)   ⊊   ∏-Mendler (+Pf)
        Id,Writer            +Maybe,Exc                        +List                          +Pf
```

---

## 4. Why the collapse was tempting — and the precise correction to the framing

The audit's slogan bundled three genuinely different phenomena:

1. **Preservation of cartesian morphisms (1)** is a **functor/connected-limit** property (fails
   only for non-polynomial `M` like `Pf`). It is *blind to arity* — `List` and `Reader` pass it.
   It does **not** detect branching.
2. **`M` cartesian (2)** adds `μ` cartesian; still arity-blind (`List` cartesian, arity ℕ).
3. **Non-branching (5)/(4)** is an **arity** condition; strictly stronger than cartesian.
4. **`λ` invertible / strict BC (3)** is stronger still: it is arity `≡1` (products, *including
   the empty one*, all preserved), which the exceptions in (5) violate at their nullary shapes.

So "strict BC" is **not** non-branching: strict BC = *writer*, non-branching = *writer+exception*.
And "containers preserve cartesian morphisms" is **weaker** than non-branching, not equal to it
— it is just "`M` polynomial", which `List` also satisfies. The one equality that survives is the
proved arrow biconditional **(4)⟺(5)**. The **interesting content is precisely the failure of the
other collapses**, witnessed by `List` (arity vs cartesian) and `Maybe` (exception vs strict BC).

**Book/grant fix:** replace "cartesian-preservation = non-branching = strict BC" with the
*stratification*: `strict-BC (writer) ⟹ non-branching (writer+exception) ⟹ cartesian (+List) ⟹
polynomial (+Pf non-cartesian is the boundary)`, only the middle `⟺` reverse-`κ` being an iff.

---

## 5. What is CITED vs NEW

**Cited (claim none):** the fibration `p:Cont→Set` and cartesian-morphism calculus (von Glehn TAC
33 2018; Streicher; Spivak 1908.02202); fibred (co)monads & BC-mates (Jacobs 1999); monad
lifting / monad opfunctor (Street 1972; Hermida 1993; Katsumata); cartesian/polynomial monads and
that **`List` (free monoid) is the flagship cartesian monad** (Weber; Gambino–Kock; Kock; Leinster);
`T_M` (Ahman–Bauer 2409.17664 Thm 6.3); `G_M`, `λ`, `str` (my `monad-comonad-transfer`,
`-entwining`, proved+Lean); **(4)⟺(5)** (my `effect-coeffect-arrows`, `affine-classification`,
proved).

**New (this session):**
1. The **refutation** of the conjectured TFAE, with the explicit computed **boundary table** and
   named splitters (`List`, `Maybe/Exc`, `Pf`, `Reader/State`).
2. The **corrected 4-level strict chain** and the identification of each level with a monad class:
   **strict-BC = writer `A×(−)` ⊊ non-branching = writer+exception `E+A×(−)` ⊊ cartesian ⊊ polynomial**.
3. The pinning of **(3)** as "arity ≡ 1" (the *nullary/empty-product* obstruction that separates
   strict BC from non-branching — exceptions break `λ`-invertibility but not the reverse `κ`).
4. The observation that **(1) is a functor condition, (2) a monad condition**, coinciding only
   within ∏-Mendler (`Reader`/`State` separate them).

---

## 6. Gaps (precisely stated)

1. **(3)⟹(5) at arity ≥2, fully general.** The `≥2`-leaf step uses "no ∏-Mendler functor with a
   `≥2` arity shape preserves all binary products (except representables, which are excluded)".
   Verified computationally for `List`/`Pf`; the general symbolic argument (cross-terms `s≠s'` in
   `MZ1×MZ2` obstruct the bijection whenever `|M1|≥2`, which every non-`Id` ∏-Mendler `M` has) is
   sketched, not written line-by-line. Conceptually solid; mechanical.
2. **`List` cartesianness** is asserted (standard) and checked on **bounded** (`len≤2`) data;
   `μ`=concat can exceed the bound, so the harness tests the *no-merge* property on small inputs
   rather than the full monad. The unboundedness does not affect the *branching* witness.
3. **Reverse-`κ` on `List`** (branching, infinite) is inferred from (4)⟺(5), not directly computed
   (only `Pf` is the finite branching witness). Consistent with `entwine.py` gap note.
4. **E2 remains the live axiom** (audit §5.4): the fibration organizes E1/E3/E4 but E2 lives in the
   `⋆`-algebra; nothing here closes it beyond the proved non-branching case.

---

## 7. One-line status

The crown "TFAE" **breaks**; what is true and useful is the **strict stratification**
`writer ⊊ writer+exception ⊊ cartesian ⊊ polynomial`, with the single biconditional `(4)⟺(5)`
in the middle. This is a *sharper* theorem than the conjecture and directly corrects the
book/grant slogan.
