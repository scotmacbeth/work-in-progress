# VCont plain-language note for Neil — READY TO SEND

**Status:** Written and refined this WRITE session (2026-08-22). Compiles clean
(pdflatex, 4 pages, no errors/warnings). Handoff copies:
- `for-robin/vcont-plain-note.tex` + `.pdf`
- source of record: `expository/vcont-plain-note.tex` / `.pdf`

**NOT SENT.** Write-session rules forbid email ("No email. Do not check or send
email."). WRITE.md's deliverable is the sent email to Neil (CC Robin). Resolution:
the send belongs to the next **wake** session, which emails Neil every morning
anyway. The note below is ready to paste.

## What this note is
The short, plain-language VCont note Neil asked for in his five 2026-08-21 emails:
he can't evaluate the dense linear-container math and wants a one-sitting read that
motivates it from prompt/response systems, with proved-vs-proposal made explicit.
Full theorems live in `expository/containers-over-vec.tex`.

## What I changed from the wake first-draft
The first-draft agent flagged three fixes; all now resolved:
1. **§4 collapsed from FOUR wirings to THREE.** In finite Vec, product = biproduct
   (`⊕=×`), so "choose a branch" and "hold both" are ONE wiring, not two. The note
   now states this collapse honestly as itself the clean point (it's the §2 biproduct
   collapse seen at workflow level). Three genuine wirings remain: `⊕`(menu/both),
   `⊗`(parallel), `◁`(pipeline).
2. **§4 `◁` "response-as-next-prompt"** now inline-flagged as the proposal layer.
3. **"differentiable by construction"** softened to "the hope is that… would be the
   payoff" — clearly speculative.

§5's Proved list was verified line-by-line against `containers-over-vec.tex`
(biproduct collapse §sec:collapse; extensivity crux / not-full §sec:crux;
◁-comonoid = family of k-algebras prop:comonoid; Mat(Vec)/algebroid §sec:algebroid).
Attributions (Carboni–Lack–Walters = extensivity; Bénabou/Mitchell = algebroid;
Diers = familial rep) are classical, attributed inline; no formal \cite needed.

## Ready-to-send email

**To:** neil@kodamai.com
**CC:** langer.robin@gmail.com  (always)
**Subject:** The plain-language VCont note — prompt/response, no proofs

Neil —

Here is the short version you asked for: linear containers (VCont) for
prompt/response systems, readable in one sitting, no proofs, every abstract idea
landed on a concrete example. The technical note (`containers-over-vec.tex`) has
the theorems; this one is so you can decide whether that note is worth an evening.

The through-line is your own motivation: a response is a vector because a response
is uncertain, and that uncertainty is what a learning system trains — so Vec, not
Set, is the home.

The one fact that carries everything: Set is extensive (you can always tell which
branch of a choice you're in), Vec is not. That single missing property is why
shapes go invisible (the "biproduct collapse") and why the container→functor map
stops being full. Two masks, one fact.

I've been honest about altitude. The math that's solid (biproduct collapse;
extensivity crux; ◁-comonoids = family of k-algebras; the Mat(Vec) home for
algebroids) is elementary once you accept the base change. The exciting part — the
"find a use" thrust you pushed — is a *proposal*: three workflow wirings (menu /
parallel / pipeline; note that over Vec choice and product are the *same* wiring),
with Vec chosen because responses are trainable vectors. That's the bet, clearly
marked as a bet, not a theorem.

Note attached (`vcont-plain-note.pdf`, 4 pages).

— MacBeth

## Attachment
`/home/agent/projects/expository/vcont-plain-note.pdf`
