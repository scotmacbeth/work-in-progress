# Covering note — Rick (CC Robin)
## Standalone band-boundary note (extracted from §5 of the inventory gerbe note)

**Date:** 2026-10-11 · **From:** MacBeth · **Status: for referee — one prior pass only, NOT yet
independently reviewed in this standalone form.**

Rick —

I have pulled the **band** story out of §5 of the inventory gerbe note
(`papers/supply-chain-inventory-gerbe.tex`, the one you are currently re-reviewing) and written it up
as a self-contained ~8-page note: **`papers/inventory-band-boundary.tex`** ("The band boundary: the
first nonabelian obstruction of the supply-chain inventory gerbe"). It is a Strathclyde mini-course
handout and a grant beat; there is also a one-slide summary
(`papers/inventory-band-boundary-slide.md`).

**Why a standalone note.** The band is the program's first genuinely *nonabelian* content, and it was
buried as a §5 subplot behind the abelian gerbe class. Neil's course wanted it pulled forward as its
own beat. The note re-proves nothing new — it restructures the already-submitted material for a reader
who has not seen the parent note.

**What is claimed, and at what grade (please hold me to these):**

1. **Lemma (band is a strict $\operatorname{Out}$-cocycle)** and **Thm a (triviality criterion,
   $\beta=0\iff$ transport inner up to outer relabel)** + **Cor a′ (staged obstruction)** — **proved**,
   elementary Schreier; $D_4$ machine-check. *Unchanged from §5 of the gerbe note you have.*
2. **Thm b (fungible $S_n$ doubly vacuous, disjoint exceptions $n=6$/$n=2$)** — **proved**, classical
   $\operatorname{Aut}S_n$/$Z(S_n)$ arithmetic (Rotman 7.5–7.7) + explicit $S_6$ outer-automorphism
   witness. *Unchanged.*
3. **Thm c (nonvacuous band on $(\mathbb Z/p)^2 + B\mathbb Z$)** — an explicit, **machine-checked
   witness** ($\beta=[A]\neq0$), clean $S^1$ separation. *Unchanged.*
4. **§6 coupling on $T^2$ (Remark + open-problem para)** — this is **NEW relative to the gerbe note you
   have**, and I flag it explicitly as **trust grade `computed`, not refereed, not Lean-checked**. It
   reports the 10-11 witness $G=D_4\times C_2$ where a nonzero band *forces* a nonzero degree-2 lifting
   class $\delta(\beta)=[A,B]=[s]\neq0$. **Two honest corrections to my earlier framing are baked in:**
   (i) the coefficient of the connecting map is $\operatorname{Inn}G$, **not** $Z(\operatorname{Aut}F)$
   (different extension; for $D_4\times C_2$ they are abstractly isomorphic but distinct functors);
   (ii) $\delta(\beta)$ is **independent** of the band trivialisation — it is a canonical *function* of
   $\beta$, not a free parameter. Minimality over order $\le16$ is **not** claimed. The structured
   classification of banded gerbes is stated as the one open problem.

**Specific things I would value your eye on:**
- The $(\Leftarrow)/(\Rightarrow)$ Schreier argument in Thm a — is the surjectivity-of-$q$ lift step
  stated cleanly enough, and is the cocycle-preservation line ($\tilde\alpha(gf)=\dots$) watertight?
- Cor a′: is "staged" the right word, i.e. is the claim that $[\mathfrak g]$ is only *defined* once
  $\beta=0$ (not merely zero) correct as I've phrased it? I lean on your N2 feedback that an $H^2$ class
  is a splitting obstruction of an already-associative structure.
- §6, the coupling remark: is `computed` the honest grade, and is the $\operatorname{Inn}G$-vs-$Z$
  correction stated carefully enough that it does not read as overclaiming a refereed result?

Citations are all classical/deep-read (Giraud, Breen, Rotman, Ahman–Uustalu); I deliberately did **not**
cite the MathOverflow band thread (it is only at `agent-summary` in my sources), attributing the
"band up to inner automorphism" slogan to Giraud's *lien* instead.

Thanks — MacBeth
(CC Robin Langer, as always)
