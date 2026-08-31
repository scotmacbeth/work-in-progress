# δ ≟ Φ — is Weber's distributivity comparison the T2 closedness obstruction?

**MacBeth — 2026-08-28.** Executes the decision procedure of
`memory/questions/weber-delta-vs-t2-phi.md` (§"How to decide (cheap first)"). Grade of
everything concluded here: **`computed`** (an agent's derivation, reconstructing Weber's δ from
the reading-log description of `1106.1983`, not from a line-by-line PDF read).

**VERDICT (up front): DISTINCT.** δ and Φ are *logically independent* conditions — neither
implies the other — and a fortiori not the same natural transformation. They agree in *value*
(both hold) over cartesian bases and (both hold) on the tiny/fd corner, and both fail on generic
`Fam(Vec^op)` data, but this is a coincidence of "everything finite-dimensional," not an
identity of maps. The separating fact: **δ constrains the LEFT (composition) positions `P_s`;
Φ constrains the RIGHT (tensor) positions `Q_t` and the target `(R,M)` — different data.**
A bonus correction: Φ's *familial representability* is a **Weber comparison map, but from his
parametric-right-adjoint / familial-functor theory, not from the distributivity-pullback δ of
`1106.1983`.** The specific conjecture "δ = Φ" is false; the right Weber home for T2 is a
different Weber theorem.

---

## 1. The two maps, written explicitly on a 2-shape family

Fix `(C, ⊗, I, [-,-])` closed symmetric monoidal, cocomplete. `Fam(C^op)` as in T2 Def 0.1:
objects `(S,(P_s))`, homs `∏_a ∐_b C(Y_b, X_a)`; generators `⟨Z⟩ = ({∗}, Z)`; extension
`⟦S,P⟧X = ∐_s [P_s, X]`.

Take throughout the **2-shape** left family `p = (S,P)`, `S = {1,2}`, positions `P_1, P_2 ∈ C`,
and a right family `q = (T,Q)`, `T = {1,2}`, positions `Q_1, Q_2 ∈ C`. Target for the internal
hom: `(R,M)`, `R = {1,2}`, `M_1, M_2 ∈ C`.

### 1a. Weber's δ (transported to `Fam(C^op)`)

Weber `1106.1983`: polynomial composition runs on **distributivity pullbacks**; a candidate
diagram around a composable pair is the distributivity pullback ⟺ a canonical comparison **δ is
iso** ⟺ **the middle leg is exponentiable** (reading-log `2026-08-28.md`, confirmed). In the
polynomial-functor reading, δ-iso is exactly the distributive law that makes the *composite*
`⟦p⟧∘⟦q⟧` again a polynomial — i.e. it is the condition for the **substitution product `◁`** to
be well-defined (land back in containers), replacing GK's LCCC/internal-Π.

Transport to `Fam(C^op)` via the extension. Test δ on a single left generator `⟨Z⟩` composed
with `q`:
```
   ⟦⟨Z⟩ ◁ q⟧ X = [ Z , ⟦q⟧X ] = [ Z , ∐_{t∈{1,2}} [Q_t, X] ] = [ Z , [Q_1,X] ∐ [Q_2,X] ].
```
For this to be a container extension `∐_u [N_u, X]`, the middle leg `[Z,−]` must distribute over
the position coproduct `∐_t`. **δ is exactly this comparison map:**
```
   δ_{Z,q}(X) :  ∐_{τ : Z→T} [ ⊗?...]  ... i.e. the canonical
   δ_{Z,q}(X) :  [Z, [Q_1,X]] ∐-branching  ⟶  [ Z, [Q_1,X] ∐ [Q_2,X] ].
```
Concretely the *always-defined* canonical map runs
```
   δ_{Z,q}(X) :  ∐_{τ:Z→T} [ Z, [Q_{τ}, X] ]_{fibred}  ⟶  [ Z, ∐_t [Q_t,X] ],
```
the map assembling, for each "branch choice" `τ : Z→T`, the sub-hom of `Z`-indexed families all
landing in the `τ`-chosen summand, into the full hom into the coproduct. **Over `Set`** this map
is the classical iso (DIST of T4-left §1):
```
   [Z, ∐_t B_t] ≅ ∐_{τ:Z→T} ∏_{d∈Z} B_{τ(d)},        (Set: Z exponentiable ⟹ δ iso)
```
so `⟨Z⟩◁q` is the container with **shape set `T^Z`** and positions `∐_{d∈Z} Q_{τ(d)}`. **Over
`Vec`** `δ_{Z,q}` is iso **iff `Z` is tiny (= dualizable = finite-dimensional)**, in which case
`[Z,−] = Z^*⊗(−)` is a left adjoint and
```
   [Z, ∐_t [Q_t,X]] = ∐_t [Z, [Q_t,X]] = ∐_t [Z⊗Q_t, X]      (Z fd ⟹ δ iso),
```
i.e. `⟨Z⟩◁q = ⟨Z⟩⊗q` — precisely T4-left Prop 2.1 (the collapse). For infinite-dimensional
`Z`, `[Z,−]` does not preserve `∐_t`, δ is not iso, and `⟨Z⟩◁q` is not a container.

**Reading of δ on the 2-shape family.** For `p = (P_1,P_2)`, `⟨p⟩◁q` is a container iff
`δ_{P_1,q}` **and** `δ_{P_2,q}` are iso, i.e. iff **both left positions `P_1,P_2` are
exponentiable/tiny**. *δ is a condition on the LEFT positions `P_s` (and, mildly, on the index
set `T` of `q`, through the branch set `T^{P_s}`).* It is entirely internal to `C`
(exponentiability of the `C`-object `P_s`) and says **nothing about the target `(R,M)`** — it is
not an internal-hom / closedness statement at all; it is the well-definedness of the monoidal
product `◁`.

### 1b. T2's Φ (familial-representability comparison for `⊗`-closedness)

T2 Thm 1.1: `(−)⊗q` has a right adjoint `[q ⇒ −]` in `Fam(C^op)` ⟺ for every target `(R,M)`
```
   Φ_{q,M}(Z) = ∏_{t∈T} ∐_{r∈R} C(M_r, Z⊗Q_t) : C → Set     is familially representable.
```
On our 2×2 data:
```
   Φ(Z) = [ C(M_1,Z⊗Q_1) ∐ C(M_2,Z⊗Q_1) ] × [ C(M_1,Z⊗Q_2) ∐ C(M_2,Z⊗Q_2) ].
```
Set-distributivity (★) reindexes over `ρ:T→R` (four branches `ρ ∈ R^T`):
```
   Φ(Z) ≅ ∐_{ρ:{1,2}→{1,2}} Θ_{M∘ρ, Q}(Z),   Θ_{A,Q}(Z) = C(A_1, Z⊗Q_1) × C(A_2, Z⊗Q_2).
```
The **candidate representing object** for the `ρ`-branch is `N_ρ`, and the **canonical
comparison map is**
```
   γ_{ρ}(Z) :  C(N_ρ, Z)  ⟶  Θ_{M∘ρ,Q}(Z),      N_ρ "=" M_{ρ(1)}⊗Q_1^* ∐ M_{ρ(2)}⊗Q_2^*,
```
assembled from the two single-factor comparisons
```
   γ_{A,Q_t}(Z) :  C(A⊗Q_t^*, Z)  ⟶  C(A, Z⊗Q_t),
        g ⟼  ( A --A⊗coev_{Q_t}--> A⊗Q_t^*⊗Q_t --g⊗Q_t--> Z⊗Q_t ).
```
`γ_{A,Q_t}` is **defined only when `Q_t` has a dual** (needs `coev_{Q_t}`), and is **iso iff
`Q_t` is dualizable** (`Vec`: fd) — this is T2 Lemma 3.1. The total comparison
```
   Γ(Z) : ∐_{ρ:T→R} C(N_ρ, Z)  ⟶  Φ(Z)
```
is the familial-representability comparison; **Φ-representable ⟺ Γ iso** ⟺ `⊗` closed at
`(q, target)`. (Over `Set`/cartesian bases the candidate `N_ρ` is instead built by the
projection split `C(A,Z×Q)=C(A,Z)×C(A,Q)`, giving `N_ρ = ∐_t M_{ρ(t)}` up to a copower — a
*different* representing object, but the same "is Γ iso" comparison.)

**Reading of Φ on the 2-shape family.** `Φ` depends only on `q = (T,Q)` (the RIGHT positions
`Q_1,Q_2`) and the **target** `(R,M)`. The left positions `P_1,P_2` appear **only** as the
universally-quantified variable `Z` — they are *not* part of the data of Φ. Φ constrains the
**RIGHT positions `Q_t` (dualizability) and the index set `T` (summability of `∐_t N_t`)**, plus
the target.

---

## 2. The decisive separation (both implication directions fail)

The cheapest possible test: since δ depends on `(P_s ; T)` and Φ depends on `(Q_t ; R,M)`, feed
them **mismatched finite/infinite data** over `C = Vec` and watch them come apart.

**Direction 1 — δ iso while Φ NOT representable.** Take left `p` with `P_1,P_2` **finite-
dimensional** (tiny), and right `q` with `Q_1 = k^{(ℕ)}` **infinite-dimensional**, target
`(R,M)` anything.
- δ: each `P_s` is tiny ⟹ `[P_s,−]` preserves `∐_t` ⟹ `δ_{P_s,q}` iso ⟹ `⟨p⟩◁q` **is** a
  container (`= ⟨p⟩⊗q`). **δ iso. ✓**
- Φ: contains the factor `C(M_r, Z⊗Q_1)` with `dim Q_1 = ∞`; by T2 Lemma 3.1 the single factor
  `Z ↦ C(M_r, Z⊗Q_1)` is **not** familially representable ⟹ Φ not representable ⟹ **`⊗` not
  closed. Φ FAILS. ✗**

So **δ iso ⇏ Φ representable.**

**Direction 2 — Φ representable while δ NOT iso.** Take right `q` with `Q_1,Q_2 = k`
(fd), `T = {1,2}` finite, target `M_1,M_2 = k` (fd) — a full `Fam_fin(Vec_fd^op)` right/target
datum, so **Φ representable ⟹ `⊗` closed. ✓** (T2 Thm 3.2(1).) Now take the left `p` with
`P_1 = k^{(ℕ)}` **infinite-dimensional**.
- Φ: unchanged — it never saw `P_1` — still representable. **Φ holds. ✓**
- δ: `P_1` not tiny ⟹ `[P_1,−]` does not preserve `∐_t` ⟹ `δ_{P_1,q}` **not** iso ⟹ `⟨P_1⟩◁q`
  is not a container / `◁` ill-defined at this datum. **δ FAILS. ✗**

So **Φ representable ⇏ δ iso.**

**Both directions fail ⟹ δ and Φ are logically independent conditions, hence not equal or
mutually-representing maps.** The "coincidence of failure loci over Vec" noted in the question
file is an artifact of probing `Fam(Vec^op)` with *generic* (everywhere-infinite-dimensional)
data, where both fail at once. Mixed data (fd-left/∞-right and ∞-left/fd-right) separates them
cleanly. **VERDICT = DISTINCT**, and not even CORNER-ONLY: they are different maps *everywhere*,
merely both iso on the tiny corner and both iso over cartesian bases.

---

## 3. Why they are different in one sentence each (the load-bearing reasons)

1. **Different adjoints / different functors.** δ ⟺ the composition/substitution `◁` is
   well-defined ⟺ pullback `f^*` has a right adjoint `Π_f` (dependent product / exponentiable
   middle leg). Φ ⟺ the Dirichlet tensor `(−)⊗q` has a right adjoint `[q⇒−]` (internal hom /
   closedness). Right adjoints to **different functors** (`f^*` vs `(−)⊗q`) ⟹ different
   universal properties ⟹ different canonical comparison maps. δ is not an internal-hom
   statement at all; it is monoidal-product well-definedness.

2. **Different data / different legs.** δ = "**left** positions `P_s` exponentiable/tiny"
   (`[P_s,−]` distributes over `∐_t`); Φ = "**right** positions `Q_t` dualizable AND `∐_t N_t`
   summable" + target. §2 turns this into two concrete Vec witnesses where one holds and the
   other fails. They constrain disjoint pieces of the composite `⟨p⟩◁q` / `p⊗q`.

**Where they DO touch (the T4-left collapse, and only there).** On `Fam_fin(Vec_fd^op)` every
position (left and right) is fd, so simultaneously: δ iso (left positions tiny ⟹ `◁ = ⊗`) and
Φ representable (right positions dualizable + finite `T` ⟹ `⊗` closed). There the substitution
`◁` collapses onto the closed symmetric `⊗` (T4-left Prop 2.1 + Thm 3.1), so the *adjoint that
δ enables* (composition, now = `⊗`) and *the adjoint Φ enables* (the `⊗` internal hom) live on
the same monoidal structure. But δ (a coproduct-preservation iso of `[Z,−]`) and Φ (a
representing-object iso for an internal hom) remain **distinct maps that are co-enabled by
dualizability**, not one map. This is exactly the question file's warning (i): any identification
needs the `◁=⊗` collapse first, and even then it is co-enablement, not equality.

---

## 4. The correction: Φ *is* a Weber comparison — but a different Weber

The conjecture mislocates T2 inside Weber's œuvre. Two distinct "canonical map iso" theories:

- **Weber `1106.1983` (distributivity pullbacks), δ:** exponentiability of the middle leg;
  governs when polynomial **composition ◁** is defined. Transported to `Fam(C^op)`, δ ⟺
  **tininess of the left positions** — which is precisely the load-bearing hypothesis of
  MacBeth's **T4-left** (Prop 2.1 collapse), *not* of T2. **So Weber-δ ↔ T4-left, not T2.**

- **Weber's parametric-right-adjoint / familial-functor theory** ("Familial 2-functors and
  parametric right adjoints", TAC 18, 2007; same author, different paper): a functor is
  *familial* (p.r.a.) iff it is, fibrewise, a coproduct of representables. T2's condition —
  `Φ` **familially representable** — is *verbatim* the statement that the functor representing
  `(−)⊗q`'s would-be adjoint is **familial/p.r.a.** in Weber's 2007 sense. **So T2 ↔ Weber's
  familial/p.r.a. comparison, a different Weber theorem.**

Hence: δ (1106.1983) pairs with **T4-left** (`◁` well-definedness / tininess), and **T2** pairs
with **Weber's p.r.a./familial machinery**. The question conflated the two Weber comparisons
because both are "a canonical map becomes iso." Correctly separated, the DISTINCT verdict is
structural, not accidental.

---

## 5. Confidence, registrability, what would upgrade

**Confidence: high** for DISTINCT. The separation argument (§2) needs only: (a) δ ⟺ left-position
exponentiability/tininess (from the reading-log statement "δ iso ⟺ middle leg exponentiable",
plus the extension identity `⟦⟨Z⟩◁q⟧X = [Z,∐_t[Q_t,X]]` which forces δ onto the `Z=P_s` leg);
(b) Φ ⟺ right-position dualizability + summability (MacBeth's own `proved` T2 Lemma 3.1 / Thm
3.2). Both witnesses live in `Vec` and are already numerically corroborated in the T2/T4 scratch
scripts. The logical-independence conclusion does **not** depend on the exact fibrewise formula
of Weber's δ — only on *which leg* it tests, which the extension computation pins unambiguously
(δ concerns `⟨Z⟩◁q`, so it concerns `Z = P_s`).

**Registrable as `computed`?** Yes — as a **negative / clarifying** Front-D result:

> **(computed) δ ≠ Φ.** Weber's distributivity-pullback comparison δ (`1106.1983`) and MacBeth's
> T2 `⊗`-closedness obstruction Φ are *logically independent* on `Fam(C^op)`: δ tests
> exponentiability/tininess of the LEFT (composition) positions and governs well-definedness of
> `◁`; Φ tests dualizability/summability of the RIGHT (tensor) positions + target and governs
> closedness of `⊗`. Two `Vec` witnesses (fd-left/∞-right and ∞-left/fd-right) separate them in
> both directions. The correct Weber home for T2 is his **parametric-right-adjoint / familial**
> theory (TAC 18, 2007), not the distributivity-pullback δ. Weber-δ instead matches MacBeth's
> **T4-left** tininess collapse.

This *does not* fold T2 into Weber's weakening tower as the conjecture hoped; it **re-files**
both T2 and T4-left against the correct Weber theorems, which is a cleaner Front-D placement than
the conjectured single identification. The would-be crown ("T2 = Weber-distributivity in
disguise") is **refuted**; the survivable, valuable statement is the two-way re-filing.

**What would upgrade to `proved`:** (i) a line-by-line read of Weber `1106.1983` §2 confirming
δ's fibrewise formula and that its transport to the family fibration `Fam(C^op)` lands on the
left-position exponentiability as claimed (I reconstructed this from the extension identity + the
reading-log characterization, not the PDF); (ii) checking Weber TAC 18 (2007) Def of familial /
p.r.a. against T2's familial-representability verbatim, to make the "T2 ↔ Weber p.r.a." pairing a
citable equivalence rather than a recognized match; (iii) the external-vs-internal `∐` point
(question warning (ii)) is *subsumed* by the §2 separation — it need not be resolved to conclude
DISTINCT — but confirming that Weber's *internal* distributivity pullback, when the base is
`Fam(C^op)` with its external-Set-`∐`, still reads off as left-position tininess would tighten
(i).

**Where I did NOT fabricate:** I did not reconstruct the exact arrow-level formula of Weber's δ
(the `∐_{τ}∏_d`-assembly in §1a is the `Set`/general-shape of the distributive comparison, stated
as such); the argument is built on *which leg δ constrains*, which is forced by the extension
computation, not on δ's internal formula. If a reader needs δ's precise cells, that is gap (i).
