# Orientation — Logic of containers: Cont(cod) as a fibration of predicates over positions

**Source:** Neil UID-132 (2026-08-27 reply). Ask: turn `cod : Set^→ → Set` into a *logic of
containers*; concretely, apply `Cont` to a fibration to get `Cont(Set^→) → Cont(Set)` as a fibration,
where `Cont C = Fam(C^op)`.

**Status of the facts below:** all verified at `computed`/folklore level by a research agent
(2026-08-28 WAKE), cross-checked against standard sources. NOT yet written as a rigorous proof — that
is the PROVE target. Nothing here is `proved` yet.

## The construction (verified)

1. **`Cont(−) = Fam((−)^op)` is functorial.** `Fam` is the free-coproduct 2-monad (Carboni–Lack–Walters
   JPAA 1993; nLab free coproduct completion); `(−)^op` is a 2-functor. So `G:C→D` induces
   `Cont(G)=Fam(G^op):Fam(C^op)→Fam(D^op)`, `(S,{P_s})↦(S,{G P_s})`. In particular `cod` induces
   `Cont(cod)=Fam(cod^op)`.

2. **`cod : Set^→ → Set` is a BIFIBRATION.** Streicher's fundamental fibration: always an opfibration
   (opcartesian lift = post-composition = `Σ_β`); a fibration iff base has pullbacks (cartesian lift =
   pullback `β*`). `Set` has pullbacks ⟹ bifibration. (Jacobs CLTT §1.1/1.4; Streicher fibrations notes.)

3. **op of a fibration = opfibration; op of a bifibration = bifibration.** So
   `cod^op : (Set^→)^op → Set^op` is a bifibration, in particular a fibration.
   Cross-check: `(Set^→)^op ≅ (Set^op)^→`, under which `cod` becomes `dom`, and `dom` is a fibration
   over ANY base (cartesian lift = composition). Independent confirmation.

4. **KEY LEMMA — Fam preserves fibrations.** If `p:E→B` is a fibration then `Fam(p):Fam(E)→Fam(B)` is
   a fibration (in fact iff `p` is). **Cartesian lift:** given target `(J,{e'_j})` and base morphism
   `(u,{ψ_i : b_i → p e'_{u(i)}})`, take `(u,{χ_i})` where `χ_i` is the `p`-cartesian lift of `ψ_i`; it
   is cartesian in `Fam(p)` (test morphism factors uniquely, componentwise, using each `χ_i` cartesian
   + disjointness of Set-coproducts). Folklore; cite Hermida (PhD 1993) / Jacobs CLTT Ch.1. **This is
   the load-bearing fact — write the proof in full.**

**Chaining (1)+(2)+(3)+(4):** `Cont(cod)=Fam(cod^op) : Cont(Set^→) → Cont(Set)` **is a fibration** =
"apply Cont to a fibration → a fibration of containers over containers." ∎ (modulo writing 4 rigorously)

## The logic (the payoff)

- **Objects of `Cont(Set^→)`:** `(S, {f_s : A_s → B_s}_s)`. `Cont(cod)` sends it to the container
  `(S,{B_s})`.
- **Fibre over a container `(S,{P_s})`:** `∏_{s∈S} (Set/P_s)^op`. An object = for each shape `s` and
  position `p∈P_s` a set `A_{s,p}` = a **proof-relevant predicate on positions**.
- **⚠ Fibrewise op:** the fibre is `(Set/P_s)^op`, NOT `Set/P_s` — vertical hom-direction DUALISED.
  This is von Glehn's fibrewise contravariance (`Cont = ∫_Set cod^op`, TAC 33 2018; my memory
  [[contravariance-is-fibrewise-op]]). The logic of containers is a **dualised** predicate logic — the
  interesting wrinkle.
- **Reindexing + quantifiers:** container morphism `(u:S→S', {ρ_s : P'_{u(s)} → P_s})`; reindexing is
  componentwise base-change along `ρ_s`. `Set` LCCC ⟹ each fibre carries `Σ_ρ ⊣ ρ* ⊣ Π_ρ`
  (Exists ⊣ reindex ⊣ All). **These are EXACTLY the A/E = ∏/Σ predicate liftings** (my proved UID-94
  result [[neil-A-E-predicate-liftings-proved]]), now identified as the fibred quantifiers of
  `Cont(cod)`; the fibrewise op swaps which is left/right. Loop closed: the liftings ARE the quantifiers.

## Prior art (frame the delta; do NOT re-claim)

- **von Glehn, TAC 33 (2018) / PhD Cambridge 2015** — `Cont = ∫_Set cod^op`, fibrewise-op. THE ancestor.
  Cite hardest. My fibre `(Set/P_s)^op` is his contravariance.
- **Aberlé 2604.01303** (*Compositional Program Verification with Polynomial Functors in DTT*, CMU,
  Apr 2026) — only GESTURES: Def 0.4 remark "a dependent polynomial over `p` = a polynomial functor on
  `Type^→` lying over `p` via `cod`". NO Fam, NO fibration theorem, NO cartesian lift, NO quantifier
  calculus. My result is NOT pre-empted.
- Gambino–Hyland 2004 / Gambino–Kock — dependent polynomials via `cod`/LCCC (`Σ⊣Δ⊣Π`), the standard home.
- Altenkirch–Ghani–Hancock–McBride–Morris, *Indexed Containers* JFP 2015 — indexed containers ARE
  predicates/families over container data; overlaps the "predicate on positions" reading.
- Jacobs CLTT 1999 — codomain/family fibrations, LCCC quantifiers = textbook `∃/∀`.
- Moss–von Glehn, Dialectica models of type theory (LICS 2018) — predicate/proof structure over
  poly-like data; connects to my `⋉/⋊` Dialectica notes.

**Delta:** assemble `Cont(cod)=Fam(cod^op)` EXPLICITLY as the fibration of proof-relevant predicates
over positions, prove it via "Cont preserves fibrations", identify quantifiers with the A/E liftings,
and expose the fibrewise-op dualisation. Same crown meta-pattern: the delta is what von Glehn/Aberlé
gestured at but did not assemble.

## What remains for a real PROVE (the increment beyond folklore)

The structural fibration claim is folklore-assembly. The *logic* content worth proving:
1. Full rigorous proof of "Fam preserves fibrations" (the cartesian-lift lemma) and the chaining.
2. **Beck–Chevalley** for `Cont(cod)`: does BC for `cod`/Set's LCCC lift through `Fam(−^op)`? (The
   fibrewise op means BC squares get dualised — check the direction carefully.)
3. **Frobenius reciprocity** (for `Σ`) and the dual for `Π`, fibrewise, and whether they survive `Fam`.
4. State precisely the DUALISED first-order structure: because fibres are `(Set/P_s)^op`, `Σ`/`Π`
   swap roles — write down what "∃ position" and "∀ position" MEAN in the container logic, and whether
   the resulting hyperdoctrine is the op of a standard one or genuinely new.
5. Proof-relevant vs propositional (subobject) truncation: `Sub(Set^→)` version = strict Lawvere
   hyperdoctrine; proof-relevant version = the full `Set/P_s` fibres. (Asked Neil which he wants,
   UID-132 reply; instinct = proof-relevant, truncation as corollary.)
6. Generality: "Cont preserves fibrations" as a functor `Fib(B) → Fib(Cont B)`? i.e. is Cont a
   morphism of the 2-category of fibrations? That's the clean general statement.

## Registry
New node. Builds on `neil-A-E-predicate-liftings-proved` (proved) and the memory
[[contravariance-is-fibrewise-op]]. Lives near Front D (fibrational leg, approach 3).
