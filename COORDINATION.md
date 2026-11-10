# Coordination

Shared task board for concurrent sessions. Claims use the Arena session ID. File scopes must not overlap.

## Session constraints

- Session `449ce08f-tino2` is required by Arena to work only on `arena/449ce08f-tino2`; separate session branches/worktrees cannot be created in this environment.
- Integration and publication are included in this session's claim because the repository contained no existing implementation or other claims at session start.

## Tasks

| Task | Status | Owning session | File scope | Started (UTC) |
|---|---|---|---|---|
| Source official tax, inheritance, property, insurance, housing and utility references | complete | 449ce08f-tino2 | `research/`, `site/data/sources.js`, `site/data/model.js` | 2026-11-10 |
| Build privacy-safe static dashboard and decision analysis | complete | 449ce08f-tino2 | `site/`, `assets/`, `index.html`, `.nojekyll`, `README.md` | 2026-11-10 |
| Verify calculations, sources, privacy and links; integrate and deploy | in progress | 449ce08f-tino2 | integration, PR, merge and GitHub Pages | 2026-11-10 |

## Requests to other scopes

None.

## Handoff / conflict log

None.

## Verification and publication log

- 2026-11-10: implemented eight-page static dashboard, deterministic model, 45-source official register, methodology, legal watchlist, and 22-item review queue. No private documents or identifiers added.
- `node scripts/validate.js`: 275 checks passed (model arithmetic, no rental-loss refunds, rounding, script syntax, local links, source references, HTTPS, privacy directives).
- Browser-style JSDOM runtime test: 56 assertions passed across all eight pages; interactive controls, reset, table counts and source rendering passed. Temporary test dependency installed outside the repository; site remains dependency-free.
- Local HTTP preview: all eight pages and core assets returned HTTP 200.
- Source review replaced unavailable legacy Santa Clara payment URL with current DTAC portal. Added SF File 261020 (pending, not enacted) and AB 1482's current statutory 2030 sunset to watchlist.
- Household historical irregularities remain disclosed and unverified; parcel rates, insurance quotes, trust/estate facts and rent coverage remain open without blocking publication.
- PR, merge and GitHub Pages deployment: pending.
