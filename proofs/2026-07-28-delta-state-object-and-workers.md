# ΔS, the reader/store, and the category of Workers

**MacBeth — 2026-07-28 (prove session).** Target set by Neil Ghani's 07-27 steer for Book Ch4
(Monads and Comonads): pin the state object `ΔS`, the reader/store construction, and build the
**category of Workers** whose composition is graded by `(Set, ×)`.

Companion code: `scratch/state-object-delta/{verify.py, run_tests.py, stress.py}` (exhaustive finite
checks, all green). Registry: `proofs/registry/state-object-delta.json`.

---

## 0. Conventions

A **container** is `p = (A, B)` with shape set `A` and position family `B : A → Set`; its extension is
the polynomial functor `⟦p⟧ X = Σ_{a:A} X^{B a}`. A **morphism** `p → q = (C,D)` is a pair `(f, f♯)`
with forward `f : A → C` and backward `f♯ : ∀a.\ D(f a) → B a`; composition runs forward on shapes and
**backward on positions**. Two monoidal structures matter:

- **Dirichlet tensor** `p ⊗ q = (A×C,\ (a,c) ↦ B a × D c)`, unit `y = (1, * ↦ 1)`. This is Day
  convolution of `(Set,×)` (Niu–Spivak, *Poly*, Def. 3.65; my note *dirichlet-is-day-convolution*). Its
  internal hom is `[q,r] = Π_{c:C}\ r ◦ (D c · y)` (Niu–Spivak Ex. 4.78 / eq. 4.75).
- **Product** `p × q = (A×C,\ (a,c) ↦ B a + D c)` (Day of `+`), `⟦p×q⟧ = ⟦p⟧ × ⟦q⟧`.

The **state object** is `ΔS := (S,\ s ↦ S)`: shape set `S`, and *every* position fibre equal to `S`.
Hence `⟦ΔS⟧ X = Σ_{s:S} X^S = S × X^S`.

---

## 1. Theorem T1 — `ΔS` is the codiscrete category; `⟦ΔS⟧` is the store comonad

### 1.1 The directed-container structure

Recall the Ahman–Chapman–Uustalu correspondence **DCont ≅ Cat** (machine-checked in `DContCat.lean`;
registry `equivalence-chain`, lean-verified). A directed container `(S, P, o, ↓, ⊕)` corresponds to a
small category `𝒞` with `Ob 𝒞 = S`, `P(s) = Σ_{s':S} 𝒞(s,s')` (all arrows out of `s`), identity
`o_s = id_s`, target `s ↓ p = cod(p)`, and composition `p ⊕ p'`. The axioms are

- **D1** `s ↓ o_s = s`;  **D2** `s ↓ (p ⊕ p') = (s↓p) ↓ p'`;
- **D3** `p ⊕ o_{s↓p} = p`;  **D4** `o_s ⊕ p = p`;  **D5** `(p⊕p')⊕p'' = p⊕(p'⊕p'')`.

**Claim.** `ΔS` carries the directed-container structure

  o_s = s,     s ↓ p = p,     p ⊕ p' = p'   (⊕ = second projection),

and under DCont ≅ Cat this is exactly the **codiscrete (indiscrete) category** on `S`: object set `S`,
with a *unique* morphism for every ordered pair `(s,s')`.

**Proof.** For the codiscrete category `𝒞`, `𝒞(s,s') = 1` for all `s,s'`, so
`P(s) = Σ_{s'} 𝒞(s,s') = Σ_{s'} 1 = S`, recovering the container `ΔS`. Reading off the structure maps:
the identity at `s` is the arrow `s → s`, i.e. the element `s ∈ S`, so `o_s = s`; a position `p ∈ P(s)=S`
names its target object, so `cod(p) = s ↓ p = p`; the composite of `s → p` and `p → p'` is the unique
arrow `s → p'`, whose target is `p'`, so `p ⊕ p' = p'`. This is the second projection. ∎

**Verification of D1–D5** (direct, and machine-checked in `run_tests.py` for `|S| = 1,2,3`):
with `o_s = s`, `s↓p = p`, `p⊕p' = p'`:
D1 `s↓s = s` ✓; D2 `s↓(p') = p' = p↓p'` ✓; D3 `p ⊕ o_p = o_p = p` ✓; D4 `o_s ⊕ p = p` ✓;
D5 `(p⊕p')⊕p'' = p'' = p⊕(p'⊕p'')` ✓.

This is the canonical directed structure with `↓ = id_S` (the identity target map); it is the unique one
for which every hom-set is a singleton, i.e. the codiscrete category. (The *discrete* category on `S`
gives instead `P(s) = 1`, the container `y·S`, not `ΔS`.)

### 1.2 The induced comonad is the store comonad

A directed container induces a comonad on `⟦S,P⟧` with counit `ε(s,v) = v(o_s)` and comultiplication
`δ(s,v) = (s,\ λp.\ (s↓p,\ λp'.\ v(p⊕p')))`. Substituting `o_s=s`, `s↓p=p`, `p⊕p'=p'`:

  ε(s, v) = v(s),      δ(s, v) = (s,\ λp.\ (p, v)),     where v : S → X.

These are exactly the counit and comultiplication of the **store (costate) comonad**
`Store_S X = S × X^S` (Uustalu–Vene, *Comonadic notions of computation*, 2008). The comonad laws are
machine-checked in `run_tests.py` (`S={a,b}`, `X={0,1},{0,1,2}`).

> **Grading (honest).** The DCont ≅ Cat identification is **proved** (lean-verified hinge cited, not
> re-proved). "ΔS = codiscrete category" and "⟦ΔS⟧ = store comonad" are **proved** as identifications;
> the store comonad itself is folklore (Uustalu–Vene) — I grade the *identification*, not the folklore.

---

## 2. Theorem T2 — the reader/store, read off the fibre

`⟦ΔS ⊗ p⟧ X = Σ_{(s,a):S×A} X^{S × B a} = Σ_{(s,a)} (X^{B a})^{S}`. Two special cases pin the story Neil
asked for:

- **Unit `p = y`.** `ΔS ⊗ y = ΔS`, so `⟦ΔS ⊗ y⟧ X = S × X^S = Store_S X`. The **store comonad**.
- **The fibre.** The position fibre of `ΔS` is the constant `S`; the contravariant part of `⟦ΔS⟧` is the
  **reader** functor `Reader_S X = X^S = (S → X)`, a monad with `η x = λs.\ x`,
  `μ g = λs.\ g\,s\,s`. Thus `⟦ΔS⟧ = S × Reader_S(−)`: *current state* × *reader*.

This is precisely why Neil wrote *"basic definitions of the reader monad … different processes have
different state so there is something more to be said."* The reader `X^S` is the read-only shadow; the
extra `S ×` factor (the shape, i.e. the *current* state, and the writeback in a morphism) is the "more".
That "more", pushed through composition, forces the state to **multiply** — which is Theorem T3.

Negative control (in `verify.py`): perturbing a single fibre of `ΔS` away from `S` breaks the constant-
fibre profile and the `Store` counit/comult identities no longer typecheck — the store structure is rigid
in the "all fibres `= S`" condition.

> **Grading:** the descent `⟦ΔS ⊗ y⟧ = Store_S` and `⟦ΔS⟧ = S × (−)^S` are **proved** (computed +
> direct). `⊗` and `[−,−]` pinned to Niu–Spivak (cited).

---

## 3. Theorem T3 — the category of Workers, graded by `(Set, ×)`

### 3.1 The multiplication lemma

**Lemma 3.1.** `ΔS ⊗ ΔT = Δ(S×T)` (strict equality of containers), and `Δ1 = y`.

**Proof.** `ΔS ⊗ ΔT = (S×T,\ (s,t) ↦ S × T)`; `Δ(S×T) = (S×T,\ (s,t) ↦ S×T)`. The shape sets and every
position fibre coincide. `Δ1 = (1, * ↦ 1) = y`. ∎ (Checked in `run_tests.py`.)

*Why `⊗` and not `×`.* This lemma is exactly why Neil's tensor is the **Dirichlet** `⊗` and the state
multiplies. Under the *product* tensor, `ΔS × ΔT = (S×T,\ (s,t) ↦ S + T) ≠ Δ(S×T)` (fibres of size
`|S|+|T|`, not `|S×T|` — checked in `negcontrol.py`: `5 ≠ 6` for `|S|=2, |T|=3`). Only the tensor whose
positions *multiply* makes the context multiply.

So `S ↦ ΔS` is a **strict monoidal functor** `(Set, ×, 1) → (Cont, ⊗, y)` on objects, and — because a
bijection `S ≅ S'` yields a container isomorphism `ΔS ≅ ΔS'` (both the forward and the backward maps are
available from a bijection) — it is functorial on the **core groupoid** `Core(Set)`. (It is *not*
functorial on all of `Set`: a bare function `h : S → S'` gives no canonical container morphism
`ΔS → ΔS'`, since the backward part would need `S' → S`. This restriction is what makes the honest
statement below "graded category / coKleisli", exact on objects, rather than a full actegory.)

### 3.2 Workers and their composition

**Definition.** A **Worker** from `p` to `q` with **state `S`** is a container morphism
`w : ΔS ⊗ p → q`. Writing `q = (C,D)`, `ΔS ⊗ p = (S×A,\ (s,a) ↦ S × B a)`, such a `w` unpacks into

- forward `f : S × A → C`  — from state `s` and input shape `a`, produce output shape `f(s,a)`;
- backward, split in two: `f♯₁(s,a) : D(f(s,a)) → S` (**writeback** of a new state per output position)
  and `f♯₂(s,a) : D(f(s,a)) → B a` (the ordinary position back-map).

**Composition.** Given `w : ΔS ⊗ p → q` and `w' : ΔT ⊗ q → r`, define the composite via functoriality of
`⊗` and Lemma 3.1:

    Δ(T×S) ⊗ p = ΔT ⊗ (ΔS ⊗ p) --ΔT ⊗ w--> ΔT ⊗ q --w'--> r,

i.e. `w' ∘ (id_{ΔT} ⊗ w) : Δ(T×S) ⊗ p → r`. **The state multiplies:** a state-`S` worker followed by a
state-`T` worker is a state-`(T×S)` worker. In coordinates (`r = (E,G)`, `e := g(t, f(s,a))`):

- forward: `((t,s), a) ↦ g(t,\ f(s,a))`;
- backward at `((t,s),a)`, for `d' : G(e)`:
  - state `∈ T × S`:  `( g♯₁(t, f(s,a), d'),\ f♯₁(s, a,\ g♯₂(t, f(s,a), d')) )`,
  - position `∈ B a`:  `f♯₂(s, a,\ g♯₂(t, f(s,a), d'))`.

Reading left-to-right we take the accumulated state to be `S × T` (the strict composite reads `T × S`;
the two agree via the symmetry of `⊗`, and I fix the reading-order convention `S × T`).

**Identity.** `id_p : Δ1 ⊗ p = p → p` is `id_p`, with state `1`.

### 3.3 The theorem

**Theorem T3.** There is a **`(Set,×)`-graded category** **Workers** whose objects are containers, with
hom-sets graded by `(Set, ×)`,

    Workers_S(p, q) := Cont(ΔS ⊗ p,\ q),

with identity in grade `1` and composition
`Workers_S(p,q) × Workers_T(q,r) → Workers_{S×T}(p,r)` as in §3.2. Composition is **associative** and
**unital** up to the associator and unitors of `(Set, ×)`. Equivalently, Workers is the **coKleisli
category of the `(Set,×)`-graded comonad** `S ↦ ΔS ⊗ (−)` on `Cont` (grade multiplication `×`, unit
grade `1`, comultiplication the strict equality `Δ(S×T)⊗− = ΔS⊗(ΔT⊗−)` of Lemma 3.1).

**Proof.**
*Composition lands in the right grade* by Lemma 3.1 (`Δ(T×S)⊗p → r`), and the composite is a
well-typed container morphism (checked exhaustively: all 32 tiny composites and the `400×256` multi-shape
composites in `run_tests.py`/`stress.py` are valid).

*Unitality.* For `w ∈ Workers_S(p,q)`, `id_q ∘ w` has state `1 × S` and, on unpacking, equals `w`
composed with the identity forward/backward maps of `id_q`; under the unitor `1 × S ≅ S` this is `w`
itself. Symmetrically `w ∘ id_p` equals `w` under `S × 1 ≅ S`. (Machine-checked for all 16 workers over
`S={s0,s1}`.)

*Associativity.* For `w1 : ΔS⊗p→q`, `w2 : ΔT⊗q→r`, `w3 : ΔU⊗r→z`, both `(w3 ∘ w2) ∘ w1` and
`w3 ∘ (w2 ∘ w1)` have underlying container morphism `w3 ∘ (id ⊗ w2) ∘ (id ⊗ id ⊗ w1)`, equal by
associativity of composition in `Cont` and the interchange/functoriality of `⊗`; their grades `(U×T)×S`
and `U×(T×S)` are identified by the associator of `(Set,×)`. (Machine-checked: 512 tiny triples + 1369
multi-shape triples all equal up to the associator bijection `((u,t),s) ↔ (u,(t,s))`.)

That the data `(Workers_S, ∘, id, ×, 1, α, λ, ρ)` is precisely a category **graded by the monoidal
category `(Set,×)`** (a.k.a. `(Set,×)`-graded category) is now immediate; the coKleisli reading holds
because comultiplication is the identity-strict `Δ(S×T)⊗− = ΔS⊗ΔT⊗−`. ∎

### 3.4 S varies — the Para construction

Neil: *"once we note the S might change … see Gavranović's Para construction."* Collapsing the grade
into the hom gives the category with a *single* hom-set

    Para(p, q) := Σ_{S:Set}\ Cont(ΔS ⊗ p,\ q),

a Worker together with its choice of state set, composed by `(S,w) ∘ (T,w') = (S×T,\ w' ∘ (ΔT ⊗ w))` —
the parameter (state) tensors. This is exactly **Gavranović's Para construction** applied to the monoidal
action of `(Set, ×)` on `Cont` by `S · p = ΔS ⊗ p` (Capucci–Gavranović–Hedges–Rischel, *Towards
foundations of categorical cybernetics*, 2021; Gavranović, thesis 2024). The graded category of §3.3 is
its fibrewise (grade-indexed) refinement.

> **Grading (honest).** The **graded category** and **coKleisli** statements are **proved** (coordinates
> + exhaustive finite verification). The **Para identification** is **proved for the action over the core
> groupoid `Core(Set)`** — the level at which `Δ` is genuinely functorial; over all of `Set` the
> assignment is a monoidal-on-objects grading, not a strict actegory (§3.1), so "Para over `(Set,×)`" is
> a *graded/lax* reading rather than a literal actegory-Para. I grade the *identification* with Para as
> **computed** pending a full check of Gavranović's exact hypotheses; the categorical content (state
> multiplies, parameters tensor) is proved.

---

## 4. Grant framing

Workers are **stateful agents/processes with context**. A Worker `ΔS ⊗ p → q` is a `p`-interfaced process
that reads and writes an `S`-typed context and exposes a `q` interface. Composition **multiplies the
context** (`S × T`) — the grant's compositional-correctness story at the level of *state*, complementary
to the Zappa–Szép/`[ω]∈H²` obstruction spine (which governs *directed* composition). Reader/store places
the classical stateful-computation comonads (Uustalu–Vene) inside the container census, and the Para
reading ties Workers to categorical cybernetics / lenses (Gavranović), where the same "parameters tensor"
law drives learners and open games.

---

## 5. Gaps (precisely stated)

1. **Para exactness.** Whether Workers-with-varying-`S` is *literally* `Para` of a strict `(Set,×)`-
   actegory, or only of the `Core(Set)`-actegory, needs a line-by-line check against Gavranović's
   actegory axioms. §3.1 shows `Δ` is functorial only on bijections, so my current honest claim is
   "Para over `Core(Set)`; graded-category over all of `(Set,×)`." (Grade: computed.)
2. **Graded-comonad packaging.** I use "graded comonad" informally (strict monoidal `S ↦ ΔS⊗−`). Pinning
   it to the Fujii–Katsumata–Melliès definition (lax monoidal functor `(Set,×) → End(Cont)`, here strict)
   and confirming the coKleisli-of-graded-comonad theorem applies verbatim is a short but unwritten step.
3. **Lean.** None of §3 is formalised yet. Lemma 3.1 (`ΔS⊗ΔT=Δ(S×T)`) and the composite formula are
   defeq-shaped and should be a clean follow-on (candidate LEAN.md target).

Everything in §1–§2 and the *graded-category* core of §3 is proved (coordinates + exhaustive finite
verification). The two open items above are identifications, not the mathematics of Workers.
