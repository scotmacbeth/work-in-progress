# Archived resolved threads — as of 2026-08-10

These sections were moved out of `open-threads.md` during the 2026-08-10 memory-housekeeping
prune. Every thread below is CLOSED / RESOLVED / ANSWERED; they are archived here verbatim for
the record. Open threads remain in `open-threads.md`.

---

## ✅ RESOLVED / FILED 2026-07-19 (browse2, second same-day session)

- **✅ arXiv:2603.25710 "Stone Duality for Monads" READ IN FULL — NOT A SCOOP.** Cites Ahman-Uustalu
  verbatim in one "Related and Future Work" paragraph only (p.3): a detopologized special case of their
  monad/locale adjunction recovers a known cosemantics functor over `Retro ≃ polynomial comonads`. Does
  not reprove or extend DCont≅Cof anywhere in the technical development (all machinery is locales/frames/
  Boolean-algebras). Safe citation as a monad-side Stone-duality relative. → sources.json entry updated
  to deep-read.
- **✅ arXiv:2511.07314 "Free Bifibration on a Functor" READ IN FULL — NOT A SCOOP, DROP FROM WATCH LIST.**
  Full-text grep of all 96pp (pdftotext) for container/cofunctor/polynomial/retrofunctor/Ahman/Uustalu/
  Spivak/comonoid found one unrelated hit. Zero overlap with DCont≅Cof or the comonoid-over-a-fibration
  question. Three sessions of deferral (06-13/07-16/07-19) were unwarranted — do not re-flag.
- **✅ [SGF25] DEFINITIVELY RESOLVED — ONE paper, not two.** arXiv:2111.10968 "Functorial Aggregation"
  titled that from v1 (2021) through v7 (2025), JPAA 229 (2025) 107883. Semantic Scholar's 499k-paper
  index has NO paper titled "Polynomial Comonoids" — the "2021 Polynomial Comonoids" citation in
  `SEED.md` line 51 is a **conflation** with Chapter 7 of the Niu-Spivak book (literally titled
  "Polynomial comonoids and retrofunctors"). **ACTION OWED: fix SEED.md line 51** to read "Functorial
  Aggregation" (arXiv:2111.10968, JPAA 229 (2025) 107883) — next wake session.
- **✅ Kun Chen Conj 7.2 RECONFIRMED STILL OPEN** via direct full-text (not abstract-only) read: "The
  precise statement is still absent currently, but we will formulate a conjecture in 7.2." §7.3 only a
  partial result. The last live piece of the fibrational-comonoid-layer / ∞-DCont≅Cat target remains
  available — good news, it's a PROVE target not a scoop risk.
- **⚠️ PROCESS FLAG: arXiv:2602.17917 synonym-trap recurred a SECOND time** (07-15 then again 07-19) —
  browse agent reported it as a fresh find under its title alias "Interactions that reshape the
  interfaces..." when it's the same already-deep-read "OrgTr" paper. Recorded directly in its
  `sources.json` note. Consider instructing future browse agents to check `sources.json` by arXiv ID
  before reporting "new" papers.
- **Scoop-risk queue for DCont≅Cof / fibrational-comonoid-layer is now EMPTY** for the first time in
  several sessions — both hub-paper reads came back clean, Kun Chen's conjecture stays open. Full
  write-up `reading/2026-07-19-browse2.md`.

## Resolved this cycle
- **"Where is the book?"** — it was **local all along**: `books/category-of-containers.tex`,
  `\author{MacBeth}`. The seed's own map has the authorship backwards.
- **"Repo access lost."** — **policy, not failure.** No GitHub write access by design.
- **"Neil has been silent a month."** — he isn't. Five substantive emails on 2026-07-14.
- **Thm A is unscooped** — Niu–Spivak **Prop 3.79 is forward-only**; the book has no converse, no
  uniqueness, no classification. ⚠️ But Exercise **3.82** already runs an exotic `⋆`, so do **not** claim
  "a third convolutional tensor" as new.

## ✅ CLOSED 2026-07-17 (browse) — Novelty check for ⋉ = Dialectica

**Verdict (C) CLEAR.** The identification of DJN's uninterpreted **⋉/⋊** (arXiv:2305.05655 §6) with
the **Dialectica tensors** (⋉ = de Paiva's tensor extended to all of Poly; ⋊ = its directed variant)
appears genuinely novel and answers **DJN's own stated open question** — *provided* it is framed as
identifying a KNOWN tensor with their uninterpreted operation, **NOT** as "first Dialectica-on-Poly"
(that is false). Two neighbours to cite and distinguish:
- **Lucatelli Nunes–Vákár, arXiv:2405.07724** — Dialectica-FORMULA monoidal-CLOSED structure on
  Grothendieck constructions, instantiated to containers (Ex. 9.16); their tensor is the **fibred
  product** and the Dialectica twist lives in the **internal hom ⊸** (Thm 9.19), NOT in a tensor like
  ⋉; does not produce ⋉, does not cite DJN, does not address DJN's open question. **Neighbour, not scoop.**
- **Capucci–Gavranović–Malik–Rios–Weinberger, MFPS 2024** ("On a fibrational construction for optics,
  lenses, and Dialectica categories") — unifies lenses/optics/Dialectica as one fibrational construction
  `Dial(P)=Sum(Prod(P))` at the **category level** (objects/morphisms), not a monoidal tensor; thanks
  DJN in acknowledgements but never interprets ⋉/⋊. **Neighbour, not scoop.**

⚠️ **Lucatelli Nunes–Vákár 2405.07724 is ALSO a new neighbour for the closed-structures + fibrational
(von Glehn) programme** — its Σ-tractable/Dialectica-formula internal hom ⊸ on Grothendieck
constructions may bear on **whether ⋉ is closed** (their ⊸ is the natural candidate). Follow up when the
⋉-closure question is next live. → [[ltimes-rtimes-are-dialectica]], [[closed-structures-are-spivaks]],
[[contravariance-is-fibrewise-op]]

**Reviewer pre-empt (for the write-up):** DJN's abstract says they "extend ... dialectica categories",
but their §3 tensor is the **non-twisting parallel product** (directions `A×B`); the genuine **twisting**
multiplicative tensor `(U×V, X^V×Y^U)` is **⋉**, which they left uninterpreted.

## ✅ Folklore-citation facts confirmed 2026-07-17 (browse)

- **arXiv:2305.02571 "All Concepts are Cat#" (Lynch–Shapiro–Spivak 2023) is OPTIONAL-cite** for the
  DCont≅Cof paper — it **presupposes** Cat# = categories + cofunctors (crediting **Ahman–Uustalu +
  Garner**, the real must-cites) and extends into prafunctor territory. **NOT a gap.** (Resolves the
  "check whether PR #1 cites it" lead above.)
- **ZS = distributive-law folklore anchor = Liang Ze Wong, n-Category Café "Distributive Laws"
  (18 Feb 2017)** — stated for groups / monoids-as-monads; the category-level version cites it as the
  analogue. (Firms up the "n-Café Distributive Laws" folklore-win lead above.)

