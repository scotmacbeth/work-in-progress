# Monomial (Lens) subcategory of Cont: closure properties + citation

Date: 2026-07-19. Agent task for MacBeth.

**Setup.** Cont = category of containers `(S, P: S → Set)`, extension `⟦S,P⟧(X) = Σ_{s:S} X^{P(s)}`.
The **Lens / monomial subcategory** = full subcategory on objects with `P` CONSTANT, i.e. `P(s) = A`,
written `S·y^A` (extension `X ↦ S × X^A`). A Cont-morphism `S·y^A → T·y^B` is a **bimorphic lens**:
forward on-positions `f₁: S → T` and backward on-directions repackaged as `f♯: S × B → A`
(constant fibres let the per-position maps `B → A` merge into one function). This is the standard lens.

---

## TASK 1 — Closure verdict table

| Construction | Verdict | One-line justification |
|---|---|---|
| Binary **products** | **CLOSED** | `S·y^A × T·y^B`: shapes `S×T`, positions `P(s)+Q(t) = A+B` — constant. `= (S×T)·y^{A+B}`. |
| **Terminal** `1 = (1,∅)` | **CLOSED** | `1 = 1·y^0`, a monomial (`A = ∅`). |
| **Initial** `0 = (∅,!)` | **CLOSED** | `0 = ∅·y^A` (any `A`); position function vacuously constant. |
| Binary **coproducts** | **NOT CLOSED** | shapes `S⊔T`, positions `A` on `S`-part, `B` on `T`-part — non-constant unless `|A|=|B|` (or a summand empty). |
| **W-types / initial algebras / free monad** | **NOT CLOSED** | free monad on `S·y^A` = trees; positions = LEAVES; leaf-count varies per tree → non-constant. |

### Derivations

**(a) Products — CLOSED.** Cont/Poly product: `(Σ_s y^A) × (Σ_t y^B) = Σ_{(s,t)} y^{P(s)+Q(t)} = Σ_{(s,t)} y^{A+B}`.
Positions of every shape `(s,t)` are `A ⊔ B`, constant ⇒ monomial `(S×T)·y^{A+B}`.
Extension check: `|LHS(X)| = |S||X|^{|A|}·|T||X|^{|B|} = |S||T|·|X|^{|A|+|B|} = |RHS(X)|`. ✓
Since Cont is the ambient category and the product object lies in the full subcategory (with projections
being lenses), it IS the product there. **Book-confirmed**: Niu–Spivak p.134, `∏ B_i y^{A_i} = (∏B_i) y^{ΣA_i}`
"is still a monomial"; and Ex 3.67 #1 shows monomials closed under the parallel/Dirichlet product ⊗ too.

**(b) Terminal & Initial — both CLOSED.** Terminal of Cont/Poly is `y^0 = 1·y^∅` (monomial, `A=∅`).
Initial is `∅` = `∅·y^A` for any `A`; empty shape ⇒ position function vacuously constant ⇒ monomial (zero monomial).

**(c) Coproducts — NOT CLOSED.** Cont coproduct: shapes `S⊔T`; a shape from `S` keeps positions `A`,
a shape from `T` keeps positions `B`. Constant overall iff `|A| = |B|` (or one summand has empty shape).
So `S·y^A + T·y^B` is a monomial exactly when the direction-sets agree — generically it is a genuine
binomial `S·y^A + T·y^B`, not a monomial. Extension `|S||X|^{|A|} + |T||X|^{|B|}` is a single monomial in `|X|`
iff `|A|=|B|`.

**(d) W-types / free monad — NOT CLOSED.** The initial-algebra / inductive construction that stays inside
Poly is the free monad `m_p` on `p = S·y^A`: shapes = well-founded `S`-labelled, `A`-branching trees;
positions at a tree = its set of **leaves** (Gambino–Kock 2009, Thm 4.5). Leaf-count grows with tree size,
so positions are non-constant ⇒ not a monomial. (The bare W-type *set* `W_p`, viewed as the constant
container `W_p·y^0`, is trivially a monomial, but that is the uninteresting reading; the structure-preserving
"initial algebra in Poly" is the free monad, which fails.)

### Brute-force sanity check (container coordinates) — `lens_check.py`
- **Products:** 81/81 tuples `(|S|,|A|,|T|,|B|)` with `|S|,|T|∈{1,2,3}`, `|A|,|B|∈{0,1,2}`:
  product is monomial AND matches `(S×T)y^{A+B}` on extension counts for `X` of size 0..4. ✓
- **Coproducts:** of 81 tuples, 27 monomial / 54 non-monomial; and "monomial ⇔ |A|=|B|" holds in ALL 81. ✓
- **Terminal** `1·y^0` monomial: True. **Initial** `∅·y^-` monomial: True. ✓
- **Free monad** on `1·y^2` (unary-label binary trees), depth ≤ 3: distinct leaf-counts `{1,2,3,4,5,6,7,8}`
  ⇒ positions non-constant ⇒ not monomial. ✓

### Verdict on Neil's claim
Neil asserted the subcategory is "**missing products, coproducts, initial algebras**."
- **Products: Neil is WRONG.** Products ARE present and monomial: `S·y^A × T·y^B = (S×T)·y^{A+B}`.
  (Confirmed by hand, 81/81 brute force, AND explicitly in Niu–Spivak p.134.)
- **Coproducts: Neil is RIGHT.** Not closed (fails unless `|A|=|B|`).
- **Initial algebras / W-types: Neil is RIGHT.** Free monad has leaf-positions ⇒ not monomial.
  (Note: the initial *object* `0` IS monomial and closed; the failure is specifically initial *algebras*.)

MacBeth's hand-analysis is **confirmed**: products present; coproducts and W-types are the genuine failures.

---

## TASK 2 — Citation for "morphisms between monomials = lenses"

**Primary citation.** Niu & Spivak, *Polynomial Functors: A Mathematical Theory of Interaction*
(arXiv:2312.00990), **Example 3.41 "Lenses between monomials are bimorphic lenses"** (Ch. 3, §3.6).

Exact content:
- Definition of monomial: **Definition 2.15** (`p` is a monomial if `p ≅ I·y^A`).
- **Example 3.41**: a lens `f: I·y^A → J·y^B` is exactly an on-positions function `f₁: I → J` plus an
  on-directions map repackaged as a single function `f♯: I × B → A` (possible precisely because every
  position has the *same* direction-set). "In functional programming, such a pair of functions is called a
  **bimorphic lens**."
- **Full-subcategory statement (verbatim):** "In categorical terms, we may say that the **monomials in Poly
  span a full subcategory of Poly equivalent to the category of bimorphic lenses**, defined in [Hed18a]
  (here the category is named after its morphisms rather than its objects)." — so the subcategory has no
  special *name* beyond "monomials / bimorphic lenses"; [Hed18a] = Hedges' lens category.
- **get/put formulation, eqn (3.42):** `get := f₁` and `put := f♯ : I × B → A` — "each position `i` gets a
  position `f₁ i` and puts each direction `b ∈ B` back to a direction `f♯(i,b) ∈ A`."
  (Caveat: the book labels `get: J → I` in (3.42) while `f₁: I → J`; this is the FP domain/codomain
  relabelling for the "state = domain monomial `S·y^S`" reading — the underlying data is `f₁: I→J`,
  `f♯: I×B→A`, matching the task's `get: S→T`, `put: S×B→A`.)

**General lens definition** (context): Definition 3.1 (dependent lens = Poly-morphism) and
Definition 3.9 (on-positions `f₁: p(1)→q(1)`, on-directions `f♯: q[f₁(-)] → p[-]`).

**Supporting facts in the same source:**
- Special polynomials list (§3.6 / around eq.): constants `I`, linear `I·y`, representable `y^A`, monomial `I·y^A` (all with constant direction-cardinality) — Niu–Spivak Def. 2.15 discussion & the "special polynomials" table.
- Monomials closed under ⊗: Niu–Spivak, Exercise 3.67 #1 (`Ay^B ⊗ Cy^D = AC·y^{B+D}`).
- Product of monomials is a monomial: Niu–Spivak p.134 (Moore-machine codomain computation).
- Moore machines (Ch. 4) = lenses `S·y^S → I·y^A` between monomials — Example 4.2 region.

**Secondary citations.**
- Spivak, *Poly: An Abundant Categorical Setting* (arXiv:2005.01894) — monomials & lenses in the same framing.
- Spivak, *Reference: Categorical Structures on Poly* (arXiv:2202.00534) — reference-style catalogue.
- [Hed18a] = J. Hedges, the bimorphic-lens category cited by Niu–Spivak for the equivalence.

**Bottom line for the name/status:** there is no distinguished proper name for the monomial full subcategory
in the Poly literature; Niu–Spivak state it is the full subcategory of monomials, **equivalent to the category
of (bimorphic) lenses**. It is closed under ⊗ (parallel product) and × (product), but NOT under + or free monads.
