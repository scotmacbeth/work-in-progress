---
name: census-framing-preferred
description: Peer + PI both prefer the "census" framing of the four-monoidal picture ("every monoidal structure on Set induces one by Day convolution") over "four canonical structures".
metadata:
  type: feedback
---

# Frame the monoidal picture as a CENSUS, not "four canonical structures"

**Two independent endorsements** of the census framing for the monoidal-structures-on-Cont work:
- **Rick** (peer agent, email uid-57, 2026-07-15): explicitly endorses *"every monoidal structure on
  Set induces one on Cont by Day convolution"* over *"four canonical structures on Cont."*
- **Neil** (PI, email uid-51, 2026-07-14): accepted "four canonical monoidal structures" but
  immediately asked *"are there OTHER interesting monoidal structures on Set?"* — i.e. he too reads it
  as a census with more entries, not a closed list of four.

**Why:** the mathematics IS a census — **Theorem A** says Day convolution is an *equivalence*
{monoidal structures on Set} ≃ {convolutional structures on Cont}. "Four canonical" undersells it
(the four are just `+`, `×`, `⊗`, `◁`) and, worse, reads as a *classification claim* that the
⋉/⋊ = Dialectica discovery then **refutes** — the linear-logic tensors are non-convolutional and sit
OUTSIDE the Day family, so there is no finite canonical list. Census framing makes the Day family and
its boundary (⋉/⋊) part of one honest story instead of an embarrassing exception.

**How to apply:** in the four-monoidal chapter and grant narrative, lead with "Day convolution turns
every monoidal structure on Set into one on Cont — a *proper class* of them (Cor 5.5)" and present
`+/×/⊗/◁` as the *named/most-useful* members, then ⋉/⋊ as the outside-the-family case. Never write
"the four monoidal structures on Cont" as if exhaustive.

**Also from Rick uid-57:** read Shapiro–Spivak duoidal machinery BEFORE any claim about the
`dirToSeq` (⊗→◁ comparitor) asymmetry — [[comparitor-points-the-wrong-way]] rests on it. And his
policy note: my `lean-verified` status does NOT auto-cross into his registry (checked-sober); he holds
my refutation at peer-claimed/methodology until he re-derives by hand. Related:
[[day-family-classified]], [[ltimes-rtimes-are-dialectica]].
