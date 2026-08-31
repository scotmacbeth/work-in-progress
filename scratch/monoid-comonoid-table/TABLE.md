# Monoids and comonoids for the four monoidal structures on Cont

*Assembled 2026-07-18 for Neil (uid 65). Cells C1–C6 brute-force verified (shapes ≤3, positions ≤3):
`scratch/monoid-comonoid-table/{table,claims,c6_deep,c6_oplax}.py`. Trust: the ⊗-monoid cell is
`computed` (registry `dirichlet-monoid-classification`); the rest are known / proved.*

Conventions: container `c = (S, P)`, `P: S → Set`. Morphism `c → d` = forward `φ: S_c → S_d` +
BACKWARD `φ♯_s : d[φ s] → c[s]`. Comonoid = `(δ: c → c⊙c, ε: c → I)`; monoid = `(μ: c⊙c → c, η: I → c)`.

## The table

| ⊙ (unit) | COMONOIDS | MONOIDS |
|---|---|---|
| **◁** composition (y) | **small categories** (= directed containers). *AU; my M3, lean-verified.* **[INTERESTING]** | **polynomial monads**. *Gambino–Kock 0906.4931; indexed version = De Pascalis–Uustalu–Veltrì 2509.25879; my free-monad grafting, lean-verified.* **[INTERESTING]** |
| **⊗** Dirichlet (y) | **families of monoids** `Σ_s y^{M_s}`, each `M_s` an arbitrary monoid. *Proved 07-17 (bare-dirichlet-comonoid); answers Ch9 Q5 Poly/⊗ slice.* **[INTERESTING]** | **a monoid `(S,·,e)` + an oplax monoidal functor `P:(S,·,e)→(Set,×)`** (`φ_{s,s'}:P(s·s')→P(s)×P(s')`, `ε:P(e)→1`). *Computed today; dual of the comonoid cell; = Niu–Spivak Rmk 3.78 future work.* **[INTERESTING — new]** |
| **×** product (terminal 1 = one shape, ∅ positions) | **trivial**: every container is a comonoid, uniquely (diagonal Δ + terminal ε). *Cartesian ⇒ cataloguing.* | **constrained**: `η:1→c` needs the unit shape to have **empty positions**; generically **0**; when positions are all empty, ×-monoids = monoids on the shape set `S`. |
| **+** coproduct (initial 0 = empty shapes) | **trivial**: only `0` itself (a counit `c→0` forces `c≅0`). | **trivial**: every container is a monoid, uniquely (codiagonal ∇ + initial η). *Cocartesian ⇒ cataloguing.* |

**The story (for Neil's "interesting vs cataloguing"):** the two CANONICAL structures (×, +) give
degenerate (co)monoids — the cartesian/cocartesian collapse: on one side every object uniquely, on the
other only the unit. All the content is in the two DAY-EXOTIC structures ◁ and ⊗, and there it is
*rich and dual*:

- **◁**: comonoid = category, monoid = monad. (The Poly ↔ Cat / Poly ↔ monad dictionary.)
- **⊗**: comonoid = family of monoids (lax: a monoid on each fibre), monoid = monoid-on-shapes +
  oplax-functor-on-fibres. **The lax/oplax duality is exactly the comonoid/monoid duality**, with the
  shape map dualising diagonal (forced) ↔ arbitrary monoid.

## The ⊗ duality, spelled out (the pretty part)

`c = Σ_s y^{P(s)}`.
- **Comonoid** `δ: c → c⊗c`: shapes `S → S×S` must be a comonoid in `(Set,×)` = **diagonal (forced)**;
  backward `c[s]×c[s] → c[s]` = a **monoid on each `P(s)`**. ⟹ *family of monoids*.
- **Monoid** `μ: c⊗c → c`: shapes `S×S → S` = a **monoid on `S`**; backward
  `c[m(s,s')] → c[s]×c[s']` = an **oplax structure map**; unit `η:y→c` = `e∈S` + `ε:c[e]→1`. ⟹
  *monoid on `S` + oplax monoidal functor `P:S→(Set,×)`*.
  When `|S|=1` the oplax functor is a comonoid in `(Set,×)` = diagonal, so the ⊗-monoid is **unique**.

Counts (raw structures on labelled fibres), matched by two independent enumerations:
`⊗-comonoid`: |P|=1,2,3 → 1, 4, 33. `⊗-monoid`: (S=2,P=1)→4; (S=1,P=2)→1; (S=2,P=[2,1])→9;
(S=3,P=1)→33.

## Y-liftings (representables `y^A = (1,A)`)

`y^A ⊗ y^B = y^{A×B}`, unit `y = y^1`.
- A **⊗-comonoid** on `y^M` ⟺ a **monoid on `M`** (one shape, one fibre = the whole family). ✓ consistent.
- A **⊗-monoid** on `y^M` ⟺ a **comonoid on `M` in (Set,×)** = the diagonal, **always present, unique**.
So the representable column: `y^(−)` sends monoids-in-Set to ⊗-comonoids and (trivially) every object to a
unique ⊗-monoid. For ◁, `y^A ◁ y^B = y^{A×B}` too but sequential; representable ◁-comonoids = one-object
categories = monoids (again), representable ◁-monoids = one-object … (to work out in the write-up).

## Citations for the table
- ◁-comonoid: Ahman–Chapman–Uustalu (D1–D5); Ahman–Uustalu (DCont≅Cat). My M3/M3b lean-verified.
- ◁-monoid: Gambino–Kock 0906.4931 Thm 4.5 (poly monad); **indexed: 2509.25879 (DUV)**. My Free.lean.
- ⊗-comonoid: my `2026-07-17-bare-dirichlet-comonoid.md` (answers Ch9 Q5 slice); Niu–Spivak Rmk 3.78 (dual as future work).
- ⊗-monoid: **new (computed)**; anchor Niu–Spivak Rmk 3.78; novelty ORTHOGONAL to DUV 2509.25879.
- ×,+ cells: standard cartesian/cocartesian (co)monoid facts; the ×-monoid empty-positions constraint is a container-specific refinement worth stating.

## TODO
- PROVE: upgrade the ⊗-monoid characterization from `computed` to `proved` (analytic proof of the oplax
  characterization; brute force is only ≤3).
- WRITE: this table as a containers-chapter section; work out the ◁-monoid representable lifting.
- Note for Neil (uid 66): introduce DCont in the monads/comonads chapter, forward-ref from here.
