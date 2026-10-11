# The band boundary — one slide
### The first nonabelian obstruction of the supply-chain inventory gerbe
*MacBeth · Kodamai · for the Strathclyde mini-course, 13–16 Oct 2026*

---

**Setup.** Supply chain = small category $\mathcal C$; inventory fibre $F$; relabelling group
$G=\operatorname{Aut}F$. Fungible stock ⟹ charts glue only up to $G$ ⟹ an **$\operatorname{Aut}F$-gerbe**
over the nerve $N(\mathcal C)$. Chart comparison = a transport $\alpha:\operatorname{Mor}\mathcal C\to\operatorname{Aut}G$,
functorial *up to inner automorphism*.

**The obstruction is STAGED (Giraud).**

| stratum | datum | class | must vanish |
|---|---|---|---|
| **band** (floor) | outer transport $\rho=q\circ\alpha$ | $\beta=[\rho]\in H^1(N(\mathcal C);\operatorname{Out}G)$ — *nonabelian* | **first** |
| gerbe class | centre cocycle | $[\mathfrak g]\in H^2(N(\mathcal C);Z(G))$ — abelian | then |

$[\mathfrak g]$ is not even **defined** until $\beta=0$.

---

**Three results.**

- **(a) Criterion.** $\beta=0 \iff$ transport is inner-valued up to an $\operatorname{Out}G$-relabelling
  of nodes (elementary Schreier). ⟹ **strict global inventory $\iff \beta=0$ AND $[\mathfrak g]=0$.**
  The old gerbe theorem is exactly the *band-trivial stratum*.

- **(b) Fungibility is doubly vacuous.** $G=S_n$: $\operatorname{Out}S_n=1$ **and** $Z(S_n)=1$ for all
  $n\ge3,\ n\neq6$. Exceptions **disjoint**: $n=6$ band-only ($\operatorname{Out}S_6=\mathbb Z/2$),
  $n=2$ centre-only. **Headline: commodity stock carries NO nonabelian obstruction — the phenomenon
  needs gauge-/torsor-structured assets.**

- **(c) Nonvacuous band.** $G=(\mathbb Z/p)^2$, $\mathcal C=B\mathbb Z$ ($N\simeq S^1$): any
  $\alpha(t)=A\neq I$ gives $\beta=[A]\neq0$, while $H^2(S^1;-)=0$ kills the centre class. Band is the
  **sole, nonzero, nonabelian** obstruction.

---

**Coupling (live lane, grade = computed).** On $S^1$ the strata decouple. On $T^2=N(B\mathbb Z^2)$ they
**talk**: witness $G=D_4\times C_2$ with two commuting outer involutions has $\beta\neq0$ and
$\delta(\beta)=[A,B]=[s]\neq0\in H^2(T^2;\operatorname{Inn}G)$ — a nonzero band *forces* a nonzero
degree-2 class. Coefficient is $\operatorname{Inn}G$, **not** $Z$. *Not yet refereed; classification of
banded gerbes is open.*

**One line.** *Beneath the abelian inventory gerbe sits a nonabelian floor — the band — invisible to
fungibility and the program's first genuinely nonabelian invariant.*
