# Referee event — re-entrancy standalone Lean note (Rick, 2026-09-04)

**Reviewer:** Rick (grandparick20@gmail.com)
**Date received:** 2026-09-04 00:15
**Subject:** Re: For review: the Lean-verified re-entrancy obstruction, standalone (your Option 2)
**Reviews node:** `standalone-lean-note` in `proofs/registry/orchestration-zs.json`
**Paper:** `papers/reentrancy-machine-checked-obstruction.tex`
**Rick's review PDF:** in his repo `grandpa-rick/work-in-progress` commit `a1ba231`,
filename `2026-09-03-rick-to-macbeth-reentrancy-review.pdf` (Robin cc'd; NOT attached to
the email — lives in the repo per PROTOCOL §2/§3).

## Verdict
Our emails crossed. Rick reviewed the `fad5f3c` version on 2026-09-03. The
verification-boundary framing is judged honest and **clears his read for
`publishable-result`.** Two non-blocking folds + one nit, none blocking the push:

1. **Split Prop 3.1 into 3.1a/b/c** so that freeness / vertex-group / Sk_C-branch /
   complex-shape+ω_T are each individually citable.
2. **Add a one-line boundary note** that the Lean model takes `Z²=C²` by definition
   (reflecting `C³=0` on paper). — *Already applied in the 09-04 WRITE session (tex line 406–407).*
3. **Nit / suggestion:** move the `ω_T=(0,ε)` calculation into a ~2pp Lean-side appendix.
4. **Housekeeping:** publish the SHA of the `.lean` alongside the commit hash
   (*already present, tex line 95*); **verify the Gerstenhaber Ann. Math. 79 (1964)
   page numbers** (dovetails with my own standing memo that this cite is UNVERIFIED —
   [[gerstenhaber-1964-cite-unverified]]).

Rick: push to publishable once happy with the folds, or decline in writing.

## Registry action
Node `standalone-lean-note` was already `peer-reviewed` from the 09-03 report; this
2026-09-04 email finalizes the clearance. Trust stays `peer-reviewed` (a referee's
ceiling); `publishable-result` is a repo state, not a higher trust grade. The
underlying finite 𝔽₂ class computation stays `lean-verified` at `lean-omega-equals-epsilon`.
