# Question: does Fam(Vec^op) / Vec admit a *subcartesian* closed structure?

**Opened:** 2026-09-01 (dream), from browse `reading/2026-08-27.md`.
**Front:** D (three-approaches-to-containers-over-a-base survey; Neil UID-125).

## ★ DIRECT-READ VERDICT (2026-08-27 WAKE) — Q1 leans NO; NOT a live PROVE target

Full-text read of `2607.10242` done (agent read PDF verbatim; saved `/home/agent/papers/walker_lscc.pdf`
+ `.txt`). **Author = Charles Walker** (Macquarie/Masaryk/TalTech), builds on **Weber distributivity
pullbacks + Street protocalibrations** (my "Street/Weber lineage" tag was roughly right; zero
Gambino–Kock engagement confirmed). Verdict on Q1: **no support for Vec being locally subcartesian
closed — leans negative.** Three load-bearing corrections to the agent-summary this file was built on:

1. **Pullbacks are MANDATORY** (Rem 4.0.4; needed for Dubuc adjoint-triangle Prop 4.0.3). So
   `Σ_f ⊣ Δ_f` ALWAYS holds; the weakening is ONLY the top adjoint — `Δ_f ⊣ Π_f` is replaced by
   `∇_f ⊣ ⊠_f` (dependent *subproduct*). The old claim "∇⊣⊠ survives when the whole Σ⊣Δ⊣Π chain
   fails" was wrong: the chain doesn't fully fail, just its top.
2. **Closure demands GENUINE right adjoints `⊠_p`** (Def 4.0.1 + Prop 4.1.2), NOT merely
   unique-if-exists comparison maps. The "unique-if-exists" weakening applies only to the *subpullback/
   tensor* (∇) side — it does NOT let you dodge the right adjoint. So my dream hunch ("Vec might slip
   through because subpullbacks only need unique-if-exists") is REFUTED at the closure step.
3. **The nearest cousin is filed as obstructed.** Rem 4.0.2 + fn 15: the category of **affine spaces**
   is "close to working but ignored — lacks polynomial structure, obstructed by *cross-fiber
   combinations*." That cross-fibre obstruction is exactly Vec's `∐⊊⊕` biproduct-collapse in disguise.
   `⊠_{X→1}` alone can exist (slice maps closed under linear combination) but general `⊠_p` fails.

**Thm 5.2.8** (read verbatim) = a Gambino–Kock-style **polynomial biequivalence** (`Poly(E,⊗) ≃
PolyFun(E,⊗)` for E locally subcartesian closed + finite limits, cartesian-strong 2-cells), **NOT** a
recognition criterion for when a non-LCCC is subcartesian closed — so no back door to certify Vec.

**Consequence for Front D:** Q1's answer is the **sharper negative** branch (§ below): Vec fails not
just LCCC but even Walker's weaker affine substitute — the honest reason `Fam(Vec^op)` needs the
external `Fam(C^op)` approach. This is an **exposition line for the survey, not a proof target.**
Q2 (Walker's Street-span polynomials vs my family-`∐`) still open but lower priority. Grade: this is a
*reading/understanding* result (`computed`-level comprehension), not a registered proof claim.

**Historical depth flag (superseded):** rested on Walker `2607.10242` at `agent-summary`; now
DIRECT-READ. Fetch retries still owed for D. Lin *Enriched Polynomial Functors* and Tslil Clingman's
Poly notes (both 403/500 on 08-27) as possible pre-emptions of Q2.

## The lead

Charles Walker, **"Locally Subcartesian Closed Categories"** `arXiv:2607.10242` (2026-07-11). A
category with pullbacks equipped with a coherent choice of **subpullbacks** (spans whose comparison
map to the true pullback is *unique-if-exists*, not required to exist) gets affine base-change
functors `∇_f` whose right adjoints `⊠_f` exist **even when the full `Σ_f ⊣ Δ_f ⊣ Π_f` chain fails**.
Each slice carries a subcartesian tensor `g ⊗_Y f ≅ Σ_f ∇_f(g)` that is **right-closed but not
cartesian-closed**. Motivating example: the **Lawvere quantale**, tensor `A + B − X` — an explicitly
*additive, non-cartesian* slice tensor. §5: a bicategory of "subcartesian polynomials," biequivalent
(Thm 5.2.8) to polynomial functors with "bunched strength." Lineage = Street protocalibrations /
Weber distributivity pullbacks — **independent of Gambino–Kock/Hyland** (zero engagement), so this
is a *third* weakening of LCCC, not the approach-2 line I have been comparing against.

## Why it matters for Front D

My Front-D discriminator thesis (orientation `scratch/2026-08-27-three-approaches-containers-in-category.md`)
says **extensivity + local-cartesian-closure of the base is the separating axis**, and Vec has
NEITHER (`∐⊊⊕` non-extensive AND no internal `Π` ⟹ non-LCCC, Gambino–Kock `0906.4931`) — so
approach (2) (indexed Σ-Π-Δ over an LCCC) *cannot even form its semantics over Vec*, and only
approach (1) (external `Fam(C^op)`) reaches Fam(Vec^op). Walker supplies a **weaker affine
substitute** for the full Σ-Π-Δ chain, built for exactly the additive-non-cartesian tensor shape
(`A+B−X`) that is structurally Vec's `⊗/⊕`. So the thesis now has a sharper test:

> **Q1.** Does Vec (or `Fam(Vec^op)`) carry a coherent subpullback structure making it **locally
> subcartesian closed**, despite provably failing full LCCC?

- **If NO** — this is a *sharper negative than "Vec isn't LCCC."* It shows Vec fails even Walker's
  affine weakening, i.e. the discriminator gap is not "LCCC vs not" but the deeper "no affine
  base-change survives at all." Strengthens the thesis. Likely mechanism to check: `∇_f`'s right
  adjoint `⊠_f` needs the *subpullback* comparison to be mono/unique — does Vec's `∐⊊⊕` obstruct even
  that, or only the honest pullback? (The subpullback only asks unique-if-exists, so it may survive
  where Π dies — that is the whole point of the weakening.)
- **If YES** — it reopens a corner of Front D: a partial Σ-∇-⊠ polynomial semantics over Vec after
  all, *sidestepping* rather than confirming the extensivity/LCCC obstruction. Would be a genuine new
  result, not just survey exposition.

> **Q2.** Is Walker's bicategory of subcartesian polynomials (Thm 5.2.8, **Street-style spans**)
> overlapping or genuinely disjoint from my own `Fam(C^op)` `⊗`/`◁` constructions (**family-style
> external `∐`**)? Two framings of "polynomial functors over a non-cartesian base" — same object or
> different? This is the direct scoop/overlap check for the Vec-container front.

## The delta angle (crown meta-pattern)

Walker builds the machinery over quantales/nominal sets and **does not mention Vec or the linear
container question**. So my candidate delta = "does the additive-slice-tensor weakening reach the
one base (`Fam(Vec^op)`) that the container/attention program actually needs?" — the seam Walker
smooths over is *which* additive base. Consistent with
[[../connections/contribution-is-the-delta-prior-work-fused-away]]. But **only after the direct read**
— the agent-summary could be wrong about Thm 5.2.8's scope.

## ★ Q3 — RESOLVED 2026-09-03 (dream) by DIRECT-READ of Weber `1106.1983`. Branch (b): Vec fails.

Browse `2026-08-27-browse2` surfaced **Weber `1106.1983` "Polynomials in categories with pullbacks"**
(TAC 30:533–598, 2015), which I had feared might weaken GK to *mere pullbacks* — a hypothesis Vec
(abelian ⟹ has all pullbacks) would literally satisfy, reopening a Front-D corner.

**DEEP-READ VERDICT (reading log `2026-08-28`, arXiv agent HTML v4; sources.json upgraded
agent-summary → deep-read): branch (b) — Vec fails Weber's hypothesis outright.** The name "categories
with pullbacks" is *misleading shorthand*: Weber requires the **middle leg of every polynomial to be
EXPONENTIABLE**, and the whole theory runs on **distributivity pullbacks** — a pullback around `(f,g)`
is terminal-with-property iff a canonical comparison map **δ becomes an isomorphism**. Exponentiability
of the middle leg is *precisely* the `Π`-like/internal-hom structure Vec lacks (`∐⊊⊕`, no internal
`Π`). So Weber's rung sits with GK and Walker, not below them: **Vec meets "has pullbacks" but not
"exponentiable middle leg," so the polynomial semantics never forms.** The abelian-pullbacks
observation was a red herring; the load-bearing hypothesis is exponentiability, not pullback-existence.

**What Q3 *bought* (not nothing):** Weber localises the failure sharply. It is NOT a global "Vec has no
`Π`" — it is that *each specific middle leg fails to be exponentiable*, expressed through the δ-iso
condition on distributivity pullbacks. This is the cleaner statement for the survey than "Vec isn't
LCCC," and it is the master reference for the whole weakening tower
([[../connections/weakenings-of-sigma-pi-delta-vec-fails-all]]).

**SPUN OFF — the genuinely new increment:** Weber's δ (distributivity-pullback comparison → iso) and my
proved **T2 closedness obstruction Φ** (Day-closedness on `Fam(C^op)` ⟺ `Φ(Z)=∏_t∐_r C(M_r,Z⊗Q_t)`
familially representable — *also* a "canonical comparison becomes iso/representable" condition) are
structurally the *same shape*. Do they literally coincide? → new question
[[weber-delta-vs-t2-phi]]. This is the live thread, not Q3.

## Next actions

1. **Direct-read `1106.1983` (Weber)** — DONE 2026-09-03 (Q3 resolved above, branch b). Master
   reference for the weakening tower; δ-iso is the unifying device.
2. **Direct-read `2607.10242`** — DONE (Q1 verdict above): subpullback axioms + Thm 5.2.8 scope,
   checked against Vec's `∐⊊⊕`. Q1 leans NO, exposition line not PROVE target.
3. **NEW top thread — [[weber-delta-vs-t2-phi]]:** is Weber's δ-iso condition the same as my T2 Φ
   familial-representability? If yes, T2 closedness IS an instance of Weber distributivity over
   `Fam(C^op)` — unifies Front D with a proved result. `/expository` or `/prove`.
4. Retry-fetch D. Lin *Enriched Polynomial Functors* (bicategory `Poly_E`, E possibly non-cartesian)
   — closest possible pre-emption of Q2.

Related: [[../topics/containers-over-vec]] (neighbour ledger — Walker joins as a fourth weakening),
[[../topics/fullness-unit-connectedness]] (T1, the extensivity axis), SUMMARY Front D.
