# Effect–coeffect arrows on `Cont`: the compositor is the *reverse* entwining, and it exists iff `M` does not branch

**MacBeth — PROVE session, 2026-07-29.** Target: Neil Ghani's 07‑29 steer. Turn the proved
entwining `λ : T_M G_M ⇒ G_M T_M` (07‑27) into the coherence theorem for a category of
**effect–coeffect container arrows** `G_M p → T_M q`, and name the structure (Freyd / arrow /
bialgebra / Plotkin–Turi).

---

## Answer in one line

The effect–coeffect arrows `G_M p → T_M q` **do** form a category — the **biKleisli category**
(coKleisli‑of‑Kleisli) of the two feeds of one Set‑monad `M` — but its compositor is **not** the
proved entwining `λ : T_M G_M ⇒ G_M T_M`. Composition needs the **opposite** mixed distributive law
`κ : G_M T_M ⇒ T_M G_M`, the map that commutes `T` *out of* `G`. By the 07‑27 dichotomy this `κ`
exists (satisfying its four axioms) **iff `M` is non‑branching (arity ≤ 1)**. Hence:

> **The category of effect–coeffect arrows on `Cont` exists ⟺ `M` is non‑branching**
> (`Maybe`, exception `E+(−)`, `Writer`, `Id`). For branching `M` (`Pf`, `List`) there is **no such
> category**: composition is *non‑associative*, with an explicit counterexample.

What survives for **all** `M` is the *other* direction `λ`: it is not a compositor but a
**bialgebra / entwining** (Plotkin–Turi). So Neil's "genuine unification of effects and coeffects for
containers" splits into two faces, dual to each other, coinciding only for arity ≤ 1:

| structure | law | which `M` | what it is |
|---|---|---|---|
| **arrow / Freyd category** of `G_M p→T_M q` | `κ:G_MT_M⇒T_MG_M` (lax) | **non‑branching only** | biKleisli of a monad+comonad |
| **bialgebra / entwining** (`G_M`↑`T_M`‑alg, `T_M`↑`G_M`‑coalg) | `λ:T_MG_M⇒G_MT_M` (oplax `str`) | **all `M`** | Plotkin–Turi distributive law |

This corrects the orientation guessed in `PROVE.md` (which identified the compositor with `λ`): the
act of *"commuting a `T_M` past a `G_M`"* in a composite produces the arrow `G_M T_M ⇒ T_M G_M`, i.e.
`κ` — the branching‑obstructed one — not `λ`.

---

## 0. Setup

Containers, morphisms `(u,f):(S,P)→(T,Q)` (forward `u:S→T`, **backward** `f_s:Q(us)→Ps`; positions
contravariant; backward maps compose in the opposite order), extension `⟦S,P⟧Y=Σ_s Y^{Ps}`, all as
in `2026-07-25-monad-comonad-transfer.md` and `2026-07-27-monad-comonad-entwining.md`. Fix a Set‑monad
`M` with a support/leaf structure carrying the **`∏`‑cointerpretation** weak Mendler algebra
(Ahman–Bauer, arXiv:2409.17664, §6). The two liftings of `M`:

* **`G_M(S,P)=(S,M∘P)`** — the transfer **comonad** (`2026-07-25`, proved + Lean). Counit `ε` backward
  `η_{Ps}`, comultiplication `δ` backward `μ_{Ps}`; identity on shapes.
* **`T_M(S,P)=(MS,P^\star)`** — the Ahman–Bauer **monad** (Thm 6.3), `P^\star(m)=∏_{b∈lv(m)}P(x_b)`.
  Unit `η^T` covers `η^M` (backward the singleton projection `i`), multiplication `μ^T` covers `μ^M`
  (backward the Mendler restriction `j`).

The proved (07‑27) **entwining** is the identity‑on‑shapes 2‑cell
`λ_X : T_M G_M X → G_M T_M X` whose backward map at `m∈MS` (leaves `b`, `Z_b:=P(x_b)`) is the **oplax**
product comparison
`str : M(∏_b Z_b) → ∏_b M(Z_b), w ↦ (M(π_b)w)_b`.
It satisfies the four entwining axioms E1–E4 for **every** such `M`; and `G_M` lifts to a comonad on
`T_M`‑algebras, `T_M` to a monad on `G_M`‑coalgebras.

**Effect–coeffect arrow.** For containers `p,q` an **arrow** `p ⇝ q` is a `Cont`‑morphism
`f : G_M p → T_M q`. (Coeffect comonad on the source; effect monad on the target — the container
analogue of a "coKleisli‑of‑`G` then Kleisli‑of‑`T`" arrow `GA→TB`, Neil's exact object.)

---

## 1. The biKleisli category and its compositor

Write `T=T_M` (monad `η^T,μ^T`), `G=G_M` (comonad `ε,δ`). The arrows `Gp→Tq` are exactly the
morphisms of the **coKleisli category of the comonad `G` lifted to the Kleisli category `Kl(T)`**
(the "biKleisli" or "two‑sided Kleisli" category; Uustalu–Vene, *Comonadic notions of computation*,
2008; Brookes–Geva; Power–Watanabe, *Combining a monad and a comonad*, TCS 280 (2002)). Explicitly:

* **Identity** `p⇝p`:  `Gp --ε_p--> p --η^T_p--> Tp`, i.e. `η^T_p ∘ ε_p`.
* **Composition** of `f:Gp→Tq` and `g:Gq→Tr`:
  $$
  Gp \xrightarrow{\ \delta_p\ } GGp \xrightarrow{\ Gf\ } GTq
      \xrightarrow{\ \kappa_q\ } TGq \xrightarrow{\ Tg\ } TTr
      \xrightarrow{\ \mu^T_r\ } Tr .
  $$

The middle step **`κ_q : G T q → T G q`** is a natural transformation `κ : GT ⇒ TG`. This is the
**crux**: composition commutes the effect `T` *out through* the coeffect `G` (from `GTq` to `TGq`),
which is the arrow `GT ⇒ TG` — **the reverse of the proved `λ : TG ⇒ GT`.**

On positions `κ` runs backward `∏_b M(Z_b) → M(∏_b Z_b)`, the **lax** product comparison
(union/cartesian‑product for `Pf`; `η`‑padding for `Maybe`). This is precisely the "reverse
orientation" studied and obstructed in 07‑27 §4.

### 1.1 Why `κ`, not `λ` (correcting `PROVE.md`)

`PROVE.md` T2 wrote *"to compose them you must commute a `T_M` past a `G_M` — exactly the mixed
distributive law `λ:T_MG_M⇒G_MT_M`."* The identification of the **direction** is off by the swap.
In the composite the object one must transform is `G(Tq)`, and it must become `T(Gq)`; as a natural
transformation between functors that is `GT ⇒ TG = G_M T_M ⇒ T_M G_M`, i.e. **`κ`**, whose backward
map is the **lax** `∏M→M∏`. The proved `λ` has backward the **oplax** `M∏→∏M` and is the 2‑cell
`T_M G_M ⇒ G_M T_M` — it does *not* fit the composite. The two laws are genuinely different (dual)
data; §3 shows the difference is decisive.

---

## 2. The structural theorem

**Theorem A (existence ⟺ non‑branching).** Let `M` be a `∏`‑cointerpretation Set‑monad. The following
are equivalent.

1. The effect–coeffect arrows `Gp→Tq` form a category with identity `η^T∘ε` and the biKleisli
   composition of §1.
2. The comonad `G=G_M` lifts to a comonad `G̃` on the Kleisli category `Kl(T_M)`.
3. There is a natural `κ : G_MT_M ⇒ T_MG_M` satisfying the four mixed‑distributive‑law axioms
   (the two comonad axioms for `G`, the two monad axioms for `T`) — abbreviate E1′–E4′.
4. `M` is **non‑branching**: every `m∈MS` has support `|lv(m)|≤1` (equivalently, `M`'s multiplication
   never merges two distinct leaves).

*Proof.*

**(1)⇔(2)⇔(3).** Standard (Power–Watanabe TCS 280 (2002), §3; the mixed analogue of Beck's
monad–monad theorem). A lifting of a comonad `G` to `Kl(T)` is the same datum as a distributive law
`κ:GT⇒TG` obeying E1′–E4′, and the coKleisli category of the lifted comonad `G̃` is exactly the
category in (1), with hom‑set `Kl(T)(G̃p,q)=Kl(T)(Gp,q)=Cont(Gp,Tq)`, identity `η^T∘ε`, and the §1
composite. Concretely the two category laws unwind as:

* **Unit laws** ⟺ E1′ (`κ∘Gη^T=η^TG`) and E3′ (`Tε∘κ=εT`), together with the comonad counit and
  monad unit laws of `G,T` (already true).
* **Associativity** ⟺ **E2′** (`κ∘Gμ^T = μ^TG∘Tκ∘κT`, "the mult‑`T` axiom") together with E4′ and
  naturality. E2′ is precisely the statement that `G̃` *preserves Kleisli composition*
  (`G̃(b•a)=G̃b•G̃a`); its failure makes `G̃` a non‑functor and the coKleisli composition
  non‑associative.

**(3)⇔(4).** This is the 07‑27 dichotomy (`2026-07-27-monad-comonad-entwining.md` §4, machine‑verified
`entwine.py`): the lax `κ` satisfies E1′, E3′, E4′ for every `M`, and satisfies **E2′ iff `M` is
non‑branching**. For branching `M` the failure is *union‑of‑products ≠ product‑of‑unions*: `μ^M`
merges an overlapping leaf and the cartesian lax map cannot enforce that the choices at the shared
leaf agree. Witness `M=Pf`, `X=({a,b},a↦\{0,1\},b↦\{0\})`, at `{{a,b},{a}}∈Pf\,Pf\,S`. ∎

**Corollary A′.** For non‑branching `M` (`Maybe`, exception `E+(−)`, `Writer_N`, `Id`) the arrows
`G_Mp→T_Mq` form a category; for branching `M` (`Pf`, `List`, non‑trivial free monads) they do **not**.

The equivalence (1)⇔(4) is what makes the result sharp: *the existence of an effect–coeffect arrow
calculus on containers is a property of the effect monad `M`, namely non‑branching, and the obstruction
is exactly the entwining axiom E2′ that branching destroys.*

### 2.1 Direct arrow‑level confirmation (not only the abstract law)

The abstract argument routes through E2′; I also verified the category axioms **directly on the arrows
themselves** (`scratch/monad-comonad-transfer/bikleisli.py`, building the §1 composite as an honest
`Cont`‑morphism):

* **`M=Maybe`**: over `p=r=({0},\{0\})`, `q=z=A1=({a,b},\{a:2,b:1\})`, **all** 1536 associativity
  triples pass, both identity laws hold on all 8 arrows `p⇝q`, all sampled composites well‑typed. A
  genuine category.
* **`M=Writer/ℤ₂`**: same objects, **all** 4608 associativity triples pass; identity laws hold. A
  second non‑branching positive control.
* **`M=Pf`**: identity laws and well‑typedness still hold (E1′,E3′,E4′ survive), but associativity
  **fails**. Explicit triple `f,g,h : G(A1)→T(A1)` (all forward `a↦\{a\}, b↦\{a,b\}`) with
  `(h∘g)∘f ≠ h∘(g∘f)`: the two associations differ at shape `b`, position `(1,0)`, giving `∅` versus
  `\{0\}`. **No category.**

The signature is telling: for `Pf` *only associativity breaks*, never the unit laws — matching E2′
being the sole failing axiom.

---

## 3. What the category *is* (non‑branching case)

For non‑branching `M`, the category of §1 is the **biKleisli category** `coKl_{Kl(T)}(G̃)` of a
monad‑and‑comonad with a distributive law — the canonical source of **Hughes arrows** (J. Hughes,
*Generalising monads to arrows*, SCP 37 (2000)) and equivalently of **Freyd categories**
(Power–Robinson, *Premonoidal categories and notions of computation*, MSCS 7 (1997); Atkey, *What is a
categorical model of arrows?*, ENTCS 229 (2011); Jacobs–Heunen–Hasuo, *Categorical semantics for
arrows*, JFP 19 (2009)). Precisely:

* There is an **identity‑on‑objects functor** `J : Cont → Arr_M` sending a container morphism
  `φ:p→q` to the arrow `Gp --ε--> p --φ--> q --η^T--> Tq` (pure processes: coeffect discarded by `ε`,
  effect freely introduced by `η^T`). `J` is faithful on the pure part and identity on objects — the
  defining shape of a Freyd/arrow structure.
* The **effect** sub‑calculus is the Kleisli category `Kl(T_M)` (arrows `p→Tq`, i.e. `G=Id` collapsed
  by counit): container programs with the Ahman–Bauer effect. The **coeffect** sub‑calculus is the
  coKleisli category `coKl(G_M)` (arrows `Gp→q`): container programs reading the transfer‑comonad
  context. The biKleisli category **fuses** them, and Theorem A says the fusion is coherent exactly
  when `M` does not branch.

**Promotion to a full `Arrow` / premonoidal structure** (the `first`/strength operator, i.e.
`Arr_M(p,q)→Arr_M(p⊗s, q⊗s)`) requires `T_M` to be a *strong* monad and `G_M` a *costrong* comonad for
a chosen monoidal structure on `Cont` (e.g. Dirichlet `⊗`, or `×`), compatibly with `κ`. That extra
(co)strength is the natural next increment and is **not** claimed here (Gap 3). The **category**
(Theorem A) is unconditional for non‑branching `M`; the *arrow/Freyd* identification is at the level of
"this is the biKleisli category, the standard arrow, pending the (co)strength check."

### 3.1 Workers are the `T=Id` slice (sanity anchor)

The Workers category (07‑28, `2026-07-28-delta-state-object-and-workers.md`) has arrows
`ΔS⊗p→q` — a coeffect‑only calculus with **no effect monad** (`T=Id`). It composes for *every* `S`
because with `T=Id` the compositor `κ:GT⇒TG` is the identity and E2′ is vacuous: there is no `T` to
commute past, hence no branching obstruction. Workers thus sit inside the present picture as the
`T=Id` corner (coKleisli of the graded comonad `ΔS⊗−`), consistent with Theorem A. The effect–coeffect
category adds a genuine effect `T_M` on the target, and *that* is where branching can bite.

---

## 4. Plotkin–Turi / bialgebra — the face that survives branching

Neil asked whether this is Plotkin–Turi bialgebraic semantics (lift the comonad to algebras, the monad
to coalgebras). **Yes — but for the `λ`‑direction, not the `κ`‑direction, and this is exactly the face
that branching preserves.**

The proved entwining `λ:T_MG_M⇒G_MT_M` (07‑27, all `M`) is a **mixed distributive law of Beck's EM
type**: it lifts `G_M` to a comonad on the **Eilenberg–Moore** category `Alg(T_M)` of effect‑algebras,
and lifts `T_M` to a monad on the EM category `Coalg(G_M)` of coeffect‑coalgebras. That is precisely a
**λ‑bialgebra** in the Turi–Plotkin sense (D. Turi, G. Plotkin, *Towards a mathematical operational
semantics*, LICS 1997): a `T_M`‑algebra‑and‑`G_M`‑coalgebra structure compatible along `λ`. Its
existence is **unconditional in `M`** (07‑27 proved E1–E4 for every `M`).

So the honest statement of Neil's "unification of effects and coeffects for containers" is a
**dichotomy of two dual structures**:

* **Operational / arrow face** (`κ:GT⇒TG`, biKleisli, Hughes/Freyd): the syntax of *composing*
  effect–coeffect programs `Gp→Tq`. Exists **iff `M` non‑branching**.
* **Denotational / bialgebra face** (`λ:TG⇒GT`, EM, Turi–Plotkin): the *semantics* where the comonad
  acts on algebras and the monad on coalgebras. Exists for **all `M`**.

For arity ≤ 1 they coincide (there `str=`lax up to the coherent unit padding, so `κ` and `λ` are two
readings of one iso), giving the clean case where operational and denotational agree. For branching
`M` the denotational bialgebra exists but there is **no operational arrow category** — the effect and
coeffect cannot be *sequentially composed*, only *paired* bialgebraically. This is the paper's sharpest
content: **branching is exactly the obstruction that separates the bialgebra from the arrow.**

---

## 5. Verification (computational)

`scratch/monad-comonad-transfer/{entwine.py, bikleisli.py}`:

* **`κ` axioms** (`entwine.py`, reverse `GT⇒TG`): E1′,E3′,E4′ **PASS** for `Maybe, Pf` on all
  containers; **E2′ PASS for `Maybe`, FAIL for `Pf`** on branching containers `A1,A3`, PASS on the
  single‑shape `A2` (no overlap). Failure element printed (correlated vs full product).
* **biKleisli category** (`bikleisli.py`, the §1 composite built as a real `Cont`‑morphism):
  * `Maybe`: 1536/1536 associativity triples pass, identity laws hold, composites well‑typed.
  * `Writer/ℤ₂`: 4608/4608 associativity triples pass, identity laws hold.
  * `Pf`: identity laws hold; **associativity fails**, explicit witness triple printed (differ at
    shape `b`, pos `(1,0)`: `∅` vs `\{0\}`).
* Forward entwining `λ:TG⇒GT` all four axioms **PASS** across `{Maybe,Pf,Writer/ℤ₂,Writer/T₂}` ×
  `{A1,A2,A3}` (12/12), re‑confirming the `λ`‑face for all `M` (§4).

---

## 6. Novelty / attribution

* **biKleisli / coKleisli‑of‑Kleisli of a monad+comonad distributive law**: folklore
  (Power–Watanabe TCS 280 (2002); Uustalu–Vene 2008; Brookes–Geva). **Arrow ⇔ Freyd category**:
  Hughes SCP 37 (2000); Power–Robinson MSCS 7 (1997); Atkey ENTCS 229 (2011); Jacobs–Heunen–Hasuo
  JFP 19 (2009). **λ‑bialgebra / operational semantics**: Turi–Plotkin LICS 1997. All cited, not
  claimed.
* **`T_M`** = Ahman–Bauer arXiv:2409.17664 Thm 6.3 (prior art). **`G_M`, `λ`** = the transfer + the
  07‑27 entwining (mine, proved).
* **Neighbour, different engine**: Katsumata–Rivas–Uustalu, *Interaction Laws of Monads and Comonads*
  (arXiv:1912.13477) answer effect/coeffect interaction via **Chu spaces / Day convolution** (monad–
  comonad interaction laws as monoids in `Chu`, greatest interacting comonad = Sweedler dual) — a
  *pairing* `TX⊗DY→…`, **not** the biKleisli composition of arrows `Gp→Tq`. Distinct structure; cite
  as the alternative unification.
* **Contribution (MacBeth):** (i) assembling the effect–coeffect **arrow category** for the two
  container feeds of one `M`; (ii) the identification that its compositor is `κ:GT⇒TG` (lax), the
  **reverse** of the proved entwining `λ` — correcting the guessed orientation; (iii) **Theorem A**:
  the category exists **iff `M` is non‑branching**, with E2′ as the exact obstruction and an explicit
  `Pf` non‑associativity witness; (iv) the **dichotomy** — arrow face (`κ`, non‑branching) vs
  bialgebra/Turi–Plotkin face (`λ`, all `M`) — as the honest form of "unifying effects and coeffects
  for containers." This is the container‑specific content Neil flagged as paper‑worthy; the general
  machinery is folklore, deployed here where the base monad `M` sits on positions and *branching* is
  the decisive parameter.

---

## 7. Gaps (precisely stated)

1. **E2′ general index‑chase.** As in 07‑27: the E2′ failure is proven conceptually (str/lax vs the
   product‑reindexing `j`) and machine‑verified for `∏`‑Mendler examples incl. branching `Pf`; the
   fully symbolic chase over an arbitrary weak Mendler `j` is not spelt out. Conceptual content
   complete; mechanical only.
2. **"Only associativity fails."** Verified computationally that for `Pf` the unit laws hold and only
   associativity breaks; a from‑scratch proof that E1′,E3′,E4′ always hold (so the failure is *always*
   confined to E2′/associativity) follows from 07‑27 but is not re‑derived here at the arrow level.
3. **Arrow/premonoidal (co)strength.** The identification as a full **Arrow**/Freyd category (the
   `first` operator) needs `T_M` strong and `G_M` costrong for a monoidal structure on `Cont`
   (`⊗` or `×`), compatibly with `κ`. Not checked; the *category* (Theorem A) does not depend on it.
   Natural next PROVE/LEAN target.
4. **Scope = `∏`‑cointerpretation.** As in 07‑27, both `λ` and `κ` use the product structure of
   `P^\star`; a non‑`∏` weak Mendler algebra is out of scope.
5. **`Cont(Set^→)→Set` logic angle.** Neil's predicate‑lifting/fibration question (bialgebra as
   logic over the container fibration) is not addressed; flagged for a later session.
