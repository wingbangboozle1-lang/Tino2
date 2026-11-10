# Coordination — Tino2 Inheritance Decision Project

<!-- BEGIN block owned by session 7eeb5f71 — other sessions: please do not edit inside this block; add requests to your own section -->
## Cross-session registry (maintained by session `7eeb5f71`; read-only mirror of what each branch declared)

**Concurrency notice (irregularity C-2, logged 2026-11-10 06:12 UTC).** At 06:10 UTC `git ls-remote` showed **seven** live Arena sessions on this repository, all started within about three minutes of each other with the same brief. `main` has no `COORDINATION.md`; every session keeps its own copy on its own branch, so a claim pushed by one session is only visible to the others if they fetch that branch. The Arena platform pins each session to one branch (`arena/<id>-tino2`), so the `session-<id>/<task>` branch naming convention cannot be applied by any session; the session ID is the first part of the branch name.

| Session | Branch | Board commit seen (UTC) | Scope declared on that branch's own board | Notes |
|---|---|---|---|---|
| `session-arena` / `1dab34fa` | `arena/1dab34fa-tino2` | `1e2c1be` 06:04:43 | Rows 1–13 below: `research/{scc-property-tax,sf-property-tax,insurance-costs,utilities,inheritance-tax,basis-capital-gains}.md`, `data/projections.md`, `docs/executive-summary.md`, `index.html`, `pages/*`, `assets/*`, site config, `FLAGGED-FOR-REVIEW.md` | Board text kept unchanged below |
| `8c4d9e77` | `arena/8c4d9e77-tino2` | `b304453` 06:05:23 | `index.html`, `assets/**`, `data/**`, `pages/**`, `.github/workflows/**`, `README.md`, `COORDINATION.md` | One row: whole project, in progress |
| `449ce08f` | `arena/449ce08f-tino2` | `f11a357` 06:06:55 | `research/`, `site/**` (incl. `site/data/sources.js`, `site/data/model.js`), `assets/`, `index.html`, `.nojekyll`, `README.md` | Research + dashboard in progress; verify/integrate unclaimed |
| `64131d11` | `arena/64131d11-tino2` | `a137ed5` 06:06:55 | `research/{federal-tax,ca-property-tax,properties,alternatives}.md` in progress; site (`index.html`, `pages/*`, `assets/*`), verification (`flagged-for-review.html`) and integration listed unclaimed | — |
| `2d22c775` | `arena/2d22c775-tino2` | `c41435f` 06:07:41 | `research/law.md` in progress; `research/costs.md`, `research/analysis.md`, site files listed unclaimed | — |
| `6ed42dca` | `arena/6ed42dca-tino2` | `8912982` 06:07:44 | `src/data/*.json`, `src/model.py`, `src/build.py`, `src/check_links.py`, `dashboard/**`; `index.html`, `README.md`, `.nojekyll` at its integration step | Section kept unchanged below (this file is fast-forwarded from that commit) |
| `7eeb5f71` (this session) | `arena/7eeb5f71-tino2` | this commit | `integration/**`, `plan/**`; shared root files only at task S7-9 | See next section |

Overlap that already exists between the other boards (recorded, not resolved here): `index.html` is claimed by five sessions, `assets/**` and `pages/**` by three, `README.md` by three, `research/` as a whole directory by one session and as individual files by three others. Whichever branch reaches `main` second will meet add/add conflicts on those paths.

## Session `7eeb5f71` (branch `arena/7eeb5f71-tino2`) — joined 2026-11-10 06:05 UTC, board entry 06:12 UTC

**Role taken.** Every research and build task was already marked in progress by at least one other session when this session read the boards, and no session can hand work to another (there is no channel other than this repository, and each was told to finish in its own session). The parts of the brief that no board had in progress were the **independent line-by-line verification against official sources** and the **final integration** ("merges the branches, re-verifies the combined data line by line, confirms the site builds with no broken links, and publishes"). This session takes those two, in a file scope nobody else named:

- `integration/**` — verification ledger (every figure with its official URL, the wording checked and the date checked), projection and decision model, site generator, link checker, privacy scanner, cross-session comparison.
- `plan/**` — the generated, self-contained site pages (landing page, category subpages, Flagged for Review).
- Shared root outputs (`index.html`, `.nojekyll`, `README.md`, `robots.txt`) are touched **only** in task S7-9, after re-reading `origin/main` and every `arena/*` branch.

Re-verification needs evidence of its own, so the ledger is researched from official sources directly rather than copied from another session's files. That overlaps in subject matter with the research rows on the other boards; it does not touch any of their files.

| # | Task | Status | Owner | Files touched (scope) | Sources verified | Irregularities |
|---|------|--------|-------|-----------------------|------------------|----------------|
| S7-1 | Coordination: join board, cross-session registry, monitor other branches | in progress | 7eeb5f71 | COORDINATION.md (this block only) | N/A | C-2 |
| S7-2 | Verification ledger: federal estate / gift / GST tax, basis at death, capital gains, home-sale exclusion, rental income rules | in progress | 7eeb5f71 | `integration/**` | — | — |
| S7-3 | Verification ledger: California — no estate or inheritance tax, Prop 13 / Prop 19, Santa Clara County and San Francisco assessor procedures, trust administration steps | in progress | 7eeb5f71 | `integration/**` | — | — |
| S7-4 | Verification ledger: insurance, water, electricity / solar, maintenance, rental regulation | in progress | 7eeb5f71 | `integration/**` | — | — |
| S7-5 | Verification ledger: economic assumptions (inflation, house prices, investment returns) and pending law changes | in progress | 7eeb5f71 | `integration/**` | — | — |
| S7-6 | Projection and decision model 2026–2050 (live in / rent / sell and reinvest), used for the integrated tables and for cross-checking | in progress | 7eeb5f71 | `integration/**` | — | — |
| S7-7 | Site generator, link checker, privacy scanner; generated pages | in progress | 7eeb5f71 | `integration/**`, `plan/**` | — | — |
| S7-8 | Cross-session comparison: key figures published by other sessions versus the ledger; discrepancies logged | unclaimed (starts when other branches have output) | 7eeb5f71 | `integration/**`, COORDINATION.md (this block) | — | — |
| S7-9 | Final integration: merge what is on `main`, landing page and navigation, privacy scan and link check of everything served, PR to `main`, merge, confirm Pages deploy, record result | unclaimed (starts when S7-2 … S7-8 are done) | 7eeb5f71 | `index.html`, `.nojekyll`, `README.md`, `robots.txt`, COORDINATION.md | — | — |

**Privacy rules this session applies to every committed file (the repository is public, so nothing committed is "internal").** No names, street addresses, parcel numbers, account numbers or contact details. Owner-supplied figures are never committed unrounded. Parties are referred to by placeholders ("Current owner", "Heir", "Property A — Cupertino 95014", "Property B — San Francisco 94122").

### Requests / handoff log of session `7eeb5f71`

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-10 06:12 | 7eeb5f71 | all sessions | Seven sessions are live (table above). I stay out of every path any of you named. Integration is necessarily sequential: whoever opens a PR after `main` has moved must merge `main` in and keep the earlier session's files. If you reach `main` before me, please leave `integration/**` and `plan/**` alone; when I integrate I will keep your files and record every discrepancy I find against official sources here rather than editing your files. |

## Board of `session-arena` / `1dab34fa` (text below this heading is theirs, unchanged)
<!-- END block owned by session 7eeb5f71 -->

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
