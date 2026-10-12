# Covering note — Rick (CC Robin)
## Strathclyde capstone: "The inventory gerbe couples on the torus"

**Date:** 2026-10-12 · **From:** MacBeth · **Status: consolidation at honest registry grades — NOT
yet independently reviewed in this standalone form. One new theorem (the general δ-commutator lemma);
everything else restructured from existing proof files.**

Rick —

For Neil's Strathclyde mini-course (13–16 Oct) I have consolidated the whole nonabelian-inventory-gerbe
arc into one self-contained ~9-page note: **`papers/inventory-gerbe-couples-on-torus.tex`**. It is a
course handout and a grant Applications beat. It re-derives nothing — it pulls four existing results
into a single narrative (floor → coupling → sharpness → rarity) built around the one piece of genuinely
new mathematics, the general δ-commutator lemma that landed in the 10-12 PROVE session.

**The unifying device (and the recurring bookkeeping hazard, handled).** The relabelling group
`K = Aut F` sits in *two* abelian-kernel extensions sharing the middle term `Inn K`:

    (II)  Z(K) ↪ K     ↠ Inn K     coeff Z(K)   — the degree-2 inventory class [𝔤]
    (I)   Inn K ↪ Aut K ↠ Out K     coeff Inn K  — the band strictification δ

I made the Inn-vs-Z(K) coefficient distinction the **spine** of the note rather than a footnote, since
it is exactly where we keep tripping (cf. the off-by-one lane and the 10-11 coefficient correction). The
δ-commutator lemma is the single engine for both extensions.

**What is claimed, and at what grade (please hold me to these — they match the registry exactly):**

1. **Floor (Cor 2.5):** strict global inventory ⟺ `β=0 ∧ [𝔤]=0`. — **proved** (thm-A / band-boundary
   clause-a′; rests on published Giraud/Breen + Brown IV.3). *Unchanged; stated as baseline.*

2. **δ-commutator lemma (Thm 3.3) + coupling criterion (Cor 3.5):** for an abelian-kernel extension
   `1→M→E→Q→1` and a band `ρ:ℤ²→Q`, `δ(ρ)=[[A,B]] ∈ H²(T²;M)=M_{ℤ²}`, lift-independent; `K` couples
   on `T²` ⟺ some commuting outer pair has no commuting lift ⟹ the extension is non-split (necessary,
   not sufficient). — **proved** (`coupled-T2-general-delta-lemma`). The one non-classical step is the
   explicit Koszul↔bar comparison map `φ₂(e_st)=[s|t]−[t|s]`; the vanishing dictionary (C1–C3) is cited
   to Brown IV.3–4 / Eilenberg–Mac Lane, not re-derived. **This is the new result.**

   *Note on generality:* the companion proof file states the lemma for `G` of class ≤2 with `M=Inn G`,
   but its proof uses only `M` abelian; I state it for a general abelian-kernel extension (which is what
   the proof gives) and flag that class ≤2 is what makes `Inn K` abelian in application (I). The central
   case (II), `M=Z(K)`, is the classical fact already carried by thm-D. If you think stating it at the
   abelian-kernel level over-reaches the registered node, say so and I will pin it back to `M=Inn G`.

3. **Coupling witness `K=D₄×C₂` on `T²` (§4):** `β≠0` and `δ(β)=[A,B]=[s]≠0 ∈ H²(T²;Inn K)=(ℤ/2)²`;
   same group also couples the central stage (`[r,s]=r²∈Z(K)`). — **computed**; arithmetic core
   **lean-verified** (`coupled-T2-finite-core-lean`, [propext]). I explicitly do **not** grade this
   above computed, and do **not** claim minimality over all order-≤16 groups.

4. **Sharp line (Thm 5.2):** `K=D_n`; `[𝔤]` essentially nonzero ⟺ (II) non-split ⟺ `4∣n`. `D₆≅ℤ/2×S₃`
   is the necessary-not-sufficient witness. — **proved** (thm-D); finite split-test core
   **lean-verified, axiom-free** (`dihedral-split-finite-check`, 10-12).

5. **Rarity (§6):** only `D₄×C₂, Q₈×C₂` couple; `M₁₆, C₄⋊C₄` are non-split but do **not** couple. —
   **computed over the enumerated order-≤16 (+ES⁺₃₂, Heis F₃) class-2 family only — not a census.**
   Stated as such in the text.

**Specific things to attack:**

- The abstract/intro compress "couples on `T²` via (I)" and "essentially nonzero via (II)" — is that
  conflation misleading, or acceptable compression given §4–§5 keep them distinct?
- §3.2 proof (ii): the factor-set values `f(s,t)=0`, `f(t,s)=w⁻¹` and the sign in `δ(ρ)=[0−(−w)]=[w]`.
- Whether the general-abelian-kernel framing of Thm 3.3 (point 2 above) is honest w.r.t. the node.

**Not emailed yet** — write sessions commit but cannot send; this note is queued for the next WAKE to
deliver (per the standing "WAKE delivers undelivered covering notes" feedback). PDF compiles clean
(9pp, no warnings); citation footprint check passes (all refs published/textbook — Giraud, Breen,
Brown, Eilenberg–Mac Lane, Rotman; no arXiv sources below deep-read). Content commit `1c9affb`.

— MacBeth
