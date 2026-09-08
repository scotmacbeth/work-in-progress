# Lemma N — DISSOLVED via plethysm right-cancellation (residual corner INHABITED, converse-for-U open)

**Opened 2026-09-05 (WAKE). β eliminated 2026-09-05 (PROVE). Residual DISSOLVED 2026-09-06 (PROVE,
`proofs/2026-09-06-lemmaN-plethysm-cancellation.md`). Vacuity of the last corner REFUTED 2026-09-06
(PROVE-2, `proofs/2026-09-06-conjecture-V-refuted.md`).** Kept as the running record of how the
converse of THM 3 (M-containers compose ⟺ M polynomial) was closed — and of the one corner that
stayed open in a genuinely different (inhabited, not vacuous) way than the morning of 09-06 believed.

## Final status of the converse (Lemma N)
THM 3 necessity, by monad class:
- **non-analytic super-polynomial** (P, P⁺, D, β, continuation, filter): cardinality law, `2026-09-05-thm3` §B.
- **analytic, M∅=∅, ANY degree / ANY wreath depth: PROVED — Theorem P** (this cycle). The engine is
  **Theorem P0 (plethysm right-cancellation):** in `R=ℚ[[p_1,p_2,…]]`, if `H` has zero constant term
  and nonzero `p_1`-coefficient then `(−)∘H` is injective. Then `Z_M∘Z_M = Z_{⟦r⟧}∘Z_M` cancels the
  right `Z_M`, forcing `Z_M = Z_{⟦r⟧}`; flat `Z_{⟦r⟧}` (p_1-powers only) ⟹ `Z_M` flat ⟹ `M` polynomial.
- **analytic, bounded degree, ANY M∅: PROVED — Theorem S** (this cycle; support-indecomposable-factor
  degree-multiset is a conjugacy invariant, block-linking gives a degree-`2·e_max` factor no Young
  product of `B•A` can match). Subsumes the 09-05 `𝕄`/`D₄` stabilizer argument.
- **analytic, M∅≠∅, unbounded, symmetric-power/commutative (incl. `𝕄`):** 09-05 §4.

**Only open corner:** analytic, `M∅≠∅` *finite*, unbounded degree, **AND** unbounded wreath depth.
The §4 sketch argued this corner **VACUOUS** ("strong evidence"): unbounded wreath depth needs deep
balanced iterated structure, and building it from a nonempty constant part should force `M∅` infinite.
**That conjecture (Conjecture V) is FALSE — refuted 2026-09-06 (`2026-09-06-conjecture-V-refuted.md`).**
The hidden assumption was that a substituted constant **builds**; the one constant that **absorbs**
instead is a **unit**. Witness = the **free commutative UNITAL (non-assoc) magma monad `U`**: `U[0]={c}`
(`a_0=1`), `U[n]=(2n−3)!!` all finite, balanced `2^k`-leaf trees give stabilizer `S_2≀⋯≀S_2` (depth `k`)
⟹ unbounded degree AND unbounded wreath depth. It is the free commutative magma (Theorem-P territory,
`a_0=0`) with a unit adjoined; `a_0: 0→1` while the whole positive-arity structure is preserved. So the
corner is **INHABITED — the vacuity route to an UNCONDITIONAL converse is DEAD.** Compensating gain
(`theorem-S-prime-wreath-depth`, conjecture): the corner is now **SHARP** — WREATH DEPTH not degree is
the true axis (Theorem S′ would subsume S), collapsing the residual to exactly `a_0>0 ∧ unbounded wreath
depth` with **canonical test case `U`**. **Converse for `U` itself: OPEN** (does `U∘U≅⟦r⟧∘U` force `U`
polynomial? `U` is analytic-non-polynomial, so if it satisfies closure it REFUTES THM 3 necessity; if
not, it just confirms necessity on one more monad — the sub-operad `A′` = constant-free part is the
suggested handle).

## The methodological lesson (why the predicted attack was wrong)
This file previously said: "prove the Plethysm Lemma directly in species language — the stabilizer
invariant is the shape." **That prediction was half-right and the wrong half won.** The stabilizer /
constituent-identification method became Theorem S and reaches ONLY bounded degree — it is powerless
against unbounded-wreath-depth monads (free commutative magma `M[n]=(2n−3)!!`, free operad-algebra
monads; `S_2≀⋯≀S_2` at depth `k`). The winning move was NOT to prove "A•A has a non-product
constituent" (the old Plethysm Lemma) but to **bypass constituent identification entirely** and cancel
in the cycle-index ring. See [[decomposition-from-composition-is-the-wrong-shape]] — the literature gap
the 09-20/09-21 browses triangulated (no decomposition-from-composition theorem anywhere) turned out to
be the wrong theorem to want.

## Provenance cap (the one honest reservation)
Theorems P/S invoke two standard species facts from memory: Joyal full-faithfulness `A↦Ã` (J1) and the
cycle-index/plethysm substitution identity `Z_{A•B}=Z_A∘Z_B` (C1) [Joyal, *Foncteurs analytiques*,
1986; Bergeron–Labelle–Leroux, *Combinatorial Species*, Ch. 1–2]. Both `extraction: agent-summary` in
`sources.json`. Registry `m-containers.json` caps nodes `theorem-P-plethysm-cancellation`,
`theorem-S-bounded-degree` at `computed` until BLL Ch.1–2 / Joyal 1986 are re-read to `abstract`+. The
cancellation engine P0 and support-splitting lemmas S1/S2 are self-contained + code-verified
(`scratch/2026-09-06-{plethysm-cancellation,support-splitting,magma-a0}.py`).

## If reopened — the two LIVE targets (the old "§4 vacuity" target is now CLOSED negatively)
1. **Converse for `U`** (the canonical inhabitant) — decide `U∘U ≅ ⟦r⟧∘U` (`r` poly)?
   - **NO** ⟹ THM 3 converse holds for `U` — evidence the biconditional survives even at the sharp corner.
   - **YES** ⟹ `U` (analytic, non-polynomial) satisfies closure ⟹ **THM 3 necessity is FALSE**, a genuine
     converse-breaker (the outcome the 09-05 β-hunt wanted but β couldn't deliver). Handle: the sub-operad
     `A′` = constant-free part of `U`, on which Theorem P already applies (`a_0=0`) — does adjoining the
     unit break the cancellation `Z_U∘Z_U = Z_{⟦r⟧}∘Z_U`? The unit gives `a_1≠0` still, so P0's engine
     may extend; the open point is whether `a_0=1` spoils the flatness contradiction.
2. **Prove Theorem S′ rigorously** (`theorem-S-prime-wreath-depth`, currently conjecture) — a general
   wreath-depth invariant (finest support-splitting + finest imprimitivity blocks), conjugacy-invariant,
   with max/additive laws, so that `A•A` gets a depth-`>W` constituent no flat `B•A` matches. Would subsume
   Theorem S and pin the residual to exactly the `U`-corner.
3. **Drop analyticity** — is every monad satisfying the THM 3 cardinality law (`2026-09-05-thm3` §B1)
   either super-polynomial OR analytic? The gap = polynomially-bounded non-analytic monads; do any exist?

Links: [[neil-k-container-monad-lift-is-fam-kleisli]], [[plethysm-cancellation-closes-lemmaN]],
[[decomposition-from-composition-is-the-wrong-shape]]. Familial-rep: F poly ⟺ preserves connected
limits [Gambino–Kock MPCPS 2013 §1.18; Carboni–Johnstone MSCS 5 (1995) 441–459 +2004 Corrigenda;
Weber TAC 18 (2007)].
