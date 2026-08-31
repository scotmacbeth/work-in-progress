# Q: Does Workers `ΔS`-grading generalize to BHM's `T_P(X)=X▷P`? — RESOLVED 2026-08-29: NO (different products; retract not fibre)

**Opened:** 2026-08-28 browse2 consolidation. **RESOLVED 2026-08-29 (`computed`),
sub-question 1 answered NEGATIVE.**

## VERDICT (2026-08-29)
The cheap `X▷ΔS` check (below) settles it: **NOT a fibre.** Workers grades by the
Dirichlet tensor `⊗`, BHM by the composition product `▷` — different products. At
`|S|=|T|=2`, `ΔS▷ΔT = 8·y⁴` (shapes `|S|·|T|^|S|`) ≠ `ΔS⊗ΔT = Δ(S×T) = 4·y⁴`
(shapes `|S×T|`). `⊗` is a canonical **retract** (diagonal collapse) of `▷`, not a
fibre. Sub-question 1's parenthetical was the crux: the `ΔS⊗ΔT=Δ(S×T)`
multiplicativity is EXTRA structure `⊗` has that `▷` does NOT share. Working
`scratch/2026-08-29-workers-bhm-triangle-vs-dirichlet.md`; connection file updated;
[[../connections/workers-grading-is-fibre-of-bhm-polynomial-grading]].
**Sub-question 2 RESOLVED 2026-08-30 (PROVE, `proved`): NO — see below; sub-question 3
still fully open.** (3) the three-products picture — Snoc (free ℕ), BHM (▷), Workers (⊗): is there one object
over `(Poly,▷)` whose ⊗-diagonal retract is Workers and whose free-graded quotient
is Snoc? Raised with Neil 2026-08-29 daily; candidate `/prove` or `/expository`.

---
*Original framing (superseded — conjecture refuted):*

## Statement
Braithwaite–Hedges–Mihejevs (ACT 2026, deep-read) model Poly's composition
product as a noncommutative graded monad `T_P(X)=X▷P` graded by an arbitrary
polynomial `P`. My proved Workers result is a `(Set,×)`-graded category via `ΔS`.
Conjecture: **Workers = the `P=ΔS`-representable fibre** of `T_P`. See
[[../connections/workers-grading-is-fibre-of-bhm-polynomial-grading]].

## Sub-questions
1. Verify `P=ΔS` specialization explicitly (write `X▷ΔS` and compare to the store
   grading). Does `ΔS⊗ΔT=Δ(S×T)` multiplicativity come for free, or is it extra
   structure Workers has that general `P` lacks?
2. Is BHM's "`▷` not fibred in its left variable" literally the T4-left tininess
   collapse ([[t4-left-closedness-lhd-famcop]])? Both say `◁` misbehaves in the
   left variable, repaired only at representability/tininess.
3. Three-way unification: Snoc (free `ℕ`-graded monad, Ghani et al. Thm 3.5),
   BHM (`P`-graded), Workers (`ΔS`). Fibres of one thing? Neil's own paper is in
   the frame — worth raising with him directly.

## Why not urgent
If it checks out, the generality is THEIRS — I cite, not claim. Value is
(a) a clean citable home for Workers inside a published Poly-language line, and
(b) possible confirmation that T4-left's obstruction is the "standard" one. Both
are consolidation wins, not new theorems. Do the cheap `P=ΔS` check first before
committing a `/prove` session.

## Decision procedure (cheap first step)
Write `X▷ΔS` for the store polynomial `ΔS=S·y^S` and read off the grading monoid;
compare to Workers' `(Set,×)` grading. One page. If it matches → cite in the next
orchestration/Workers `/write`. If it diverges → there's a real delta and it
becomes a `/prove` target.


---

## SUB-Q2 — **RESOLVED 2026-08-30 (PROVE). Grade: `proved`. Answer: NO.**

`proofs/2026-08-30-fibredness-vs-left-closure.md` · registry `fibredness-vs-left-closure.json`
(validates) · `scratch/fibredness-vs-closure/verify.py` (6 checks green) ·
[[bhm-fibredness-vs-t4-left-separable]].

Shape fibration `π:Fam(C^op)→Set`, `π(S,P)=S`. For `L_q=(−)◁q`: **(V)** vertical, **(F)** fibred,
**(C)** right adjoint exists.
- **Thm A (Set):** `(V)⟺(F)⟺(C)⟺|T|=1`.
- **Thm B (Vec_fd):** `(F)` always; `(V)⟺|T|=1`; `(C)⟺#{t:Q_t≠0}` finite ⟹ **`(V)⊊(C)⊊(F)`**
  strictly. `q=(2,k)` closed-not-vertical; `q=(ℕ,k)` **fibred-not-closed**. Two-sided ⟹ the answer
  does not depend on which notion of "fibred" PP26 meant.
- **Cited background, NOT a bonus finding** (*attribution corrected 2026-08-31*): `◁` **is** fibred
  in its **right** variable ∀q with base functor literally `⟦q⟧` — this is **Pradic–Price
  `2601.15420` Lemma 15** (p. 14, proof p. 31), *with the same base functor*; and both variables
  preserve cartesian morphisms unconditionally — this is **Niu–Spivak `2312.00990` Prop 6.88**
  (p. 213), which PP themselves cite. **Neither is mine.** What is mine is the *observation* that
  the two together **isolate** the failure: non-fibredness is *only* base-functoriality, never
  cartesianness — an observation about known facts, not a new theorem.
- **Diagnosis:** fibredness = the shape object **collapses**; closure = collapse **+ summability in
  the base**. Same test (`G_r` familially representable) at the **shape probe** vs the **position
  probe**.
- **Still open:** "closed ⟹ fibred" over an arbitrary base. **The PP `2601.15420` attribution is
  CLOSED (2026-08-30) and it closed AGAINST me** — the paper is on disk and was read; their `shape`
  fibration *is* my `π`, their Def 13.1 is my (F) with strict equality (so PP-fibred ⟹ (F), and
  Thm A refutes a fortiori). **What survives as mine: Corollary A′** — Theorem A supplies a *proof*
  of their **Remark 16** (p. 14), which they assert with none — **and Theorem B**, outside their
  scope entirely (standing hypothesis p. 7: *"all categories in sight shall be lextensive"*;
  `Vec_fd` is not). ★ That hypothesis is direct **corroboration of the extensivity thesis**: prior
  work assumes the very condition under which the seams fuse, so it structurally cannot see the
  separation.

The recon below is preserved as the record of how the target was scoped; its `computed` separator
has now been re-derived by hand and is Corollary B′ of the proof.

---

## SUB-Q2 — scoped 2026-08-30 (WAKE recon agent). Grade: `computed`. NOT yet re-derived by hand.

**Primary source located** (was believed unavailable): `/home/agent/papers/BHM-polylang-ACT2026.pdf`
(+ `.txt` extract; companion `BHM-substructural-ACT2026.*`). It is a **2-page extended
abstract**. The whole BHM claim is one parenthetical clause in §3 (Fixpoints), with no
definition, no proof, no theorem number:

> "Our construction of fixpoints is taken from [GH14]; compare [PP26] which restricts to
> fixpoints of fibred endofunctors, which we are not using because the composition product
> ▷ is not fibred in its left variable."

⟹ **Citable as corroboration, NOT usable as a lemma.** Any identification is mine to define
and prove.

**Findings.**
1. **Variable alignment CONFIRMED** (this was the suspected trap; it is not one). BHM's
   graded monad is `T_P(X)=X▷P`, so their varied "left" variable is `(−)▷P`; my T4-left
   closure is the right adjoint to `(−)◁q`. Same functor.
2. **Different logical shape.** Non-fibredness is *not* a missing adjoint. `(−)◁q` is
   fibred over the shape fibration `Cont(Set)=Fam(Set^op)→Set` iff `π(p◁q)=Σ_s T^{P_s}`
   factors through `π(p)=S`. It fails because the shape set of `p◁q` reads `p`'s
   **positions** — a failure of base-functoriality, not of a cartesian lift, not of an
   adjoint.
3. **One formula causes both:** `Σ_s T^{P_s}`, exponent = left argument's positions.
   Tininess collapses it to `S×T`, which simultaneously restores base-functoriality *and*
   supplies the adjoint. Over `Set` the two boundaries appear to coincide: fibred ⟺
   closed ⟺ `q` monomial (`|T|=1`).
4. **★ CANDIDATE SEPARATOR — the answer is probably NO in general.** Over
   `Fam(Vec_fd^op)` take `T=ℕ`, all `Q_t=k`. Positions tiny ⟹ `◁=⊗` ⟹ shapes `S×T`
   depend only on shapes ⟹ `(−)◁q` **IS fibred** — yet my proved T4-left Thm 3.1(2) says
   the **closure FAILS** there (`⊕_{t∈ℕ}` leaves `Vec_fd`). So **fibred ⇏ closed**, and any
   identification is `Set`-local. Diagnosis: fibredness tests only that the exponent
   **collapses**; closure additionally needs the collapsed coproduct to be **summable in
   the base**. Collapse repairs fibredness but not summability.
5. ~~**UNVERIFIED and load-bearing:**~~ **RESOLVED 2026-08-30 — the reading was RIGHT.**
   BHM's "fibred" is inherited from [PP26] = Pradic–Price `2601.15420`, at the time **not on
   disk**, and the reading that their fibration is the shape fibration rested on
   `sources.json:412` (agent-summary). *The paper has since been fetched and read:* they describe
   it as "exactly the fibrewise opposite of the codomain fibration" (§2.2, pp. 8–9), which is my
   `π`. Finding 2 stands and did not need redoing. (Kept verbatim above as the record of a
   load-bearing gap correctly flagged **before** it was discharged.)

**This is the same moral as δ≟Φ** ([[weber-delta-vs-t2-phi-distinct]]): two
canonical-looking conditions that turn out to constrain **different legs**. Second
occurrence of that pattern — worth noting if it recurs a third time.

**→ `state/PROVE.md` (2026-08-30):** (A) the `Set`-local TFAE fibred ⟺ closed ⟺ monomial;
(B) the `Vec_fd` separation; (C) the collapse-vs-summability diagnosis. Cheapest falsifier
named in the trigger and to be run FIRST, per the 09-05 dream's standing lesson.
