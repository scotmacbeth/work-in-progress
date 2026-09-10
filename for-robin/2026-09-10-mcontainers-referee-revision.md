# M-containers §5 — referee revision pushed (for Robin & Neil; re-review request to Rick)

**MacBeth, 2026-09-10 (write session).**

**Paper (revised):**
`scotmacbeth/work-in-progress@4158115` →
`papers/mcontainers-codensity-polynomiality.pdf`
(stamp commit on page 1 is `4158115`; `84b7c5e` only adds the stamp). 29 pp, compiles clean.

This closes Rick's referee loop on `70becd9` (accept with minor revisions, `proofs/reviews/2026-09-10-m-containers-thm3-arc.md`) — but with one **substantive correction that overrides my own WRITE.md**, so please read the next section before anything else.

---

## ⚠️ WRITE.md was stale — I did NOT fold in the O_{2,C₃} "commutative-μ" result

WRITE.md (written in the 10:09 wake session) told me to fold in
`o2c3-commutative-mu-dividing-line` ("necessity holds ⟹ the dividing line is *commutative binary
composite*, strictly weaker than fully symmetric — headline CORROBORATED") to **strengthen** the paper.

That result rests on a **modeling bug** and was **refuted the same day** by the PROVE session
(`proofs/2026-09-10-commutative-mu-corrected-dividing-line.md`, graded **proved**; and PROVE.md's own
status header now says the seeded "commutative binary composite" target is *false as stated*). The bug:
`o2c3-model.py` forced `ω(x,y,e) := μ` commutative; under genuine C₃, `ω(x,y,e)` is **rigid**. So the
"one escape at m=4" was an artifact.

Folding the refuted claim in would have put a false headline into a refereed paper. I wrote up the
**corrected** mathematics instead — which is a *stronger* outcome than WRITE.md hoped for: a **proved
theorem** on a class strictly larger than the fully symmetric operads, not a re-hedge.

---

## What the revision actually says (the corrected §5.9)

- **New Main Theorem ("escape criterion", Thm 5.22, proved).** For a unital non-flat operad with
  **(i)** every binary composite commutative and **(ii)** no locked-double-swap derived operation on 4
  leaf-slots: `M∘M ≇ ⟦r⟧∘M` for all polynomial `r` (necessity holds). Built from a **Witness Lemma**
  (5.20, needs only a commutative binary composite + a₀≥1) and a **Characterization Proposition** (5.21:
  `Δ_C2 ∈ 𝒮 ⟺ (M1) coexisting rigid + commutative binary composite, or (M2) a locked-swap derived op`).
- **Full symmetry is now a corollary (5.23)** — recovers 𝒰, the corner `U`, the `Uₙ`. The theorem is
  **strictly larger**: the A₄- and V₄-operads satisfy (i)+(ii) but aren't fully symmetric (V₄ even has a
  rigid *ternary* composite yet still escapes).
- **The dividing line is corrected**: NOT "commutativity of μ" but `Δ_C2 ∈ 𝒮`, read off by (M1)∨(M2) ---
  **and only among operads that possess a commutative binary composite** (see the precision note below).
  Refutation table: "has a commutative binary composite" (O_μν, M1), "no rigid binary composite" (pentagon
  D₅, M2), "no rigid tree of any arity" (V₄), "fully symmetric" (A₄,V₄) are each refuted as the line.
- **The two endpoint theorems are UNCHANGED and still correct**: full-symmetry→necessity, and the pure-C₃
  operad→necessity-fails (Thm 5.24). The bug was in the *separate* hybrid O_{2,C₃} (which has an extra
  binary μ), never in the paper's pure-C₃ operad, whose `ω(x,y,e)` genuinely is rigid.
- **Problem 5.23 recast** as the open converse (`Δ_C2∈𝒮 ⟹ image closed`), *within* the commutative-
  binary-composite class; verified `m≤4` for O_μν, open in general.

## Precision fix I made beyond the proof file (please sanity-check)

The proof file's "Reach" section says "(i)+(ii) ⟺ Δ_C2∉𝒮". That equivalence is **not quite right** and I
did **not** put it in the paper. Δ_C2∉𝒮 alone does *not* imply necessity: the pure **C₃ operad has no
commutative binary composite**, so the swap witness can't even be built — and it *composes* (Thm 5.24).
(Indeed C₃ contains no transposition, so plausibly Δ_C2∉𝒮 there too — which would make a naive global
"compose ⟺ Δ_C2∈𝒮" biconditional false, C₃ being the counterexample.) So throughout the paper I scoped
the dividing-line statement to **"among operads with a commutative binary composite"**, where (i)+(ii) ⟺
[commutative binary composite ∧ Δ_C2∉𝒮] genuinely holds. The proved forward theorem (Thm 5.22) is stated
by its exact hypotheses (i)+(ii), so it's airtight regardless.

**TODO for a PROVE session:** confirm Δ_C2∉𝒮 for the pure C₃ operad (no transposition ⟹ no order-2 tree
automorphism). If so, C₃ is a clean counterexample to any *unscoped* "compose ⟺ Δ_C2∈𝒮", worth stating.
The scoped converse remains the target already in PROVE.md.

## Flag 2 surfaced a genuine error (retracted, not patched)

Rick's flag 2 asked me to back the "a₁≠0 is sharp" aside in Lemma 5.17 with an explicit collision at
`H=p₂+½p₁²`. A compute check (exact, kernel 0 in every degree, + clean all-degrees proof) shows **there is
no such collision**: `(−)∘H` is injective for *every non-constant* `H`; right-cancellation collapses only
when `H` is constant. So the sharpness claim was **false**. I **withdrew** it (§5.6) and noted the true
fact (hypothesis sufficient, not necessary). The main theorem (Thm 5.18, cancellation converse) only uses
the sufficient direction at a₁≥1, so it is **unaffected**. Flagged in the Provenance section.

**Possible LEAN/PROVE follow-up:** the stronger "injective for every non-constant H" (via algebraic
independence, unique-top-index) could be formalized to replace the a₁≠0 hypothesis in the P0 engine
(`lean-p0-order-cancellation-engine`). Not urgent.

## Flags 1, 3, 4 (polish, done)
- **Flag 1:** Thm S′ (5.14) witness — spelled out the depth≥1 step (non-flat ⟹ some H_l≠1 ⟹ orbit ≥2 ⟹
  h_t≥1).
- **Flag 3:** added "e is the **unique** nullary" to the fully-symmetric def; addressed Q3 (a₀≥2, 𝔥=∞
  residual is covered by Thm 5.22 whenever Δ_C2∉𝒮; otherwise in the open converse).
- **Flag 4:** added the explicit arity-preserving bijection (unit-completed C₃-trees on `[n]` ↔ lists of
  C₃-trees on set-partitions of `[n]`); surfaced the "positive-arity q" hypothesis (Q2) in Thm 5.24's
  statement.
- Nits: `(see §5.6)` at the first Def-5.14 forward-ref; `\cite[§1]{GambinoKock}` for the "P polynomial
  preserves the connected limit" step in Prop 5.10; the "forces" ambiguity dissolved by dropping the
  "commutative μ forces…" framing.

## Registry / provenance
- No new external citations (all internal; only reused `GambinoKock`). Footprint check clean.
- Registry implication (a WAKE/registry-session job, not this write session): the paper now rests on
  `commutative-mu-corrected-dividing-line` (**proved**); `o2c3-commutative-mu-dividing-line` should be
  marked **refuted/superseded** (memory already reflects this). The 8 §5 THM-3-arc nodes stay
  peer-reviewed; the *characterization + main theorem* is new material Rick has **not** seen.
- **`publishable-result` NOT touched** (per WRITE.md — hold until the converse firms up).

## Ask to Rick (for a future comms session — I did not email this session)
Please re-review the rewritten §5.9 (Lemmas 5.19–5.20, Prop 5.21, Thm 5.22, Cor 5.23, Problem 5.23). It is
new since `70becd9`: it *replaces* the "commutativity of μ is the dividing line" headline you reviewed
with the corrected `Δ_C2∈𝒮` criterion, and it supersedes the O_{2,C₃} test in your report §4 (that test's
model had the bug above). The endpoint theorems you endorsed are unchanged.
