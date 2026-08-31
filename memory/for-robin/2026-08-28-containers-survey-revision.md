# Revision note — `containers-over-a-base.tex` (2026-08-28 write session)

**File:** `/home/agent/projects/papers/containers-over-a-base.tex` (compiles clean, 14pp, was 12pp).

## What changed
The 2026-08-27 draft had Approach (3) (the fibrational leg) as a ~40-line "referee" stub. Neil's
UID-132 reply asked for a *logic of containers*, and I proved it in the 2026-08-28 PROVE session
(`proofs/2026-08-28-cont-cod-fibration.md`). This revision carries that proved result into §5 as its
concrete anchor:

- **New §5.1** — Lemma: `Fam` preserves fibrations (componentwise cartesianness), proof sketched.
- **New §5.2** — Theorem: `Cont(cod)=Fam(cod^op)` is a **bifibration**; fibre over `(S,{P_s})` is
  `∏_s (Set/P_s)^op` = proof-relevant predicates on positions (von Glehn's fibrewise op).
- **New §5.3** — Theorem: along the collapse, the string `A ⊣ Δ_c ⊣ E` = the **A/E predicate
  liftings** (E = Exists = cartesian reindexing, A = All); plus the reindexing TRAP remark
  ((Σ_ρ)^op, not ρ^*).
- **New §5.4** — the **dualisation theorem**: the container hyperdoctrine is the *fibrewise opposite*
  of Set's (∃↔∀, ∧↔∨, ⊤↔⊥; each fibre a co-topos with subtractive logic). This is the payoff.
- Honest **scope remark**: position-level only; shape-level quantifiers + joint BC/Frobenius + the
  intrinsic BC-square class are stated OPEN, not claimed.

Supporting edits: abstract gained a closing sentence on the logic of containers; intro bullet (3),
outline, and "what is new" now credit von Glehn (ancestor) + Jacobs/Hermida (folklore) and list the
new assembly as the delta; conclusion gained a bridging paragraph so intro↔conclusion stay consistent.
Bibliography +3 (von Glehn, Jacobs CLTT, Hermida PhD). The T1/T2/T4 discriminator spine is unchanged.

## What still needs work (for a future session, NOT this one)
1. **Citation provenance (before any arXiv submission).** von Glehn TAC 33 (2018) / PhD Cambridge 2015
   is cited from my starred memory, but is **not** in `memory/reading/sources.json`. Needs a browse
   session to deep-read and log it. Jacobs/Hermida are standard textbooks (fine as-is; they carry no
   arXiv ID so `citation_check.py` doesn't see them).
2. **The two honest gaps in §5** (Remark "Scope of the logic") are genuine PROVE targets: (a) the
   combined shape×position hyperdoctrine's BC/Frobenius, (b) an intrinsic characterisation of the
   BC-square class in terms of container pullbacks. These are secondary to the survey's headline open
   problem (the DPUV branching-hierarchy question, §8), but worth logging.
3. The `Exists = ◁` identification (true, from earlier work) is *not* explained in the paper — I cut a
   parenthetical claim of it to avoid an unsupported-looking leap. If we want it, it needs a proper
   bridge to the ◁ material of §2/§3.

No email sent (write session). Robin can read the PDF/tex directly from the projects volume.
