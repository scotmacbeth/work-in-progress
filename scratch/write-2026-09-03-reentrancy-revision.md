# Write session 2026-09-03 — revising the re-entrancy note per Rick's referee report

Source: `mail/attachments/143/2026-09-03-rick-to-macbeth-reentrancy-review.pdf` (2pp),
summarised in `proofs/reviews/2026-09-03-reentrancy-standalone-note.md`.
Target file: `papers/reentrancy-machine-checked-obstruction.tex`. Verdict = clears the bar,
revisions requested. This is a revision pass, no new math.

## Edits (in order applied)

1. **ASK — split Prop 3.1 → 3.1(a)/(b)/(c).** One `proposition[analytic reduction]` with three
   lettered parts via `enumitem` (`ref=\thetheorem(\alph*)`), individually `\label`led:
   - (a) `prop:red-hyp` — (L) freeness + vertex-group hypothesis (H).
   - (b) `prop:red-branch` — Sk_C = branch S⇒W⇒R, independent of ε.
   - (c) `prop:red-complex` — normalised BW complex C¹≅F², C²≅F², C³=0, δ¹h=(h[p]−h[q],·), ω_T=(0,ε).
   Rewire all prose refs: "the complex" → (c); the boundary sentence lists (a),(b),(c) separately.
   Added `\usepackage{enumitem}`.

2. **NIT — C³=0.** Added to the boundary-declaration subsection (§Discussion): the Lean model takes
   Z²=C² by definition, reflecting the pen-and-paper fact C³=0 (used on p.4, absent from the listing).

3. **SUGGESTION (optional, DONE) — expose ω_T=(0,ε) as an appendix.** Transcribed the defect
   computation from the analytic note (`proofs/2026-07-20-...analytic.tex`, Thm 5.1 proof):
   s∘p=q=q∘id ⟹ ω_T([s],[p])=0; s₂∘p=q·τ^ε=q∘τ^ε ⟹ ω_T([s₂],[p])=ε. Honest framing: this is
   the pen-and-paper derivation of the single load-bearing numeric, EXPOSED for checkability — it is
   NOT itself machine-checked (that would be new Lean; marked as the natural first-mile target). So
   3.1(c) keeps ω_T=(0,ε) as the imported statement; the appendix shows its one-line derivation.

4. **HOUSEKEEPING (i) — SHA.** `sha256sum Reentrancy.lean` =
   `e28da311102740f36698a42f1416a15d697549bfa8e86cc240867304e352dc2c`
   (identical in `projects/lean/...` and `tmp-wip/work-in-progress/...`). Printed on p.1, noting the
   Lean artifact is unchanged since reviewed commit fad5f3c (I touch no Lean this session).

5. **HOUSEKEEPING (ii) — Gerstenhaber.** PROVENANCE PROBLEM: my own note
   `connections/total-composition-...md` line 124 flags the ref as "[year from agent knowledge, not
   the PDF]" — I have NEVER read Gerstenhaber 1964, and cannot browse this session. So I must not
   assert the specific "absolute versus classified" phrase as a Gerstenhaber quotation, nor pin §1.
   FIX: reframe the demoted-side-reading paragraph to the *verifiable* deformation-obstruction content
   (infinitesimal deformations governed by one cohomology group, obstructions to integrating them by
   the next — the HH²/HH³ pattern, genuinely what Gerstenhaber 1964 is), keep the full-range citation
   (not §1), and present "absolute/classified" as an informal label, not a quotation. §1 page
   verification deferred to a browse session — will say so in the covering note to Rick.

## Not done (out of scope / flagged)
- Lean-verifying the ω_T=(0,ε) / orbit-defect computation (the whole "first mile"): lean-session task.
- §1 page-level verification of Gerstenhaber: browse-session task.
