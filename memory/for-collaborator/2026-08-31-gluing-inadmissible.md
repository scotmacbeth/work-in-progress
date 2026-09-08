# Gl((−)²) is `◁`-inadmissible — and connectedness ≠ admissibility

**MacBeth → Neil / Robin, 2026-08-31 (PROVE session).**
Full proof: `proofs/2026-08-31-gluing-inadmissible-pi0.md`. Scripts:
`scratch/2026-08-31-gluing-{admissibility-lemmaS,extensivity,exp-construct}.py`. All green.

## The one-line story

I set out to test my last surviving Gap-1 candidate — the Artin gluing `Gl((−)²)` — hoping it would
be a *non-extensive, admissible, connected-unit* base and so show **Theorem B is not sharp**. It
turned out to be neither of the two things I needed, and the failure is more interesting than the
hoped-for success.

1. **`Gl((−)²)` is a topos.** `(−)² = Set(2,−)` is a right adjoint (to `2×(−)`), hence left exact;
   Artin gluing of a lex functor between toposes is a topos. So `Gl((−)²)` is a **Grothendieck
   topos**: cartesian closed, cocomplete, **infinitary extensive**. My own `2026-08-26` note labelled
   it "non-extensive" — that was an error (it confused "`T` doesn't preserve coproducts" with
   "`Gl(T)` isn't extensive"). **So it was never a Gap-1 base. Gap 1 stays empty of known inhabitants.**

2. **`Gl((−)²)` is `◁`-INADMISSIBLE.** Its objects are **graphs** (`B` vertices, `A` edges,
   `β : A → B²`), its categorical product is the **graph tensor product**, and the components functor
   `π₀ ⊣ (−)·1_C` is left adjoint to "discrete". I show:

   > Over such a base, **Lemma S ⟺ `π₀` preserves finite products** — and by **Weichsel's theorem**
   > (tensor of two connected bipartite graphs = 2 components) it does not: `π₀(K×K) = 2 ≠ 1` for `K`
   > a single edge. So Lemma S fails, hence no `◁`.

   Explicitly (searched and verified): `[K,\ 2·1_C] ≅ 2·1_C ⊔ K` — two looped vertices carrying the
   two points, **plus a bald edge** with no loop. That stray edge is a `π₀`-component with no point;
   a copower of `1_C` is "all diagonal", so the bald edge is exactly what breaks Lemma S.

3. **The corollary I did not expect — this is the deliverable.**

   > **Connectedness of the monoidal unit is necessary but NOT sufficient for `◁`-admissibility.**

   `Gl((−)²)` has a **connected** unit — its *points* functor `C(I,−) = β⁻¹(Δ)` (the loops)
   preserves coproducts — yet it is inadmissible. This is the **first base separating the two
   conditions**, and it does so *on the extensive pole*, where Theorem B already gives
   `admissible ⟹ connected`. So the extensive pole is not uniformly admissible: it splits by whether
   `π₀` is multiplicative.

## Why this is worth your time, Neil

- It answers the **"is Lemma S sufficient?"** gap in the strong negative. Not only is "Lemma S +
  extensivity" not enough for admissibility — **Lemma S itself fails on a connected-unit extensive
  topos.** Admissibility is strictly finer than connectedness.

- It gives a **checkable criterion** for the whole programme: over a nice base, `Fam(C^op)` is
  `◁`-closed only if the **connected-components functor is multiplicative**, `π₀(X×Y) ≅ π₀X×π₀Y`.
  This is the real content of Lemma S "having teeth" between the `Set` (`π₀=Id`) and `Vec` (`1_C=0`)
  degeneracies.

- The trichotomy table gains a **third inadmissible base with a third mechanism**:

  | base | extensive | unit connected | admissible | obstruction |
  |---|---|---|---|---|
  | `Set`, connected topos | ✓ | ✓ | **yes** | — |
  | `Set×Set` | ✓ | ✗ | no | disconnected unit (Thm B) |
  | **`Gl((−)²)`** | ✓ | **✓** | **no** | **`π₀` not multiplicative (Weichsel)** |
  | `Set_*` | ✗ | ✗ | no | polynomial degree `a=−4` (Thm A) |

- For the applications / "logic of containers" line: **a resource base needs its notion of "joint
  resource" to preserve connectedness.** If pairing two connected resources can *disconnect* them
  (a tensor-like, not cartesian-like, product — which is precisely what `Gl((−)²)` models), no
  external substitution calculus `◁` exists, *even though the base is a topos with a connected unit*.
  Concrete design test before building any composition operator: check `π₀(X×Y) =? π₀X × π₀Y`.

## Honest status

- Theorem G (inadmissibility) is `proved`: it rests on the `proved` reduction Prop 3.1 (pure category
  theory) and the finite, hand-verifiable computation `π₀(K×K)=2` (vertices `{00,01,10,11}`, edges
  `00–11`, `01–10`, two components). Weichsel is cited for the name, not load-bearing.
- Toposhood/extensivity (Prop 1.1) leans on the standard Artin gluing theorem (MacLane–Moerdijk),
  known to me at recall level; independently sanity-checked computationally (0 failures). It is used
  only for the *interpretation* (placing `Gl` on the extensive pole), not for Theorem G.
- **Gap 1 is disqualified-of-this-candidate, not proved empty.** Whether a genuinely non-extensive,
  non-collapse, admissible base exists is still open. `PROVE.md` task (3) (dropping cartesianness from
  Theorem B via idempotent splitting) is orthogonal and not attempted.
- Novelty ungated beyond the two textbook citations (Artin gluing; Weichsel). The *application* of
  Weichsel to container admissibility, and the reduction Prop 3.1, are mine.

— MacBeth
