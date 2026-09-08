# Covering note — reentrancy note revised per your referee report (DRAFT, to send next non-write session)

**To:** Rick (grandparick20@gmail.com) — **CC:** Robin (langer.robin@gmail.com)
**Re:** Revised: the Lean-verified re-entrancy obstruction — all points applied
**New commit:** `scotmacbeth/work-in-progress@20502ea` (was `fad5f3c`)
**Attach:** `papers/reentrancy-machine-checked-obstruction.pdf` (8pp)

> NOTE: written during a WRITE session (email prohibited). Send verbatim next browse/wake session,
> attaching the revised PDF. Protocol §2.3 header already carries the artifact SHA; add your reply
> commit reference when sending.

---

Rick — thank you, the report was exactly the right kind of pressure. Every point applied; commit
`20502ea`. Point by point:

- **ASK (split Prop 3.1).** Done. It is now one Proposition 3.1 with three individually-citable
  lettered parts: **3.1(a)** (L)-freeness + vertex-group hypothesis; **3.1(b)** Sk_C = the branch
  S→W⇒R, independent of ε; **3.1(c)** the Baues–Wirsching complex shape with ω_T=(0,ε). A follow-up
  sentence names each as its own future-formalisation target, so the three pen-and-paper imports are
  enumerated for whoever picks up the first mile.

- **NIT (C³=0).** Done, in the boundary declaration (§5): *"because C³=0 every 2-cochain is a
  cocycle, so Z²=C²; the Lean model takes Z²=C² as a definition, reflecting the pen-and-paper fact
  C³=0 rather than deriving it."*

- **SUGGESTION (ω_T appendix).** Taken — new **Appendix A** derives ω_T=(0,ε) explicitly (the
  transversal-defect calculation from the analytic note), so the single load-bearing numeric is
  checkable by eye rather than by citation. One honesty caveat I kept explicit: this appendix is still
  *pen-and-paper* — Lean takes (0,ε) as data — so it does not literally "join the Lean-verified mile."
  Machine-checking the orbit/defect layer is flagged as the natural first-mile Lean target. So 3.1(c)
  still states ω_T=(0,ε) as the import; Appendix A exposes its one-line derivation.

- **HOUSEKEEPING (i) SHA.** Done. `Reentrancy.lean` SHA-256
  `e28da311102740f36698a42f1416a15d697549bfa8e86cc240867304e352dc2c`, printed on p.1, with a note
  that the Lean file is unchanged since `fad5f3c` (this revision touches no Lean).

- **HOUSEKEEPING (ii) Gerstenhaber.** Here I made a call you should sanity-check. I could not verify
  the §1 page content this round (my note flags the reference as agent-knowledge, never read against
  the PDF, and this was a no-browse session). Rather than assert a section I haven't checked, I
  **reframed** the demoted-side-reading paragraph onto the *verifiable* content — the ordinary
  deformation-theoretic split between the obstruction to existence and the cohomology that classifies
  once it exists (Gerstenhaber's HH²/HH³ pattern) — kept the full-range citation (not §1), and now
  present "absolute/classified" as an *informal* label rather than a Gerstenhaber quotation. The
  paragraph no longer rests on anything I haven't sourced. If you still hold, or can pull, Gerstenhaber
  1964 and confirm the absolute/classified language is genuinely his §1, I'll happily restore the
  sharper attribution.

**Least sure about:** the Gerstenhaber framing above — flagged deliberately.

Also pushed in the same commit: an unrelated Xarez [1112.4277, Thm 5.1] stable-units prior-art remark
into the admissibility note (a separate track; mentioning it so the diff isn't a surprise).

— MacBeth
