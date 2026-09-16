# Digest note — security case study revised: KelpDAO bridge witness folded in (2026-10-08)

**For the daily digest (Neil/Robin). Not emailed from the write session, per WRITE-session rules.**

## What changed
Revised the grant-Impact case study `expository/2026-10-04-security-audits-failed-distributive-laws.tex`
("security-audit bugs are failed distributive laws") to fold in two new incidents:

- **KelpDAO / LayerZero** (2026-04-18, ≈$290M) — the **fifth** state-divergence witness and the
  exemplar of a **new (1d) bridge sub-family**: the two non-commuting channels are the source-chain
  **settlement** channel (burn events sequenced by nonce) vs the off-chain **verification** channel
  (DVN attestation). A single zero-threshold DVN attested a forged burn at nonce 308 while the true
  sequence stood at 307 — the verification channel reported a settlement the settlement channel never
  produced, i.e. the distributive law δ: VΣ ⇒ ΣV fails at that nonce. Framed as the absence of any
  construction forcing δ; the redundant-verifier remedy is the *same categorical move* as the Venus fix
  (make δ hold by construction), now at bridge scale.
- **YieldBlox / Blend** (Stellar, ≈$10M) — a minor oracle-flavoured channel/channel instance; one row.

State-divergence class is now **five principal witnesses across four sub-families**
(module · entry-point · channel · bridge), all in one dedicated witness table.

## The punchline (grant-Impact)
The **same** categorical defect — one missing δ: ST ⇒ TS — scales from an eight-figure accounting slip
to a **$290M** cross-chain bridge exploit; only *where* the two channels sit changes. Abstract and §4
now carry this "one defect, blast radius spanning ~two orders of magnitude" statement.

## Honesty / provenance
- No new theorems. Illustrative postmortem mappings, not formal verification. The only verified claim
  invoked remains the re-entrancy [ω]=ε Lean result.
- KelpDAO/YieldBlox figures are `agent-summary`-grade (Rekt/Chainalysis postmortems), covered by the
  standing page-1 status disclaimer. No `\cite`/bibliography in the paper; citation footprint clean.
- Softened one unsourced magnitude claim ("three orders" → "~two orders", grounded by the table span
  $2.7M–$290M).

## Provenance / push
- Pushed to `scotmacbeth/work-in-progress`: content-commit **50fb999**, stamp commit **7a7ed15**.
  Page 1 stamped with content-commit 50fb999 (PROTOCOL §2.3). Compiles clean, 5pp.

## Still open / next
- The connections memory also lists **GMX V1 ($42M, module/module reentrancy)** as a witness; I did NOT
  add it to the paper (Bunni already carries module/module; GMX would be a redundant sixth). Add only if
  Neil wants a reentrancy-flavoured module/module dollar headline.
- Shape (3) self-composition still has a single witness (Hashmasks loop). More shape-3 examples remain
  the rarest and most mathematically distinctive — a future browse target (Immunefi/Code4rena).
