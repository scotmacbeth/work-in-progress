# Fibrational framing of the container monad/comonad liftings — precision audit

**2026-08-05, research-agent note (dispatched by MacBeth) — feeds Neil's 08-05 fibrational
steer, the PROVE session, and book Ch7.** Labels: SOLID / NEEDS-PROOF / OPEN / CITE.

Source files: `proofs/2026-07-25-monad-comonad-transfer.md`,
`proofs/2026-07-27-monad-comonad-entwining.md`,
`scratch/2026-07-14-fibrational-containers-derivation.md`,
`memory/reading/2026-07-14-fibrational-containers.md`.

## 1. The fibration — SOLID / CITE
- Projection `p:Cont→Set`, `(S,P)↦S` (shape-forgetting), `(u,f)↦u`. Via `Cont≅∫_{S}(Set/S)^op`.
- Fibre over `S` = `(Set^op)^S≅(Set/S)^op`; vertical morphisms = families of **backward** maps
  `{Q s→P s}`. The **fibrewise op = position-contravariance**.
- Cartesian morphism `(u,f):(S,P)→(T,Q)` ⟺ backward `f` iso, i.e. `P≅Q∘u`. Cartesian lift of
  `(T,Q)` along `u` = `(S,Q∘u)`. Reindexing `u^*(T,Q)=(S,Q∘u)` = **precompose position family**.
  `p` is a split fibration, in fact a bifibration (base LCC ⟹ Σ⊣u^*⊣Π).
- **CITE:** von Glehn TAC 33 (2018) no.36 (`Cont(q)=Σ_q(q^op)`); Streicher *Fibered Categories à
  la Bénabou* Ch.5–6 (fibrewise-opposite; "don't dualize the total category" trap);
  Spivak 1908.02202 (`Lens_F=Gr(F^p)`). **Claim none of the fibration itself.**

## 2. `T_M` lies over `M` — SOLID + one NEEDS-PROOF
- `p∘T_M=M∘p` strictly; unit/mult cover `η^M,μ^M`. **SOLID.**
- **Right word:** `T_M` is NOT a "fibred monad" (that = vertical, covers `id`). Correct: `p:(Cont,
  T_M)→(Set,M)` is a **strict monad morphism / monad opfunctor** (Street 1972) = **a lifting of the
  base monad `M` along `p`** (monad in `Fib` over an arbitrary base functor). Reserve "fibred monad"
  for `G_M`.
- **Cartesianness (load-bearing):** `T_M` preserves cartesian morphisms **⟺ `M` is a cartesian
  monad** (η,μ naturality squares are pullbacks; leaves relabel bijectively, no merging).
  Maybe/writer/reader/free cartesian ⟹ `T_M` cartesian; **`Pf` NOT cartesian** (`μ=∪` merges leaves)
  ⟹ `T_{Pf}` fails — SAME union-vs-product phenomenon as the branching obstruction. Forward
  direction SOLID for the ∏-Mendler class; full biconditional + placement of **List (only *weakly*
  cartesian)** and **state (unclear)** = NEEDS-PROOF (= the prove target boundary cases).

## 3. `G_M` is a vertical fibred comonad — SOLID (proved + Lean)
- Vertical: `p∘G_M=p`. Fibrewise `G_M=(M^op)_*` = pushforward along `M^op:Set^op→Set^op`.
- `M` monad on Set ⟺ `M^op` comonad on Set^op ⟹ `G_M` comonad, counit=`η`/comult=`μ` read in
  Set^op; three comonad laws = `M`'s three monad laws through the fibre-op. (Machine-checked,
  `lean-monad-comonad-transfer-done`.)
- **Genuinely fibred:** `u^*G_T=G_S u^*` (both `Q↦M∘Q∘u`); `ε,δ` reindexing-stable; `G_M` preserves
  cartesian morphisms **for every `M`** (Fubini, no hypothesis). So `G_M` = a **cartesian vertical
  fibred comonad = comonad in `Fib(Set)` (strict Jacobs sense)**.
- **Asymmetry:** `G_M` cartesian ∀M; `T_M` cartesian only for cartesian `M`. All branching fragility
  is on the `T_M`/shapes side, none on `G_M`/positions.

## 4. `λ` as Beck–Chevalley — SOFTEN the claim
- `λ:T_M G_M⇒G_M T_M` exists ∀M (backward = oplax product-comparison `str:M(∏Z_b)→∏M(Z_b)`).
- `P^⋆(m)=∏_b P(x_b)` is a fibrewise `Π`-pushforward along `lv(m)→1`; `str` = the **BC mate**
  measuring whether `M` commutes with that `Π`. So `λ` is a **genuine but oplax (non-invertible) BC
  mate**. Strict BC (mate iso) ⟺ `M` preserves those products ⟺ `M` cartesian ⟺ `T_M` cartesian ⟺
  **non-branching**; fails exactly for `Pf`.
- **Book fix:** rephrase "λ *is* Beck–Chevalley" → "λ is the (oplax, generally non-invertible) BC
  mate; strict BC ⟺ `M` cartesian ⟺ non-branching." The interesting content is the *failure*.

## 5. What the fibration BUYS — mixed, honest
**Load-bearing (SOLID):**
1. `G_M` vertical+cartesian+reindexing-stable ⟹ "fibred comonad ⟹ comonad on total cat, laws =
   fibrewise laws" — *why* each comonad law = the same-named monad law of `M` at fibre `(1,A)`.
2. E1/E3/E4 come cheaply (only `η,μ` naturality = `ε,δ` reindexing-stable = `G_M` fibred).
3. **Crown:** cartesian-morphism preservation is THE hinge — `T_M` cartesian ⟺ `M` cartesian ⟺
   strict BC ⟺ branching vanishes ⟺ reverse orientation `G_MT_M⇒T_MG_M` exists. **"Containers
   preserve cartesian morphisms" = "M non-branching" = "strict BC"** — the payoff / book+grant line.

**NOT delivered (honest limits):**
4. **E2 (mult-T) is NOT free** — touches `T_M`'s fibre multiplication `j` (Ahman–Bauer `⋆`, extra
   algebra), not forced by `p`. Cartesianness of `T_M` alone does not hand E2; general symbolic
   chase stays open. Fibration organizes + cheapens, does not eliminate the hard axiom / obstruction.

**Verdict:** load-bearing, not mere repackaging; real bite = (a) collapse `G_M`→fibrewise M-laws,
(b) cartesian-preservation = non-branching = strict BC.

## PROVE-SESSION TARGET (NEEDS-PROOF, high value)
> `T_M` preserves cartesian morphisms ⟺ `M` cartesian monad ⟺ `λ` invertible (strict BC) ⟺ both
> entwining orientations hold ⟺ no branching obstruction.
Anchors: `Pf` non-cartesian ⟹ reverse E2 fails (computed); Maybe/writer/reader/free cartesian ⟹
both orientations. **Boundary probes: List (weakly cartesian), state (unclear)** — pins whether the
equivalence is with *cartesian* or *weakly cartesian* monads.

## 6. Ownership / scoop — CITE, do not CLAIM the framing
- **Fibred (co)monad, Σ/Π, BC:** Jacobs, *Categorical Logic and Type Theory* (1999) — use for `G_M`.
- **Monad lifting / monad-morphism `T_M→M`:** Street, *Formal theory of monads* (1972); fibred
  logical-predicate liftings: **Hermida** PhD (1993), **Katsumata** (⊤⊤-lifting) — "lift a base monad
  to a monad on the total cat, cartesian over it" is standard. Do NOT claim "lifting a monad to Cont".
- **(Weakly) cartesian / polynomial monads, leaf machinery:** Weber, Gambino–Kock, Zawadowski.
- **`T_M` itself:** Ahman–Bauer 2409.17664 Thm 6.3 (∏-cointerpretation); Ahman–Uustalu Update Monads.
- **Entwining / mixed DL:** Beck 1969; Power–Watanabe; Brzeziński–Majid.
- **`G_M`:** MacBeth's (folklore-instance; contribution = coordinate proof + coclosure/Lan id).

**Scoop verdict:** no scoop on `G_M`/entwining as results. The fibrational repackaging = standard
2-categorical tech = **framing to CITE, not a result to claim**. Claimable novelty: (i) two feeds of
one `M` entwine; (ii) `str` is the law; (iii) one-directionality + branching obstruction; (iv) the
proposed **cartesian-preservation = non-branching = strict-BC** equivalence (the new theorem).
