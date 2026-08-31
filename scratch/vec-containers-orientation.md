# Containers over Vec — orientation note (2026-08-18)

Neil's steer (email 2026-08-15): monads/comonads are "done enough"; new front =
**containers over other base categories**, specifically **Fam(Vec^op)**, so the *answer space is a
vector space*. Start thinking about the categorical structure of **Vec** and **how much of basic
container theory carries over** under the base change `Set → Vec`.

This note is my first read, to seed the PROVE/WRITE triggers. Compute-first + expository-first: there
is a large adjacent literature (see §Neighbours) and I must NOT reinvent it.

## 0. The dictionary (what a "linear container" should be)

- **Set container:** `(S, P)`, `P : S → Set`; `Cont ≅ Fam(Set^op)` (free coproduct completion of
  `Set^op`). Extension `⟦S,P⟧ X = Σ_{s∈S} Set(P_s, X) = Σ_s X^{P_s}` — a functor `Set → Set`.
- **Vec container (proposal):** an object of `Fam(Vec^op)` = a set `S` of shapes + a family
  `(P_s)_{s∈S}` of `k`-vector spaces (positions are now *vector spaces*, morphisms contravariant/linear).
- **Extension into Vec** (Neil's "answer space is a vector space"):
  `⟦S,P⟧ W := ⊕_{s∈S} Vec(P_s, W)`, a functor `Vec → Vec`.
  Each `Vec(P_s, W)` is a `k`-vector space; `⊕` (direct sum) is the coproduct in `Vec`, valid for any
  index set `S`. If `dim P_s = n_s` then `Vec(P_s, W) ≅ W^{⊕ n_s}`, so
  **`⟦S,P⟧ W ≅ ⊕_{s∈S} W^{⊕ n_s}`** = a coproduct of "additive representables" `(−)^{n_s}`.

So a linear container = a set of shapes, each carrying an **arity** `n_s = dim P_s` (a cardinal). The
extension is an **additive polynomial functor** — a direct sum of powers.

## 1. THE ASTONISHMENT — the biproduct collapse

Over `Set`, `Σ` (coproduct) ≠ `Π` (product), so `Σ_s X^{P_s}` **keeps the shapes separate**: shapes are
recovered as `F(1) = S` at the terminal object. Over `Vec` this **breaks in two ways**:

1. **Terminal recovery fails.** `Vec`'s terminal object is the **zero object** `0` (terminal = initial).
   `⟦S,P⟧(0) = ⊕_s Vec(P_s, 0) = ⊕_s 0 = 0`. **You cannot read off `S` at the terminal object.** The
   Set slogan `F(1)=S` has no analog. (Candidate replacement: evaluate at the unit `k`:
   `F(k) = ⊕_s Vec(P_s,k) = ⊕_s P_s^*`, `dim F(k) = Σ_s n_s` — recovers only the *total* arity.)

2. **Finite biproduct collapse.** For finite `S` and finite arities, `⊕` = `Π` = **biproduct**, so
   `⟦S,P⟧ W = ⊕_s W^{n_s} = W^{N}`, `N = Σ_s n_s`. **The shape partition is invisible** — a finite
   linear container is determined by the single number `N`. The whole shape/position bookkeeping that
   makes Set-containers rich *collapses* to total dimension.

   → Shapes only reappear as extra structure: **`S` = the set of indecomposable direct summands** of the
   functor `F = ⊕_s F_s`. "Shape" over `Vec` = "indecomposable summand," not "point of `F(1)`."

This is the headline: **base-change Set→Vec trades the coproduct/product distinction for a biproduct,
and the container's shape data goes from *free* (readable at the terminal) to *hidden* (a direct-sum
decomposition).** Where does content survive? Infinite `S` / infinite-dim positions (`⊕ ≠ Π`), and the
**morphism** layer (container morphisms, comonoids), which the collapse does not trivialize.

## 2. What to check, carry-over by carry-over

| Set fact | Vec analog — conjecture | risk |
|---|---|---|
| `Cont ≅ Fam(Set^op)` | `LinCont := Fam(Vec^op)`, ext into `Vec` via `⊕ Vec(P_s,−)` | low (definitional) |
| Rep. thm: `F` container ⟺ preserves wide pullbacks / connected limits | `F: Vec→Vec` linear container ⟺ preserves connected limits AND is a coproduct of corepresentables `Vec(P,−)`; additive ⟹ care needed (biproduct) | **med — this is strict-poly-functor territory, verify novelty** |
| `F(1)=S` recovers shapes | **FAILS** (`F(0)=0`); shapes = indecomposable summands | resolved above |
| Directed containers / poly comonoids ≅ small categories | **linear directed containers ≅ `k`-linear categories (algebroids)**; one object ⟹ a `k`-algebra | **high value, med risk — the crown analog** |
| Day family: convolutional tensors on `Cont` ≃ monoidal structures on `Set` (my Thm A) | convolutional tensors on `Fam(Vec^op)` ≃ monoidal structures on `Vec` (`⊗_k`, `⊕`) | med — direct extension of my classification |
| ZS product / distributive laws for composing dir. containers | ZS for `k`-linear categories = ? matched pairs of algebroids | later |

The **crown target** is the comonoid row: *does `poly comonoid over Vec = k-linear category`?* If yes,
the equivalence-chain spine `Containers ≃ Dir.Cont ≃ Poly-comonoids ≃ Cat` base-changes to
`LinCont ≃ Lin.Dir.Cont ≃ ? ≃ k-Lin-Cat (algebroids)` — a representation-theory bridge for the grant.

## 3. Neighbours — READ BEFORE CLAIMING (novelty floor)

- **Strict polynomial functors (Friedlander–Suslin 1997, Touzé, Krause).** Functors `Vec→Vec` built
  from `⊗`, `Sym`, `Λ`, direct sums — *exactly* "polynomial functors over a field." My "additive
  polynomial functor `⊕_s W^{n_s}`" is the **degree-≤1 / additive** corner of this. The full theory
  (homogeneous strict poly functors of degree `d`, the category `P_d`) is highly developed. **The
  container/`Fam(Vec^op)` framing and the what-carries-over table are my delta, NOT the objects.**
- **Linear species / vector species / twisted commutative algebras** (Joyal linearised; Sam–Snowden).
  Species valued in `Vec`. Overlaps the "shapes with linear positions" picture.
- **Additive/accessible functor representation theory** (Freyd, Adámek–Rosický): which functors are
  small coproducts of representables — the abstract home of the representation theorem.
- **Enriched containers / polynomial functors in a category** (Gambino–Kock "Polynomial functors and
  polynomial monads"; Weber; Spivak `Poly` is over `Set`). Check whether `Poly(Vec)` / polynomial
  functors valued in an extensive/abelian base is already treated.
- **Algebroids / `k`-linear categories** (Mitchell's theorem: a ring = one-object `Ab`-category). The
  target of the comonoid row.

## 4. Two honest structural cautions

- `Vec` is **additive/abelian**: biproducts, zero object, every mono/epi splits partially, `Hom` is a
  vector space. Extensivity (which underpins the Set container rep. theorem via disjoint coproducts)
  **fails** — coproducts in `Vec` are not disjoint (they're biproducts). So the *proof* of the
  representation theorem cannot be copied; the connected-limit characterization may or may not survive.
- Two monoidal structures compete on `Vec`: `⊗_k` (closed, unit `k`) and `⊕` (biproduct, unit `0`).
  "Which is the `◁`-analog?" is a real question — the substitution/composition tensor `◁` on
  `Fam(Vec^op)` needs to be pinned (composition of linear containers = ?).

## 5. Seeded triggers (for the wake session to write)

- **PROVE** = §0–§1 made rigorous: define `LinCont = Fam(Vec^op)` + extension `Vec→Vec`; prove the
  **biproduct-collapse theorem** (finite linear containers ≅ `W↦W^N`, shapes = indecomposable summands,
  terminal-recovery fails) and state/attempt the **representation theorem** (which `F:Vec→Vec` are
  linear containers). Compute-first in small dims; **expository/neighbour pass FIRST** (strict poly
  functors) so the novelty claim is honest — the *framing* is the deliverable, not the objects.
- **WRITE / expository** = the landscape §0–§4 as a clean note "Containers over Vec": the dictionary,
  the biproduct-collapse astonishment, the carry-over table, the neighbours. Understanding-building for
  the grant's new front (uses `/expository`).
- **LEAN** = hold this cycle (nothing proved yet on the new front).

## 6. Open (fold into Neil download / open-threads)
- Is `Fam(Vec^op)`'s extension better taken into `Set` (`Σ Vec(P_s,−)`) or `Vec` (`⊕ Vec(P_s,−)`)?
  Neil says vector-space answers ⟹ `Vec`. Keep the `Set`-valued version as a shadow.
- Rick's live challenge (non-abelian `[ω]`: construct the 2-cocycle, test descent to coset-valued;
  `|A\U/B| =? dim Ext¹`) — a monads/comonads-line open thread, NOT the new front. Reply + log as open.
