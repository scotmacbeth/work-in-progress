/-!
# Reader and State fall *outside* ∏-Mendler: their `μ` **drops leaves** (`κ_μ` non-total)

This file machine-checks the corrected boundary fact of MacBeth's PROVE session
`proofs/2026-08-06-state-reader-ladder-census.md` (registry node
`state-reader-outside-pi-mendler`). It supersedes the *refuted* earlier claim that Reader/State
are ∏-Mendler monads witnessing `cartesian ⊊ ∏-Mendler`.

## The mathematics being certified

For the ∏-cointerpretation lift `T_M (S,P) = (M S, P⋆)` of a `Set`-monad `M`
(Ahman–Bauer, arXiv:2409.17664, Thm 6.3), the multiplication laxator
`j_{mm} : P⋆(μ mm) → (P⋆)⋆(mm)` — which a monad structure on `Cont` **forces** to run
target→source, i.e. `∏_{lv(μ mm)} → ∏_{I(mm)}` — is, by naturality in `P` (a Yoneda argument,
`census` Lemma 1), **exactly reindexing along a total, label-preserving function**

  `κ_μ : I(mm) → lv(μ mm)`,   `label_{μ mm}(κ_μ i) = label(i)`  for every inner-leaf token `i`,

where `I(mm) = ⊔_{b ∈ lv mm} lv(inner_b)` is the set of inner-leaf tokens. Consequently:

> **`T_M` carries a multiplication `μ^T` (i.e. `M` is ∏-Mendler) iff for every `mm` such a
> total label-preserving `κ_μ` exists.**   (`census` §1 Criterion.)
> `κ_μ` injective ⟺ `μ^T` cartesian (no merge); `κ_μ` **non-total** ⟺ `μ` **drops** an inner
> leaf whose label is absent from `μ mm` ⟹ **no `j` at all** ⟹ `M ∉ ∏-Mendler`.

The trichotomy of non-cartesian `μ` by *how* `κ_μ` fails (`census` §3):

```
  κ_μ:              total   injective   ∏-Mendler?   monads
  ──────────────────────────────────────────────────────────────
  cartesian         yes     yes         YES          Id, Maybe, Writer, List
  MERGE (share)     yes     NO          YES          Pf   ← witnesses cartesian ⊊ ∏-Mendler
  DROP  (diagonal)  NO      —           NO           Reader, State   ← THIS FILE
  SYMMETRY          NO      —           NO           Bag (multisets)
```

The cartesian rung is certified in `Containers.TMCartesianBoundary` (`Maybe`), the MERGE rung by
the `Pf` witness there (`κ_μ` total, non-injective ⟹ the product-reindex fails *surjectivity*).
This file certifies the **DROP** rung: for `Reader` and `State` there is a finite `mm` at which
`κ_μ` is **not even total**, so no natural `j` exists and the ∏-cointerpretation has no
multiplication.

## What is certified here (finite, decidable, Lean 4 core, no Mathlib)

`κ_μ` totality is the pointwise condition "every inner-leaf token has *some* `μ`-leaf of matching
label"; a total label-preserving `κ_μ` exists **iff** this holds (`census` Lemma 1). We formalise
that pointwise predicate and exhibit finite witnesses (`Reader` over `E = Bool`, `State` over
`S = Bool`, labels in `Fin 3`) at which it fails, together with the explicit dropped token. We do
**not** re-formalise the Yoneda reduction — that is `census` Lemma 1; here the machine-checked
content is the combinatorial core the reduction lands on.

Everything is `Type`-level Lean 4 core; no `sorry`, no classical axioms (`decide` and explicit
case analysis only).

**Both sides of the proof-relevance boundary are now certified here.** §§1–3 certify the *failing*
(proof-relevant) side — the Ahman–Bauer `∏` `T_M`-monad has no multiplication (`κ_μ` not
forward-total). §§4–6 certify the *surviving* (proof-irrelevant) side — the `□` necessity predicate
lifting `□P(m) = ∀ leaf. P` **is** a genuine monad lifting of both Reader and State, because the
*reverse* covering is total (each dropped-to leaf keeps its distinguished token). This answers
Neil's UID-91 question ("is there really *no* predicate lifting for Reader/State?"): there is one —
just not the proof-relevant `∏` one. The `□` laws are pure terms, depending on **no axioms at all**
(checked via `#print axioms`). Reference: MacBeth PROVE `proofs/2026-08-07-proof-relevance-boundary.md`.
-/

namespace Containers

namespace ReaderStateOutsidePiMendler

/-- A three-element **label** type (the value set `X`, `≅ Fin 3`). We use a bespoke enumeration
rather than `Fin 3` so that `decide` stays **axiom-free**: `Fin`'s `DecidableEq` routes through
`propext`, whereas a `deriving DecidableEq` enumeration does not. `l0, l1, l2` stand for
`0, 1, 2`; the Reader witness `Gw` below is `![![l0,l0],![l1,l0]]`, i.e. `![![0,0],![1,0]]`. -/
inductive Lbl : Type
  | l0 | l1 | l2
  deriving DecidableEq

open Lbl

/-! ## 1. Reader `(−)^E`, `E = Bool` — the DROP certificate

`M X = X^E` is a monomial container: **one** shape, `E` leaves, and `M(u)` fixes the leaf set
(`u_* = id_E` bijective — Reader is a genuine polynomial functor). Its *multiplication* is the
**diagonal**: for `mm = G ∈ (X^E)^E`, `μ G : E → X`, `(μ G) e = G e e`. Inner-leaf tokens are
`I = E × E` with `label (e, e') = G e e'`; the leaves of `μ G` are `E` with `label e'' = G e'' e''`
(a diagonal value). A total label-preserving `κ_μ : E × E → E` would have to send every
off-diagonal token `(e, e')` to some leaf `e''` with `G e'' e'' = G e e'` — impossible once
`G e e'` is a value never appearing on the diagonal. -/

/-- **`κ_μ` totality for Reader over `E = Bool`** (the pointwise Lemma-1 criterion): every
inner-leaf token `(i.1, i.2)`, labelled `G i.1 i.2`, has *some* leaf `e` of the diagonal `μ G`
whose label `G e e` matches. A total label-preserving `κ_μ` exists iff this holds. -/
def ReaderKappaTotal (G : Bool → Bool → Lbl) : Prop :=
  ∀ i : Bool × Bool, ∃ e : Bool, G e e = G i.1 i.2

/-- The witness `G = ![![0,0],![1,0]]` (rows indexed by the outer leaf, columns by the inner):
`G false _ = l0`, `G true false = l1`, `G true true = l0`. Its diagonal is `μ G = (l0, l0)` —
every leaf of `μ G` is labelled `l0` — while the off-diagonal inner token `(true, false)` is
labelled `l1`, a value the diagonal never realises. -/
def Gw : Bool → Bool → Lbl
  | false, false => l0
  | false, true  => l0
  | true,  false => l1
  | true,  true  => l0

/-- **The dropped token, explicitly.** No leaf of the diagonal `μ Gw` carries the label `1` of the
off-diagonal inner token `(true, false)`: both diagonal values `Gw false false` and
`Gw true true` are `0 ≠ 1`. -/
theorem reader_diagonal_drops : ∀ e : Bool, Gw e e ≠ Gw true false := by
  intro e; cases e <;> decide

/-- **Reader is not ∏-Mendler: `κ_μ` is not total.** The inner-leaf token `(true, false)` (label
`Gw true false = 1`) is matched by no leaf of the diagonal `μ Gw` (all labelled `0`). Hence no
total label-preserving `κ_μ` exists, so (by `census` Lemma 1) the multiplication laxator `j` does
not exist and `T_Reader` has no multiplication — `Reader ∉ ∏-Mendler`. -/
theorem reader_kappa_not_total : ¬ ReaderKappaTotal Gw := by
  intro h
  obtain ⟨e, he⟩ := h (true, false)
  cases e <;> exact absurd he (by decide)

/-- **The drop is label-specific, not structural** (honest non-vacuity check). For a *constant*
`G` — every label equal — `κ_μ` **is** total: each inner token is matched by any diagonal leaf.
So the failure above is genuinely the fresh off-diagonal label of `Gw`, exactly the choice
`census` §2 makes ("pick `G e e'` absent from the diagonal"), not an artefact of the diagonal
`μ` per se. -/
theorem reader_kappa_total_of_const (x : Lbl) : ReaderKappaTotal (fun _ _ => x) :=
  fun _ => ⟨true, rfl⟩

/-! ## 2. State `S ⇒ (S × −)`, `S = Bool` — the same DROP mechanism

`M X = (S × X)^S`. An `mm ∈ M (M X)` is `F : S → S × M X`; its multiplication **threads the
state**: `(μ F) s₀ = (F s₀).2 ((F s₀).1)` — it reads the inner element `(F s₀).2` only at the
threaded state `(F s₀).1`, **dropping** the inner leaves at other states, whose labels can be
fresh. Inner-leaf tokens are `(s₀, s') ∈ S × S` with label `((F s₀).2 s').2`; the leaves of `μ F`
are `S` with label `((μ F) ll).2`. -/

/-- **`κ_μ` totality for State over `S = Bool`**: every inner-leaf token `(s₀, s')`, labelled
`((F s₀).2 s').2`, is matched by some leaf `ll` of the threaded `μ F`, labelled `((μ F) ll).2`. -/
def StateKappaTotal (F : Bool → Bool × (Bool → Bool × Lbl)) : Prop :=
  ∀ s₀ s' : Bool, ∃ ll : Bool,
    ((F ll).2 ((F ll).1)).2 = ((F s₀).2 s').2

/-- The State witness. `F false` threads to state `false` reading the inner element
`fun b => if b then (·, l2) else (·, l0)`; `F true` threads to `true` reading a constant-`l0`
inner element. So `μ F = (label l0 at false, label l0 at true)`, while the inner token
`(false, true)` carries the fresh label `l2`, dropped by the threading. -/
def Fw : Bool → Bool × (Bool → Bool × Lbl)
  | false => (false, fun b => match b with
                              | false => (false, l0)
                              | true  => (false, l2))
  | true  => (true,  fun _ => (false, l0))

/-- **The dropped token, explicitly.** No leaf of the threaded `μ Fw` carries the label `2` of the
inner token `(false, true)`: both `μ Fw` leaves have label `0 ≠ 2`. -/
theorem state_threading_drops :
    ∀ ll : Bool, ((Fw ll).2 ((Fw ll).1)).2 ≠ ((Fw false).2 true).2 := by
  intro ll; cases ll <;> decide

/-- **State is not ∏-Mendler: `κ_μ` is not total.** The inner-leaf token `(false, true)` (label
`2`) is matched by no leaf of `μ Fw` (all labelled `0`). Hence no total label-preserving `κ_μ`
exists ⟹ no `j` ⟹ `T_State` has no multiplication — `State ∉ ∏-Mendler`. -/
theorem state_kappa_not_total : ¬ StateKappaTotal Fw := by
  intro h
  obtain ⟨ll, hll⟩ := h false true
  cases ll <;> exact absurd hll (by decide)

/-! ## 3. Summary

`Reader` and `State` are polynomial (container) monads whose multiplication `μ` **drops leaves**:
at the finite witnesses `Gw` / `Fw` the `κ_μ`-totality predicate fails, so the ∏-cointerpretation
multiplication laxator `j` does not exist and neither monad lies in the ∏-Mendler class. This is a
*strictly worse* failure than the MERGE of `Pf` (whose `κ_μ` is total but non-injective —
∏-Mendler, non-cartesian; `Containers.TMCartesianBoundary`): dropping is not tolerated, merging
is. Thus `cartesian ⊊ ∏-Mendler` keeps its classical witness `Pf`, and `Reader`/`State` sit
outside ∏-Mendler on the DROP rung of the trichotomy, opposite `Bag` (SYMMETRY). -/

/-- **The DROP certificate, packaged.** Both `Reader` (`Gw`) and `State` (`Fw`) fail `κ_μ`
totality, each with an explicit dropped inner-leaf token whose label no `μ`-leaf realises. -/
theorem reader_state_outside_pi_mendler :
    (¬ ReaderKappaTotal Gw ∧ ∀ e : Bool, Gw e e ≠ Gw true false) ∧
      (¬ StateKappaTotal Fw ∧
        ∀ ll : Bool, ((Fw ll).2 ((Fw ll).1)).2 ≠ ((Fw false).2 true).2) :=
  ⟨⟨reader_kappa_not_total, reader_diagonal_drops⟩,
   ⟨state_kappa_not_total, state_threading_drops⟩⟩

/-! ## 4. The *surviving* side: Reader carries the `□` propositional monad lifting

The sections above certify the **failing** (proof-relevant) direction: the Ahman–Bauer `∏`
`T_M`-monad has no multiplication because `κ_μ` is not **forward**-total (`reader_kappa_not_total`).
This section certifies the **surviving** (proof-irrelevant) direction, answering Neil's UID-91
question ("are we saying there is *no* predicate lifting for Reader/State?"). There **is** one: the
`□` necessity predicate lifting `□P(m) = ∀ leaf. P` is a genuine monad lifting of Reader on the
subobject fibration, because the *reverse* covering is total.

Mathematics certified (MacBeth PROVE `proofs/2026-08-07-proof-relevance-boundary.md`, §3–4;
node `proof-relevance-boundary`): with `□P(m) := ∀ e. P (m e)` on Reader elements `m : E → X`,

* the **unit** law `P x → □P (η x)` holds (`η x` is the constant Reader, all leaves `= x`);
* the **multiplication** law `□□P mm → □P (μ mm)` holds for **every** `mm` and **every** `P`, by
  instantiating the diagonal token — `μ` (the diagonal) keeps exactly the token it needs;
* fixing `mm`, the multiplication law (∀ `P`) is **equivalent** to *reverse*-totality of `mm`
  (§3.4, single test predicate `P₀ = Lab(I(mm))`); and reverse-totality holds for **every** `mm`
  (each surviving diagonal leaf `e` *is* the inner token `(e,e)`).

So Reader lands on the surviving side of the proof-relevance boundary: `κ_μ` **not** forward-total
(no `∏`-monad) yet reverse-total **always** (the `□`-monad lifts). Everything here is a pure term
or `rw`/`obtain` — **axiom-free**, no `decide`/`propext`, `P : Lbl → Prop` a genuine proposition. -/

/-- Reader `□` (necessity) predicate lifting: `□P(m) := ∀ e, P (m e)` on a Reader element
`m : E → X` (all `E`-leaves lie in `P`). -/
def ReaderBox (P : Lbl → Prop) (m : Bool → Lbl) : Prop := ∀ e : Bool, P (m e)

/-- Double box: `□□P(mm) := ∀ e e', P (mm e e')`, the predicate `□(□P)` on `mm : M (M X)`
(all inner-leaf tokens `(e, e')` lie in `P`). -/
def ReaderBoxBox (P : Lbl → Prop) (mm : Bool → Bool → Lbl) : Prop :=
  ∀ e e' : Bool, P (mm e e')

/-- Reader multiplication (the **diagonal**): `μ mm = fun e => mm e e`. -/
def readerMu (mm : Bool → Bool → Lbl) : Bool → Lbl := fun e => mm e e

/-- **Unit lifting law.** `P x → □P (η x)` where `η x = fun _ => x` is the constant Reader.
Since every leaf of `η x` is labelled `x`, `□P (η x) = ∀ e, P x`. Holds for all `P`, all `x`. -/
theorem reader_box_unit (x : Lbl) (P : Lbl → Prop) (hx : P x) :
    ReaderBox P (fun _ => x) := fun _ => hx

/-- **Multiplication lifting law — the DROP-surviving direction.** `□□P mm → □P (μ mm)`, by
instantiating the diagonal token `e' := e`: the surviving leaf `e` of the diagonal `μ mm` is the
inner token `(e, e)`, which `□□P` already covers. Holds for **all** `P`, **all** `mm` —
unconditionally, in exact contrast to `reader_kappa_not_total`. -/
theorem reader_box_mult (mm : Bool → Bool → Lbl) (P : Lbl → Prop)
    (h : ReaderBoxBox P mm) : ReaderBox P (readerMu mm) := fun e => h e e

/-- **Reverse-totality for Reader** — the posetal shadow of `κ_μ`, opposite direction to
`ReaderKappaTotal`: every surviving diagonal leaf `e` has *some* inner token `i` of matching label
(`Lab(lv(μ mm)) ⊆ Lab(I(mm))`). This — not forward-totality — is what the `□` multiplication needs. -/
def ReaderReverseTotal (mm : Bool → Bool → Lbl) : Prop :=
  ∀ e : Bool, ∃ i : Bool × Bool, mm i.1 i.2 = mm e e

/-- **Reverse-total holds for every `mm`.** Each diagonal leaf `e` is its own inner token `(e, e)`
(`rfl`). The universal survival of the reverse covering is exactly why the `□` lifting succeeds
where the `∏` `T_M`-monad (`reader_kappa_not_total`) fails. -/
theorem reader_reverse_total_always (mm : Bool → Bool → Lbl) :
    ReaderReverseTotal mm := fun e => ⟨(e, e), rfl⟩

/-- **The theorem (PROVE §3.4), Reader instance.** For a fixed `mm`, the `□`-multiplication law
quantified over *all* predicates `P` is **equivalent** to reverse-totality of `mm`. The forward
implication instantiates the single test predicate `P₀ y := ∃ token i, lab i = y`
(`= Lab(I(mm))`); the backward implication rewrites each surviving leaf along its witnessing token.
Combined with `reader_reverse_total_always`, this re-derives `reader_box_mult` and shows the `□`
lifting is exactly as strong as reverse-totality. -/
theorem reader_box_mult_iff_reverse_total (mm : Bool → Bool → Lbl) :
    (∀ P : Lbl → Prop, ReaderBoxBox P mm → ReaderBox P (readerMu mm))
      ↔ ReaderReverseTotal mm := by
  constructor
  · intro hbox e
    exact hbox (fun y => ∃ i : Bool × Bool, mm i.1 i.2 = y)
      (fun a b => ⟨(a, b), rfl⟩) e
  · intro hrev P h e
    obtain ⟨i, hi⟩ := hrev e
    show P (mm e e)
    rw [← hi]
    exact h i.1 i.2

/-- **The proof-relevance boundary, both directions, at the same Reader monad.** The proof-relevant
`∏` `T_M`-multiplication FAILS (`κ_μ` not forward-total, `reader_kappa_not_total`) while the
proof-irrelevant `□` predicate-multiplication HOLDS for every `mm` and every `P`
(`reader_box_mult`), because the reverse covering is universal (`reader_reverse_total_always`).
This is the Lean witness to Neil's UID-91 point: the predicate lifting exists even though the
container monad does not. -/
theorem reader_proof_relevance_boundary :
    (¬ ReaderKappaTotal Gw)
      ∧ (∀ (mm : Bool → Bool → Lbl) (P : Lbl → Prop),
            ReaderBoxBox P mm → ReaderBox P (readerMu mm))
      ∧ (∀ mm : Bool → Bool → Lbl, ReaderReverseTotal mm) :=
  ⟨reader_kappa_not_total, reader_box_mult, reader_reverse_total_always⟩

/-! ## 5. State: the same surviving side (threading keeps the threaded token)

The identical story for State `M X = (S × X)^S`. The multiplication threads the state, keeping —
per surviving leaf `s₀` — exactly the threaded inner token `(s₀, (F s₀).1)`. So the reverse
covering is again universal and the `□` lifting `□P m := ∀ s, P (m s).2` goes through, while the
`∏` `T_M`-monad fails (`state_kappa_not_total`). -/

/-- State `□` predicate lifting: `□P m := ∀ s, P (m s).2` on a State element `m : S → S × X`
(every leaf's *value* label lies in `P`). -/
def StateBox (P : Lbl → Prop) (m : Bool → Bool × Lbl) : Prop := ∀ s : Bool, P (m s).2

/-- Double box for State: `□□P F := ∀ s₀ s', P ((F s₀).2 s').2`, all inner-leaf tokens in `P`. -/
def StateBoxBox (P : Lbl → Prop) (F : Bool → Bool × (Bool → Bool × Lbl)) : Prop :=
  ∀ s₀ s' : Bool, P ((F s₀).2 s').2

/-- State multiplication (the **threading**): `μ F s₀ = (F s₀).2 ((F s₀).1)` — read the inner
element at the threaded state. -/
def stateMu (F : Bool → Bool × (Bool → Bool × Lbl)) : Bool → Bool × Lbl :=
  fun s₀ => (F s₀).2 ((F s₀).1)

/-- **Unit lifting law (State).** `P x → □P (η x)` where `η x = fun s => (s, x)`; every leaf's
value label is `x`, so `□P (η x) = ∀ s, P x`. -/
theorem state_box_unit (x : Lbl) (P : Lbl → Prop) (hx : P x) :
    StateBox P (fun s => (s, x)) := fun _ => hx

/-- **Multiplication lifting law (State) — the surviving direction.** `□□P F → □P (μ F)`, by
instantiating the inner state `s' := (F s₀).1` (the threaded token). Holds for all `P`, all `F`. -/
theorem state_box_mult (F : Bool → Bool × (Bool → Bool × Lbl)) (P : Lbl → Prop)
    (h : StateBoxBox P F) : StateBox P (stateMu F) := fun s₀ => h s₀ ((F s₀).1)

/-- **Reverse-totality for State**: every surviving threaded leaf `s₀` has *some* inner token
`p` of matching value label. -/
def StateReverseTotal (F : Bool → Bool × (Bool → Bool × Lbl)) : Prop :=
  ∀ s₀ : Bool, ∃ p : Bool × Bool, ((F p.1).2 p.2).2 = (stateMu F s₀).2

/-- **Reverse-total holds for every `F`.** The threaded leaf `s₀` is the inner token
`(s₀, (F s₀).1)` (`rfl`). -/
theorem state_reverse_total_always (F : Bool → Bool × (Bool → Bool × Lbl)) :
    StateReverseTotal F := fun s₀ => ⟨(s₀, (F s₀).1), rfl⟩

/-- **The theorem (PROVE §3.4), State instance.** The `□`-multiplication law (∀ `P`) at a fixed
`F` is equivalent to reverse-totality of `F`. -/
theorem state_box_mult_iff_reverse_total (F : Bool → Bool × (Bool → Bool × Lbl)) :
    (∀ P : Lbl → Prop, StateBoxBox P F → StateBox P (stateMu F))
      ↔ StateReverseTotal F := by
  constructor
  · intro hbox s₀
    exact hbox (fun y => ∃ p : Bool × Bool, ((F p.1).2 p.2).2 = y)
      (fun a b => ⟨(a, b), rfl⟩) s₀
  · intro hrev P h s₀
    obtain ⟨p, hp⟩ := hrev s₀
    show P (stateMu F s₀).2
    rw [← hp]
    exact h p.1 p.2

/-- **The proof-relevance boundary for State**, both directions at the same monad: `∏` `T_M`-monad
FAILS (`state_kappa_not_total`), `□` predicate lifting HOLDS for every `F`, `P` (`state_box_mult`),
reverse covering universal (`state_reverse_total_always`). -/
theorem state_proof_relevance_boundary :
    (¬ StateKappaTotal Fw)
      ∧ (∀ (F : Bool → Bool × (Bool → Bool × Lbl)) (P : Lbl → Prop),
            StateBoxBox P F → StateBox P (stateMu F))
      ∧ (∀ F : Bool → Bool × (Bool → Bool × Lbl), StateReverseTotal F) :=
  ⟨state_kappa_not_total, state_box_mult, state_reverse_total_always⟩

/-! ## 6. The boundary, both rungs, packaged

The DROP failure (`reader_state_outside_pi_mendler`, §3) and the `□` survival (§4–5) together are
the Lean-certified proof-relevance boundary: at Reader **and** State, the proof-relevant `∏`
container monad has no multiplication while the proof-irrelevant `□` predicate monad lifting does. -/

/-- **The proof-relevance boundary, fully packaged** for both Reader and State: each fails the
`∏` `T_M`-monad (`κ_μ` not forward-total) yet carries the `□` predicate monad lifting
(unit + multiplication, unconditional). -/
theorem proof_relevance_boundary_reader_state :
    (¬ ReaderKappaTotal Gw ∧
        (∀ (mm : Bool → Bool → Lbl) (P : Lbl → Prop),
            ReaderBoxBox P mm → ReaderBox P (readerMu mm))) ∧
      (¬ StateKappaTotal Fw ∧
        (∀ (F : Bool → Bool × (Bool → Bool × Lbl)) (P : Lbl → Prop),
            StateBoxBox P F → StateBox P (stateMu F))) :=
  ⟨⟨reader_kappa_not_total, reader_box_mult⟩,
   ⟨state_kappa_not_total, state_box_mult⟩⟩

/-! ## 7. The proof-relevant *surviving* lifting: Reader carries a Σ-container **monad**

Sections §§4–6 answered Neil's UID-91 with the `□` predicate lifting — but `□` is
*proof-irrelevant* (`P : Lbl → Prop`). The parity grading of MacBeth's boundary result predicts
that Reader should also carry a genuinely *proof-relevant* monad lifting — just not the `∏` one
(`reader_kappa_not_total`) that Ahman–Bauer single out. It is the **Σ-container lifting**

  `T^Σ_M (S,P) = (M S, P^Σ)`,  `P^Σ(m) = ∐_{b ∈ lv m} P(x_b)`,

with unit the **codiagonal fold** and multiplication **reindexing along the diagonal section**
`σ(mm, L) = (L, L)`. This section machine-checks that `(T^Σ_Reader, η^Σ, μ^Σ)` satisfies the three
monad laws, for Reader over `E = Bool` and an **arbitrary** base container `(S, P)` — i.e. the
"all containers `C`" quantifier of the reduction Corollary 2.3 is realised by keeping `S`, `P`
general.

Reference: MacBeth PROVE `proofs/2026-08-07-sigma-monad-proved.md`, §§2–4 (node
`sigma-monad-coherence`, computed → proved). The engine there is the **reduction lemma**: every
backward position map is a coproduct-pushforward `Σ_α` and `Σ` is faithful (Lemma 2.2), so each
monad law collapses to a single equation between label-preserving index functions. Here we verify
those index identities *directly* by exhibiting the backward maps as concrete functions on the
Σ-position `Sigma` types and proving the law composites equal — for Reader the diagonal section is
constant, so all three are `rfl`. Everything is `Type`-level core Lean 4, **no axioms** (no
`decide`, no `propext`); the base family `P : S → Type` is a genuine proof-relevant container. -/

universe u

/-- Reader multiplication (the diagonal), polymorphic in the base type `A`:
`μ mm = fun e => mm e e`. Used at several levels (base `S`, and `M S`). -/
def rMu {A : Type u} (mm : Bool → Bool → A) : Bool → A := fun e => mm e e

/-- Reader unit (the constant Reader), polymorphic in `A`: `η s = fun _ => s`. -/
def rEta {A : Type u} (s : A) : Bool → A := fun _ => s

variable {S : Type u} (P : S → Type u)

/-- Σ-position of `T C` at a Reader element `m : Bool → S`: a surviving leaf `b` together with a
`P`-position at its label `m b`. This is `P^Σ(m) = ∐_{b ∈ lv m} P(x_b)` for `E = Bool`. -/
def RSig (m : Bool → S) : Type u := Σ b : Bool, P (m b)

/-- Σ-position of `T T C` at `mm : Bool → Bool → S`: outer leaf `b`, inner leaf `c`, and a
`P`-position at `mm b c`. Equal to `∐_{b} (P^Σ)(mm b) = (P^Σ)^Σ(mm)`. -/
def RSigSig (mm : Bool → Bool → S) : Type u := Σ b : Bool, Σ c : Bool, P (mm b c)

/-- Σ-position of `T T T C` at `mmm`: the triple-token set `I₂(mmm)`. -/
def RSig3 (mmm : Bool → Bool → Bool → S) : Type u :=
  Σ a : Bool, Σ b : Bool, Σ c : Bool, P (mmm a b c)

/-- **Unit backward map** `η^Σ.♯ : P^Σ(η s) → P s`, the **codiagonal fold** `⟨b, p⟩ ↦ p`. No leaf
is chosen — the fold is unconditional (`(η s) b = s` for every leaf `b`, so `P ((η s) b) = P s`). -/
def rEtaBwd (s : S) : RSig P (rEta s) → P s := fun x => x.2

/-- **Multiplication backward map** `μ^Σ.♯ : P^Σ(μ mm) → (P^Σ)^Σ(mm)`, reindexing along the
diagonal section `σ(mm, L) = (L, L)`: `⟨L, p⟩ ↦ ⟨L, L, p⟩`. Well-typed because
`lab(σ(mm,L)) = mm L L = (rMu mm) L = lab(L)` — the position `p` is carried unchanged. -/
def rMuBwd (mm : Bool → Bool → S) : RSig P (rMu mm) → RSigSig P mm :=
  fun x => ⟨x.1, x.1, x.2⟩

/-- `η^Σ_{TC}.♯` — the unit backward map one level up (at container `T C`): the **outer** fold that
forgets the pure outer leaf of `η_{MS} m`. Domain `(P^Σ)^Σ(η_{MS} m) = Σ b, RSig P m` (each
`(η_{MS} m) b = m`), codomain `RSig P m`; `⟨b, ⟨c, p⟩⟩ ↦ ⟨c, p⟩`. -/
def etaSigTC (m : Bool → S) : (Σ _b : Bool, RSig P m) → RSig P m := fun x => x.2

/-- `T(η^Σ_C).♯` — the unit backward map lifted **leafwise** by `T`: the *inner* fold that forgets
the pure inner leaf. Domain `(P^Σ)^Σ(M(η) m) = Σ b, Σ c, P (m b)` (each `(M(η) m) b c = m b`),
codomain `RSig P m`; `⟨b, ⟨c, p⟩⟩ ↦ ⟨b, p⟩`. -/
def TetaSig (m : Bool → S) : (Σ b : Bool, Σ _c : Bool, P (m b)) → RSig P m :=
  fun x => ⟨x.1, x.2.2⟩

/-- `μ_{MS} mmm` — collapse of the **outer** two `M`-levels: `dd b c = mmm b b c`. -/
def dd (mmm : Bool → Bool → Bool → S) : Bool → Bool → S := fun b c => mmm b b c

/-- `M(μ) mmm` — leafwise collapse of the **inner** two levels: `ee a c = mmm a c c`. -/
def ee (mmm : Bool → Bool → Bool → S) : Bool → Bool → S := fun a c => mmm a c c

/-- `μμ mmm` — the fully collapsed diagonal `ddiag e = mmm e e e` (the shared shape of both sides of
the associativity square, by Reader's monad associativity). -/
def ddiag (mmm : Bool → Bool → Bool → S) : Bool → S := fun e => mmm e e e

/-- `μ^Σ_{TC}.♯` — multiplication backward one level up (at `T C`): the diagonal section on the
**outer** leaf. Domain `(P^Σ)^Σ(dd mmm) = Σ b, Σ c, P (mmm b b c)`, codomain `RSig3 P mmm`;
`⟨b, c, p⟩ ↦ ⟨b, b, c, p⟩`. -/
def muSigTC (mmm : Bool → Bool → Bool → S) : RSigSig P (dd mmm) → RSig3 P mmm :=
  fun x => ⟨x.1, x.1, x.2.1, x.2.2⟩

/-- `T(μ^Σ_C).♯` — multiplication backward lifted **leafwise** by `T`: the diagonal section on the
**inner** two levels. Domain `(P^Σ)^Σ(ee mmm) = Σ a, Σ c, P (mmm a c c)`, codomain `RSig3 P mmm`;
`⟨a, c, p⟩ ↦ ⟨a, c, c, p⟩`. -/
def TmuSig (mmm : Bool → Bool → Bool → S) : RSigSig P (ee mmm) → RSig3 P mmm :=
  fun x => ⟨x.1, x.2.1, x.2.1, x.2.2⟩

/-- **LEFT UNIT** `μ^Σ_C ∘ η^Σ_{TC} = id_{TC}`, backward part, at every shape `m ∈ MS` and every
Σ-position `x`. The composite `etaSigTC ∘ rMuBwd (η_{MS} m)` sends `⟨L, p⟩ ↦ ⟨L, L, p⟩ ↦ ⟨L, p⟩`,
which is `x` by `Sigma`-eta. This is index-identity **(U1)** (`innerleaf(σ(η_{MS}m, L)) = L`) of the
reduction — for Reader immediate, the diagonal section's inner component is the survivor. -/
theorem reader_sigma_left_unit (m : Bool → S) (x : RSig P m) :
    etaSigTC P m (rMuBwd P (rEta m) x) = x := rfl

/-- **RIGHT UNIT** `μ^Σ_C ∘ T(η^Σ_C) = id_{TC}`, backward part. The composite
`TetaSig ∘ rMuBwd (M(η) m)` sends `⟨L, p⟩ ↦ ⟨L, L, p⟩ ↦ ⟨L, p⟩ = x`. This is index-identity
**(U2)** (`outer(σ(M(η)m, L)) = L`) — the diagonal section's outer component is the survivor. -/
theorem reader_sigma_right_unit (m : Bool → S) (x : RSig P m) :
    TetaSig P m (rMuBwd P (fun e => rEta (m e)) x) = x := rfl

/-- **ASSOCIATIVITY** `μ^Σ_C ∘ μ^Σ_{TC} = μ^Σ_C ∘ T(μ^Σ_C)`, backward part, at every triple `mmm`.
The two composites are `muSigTC ∘ rMuBwd (dd mmm)` and `TmuSig ∘ rMuBwd (ee mmm)`; both send
`⟨L, p⟩ ↦ ⟨L, L, L, p⟩`, so they are equal by `rfl`. This is the section pentagon **(A)** — the
Reader diagonal threads associatively (the constant diagonal composes to the triple diagonal),
`= (e ↦ (e,e,e))` on both sides. -/
theorem reader_sigma_assoc (mmm : Bool → Bool → Bool → S) (x : RSig P (ddiag mmm)) :
    muSigTC P mmm (rMuBwd P (dd mmm) x) = TmuSig P mmm (rMuBwd P (ee mmm) x) := rfl

/-- **The Σ-container lifting of Reader is a monad**, all three laws at once, for `E = Bool` and an
arbitrary base container `(S, P)`. Bundles `reader_sigma_left_unit`, `reader_sigma_right_unit`,
`reader_sigma_assoc`. This is the **proof-relevant** monad lifting of Reader (`P : S → Type`, no
`Prop`), the Σ-partner of the `□` lifting under the parity grading — and the concrete positive
answer to "does Reader carry *any* proof-relevant monad lifting?": yes, the Σ one. -/
theorem reader_sigma_monad_lifting :
    (∀ (m : Bool → S) (x : RSig P m), etaSigTC P m (rMuBwd P (rEta m) x) = x) ∧
      (∀ (m : Bool → S) (x : RSig P m), TetaSig P m (rMuBwd P (fun e => rEta (m e)) x) = x) ∧
        (∀ (mmm : Bool → Bool → Bool → S) (x : RSig P (ddiag mmm)),
            muSigTC P mmm (rMuBwd P (dd mmm) x) = TmuSig P mmm (rMuBwd P (ee mmm) x)) :=
  ⟨reader_sigma_left_unit P, reader_sigma_right_unit P, reader_sigma_assoc P⟩

/-! ## 8. The triptych: at the *same* base monad Reader, ∏ ✗ / □ ✓ / Σ ✓

The payoff of the whole file. At Reader, exhibited simultaneously:

* the proof-relevant **∏**-container `T_M`-monad has **no** multiplication (`κ_μ` not
  forward-total, `reader_kappa_not_total`, §1) — the direction Ahman–Bauer single out;
* the proof-irrelevant **□** predicate lifting **is** a monad (`reader_box_mult`, §4), because the
  reverse covering is universal (`reader_reverse_total_always`);
* the proof-relevant **Σ**-container lifting **is** a monad (`reader_sigma_monad_lifting`, §7).

So the parity grading is a statement about *monads*, both sides certified: dropping proof-relevance
is unnecessary for a lifting to exist — one must instead switch `∏ ⇝ Σ` (the surviving, reverse-
total half of the grading). -/

/-- **The proof-relevance triptych for Reader.** `∏` fails; `□` holds; `Σ` holds — the last as a
genuine proof-relevant monad lifting (unit + associativity displayed). Parameterised by the
arbitrary base family `P` witnessing that the Σ lifting works for *every* container `C = (S,P)`. -/
theorem reader_proof_relevance_triptych :
    (¬ ReaderKappaTotal Gw) ∧
      (∀ (mm : Bool → Bool → Lbl) (Q : Lbl → Prop),
          ReaderBoxBox Q mm → ReaderBox Q (readerMu mm)) ∧
        (∀ (m : Bool → S) (x : RSig P m), etaSigTC P m (rMuBwd P (rEta m) x) = x) ∧
          (∀ (mmm : Bool → Bool → Bool → S) (x : RSig P (ddiag mmm)),
              muSigTC P mmm (rMuBwd P (dd mmm) x) = TmuSig P mmm (rMuBwd P (ee mmm) x)) :=
  ⟨reader_kappa_not_total, reader_box_mult, reader_sigma_left_unit P, reader_sigma_assoc P⟩

/-! ## 9. The proof-relevant *surviving* lifting for **State**: the Σ-container **monad**

The State analogue of §7. Where Reader's multiplication reindexes along the *constant diagonal*
section `σ(mm, L) = (L, L)`, State's reindexes along the **threaded** section
`σ(mm, s₀) = (s₀, (mm s₀).1)` — the surviving input-state leaf `s₀` pairs with the *next state*
`(mm s₀).1` that the outer step threads into the inner one. This is a genuinely different
`(U1, U2, A)` instance from Reader: the outer component of `σ` is always the survivor (so `(U2)` is
free, as for Reader), but the inner component is now the state-dependent threading rather than a
constant, and `(A)` holds because *threading is associative* — the section-level shadow of State's
own `μ`-associativity, not a Reader accident.

For State over `St = Bool`, an element of `M A = (St × A)^{St}` is `m : Bool → Bool × A`
(input state ↦ (next state, value)); its leaves are the input states, the label of leaf `s` is the
value `(m s).2`. The Σ-lifting `T^Σ_State (S,P) = (M S, P^Σ)`, `P^Σ(m) = ∐_{s} P((m s).2)`, has
unit the codiagonal fold and multiplication `μ^Σ` reindexing along the threaded section. This
section machine-checks the three monad laws for State over `St = Bool` and an **arbitrary** base
container `(S, P)`, matching the "all containers `C`" quantifier of the reduction Corollary 2.3.

Reference: MacBeth PROVE `proofs/2026-08-07-sigma-monad-proved.md`, §5 (State: the threading
section satisfies (U1),(U2),(A) — all `St`; node `sigma-monad-coherence`, computed → proved).
The `∏` `T_M`-monad this Σ-lifting stands in contrast to is the Ahman–Bauer cointerpretation
(arXiv:2409.17664, Thm 6.3), whose multiplication laxator `κ_μ` is **not** forward-total for State
(`state_kappa_not_total`, §2). As in §7, every backward map is exhibited as a concrete function on
the `Sigma` position types; the threaded section reduces through the pair projections, so all three
laws are `rfl`. Pure `Type`-level core Lean 4, **no axioms** (no `decide`, no `propext`); the base
family `P : S → Type` is a genuine proof-relevant container. -/

/-- State unit (keep the state), polymorphic in the base type `A`: `η x = fun s => (s, x)`. Used at
several levels (base `S`, and `M S`). Its next-state map is the **identity**, which is exactly what
discharges `(U1)`. -/
def sEta {A : Type u} (x : A) : Bool → Bool × A := fun s => (s, x)

/-- State multiplication (the **threading**), polymorphic in `A`:
`μ mm s = (mm s).2 ((mm s).1)` — read the inner element only at the threaded next state. -/
def sMu {A : Type u} (mm : Bool → Bool × (Bool → Bool × A)) : Bool → Bool × A :=
  fun s => (mm s).2 ((mm s).1)

/-- Σ-position of `T C` at a State element `m : Bool → Bool × S`: a surviving input-state leaf `s`
together with a `P`-position at its value label `(m s).2`. This is `P^Σ(m) = ∐_{s} P((m s).2)` for
`St = Bool`. -/
def StateSigma (m : Bool → Bool × S) : Type u := Σ s : Bool, P (m s).2

/-- Σ-position of `T T C` at `mm`: outer input state `s₀`, inner input state `s'`, and a
`P`-position at the value `((mm s₀).2 s').2`. Equal to `(P^Σ)^Σ(mm)`. -/
def StateSigma2 (mm : Bool → Bool × (Bool → Bool × S)) : Type u :=
  Σ s₀ : Bool, Σ s' : Bool, P ((mm s₀).2 s').2

/-- Σ-position of `T T T C` at `mmm`: the triple-state token set `I₂(mmm)`, position at the fully
threaded value `(((mmm a).2 b).2 c).2`. -/
def StateSigma3 (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) : Type u :=
  Σ a : Bool, Σ b : Bool, Σ c : Bool, P (((mmm a).2 b).2 c).2

/-- **Unit backward map** `η^Σ.♯ : P^Σ(η x) → P x`, the **codiagonal fold** `⟨s, p⟩ ↦ p`. Every
leaf of `η x` has value `x` (`(η x s).2 = x`), so the fold is unconditional and no leaf is chosen. -/
def sEtaBwd (x : S) : StateSigma P (sEta x) → P x := fun z => z.2

/-- **Multiplication backward map** `μ^Σ.♯ : P^Σ(μ mm) → (P^Σ)^Σ(mm)`, reindexing along the
**threaded section** `σ(mm, s₀) = (s₀, (mm s₀).1)`: `⟨s₀, p⟩ ↦ ⟨s₀, (mm s₀).1, p⟩`. Well-typed
because `lab(σ(mm,s₀)) = ((mm s₀).2 ((mm s₀).1)).2 = (μ mm s₀).2 = lab(s₀)` — the position `p` is
carried unchanged. Contrast Reader's constant diagonal `⟨L, p⟩ ↦ ⟨L, L, p⟩` (`rMuBwd`). -/
def sMuBwd (mm : Bool → Bool × (Bool → Bool × S)) :
    StateSigma P (sMu mm) → StateSigma2 P mm :=
  fun z => ⟨z.1, (mm z.1).1, z.2⟩

/-- `η^Σ_{TC}.♯` — the unit backward map one level up (at container `T C`): the **outer** fold that
forgets the pure outer leaf of `η_{MS} m` (each `(η_{MS} m) s₀ = m`, so its value at leaf `s'` is
`(m s').2`). Domain `(P^Σ)^Σ(η_{MS} m) = Σ s₀, StateSigma P m`, codomain `StateSigma P m`;
`⟨s₀, ⟨s', p⟩⟩ ↦ ⟨s', p⟩`. -/
def etaSigTCState (m : Bool → Bool × S) :
    (Σ _s₀ : Bool, StateSigma P m) → StateSigma P m := fun z => z.2

/-- `T(η^Σ_C).♯` — the unit backward map lifted **leafwise** by `T`: the *inner* fold that forgets
the pure inner leaf of `M(η) m` (each inner element is `η ((m s₀).2)`, value at any `s'` is
`(m s₀).2`). Domain `(P^Σ)^Σ(M(η) m) = Σ s₀, Σ s', P (m s₀).2`, codomain `StateSigma P m`;
`⟨s₀, ⟨s', p⟩⟩ ↦ ⟨s₀, p⟩`. -/
def TetaSigState (m : Bool → Bool × S) :
    (Σ s₀ : Bool, Σ _s' : Bool, P (m s₀).2) → StateSigma P m := fun z => ⟨z.1, z.2.2⟩

/-- `μ_{MS} mmm` — collapse of the **outer** two `M`-levels by State threading: `sDd = sMu mmm`. -/
def sDd (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    Bool → Bool × (Bool → Bool × S) := sMu mmm

/-- `M(μ) mmm` — leafwise collapse of the **inner** two levels:
`sEe s = ((mmm s).1, sMu (mmm s).2)` (thread only inside, carry the outer next state). -/
def sEe (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    Bool → Bool × (Bool → Bool × S) := fun s => ((mmm s).1, sMu (mmm s).2)

/-- `μμ mmm` — the fully collapsed shape `sMu (sDd mmm)`, the shared codomain shape of both sides of
the associativity square. State's `μ`-associativity makes `sMu (sEe mmm)` **definitionally equal**
to this, so a single `x : StateSigma P (sDdiag mmm)` feeds both composites below. -/
def sDdiag (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    Bool → Bool × S := sMu (sDd mmm)

/-- `μ^Σ_{TC}.♯` — multiplication backward one level up (at `T C`): the threaded section on the
**outer** leaf. Domain `(P^Σ)^Σ(sDd mmm)`, codomain `StateSigma3 P mmm`;
`⟨s₀, s', p⟩ ↦ ⟨s₀, (mmm s₀).1, s', p⟩` (the outer next state `(mmm s₀).1` is inserted). -/
def muSigTCState (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    StateSigma2 P (sDd mmm) → StateSigma3 P mmm :=
  fun z => ⟨z.1, (mmm z.1).1, z.2.1, z.2.2⟩

/-- `T(μ^Σ_C).♯` — multiplication backward lifted **leafwise** by `T`: the threaded section on the
**inner** two levels. Domain `(P^Σ)^Σ(sEe mmm)`, codomain `StateSigma3 P mmm`;
`⟨a, L, p⟩ ↦ ⟨a, L, ((mmm a).2 L).1, p⟩` (the inner next state `((mmm a).2 L).1` is inserted). -/
def TmuSigState (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) :
    StateSigma2 P (sEe mmm) → StateSigma3 P mmm :=
  fun z => ⟨z.1, z.2.1, ((mmm z.1).2 z.2.1).1, z.2.2⟩

/-- **LEFT UNIT** `μ^Σ_C ∘ η^Σ_{TC} = id_{TC}`, backward part, at every shape `m` and Σ-position
`x`. The composite `etaSigTCState ∘ sMuBwd (η_{MS} m)` sends `⟨s₀, p⟩ ↦ ⟨s₀, s₀, p⟩ ↦ ⟨s₀, p⟩`,
which is `x` by `Sigma`-eta. This is index-identity **(U1)**: the threaded section's inner component
on `η_{MS} m` is the survivor, *because State's unit threads the identity next state*
(`(sEta m s₀).1 = s₀`). -/
theorem state_sigma_left_unit (m : Bool → Bool × S) (x : StateSigma P m) :
    etaSigTCState P m (sMuBwd P (sEta m) x) = x := rfl

/-- **RIGHT UNIT** `μ^Σ_C ∘ T(η^Σ_C) = id_{TC}`, backward part. The composite
`TetaSigState ∘ sMuBwd (M(η) m)` sends `⟨s₀, p⟩ ↦ ⟨s₀, (m s₀).1, p⟩ ↦ ⟨s₀, p⟩ = x`. This is
index-identity **(U2)**: the threaded section's **outer** component is always the survivor. -/
theorem state_sigma_right_unit (m : Bool → Bool × S) (x : StateSigma P m) :
    TetaSigState P m (sMuBwd P (fun s => ((m s).1, sEta (m s).2)) x) = x := rfl

/-- **ASSOCIATIVITY** `μ^Σ_C ∘ μ^Σ_{TC} = μ^Σ_C ∘ T(μ^Σ_C)`, backward part, at every triple `mmm`.
The two composites `muSigTCState ∘ sMuBwd (sDd mmm)` and `TmuSigState ∘ sMuBwd (sEe mmm)` both send
`⟨s, p⟩ ↦ ⟨s, (mmm s).1, ((mmm s).2 ((mmm s).1)).1, p⟩` — the **fully threaded** triple token
`(s, h₀ s, h₁^s(h₀ s))` — so they are equal by `rfl`. This is the section pentagon **(A)**: the two
ways of threading three `M`-levels coincide, the section-level shadow of State's own
`μ`-associativity. -/
theorem state_sigma_assoc
    (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S))) (x : StateSigma P (sDdiag mmm)) :
    muSigTCState P mmm (sMuBwd P (sDd mmm) x) = TmuSigState P mmm (sMuBwd P (sEe mmm) x) := rfl

/-- **The Σ-container lifting of State is a monad**, all three laws at once, for `St = Bool` and an
arbitrary base container `(S, P)`. Bundles `state_sigma_left_unit`, `state_sigma_right_unit`,
`state_sigma_assoc`. This is the **proof-relevant** monad lifting of State (`P : S → Type`, no
`Prop`), the Σ-partner of the `□` lifting under the parity grading — the second canonical drop-monad
(after Reader) shown to carry it, and via a genuinely *threaded* (not diagonal) section. -/
theorem state_sigma_monad_lifting :
    (∀ (m : Bool → Bool × S) (x : StateSigma P m),
        etaSigTCState P m (sMuBwd P (sEta m) x) = x) ∧
      (∀ (m : Bool → Bool × S) (x : StateSigma P m),
          TetaSigState P m (sMuBwd P (fun s => ((m s).1, sEta (m s).2)) x) = x) ∧
        (∀ (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S)))
            (x : StateSigma P (sDdiag mmm)),
              muSigTCState P mmm (sMuBwd P (sDd mmm) x)
                = TmuSigState P mmm (sMuBwd P (sEe mmm) x)) :=
  ⟨state_sigma_left_unit P, state_sigma_right_unit P, state_sigma_assoc P⟩

/-! ## 10. The triptych for State: at the *same* base monad State, ∏ ✗ / □ ✓ / Σ ✓

The State mirror of §8, completing the triptych for the second canonical drop-monad. At State,
exhibited simultaneously:

* the proof-relevant **∏**-container `T_M`-monad has **no** multiplication (`κ_μ` not
  forward-total, `state_kappa_not_total`, §2) — the direction Ahman–Bauer single out;
* the proof-irrelevant **□** predicate lifting **is** a monad (`state_box_mult`, §5), because the
  reverse (threaded) covering is universal (`state_reverse_total_always`);
* the proof-relevant **Σ**-container lifting **is** a monad (`state_sigma_monad_lifting`, §9), via
  the *threaded* section — a different `(U1,U2,A)` instance from Reader's diagonal.

So the parity grading is certified at both canonical drop-monads, and by two structurally distinct
sections (diagonal for Reader, threaded for State): dropping proof-relevance is unnecessary for a
lifting to exist — one instead switches `∏ ⇝ Σ`. -/

/-- **The proof-relevance triptych for State.** `∏` fails; `□` holds; `Σ` holds — the last as a
genuine proof-relevant monad lifting via the *threaded* section (unit + associativity displayed).
Parameterised by the arbitrary base family `P` witnessing the Σ lifting for every container. -/
theorem state_proof_relevance_triptych :
    (¬ StateKappaTotal Fw) ∧
      (∀ (F : Bool → Bool × (Bool → Bool × Lbl)) (Q : Lbl → Prop),
          StateBoxBox Q F → StateBox Q (stateMu F)) ∧
        (∀ (m : Bool → Bool × S) (x : StateSigma P m),
            etaSigTCState P m (sMuBwd P (sEta m) x) = x) ∧
          (∀ (mmm : Bool → Bool × (Bool → Bool × (Bool → Bool × S)))
              (x : StateSigma P (sDdiag mmm)),
                muSigTCState P mmm (sMuBwd P (sDd mmm) x)
                  = TmuSigState P mmm (sMuBwd P (sEe mmm) x)) :=
  ⟨state_kappa_not_total, state_box_mult, state_sigma_left_unit P, state_sigma_assoc P⟩

end ReaderStateOutsidePiMendler

end Containers
