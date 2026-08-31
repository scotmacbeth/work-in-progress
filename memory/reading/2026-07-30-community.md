# Browse 2026-07-30 — community sites (MathOverflow, nLab, nForum, cstheory.SE, Zulip, n-Category Café)

Context: MacBeth proved effect–coeffect "arrows" on Cont (built from monad G_M/T_M pair) form a genuine
Freyd/arrow category iff the underlying Set-monad M is "non-branching" (arity ≤ 1). Searching for
(a) prior folklore on premonoidal/commutative-monad ↔ arity, (b) named dichotomy for branching monads
failing arrow-hood, (c) classification of E+A×(−) monads.

Infrastructure note: WebFetch cannot reach mathoverflow.net or nforum.ncatlab.org directly (both
blocked/Cloudflare-403'd); Playwright browser is currently broken in this container (crashpad
"--database is required" launch failure, both retries). Worked around by curling MathOverflow's
`/search?q=...` and cstheory.stackexchange.com's `/search?q=...` HTML directly via Bash and grepping
`href="/questions/..."` — this works and is a viable pattern for future browse sessions if Playwright
stays broken.

## 1. Premonoidal category + commutative monad — CONFIRMED FOLKLORE, well-documented, NOT new

This is precisely stated, standard, and citable (not a new finding, but confirms the exact statement
MacBeth wanted):

- **nLab, "premonoidal category"** (https://ncatlab.org/nlab/show/premonoidal+category): states
  outright "This premonoidal structure is only a monoidal structure if T is a commutative monad."
  Cites Power–Robinson 1997 "Premonoidal categories and notions of computation" (the origin), Staton–Levy
  2013, Román 2022. Also discusses Freyd categories as the fix for premonoidal-functor definitional
  issues. **No mention of arity, branching, powerset monad, or MacBeth's dichotomy.**
- **nLab, "commutative monad"** (https://ncatlab.org/nlab/show/commutative+monad): defines via
  commuting strengths; explicitly lists **the powerset monad as an example of a commutative monad**
  ("The power set monad is commutative, with monoidal structure given by forming the product of
  subsets."). No arity/branching/classification content.
- **Jules Hedges, "Folklore: Monoidal Kleisli categories"** (https://julesh.com/posts/2019-04-18-folklore-monoidal-kleisli-categories.html):
  clean informal write-up of the same folklore theorem, examples = powerset monad, finite-support
  distribution monad, reader monad. Frames commutativity as "no implicit dataflow between the two
  Kleisli arms." Non-commutative case → symmetric premonoidal, not monoidal. No arity/branching framing.
- **nLab, "Freyd category"** (https://ncatlab.org/nlab/show/Freyd+category): confirms Kleisli category
  of ANY strong monad forms a Freyd category (premonoidal) — existence is unconditional; it's only the
  extra step to a genuinely *monoidal* Kleisli category that needs commutativity. References: Power–Thielecke,
  Levy–Power–Thielecke, Levy 2004, Power 2006, Staton 2014 (Freyd cats = enriched Lawvere theories),
  Jacobs–Heunen–Hasuo 2009, Asada MSFP'10, Román ACT 2022. No arity/branching content, no open questions
  flagged on the page itself.

**Verdict: confirms existing understanding, not a new lead as stated.** But see §3 below — a genuine
and important disanalogy surfaced while chasing this.

## 2. MathOverflow / nForum / cstheory.SE — searched directly, essentially empty for this cluster

Curled `mathoverflow.net/search?q=...` for: "premonoidal commutative monad" (0 hits), "premonoidal"
(4 hits, none on-topic — mostly general monoidal-category coherence questions), "Freyd category arrow"
(14 hits, all irrelevant — semidirect products of groupoids, small-object argument, etc.), "nondeterminism
monad commutative" (0), "affine monad" (0), "commutative monad classification" (0), "exception monad
writer monad" (0).

One MathOverflow hit worth a one-line flag: **"Are all binoidal categories in the literature actually
strict?"** (https://mathoverflow.net/questions/60342) — a coherence nitpick about binoidal/premonoidal
definitions (does `f⋉(A⊗B) = (f⋉A)⋉B` follow from the binoidal axioms). Purely about definitional
completeness of premonoidal structure, zero arity/branching/Poly content. **Not relevant.**

nForum: blocked by Cloudflare (403, "Just a moment...") from this container — could not search.
cstheory.stackexchange.com: searched "premonoidal category", "commutative monad", "arrow category",
"Kleisli category monoidal", "nondeterminism monad" — only generic hits (reader/writer monads, type
classes), nothing on the specific dichotomy. **No thread found anywhere naming or studying MacBeth's
branching/leaf-symmetry vs associativity distinction.** This looks like genuinely unassembled territory
in the public forum record, consistent with prior sessions' findings for the effect-coeffect arrow work.

n-Category Café: not searched directly (no working site search found in the time budget); one tangential
2009 hit ("The Monads Hurt My Head — But Not Anymore") surfaced via general web search on affine monads,
not fetched — low priority, general monad-101 post by the title.

Zulip Category Theory archive: not reachable by direct search tooling in this session (no public
full-text search endpoint found quickly); general web search for "zulip premonoidal commutative monad
arity branching" returned only arXiv/nLab papers already covered above, no Zulip threads surfaced.
**Flag as unsearched — worth a dedicated Zulip-archive pass (archive.org mirror or Zulip's own search
UI via a working browser) in a future session if Playwright gets fixed.**

## 3. Important disanalogy found: "commutative" (Power–Robinson) ≠ "non-branching" (MacBeth's arity ≤ 1)

This is the most useful finding of the session, surfaced by chasing concrete examples rather than by a
single search hit:

- **Powerset/nondeterminism monad Pf is COMMUTATIVE** (nLab, confirmed above) — yet it is exactly
  MacBeth's paradigm **branching** monad (arity ≥ 2; this is the monad used throughout the prior
  effect-coeffect sessions, e.g. `effect-coeffect-arrows-first-strength.md`, as the case where the arrow
  category fails).
- **The exception/coproduct monad `T(X) = X + E` is commutative ONLY when `|E| = 1`** (per general web
  search on strong-monad literature: "the exception monad is only commutative if there's exactly one
  exception... with multiple exception types, strong but not commutative"). Yet `X + E` (any `E`) is
  exactly the non-branching shape MacBeth conjectures always yields a genuine arrow category (arity ≤ 1:
  each operation either raises one of `|E|` exceptions or returns one value — no *fan-out*, but plenty of
  non-trivial "width" in the exception set).

So the two conditions run in **opposite directions on these examples**: Pf is branching-but-commutative,
and `X+E` (`|E|>1`) is non-branching-but-NOT-commutative. **This means MacBeth's "non-branching ⟺ arrow
category exists" dichotomy is NOT a restatement of Power–Robinson commutativity in different words — it
is measuring a genuinely different structural property**, even though both are "does some coherence
square commute" conditions on a strong monad's structure maps. Concretely: Power–Robinson commutativity
is about **order-of-evaluation independence** between two independent effectful arguments (a dataflow/
scheduling condition); MacBeth's non-branching condition (from `effect-coeffect-arrows-first-strength.md`)
was pinned down as a **naturality/leaf-symmetry** condition on how many output branches a single
operation produces, unrelated to reordering two separate computations. This is worth stating explicitly
in the writeup/paper as a "not the same as commutativity, despite surface resemblance" remark, with Pf and
`X+E` as the two witnessing examples. Recommend double-checking the `X+E` non-commutativity claim by hand
before citing (it followed from a WebSearch synthesis, not a primary-source quote) — but it is very
plausible and matches the general folklore that exceptions only commute past each other when there's
nothing to distinguish, i.e. one exception value.

## 4. Terminology collision: "affine monad" is ALREADY TAKEN, means something ~opposite

**Do not name the E+A×(−) conjectural class "affine monads."** nLab, "affine monad"
(https://ncatlab.org/nlab/show/affine+monad): a commutative monad `T` on a cartesian category is affine
iff `η₁: 1 → T1` is an isomorphism, i.e. **T preserves the terminal object**. This is the standard
categorical-probability notion (Jacobs 2016 "Affine Monads and Side-Effect-Freeness"; Fritz's work on
Markov categories) — "Kleisli category of an affine commutative monad is a Markov category." Crucially,
for the exception monad `T(X) = X+E`, `T(1) = 1+E ≠ 1` whenever `E ≠ ∅` — so exception monads are
**generically NOT affine** in the established sense, almost the opposite of what the name would suggest
for MacBeth's conjecture. If MacBeth wants a name for "monads of shape `E + A×(−)`," coin a fresh term
(e.g. "linear-affine monad" is also risky — "affine" is claimed; maybe "exception-writer monad" or
"width-1 monad" tracking the arity≤1 idea directly) — but flag this collision before it ships in a paper
or the book.

No classification theorem for `E + A×(−)`-shaped monads was found anywhere (nLab, MathOverflow, arXiv
search, cstheory.SE) — this classification question (part (a) of MacBeth's task) appears genuinely open /
unaddressed in the literature, at least not under any name searched this session.

## 5. Dedup / prior-session cross-check

Grepped `/home/agent/projects/memory/reading/sources.json`, `feeds.md`, and `connections/*.md` for
premonoidal, commutative monad, Freyd, affine monad, Power-Robinson, non-branching, arity before starting:
**zero prior hits** — this cluster (Power–Robinson/premonoidal/commutative-monad literature) had not been
searched in any prior session, unlike KRU 1912.13477, Ahman-Bauer, Petricek-Orchard-Mycroft, entwining/
distributive-law/wreath-product nLab pages, all of which are previously-confirmed-null and were NOT
re-searched here (per instructions). One incidental hit worth flagging: general search surfaced
Petřícek–Orchard "Patterns for computational effects arising from a monad or a comonad" (1310.0605) and
"Breaking a monad-comonad symmetry between computational effects" (1402.1051) again in the affine-monad
search — both already covered by the standing Petricek-Orchard-Mycroft null result per instructions, not
re-read this session, note only that they keep surfacing (expected, same author cluster).

Also surfaced but not deep-read (false-friend on the word "arity," flag so nobody chases it later):
**Berger–Melliès–Weber, "Monads with arities and their associated theories"**
(https://www.irif.fr/~mellies/papers/bmw-arities.pdf) — "arity" here means *dense generator* /
accessibility rank of a monad (Lawvere-theory-style operation arity = number of *inputs*), a completely
different technical notion from MacBeth's arity = number of output branches / fan-out of an operation.
Not relevant, but the naming collision is worth a one-line footnote if MacBeth's write-up ever uses the
bare word "arity" near a citation list — a reader could conflate the two.

## Open questions worth MacBeth pursuing

1. Is there a clean formal statement of *why* Pf (branching, commutative) and `X+E` (non-branching,
   non-commutative for `|E|>1`) sit on opposite sides of both dichotomies? A 2×2 table (branching × 
   commutative) with concrete inhabitants in all 4 cells would make a strong, citable, self-contained
   remark for the book/paper — worth 30 minutes of direct computation rather than more searching.
2. Zulip archive and n-Category Café were not properly searched this session (tooling gaps) — worth a
   dedicated pass once Playwright is working again, since these are exactly the venues where an informal
   "isn't this the same as commutativity?" objection would have been raised and answered if this dichotomy
   were folklore.
3. No existing classification of `E + A×(−)`-shaped monads found — if MacBeth wants positive coverage
   of part (a) of the original task, this looks like it needs to be proved from scratch rather than cited.
