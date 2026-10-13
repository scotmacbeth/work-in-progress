# For Rick — your 2026-10-13 referee MUSTs are landed (floor / nerve / crown / gerbe Thm D′)

**Date:** 2026-10-13 · WRITE session · re-delivery of four corrected PDFs
**To:** Rick (grandparick20@gmail.com) · **CC:** Robin Langer (always)
**Repo:** `github.com/scotmacbeth/work-in-progress`, content commit **`ccbf3b6`**, stamp commit **`6883c34`**
(two-commit pattern; every PDF page 1 carries author/date/recipient/title + content commit `ccbf3b6`).
**Attach on send:** the four PDFs under `papers/` listed below.

Thank you for the four reports (UID 223/224/225). Every MUST is applied; no theorem statements changed
except where you flagged a statement as false, which I retracted. Registries re-validated GREEN
(`supply-chain-inventory-gerbe-h2`, `composition-nerve-level`, `game-comonad-poly`). I did **not**
re-promote the band-boundary (still `computed`), per your instruction.

---

## 1. Floor D1-vs-D2 — `papers/inventory-floor-d1-vs-d2.tex`  (UID 223, BLOCKING)
- **α strict is now the standing hypothesis**, stated once up front (intro paragraph) and again in §2;
  Definition (D2) and the clause-(a) citation are explicitly scoped to strict α (with the B(ℤ/3), D4
  non-strict failure noted).
- **Retracted** the "gap exactly when the centre is too small" characterisation (abstract, Thm 1.3
  part 3, Prop "D1⟹D2", Upshot) **and** the backwards D2⟹D1 in the abstract. Kept only **D1⟹D2
  (strict)** and the separation. New framing: on a 1-dimensional base H²=0 forces [𝔤]=0 for every K,
  so the gap is a matter of **degree, not centre size** — witnessed by both B(ℤ)/S₃ (centreless) and
  **B(ℤ)/D₄** (Z=ℤ/2), exactly your separating point. A short Remark marks the exact gap-locus as open.
- §2's clause-(a) citation now reads "for strict α" with the non-strict caveat.
- Cited your **0 / 248 strict-α** sweep (controls failing as required), inline (`scripts/day238`).

## 2. Nerve — `papers/composition-is-a-nerve-level-two-datum.tex`  (UID 224, 1 MUST)
- **Sec 2 and Rem 13 reconciled with Rem 17**: it is the extension **E_ω** (equivalently the candidate
  weld), **not 𝒮 itself**, that splits; a base presented as 𝒞⋈𝒟 has [ω]=0 by construction. No
  statement heads changed (your 10/10 verbatim stands).

## 3. Crown Stage 2 — `papers/crown-stage2-unfolding-vs-descent.tex`  (UID 224, 2 MUSTs)
- The two bare "Ψ is no functor" lines now carry the **hypothesis** ("covering the embeddings, nor any
  acting by the canonical action on automorphisms").
- **Rem 20 corrected**: dropped the false "escapes are *exactly* those acting trivially on
  automorphisms." Your **sign action on the three-leaf star** is cited as an escape acting
  *nontrivially* on automorphisms; what every escape shares is only that none acts by the *canonical*
  branch action (the single hypothesis Thm 19 closes). Credit and Thm 19 = your 18′ left as is.

## 4. Inventory gerbe Thm D′ — `papers/supply-chain-inventory-gerbe.tex`  (UID 225, 2 MUSTs)
- **Sec 2.3 / Rem 11:** "strict functor carrying the k_{g,f}" is corrected — the datum is a strict
  functor into the **2-group AUT(F)** (= a pseudofunctor); the sharp results are stated under **k ≡ e**.
  A central k contributes its own class, [𝔤] = ρ*[⋆] + [k], moving the line to **2∣n**; flagged in both
  Sec 2.3 and Rem 11, and in the Thm 28 statement.
- **Thm 28 scoped to the trivial band** ("always rectifiable unless 4∣n" is a trivial-band statement).
  New **Rem (d6band)**: the banded exception — n=6 on B(ℤ/2), outer involution r↦r⁵, s↦sr ∈ Out D₆≅ℤ/2
  admits no inventory — tied to the forced-correlation companion (`gerbetorus`, the banded T² note).
  Intro/abstract D₆ claims now say "over the trivial-band stratum."

---

**Status I'm claiming:** these are revisions discharging your blockers, not new claims. Floor should
now stabilise at "proved" under α-strict; the gerbe Thm 28 chain is checked-sober under k≡e with the
banded case flagged, not claimed. Please re-read at your convenience — flag anything still off.
