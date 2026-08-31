Subject: Daily: the retract is now a theorem — ⊗ is the diagonal of ▷, and the store comonad is what nesting sees that entanglement collapses

Neil,

**Yesterday** the retract I flagged to you went from `computed` to **proved**, and it grew a
third part I did not expect.

Recall the setup: Workers grades by the Dirichlet tensor (`ΔS ⊗ ΔT ≅ Δ(S×T)`, `4·y⁴` at
`|S|=|T|=2`), BHM grade by the composition product (`ΔS ▷ ΔT`, `8·y⁴`). Different products;
the "Workers is a fibre of BHM" story was false. What survives:

**(P2) The retract, as genuine Poly morphisms.** Section `σ : (s,t) ↦ (s, const_t)`,
retraction `r : (s,g) ↦ (s, g(s))` (self-evaluation), with `r∘σ = id_{Δ(S×T)}` and
`σ∘r ≠ id`. The variance is the part that needed care — a Poly morphism carries a backward
map on positions, and those compose in reverse; shape-only reasoning would have got this
wrong. Both backward maps come out identity. Verified n ≤ 3.

**(P3) Coherence.** `σ` satisfies the oplax associativity hexagon, `r` the lax one (because
self-evaluation is associative: `(s, (g(s), k(s, g(s))))`), both unit-coherent, `σ` natural
under bijections.

**(P3c) The theorem I actually like.** `r ∘ δ = Δ(d)`: the store comultiplication
`δ : ΔS → ΔS▷ΔS` is a *lift* of the `⊗`-diagonal along `r`. Read backwards, this says
**`⊗` is the diagonal of `▷`**, and the off-diagonal part `(1−e)δ` (with `e = σr` the
idempotent) measures exactly the failure of composition to be that diagonal. The store
comonad is precisely what nesting sees that entanglement collapses.

**(P3d) And an impossibility, which is why the tidy story fails.** `σ∘Δd` is coassociative
but **not counital** — so it is not a comonad, and `Δ : (Set,×) → (Poly,▷)` is oplax via `σ`
and lax via `r` **only on the core groupoid `(Set_≅,×)`**, not on all of `(Set,×)`. The
store comonad is internal to the ⊗-picture; it does not export to ▷ as a monoidal functor.

Registry `workers-retract-of-bhm-grading`, `proved`. Also shipped a referee pass on the
"containers over a base" survey — no new mathematics, three clarity fixes, 16pp, compiles
clean.

**Today** I want to close the sibling question, which is cheap and could be worth more than
the retract. BHM say the composition product is "not fibred in its left variable." My proved
T4-left result says `◁`-left-closedness (right adjoint to `(−)◁q`) is obstructed over
extensive bases and repaired exactly at tininess/dualizability of positions, where `◁`
collapses to `⊗`. Both statements say: *the left variable of composition misbehaves, and is
repaired only at representability.* Are they literally the same obstruction, or two? If the
same, T4-left gets a citable home inside a published Poly-language line and I know my
obstruction is the standard one. If different, I have a second independent axis — which
would be the more interesting answer. Either way it is a one-session question, and I am
setting it up with the cheapest falsifier named in advance (a `|S|=2` computation that
separates them), because that discipline is what caught the fibre conjecture before it
became load-bearing.

Behind it, queued: the two retract identities (`r∘σ=id`, `r∘δ=Δ(d)`) are finite and
defeq-flavoured, so they sit naturally next to the already-formalised `ΔS⊗ΔT=Δ(S×T)` in Lean.

**Still open on your side**, no urgency, just so it does not fall off: your view on the
three-graded-monad question I raised yesterday (Snoc / BHM / Workers grading by three
*different* products, your own paper inside), and whenever you get to them, the T1 fullness
flagship and the Vec-attention note.

MacBeth
