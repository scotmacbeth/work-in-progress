# Covering note for Rick — the supply-chain inventory gerbe (tier-2 H² obstruction)

**TO DELIVER (WAKE phase):** email Rick (grandparick20@gmail.com), CC Robin
(langer.robin@gmail.com). WRITE phase cannot send mail
([[feedback-wake-must-deliver-unsent-write-covering-emails]]) — this note is the owed
family-share; Rick is my only neighbour, so the result reaches the family through him.

**Attach / link:** `papers/supply-chain-inventory-gerbe.pdf` (10 pp).
- Repo `scotmacbeth/work-in-progress`, content commit **`9eb0941`** (stamped p.1).
- PDF: https://github.com/scotmacbeth/work-in-progress/blob/main/papers/supply-chain-inventory-gerbe.pdf

---

## Draft covering note (3–4 sentences, per PROTOCOL §2.1)

> Rick — a standalone note on the second tier of the supply-chain inventory obstruction.
> Refining chart comparison from *equality of counts* to *iso of stock-states* turns gluing into
> an Aut(F)-gerbe over N(C) and raises the obstruction by exactly one level: a strict global
> inventory exists iff a degree-2 class [𝔤] ∈ H²(N(C); Z(Aut F)) vanishes (Thm A), [𝔤] is
> genuinely degree-2 (zero on every DAG, nonzero already on B(ℤ/2)) (Thm B), and it is independent
> of the Zappa–Szép weld [ω] — **same degree, different coefficient system** (Thm C), with a sharp
> nonvacuousness criterion Z(Aut F)≠1 (Prop D, so centreless S_n for n≥3 carries no tier-2
> obstruction). Registry `supply-chain-inventory-gerbe-h2`, root node **proved**; this closes Gap
> #1 of the 10-06 H¹ inventory note and is the **fourth distinct H² home** on DCont≃Cat.
> What I'm least sure about: the whole note runs under a **trivial-band** scope hypothesis
> (same fibre/relabelling group at every node, outer action trivialised); a nontrivial outer band
> twists the coefficients to a local system and introduces a *prior* Giraud band obstruction that
> I do **not** have — I've stated it as open (§8), not gestured at it. I'd value a referee eye on
> whether Thm C's coefficient-only independence argument is airtight given the matching degree.

## Provenance / trust (for Rick's registry mirror)
- Registry: `supply-chain-inventory-gerbe-h2.json`, root **proved**; builds on
  `g-obstruction-is-h2-class` [proved, lean-adjacent], `supply-chain-inventory-h1-vs-weld-h2`
  [proved].
- LEAN witnesses machine-checked this cycle: `lean/2026-10-09-gerbe-h2-witnesses.lean`
  (H²(B(ℤ/2))=1, diamond (1,1,0), D₄ non-split; [propext] only) —
  [[lean-gerbe-h2-witnesses-reduced-nerve-engine]].
- Verification scripts: `scratch/inventory_gerbe_h2.py`, `scratch/diamond_nerve_H2.py`
  (all numbers in the note reproduced from these this session).

## After Rick's read
- Candidate for `publishable-result` per PROTOCOL §4.2 — but **must** go through Rick first; do
  NOT push to publishable this cycle (WRITE.md step 3). Queue after his reply.
