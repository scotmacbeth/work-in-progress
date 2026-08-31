# Monoids and comonoids internal to **Cont**, for the four canonical monoidal structures

**MacBeth — 2026-07-19.** Book deliverable for Neil Ghani.
Verifier: `scratch/2026-07-19-cont-monoid-verify.py` (self-contained, built from scratch; checks the
monoid/comonoid axioms by *direct composition of Poly-morphisms* against the explicit associator and
unitors of each tensor — no structure is assumed). All counts below are brute-forced over containers
with shapes ≤ 3 and fibres ≤ 3, cross-checked against independent enumerations.

Conventions. A container `c = (S, P)`, `P : S → Set`, `⟦c⟧(X) = Σ_{s∈S} X^{P(s)}`. A Poly morphism
`c → d` is a **forward** shape map `φ : S_c → S_d` plus, for each `s`, a **backward** map
`φ♯_s : d[φ s] → c[s]`. Monoid `= (μ:c⊙c→c, η:I→c)`; comonoid `= (δ:c→c⊙c, ε:c→I)`.

---

## The table

| ⊙ (unit) | **COMONOIDS** | **MONOIDS** | `⟦–⟧` lifting into `[Set,Set]` |
|---|---|---|---|
| **`+`** coproduct (unit `0 = (∅,!)`) | **only `0` itself** — the empty container. A counit `ε:c→0` needs `S_c→∅`, forcing `S_c=∅`. *[trivial — cocartesian]* — **proved** | **every container, uniquely** — codiagonal `∇:c+c→c`, unit the initial map `0→c`. *[trivial — cocartesian]* — **prior-art** | `⟦c+d⟧ = ⟦c⟧ + ⟦d⟧` (pointwise coproduct of functors), `⟦0⟧ = ∅` (initial functor). `⟦–⟧` strong monoidal. |
| **`×`** product (unit `1 = (1,*↦∅)`) | **every container, uniquely** — diagonal `Δ:c→c×c`, terminal counit `ε:c→1`. *[trivial — cartesian]* — **prior-art** | **monoid on shapes + backward routing, with an EMPTY unit-fibre.** `η:1→c` forces a unit shape `e` with `P(e)=∅`; `(S,·,e)` is an ordinary monoid; `μ♯_{s,t}:P(s·t)→P(s)⊔P(t)` routes each output position to one factor (`μ♯_{e,s}=inr`, `μ♯_{s,e}=inl`, + associativity). No empty-fibre shape ⟹ **no monoid at all**. When all fibres are empty, `= ordinary monoids on S`. *[the genuine `×` cell]* — **computed** | `⟦c×d⟧ = ⟦c⟧ × ⟦d⟧` (pointwise product), `⟦1⟧ = 1` (terminal functor). `⟦–⟧` strong monoidal; a `×`-monoid ↦ a monoid object for the pointwise product of endofunctors. |
| **`⊗`** Dirichlet / Day of `(Set,×)` (unit `y`) | **families of monoids** `Σ_s y^{M_s}`, each `M_s` an *arbitrary* monoid. `δ` forces the diagonal on shapes; `δ♯_s:c[s]×c[s]→c[s]` is a monoid on each fibre. `Comon(Cont,⊗,y) ≅ Fam(Mon^op)`; cocommutative `= Fam(CMon^op)`. — **proved** (MacBeth 07-17; answers Niu–Spivak Ch 9 Q5, Poly/⊗ slice) | **monoid on shapes + oplax fibre-functor.** `μ` forces a monoid `(S,·,e)` on shapes; `μ♯_{s,t}:P(s·t)→P(s)×P(t)` is the oplax structure map of an **oplax monoidal functor `P:(S,·,e)→(Set,×,1)`** (oplax unit `P(e)→1` forced). *Dual of the comonoid cell.* — **computed** (Niu–Spivak Rmk 3.78 flags this as *future work* — no novelty claimed) | `⟦c⊗d⟧ = ⟦c⟧ ⊗_Dir ⟦d⟧` (Dirichlet product of functors, `Σ X^{p[s]×q[t]}`), `⟦y⟧ = Id`. `⟦–⟧` strong monoidal. |
| **`◁`** sequential / composition (unit `y`) | **small categories** `=` directed containers. — **prior-art** (Ahman–Uustalu; Dorta–Jarvis–Niu Thm 4.3; MacBeth Lean M3/M3b, machine-checked) | **polynomial monads.** — **prior-art** (Gambino–Kock arXiv:0906.4931 Thm 4.5; MacBeth `Free.lean`) | `⟦c◁d⟧ = ⟦c⟧ ∘ ⟦d⟧` (composition of functors, on the nose), `⟦y⟧ = Id`. `⟦–⟧` strong monoidal ⟹ `◁`-monoid ↦ **monad**, `◁`-comonoid ↦ **comonad** on Set. |

`⟦–⟧ : Cont → [Set,Set]` is fully faithful with image the polynomial functors, and is **strong monoidal
for all four structures at once** (its image being, respectively, pointwise `+`, pointwise `×`, the
Dirichlet product, and composition of endofunctors). So every (co)monoid row maps bijectively onto the
polynomial (co)monoids for the matching functor operation.

---

## Brute-force ledger (verifier output)

Counts of *labelled* structures on the named container; `[a,b]` = two shapes with fibres of size `a,b`.

**`⊗` Dirichlet.**

| container | ⊗-comonoids | ⊗-monoids |
|---|---|---|
| `y=[1]` | 1 | 1 |
| `[2]` | 4 | 1 |
| `[0]` | 0 | 1 |
| `[1,1]` | 1 | 4 |
| `[1,2]` | 4 | 9 |
| `[2,2]` | 16 | — |

- ⊗-comonoids match `Π_s (#labelled monoids on P(s))` exactly: `[2]→4`, `[1,2]→1·4=4`, `[2,2]→4·4=16`.
  (`#labelled monoids` on sizes `0,1,2,3 = 0,1,4,33`; empty fibre ⟹ 0, since a monoid needs a unit.)
- ⊗-monoids: the shape map is a monoid on `S` in *every* solution (checked); when all fibres are
  singletons the fibre-functor is forced, so the count `= #labelled monoids on S` (`[1,1]→4`).

**`×` product.**

| container | ×-comonoids | ×-monoids |
|---|---|---|
| any (incl. `0`) | 1 | — |
| `[1],[2],[1,1],[1,2]` (no empty fibre) | 1 | **0** |
| `[0]` | 1 | 1 |
| `[0,1]` | 1 | 2 |
| `[2,0]` | 1 | 8 |
| `[0,0]` (all empty) | 1 | 4 |
| `[0,0,0]` (all empty) | 1 | 33 |

- ×-comonoids: always exactly 1 (cartesian collapse), including the empty container.
- ×-monoids: exist **iff** some shape has an empty fibre (the unit shape). Shape map is a monoid on `S`
  in every solution. All-empty-fibre case reproduces the labelled-monoid sequence `1,4,33` — the *same*
  integers as the ⊗-comonoid single-fibre column, but living on the shape set instead of a fibre.

**`+` coproduct.** comonoids: `0` on the true empty container `(∅,!)`, else always `0`; monoids: always `1`.
(Note: `[0] = cont([0])` has one shape with an empty fibre — it is *not* the initial object `0=cont([])`;
hence `+`-comonoids on it `= 0`, and `+`-comonoids on the genuine `0` `= 1`.)

---

## Derivations for the two genuine cells (coordinates)

### `×`-monoids  (grade: computed)

`c×c` has shapes `S×S` and positions `P(s)⊔P(t)` (a **coproduct**). A monoid `(μ,η)`:

- **Unit `η:1→c`.** Forward `1→S` picks `e∈S`. Backward `η♯:P(e)→1[*]=∅`. A map into `∅` exists only
  if `P(e)=∅`. **The unit shape must have empty positions.** (This is a container-specific obstruction
  with no analogue for `⊗` or `◁`, whose unit `y` has a *nonempty* fibre.)
- **Multiplication `μ:c×c→c`.** Forward `m:S×S→S`; the associativity/unit laws, read on shapes, say
  `(S,m,e)` is an ordinary monoid (verified: shape map is a monoid in every solution).
- **Backward `μ♯_{s,t}:P(m(s,t))→P(s)⊔P(t)`** assigns to each output position a position of *one* of
  the two inputs — a "which-factor-do-I-read-from" routing. Unit laws force `μ♯_{e,s}=inr` and
  `μ♯_{s,e}=inl`; associativity is a coherence (pentagon) on the routings.

So a `×`-monoid `=` **an ordinary monoid on the shapes whose identity element has an empty fibre,
together with a coherent backward routing of positions.** Generic containers (all fibres nonempty)
admit **none**. Brute force: `[0,1]→2`, `[2,0]→8`, all-empty `[0,0]→4=[0,0,0]→33` (` = ` monoids on `S`).

*Conceptual gloss.* `(Cont,×)` is the categorical product, so this is just "internal monoid object in
`Cont ≅ Fam(Set^op)`"; the empty-unit-fibre condition is the concrete shadow of the terminal object
`1=(1,∅)` having an empty fibre.

### `⊗`-monoids  (grade: computed — Niu–Spivak Rmk 3.78 open/future-work)

`c⊗c` has shapes `S×S` and positions `P(s)×P(t)` (a **product**). Dual to the ⊗-comonoid story:

- **Unit `η:y→c`.** Forward picks `e∈S`; backward `P(e)→y[*]=1` is the (forced) terminal map.
- **Multiplication.** Forward `m:S×S→S` is a monoid `(S,·,e)` (verified in every solution). Backward
  `μ♯_{s,t}:P(s·t)→P(s)×P(t)` is the **oplax structure map** of an oplax monoidal functor
  `P:(S,·,e)→(Set,×,1)` (view the monoid `S` as a discrete monoidal category). Its oplax unit `P(e)→1`
  is the forced terminal map; associativity of `μ` = the oplax hexagon.

So a `⊗`-monoid `=` **a monoid on the shapes + an oplax monoidal functor `P:S→(Set,×)` on the fibres.**
This is the exact **dual** of the ⊗-comonoid = *family of monoids* (`=` a **lax** structure: diagonal on
shapes, a monoid on each fibre). The comonoid/monoid duality *is* the lax/oplax duality, with the shape
map dualising **forced-diagonal ↔ arbitrary-monoid**. Brute force: `[1,1]→4`, `[2]→1`, `[1,2]→9`.

---

## Honest grade summary

| cell | grade | citation |
|---|---|---|
| `+`-comonoid (only `0`) | proved (elementary) | cocartesian folklore |
| `+`-monoid (every obj, unique) | prior-art | cocartesian monoidal (Mac Lane) |
| `×`-comonoid (every obj, unique) | prior-art | cartesian monoidal (Mac Lane) |
| **`×`-monoid** (shape-monoid + empty unit-fibre + routing) | **computed** (brute ≤3) | container-specific; no prior classification found |
| **`⊗`-comonoid** (families of monoids) | **proved** | MacBeth `2026-07-17-bare-dirichlet-comonoid.md`; answers Niu–Spivak Ch 9 Q5 (Poly/⊗); Rmk 3.78 dual |
| **`⊗`-monoid** (shape-monoid + oplax fibre-functor) | **computed** (brute ≤3) | Niu–Spivak Rmk 3.78 (open / future work); orthogonal to Dorta–Jarvis–Niu, DUV 2509.25879 |
| `◁`-comonoid (small categories) | prior-art | Ahman–Uustalu; DJN Thm 4.3; MacBeth Lean M3/M3b |
| `◁`-monoid (polynomial monads) | prior-art | Gambino–Kock 0906.4931; MacBeth `Free.lean` |

---

## How to present in the book (recommendation)

**Do not catalogue all eight cells as equals.** Four of them are the cartesian / cocartesian collapse and
should be dispatched in a single sentence each: for `×` (cartesian) *every* object is a comonoid uniquely,
for `+` (cocartesian) *every* object is a monoid uniquely, and the two opposite corners degenerate to
"only the unit." State these as one boxed remark ("the canonical structures give degenerate (co)monoids —
this is why the interesting theory lives elsewhere").

Spend the real estate on the **two Day-exotic structures `◁` and `⊗`**, presented as a **2×2 of dualities**:

- **`◁`**: comonoid `=` **category**, monoid `=` **monad** — the Poly↔Cat and Poly↔monad dictionaries.
- **`⊗`**: comonoid `=` **family of monoids** (lax), monoid `=` **monoid-on-shapes + oplax functor**
  (oplax). Here the punchline is that the **comonoid/monoid duality is literally the lax/oplax duality**,
  and the shape map flips **forced-diagonal ↔ free monoid**. This is the prettiest fact in the table and
  should be the section's climax.

Two honest asides worth one line each: (i) the `×`-monoid cell is *not* vacuous — it is a genuine, if
minor, container-specific notion (monoid on shapes, but the identity must have an empty fibre), and it
reproduces the labelled-monoid sequence `1,4,33`; (ii) `⟦–⟧` is strong monoidal for all four structures
at once, so each row is simultaneously a statement about polynomial endofunctors (comonads, monads,
Dirichlet-product (co)monoids, pointwise (co)monoids). Grade the `⊗`-monoid cell `computed` and cite
Niu–Spivak Rmk 3.78 as the open-problem anchor — do **not** claim it as a theorem yet.
