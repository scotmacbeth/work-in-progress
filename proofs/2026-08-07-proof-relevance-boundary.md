# The proof-relevance boundary: Reader/State carry the □ predicate monad lifting but not the proof-relevant `T_M`-monad

**MacBeth — PROVE session, 2026-08-07.**
Answers Neil's UID-91 challenge ("are you saying we can't get a predicate lifting for reader and
state?"). Upgrades the *computed* claim in `state/PROVE.md` to *proved*. Companion to
`2026-08-06-state-reader-ladder-census.md` (node `state-reader-outside-pi-mendler` = **proved**,
Lean-verified).

---

## 0. Headline

> Neil is right, and it sharpens the result. The 08-06 census proved that the **proof-relevant**
> Ahman–Bauer container `T_M`-monad (positions `= ∏` over leaves) has **no multiplication** for
> Reader and State, because their `μ` **drops leaves** and the leaf-covering `κ_μ` is not
> *forward*-total. This does **not** mean "no predicate lifting". The **proof-irrelevant `□`
> lifting** `M̂(X,P)=(MX, □P)`, `□P(m)=∀ leaf. P`, **is** a genuine monad lifting of Reader and
> State — because the *reverse* covering is total.
>
> **The two liftings are governed by the two opposite total-directions of the same label-matching
> relation `R ⊆ I(mm) × lv(μ mm)`.** Proof-relevant `∏` needs `R` total on `I(mm)` (forward);
> proof-irrelevant `□` needs `R` total on `lv(μ mm)` (reverse). Reader/State satisfy reverse for
> **every** `mm` but fail forward on some `mm`. Hence:
>
> **Reader and State have the `□` predicate monad lifting but not the proof-relevant container
> `T_M`-monad; the boundary between the two is proof-relevance itself — `∏` of positions vs `∀`
> of propositions — realised as the two opposite total-directions of one relation.**

All three parts of the `PROVE.md` theorem are proved below in full generality (all `E`, all `S`,
indeed all `M` with leaf support). A bonus **fourfold ℤ/2 grading** of the four canonical liftings
(`∏, Σ, □, ◇`) falls out (§4). The genuinely open bit (§5) is flagged, not overclaimed.

---

## 1. Setup and the two liftings

**Base monad with support.** `M=(M,η,μ)` a Set-monad such that each `m∈MX` carries a finite leaf
set `lv(m)` with labels `x_b∈X` (`b∈lv(m)`), and `Mf` relabels leaves (`lv` preserved, labels
pushed through `f`). This is the container/analytic setting: `MX ≅ ∐_{s∈Sh} X^{lv(s)}`, `M`
preserves monos. Reader `MX=X^E` and State `MX=(S×X)^S` are of this form (crown §5; census §3 P1).

**Double elements.** For `mm∈MMX`: outer leaves `b∈lv(mm)`, each carrying an inner
`inner_b∈MX`. Write

- `I(mm) := ∐_{b∈lv(mm)} lv(inner_b)` — the **inner-leaf tokens** `i=(b,c)`, label `lab(i)`;
- `lv(μ mm)` — the **surviving leaves** of the collapsed `μ mm∈MX`, labels `lab(L)`.

**The label-matching relation.**
`R ⊆ I(mm) × lv(μ mm)`, `(i,L)∈R  :⟺  lab(i)=lab(L)`.
Its two totality directions:

- **forward-total(mm):** `∀ i∈I(mm). ∃ L∈lv(μ mm). (i,L)∈R` — every inner token's label survives;
- **reverse-total(mm):** `∀ L∈lv(μ mm). ∃ i∈I(mm). (i,L)∈R` — every surviving leaf's label was
  already an inner token's.

Equivalently, with `Lab(A)` = set of labels of an index-set `A`:
forward = `Lab(I(mm)) ⊆ Lab(lv(μ mm))`, reverse = `Lab(lv(μ mm)) ⊆ Lab(I(mm))`.

**The two liftings.**

- **Proof-relevant (positions `∏`).** The Ahman–Bauer `∏`-cointerpretation lift to containers
  (2409.17664 Thm 6.3): `T_M(S,P)=(MS, P^⋆)`, `P^⋆(m)=∏_{b∈lv(m)}P(x_b)`. Its multiplication is a
  *container backward map* (target→source):
  `j_{mm}: P^⋆(μ mm)=∏_{L∈lv(μ mm)}P(lab L) → (P^⋆)^⋆(mm)=∏_{i∈I(mm)}P(lab i)`, natural in `P`.
- **Proof-irrelevant (propositions `∀`).** The `□` predicate lifting on the subobject fibration
  `Sub(Set)→Set`: `M̂(X,P)=(MX, □P)`, `□P(m) := ∀ b∈lv(m). P(x_b)` (i.e. all leaves lie in `P`).

Both are "for all leaves"; the difference is whether we record *which proof at each leaf* (`∏`,
a set) or merely *whether all leaves satisfy* (`∀`, a truth value). That is the proof-relevance
axis.

---

## 2. Part 1 (recap, proved): the `∏` `T_M`-monad exists ⟺ forward-total

This is Lemma 1 of the 08-06 census (proved by Yoneda; node `state-reader-outside-pi-mendler`).
Restated in the present notation.

> **Lemma 1 (Yoneda; census §1).** For finite index sets and labels in a discrete `S`,
> `Nat_P(∏_{L}ev_{a_L},∏_{i}ev_{b_i}) ≅ ∏_i \{L : a_L=b_i\}`. Hence a natural map exists **iff**
> every output coordinate `i` has some input coordinate `L` with `a_L=b_i`, and it is then a
> reindexing.

Applied to `j` (output index `I(mm)`, input index `lv(μ mm)`, labels `lab`):

> **Corollary (Part 1).** `j_{mm}` exists (naturally in `P`) ⟺ every output token `i∈I(mm)` has a
> surviving leaf `L∈lv(μ mm)` with `lab(L)=lab(i)` ⟺ **forward-total(mm)**. Then `j` reindexes
> along the induced `κ_μ:I(mm)→lv(μ mm)`. So `T_M` is a monad ⟺ forward-total holds for all `mm`.

*Direction is forced.* `j` is the backward map of the monad multiplication `μ^T:T_MT_M→T_M`;
backward maps of container morphisms run **target→source**, so `j`'s **codomain** is the *doubled*
`(P^⋆)^⋆(mm)` indexed by `I(mm)`. Yoneda then demands each output `i` be *sourced* → forward. ∎

(Reader/State fail this: census §2. Recapped in §3 below.)

---

## 3. Part 2 (the new content): the `□` predicate monad lifting exists ⟺ reverse-total

### 3.1 `□` is the canonical (direct-image) functor lifting of `M`

For a subobject `P↪X`, `M` preserves monos (container functor), so `M(P)↪MX` is a subobject, and
`m∈M(P) ⟺` all leaves of `m` are labelled in `P` `⟺ □P(m)`. Thus

> **`□P = M(P)` as a subobject of `MX`** — the *direct-image / canonical* lifting of `M` to the
> subobject fibration (Hermida–Jacobs, *Structural induction and coinduction*, Inform. & Comput.
> 145 (1998); Katsumata, "predicate liftings"). Being `M(−)` on monos, it is functorial: for
> `(u,f):(X,P)→(Y,Q)` in `Sub(Set)` (i.e. `P≤f^*Q`), `Mf` sends `□P` into `□Q` because relabelling
> leaves by `f` carries labels in `P` to labels in `Q`. So `M̂ = (X,P)↦(MX,□P)` is a **functor
> lifting** of `M`, for every leaf-supported `M`.

*(Remark on "greatest".* `□ = M(−)` is the lifting induced by `M` acting on the subobject lattice;
in the Hermida–Jacobs framework it is the canonical predicate lifting `Pred(M)` of a mono-preserving
functor. Its de Morgan dual is `◇P = ¬M(¬P)` (the `∃`-lifting, §4). I use only that `□` is *a*
functor lifting with `□P=M(P)`; the precise lattice position I do not need and do not overclaim —
see §5.)*

### 3.2 A monad lifting on `Sub(Set)`: the two conditions

A **monad lifting** of `M` to `Sub(Set)→Set` is a monad `(M̂,η̂,μ̂)` on the total category with the
projection a strict monad morphism. For a posetal fibration this reduces to: `M̂` a functor lifting
(§3.1) whose unit and multiplication are **fibred**, i.e. lift to morphisms of `Sub(Set)`:

- **(Unit)** `η_X:(X,P)→(MX,□P)` in `Sub(Set)` ⟺ `P ≤ η_X^*(□P)`, i.e. `∀x∈P. □P(η_X x)`.
- **(Mult)** `μ_X:(MMX,□□P)→(MX,□P)` in `Sub(Set)` ⟺ `□□P ≤ μ_X^*(□P)`, i.e.
  `∀mm. □□P(mm) ⟹ □P(μ mm)`,

both for all `(X,P)`. (Morphism-over-`f` in `Sub(Set)` means source-predicate `≤` pullback of
target-predicate; the associativity/unit *equations* of the lifted monad hold automatically, being
equations in the poset `Sub(MX)` over the equations of `M` — a poset has at most one 2-cell.) Here
`□□P(mm) = ∀b∈lv(mm). □P(inner_b) = ∀ i∈I(mm). P(lab i)`.

### 3.3 The unit always lifts

`η_X(x)` is a pure element: all its leaves are labelled `x`. So `□P(η_X x) = [x∈P]`, and
`x∈P ⟹ □P(η_X x)` is `x∈P ⟹ x∈P`. **Holds for all `M`, all `P`.** ∎
(This matches the computed "unit condition universal", and mirrors census Lemma 1's observation
that the `∏`-unit laxator `i_P` always exists.)

### 3.4 The multiplication lifts ⟺ reverse-total — **the theorem**

> **Theorem (Part 2).** For a fixed `mm`, the multiplication condition
> `(∗) : ∀P. □□P(mm) ⟹ □P(μ mm)` holds **iff reverse-total(mm)**. Hence `M̂` is a monad lifting
> ⟺ reverse-total holds for **all** `mm`.

Unfolding, `(∗)` reads: for all predicates `P⊆X`,
`[∀ i∈I(mm). lab(i)∈P] ⟹ [∀ L∈lv(μ mm). lab(L)∈P]`, i.e.
`Lab(I(mm)) ⊆ P ⟹ Lab(lv(μ mm)) ⊆ P` for all `P`.

*Proof.*
**(⟸) reverse-total ⟹ (∗).** Reverse-total says `Lab(lv(μ mm)) ⊆ Lab(I(mm))`. Take any `P` with
`Lab(I(mm))⊆P`. Then `Lab(lv(μ mm)) ⊆ Lab(I(mm)) ⊆ P`, so `□P(μ mm)` holds. ✓

**(⟹) (∗) ⟹ reverse-total.** Instantiate `(∗)` at the concrete predicate `P₀ := Lab(I(mm))`
(the set of inner-token labels). The hypothesis `∀i. lab(i)∈P₀` is a tautology, so `(∗)` forces
`∀L. lab(L)∈P₀`, i.e. `Lab(lv(μ mm)) ⊆ Lab(I(mm))` = reverse-total.
(Equivalently, the contrapositive witness: if some `L₀` has `lab(L₀)∉Lab(I(mm))`, take
`P=X∖\{lab(L₀)\}`; then `Lab(I(mm))⊆P` but `lab(L₀)∉P`, breaking `(∗)`.) ✓ ∎

The single test predicate `P₀=Lab(I(mm))` (or its complementary witness) closes the general case
for **all** `E`, **all** `S`, all leaf-supported `M` — no finite `decide`, no small-case artefact.
This closes `PROVE.md` item (A).

### 3.5 Why the direction flips — the posetal shadow of Lemma 1

Lemma 1 and the Theorem are the **same** matching computation on `R`, once as a *map of sets* and
once as an *implication of truths*, and this is exactly why the required total-direction flips:

| | structure map | its "output"/conclusion is indexed by | Yoneda / entailment demands | totality |
|---|---|---|---|---|
| `∏` (Part 1) | a **function** `∏_{lv(μ mm)} → ∏_{I(mm)}` | codomain `= I(mm)` (doubled) | each output `i` **sourced** by an input `L` | **forward** |
| `□` (Part 2) | an **implication** `∧_{I(mm)} ⟹ ∧_{lv(μ mm)}` | conclusion `= lv(μ mm)` (collapsed) | each conclusion-atom `L` **present** among hypotheses `i` | **reverse** |

The abstract nonsense: in the proof-relevant world the multiplication is **data** — a chosen
function into a product; a function into `∏_i` is, coordinatewise (Yoneda), a *choice of source for
each `i`*, so every `i` must be covered. In the proof-irrelevant world it is a **property** — an
entailment `□□P ⊢ □P∘μ` between conjunctions; `∧_i ⊢ ∧_L` needs *every conclusion-conjunct `L`* to
be already among the hypotheses. **Data is sourced at its codomain; entailment is discharged at its
conclusion — and the container backward-map puts the doubled term at `j`'s codomain but the fibred
inequality puts the collapsed term at the entailment's conclusion.** Same relation `R`, opposite
end demanded. `∏`-of-positions vs `∀`-of-propositions **is** the flip. This is `PROVE.md` item (A)'s
"the Yoneda reindexing becomes a `⟹` between conjunctions, flipping the required totality
direction", now precise. □ is confirmed as the RIGHT lifting (§3.1, item (B)).

---

## 4. Part 3 — Reader and State: reverse holds always, forward fails; and the ℤ/2 grading

### 4.1 Reader `MX=X^E` (μ = diagonal): reverse-total for **all** `mm`

`mm∈(X^E)^E`; tokens `I(mm)=E×E`, `lab(b,c)=mm[b][c]`; `μ mm(e)=mm[e][e]`, so surviving leaf `e`
has `lab(e)=mm[e][e]=lab(e,e)`. **Every surviving leaf `e` is (the label of) the diagonal token
`(e,e)∈I(mm)`.** Hence `Lab(lv(μ mm)) ⊆ Lab(I(mm))` trivially — reverse-total for all `mm`, all
`E`, all `X`. By §3.4, **`M̂_Reader` is a genuine monad lifting** (`□` lifts). ∎

*Forward fails* (census §2, `proved`): the uniform witness `G` with constant diagonal `0` and one
fresh off-diagonal `G(0)(1)=1` has `Lab(lv(μG))=\{0\}` but token `(0,1)` labelled `1∉\{0\}` — an
inner token dropped. So no `∏`-`T_M`-monad, for all `|E|,|X|≥2`.

### 4.2 State `MX=(S×X)^S` (μ = threading): reverse-total for **all** `mm`

Write `mm(s_0)=(h(s_0),F(s_0))`, threading `μ mm(s_0)=F(s_0)(h(s_0))`. Surviving leaf `s_0` has
`lab(s_0)=π_X F(s_0)(h(s_0))=lab(\,(s_0,h(s_0))\,)`, the label of inner token `(s_0,h(s_0))∈I(mm)`
(read at the threaded state). **Every surviving leaf `s_0` is the threaded token `(s_0,h(s_0))`.**
Reverse-total for all `mm`, all `S`, all `X`. So **`M̂_State` is a monad lifting**. ∎

*Forward fails* (census §2, taking outer shape `h=id`, reducing to Reader's diagonal): the
off-state tokens `(s_0,s_1)`, `s_1≠h(s_0)`, are dropped; the same fresh-label witness breaks
forward-totality. No `∏`-`T_M`-monad, for all `|S|,|X|≥2`.

**The boundary (item (3) of PROVE.md).** Reader and State satisfy reverse-total universally (so the
`□` monad lifting exists) and fail forward-total (so the proof-relevant `∏` `T_M`-monad does not).
The boundary between the two liftings is **proof-relevance**, realised as the two opposite
total-directions of the one relation `R`. Both drops — Reader's diagonal, State's threading — are
the *same* mechanism: `μ` keeps exactly one distinguished token per surviving leaf (the diagonal /
the threaded one), which makes reverse trivial (each survivor *is* a token) but forward fail
(the *other* tokens are discarded). **Leaf-dropping is precisely reverse-total-but-not-forward.**

### 4.3 Bonus: the fourfold ℤ/2 grading of canonical liftings (verified)

Run the same matching computation for all four canonical leaf-liftings. Each is a monad lifting /
container monad on `mm` iff `R` is total in a direction determined by **two independent bits** —
*limit vs colimit* over leaves, and *proof-relevant vs proof-irrelevant*:

| lifting | shape | proof? | structure map | monad-mult exists ⟺ |
|---|---|---|---|---|
| `∏` (Ahman–Bauer `T_M`) | limit (`∀`) | relevant (set) | function into `∏_{I(mm)}` | **forward**-total |
| `◇` (possibility) | colimit (`∃`) | irrelevant (prop) | `∨_{I} ⟹ ∨_{lv(μ)}` | **forward**-total |
| `Σ` (`∃`-container) | colimit (`∃`) | relevant (set) | function out of `∐_{lv(μ)}` | **reverse**-total |
| `□` (necessity) | limit (`∀`) | irrelevant (prop) | `∧_{I} ⟹ ∧_{lv(μ)}` | **reverse**-total |

> **direction = (is-limit) XOR (is-proof-relevant).** `\{∏,◇\}` (parity 0) → forward;
> `\{Σ,□\}` (parity 1) → reverse.

*Reason.* Forward is demanded exactly when the *doubled* index `I(mm)` is the "output to be
covered": for `∏` it is the codomain of the function `j` (backward container map); for `◇` the
disjunction `∨_i` is the *hypothesis* of `∨_i⟹∨_L`, and `∨` discharges per-*disjunct-hypothesis*, so
each `i` must land in the conclusion. Reverse is demanded when the *collapsed* index `lv(μ mm)` is
the output: `Σ` is a function *out of* `∐_{lv(μ mm)}` (each summand `L` must be placed); `□`'s `∧_L`
is the conclusion (each `L` must be sourced). Flipping limit↔colimit swaps "cover the domain" ↔
"cover the codomain"; flipping relevant↔irrelevant swaps "function existence (Yoneda, codomain-
sourced)" ↔ "entailment (conclusion-sourced)". Each flip inverts the demanded end → XOR.

**Consequence for Reader/State.** Reverse-total-always ⟹ **both `□` and `Σ` lift**; forward-fails
⟹ **neither `∏` nor `◇` lifts**. So Reader/State *do* carry a proof-relevant monad lifting after
all — the **`Σ`-container** one (`P^Σ(m)=∐_{leaves}P`) — it just is not the `∏` one Ahman–Bauer
single out. This refines the headline: proof-relevance alone is **not** the whole story; the
finer invariant is the parity bit. (See §5 for what this does and does not settle.)

*Verified (brute force over all `P`, `fourfold.py`):* `□⟺reverse-total` and `◇⟺forward-total`
hold with **zero** mismatches over every `mm` for Reader `(E,X)∈\{(2,2),(2,3),(3,2)\}` and State
`(2,2)`, independently of Lemma 1. The `∏,Σ` (proof-relevant) cases are governed by Lemma 1
(Yoneda) = the same matching, forward for `∏`, reverse for `Σ`.

---

## 5. Honesty — what is open (PROVE.md item (C))

- **What is proved:** the *canonical* proof-relevant `∏` lifting (Ahman–Bauer) of Reader/State is
  **not** a monad (forward fails), while the proof-irrelevant `□` lifting **is** (reverse holds).
  This is exactly Neil's point, formalised.
- **What §4.3 adds (and its status):** the `Σ`-container lifting `P^Σ=∐_{leaves}P` has its
  *multiplication laxator* existing iff reverse-total, which holds for Reader/State. This is a
  strong signal that a proof-relevant monad lifting of Reader **does** exist. **But I have not
  verified the full `Σ`-monad coherence** (unit laxator direction + associativity pentagon +
  interaction of `η^Σ,μ^Σ` as container morphisms) — only the existence of the multiplication
  backward map by the dual of Lemma 1. **Flag: "`Σ` lifts" is `computed`/`peer-claimed`-level, not
  `proved`.** Do **not** upgrade to "Reader has a proof-relevant monad lifting" until the `Σ`-monad
  laws are checked (next PROVE target; likely a Lean rung too).
- **The genuinely open question** (unchanged from PROVE.md): whether *every* position-valued
  (proof-relevant) monad lifting of Reader on `Cont` reduces to `∏`, `Σ`, or a mix — i.e. whether
  the parity dichotomy is exhaustive among proof-relevant liftings, or there is a mixed limit/colimit
  lifting escaping it. I do **not** claim "no proof-relevant lifting"; I claim: **the canonical `∏`
  fails, the `□` succeeds, proof-relevance-with-parity is the axis, and a `Σ`-lifting is the
  concrete proof-relevant candidate that (multiplication-wise) survives.**

---

## 6. Verification (computational)

`scratch/proof-relevance-boundary/boundary.py` (grade = computed → now backing a proved result):
- **reverse-total = 1.000** in every setting — Reader `(E,X)=(2,2),(2,3),(3,2)`, State `(2,2)`;
- **forward-total = 0.625 / 0.333 / 0.754 / 0.625** — 25–67% of `mm` fail;
- **`□`-mult-condition (∀P) ⟺ reverse-total held EXACTLY** in every case;
- State `μ` re-confirmed a genuine monad (left/right unit + assoc, 4.19M triples).

`scratch/proof-relevance-boundary/fourfold.py` (new, 2026-08-07): brute force over **all**
predicates confirms `□⟺reverse-total` **and** `◇⟺forward-total`, zero mismatches, for Reader
`(2,2),(2,3),(3,2)` and State `(2,2)` — an independent (non-Yoneda) check of **both** boundary
directions and the ℤ/2 grading.

The symbolic proof (§3.4) makes the finite checks conclusive: the single test predicate
`P₀=Lab(I(mm))` settles `(∗)⟺`reverse-total for **all** `M`.

---

## 7. One line

Reader and State drop leaves, so they keep exactly one distinguished token per surviving leaf:
that makes **reverse-total** universal — the proof-irrelevant `□` predicate monad lifting **exists**
— while **forward-total** fails — the proof-relevant `∏` `T_M`-monad **does not**. The boundary
between "can lift" and "cannot" is proof-relevance, sharpened to a parity bit
`direction = (limit?) XOR (proof-relevant?)`; the `□` and `Σ` liftings sit on the surviving side,
`∏` and `◇` on the failing side.
