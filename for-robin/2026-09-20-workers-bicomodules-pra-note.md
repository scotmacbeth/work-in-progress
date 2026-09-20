# For Robin/Neil — expository note: "Workers, Bicomodules, and Parametric Right Adjoints"

**MacBeth, 2026-09-20 (WRITE session).**
File: `expository/2026-09-20-workers-bicomodules-pra.tex` (+ compiled PDF, 6pp).

## What this is
An **exploratory** note (knowledge base, per WRITE.md), not a venue paper. It sets two things
side by side and poses — but deliberately does **not** assert — a bridge conjecture.

- **Established input 1 (deep-read literature):** Spivak–Garner–Fairbanks, *Functorial
  Aggregation* (JPAA 2025 / arXiv:2111.10968). Thm 4.28: Cat♯ ≃ Comod(Poly); loose maps =
  bicomodules = parametric right adjoints between copresheaf categories. Prop 3.6: every
  prafunctor factors as a **right-adjoint** content part `F/1` followed by a **coproduct
  Σ**-aggregation tail that is *not* bicomodule data.
- **Established input 2 (my proved result):** `proofs/2026-08-29-workers-retract-of-bhm-grading`
  — Workers `⊗`-grading is a canonical **retract** of the BHM `▷`-grading, idempotent
  `e=σr` collapsing each branch map `g` to `const_{g(s)}` (self-evaluation).

## The conjecture, and why I stopped short of claiming it
Both split a construction into "kept content" + "discarded tail," same shape. Conjecture 5.1:
**worker = bicomodule/PRA**, retract kernel = Σ-tail. But I found — during the write — a concrete
obstacle worth flagging loudly:

- **★ Gap 5.2 (adjointness reversal):** the retract discards the branch maps `g:S→T`, which are
  **exponential/power** data (`T^S`), i.e. **right-adjoint**-flavoured; but SGF discards a
  **coproduct Σ**, i.e. **left-adjoint**-flavoured. The two "tails" point in opposite adjoint
  directions. Either a handedness / (σ-vs-e) change of comparison fixes it, or the conjecture is
  false. This is the first thing a prove session must resolve.
- **Gap 5.3 (which comonads?):** SGF's Prop 3.9 is about maps *between fixed* comonads `(c,d)`;
  `ΔS⊗ΔT`, `ΔS▷ΔT` are monoidal *products* of comonads. Need to pin what plays the role of
  `(c,d)` (likely the store comonads as codiscrete categories) before the correspondence can bite.

Nearest neighbour Capucci–Myers *Contextads* Thm A.4 gestures at "graded composition ⊂ PRA world"
but leaves it **unproven**, so it is not a shortcut.

## What I'd like from a PROVE session
Settle Gaps 5.2 and 5.3 (see §6). If both go through, "worker" gets a clean Poly semantics inside
Cat♯, unifying the state axis with the directed/retrofunctor axis — grant Theory-pillar material.

Citations all deep-read (provenance floor: deep-read; citation_check clean).
