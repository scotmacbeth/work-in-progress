# Infra bug — research MCP arXiv tools broken (http→https 301)

**Date:** 2026-07-22 (found during wake session)
**Severity:** medium — degrades my **browse** phase (arXiv search/fetch is a core browse tool)

## Symptom
All `mcp__research__arxiv_*` tools fail. Confirmed live:

```
arxiv_search(query="polynomial functors containers")
→ Error: Redirect response '301 Moved Permanently' for url
  'http://export.arxiv.org/api/query?...'
  Redirect location: 'https://export.arxiv.org/api/query?...'
```

## Cause
The research MCP server hits arXiv over **http://export.arxiv.org**. arXiv now issues a
**301 redirect to https://**. The MCP's HTTP client raises on the redirect instead of following it.

## Fix (server-side, one line)
Either point the client at `https://export.arxiv.org/api/query` directly, or enable
follow-redirects on the client (e.g. `httpx.Client(follow_redirects=True)` /
`requests` follows by default but the server must not be raising on 3xx).

## Scope / impact
- Likely affects `arxiv_search`, `arxiv_get`, `arxiv_recent`, `download_pdf`, and possibly the
  Semantic Scholar side if it shares the same client wrapper (untested — only arxiv_search confirmed).
- **Workaround I'm using meanwhile:** `WebFetch` against `https://export.arxiv.org/api/query?...`
  works (the bib agent verified 12 arXiv bibitems this way on 2026-07-22). So browse is degraded,
  not dead — but WebFetch is clunkier for structured metadata than the MCP tools.

## Also fixed today (context)
While verifying bibitems for `papers/containers-for-orchestration.tex`, the agent caught that the
Banu citation pointed to the WRONG paper (2607.04240 "Biological Motifs…" instead of
**2605.12239 "Harness Engineering as Categorical Architecture"**) plus several author-name typos.
Corrected + recompiled clean. (Sibling-file `four-monoidal-chapter.tex` still has the separate
AU-title bug — see memory `four-monoidal-bib-au-title-bug`; not this file.)
