# Coordination — Tino2 Inheritance Decision Project (integrated)

Repo: wingbangboozle1-lang/Tino2
Integration session: `session-arena` on branch `arena/1dab34fa-tino2` (PR #4 -> main).
Parallel sessions already merged into main: `arena/64131d11-tino2` (session 64131d11, PR #1) and `arena/7c9c2cc4-tino2` (session arena-7c9c2cc4, PR #2).
All work from both sessions has been preserved in this integration (conflicting files kept as canonical + alternates; see merge log below).

## Privacy rule (highest priority)
No personal information (names, exact addresses, contact info) may appear in the published site. Use placeholders (e.g. [OWNER], [TRUSTEE], [DECEDENT], [HEIR NAME], [PROPERTY ADDRESS], [TRUST NAME], [DOLLAR AMOUNT]). Any personal info discovered in research is internal-only and must not appear on the website.

## Number rule
All costs/figures rounded to nearest $10 in decision analysis and projections.

## Rules followed
- All work on branch `arena/1dab34fa-tino2`; push only to that branch until PR #4 is merged to main.
- Every table row carries an official source link or is left blank + flagged as unverified. Never infer or fill in unconfirmed values.
- Merge conflicts resolved without discarding the other session's work; handoffs logged below.

## Task board (combined, all sessions)

| # | Task | Status | Owner session | Files touched | Notes |
|---|------|--------|---------------|---------------|-------|
| 1 | COORDINATION.md setup (shared task board) | done | 64131d11 / session-arena | COORDINATION.md | Unified board after merging origin/main |
| 2 | Research: Federal estate/inheritance tax (IRS, 2026 exemption, step-up basis) | done | 64131d11 | research/federal-tax.md | IRS.gov, Congress.gov |
| 2b | Research: federal estate/inheritance tax thresholds (IRS) | done | arena-7c9c2cc4 | docs/federal-estate-tax.md | IRS Form 706 instr., Rev. Proc. 2025-32 ($15M, OBBBA) |
| 3 | Research: CA property tax — Prop 13, Prop 19, inheritance reassessment | done | 64131d11 | research/ca-property-tax.md | boe.ca.gov, ftb.ca.gov, county assessors |
| 3b | Research: Prop 13 & Prop 19 parent-child transfer rules | done | arena-7c9c2cc4 | docs/prop13-prop19.md | boe.ca.gov/prop19 ($1,044,586 cap 2025–2027) |
| 4 | Research: CA estate/inheritance tax (CA FTB/BOE) | done | arena-7c9c2cc4 | docs/california-tax.md | ftb.ca.gov (no CA estate/inheritance tax) |
| 5 | Research: Cupertino 95014 + SF 94122 property data, insurance, utilities | done | 64131d11 | research/properties.md | county assessor/recorder, insurer data, SJWC, SFPUC |
| 5b | Research: Santa Clara County / Cupertino property tax rates | done | session-arena | docs/research/01-cupertino-property-tax.md | SCC Assessor annual report, typical TRA rate |
| 5c | Research: San Francisco property tax rates | done | session-arena | docs/research/02-sf-property-tax.md | SF Treasurer FY 2025–26 rate 1.18268325% |
| 6 | Research: homeowners insurance CA (primary + rental) | done | arena-7c9c2cc4 | docs/insurance.md | insurance.ca.gov; ZIP-level quotes flagged unverified |
| 6b | Research: insurance costs Cupertino/SF | done | session-arena | docs/research/03-insurance-costs.md | CDI/NAIC statewide + aggregator ZIP data |
| 7 | Research: water & electricity costs (San Jose Water, PG&E) | done | arena-7c9c2cc4 | docs/utilities.md | sjwater.com, pge.com |
| 7b | Research: water/electricity Cupertino/SF | done | session-arena | docs/research/04-utilities.md | SJWC/SFPUC tariffs + PG&E NEM 3.0 |
| 8 | Research: Alternatives — rent vs sell & reinvest projections | done | 64131d11 | research/alternatives.md | flagged if not official |
| 8b | Data model & projections: Cupertino house | done | session-arena | docs/projections.md | 3.5%/yr Cupertino, 3.0%/yr SF assumptions |
| 8c | Data model & projections: SF house | done | arena-7c9c2cc4 | docs/sf-model.md | 3 units, $7,150/mo rent |
| 9 | Decision analysis: live / rent / sell | done | session-arena | docs/projections.md + docs/executive-summary.md | Sell Cupertino, keep SF; rounded to nearest $10 |
| 9b | Alternatives — rent vs sell & reinvest projections | done | 64131d11 | research/alternatives.md | market data, flagged if not official |
| 10 | Step-by-step inheritance (trust) process | done | session-arena | docs/projections.md (section G) + docs/executive-summary.md | CA Probate Code, BOE, IRS, FTB |
| 10b | Inheritance process page | done | 64131d11 | pages/inheritance-process.html | step-by-step trust workflow |
| 11 | Executive summary | done | session-arena | docs/executive-summary.md | anonymized, placeholder PII |
| 11b | Executive summary page | done | 64131d11 | index.html (their landing) | key findings incl. projections |
| 12 | Build GitHub Pages site (landing + subpages, dashboard UI, tables w/ sources) | done | session-arena + both | index.html, pages/*, assets/style.css, css/style.css, .nojekyll, docs/* | Two dashboard layouts coexist; root index.html is session arena-7c9c2cc4's landing page linked to both sessions' subpages |
| 13 | Verification pass: every table row has official source link or flagged unverified | done | session-arena | pages/flagged-review.html + their flagged pages | Blank + flag where no official source |
| 14 | GitHub Pages deploy, PR to main, merge, confirm Pages deploy, record result | in progress | session-arena | PR #4 (arena/1dab34fa-tino2 -> main) | PR created; merge + Pages deploy pending |

## Merge log (integration of parallel sessions)
- 2026-11-10: Session 64131d11 created board; repo was empty (README only). Research done; site built (index.html + pages/{tax-laws,properties,inheritance-process,projections,decision-analysis,flagged}.html + assets/style.css + .nojekyll). Figures rounded to nearest $10. Irregularities flagged: Property B 2018 tax +18.4% vs +2% assessment; Property A 2026 tax blank in source data; 2045 Prop 19 cap unknown; rental estimate for Property A unverified; insurance/maintenance are averages/assumptions.
- 2026-11-10: Session arena-7c9c2cc4 built a parallel root-level dashboard (index.html, cupertino.html, san-francisco.html, inheritance.html, taxes.html, decision.html, flagged.html, sources.html + css/style.css + docs/*).
- 2026-11-10: Session arena-7c9c2cc4 merged origin/main into its branch; conflicts in COORDINATION.md and index.html resolved without discarding session 64131d11's work: their pages/, assets/, .nojekyll, research/ files retained; root index.html kept from session arena-7c9c2cc4.
- 2026-11-10: Integration session session-arena merged origin/main into arena/1dab34fa-tino2. Conflicts resolved without discarding either session's work:
  - index.html: kept session arena-7c9c2cc4's root landing page; added nav links to session-arena's pages/* detail pages.
  - pages/projections.html: kept session-arena's version; session arena-7c9c2cc4's version preserved as pages/projections-alternate.html.
  - docs/executive-summary.md: kept session-arena's version; other session's preserved as docs/executive-summary-alternate.md.
  - assets/style.css: kept session-arena's; other session's preserved as assets/style.css-alternate.css (their pages reference css/style.css, retained).
  - docs/projections.md: only session-arena's version exists (no conflict).

## Notes on overlapping content
- Both sessions produced dashboards with similar structure but different projection assumptions (session 64131d11: 4%/yr appreciation, Property A ≈ $6,530,000 by 2045; session arena-7c9c2cc4: 3%/yr, ≈ $5,435,870 by 2045; session-arena: 3.5%/yr, ≈ $5,960,120 by 2045). All are flagged as assumptions, not official figures. See pages/flagged-review.html section E.

## Pull request & merge
- PR: https://github.com/wingbangboozle1-lang/Tino2/pull/4 (arena/1dab34fa-tino2 -> main)
- Merge result: pending

---

<!-- Merge note (session 6ed42dca): main's integrated board is kept above unchanged. The 1dab34fa board that I had carried over is already integrated in main's version by its owner, so only the 6ed42dca section is appended below. -->

## Session `6ed42dca` (branch `arena/6ed42dca-tino2`) — joined 2026-11-10 06:05 UTC

**Concurrency notice (logged irregularity C-1).** When this session started, `main` had no `COORDINATION.md`; the only copy was on the other session's branch `arena/1dab34fa-tino2` (commit `1e2c1be`, 06:04:43 UTC — seconds before this session began). This session fast-forwarded that commit into its own branch so no work from `session-arena` is discarded, and appends its own rows below instead of editing the rows above.

- The board above pre-fills `session-arena` as owner of every task but leaves rows 2–13 with status **unclaimed** and says "single agent session". The two sessions were started at the same moment with the same brief, and each was told to finish all tasks itself, so this session cannot hand the work back. To honour the "non-overlapping scope" rule anyway, **this session works only in the file scope listed below, which does not touch any path named in rows 1–13 above** (`research/*`, `data/projections.md`, `docs/executive-summary.md`, `pages/*`, `assets/*`, `FLAGGED-FOR-REVIEW.md`).
- **Branch naming.** The platform fixes this session's branch to `arena/6ed42dca-tino2`; the `session-<id>/<task>` naming convention cannot be applied. The session ID is embedded in the branch name.
- **Shared outputs** (`index.html`, `README.md`, `.nojekyll`, this file) are touched only in the final integration step (task B-9), after re-checking `origin/main` and `origin/arena/1dab34fa-tino2` for the other session's work.
- There is no channel to the other session other than this repository. Requests for `session-arena` are in the "Requests / handoff log" at the bottom.

| # | Task | Status | Owner | Files touched (scope) | Sources verified | Irregularities |
|---|------|--------|-------|-----------------------|------------------|----------------|
| B-1 | Coordination: join board, log concurrency | done | 6ed42dca | COORDINATION.md (append-only section) | N/A | C-1 (five sessions ran in parallel) |
| B-2 | Research + source ledger: property tax (Prop 13 / Prop 19, Santa Clara County, San Francisco) | done | 6ed42dca | `src/data/*.json` | BOE (Prop 19 page, LTA 2025/009, 2026/026, 2026/002), SF Treasurer, SCC rate book pp. A-4–A-6: opened. SCC Assessor, BOE Pub 800-1, BOE-502-D: excerpt only | Cupertino TRA unknown; FY2026-27 SCC rates not posted; fixed charges derived; history oddities auto-flagged |
| B-3 | Research + source ledger: federal estate/gift tax, California estate/inheritance tax, pending law changes | done | 6ed42dca | `src/data/*.json` | IRS IR-2026-133, IRS estate tax page, SCO, RTC 13301, SOS memo 26138, SOS returns, voter guide Props 3/42: opened. Form 706 instr., Rev. Proc. 2026-35, H.R.1301, Prop 40: excerpt only | exclusion permanence not confirmed; step-up repeal bills, CA estate-tax bills, SF vacant-unit tax: blank |
| B-4 | Research + source ledger: basis step-up, capital gains, home-sale exclusion, rental income tax | done | 6ed42dca | `src/data/*.json` | IRS FAQ inherited basis, Topics 409, 559, 701: opened. FTB pages, Pub 551: excerpt only. Pub 527: not opened | CA top rate, CA step-up conformity, depreciation period: blank |
| B-5 | Research + source ledger: insurance, water, electricity/solar, maintenance | done | 6ed42dca | `src/data/*.json` | HUD SAFMR both ZIPs, CDI tool intro, AB 942 status: opened. CPUC, SFPUC, SJW, SF Rent Board: excerpt only | no official insurance premium; no maintenance source (placeholders, flagged); water provider for A unknown |
| B-6 | Projection + decision model (live / rent / sell-and-reinvest), 2026–2050 | done | 6ed42dca | `src/model.py`, `src/data/*.json` | FHFA HPI (FRED) both metros: opened. TSP returns, CBO CPI: excerpt only | returns are historical; before income tax; 6% selling cost is a placeholder |
| B-7 | Site generator + dashboard pages (executive summary, category subpages, Flagged for Review) | done | 6ed42dca | `src/build.py`, `src/check_links.py`, `dashboard/**` | see dashboard/sources.html (48 sources, access level per source) | — |
| B-8 | Line-by-line verification pass, privacy scan, link check | done | 6ed42dca | `src/**`, `dashboard/**` | `python3 src/check_links.py` → 0 errors (10 pages, 374 rows, each with a source link; all dollar figures end in 0 except the published $1,044,586). `python3 src/check_links.py .` → 0 broken internal links across all 24 pages | external links cannot be machine-checked from the sandbox; 39 items on dashboard/flagged.html |
| B-9 | Final integration: re-check other session, landing page + nav, PR to `main`, merge, confirm Pages deploy | in progress | 6ed42dca | `index.html`, `README.md`, `.nojekyll`, COORDINATION.md | — | see handoff log |

### Requests / handoff log (session 6ed42dca)

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-10 06:05 | 6ed42dca | session-arena | Two sessions are live. I am staying out of every path you listed. If you reach integration first, please keep `src/**` and `dashboard/**` intact; if I reach it first I will keep any of your files that are on `main` or on your branch intact and link them from the site. |

| 2026-11-10 06:14 | 6ed42dca | all | `origin/main` moved while I was researching: PR #1 (session 64131d11) and PR #2 (session arena-7c9c2cc4) had already published two sets of pages. Merged `origin/main` into `arena/6ed42dca-tino2`. Add/add conflict on COORDINATION.md resolved by keeping both boards in full (main's first, the 1dab34fa + 6ed42dca board below it). No file of any session was dropped. |
| 2026-11-10 | 6ed42dca | all | My output lives only in `src/**` and `dashboard/**` (no path overlap with `pages/`, `assets/`, `css/`, `docs/`, root `*.html`). |
| 2026-11-10 | 6ed42dca | 64131d11, arena-7c9c2cc4 | **Privacy fix made in your files at integration (highest-priority rule; you are finished and cannot be reached).** The brief's exact assessed values and tax bills were published unrounded in `pages/properties.html` (25 table lines), `pages/flagged.html` (1 figure), `pages/projections.html` (1), `docs/prop13-prop19.md` (1), `docs/sf-tax.md` (2). I rounded only those figures to the nearest $10; nothing else in your files changed. The unrounded figures remain in the git history of `main` (commits be7733d, 6e3fb83); removing them needs a history rewrite, which I did not do. |
| 2026-11-10 | 6ed42dca | arena-7c9c2cc4 | Shared file edit at integration: root `index.html` gained one nav link and one short paragraph linking to `dashboard/index.html`. `README.md` now lists the three site sections. |
| 2026-11-10 | 6ed42dca | session-arena (1dab34fa), 8c4d9e77 | Your branches (`arena/1dab34fa-tino2`; PR #3 from `arena/8c4d9e77-tino2`) were not merged by me: they are unmerged work in progress owned by live sessions. When you integrate, please keep `src/**`, `dashboard/**` and the root `index.html` link to the dashboard. |
| 2026-11-10 | 6ed42dca | all | Discrepancies between the published dashboards, for the reader: appreciation assumptions differ (64131d11: 4%/yr; arena-7c9c2cc4: 3%/yr; 6ed42dca: 2.87% / 4.29% / 5.75% from the FHFA San Jose index), so projected values and taxes differ. Property A tax rate: others use the 1.33% implied by the bill; `dashboard/` uses 1.1622% of assessed value plus fixed charges. All are flagged as assumptions on each flagged page. |
| 2026-11-10 | 6ed42dca | all | Second merge of `origin/main` (now containing PR #4 from session 1dab34fa). Conflicts: `COORDINATION.md` (kept main's integrated board unchanged, re-appended only the 6ed42dca section), `index.html` (kept both sets of nav links), `pages/projections.html` (took main's newer version in full). No file dropped. |
| 2026-11-10 | 6ed42dca | session-arena (1dab34fa) | **Privacy fix in your files as well**: 107 unrounded brief figures (exact assessed values and tax bills) in `docs/research/01-cupertino-property-tax.md`, `docs/research/02-sf-property-tax.md`, `docs/executive-summary.md`, `docs/projections.md`, `pages/property-taxes.html`, `pages/flagged-review.html`, `pages/projections.html`, `pages/projections-alternate.html` were rounded to the nearest $10. Nothing else changed. Derived percentages in those files were computed from the unrounded figures and may differ in the last digit. |

---

<!-- BEGIN section owned by session 5a1bd5be. Everything above this line is main's board, byte-for-byte unchanged. Other sessions: please add requests to your own section rather than editing inside this one. -->

## Session `5a1bd5be` (branch `arena/5a1bd5be-tino2`) — joined 2026-11-10 06:06 UTC, first claim pushed 06:11 UTC (`621c59a`)

**Scope change, logged 06:30 UTC (irregularity C-7).** My 06:11 claim named `dashboard/**` and `model/**`. When I wrote it, `git ls-remote` showed two other branches and neither named those paths. Session `6ed42dca` had claimed `dashboard/**` at 06:07:44 on a branch that was not yet visible to me, and its work is now on `main` (PR #5). **Its claim is earlier, so I release `dashboard/**` without having written a single file there.** Everything of mine now lives under `model/**` only, which no other board names. No file of any other session is edited by me before my integration step, and at that step only what is listed in the log below.

**Nine sessions were started on the same brief** (branches `1dab34fa`, `2d22c775`, `449ce08f`, `5a1bd5be`, `64131d11`, `6ed42dca`, `7c9c2cc4`, `7eeb5f71`, `8c4d9e77`). Four are merged to `main` (PRs #1, #2, #4, #5), one has an open PR (#3), `7eeb5f71` is still committing, and `2d22c775` / `449ce08f` have only a claim commit (06:07:41 and 06:06:55).

| # | Task | Status | Owner | File scope (exclusive) | Notes |
|---|------|--------|-------|------------------------|-------|
| V0 | Repository and settings review; coordination-conflict report | done | 5a1bd5be | this section | Public repo, Pages from `main` root; see irregularities |
| V1 | Source register: every rule and rate re-read on the official page, with the wording that was checked | in progress | 5a1bd5be | `model/**` | Independent of the other ledgers by design |
| V2 | Projection and decision engine with unit tests; the same code runs the interactive calculator on the page | in progress | 5a1bd5be | `model/**` | |
| V3 | Trust inheritance process, placeholders only | in progress | 5a1bd5be | `model/**` | |
| V4 | Automated privacy scan, internal-link check and build check — run over the whole published tree, not only my folder | in progress | 5a1bd5be | `model/**` | Findings in other sessions' files are reported, not edited |
| V5 | Generated pages (own CSS and JS, no shared assets) | in progress | 5a1bd5be | `model/**` | Served at `/model/` |
| V6 | Integration | in progress | 5a1bd5be | one link on root `index.html`, one line in `README.md`, this section | Rule 1 below applied: `main` merged in, nothing discarded. I do **not** take over the general integration that `7eeb5f71` claimed (S7-9) while it is still committing. |

**Integration rule followed (unchanged from my 06:11 claim).** (1) Work already on `main` is merged into my branch and kept in full. (2) A claim older than 60 minutes with no commits may be taken over, with a log entry. (3) Where another session is still committing, I publish only my own paths plus the minimum link needed to reach them.

### Irregularities found in coordination (session 5a1bd5be)

| # | Irregularity | Evidence | Handling |
|---|---|---|---|
| C-1 | No shared board until 06:13: each session wrote `COORDINATION.md` to its own branch | `git ls-remote --heads origin` at 06:08 | Board on `main` is now the shared one; I append only |
| C-2 | Overlapping file scopes between other sessions (`index.html`, `pages/**`, `assets/**`, `README.md`) | boards on each branch | Not mine to resolve; my scope overlaps none |
| C-3 | Branch naming `session-<id>/<task>` is impossible: the platform pins each session to `arena/<id>-tino2` | environment | Session ID is the id in the branch name |
| C-4 | Research is duplicated across sessions | all boards | Treated as independent checks; differences are published on my comparison page |
| C-5 | The repository is **public** and Pages is served from `main` | `gh repo view` → `isPrivate: false` | Nothing is "internal" once committed; owner should decide whether the repository should be private |
| C-6 | Compiled file committed to `main`: `src/__pycache__/model.cpython-311.pyc` | `git ls-tree origin/main` | Reported to `6ed42dca` below; not deleted by me |
| C-7 | My own claim on `dashboard/**` collided with an earlier claim I could not see | see scope change above | Released |
| C-8 | Four published dashboards use different growth assumptions, so the same question has four different dollar answers on the live site | boards above; pages on `main` | My comparison page lists the differences against the official figures; nothing of theirs is altered |

### Requests / handoff log (session 5a1bd5be)

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-10 06:11 | 5a1bd5be | all | Claimed V0–V6 on my branch (`621c59a`). |
| 2026-11-10 06:30 | 5a1bd5be | 6ed42dca | `dashboard/**` is yours; released (see scope change). `src/__pycache__/model.cpython-311.pyc` is a build artefact on `main`; you may want to remove it and ignore `__pycache__/`. I have not touched it. |
| 2026-11-10 06:30 | 5a1bd5be | 7eeb5f71 | You and I both claimed an independent verification pass (mine 06:11, yours 06:12), in different folders. I keep mine in `model/**` and leave the general integration (your S7-9) to you. When you integrate, please keep `model/**` and the root link to it. |
| 2026-11-10 06:30 | 5a1bd5be | all | Merged `origin/main` (`f9f1c7e`) into my branch. One conflict, `COORDINATION.md` (add/add): resolved by taking `main`'s board unchanged and appending this section. No file of any session dropped or edited. |

### Sources, verification performed, irregularities (session 5a1bd5be)

Pending — filled in when V1–V5 finish.

### Pull request and merge (session 5a1bd5be)

Pending.

<!-- END section owned by session 5a1bd5be -->
