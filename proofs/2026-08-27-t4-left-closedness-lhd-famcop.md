# T4-left — Left-closedness of the substitution product `◁` on `Fam(C^op)`

**MacBeth — 2026-08-27 (PROVE session).** Answers Neil's directive (email UID 125):
*"Let's have left closedness too, if possible,"* hint *"left Kan extensions preserve
representability, then it's just coproducts."* Target: does the **non-symmetric** substitution
product `◁` on `Fam(C^op)` admit the **left internal hom** (`◁`-closure) that `Cont=Fam(Set^op)`
provably lacks, and if so under what hypothesis on the base `C`?

**Headline.** Yes — and the mechanism is a *collapse*, not a new adjoint. **Over a base whose
position objects are dualizable (`Vec_fd`), the substitution product `◁` and the Dirichlet
product `⊗` COINCIDE** (`(S,P)◁(T,Q)=(S×T,(P_s⊗Q_t))`, my proved Prop 4.1). Hence `◁` becomes
*symmetric*, its left and right internal homs merge, and the `◁`-closure is *exactly* the
`⊗`-internal-hom of T2. It therefore exists **on `Fam_fin(Vec_fd^op)`** — finite shape sets,
finite-dimensional positions — with

> `[(T,Q)◁(R,M)] = (R^T, (⊕_{t∈T} M_{ρ(t)}⊗Q_t^{*})_{ρ:T→R})`,

and **fails** on `Fam(Vec_fd^op)` (infinite shapes) and `Fam(Vec^op)` (infinite-dimensional
positions), for the same two dual reasons as T2.

**The crown (opposite of T1/T2).** Over the extensive base `Set`, `◁≠⊗`, `◁` is genuinely
non-symmetric, and the `◁`-closure is **obstructed** (my Workers Thm 2: the forced hom is
non-polynomial) while `⊗` is closed. **Non-extensivity of the linear base — the *obstruction*
to fullness (T1) and to `⊗`-closedness (T2) — is here the *repair*:** linearity collapses `◁`
onto the closed `⊗`. Extensivity and `◁`-left-closedness are in **opposition**. The villain of
T1/T2 is the hero of T4.

This proof is a **synthesis of three of my own `proved` results** — Prop 4.1
(`linear-containers-vec`, `◁=⊗` over `Vec_fd`), T2 (`t2-day-closedness-famcop`, `⊗`-closedness
criterion + rigid hom + Vec dichotomy), and Workers Thm 2
(`workers-x-closed-lhd-obstructed`, `◁`-closure fails over `Set`) — plus one conceptual
identification (tininess ⟺ collapse) that names the load-bearing hypothesis base-generally.

---

## 0. Setup, and the disambiguation (done first, per PROVE.md discipline)

Fix `(C,⊗,I,[-,-])` closed symmetric monoidal, cocomplete. `Fam(C^op)` has objects
`(S,(P_s)_{s∈S})` (`S` a set, `P_s∈C`) and morphisms
`Fam((A,X),(B,Y))=∏_{a}∐_{b}C(Y_b,X_a)` (Def 0.1 of `t2-day-closedness-famcop.md`). It is the
free coproduct completion of `C^op`, with generators `⟨Z⟩:=({∗},Z)`. When `C` is closed and
cocomplete, each object has an **extension endofunctor**

> `⟦S,P⟧ : C → C,   ⟦S,P⟧X = ∐_{s∈S} [P_s, X]`      (over `Set`: `Σ_s X^{P_s}` = Poly).

**The substitution product `◁`** is the monoidal structure whose extension is functor
composition, `⟦(S,P)◁(T,Q)⟧ = ⟦S,P⟧∘⟦T,Q⟧` (DJN `2305.05655`; over `Set` = the composition
product of `Poly`, Niu–Spivak). `◁`-comonoids = `C`-enriched categories (DJN Thm 4.2). `◁` is
**non-symmetric**, so it has two potential internal homs:

- **the `◁`-coclosure** — **VARIANCE CORRECTED 2026-08-30.** This line previously read
  "right internal hom = **right** adjoint to `(T,Q)◁(−)`". That is wrong on **both** counts.
  Niu–Spivak Prop 6.57 (Meyers) reads `Poly(p, r ◁ q) ≅ Poly(⌜q/p⌝, r)`, i.e.

      ⌜q/−⌝  ⊣  (−) ◁ q         with   ⌜q/p⌝ = Σ_{i∈p(1)} y^{q(p[i])}

  so the coclosure is a **LEFT** adjoint, and to `(−)◁q` — the *same* variable as the target
  below, not the other one. **KNOWN, exists over `Set`, unconditionally in `q`** (re-derived
  independently 2026-08-30, `proofs/2026-08-30-pra-vs-probe-method.md`). A left Kan extension
  (`Lan`); my `position-op-monads-to-comonads` builds it as `Lan_{(S,P)}M`. *Not the target.*
  ⚠ The old line also asserted "= directed containers". That identification is **not** the
  Prop 6.57 statement and is left unverified here — do not cite it from this file.
- **left internal hom** `[(T,Q)◁−]` = right adjoint to `(−)◁(T,Q)` = the **`◁`-closure**.
  **This is the target.** Over `Cont=Fam(Set^op)` it is **obstructed** (Workers Thm 2: the
  representing functor is non-polynomial). PROVE.md's "curry the LEFT argument."

So **T4-left = "does a richer base `C` supply the `◁`-closure (right adjoint to `(−)◁q`) that
`Set` lacks?"** — a genuinely different adjoint from the known coclosure.

---

## 1. The obstruction over `Set`, and its exact structural source

`(−)◁q` preserves coproducts in its left argument (`⟦(∐_i p_i)◁q⟧=∐_i⟦p_i⟧∘⟦q⟧`), so by the
universal property of the free coproduct completion its right adjoint exists iff, for every
target `(R,M)`, the functor `G(Z):=Fam(⟨Z⟩◁q,(R,M)):C^op→Set` is familially representable; then
`[q◁−](R,M)=(U,(N_u))` with `G≅∐_u C(N_u,-)`.

Compute `⟨Z⟩◁q` from the extension: `⟦⟨Z⟩◁q⟧X = [Z, ∐_{t}[Q_t,X]]`. **Over `Set`**,
`[Z,-]=(-)^Z=∏_{d∈Z}(-)`, and the exponential distributes over the coproduct (the
extensive/ccc distributive law):

> `[Z, ∐_t B_t] = ∐_{τ:Z→T} ∏_{d∈Z} B_{τ(d)}`,      (DIST)

so `⟨Z⟩◁q` has **shape set `T^Z`** and positions `Σ_{d∈Z}Q_{τ(d)}`. The `|T|^{|Z|}`-fold
shape set forces the representing container to carry double-exponential data, so `G` is not
familially representable when `|T|≥2` (Workers Thm 2, verified: `|T_R([n])|` grows like
`n^{2^n}=1,16,6561,…`, super-polynomial). **The obstruction is created entirely by (DIST):
`[Z,-]` failing to preserve the coproduct `∐_t`.** (Escape hatch, from Workers: if `q` is a
*monomial*, `|T|=1`, there is no branching and the closure exists even over `Set`.)

---

## 2. The repair: dualizable positions collapse `◁` onto `⊗`

**Definition.** An object `Z∈C` is **tiny** if `[Z,-]:C→C` preserves small coproducts.
In a closed symmetric monoidal category every **dualizable** `Z` is tiny: `[Z,-]=Z^{*}⊗(-)`
is a left adjoint, hence preserves all colimits. Over `Vec`, tiny = dualizable = **finite
-dimensional**.

**Proposition 2.1 (collapse `◁=⊗`).** If every position object of `p=(S,P)` is tiny, then for
every `q=(T,Q)`,
`⟦p◁q⟧ = ⟦p⊗q⟧`, and hence `p◁q = p⊗q = (S×T,(P_s⊗Q_t))` in `Fam(C^op)`.

*Proof.* Tininess of each `P_s` replaces (DIST) by genuine coproduct-preservation:
```
⟦p◁q⟧X = ∐_s [P_s, ∐_t [Q_t,X]]
       = ∐_s ∐_t [P_s, [Q_t,X]]          (P_s tiny ⟹ [P_s,-] preserves ∐_t)
       = ∐_{s,t} [P_s⊗Q_t, X]            (tensor–hom adjunction [P,[Q,X]]=[P⊗Q,X])
       = ⟦(S×T,(P_s⊗Q_t))⟧X = ⟦p⊗q⟧X.
```
Over `Vec_fd` (all objects dualizable) this is exactly my **proved Prop 4.1** of
`2026-08-18-linear-containers-vec.md`: `(S,P)◁(T,Q)=(S×T,(P_s⊗Q_t))` — the *same formula* as
`⊗`. ∎

**Reading.** The substitution's shape set is the "dependent sum" `Σ_s Dec_T(P_s)` (over `Set`,
`Σ_s T^{P_s}`); tininess collapses it to the *plain product* `S×T`. This is the same
biproduct/linearity collapse that turns the `◁`-comonoid *algebroid* into a *family of
algebras* (`vec-comonoids-algebras` §6): its object-level face. **Corollary: over a tiny base
`◁` is symmetric, and its left and right internal homs coincide with the single
`⊗`-internal-hom.** The entire "non-symmetric `◁`, two distinct homs, closure obstructed"
picture is a phenomenon of **non-tiny (extensive)** bases.

---

## 3. T4-left over the linear base

**Theorem 3.1 (`◁`-left-closedness on the linear base).** With `◁` as in Prop 2.1:

1. **`Fam_fin(Vec_fd^op)` (finite shape sets, finite-dimensional positions): `◁` IS
   left-closed.** Indeed `◁=⊗` (Prop 2.1), and `⊗` is closed there (T2 Thm 3.2(1)). The left
   internal hom is the T2 rigid hom
   ```
   [(T,Q)◁(R,M)] = (R^T, (N_ρ)_{ρ:T→R}),   N_ρ = ⊕_{t∈T} M_{ρ(t)}⊗Q_t^{*},
   ```
   which lies in `Fam_fin(Vec_fd^op)` (finite `T` ⟹ finite `⊕`, staying finite-dimensional).
2. **`Fam(Vec_fd^op)` (arbitrary shape sets): NOT left-closed.** For infinite `T` the
   representing position `⊕_{t∈T} M_{ρ(t)}⊗Q_t^{*}` is infinite-dimensional (T2 Thm 3.2(2),
   conjunct **B**: witness `T=ℕ`, all `Q_t=M_r=k`, forces `k^{(ℕ)}∉Vec_fd`).
3. **`Fam(Vec^op)` (infinite-dimensional positions): NOT left-closed.** Here the *collapse
   itself* fails: an infinite-dimensional position is not tiny, so `[Z,-]` does not preserve
   `∐_t` and `⟨Z⟩◁q ≠ ⟨Z⟩⊗q`; equivalently the single-factor representability breaks (T2
   Lemma 3.1 / Thm 3.2(3), conjunct **A**: `Z↦|Z⊗Q|` not familially representable for
   `dim Q=∞`).

*Proof.* (1) is Prop 2.1 + T2 Thm 2.3/3.2(1); the adjunction `(−)⊗q ⊣ [q⇒−]` is genuine (T2
Thm 1.1), so `(−)◁q ⊣ [q◁−]` is too. (2),(3) are the two T2 failure witnesses, re-read
through Prop 2.1. ∎

**Load-bearing conjunct, named.** As in T2, the single obstruction is
**"dualizable-and-summable"**: the hom position `⊕_{t∈T}M_{ρ(t)}⊗Q_t^{*}` must (i) *make sense*
— each `Q_t` dualizable, forcing finite-dimensional positions (tininess = the collapse) — and
(ii) *exist* — the coproduct present in `C`. Over `Vec` these are jointly satisfiable only on
the finite/fd corner. The `◁`-closure inherits T2's conjunct structure *because `◁` collapses
to `⊗`*.

**Boundary checks** (verified §5): `q=I` gives `[I◁−](R,M)=(R,M)` (`p◁I=p`); `q` a monomial
(`|T|=1`) gives the closure even without rigidity (matching the `Set` escape hatch).

---

## 4. The contrast, and why it is the crown

Assemble the two regimes:

| base `C` | extensive? | `◁ vs ⊗` | `◁` symmetric? | `⊗`-closed? | `◁`-closed (left)? |
|---|---|---|---|---|---|
| `Set` (and toposes) | ✓ | `◁ ≠ ⊗` (shapes `Σ_s T^{P_s}`) | no | **yes** (Dirichlet hom) | **NO** (Workers Thm 2) |
| `Vec_fd` (finite corner) | ✗ | **`◁ = ⊗`** (Prop 2.1) | **yes** | yes (T2) | **YES** (Thm 3.1) |

**Proposition 4.1 (extensivity ⊥ `◁`-left-closedness).** The `◁`-closure obstruction over `Set`
and its repair over `Vec_fd` are two faces of the *same* fact — the distributive law (DIST) —
with **opposite** valuation:
- Over an **extensive** base (DIST holds nontrivially), `[Z,-]` explodes `∐_t` into `T^Z`
  branches: `◁` stays distinct from `⊗`, genuinely non-symmetric, and its closure is
  non-polynomial (absent). Extensivity *is* the obstruction to `◁`-closedness.
- Over a **linear** base (DIST degenerates: `[Z,-]` is additive, preserves `∐_t`), `◁`
  collapses onto the closed, symmetric `⊗`. Non-extensivity *is* the repair.

This exactly inverts T1 and T2, where non-extensivity was the obstruction (fullness `∐⊊⊕`
fails; `⊗`-closedness needs the finite-fd corner). The reason it inverts: T1/T2 measure
whether the *external* `Set`-coproduct on shapes is seen correctly by the base
(non-extensivity breaks that), whereas `◁`-closedness needs the base's *internal hom on
positions* to NOT branch against coproducts — which is precisely additivity. **The same
`∐⊊⊕` seam that costs fullness buys `◁`-closedness.**

**Neil's hint, decoded.** "left Kan extensions preserve representability, then it's just
coproducts": over the rigid base, `C(M_r, Z⊗Q_t) = C(M_r⊗Q_t^{*}, Z)` — the left adjoint
`(−)⊗Q_t^{*}` preserves (co)representability — after which `∏_t` of corepresentables is
corepresentable at the `⊕_t` (coproducts). This is T2's rigid regime; T4 recognizes it as the
`◁`-closure via the collapse. (The *coclosure* — the other, known hom — is the genuine `Lan`;
the *closure* here uses only the trivial "`Lan`" that a dualization provides.)

---

## 5. Verification

`scratch/lhd-left-closedness-verify.py` (this session), all green:
- **(a) Collapse `◁=⊗`.** The composite-functor dimension computed via the *linear* internal
  hom (no branching), `∐_s[P_s,∐_t[Q_t,X]]`, equals the tensor dimension `∐_{s,t}[P_s⊗Q_t,X]`
  on **20000/20000** random families (dims 1–4). Contrast printed: for `|S|=2,|T|=3`, `Set`
  shape count of `p◁q` is `Σ_s|T|^{|P_s|}=12` vs the collapsed `Vec` count `|S||T|=6`.
- **(b) Closure adjunction.** The cardinality identity over `F_2`
  `|Fam((A,X)◁q,(R,M))| = |Fam((A,X),[q◁−](R,M))|` with `(A,X)◁q=(A×T,(X_a⊗Q_t))` and
  `[q◁−](R,M)=(R^T,(⊕_t M_{ρt}⊗Q_t^{*}))` holds on **3000/3000** random small families. (The
  underlying identity `∏_t Σ_r (2^X)^{m_r q_t}=Σ_{ρ}∏_t(2^X)^{m_{ρt}q_t}` is the `(★)`
  distributivity of T2.)
- **Boundaries.** `q=I` and `q` monomial both satisfy the identity. `Set` double-exponential
  non-representability is already verified in `workers-type-hierarchy/lhd_cardinality.py`
  (`t_n=1,16,6561,4294967296`).

---

## 6. Placement and honesty ledger

**Stands on (all my own `proved`):** Prop 4.1 `linear-containers-vec` (`◁=⊗` over `Vec_fd`);
T2 `t2-day-closedness-famcop` (`⊗`-closedness criterion, rigid hom, Vec dichotomy); Workers
Thm 2 `workers-x-closed-lhd-obstructed` (`◁`-closure fails over `Set`). Compose to a new
statement about the *`◁`* internal hom.

**Cited, not reproved:** DJN `2305.05655` (`◁` over a general base; comonoids = enriched
categories — they do **not** treat any closed structure for `◁`, so the `◁`-closure verdict is
the T4 delta, exactly as closedness was the T2 delta). Niu–Spivak Prop 6.57 (the *coclosure* =
the other, known hom — carefully **not** what is proved here). Gambino–Kock `0906.4931` (`Vec`
not LCCC — boundary).

**Claimed delta.** (i) Prop 2.1 as a *general* statement with its named cause (tininess ⟺
collapse of the substitution's dependent-sum shape set), lifting the `Vec_fd`-specific Prop 4.1
to a base-general mechanism. (ii) Theorem 3.1: the `◁`-**left**-closure exists on
`Fam_fin(Vec_fd^op)` with explicit hom and fails on both larger linear categories — the first
positive `◁`-closure result over any base, and the answer to Neil's "if possible." (iii)
Prop 4.1's opposition principle: extensivity obstructs `◁`-closedness while it (via `⊗`) was
neutral/beneficial for T1/T2 — the villain/hero inversion.

---

## 7. Status and gaps (precisely stated)

**PROVED.**
- Prop 2.1 (collapse `◁=⊗` under tiny/dualizable positions), base-general; the `Vec_fd`
  instance is my prior `proved` Prop 4.1.
- Theorem 3.1 (`◁`-left-closed on `Fam_fin(Vec_fd^op)` with explicit hom; not on
  `Fam(Vec_fd^op)` nor `Fam(Vec^op)`), via Prop 2.1 + T2.
- Prop 4.1 (extensivity ⊥ `◁`-left-closedness), assembling the `Set` obstruction (Workers
  Thm 2) against the linear repair.

**GAPS.**
1. **General "iff" for the collapse.** Prop 2.1 is a one-directional sufficient condition
   (tiny ⟹ `◁=⊗`). The converse — *does `◁=⊗` (or merely `◁`-left-closure existing) force the
   positions tiny over a general closed `C`?* — is proved only over `Set` (via the
   double-exponential, where non-tiny objects `|Z|≥2` genuinely break it) and over `Vec`
   (Lemma 3.1). The exact class of non-cartesian, non-rigid `C` admitting `◁`-closure is open,
   as it was for `⊗` in T2 Gap 1. Candidate: `◁`-left-closed ⟺ every position tiny **or** `q`
   monomial.
2. **`◁` over full `Vec` / DJN's exact `◁` off the tiny locus.** For infinite-dimensional
   positions the collapse fails and it is not settled whether DJN's `◁` on `Fam(Vec^op)` is
   even the endofunctor composition `(S×T,P⊗Q)` (Prop 4.1's finiteness hypothesis is used to
   land `◁` in the category). Theorem 3.1(3) states the *closure* fails there; the finer
   question of what `◁` *is* there is the same infinite-dimensional gap flagged in
   `vec-comonoids-algebras` §9.
3. **Beyond `Vec`.** Whether other non-extensive closed bases (e.g. `sSet`-like additive
   categories, categories of `G`-representations) give a *different* collapse locus, or a
   `◁`-closure by a mechanism other than `◁=⊗`, is unexplored.

---

## 8. Grant framing

T4 completes the closed-structure map of `Fam(C^op)`: of the two convolution tensors, `⊗` is
closed exactly on cartesian bases and the finite-fd linear corner (T2); the substitution `◁` is
left-closed **only** where it degenerates to `⊗` — the finite-fd linear corner — and is
genuinely *obstructed* on every extensive base. For the **applications** narrative
(agent orchestration = `◁`-composition, `orchestration-is-zappa-szep-weld`): *higher-order
substitution of resource-graded processes — a process that consumes a `q`-process in its
plug-in slot and returns an `(R,M)`-process — exists only when the resource base is
finite-dimensional-linear (and then `◁` is symmetric, substitution = parallel product), and is
structurally impossible over any set-like (extensive) resource base.* The compositional reading
of why classical (Set-based) process substitution resists currying while finite quantum/linear
substitution does not. With T1 (fullness) and T2 (`⊗`-closedness) this delimits precisely which
container calculi over which bases admit each closed structure.
