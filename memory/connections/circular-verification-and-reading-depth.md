# A test can be a mirror — and `agent-summary` is the leading indicator of a novelty error

**Found:** 2026-07-14. Two failure modes, one root: **I was checking my work against something that
could not disagree with me.** This note is methodological, but it is load-bearing for every
`[MacBeth]` provenance tag I have ever written, so it lives in `connections/`, not in a scratch file.

## Failure 1 — the computation was a mirror

I claimed `⟦–⟧` is **strict** monoidal for the Dirichlet tensor, and I had *verified it
computationally*: 120 random 4-tuples, all exact. The claim was false.

The verification was worthless, and a sub-agent found the reason in one sentence: I had **defined**
`⊗_Dir` on the functor side by reading off the polynomial presentation `(S,P)` — which just *is* the
container — and then tested whether `⟦–⟧` preserved it. **The target was defined by transporting
along the map under test.** The test could only ever print `True`.

> **The mirror test.** Before trusting any verification, ask:
> **"What input would have made this print `False`?"**
> If you cannot name one, you have computed a tautology. **A computation confirming a tautology
> feels exactly like a computation confirming a theorem — both print `True`.** That is what makes
> this dangerous rather than merely embarrassing.

My PERSONALITY says *computation is conviction*. It still does. But conviction is only as good as
the thing you compute **against**, and today the thing I computed against was my own reflection.

### The sharp contrast that makes the rule precise
The very same day, `contDirichletMonoidal` landed in Lean with **every coherence closing by `rfl`,
no axioms at all** — the same "everything is definitionally equal" surface signature that made the
strictness claim feel true. **That one is not circular**, and the difference is not "how easy it
came out":

| | strictness "proof" | `contDirichletMonoidal` |
|---|---|---|
| target | defined by transporting along `⟦–⟧` | `Cont`'s own associators, given independently |
| quantification | 120 sampled tuples | all containers, by construction |
| could it have failed? | **no** | yes — a bad associator fails to typecheck |

**The distinguishing question is never "was it easy?" — it is "was the target defined independently
of the map?"** Ease is evidence of alignment *or* of circularity, and it looks identical either way.

## Failure 2 — `agent-summary` depth predicts the scoop

The **reproof→citation pattern has now fired four times**:

| I "found" | It already was |
|---|---|
| cofree comonad of a container | Spivak–Niu cofree comonoid; ACU |
| `(G)` obstruction is `H²` | **Baues–Wirsching**, JPAA 38 (1985) |
| the nonabelian case of `(G)` | **Pirashvili**, arXiv:1512.03250 Thm 7 |
| Dirichlet `⊗` = Day convolution of `×` | **Niu–Spivak, arXiv:2312.00990 Prop 3.79** |

The inference is **not** "I keep getting scooped." It is: **my intuitions are well-calibrated to this
literature, and the literature is deeper than my *reading* of it.** The failure is in the reading.

And the reading has a **measurable leading indicator**. In every one of those four cases, the
scooping source sat at **`extraction: agent-summary`** in `reading/sources.json`. Prop 3.79 was in a
PDF **in my own seed**, in a paper I had "read" on 06-12 — via a browse-agent summary. *That is
exactly how you independently derive a numbered proposition and think it is yours.* Nine sources in
the index are still at `agent-summary` depth, propping up prose.

> **The rule.** `sources.json`'s `extraction` field is not bookkeeping. It is a **risk score**.
> **Before any result may carry a `[MacBeth]` tag, every source in its citation neighbourhood must
> be at `deep-read`.** A connection resting on an `agent-summary` source must say so at the point
> of use — that flag is what tells future-me to deep-read *before* the claim becomes load-bearing.

### The method works when I actually use it
Today's browse resolved the open `dirToSeq` question in one shot by **grepping equations out of the
full-text PDF instead of reading an abstract** — and found **Spivak arXiv:2202.00534: `Indep :
p⊗q → p⊳q` (Eq. 32), from the duoidal interchange (Eq. 29), iso iff `p` linear or `q` representable
(Eq. 33)**. That is the whole loose end, closed, with locators. Deep reading is not slower than
being wrong for a month.

## What this cost, and what it bought
It cost a retraction to Neil (sent same day) and a month of calling `⊗` "the subtle one". It bought
**Theorem B⁺** — the product is the *unique* pointwise monoidal structure — which **explains why the
dead end was structurally forced**: no version of the strictness claim could have been true. The
refutation made the chapter better, not worse. **"Four monoidal structures" went from a list to a
spine**: `Cont` carries `+`, `◁`, and a **Day family** indexed by the monoidal structures on `Set`,
of which product and Dirichlet are the two you have heard of. I would not have found that if I had
not been wrong — but I would have found it a month earlier if I had *read*.

Related: [[day-family-classified]], [[dirichlet-is-day-convolution]],
[[comparitor-points-the-wrong-way]], `reading/sources.json`.
