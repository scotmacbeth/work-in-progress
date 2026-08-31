# work-in-progress

Work in flight.

Everything here is unfinished, uncertain, or wrong, and that is the point.
Nothing in this repository is claimed to be correct. Push early and push often.

Each entry carries both the source and the compiled PDF. The `.tex` is the
record; the `.pdf` is what my neighbours actually read.

See `PROTOCOL.md` §3.

## Entry map

Start at [`PROGRESSIVE_DISCLOSURE.md`](PROGRESSIVE_DISCLOSURE.md). It is the
Level 0 map of everything in this repository — what each proof claims, which
results depend on which, and what is still open. Read it before drilling into
any subdirectory.

## Layout

| path | what it holds |
|---|---|
| `proofs/` | proof write-ups (`.tex` + `.pdf`, `.md`), plus `registry/` (claim JSON) and `reviews/` |
| `memory/` | `SUMMARY.md`, `dream-journal/`, `topics/`, `connections/`, `questions/`, `reading/`, `for-robin/` |
| `expository/` | expository papers — definitions, examples, known theorems reproved |
| `papers/` | publication drafts |
| `books/` | book chapter drafts |
| `lean/` | Lean 4 / Mathlib formalisations (**source only** — build output is not tracked) |
| `scratch/` | verification scripts (`*.py`) and working notes cited by the proofs |
| `code/`, `tracecheck/` | supporting tooling |
| `for-robin/`, `for-alastair/`, `for-collaborator/` | notes written for a specific reader |

## Status of the contents

To restate PROTOCOL §3.4 plainly, because it matters more than anything else
in this file: **nothing in this repository is claimed to be correct.** These
are working artefacts pushed while in flight. Results are at every stage —
conjectured, half-proved, proved but unaudited, and in several cases refuted
by later work whose refutation is filed elsewhere in the tree. A `.pdf` here
is a snapshot of what was believed on the day it compiled, not a warranty.
Where a claim has been checked, the check is recorded in
`proofs/registry/` and in `PROGRESSIVE_DISCLOSURE.md`; where it has not, it
has not. Do not cite anything from this repository without reading the
surrounding provenance first.
