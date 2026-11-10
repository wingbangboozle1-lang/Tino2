# Coordination — Tino2 Inheritance Decision Project

Session scope: single agent session on branch `arena/1dab34fa-tino2`. Session ID: `session-arena`.

Task board format: each row = task, status (unclaimed / in progress / done / needs review), owning session ID, files touched, sources verified (Y/N), irregularities.

| # | Task | Status | Owner | Files touched | Sources verified | Irregularities |
|---|------|--------|-------|---------------|------------------|----------------|
| 1 | Create coordination board | in progress | session-arena | COORDINATION.md | N/A | None |
| 2 | Research: Santa Clara County / Cupertino property tax, Prop 13 base-year assessment, Prop 19 parent-child transfer rules | unclaimed | session-arena | research/scc-property-tax.md | — | — |
| 3 | Research: San Francisco property tax, assessment, rental property tax treatment | unclaimed | session-arena | research/sf-property-tax.md | — | — |
| 4 | Research: homeowners insurance costs Cupertino 95014 (primary residence) and SF 94122 (rental/investment property) | unclaimed | session-arena | research/insurance-costs.md | — | — |
| 5 | Research: water (San Jose Water / SFPUC) and electricity (PG&E solar NEM) costs | unclaimed | session-arena | research/utilities.md | — | — |
| 6 | Research: federal estate tax exemption + California estate/inheritance tax, inheritance law changes pending | unclaimed | session-arena | research/inheritance-tax.md | — | — |
| 7 | Research: step-up in basis (IRC 1014), capital gains on sale of inherited home, primary-residence exclusion, rental income tax | unclaimed | session-arena | research/basis-capital-gains.md | — | — |
| 8 | Build decision model: projections of value, property tax, repairs, utilities, insurance, rent vs live vs sell | unclaimed | session-arena | data/projections.md | — | — |
| 9 | Build executive summary (anonymized, placeholders for personal info) | unclaimed | session-arena | docs/executive-summary.md | — | — |
| 10 | Create GitHub Pages site: clean landing page + category subpages, dashboard-style tables, every row with source link or blank+unverified flag | unclaimed | session-arena | index.html, pages/*, assets/*, site config | — | — |
| 11 | Verify every table row against official source; flag unverified items | unclaimed | session-arena | FLAGGED-FOR-REVIEW.md (site page) | — | — |
| 12 | Enable GitHub Pages, confirm build/deploy with no broken links | unclaimed | session-arena | GitHub Pages settings (repo) | — | — |
| 13 | Create PR from integration branch to main, summarize changes/sources/irregularities; merge; record PR link and merge result | unclaimed | session-arena | (GitHub PR) | — | — |

Rules followed: single session claims all tasks; scopes non-overlapping; small frequent commits; `git pull --rebase` before every push; unverified values left blank and flagged; personal information anonymized with placeholders; costs rounded to nearest $10.

---

## Session `6ed42dca` (branch `arena/6ed42dca-tino2`) — joined 2026-11-10 06:05 UTC

**Concurrency notice (logged irregularity C-1).** When this session started, `main` had no `COORDINATION.md`; the only copy was on the other session's branch `arena/1dab34fa-tino2` (commit `1e2c1be`, 06:04:43 UTC — seconds before this session began). This session fast-forwarded that commit into its own branch so no work from `session-arena` is discarded, and appends its own rows below instead of editing the rows above.

- The board above pre-fills `session-arena` as owner of every task but leaves rows 2–13 with status **unclaimed** and says "single agent session". The two sessions were started at the same moment with the same brief, and each was told to finish all tasks itself, so this session cannot hand the work back. To honour the "non-overlapping scope" rule anyway, **this session works only in the file scope listed below, which does not touch any path named in rows 1–13 above** (`research/*`, `data/projections.md`, `docs/executive-summary.md`, `pages/*`, `assets/*`, `FLAGGED-FOR-REVIEW.md`).
- **Branch naming.** The platform fixes this session's branch to `arena/6ed42dca-tino2`; the `session-<id>/<task>` naming convention cannot be applied. The session ID is embedded in the branch name.
- **Shared outputs** (`index.html`, `README.md`, `.nojekyll`, this file) are touched only in the final integration step (task B-9), after re-checking `origin/main` and `origin/arena/1dab34fa-tino2` for the other session's work.
- There is no channel to the other session other than this repository. Requests for `session-arena` are in the "Requests / handoff log" at the bottom.

| # | Task | Status | Owner | Files touched (scope) | Sources verified | Irregularities |
|---|------|--------|-------|-----------------------|------------------|----------------|
| B-1 | Coordination: join board, log concurrency | in progress | 6ed42dca | COORDINATION.md (append-only section) | N/A | C-1 |
| B-2 | Research + source ledger: property tax (Prop 13 / Prop 19, Santa Clara County, San Francisco) | in progress | 6ed42dca | `src/data/*.json` | — | — |
| B-3 | Research + source ledger: federal estate/gift tax, California estate/inheritance tax, pending law changes | in progress | 6ed42dca | `src/data/*.json` | — | — |
| B-4 | Research + source ledger: basis step-up, capital gains, home-sale exclusion, rental income tax | in progress | 6ed42dca | `src/data/*.json` | — | — |
| B-5 | Research + source ledger: insurance, water, electricity/solar, maintenance | in progress | 6ed42dca | `src/data/*.json` | — | — |
| B-6 | Projection + decision model (live / rent / sell-and-reinvest), 2026–2050 | in progress | 6ed42dca | `src/model.py`, `src/data/*.json` | — | — |
| B-7 | Site generator + dashboard pages (executive summary, category subpages, Flagged for Review) | in progress | 6ed42dca | `src/build.py`, `src/check_links.py`, `dashboard/**` | — | — |
| B-8 | Line-by-line verification pass, privacy scan, link check | unclaimed | 6ed42dca | `src/**`, `dashboard/**` | — | — |
| B-9 | Final integration: re-check other session, landing page + nav, PR to `main`, merge, confirm Pages deploy | unclaimed | 6ed42dca | `index.html`, `README.md`, `.nojekyll`, COORDINATION.md | — | — |

### Requests / handoff log

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-10 06:05 | 6ed42dca | session-arena | Two sessions are live. I am staying out of every path you listed. If you reach integration first, please keep `src/**` and `dashboard/**` intact; if I reach it first I will keep any of your files that are on `main` or on your branch intact and link them from the site. |
