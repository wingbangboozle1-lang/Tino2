# Coordination — Tino2 Inheritance Decision Project (integrated)

<!-- BEGIN block owned by session 4e07c8e6. It sits directly under the title, not at the end, so that it merges without conflict with the sections the other live sessions are appending at the end of this file. Other sessions: please do not edit inside this block; put requests in your own section. -->
## Live-session notice and claim of session `4e07c8e6` (branch `arena/4e07c8e6-tino2`) — 2026-11-11 07:50 UTC

**Five sessions are live at once** (same brief, started within about five minutes of each other). All 23 remote branches were fetched before this claim. Claims as pushed, oldest first:

| Session | Claim pushed (UTC) | What it claimed | Files it claimed |
|---|---|---|---|
| `246f5b3b` | 07:43:45 | Final integration, takeover of stale PR #16, privacy audit, gap fill, PR and merge | `index.html`, `site/**`, `assets/**`, `scripts/**`, `README.md`, `_config.yml` |
| `11bffb54` | 07:45:20 | Takeover of stale PR #16, gap review, final integration, PR and merge | `site/**`, `assets/app.js`, `index.html`, `scripts/validate.js`, `_config.yml`, `README.md`, `verification/11bffb54/**` |
| `14e318a1` | 07:46:31 (PR #18 merged 07:46:52) | Verification record: re-ran the existing test suite, six spot checks | `verification/14e318a1/**` — done |
| `aa1f073e` | 07:47:10 | Operating-cost research (insurance, water, electricity and solar, maintenance) and a cost page | `research/aa1f073e/**`, `verification/aa1f073e/**`, `site/operating-costs.html`, `site/data/costs.js` |
| `4e07c8e6` (this session) | this commit | Independent audit of the decision model and of the legal mechanics the decision rests on; re-check of the site after integration | `verification/4e07c8e6/**` |

**Irregularity X-C1 (claim collision, logged for whoever reads this).** `246f5b3b` and `11bffb54` each claimed final integration of the same shared files 95 seconds apart, on branches the other had not seen. By the board rule the earlier claim (`246f5b3b`, 07:43:45) holds the task. This session does not join that race: it claims no shared file and does not take over PR #16.

**Why this scope.** Every earlier verification pass either re-ran the repository's own tests (which compare the model with itself) or spot-checked a handful of headline figures. Nobody has re-derived the decision numbers with a separately written calculation, or checked the legal mechanics (how each rule works, not only its dollar amount) against the official text. That is the part of "verify line by line" still open, and it touches no file another session named.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| X-1 | Coordination: read the board and every branch, log the collision, claim a non-overlapping scope, push at once | done | 4e07c8e6 | `COORDINATION.md` (this block only) | N/A | X-C1 |
| X-2 | Legal-mechanics ledger. Open each official page directly and record the wording for every rule the decision depends on: Prop 19 formula, eligibility and deadlines; basis at death and when trust property qualifies; home-sale exclusion; rental-income rules; California conformity; federal estate and gift thresholds, filing and portability; state and local death and transfer taxes; trust-administration deadlines; rent rules that bind Property B | done (33 rules: 29 confirmed, 1 differs from the site, 3 left blank as not confirmed) | 4e07c8e6 | `verification/4e07c8e6/LEDGER.md`, `ledger.json` | IRS (estate and gift, IR-2026-133, estate FAQ, inherited-property FAQ, Topics 409, 414, 559, 701, Rev. Rul. 2023-2, Pub. 559); BOE (Prop 19 page, LTA 2025/009, LTA 2026/026); State Controller; FTB (capital gains, 2025 rate schedules); Probate Code 16061.7; RTC 480, 13301; SF Treasurer; SF Department of Elections. Every page opened on 2026-11-11; URL and wording are in the ledger | X-F1 … X-F7 in the findings table below |
| X-3 | Independent recomputation. A separately written calculation of each strategy (live in, rent, sell and reinvest) that uses only inputs already published on the site, compared with the outputs of `site/data/model.js`; every difference explained or flagged | done | 4e07c8e6 | `verification/4e07c8e6/recompute.py`, `recompute.json` | Inputs read from `site/data/model.js`; no private figure typed | All twelve headline results for 2040, 2045 and 2050 (sell, sell with growth taxed, rent, live) and both published break-even rates match to the nearest $10. One explained difference of about $500: the scenario engine grows the Property B unit rent at 1.62% (60% of 2.7%), the model input is 1.6% |
| X-4 | Brief-versus-site requirement check, read-only; findings logged below as requests to the file owners | done | 4e07c8e6 | this block | Rendered all 13 pages of `main` at `a6818a3` and read them against the brief | Findings X-F1 … X-F7 below |
| X-5 | Re-check of `main` after `246f5b3b` and `11bffb54` have merged (or have gone 60 minutes without a commit) against X-2 and X-3. Corrections to shared files are made by this session only if both integrators are done or stale at that point, and the handoff is logged here first | done: both integrators recorded `done` and merged (`11bffb54` PR #20/#22 at 07:52 UTC, `246f5b3b` PR #23/#26 at 07:59 UTC). Handoff logged below at 08:10 UTC | 4e07c8e6 | — | — | — |
| X-6 | Own PR (`verification/4e07c8e6/**` and this block only), merge, confirm Pages deploy, record the result here | in progress | 4e07c8e6 | own files + this block | — | — |
| X-7 | **Follow-up integration, narrow.** Publish findings X-F1 … X-F7 on the canonical site: new rows and sentences only, no change to the model, the navigation, the page list or any existing figure | done (see the merge record in the log below) | 4e07c8e6 | `site/data/sources.js` (three new entries), `site/plan.html` (two rows reworded, three rows added), `site/review.html` (seven items added), `site/san-francisco.html` (one row), `site/inheritance.html` (one step), `site/estate-tax.html` (one table), `index.html` (one law-watch row) | see X-2; each new row carries its official link | Checks on the edited tree: `validate.js` PASS 846 checks / 14 pages / 124 sources; `stress-test.js` PASS; `package-site.py` PASS; `check-publication.py --self-test` PASS 26 files; `runtime-test.cjs` PASS 14 pages / 1,144 source-linked rows; `qa/tools/gate.cjs` PASS 0 errors 0 warnings |

**Rules this session follows.** No personal information in any committed file. No household figure is committed unrounded, and none is repeated in this file. Every dollar figure in new files is rounded to the nearest $10 unless it is an amount published by a government body. Every table row carries a link to an official source or is left blank and marked unverified. `origin/main` is merged before every push. The platform fixes the branch name to `arena/4e07c8e6-tino2`, so the `session-<id>/<task>` naming cannot be applied.


### Findings of the audit (session `4e07c8e6`)

The published recommendation (sell Property A, keep Property B) is **confirmed**. The independent calculation reproduces every headline number, and selling stays ahead when the comparison is made on equal tax terms. The items below are what the site did not yet say. Wording and links are in `verification/4e07c8e6/LEDGER.md`; the numbers are in `verification/4e07c8e6/REPORT.md`.

| ID | Finding | Effect on the decision | Official source |
|---|---|---|---|
| X-F1 | The two published break-even rates (home prices 7.8% a year, portfolio 2.8% a year) compare a house that is sold and taxed with a portfolio that is not. On equal terms they are about 5.3% and 4.0% | The answer is less robust than the break-even cards suggest: the recorded 1976–2025 average for the metro area (6.7% a year) is above the equal-terms figure. Selling still leads in the base case | [FHFA index via FRED](https://fred.stlouisfed.org/series/ATNHPIUS41940Q) |
| X-F2 | The whole case for selling rests on the tax basis resetting at death. That holds for a revocable trust. Property in an irrevocable trust that is outside the estate keeps the old basis | If the trust is of the second kind, a sale at inheritance is taxed on the gain since purchase and the ranking has to be redone. The trust type is not known | [IRS Rev. Rul. 2023-2](https://www.irs.gov/pub/irs-drop/rr-23-02.pdf) |
| X-F3 | Prop 19 relief needs the house to be the parent's home at death. In a care facility that still counts only if the house is not rented outside the immediate family. A house held in an LLC never qualifies | Affects the live-in plan only | [BOE LTA 2026/026, Q11, Q32–35](https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf) |
| X-F4 | San Francisco Measure H (new yearly parcel tax for Muni, 15 years, inflation-adjusted) passed in the preliminary count of 3 November 2026. Not on the site's law watch | Small new fixed cost for Property B. The amount for its parcel type was not confirmed on an official page and is left blank | [SF Department of Elections](https://www.sfelections.org/results/20261103/index.html) |
| X-F5 | A house the estate holds for sale is investment property, so the selling costs can produce a deductible capital loss. If a beneficiary lives in it rent-free first, a loss is not deductible | Favors selling without moving in first. The model gives the sell plan no credit for this | [IRS Publication 559](https://www.irs.gov/publications/p559) |
| X-F6 | The model sells on the day of the inheritance. Until the sale closes, the house is taxed on its new market value and still has to be insured and kept up | About 0.15% of the house's value per month. Does not change the ranking | [BOE Prop 19](https://www.boe.ca.gov/prop19/) |
| X-F7 | The room under the federal threshold is shown in future dollars only. Stated in today's money it is smaller, because savings grow faster than the threshold is assumed to | Helps judge whether the money in the estate matters. The amount of money was not supplied | [IRS IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) |

### Requests and handoff log (session `4e07c8e6`)

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-11 07:50 | 4e07c8e6 | `246f5b3b`, `11bffb54` | You hold overlapping claims on the same files (X-C1). I am not editing any of them. Findings from my audit will be listed in this table with the official link for each, so that whichever of you integrates last can apply them. |
| 2026-11-11 07:50 | 4e07c8e6 | `aa1f073e` | Your cost research and my audit do not overlap: I am not researching insurance, water, electricity or maintenance figures. |
| 2026-11-11 08:10 | 4e07c8e6 | all sessions | **Handoff note.** Both final-integration claims are complete: `11bffb54` (E-1 … E-4 done, PRs #20 and #22 merged) and `246f5b3b` (G-1 … G-5 done, PRs #23 and #26 merged). No live session claims the shared files. This session therefore takes task X-7 above: additions to the seven files listed there, nothing else. It does not change `site/data/model.js`, `assets/**`, `scripts/**`, `_config.yml`, the page list or any published figure. If you are about to edit one of those seven files, please wait for the X-7 merge record in this table or write to me in your own section. |
| 2026-11-11 08:12 | 4e07c8e6 | `aa1f073e` | Seen: your PR #28 (merged 08:05 UTC) added `site/operating-costs.html` and `site/data/costs.js` and listed them in the publication manifest, the validator and the navigation yourself. Nothing is needed from me. Your edit to `site/review.html` is kept as is; X-7 only adds rows to that file. |
| 2026-11-11 08:09 | 4e07c8e6 | all sessions | PR [#29](https://github.com/wingbangboozle1-lang/Tino2/pull/29) (ledger, recomputation, this block, X-7 claim) **merged** 08:08:35 UTC, merge commit `b9a10f6`; PR check "Verify public Pages boundary" passed before the merge. Repository-only files; nothing on the site changed. |
| 2026-11-11 08:20 | 4e07c8e6 | all sessions | X-7 edits pushed. Not changed: `site/data/model.js`, `site/scenarios.html` (its two break-even cards still show the unequal-terms figures; the equal-terms figures are on the Best plan page and the item is on Flagged for Review), `site/verification.html`, `site/data/ledger.js`, `qa/**`, `assets/**`, `scripts/**`. Open request to any later integrator: after San Francisco certifies the 3 November 2026 results, read the Measure H text and fill in the amount for Property B. |
| 2026-11-11 08:22 | 4e07c8e6 | all sessions | **Conflict log.** `main` moved while X-7 was being pushed (PR #30, session `aa1f073e`: one more row in `site/review.html`, a correction in `site/operating-costs.html`, its research ledger, and a regenerated `qa/gate-report.json`). A rebase stopped on `qa/gate-report.json`; it was aborted and `origin/main` was merged instead, so no pushed commit was rewritten. `site/review.html` merged cleanly with both sessions' rows kept. `qa/gate-report.json` is a generated file: it was regenerated with `node qa/tools/gate.cjs` on the merged tree (14 pages, 1,145 rows, 0 errors, 0 warnings) rather than choosing either side. Nothing from `aa1f073e` was discarded. All six checks were re-run on the merged tree and pass. |
<!-- END block owned by session 4e07c8e6 -->

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
| B-9 | Final integration: re-check other session, landing page + nav, PR to `main`, merge, confirm Pages deploy | done | 6ed42dca | `index.html`, `README.md`, `.nojekyll`, COORDINATION.md | — | see handoff log |

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
| 2026-11-10 06:27 | 6ed42dca | all | **PR and merge result (session 6ed42dca).** PR: https://github.com/wingbangboozle1-lang/Tino2/pull/5 (`arena/6ed42dca-tino2` -> `main`). Result: **merged** 2026-11-10 06:27:02 UTC, merge commit `f9f1c7e`. GitHub Pages build for `f9f1c7e`: status **built**, no error. Live page fetched and read back: https://wingbangboozle1-lang.github.io/Tino2/dashboard/index.html (content matches the build). Checks before merge: `src/check_links.py` 0 errors on `dashboard/`; 0 broken internal links across all 32 pages. Still open for the owner: PR #3 (`arena/8c4d9e77-tino2`), not merged by this session; unrounded figures remain in git history. |

---

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

### Update 2026-11-10 06:30 UTC — state of `main` when this session merged it (merge commit on `arena/7eeb5f71-tino2`)

`main` moved from `61e6e58` to `cbf233b` between 06:11 and 06:19 UTC: PR #1 (`64131d11`), PR #2 (`7c9c2cc4`) and PR #4 (`1dab34fa`, which also took an integration role) were merged. PR #3 (`8c4d9e77`) is open. Two more session branches appeared after the registry above was written (`5a1bd5be`, `7c9c2cc4`), so **nine** sessions have worked on this repository. `main` was merged into this branch without discarding anything: every file from `main` is kept byte-for-byte; the only conflict was this file, resolved by keeping `main`'s board in full above, this block, and — below this block — the two board sections that existed on this branch but not on `main`.

Irregularities found on `main` at 06:30 UTC (none of them edited by this session; requests are in the log below):

| ID | What | Where | Status |
|---|---|---|---|
| P-1 | **Number rule / privacy.** Owner-supplied tax bills and assessed values are displayed **unrounded**, although the board above states "Figures rounded to nearest $10". | `pages/property-taxes.html`, `pages/properties.html`, `pages/flagged-review.html`, `pages/flagged.html`, `pages/projections.html`, `pages/projections-alternate.html`, `cupertino.html`, `san-francisco.html`, `docs/executive-summary.md`, `docs/projections.md`, `docs/prop13-prop19.md`, `docs/cupertino-tax.md`, `docs/sf-tax.md`, `docs/research/01-cupertino-property-tax.md`, `docs/research/02-sf-property-tax.md` | **Resolved on `main` by session `6ed42dca`** (PRs #5 and #6, merged 06:27–06:28 UTC, "round unrounded brief figures in other sessions' pages"). Re-scan by this session at 06:33 UTC after merging `main` again: no owner-supplied figure is displayed unrounded (the scanner's remaining exact matches are figures that were already multiples of $10). Request below withdrawn; nothing was edited by this session. |
| I-1 | Three different sets of projection assumptions and conclusions are published side by side (house-price growth 4 %, 3 % and 3.5 % a year; Property A in 2045 shown as about $6.53 M, $5.44 M and $5.96 M), with two parallel dashboards and `*-alternate*` copies. | `index.html`, `pages/projections.html`, `pages/projections-alternate.html`, `docs/*` | To be reconciled against the ledger in S7-8; shown on the Flagged for Review page. |
| I-2 | Board rows 2, 3, 5, 8 and 9b above cite `research/federal-tax.md`, `research/ca-property-tax.md`, `research/properties.md` and `research/alternatives.md`; no `research/` directory exists on `main`. | `COORDINATION.md` (rows owned by `64131d11`) | Logged; not edited. |
| I-3 | Rows 5b, 6b and 7b above describe sources that are not official ("typical TRA rate", "aggregator ZIP data"). The brief requires an official source for every row or a blank value. | `docs/research/01…04` | Each figure is being re-checked against the ledger (S7-8). |

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-10 06:30 | 7eeb5f71 | 1dab34fa, 64131d11, 7c9c2cc4 | P-1: round every owner-supplied tax bill and assessed value in the files listed under P-1 to the nearest $10. **Withdrawn 06:33 — already done on `main` by session `6ed42dca`.** |
| 2026-11-10 06:33 | 7eeb5f71 | all sessions | `main` (`540dd23`, PRs #5 and #6 of `6ed42dca`: `dashboard/**`, `src/**`, edits to `index.html`, `README.md` and rounding in other sessions' pages) merged into this branch a second time; every file kept as it is on `main`. `main` now carries three parallel dashboards (root pages, `pages/*`, `dashboard/*`). This session will not add a competing conclusion without saying which figures differ and why: task S7-8 compares every session's key figures with the ledger. |
| 2026-11-10 06:30 | 7eeb5f71 | all sessions | `integration/ledger/facts.jsonl` now holds figures checked word-for-word against official pages (IRS, U.S. Code, State Board of Equalization, State Controller, Franchise Tax Board) with the sentence that was checked. It is free to read and cite; please do not edit it — send corrections through your own section. `integration/tools/privacy_scan.py` reports unrounded dollar amounts and contact details in any file; it is safe to run before you push. |
<!-- END block owned by session 7eeb5f71 -->

---

## Board sections that existed on branch `arena/7eeb5f71-tino2` before `main` was merged (kept unchanged; superseded where the board at the top differs)

### Earlier board of `session-arena` / `1dab34fa` (commit `1e2c1be`)

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

---

## Session `449ce08f-tino2` board and publication log

Shared task board for concurrent sessions. Claims use the Arena session ID. File scopes must not overlap.

## Session constraints

- Session `449ce08f-tino2` is required by Arena to work only on `arena/449ce08f-tino2`; separate session branches/worktrees cannot be created in this environment.
- Integration and publication are included in this session's claim because the repository contained no existing implementation or other claims at session start.

## Tasks

| Task | Status | Owning session | File scope | Started (UTC) |
|---|---|---|---|---|
| Source official tax, inheritance, property, insurance, housing and utility references | complete | 449ce08f-tino2 | `research/`, `site/data/sources.js`, `site/data/model.js` | 2026-11-10 |
| Build privacy-safe static dashboard and decision analysis | complete | 449ce08f-tino2 | `site/`, `assets/`, `index.html`, `.nojekyll`, `README.md` | 2026-11-10 |
| Verify calculations, sources, privacy and links; integrate and deploy | complete | 449ce08f-tino2 | integration, PR, merge and GitHub Pages | 2026-11-10 |

## Requests to other scopes

None.

## Handoff / conflict log

- 2026-11-10: merged `origin/main` at `860df3e` (PRs #1–#7) into this branch. Root `index.html`, `README.md`, and `COORDINATION.md` conflicts resolved without deleting concurrent work. Previous main landing preserved as `research-portal.html` and linked from `site/sources.html`; all previous pages, models, source ledgers and board sections retained.

## Verification and publication log

- 2026-11-10: implemented eight-page static dashboard, deterministic model, 45-source official register, methodology, legal watchlist, and 22-item review queue. No private documents or identifiers added.
- `node scripts/validate.js`: 275 checks passed (model arithmetic, no rental-loss refunds, rounding, script syntax, local links, source references, HTTPS, privacy directives).
- Browser-style JSDOM runtime test: 56 assertions passed across all eight pages; interactive controls, reset, table counts and source rendering passed. Temporary test dependency installed outside the repository; site remains dependency-free.
- Local HTTP preview: all eight pages and core assets returned HTTP 200.
- Post-merge `node scripts/validate.js`: 276 checks passed. `python3 src/build.py`: rebuilt 10 existing dashboard pages (39 flags, 48 sources). `python3 src/check_links.py .`: 40 pages / 871 rows / 124 external links, 0 errors; 59 warnings for exact historical/research figures, including intentionally exact household bill inputs. `integration/tools/privacy_scan.py` completed in the combined check with no error.
- Source review replaced unavailable legacy Santa Clara payment URL with current DTAC portal. Added SF File 261020 (pending, not enacted) and AB 1482's current statutory 2030 sunset to watchlist.
- Household historical irregularities remain disclosed and unverified; parcel rates, insurance quotes, trust/estate facts and rent coverage remain open without blocking publication.
- PR [#8](https://github.com/wingbangboozle1-lang/Tino2/pull/8) merged to `main` at 2026-11-10 06:48:43 UTC; merge commit `4c465bbeb7ab5c965a31ed0b3dae80a91db7be03`. PR state clean/mergeable; GitHub reported no PR-specific checks, with local/model/runtime/build/link/privacy validations recorded above.
- GitHub Pages [run 42771015838](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/42771015838) completed `success` for merge commit `4c465bb`; build, report-build-status and deploy jobs passed. Pages API reports `built`, `main` / root, HTTPS enforced.
- Public deployment confirmed at https://wingbangboozle1-lang.github.io/Tino2/ (cache-busted fetch after deployment), `/site/decision.html`, and `/research-portal.html`; rendered base case and source links present. Final coordination-record PR contains documentation only.

### Conflict log — 2026-11-11 merge of `origin/main` into `arena/d7d62f7a-tino2`

Two sessions built overlapping stress sections. `origin/main` already contained session `516f904c`'s 50-year path laboratory (`site/stress.html`, `site/data/stress.js`) and its estate-ownership correction; this branch contained the recorded-episode replay page (`site/scenarios.html`, `site/data/scenarios.js`). Nothing was discarded:

- Both stress pages are retained and cross-linked. `stress.html` stays the long-horizon (2045→2095) path laboratory and remains the navigation entry; `scenarios.html` is the recorded-episode replay to 2055 with break-even thresholds, premium and catastrophe sensitivities and law-risk table, reachable from `stress.html`, `decision.html` and the landing page.
- `site/sources.js` keeps both source sets (61 keys). The register marks both sessions' checked sources as checked on 11 Nov 2026.
- `site/sources.html` conflict resolved by keeping main's per-source review-status column and adding this session's eight newly checked keys to it.
- The estate-ownership correction from `516f904c` is authoritative: only Property A is in the decedent's real-estate-only headroom. This session's scenario page was corrected to match.


## Session 516f904c — 2026-11-11 privacy and reliability integration

| Task | Status | Owner | Scope |
|---|---|---|---|
| Audit public privacy, remove exact household fingerprints, verify current-law sources, add nonconstant economic stress paths, validate and publish | in progress | 516f904c | canonical `site/`, `assets/app.js`, root landing, source/model tests, publication allowlist, legacy privacy redaction, coordination |

All previous claims predate this session by over 60 minutes and are complete or stale. No currently active competing claim found. This session is final integrator. Arena requires the fixed branch `arena/516f904c-tino2`; no alternate branch will be created. Previously published exact household histories are a privacy irregularity: rounding is not anonymization and public Git history cannot be erased by a site change. Remove histories from the published artifact and redact exact household amounts from working files. Official rules and hypothetical projections remain distinct.

### 516f904c audit results and publication scope
- Corrected the estate ownership bug: B belongs to the heir; decedent real-estate-only headroom uses A only ($11,900,000 in the 2026 illustration). Actual estate tax and missing components remain blank.
- Withheld exact household history arrays and tables from the canonical dashboard. Rounded initial assessment inputs; factual verification worksheet leaves unknown amounts blank. Prior public Git history/cache exposure is flagged prominently, not claimed erased.
- Replaced misleading historic total-bill ratios with A hypothetical 1.2% and B carried-forward ad valorem scenario excluding unknown direct charges. Added caveats; no quote/appraisal is fabricated.
- Added five automatic 50-year (2045–2095) paths with variable annual home/portfolio/inflation rates, early and late crashes, stagflation, uninsured repair, vacancy, nominal/real endpoints, live/rent/sell comparisons and 250 annual rows. Hypotheses are explicitly not official forecasts or probabilities; missing recapture, financing and estate tax remain flagged.
- Sources reopened 2026-11-11: https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax ; https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes ; https://boe.ca.gov/prop19/ ; https://www.sco.ca.gov/ardtax_estate_tax.html ; https://www.bls.gov/news.release/archives/cpi_01122023.htm ; https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance ; https://www.insurance.ca.gov/01-consumers/105-type/5-residential/index.cfm . An initial BLS TED URL returned not-found and was replaced by the official archived release. Other source-register notes are carried-forward and labeled needs revalidation, not newly verified.
- Validation: 294 static/model/source-reference checks; stress path/ownership/real-dollar tests; JSDOM rendered all 9 canonical pages, 510 source-linked table rows, zero runtime errors or broken local links. Source links in model rows are labeled framework/context, not evidence for hypothetical values. External links are not all newly reverified.
- Deployment permission irregularity: Pages API GET works; update Pages mode and Actions permissions APIs return HTTP 403 (integration scope). Retain existing main/root legacy Pages build and use Jekyll `_config.yml` exclusions. Removed `.nojekyll` deliberately so exclusions are honored. No credentials requested. Local allowlisted packaging/privacy check passes. Older research scopes retained in Git, excluded from site.
- Initial claim push: remote session branch did not exist, so `pull --rebase` used `origin/main` before first branch push. No conflict or discarded work.

### 516f904c publication result
- PR https://github.com/wingbangboozle1-lang/Tino2/pull/10 merged without waiting for approval on 2026-11-11 at 04:11:17 UTC; merge commit `e768898f6e87311adb37b0cdc08fc9614c8cf6d1`.
- Pages run https://github.com/wingbangboozle1-lang/Tino2/actions/runs/42957581416 completed success: Jekyll build, artifact upload, deploy and status report all passed. Nonblocking platform annotations concern Node action runtime deprecation and Ubuntu runner migration, not site errors.
- Public fetch confirmed updated executive summary at https://wingbangboozle1-lang.github.io/Tino2/ and rendered 50-year scenario tables at https://wingbangboozle1-lang.github.io/Tino2/site/stress.html . Legacy `/dashboard/properties.html` no longer returned the former historical dashboard (GitHub error page); HTTP removal status could not be independently established by fetch tooling. Artifact-download confirmation was blocked by outbound restrictions on Azure blob artifact storage; do not claim a downloaded-artifact audit. `_config.yml` lists all legacy published paths as exclusions.
- Follow-up: persist rendered-page test for reproduction, retain official context links after control changes, and correct overview metric labels to say decedent A only. All 294 checks, stress tests and 9-page/510-row runtime validation pass again.
- Task status: done for implementation, modeling, current-session source review and deployment; needs review for legacy source revalidation, property-specific private records, and prior public Git/cache exposure. These open items are published on Flagged for Review and do not block publication.

---


---

## Session `d7d62f7a` board — black-swan / real-conditions section (integration)

Claimed 2026-11-11. Repo state at claim: `main` at `016eb53` (PR #9 merged), working branch `arena/d7d62f7a-tino2`, `node scripts/validate.js` PASS 276 checks, `python3 src/check_links.py .` 0 errors. The eight-page dashboard under `site/` is live at https://wingbangboozle1-lang.github.io/Tino2/ with Pages status `built`.

| Task | Status | Owner | File scope |
|---|---|---|---|
| Black-swan / real-economic-conditions section: add scenario engine, page, nav entry, validation | in progress | d7d62f7a | `site/data/scenarios.js` (new), `site/scenarios.html` (new), `site/data/sources.js` (append-only), `assets/app.js` (nav), `scripts/validate.js`, `index.html`, `site/sources.html`, COORDINATION.md |
| Re-verify existing eight pages line by line; keep published numbers unchanged | in progress | d7d62f7a | read-only |
| PR to `main`, merge, confirm Pages | pending | d7d62f7a | — |

Notes: no other session is active; every other listed claim is `done`. This session edits shared outputs (`index.html`, nav) only because no other session holds them. Existing pages and their figures are left intact; all new content is additive and clearly labelled.

### Session `d7d62f7a` — completion record

- 2026-11-11: added `site/data/scenarios.js` (recorded-episode stress engine) and `site/scenarios.html` (shock-replay section), plus nav entry, landing-page card, decision-page cross-link, four review items, eight official sources and README notes.
- Merged `origin/main` (session `516f904c`'s 50-year stress laboratory, estate-ownership correction and privacy audit) into this branch. Two conflicts, both resolved without discarding work: `site/sources.html` keeps main's per-source review-status column with this session's eight newly checked keys added; `COORDINATION.md` keeps both session records. Result: ten dashboard pages, 56 official sources, two complementary stress pages (`stress.html` to 2095, `scenarios.html` to 2055) cross-linked and labelled distinctly in navigation.
- Ownership correction from `516f904c` adopted: only Property A is in the decedent's real-estate-only headroom ($11,900,000 for 2026), and this session's scenario page was corrected to match.
- Engine reproduces `MODEL.decision()` exactly at base assumptions (2045 transfer, 2055 endpoint): sell $9,125,343 · rent $7,395,618 · live $6,034,608.
- Results (recomputed after the merge): selling leads on money in 6 of 7 cases; renting wins only in the stagflation replay ($9,904,099 vs $8,236,335); break-even 7.8% home growth or 2.8% after-tax portfolio return; 12% premium growth costs the rent case $198,810 over ten years; a 10% uninsured earthquake loss removes $970,780 from every strategy; the Prop 19 exclusion is worth $15,280 a year at 2045.
- Sources added (opened and read this session): BLS historical CPI-U PDF and annual CPI table, Freddie Mac PMMS and 2021 archive, FHFA HPI datasets and Q3 2008 release, USGS Bay Area earthquake probabilities, CBO publication 61882, California FAIR Plan key statistics.
- Checks after the merge: `node scripts/validate.js` PASS 421 checks / 10 pages / 56 sources; `node scripts/stress-test.js` PASS; `node scripts/runtime-test.cjs` PASS 10 rendered pages / 567 source-linked rows / no runtime errors; `python3 scripts/package-site.py` PASS; privacy scan and link check rerun below.
- Irregularities flagged (published, non-blocking): subjective scenario weights; unverified $1,500 premium guess; Property A original basis absent, so step-up repeal is priced only per $1,000,000 of gain; no official retrofit cost, so catastrophe exposure is a share of value; whether renting Property B's vacant unit changes assessment or coverage is unverified.
- PR [#12](https://github.com/wingbangboozle1-lang/Tino2/pull/12) — black-swan and real-conditions stress section, rebased onto main and merged without waiting for approval.


### Session `d7d62f7a` — merge and publication result

- PR [#12](https://github.com/wingbangboozle1-lang/Tino2/pull/12) merged to `main` on 2026-11-11 at 04:15:23 UTC without waiting for approval; merge commit `89a6a30923f0ad4779250dda856cdb01319a5472`. State `MERGED`, mergeable/clean at merge time.
- GitHub Pages run [42958030157](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/42958030157) completed `success` for merge commit `89a6a30`: build, report-build-status and deploy jobs all passed.
- Public deployment confirmed by cache-busted fetches: https://wingbangboozle1-lang.github.io/Tino2/site/scenarios.html renders the stress-case tables and source links; https://wingbangboozle1-lang.github.io/Tino2/site/stress.html still renders the 50-year laboratory with its cross-link to the replay page.
- Final state on `main`: 10 dashboard pages, 56 official sources, `node scripts/validate.js` 421 checks, `node scripts/stress-test.js` PASS, `node scripts/runtime-test.cjs` PASS (10 pages, 567 source-linked rows), `python3 scripts/package-site.py` PASS, link check and privacy scan 0 errors.
- Status: implementation, modelling, current-session source verification and deployment are done. Needs review: the household-input and legal items listed on the Flagged for Review page, plus revalidation of carried-forward sources (the register marks which ones this session checked).

---

## Session `457907c1` (branch `arena/457907c1-tino2`) — joined 2026-11-11 04:19 UTC

**State at join.** `main` = `7a8c80e` (PRs #1–#13 merged; GitHub Pages live from `main` / root). This session read `COORDINATION.md` in full and fetched every live `arena/*` branch before claiming. Live in-progress claims found (all pushed <60 minutes before this claim, so **not** stale): `e03a1cbe` (`plan/**`), `70f163d0` (rounding pass + `site/black-swan.html` + `research/verification-2026-11-11.md`), `f16e6e34` (`qa/**`, PR #3 triage, final integration F-6 waiting), `5c9d68b9` (`inherit/**`), `c8786419` (privacy audit, needs review). Completed and not re-opened: `516f904c` (privacy/stress, PRs #10–#11), `d7d62f7a` (black-swan scenarios, PRs #12–#13), `449ce08f` (dashboard, PRs #8–#9), and earlier sessions.

**Claimed scope (new paths only — no file owned by another session is edited).** This session does **not** take the final-integration/nav/landing role (claimed by `f16e6e34` F-6, `5c9d68b9` F-6, `70f163d0` C-4, `e03a1cbe` E-14) and does not edit `site/**`, `index.html`, `pages/**`, `dashboard/**`, `docs/**`, `docs/research/**`, `qa/**`, `plan/**`, `inherit/**`, `research/**`, `scripts/**`, `src/**`, `integration/**` (requests to those owners go in the log below).

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| V-1 | Coordination: read all boards/branches, claim non-overlapping scope, push claim immediately | done | 457907c1 | `COORDINATION.md` (this section only) | N/A | None |
| V-2 | Post-merge verification of the combined `main` tree: full test suite (`scripts/validate.js`, `scripts/stress-test.js`, `scripts/runtime-test.cjs`, `scripts/package-site.py`, `src/check_links.py`, `integration/tools/privacy_scan.py`), Pages API deploy status for the current merge commit, broken-link and privacy status | done | 457907c1 | `verification/457907c1/REPORT.md` | 6/6 checks PASS on merged tree (`a841d23`); Pages run `success`; privacy scan 0 errors / 42 warnings (all non-household, other sessions' files) | V-I-1…V-I-4 in REPORT §5 |
| V-3 | Independent spot re-check of key published legal/tax figures against official sources (IRS 2026 basic exclusion, Prop 19 exclusion amount, county tax rates, rent rules, HUD SAFMRs, trust/assessor deadlines) using direct fetches; every check recorded with the official URL and access date | done | 457907c1 | `verification/457907c1/REPORT.md` §3 | 10/10 official pages opened 2026-11-11 (IRS, SCO, BOE NR 25-02, SF minutes Res. 524-26, SF Rent Board ×2, HUD SAFMR ×2, Prob. Code §16061.7, BOE pub800-9); all Match | none — 10/10 Match |
| V-4 | Publish this session's verification report and coordination record via own PR to `main`, merge without waiting, confirm Pages deploy, record PR link + merge result here | done | 457907c1 | `verification/457907c1/REPORT.md`, `COORDINATION.md` (this section) | PR #15 merged; Pages run 42961279245 success; report live | none |

**Rules this session follows:** privacy first (no personal information in any committed file; no household figure repeated in this file), all dollar figures in new files rounded to the nearest $10, every table row in the new report carries an official source link or is left blank + flagged unverified, small frequent commits, `git pull --rebase` equivalent (merge `origin/main`) before every push, conflicts resolved without discarding other sessions' work.

### Requests / handoff log (session 457907c1)

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-11 04:19 | 457907c1 | all sessions | I claim only `verification/457907c1/**` + this COORDINATION section. I will not touch shared outputs or any path listed above. Findings that belong on a flagged page I cannot edit are logged here for the owner of that page. |

### Session `457907c1` — publication result

- PR [#15](https://github.com/wingbangboozle1-lang/Tino2/pull/15) (`arena/457907c1-tino2` -> `main`) merged without waiting for approval on 2026-11-11 at 04:45 UTC; merge commit `d161c3abd50732d2844b4e03a7cb14e107750af3`. State `MERGED`, `mergeable/clean` at merge time.
- GitHub Pages run `42961279245` for `d161c3a` completed `success` (build, report-build-status, deploy). Pages API: `built`, source `main` / root.
- Live confirmation: https://wingbangboozle1-lang.github.io/Tino2/verification/457907c1/REPORT.md renders the full report on the deployed site; the landing page renders the executive summary, decision preview with per-row source links, and links to all 10 category pages including the three black-swan/stress pages.
- Verification results on the tree merged into the PR (based on `a841d23`): 6/6 automated checks PASS (581 validations / 11 pages / 70 sources; 11 rendered pages / 763 source-linked rows; 54 pages / 871 rows link check; privacy scan 0 errors); 10/10 independent official-source spot re-checks Match (IRS, SCO, BOE, SF minutes, SF Rent Board, HUD, Probate Code — URLs in the report).
- Merge log note: one conflict in `COORDINATION.md` when integrating PR #14 (session 70f163d0) was resolved by keeping both session sections in full; no other session's work was discarded.
- Open flagged items recorded in report §5 (V-I-1 non-$10 research averages in other sessions' legacy files; V-I-2 jsdom env note for runtime test; V-I-3 external links not machine-checkable; V-I-4 legacy dashboards pending final integration). Non-blocking per brief.

## Session `70f163d0` (branch `arena/70f163d0-tino2`) — claim, overlap and completion

**Claim history.** Claim table (C-1 privacy rounding, C-2 black-swan page, C-3 re-verification, C-4 nav/landing/PR) was committed and pushed to `origin/arena/70f163d0-tino2` at 2026-11-11 ~03:55 UTC. Sessions `516f904c` and `d7d62f7a` read only `main`, never saw that branch, and merged overlapping work (PRs #10–#13) before this session's PR. Per protocol nothing of theirs was discarded: this session merged `origin/main` into its branch and took main's version of every conflicting file, then re-applied only additive work.

**What main already covered (accepted as canonical):** privacy withdrawal of exact household histories and hypothetical tax rates (`516f904c`), estate-ownership correction, `site/stress.html` (2045–2095 paths), `site/scenarios.html` (recorded-episode replays to 2055), Jekyll publication allowlist (`_config.yml`, `scripts/package-site.py`). C-1 is therefore superseded: this session's $10 rounding of history tables was dropped in the merge because main withholds those tables entirely (stricter). Flagged on the review page: the rule said "rounded"; the site withholds.

**What this session added (additive):**
- `site/black-swan.html` ("Recorded data" in nav), `site/data/history-engine.js` (`window.SCEN`), `site/data/history.js` (generated by `scripts/build-history.py` from `research/data/fred_annual_2026-11-11.csv`): twelve scenarios replayed from official annual series 1970–2025 (BLS CPI-U, FHFA HPIs for San Jose MSA / SF / California, 10-yr Treasury, Freddie Mac mortgage rate, OECD share prices), 2,000-path seeded block-bootstrap Monte Carlo, Property B exposure table, year-by-year 2026–2076 table with CSV download, full data table.
- Tax-symmetric check of the sell case (`terminalAfterLiquidation` in `MODEL.decision`, shown on the Decision page and landing summary).
- Prop 19 cap now compounds at scenario home-price growth in completed two-year steps (BOE indexes to FHFA California HPI) instead of 2% per two years; text updated on Decision/Properties/Sources/Review/Shock-replays pages. `decision` results for the live case moved accordingly.
- 14 new sources (7 FRED series, CBO outlook, BOE LTA 2026/026, SOS ballot results, CA Props 40/42/43 guides, SF Rent Board rent-increase page) in a separate `Object.assign` block at the end of `site/data/sources.js`; watchlist rows for Props 40/42/43 and SF File No. 261020; nine new review items; three assumption rows.
- `scripts/validate.js` +147 checks (engine equals lab at 9 combinations incl. tax-symmetric result, CSV-to-history integrity, Monte Carlo reproducibility, Prop 19 indexing); `scripts/package-site.py` forbidden-amount test now matches whole numbers only (it false-positived on index decimals in `history.js`).
- `research/black-swan.md`, `research/verification-2026-11-11.md` (not published: `research/` is Jekyll-excluded).

**Re-verification this session (official pages read 2026-11-11):** IRS $15,000,000 exclusion; BOE NR 25-02 Prop 19 amount $1,044,586 for 2025-02-16 to 2027-02-15 (indexed to FHFA California HPI); BOE LTA 2026/026 formula and trust rule; SCO California estate tax; HUD FY2026 SAFMR for both ZIPs (3BR $5,870, 4BR $6,390, 1BR $2,730); SF Rent Board 1.6% (60% of Bay Area CPI) and $59/unit fee; all seven FRED series re-read in full and matched to the CSV; CBO Feb 2026 outlook (qualitative). Not verified (flagged): CBO 2.3% / 4.4% exact figures, SF 7% ceiling, SF FY2026-27 rate table (minutes page 1 of 9 read), insurance, household inputs.

**Checks after merge:** `node scripts/validate.js` PASS 581 checks / 11 pages / 70 sources; `node scripts/stress-test.js` PASS; `node scripts/runtime-test.cjs` PASS 11 rendered pages / 763 source-linked rows; `python3 scripts/package-site.py` PASS.


## Session `11bffb54` (branch `arena/11bffb54-tino2`) — claim 2026-11-11 07:50 UTC

State read at claim: `main` at `240f255` (PR #17). Every earlier claim is `done` or older than 60 minutes with no commits. PR #16 (`arena/f16e6e34-tino2`, last commit 04:46 UTC, mergeable/clean, never merged) is stale by the 60-minute rule and is **taken over** by this session: its branch is merged into this branch unchanged, re-checked, and carried to `main` through this session's PR. Arena fixes the branch name, so `session-<id>/<task>` naming cannot be used.

| # | Task | Status | Owner | File scope |
|---|---|---|---|---|
| E-1 | Take over stale PR #16: merge `origin/arena/f16e6e34-tino2`, rerun every validator | done | 11bffb54 | files of PR #16 (merge only) |
| E-2 | Brief-vs-site gap review, line by line; independent re-check of key figures against official pages | done | 11bffb54 | read-only + `verification/11bffb54/**` |
| E-3 | Close gaps found in E-2 (final integration: canonical `site/**`, `assets/app.js`, `index.html`, `scripts/validate.js`, `_config.yml`, `README.md`) | done; open items are needs review (published on Flagged for Review) | 11bffb54 | as listed |
| E-4 | PR to `main`, merge, confirm Pages deploy, record result | done | 11bffb54 | COORDINATION.md (this section) |

### Session `11bffb54` — completion record (2026-11-11)

- **Handoff / merge log.** PR #16 was open, mergeable and untouched since 04:46 UTC (over 60 minutes), so it was taken over. Merging `origin/arena/f16e6e34-tino2` gave one conflict, in `COORDINATION.md`; both sessions' sections were kept in full. No other file conflicted and nothing was discarded.
- **Sources opened and read by this session** (wording recorded in `verification/11bffb54/REPORT.md`): IRS What's new, estate and gift tax ($15,000,000 for 2026) https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax ; IRS IR-2026-133 ($15,480,000 for 2027; gift exclusion $19,000 / $20,000) https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts ; State Controller, California estate tax https://www.sco.ca.gov/ardtax_estate_tax.html ; IRS inherited-property basis https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances ; BOE LTA 2025/009 ($1,044,586; one prior calendar year's index change; next adjustment February 2027) https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf ; BOE Proposition 19 comparison chart https://boe.ca.gov/prop19/ ; SF Rent Board 1.6% https://www.sf.gov/news--annual-rent-increase-3126-22827-announced . All seven matched the site. Other facts keep the status given by the session that added them; they were not re-opened here.
- **Changes.** (1) Household tax and assessment history published rounded to $10 on the Verified facts page, each row marked unverified, as the owner's brief specifies (an earlier session had withheld it; the Flagged item now records the restoration and how to reverse it). (2) Landing page links Best plan and Verified facts and states the official 2027 exclusion. (3) Sources watchlist row for the federal exclusion updated to the published 2027 amount.
- **Checks on the final tree.** `node scripts/validate.js` PASS 737 checks / 13 pages / 100 sources; `node scripts/stress-test.js` PASS; `python3 scripts/package-site.py` PASS (rounding rule); `node scripts/runtime-test.cjs` PASS 13 pages / 963 source-linked rows / no broken local links; `node qa/tools/gate.cjs` PASS 0 errors, 0 warnings; scan of every tracked file for the exact household figures: 0 hits.
- **Irregularities (needs review; published on Flagged for Review; non-blocking).** Exact household figures remain in public commit history and older branch tips (owner decision: private repository, fresh repository, or GitHub Support purge); no official insurance premium for either home; Property A tax-rate area and both properties' direct charges unconfirmed; repeated yearly amounts in Property A's tax history and the 2018 jump in Property B's; legacy parallel dashboards remain in the repository but are excluded from the published site.

### Session `11bffb54` — PR and merge result

- PR: https://github.com/wingbangboozle1-lang/Tino2/pull/20 (`arena/11bffb54-tino2` -> `main`). **Merged** without waiting for approval on 2026-11-11 at 07:49:54 UTC (GitHub timestamp); merge commit `660be98`. PR #16 now shows as merged as well, because its commits are contained in PR #20.
- Before the merge `main` had moved (PRs #18 and #19, session `14e318a1`, `COORDINATION.md` and `verification/14e318a1/` only). A `pull --rebase` stopped on a `COORDINATION.md` conflict; the rebase was aborted and `origin/main` was merged instead, keeping both sessions' sections in full. All checks were re-run on the merged tree and passed.
- GitHub Pages run `42982370249` for `660be98`: completed, **success**. Pages API status: `built`.
- Live fetch after the deploy: https://wingbangboozle1-lang.github.io/Tino2/ and https://wingbangboozle1-lang.github.io/Tino2/site/verification.html both returned the rendered dashboard (the first attempt returned a temporary GitHub error page; the retry succeeded). The fetched portions did not include the new history table or the two new landing cards, so those were confirmed from the successful build of the merge commit rather than read back from the live page.

## Session `f16e6e34` (branch `arena/f16e6e34-tino2`) — joined 2026-11-11 04:08 UTC

**State at join.** `main` = `016eb53` (PRs #1–#9 merged, Pages live from `main` / root). Before claiming, this session fetched **all 13 remote branches** (claims made by other sessions are only visible on their own branches, because the platform confines every session to its own `arena/<id>-tino2` branch).

**Live claims found on other branches (not visible on `main`) — recorded here so they are in one place.**

| Session | Branch | Claim pushed (UTC) | What it claimed |
|---|---|---|---|
| c8786419 | `arena/c8786419-tino2` | 2026-11-11 04:06:58 | Privacy / verification audit of the published site (append-only findings, status `needs review`) |
| 516f904c | `arena/516f904c-tino2` | 2026-11-11 04:07:19 | Privacy remediation of `site/`, `assets/app.js`, root landing, tests, publication allowlist, legacy redaction, non-constant economic stress paths, publish |
| e03a1cbe | `arena/e03a1cbe-tino2` | 2026-11-11 04:07:26 | New `plan/**` tree: fact re-verification, black-swan scenario research, after-tax projection engine, canonical dashboard, root `index.html` at integration |
| 70f163d0 | `arena/70f163d0-tino2` | 2026-11-11 04:07:29 | $10 rounding of household figures across `site/**`, `docs/**`, `pages/**`, `dashboard/**`, root `*.html`, `src/**`, `integration/**`, `scripts/validate.js`; `site/black-swan.html`; re-verification notes; nav/landing |

Irregularity **F-C1 (coordination race):** those four claims were pushed within 31 seconds of each other on separate branches, so none of them could see the others. Their scopes overlap with each other (privacy rounding ×2, black swan ×3, landing page ×3, "final integrator" ×3). This session arrived last, saw all four, and therefore **does not start any of those tasks**. It takes only work nobody has claimed, and prepares the independent re-verification that the final integration step requires.

**Claimed scope of this session (new paths only; no file owned by another session is edited before integration).**

| # | Task | Status | Owner | File scope |
|---|---|---|---|---|
| F-1 | Coordination: read every remote branch, record all live claims, claim a non-overlapping scope | done | f16e6e34 | `COORDINATION.md` (this appended section only) |
| F-2 | Independent official-source verification ledger (law, tax, rates, thresholds, insurance, utilities) to be used for the final line-by-line re-verification of the combined data | **done** — 53 entries (48 confirmed on the opened official page, 5 not confirmed and left blank or marked) | f16e6e34 | `qa/ledger.json`, `qa/tools/ledger_add.py`, `qa/tools/build_ledger_js.py`, `site/data/ledger.js` (generated), `site/verification.html` |
| F-3 | Independent official historical series used to check baseline and black-swan numbers produced by other sessions | **done** — FHFA county indexes 1975–2025 (Santa Clara, San Francisco), BOE factor table 1976–2026, IRS thresholds 2011–2027, BOE Prop 19 amounts, CDI statewide premiums 2018–2023. No fourth black-swan page was built; the three existing ones are grouped under one navigation entry | f16e6e34 | `qa/series.json`, `site/verification.html` |
| F-4 | Whole-tree publication gate on the pages as rendered: $10 rounding rule, identifier patterns, internal links, https links, a source link in every table row. Holds no household data | **done** — PASS: 13 pages, 950 rows, 4,147 dollar amounts, 0 errors, 0 warnings | f16e6e34 | `qa/tools/gate.cjs`, `qa/gate-report.json`, `scripts/package-site.py` |
| F-5 | Triage of unmerged work nobody has claimed: open PR #3 (`arena/8c4d9e77-tino2`, conflicting), `arena/5a1bd5be-tino2` (39 commits, never merged), `arena/2d22c775-tino2` (claim only) | **done** — none merged; reasons in the triage table below | f16e6e34 | `COORDINATION.md` (this section) |
| F-6a | Integration re-verification of the merged `site/` dashboard (owners 449ce08f, 516f904c, d7d62f7a, 70f163d0 all done): corrections where an official source contradicts the site, household-level Best plan page, Verified facts page, grouped navigation, flagged items, PR, merge, Pages check | **done** — see results below | f16e6e34 | `site/data/model.js`, `site/data/history-engine.js`, `site/data/sources.js` (append), `site/estate-tax.html`, `site/properties.html`, `site/scenarios.html`, `site/black-swan.html`, `site/sources.html`, `site/review.html` (append), `site/plan.html` (new), `site/verification.html` (new), `assets/app.js`, `assets/styles.css` (append), `scripts/package-site.py`, `scripts/validate.js`, `_config.yml` (one exclusion) |
| F-6b | Landing page and README alignment | waiting — `index.html` and `README.md` are claimed by e03a1cbe (04:07:26) and 5c9d68b9 (04:08:29); not touched before those claims are merged or pass 60 minutes without a commit | f16e6e34 | `index.html`, `README.md` |

**Not started by this session (claimed elsewhere):** privacy remediation of existing pages (516f904c, 70f163d0), black-swan section (e03a1cbe, 70f163d0, 516f904c), canonical dashboard build (e03a1cbe). If any of those claims goes stale under the 60-minute rule, the takeover will be logged below before any work begins.

**Branch naming.** The platform fixes this session's branch to `arena/f16e6e34-tino2`; the `session-<id>/<task>` convention cannot be applied. The session ID is embedded in the branch name.

### Session `f16e6e34` log

| Time (UTC) | Entry |
|---|---|
| 2026-11-11 04:08 | Joined. Fetched all remote branches. Found four concurrent claims (table above). |
| 2026-11-11 04:10 | Confirmed on `main` @ `016eb53`: exact (not $10-rounded) household assessment and tax figures are present in `index.html`, `site/properties.html`, `site/inheritance.html`, `site/sources.html`, `site/data/model.js` and `scripts/validate.js`. This is already claimed for remediation by 516f904c and 70f163d0, so it is **not** edited here; it will be re-checked by the F-4 gate at integration and fixed then if still present. No figure is repeated in this file. |
| 2026-11-11 04:20 | Merged `origin/main` (PRs #10–#14 of sessions 516f904c, d7d62f7a, 70f163d0) into this branch. One conflict, in `COORDINATION.md`; resolved by keeping both sides in full (their sections first, then this section). Nothing discarded. |
| 2026-11-11 04:31 | Re-read every remote branch. Sessions 516f904c, d7d62f7a and 70f163d0 are **done and merged**; c8786419 is audit-only. Two more sessions hold live claims that exist only on their own branches: **e03a1cbe** (`plan/**`, root `index.html`, `README.md`; claim 04:07:26, no commit since) and **5c9d68b9** (`inherit/**`, root `index.html`, `README.md`, `archive/**`; claim 04:08:29, no commit since). Neither claims `site/**`, `assets/**` or `scripts/**`. This session therefore does **not** touch `index.html`, `README.md`, `plan/**`, `inherit/**` or `archive/**` unless those claims are merged or pass the 60-minute stale mark (05:07 / 05:08 UTC). |
| 2026-11-11 04:32 | **Scope extension claimed (integration re-verification of the merged `site/` dashboard; owners of these files are all marked done):** corrections limited to what an official source contradicts — `site/data/model.js` (federal exclusion for 2027; Prop 19 indexing method), `site/estate-tax.html`, `scripts/package-site.py` (see F-P1 below), `scripts/validate.js` (checks that encode the corrected values), `site/data/sources.js` (append-only block), `site/review.html` (append-only items), `assets/app.js` (navigation entries for new pages). New files: `site/plan.html`, `site/verification.html`, `site/data/ledger.js`, `site/data/household.js`. |

**Irregularities found by this session's independent verification (all published on the Flagged for Review page at integration):**

| ID | Finding | Evidence | Disposition |
|---|---|---|---|
| F-P1 | **Privacy.** `scripts/package-site.py` on `main` stores four "forbidden" household amounts as unsalted SHA-256 hashes. The inputs are 4- and 6-digit numbers, so the hashes are reversible by trying every number: this session recovered all four in 1.6 seconds. The repository is public, so the file re-publishes four exact private figures. | Brute-force test run 2026-11-11 04:36 UTC (values not printed or stored) | Replace with the rule-based scanner that contains no household data (`integration/tools/privacy_scan.py` logic: any dollar amount of $1,000 or more that is not a multiple of $10 and is not an official figure fails). Remove the hashes. |
| F-P2 | **Privacy, cannot be fixed by a commit.** Exact household figures remain readable in this public repository's commit history (commits of 2026-11-10 and early 2026-11-11) and in pull-request refs, which a session cannot delete. The current tree is clean: a scan of every tracked file finds no exact assessed value. | `git ls-files` scan 2026-11-11 04:35 UTC, 0 files | Owner decision required (history rewrite does not remove PR refs; options are a fresh repository, a GitHub Support purge request, or making the repository private). Flagged; reported to the user. |
| F-V1 | Federal exclusion for 2027 is now official: **$15,480,000** (IRS IR-2026-133, Nov 5 2026; Rev. Proc. 2026-35 §3.44). The site shows a modeled $15,300,000 and says the official amount is unknown. | https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts | Correct model and text. |
| F-V2 | Prop 19 amount indexing. BOE applies **one** year's California HPI change every second February (2023: ×1.0226; 2025: ×1.0215). `MODEL.modelAllowance` on `main` compounds **two** years of growth per step, overstating the 2040 amount by about 27%. | BOE LTA 2023/012 and 2025/009 | Correct model, validator check and page text. |
| F-V3 | "Framework only" links. `UI.ensureRowSources` appends the same IRS basis link to every table row that has no source, whatever the row is about. That satisfies an automated row check but is not a source for the row. | `assets/app.js` | Flag on the review page; relabel the column so it is not read as verification. Model rows are derived values, not official facts. |
| F-V4 | The household's San Francisco tax history moves differently from its assessed value because roughly 45% of the bill is flat parcel taxes, not the 1.18% rate (FY 2025-26: $334.38 + $319.34 + $21.50 per unit + $99 + $12). The Rent Board fee left the tax bill in 2022. | SF Treasurer parcel-tax page; SF Rent Board fee page | Publish as an explanation with sources; the 2018 jump is consistent with a new $298 parcel tax but that amount was seen only on non-official pages, so it is flagged unverified. |

### Session `f16e6e34` — completion record for F-2 … F-6a (2026-11-11)

**Official pages opened and read this session (48 confirmed facts; each with URL, date and the wording found in `qa/ledger.json`, published at `site/verification.html`):** IRS What's new — estate and gift tax; IRS IR-2026-133 and Rev. Proc. 2026-35; IRS Estate tax (threshold table); IRS estate-tax FAQ; IRS Topics 409, 414, 559, 701; IRS FAQ on inherited property; California State Controller (estate tax); FTB capital gains and 2025 rate schedules; BOE Proposition 19 page; BOE Letters to Assessors 2023/012, 2025/009, 2026/002, 2026/026; Santa Clara County tax rate book FY 2025-26; SF Treasurer secured property taxes and parcel taxes; SF Rent Board current rates and Rent Board fee; SFPUC Proposition 218 notice; San Jose Water 2026 rates; California Department of Insurance residential report and SB 824 workbook; California Secretary of State election results and Prop 3 guide; Probate Code §16061.7; Revenue and Taxation Code §480; Leginfo AB 942 status; FRED/FHFA county house-price indexes for Santa Clara and San Francisco counties.

**Not confirmed, left blank or marked (5):** insurance premium for Property A; insurance premium for Property B; the 2018 San Francisco parcel-tax amount (seen only on non-official pages); San Jose Water's requested bill amounts and the two federal estate-repeal bill statuses (read from search extracts of the official pages, not the opened pages).

**Corrections made to the merged dashboard, each with its source:**
1. Federal exclusion 2027 = $15,480,000 (IRS IR-2026-133). `MODEL.estateRow` now uses the official 2026 and 2027 amounts and indexes from 2027; estate page rows added for the 2027 amount, the 40% top rate and the annual gift exclusion.
2. Prop 19 amount: one year of home-price change per biennial step (BOE LTA 2023/012, 2025/009) in `MODEL.modelAllowance` and `SCEN` (`history-engine.js`); 2040 amount $1,329,010 instead of $1,690,870; base live case 2040→2050 moved from $5,196,300 to $5,135,780. Text on four pages and one validator check updated; two checks added.
3. `scripts/package-site.py`: reversible hashes removed; rule-based rounding check with no household data.
4. "Framework only" column relabelled as the rule the model applies, not a source for the number.

**New pages:** `site/plan.html` (four household plans — sell / rent / live / live and rent the Property B unit — for a 2040, 2045 or 2050 inheritance, with the drivers, the effect of already owning Property B, a 12-scenario stress check, a 2,000-path summary, what would change the answer, and ordered steps; built only on the existing `MODEL`, `SCEN` and `SCENARIOS` engines so its numbers agree with the other pages) and `site/verification.html` (ledger, corrections, household percent-change history checked against the BOE factor, what the tax bills are made of, official cost changes against model assumptions, 50-year county price record). Navigation: one entry per category; the three black-swan pages share one entry and a sub-navigation.

**Checks on the final tree:** `node scripts/validate.js` PASS 732 checks / 13 pages / 100 sources; `node scripts/stress-test.js` PASS; `python3 scripts/package-site.py` PASS; `node scripts/runtime-test.cjs` PASS 13 rendered pages / 950 rows; `node qa/tools/gate.cjs` PASS 0 errors.

**Triage of unmerged work (F-5):**

| Ref | Last commit (UTC) | Finding | Disposition |
|---|---|---|---|
| PR #3 `arena/8c4d9e77-tino2` | 2026-11-10 06:12 | Alternative ten-file guide from before the dashboard; conflicts with `main`; no exact household value at its tip; content superseded by `site/` | Not merged. Left open with a triage comment; recommend the owner close it |
| `arena/5a1bd5be-tino2` | 2026-11-10 07:03 | 39 commits, never opened as a PR; its tip contains six files with exact household assessed values (it predates the privacy clean-up) | **Must not be merged.** Flagged |
| `arena/2d22c775-tino2` | 2026-11-10 06:07 | Claim only, stale since 10 Nov | Nothing to merge |

**F-P2 detail (owner decision).** Besides commit history, **11 public branch tips** still contain at least one exact assessed value: `1dab34fa`, `449ce08f`, `457907c1`, `516f904c`, `5a1bd5be`, `5c9d68b9`, `64131d11`, `7c9c2cc4`, `c8786419`, `d7d62f7a`, `e03a1cbe` (most of them simply because they branched before the clean-up). Clean tips: `main`, `2d22c775`, `6ed42dca`, `70f163d0`, `7eeb5f71`, `8c4d9e77`, `f16e6e34`. This session did not delete other sessions' branches or rewrite history.

---

## Session `14e318a1` (branch `arena/14e318a1-tino2`) — joined 2026-11-11

**Branch state.** Branched from commit `240f255f` of `main` (PR #17 merged). Branch equals `main` at join; all prior session work (PRs #1–#17) is integrated, GitHub Pages is `built` on `main` / root at https://wingbangboozle1-lang.github.io/Tino2/, and the canonical site is published. This session claims only the final independent verification and the PR/merge/deploy record, touching only `verification/14e318a1/**` and this `COORDINATION.md` section. No file owned by another session is edited.

**Verification performed.** Re-ran the automated suite on the current tree: `python3 scripts/package-site.py` PASS; `node scripts/validate.js` PASS (581 checks / 11 pages / 70 sources); `node scripts/stress-test.js` PASS; `python3 src/check_links.py .` PASS (54 pages, 871 table rows, 124 external links). `node scripts/runtime-test.cjs` not run — requires optional gitignored dev dependency `jsdom` (environment note, not a site defect). Base-case decision output at 2040 inheritance / 2050 endpoint: sell $7,683,290; rent $6,249,830; live $5,196,300 (sell leads on financial value; live excludes monetized housing service).

**Independent spot re-checks vs official sources (2026-11-11).** IRS 2026 federal basic exclusion $15,000,000 — Match; SCO no California estate-tax return for deaths on/after Jan 1, 2005 — Match; BOE Prop 19 amount $1,044,586 for Feb 16, 2025 – Feb 15, 2027 — Match; SF FY2026–27 combined rate 1.18162182% — Match; HUD FY2026 SAFMR ZIP 95014 4BR $6,390 / 3BR $5,870 — Match; SF Rent Board 1.6% increase window and $59/unit fee — Match. Not verified / flagged: exact CBO figures, SF 7% ceiling, insurance quotes, household inputs.

**Report.** `verification/14e318a1/REPORT.md` — full session record, privacy statement, and irregularity register.

**Flagged irregularities (non-blocking).** 8 High-priority open items on `site/review.html` (trust instrument/title, date-of-death appraisals, full gross estate + gifts, DSUE/portability, citizenship/residency, parcel tax-rate areas, Prop 19 principal-residence eligibility, taxpayer brackets/NIIT); Property A 1.2% levy is a hypothetical scenario; historical household bills withheld from the public build; future Prop 19/federal exclusion amounts and pending legislation are scenarios, not forecasts. No personal information added to this session's files.

## Session `14e318a1` — publication result

- PR: [#18](https://github.com/wingbangboozle1-lang/Tino2/pull/18) (`arena/14e318a1-tino2` -> `main`)
- Merge result: `MERGED`, `mergeable/clean`; merge commit `143446873f552efe8dc7553fd804bb8e75a3a598`; merged without waiting for approval on 2026-11-11.
- GitHub Pages: build `1359549987` for commit `14344687` completed `built` with no error (~43 s); source `main` / root, HTTPS enforced; public URL https://wingbangboozle1-lang.github.io/Tino2/ live.

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-11 | 14e318a1 | all sessions | Independent verification complete; all automated checks PASS (validate 581, stress-test, package-site, check-links 54 pages/871 rows); 6/6 official spot re-checks Match (IRS $15M, SCO no CA estate tax, BOE Prop 19 $1,044,586 cap, SF rate 1.18162182%, HUD FY2026 SAFMRs, SF Rent Board 1.6%/$59); irregularities flagged on site/review.html and non-blocking. PR #18 merged to main (merge commit 14344687); Pages build 1359549987 `built`, site live. |


## Session `81334f2c` — publication boundary hardening (2026-11-11)

Current fixed branch: `arena/81334f2c-tino2`; base `815289a`. Prior financial dashboard implementation and completed sessions are retained. No alternate branch is created (Arena branch constraint).

| Task | Status | Owner | File scope |
|---|---|---|---|
| Enforce canonical-only Pages deployment, test publication boundary, verify existing dashboard and record release | in progress | 81334f2c | `.github/workflows/pages.yml` (new), `scripts/check-publication.py` (new), `verification/81334f2c/**` (new), this coordination section |

Finding: `scripts/package-site.py` creates an allowlisted `_public` artifact, but current Pages uses legacy root/Jekyll publication. The packaging check therefore does not prove the deployed artifact excludes all future unlisted repository files (including verification notes). This session will deploy only the packaged artifact. It will not edit another session's financial model, sources, or shared navigation. Source-link presence is not semantic verification of every financial claim; carried-forward source claims are not newly certified by this session. The open integration PR #16 is not merged here because it belongs to another active branch.

Deployment constraint: GitHub's Pages settings update API returned HTTP 403 (`Resource not accessible by integration`); the repository connection can read Pages and push code but cannot switch its build type. No credentials requested. Scope extended to `_config.yml` (completed prior owner, no current competing claim): retain working legacy Pages, explicitly exclude verification notes, and add CI that builds the *actual Jekyll output* and rejects any file outside the reviewed manifest. This closes the tested-package/deployed-output verification gap without changing an unauthorized repository setting. A strict artifact deployment migration remains an administrative follow-up, not a claimed success.

Integration note: main advanced via PR #20 during this session. Rebased onto main, then merged the original published claim commit to preserve remote ancestry without a force push. The sole conflict was our own coordination appendix; kept its full updated version and all other sessions’ sections. No other session files discarded.

PR #20 integration also brought its already-completed verification-directory exclusion and three new canonical files (Best plan, Verified facts, official ledger). Removed this branch’s redundant config entry; reviewed those three files and updated the manifest from 21 to 24 files. First PR CI correctly failed closed on these previously unlisted files. Model/runtime checks now pass 737 validations / 13 pages / 100 sources and 963 rendered source-linked rows. A pull-rebase against the old session claim attempted to replay unrelated historical commits; aborted it immediately without retaining any conflict changes, preserving main and published claim via the prior merge.

Actual-Jekyll CI finding: GitHub Pages generates the default theme stylesheet `assets/css/style.css`, absent from the hand-packaged output. Added precisely that generated CSS path to the Jekyll-only manifest; no broad asset wildcard was added. All model, package and rendering checks already passed in CI; final Jekyll audit is being rerun.

### Session `81334f2c` — completion and release

- Task status: **done** (privacy-boundary CI and integration); artifact-only deployment migration remains **needs review**, due to Pages-settings API 403. This supersedes the initial intent to switch deployment mode. Actual deployment remains legacy main/root.
- PR [#21](https://github.com/wingbangboozle1-lang/Tino2/pull/21) merged without waiting for review on 2026-11-11 07:55 UTC. Merge commit `e3ec53b8983459cc281cbc07bfb1d3b4b2bab9c0`.
- PR validation run [42982912949](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/42982912949): success before merge.
- Main verification run [42983004236](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/42983004236): success, including actual GitHub Pages Jekyll output audit. Reviewed package manifest: 24 files. Jekyll manifest: 23 (package-only `.nojekyll` and robots omitted; generated theme stylesheet included). Model checks: 737 / 13 pages / 100 source entries; rendering: 13 pages / 963 source-linked rows. Source presence is not semantic certification.
- Pages deployment [42983003027](https://github.com/wingbangboozle1-lang/Tino2/actions/runs/42983003027): **success**; Pages API reports `built`, no error, commit `e3ec53b8`.
- Live landing and Flagged for Review pages retrieved successfully at https://wingbangboozle1-lang.github.io/Tino2/ and https://wingbangboozle1-lang.github.io/Tino2/site/review.html . Existing financial/private-history uncertainties remain visible on that page. Public Git history/cache retention is not erased or claimed solved.
- Fresh official-source spot checks: IRS 2026 exclusion, California SCO estate filing status, BOE current Prop 19 amount/period/indexing, CDI residential insurance guidance, GitHub custom-workflow publication requirements. Full links and scope in `verification/81334f2c/REPORT.md` (repository-only, intentionally not published).
- All previous sessions' work preserved. Main advanced via PR #20 and #22 during this session; coordination changes retained. Ordinary flattening rebases conflicted with the old published claim ancestry and were aborted without retaining changes; merging main succeeded. Later pushes used `pull --rebase=merges` against this session branch, avoiding any force push or branch switch.
## Session `246f5b3b` (branch `arena/246f5b3b-tino2`) — joined 2026-11-11 07:43 UTC — final integration

**State at join.** `main` = `240f255` (PRs #1–#15, #17 merged; Pages live from `main` / root). All 17 remote `arena/*` branches fetched before claiming. Newest commit on any other branch: `f16e6e34` at 04:46 UTC (about three hours old), so every other claim is past the 60-minute stale mark. PR #16 (`f16e6e34`) is open, mergeable and unmerged; its session stopped before merging.

**Handoff.** This session takes over the stale final-integration task (F-6 of `f16e6e34`, E-14 of `e03a1cbe`, F-6 of `5c9d68b9`) under the 60-minute rule. The platform fixes the branch name to `arena/246f5b3b-tino2`; the `session-<id>/<task>` naming cannot be applied.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| G-1 | Claim, read all boards and branches | done | 246f5b3b | `COORDINATION.md` (this section) | N/A | none |
| G-2 | Take over PR #16 (also taken over and merged in parallel by session 11bffb54; both merges kept): merged `arena/f16e6e34-tino2` into this branch, re-ran every check, re-verified its corrections on the official pages | done | 246f5b3b | files of PR #16 | IRS IR-2026-133 ($15,480,000 for 2027; gift exclusion $20,000); IRS "What's new" ($15,000,000 for 2026); BOE Prop 19 page; BOE LTA 2025/009 ($1,044,586, 16 Feb 2025–15 Feb 2027); SCO estate tax page; SF Rent Board rates (1.6%); HUD FY2026 SAFMR; RTC 480; congress.gov H.R.1301. All match the site. | One conflict in `COORDINATION.md` (both sessions appended); resolved keeping both sides. |
| G-3 | Privacy audit of the tree, the Pages artifact, the history and every branch | done; owner decision open | 246f5b3b | whole tree (read) | GitHub Docs "Removing sensitive data" | Pages artifact (`_public/`): no exact figure except one assessed value that already ends in 0. **Ten other branch tips (`1dab34fa 449ce08f 516f904c 5a1bd5be 5c9d68b9 64131d11 7c9c2cc4 c8786419 d7d62f7a e03a1cbe`) and nine commits in `main` history still hold exact assessed values.** A session cannot delete other sessions' branches or purge history. Published as the first High item on the Flagged for Review page. Legacy root pages (`cupertino.html`, `pages/`, `dashboard/`, `docs/`, `src/` …) stay in the tree with $10-rounded figures and are excluded from Pages by `_config.yml`; not deleted because other sessions own them. |
| G-4 | Line-by-line review of the published site against the brief; gaps filled | done | 246f5b3b | `index.html`, `site/properties.html`, `site/estate-tax.html`, `site/review.html`, `site/sources.html`, `site/verification.html`, `site/inheritance.html`, `site/data/model.js`, `site/data/sources.js`, `scripts/stress-test.js`, `scripts/package-site.py`, `README.md` | New this session: RTC 13301 (no state or local gift/inheritance/estate tax); RTC 11930 (no transfer tax on transfer by death); RTC 11911 (county rate $0.55 per $500); CPUC net energy metering page; CDI residential workbook (statewide sheet only); SFPUC Prop 218 notice; CA SoS ballot results (unofficial, 10 Nov 2026) | (1) Household tax/assessed history had been withheld against the brief; restored rounded to $10 (`MODEL.historyA/B`, Properties `#history`). (2) Landing page was stale (modeled 2027 exclusion, no best plan, 2040 only); rewritten as executive summary for 2040/2045/2050. (3) No table answered "federal / state / local threshold and room"; added to Estate page. (4) No "costs upon inheriting" table; added. (5) Source register status column never matched the date format; fixed. (6) Inheritance step 8 linked the wrong county assessor; fixed. (7) Still unconfirmed and blank: both insurance premiums (ZIP sheets unreadable), solar tariff term, tax-rate areas, money in the estate. (8) Model property tax before inheritance is below the household's bills (no flat charges); disclosed. All listed on `site/review.html`. Request to earlier sessions: none; shared files were changed by this session as final integrator. |
| G-5 | PR to `main`, merge, confirm Pages deploy, record result | done | 246f5b3b | `COORDINATION.md` (this section) | GitHub Pages build API; live pages fetched | **PR https://github.com/wingbangboozle1-lang/Tino2/pull/23 — MERGED 2026-11-11 07:56 UTC, merge commit `e8abf0a`.** PR check "Verify public Pages boundary": pass. `main` moved twice while this session worked (PRs #16, #18–#22 by sessions 11bffb54, 14e318a1, 81334f2c, then #21); each time `origin/main` was merged into this branch, conflicts in `COORDINATION.md`, `index.html`, `site/properties.html`, `site/review.html`, `site/sources.html`, `site/verification.html` were resolved keeping the other sessions' text or combining both, and all checks re-run before merging. First merge attempt was refused as conflicting; fixed and retried. Pages build for `main` `7e537de` (contains `e8abf0a` and later PR #24): status `built`, no error; workflow "pages build and deployment": success. Live pages fetched and read after the build: `/` (new executive summary), `/site/estate-tax.html` (threshold table), `/site/properties.html` (costs upon inheriting); `/COORDINATION.md` returns 404 as intended. PR #16 was merged by session 11bffb54 at 07:49 UTC, so no supersede/close was needed. |

Release-record integration: PR #23 (session 246f5b3b) landed while the PR #24 record was being prepared. The only conflict was appended coordination sections; both retained in full. Its source/model/site changes are preserved and the publication manifest still admits the same canonical paths.

| G-5 | PR to `main`, merge, confirm Pages deploy, record result | unclaimed → this session | 246f5b3b | `COORDINATION.md` (this section) | — | — |

---

## Session `b0123943` (branch `arena/b0123943-tino2`) — joined 2026-11-11 07:45 UTC — independent verification + publication record

**State at join.** `main` = `240f255` (PRs #1–#17 merged; GitHub Pages live from `main` / root). An active final-integration session `246f5b3b` claimed the role at 2026-11-11 07:43 UTC (took over stale PR #16; tasks G-2..G-5). Its claim is under 60 minutes old, so this session does **not** take the integration/nav/landing role and does **not** edit `site/**`, `index.html`, `assets/**`, `scripts/**`, `src/**`, `dashboard/**`, `pages/**`, `docs/**`, `plan/**`, `qa/**`, `inherit/**`, `research/**`, `integration/**` or any file owned by another session.

**Claimed scope (new paths only + this board section):**

| # | Task | Status | Owner | Files touched | Sources verified | Irregularities |
|---|------|--------|-------|---------------|------------------|----------------|
| B0 | Coordination: read boards/branches, claim non-overlapping scope, push claim immediately | done | b0123943 | `COORDINATION.md` (this section) | N/A | none |
| B1 | Independent line-by-line verification of the published site and the PR #16/#20/#22 integration tree: run the repo check suite on a read-only worktree; fetch key official pages (IRS, BOE, SCO, leginfo, HUD, SF Rent Board, CDI) and record match/no-match with URLs | done | b0123943 | read-only (worktree of `main`) | 13/13 official pages opened 2026-11-11 MATCH (§2 of report) | none |
| B2 | Publish verification report | done (this PR) | b0123943 | `verification/b0123943/REPORT.md` | report §1–§6 | F-B1…F-B12 (none blocking) |
| B3 | PR to `main`, merge without waiting, confirm Pages deploy, record result | done | b0123943 | `COORDINATION.md` (this section) | PR #25; runs 42983734588 (verify) and 42983734021 (pages) | none |

**Rules this session follows:** privacy first (no personal information anywhere in committed files), every dollar figure in new files rounded to the nearest $10, every table row carries an official source link or is blank + flagged unverified, small frequent commits, `git pull --rebase` (or merge `origin/main`) before every push, conflicts resolved without discarding other sessions' work.

### Session `b0123943` — publication result (2026-11-11)

- PR [#25](https://github.com/wingbangboozle1-lang/Tino2/pull/25) (`arena/b0123943-tino2` -> `main`) **merged** 2026-11-11 08:01:10 UTC; merge commit `a6818a35da43a5c03b50361732a4fd5b89a5ea7c`. The `verify` check (Verify public Pages boundary) was **success** before merge (run `42983600751`).
- Main moved during this session (PRs #18–#24, #26); this branch merged `origin/main` twice to stay current; both conflicts were in `COORDINATION.md` and were resolved by keeping every session's section in full. No other session's file was edited; site code was identical to `e8abf0a` when this branch was merged into `main`.
- Post-merge `main` (`a6818a3`): `Verify public Pages boundary` run `42983734588` **success**; `pages build and deployment` run `42983734021` **success**; Pages API status `built`, source `main` / root.
- Live site confirmed serving the current dashboard (cache-busted fetch 2026-11-11): executive summary with the three-inheritance-year table (2040: sell $7,683,290 · 2045: sell $9,125,340 · 2050: sell $10,838,040), the 2027 federal exclusion $15,480,000, Best plan and Verified facts links, and the black-swan check table. Note: the un-busted URL served a cached older render; the deployed artifact matches `main`.
- Carried forward for the owner (not blocking): Insurance quotes for both ZIPs; exact household figures in public Git history (owner decision); PR #3 recommended for owner to close; Property B cost inflation and solar-credit sunset flags; Prop 19 amount beyond Feb 2027; SF File No. 261020 (not enacted); carried-forward (not re-opened) official series listed in `verification/b0123943/REPORT.md` §2.

---

## Session `aa1f073e` (branch `arena/aa1f073e-tino2`) — claim 2026-11-11 07:52 UTC

**State read at claim.** `main` = `240f255` (PR #17 merged; Pages `built`, source `main` / root; `node scripts/validate.js` PASS 581, `node scripts/stress-test.js` PASS, `python3 scripts/package-site.py` PASS, `python3 src/check_links.py .` 0 errors). All 19 `arena/*` branches fetched before claiming.

**Live claims seen on other branches at 07:50–07:52 UTC (not stale, therefore not touched):**

| Session | Branch | Claim pushed (UTC) | Claimed |
|---|---|---|---|
| `11bffb54` | `arena/11bffb54-tino2` | 2026-11-11 07:50 | Take over stale PR #16, brief-vs-site gap review, final integration (`site/**`, `assets/app.js`, `index.html`, `scripts/validate.js`, `_config.yml`, `README.md`), PR/merge/Pages |
| `246f5b3b` | `arena/246f5b3b-tino2` | 2026-11-11 07:44 | Final integration + takeover of stale PR #16 (already merged `arena/f16e6e34-tino2` into its branch) |

Irregularity **AA-C1 (coordination race):** three sessions (`246f5b3b`, `11bffb54`, this one) were started within ~8 minutes of each other with the same brief, and the first two both claimed "final integration / take over PR #16" 6 minutes apart on branches neither could see. This session therefore does **not** claim final integration, does not take over PR #16, and does not edit any file those two named. It takes the research gap that every previous session left explicitly **unverified**.

**Claimed scope (new paths only; nothing owned by an active session is edited).**

| # | Task | Status | Owner | File scope |
|---|------|--------|-------|------------|
| AA-1 | Coordination: read every branch, record the race, claim a non-overlapping scope, push immediately | **done** | aa1f073e | `COORDINATION.md` (this section only) |
| AA-2 | Operating-cost research from official/regulator sources only — insurance (CA Dept of Insurance, NAIC), water tariffs for both ZIPs, electricity/solar export tariff, maintenance benchmarks | **done** — 5 cost lines, 47 ledger entries, 41 confirmed on the official page, 6 not confirmed and left blank | aa1f073e | `research/aa1f073e/operating-cost-ledger.md` |
| AA-3 | Verification ledger for AA-2: one row per figure with the official URL, the wording found, access date; blank + flagged when no official source confirms it | **done** — merged into the AA-2 ledger (one document, one row per figure, status column) | aa1f073e | `research/aa1f073e/operating-cost-ledger.md` |
| AA-4 | Published cost page built from AA-2/AA-3 | **done** — `site/operating-costs.html` + `site/data/costs.js`, 15 new registered sources, every row linked or flagged | aa1f073e | `site/operating-costs.html`, `site/data/costs.js` (new) |
| AA-5 | Line-by-line read of the published site against the brief; findings logged for the owning session | **done** — 7 new items appended to the Flagged for Review register (2 High) | aa1f073e | `site/review.html` (append only) |
| AA-6 | Own PR to `main` (additive files only), merge, confirm Pages deploy, record result here | **done** — see result below | aa1f073e | own files + this section |

**Rules this session follows:** no personal information in any committed file; every dollar figure rounded to the nearest $10; every table row carries an official source link or is left blank and flagged unverified; no value inferred; small frequent commits; `origin/main` merged before every push; conflicts resolved without discarding another session's work.

### Requests / handoff log (session `aa1f073e`)

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-11 07:52 | aa1f073e | `246f5b3b`, `11bffb54` | You both claimed final integration minutes apart. I am staying out of `index.html`, `README.md`, `_config.yml`, `assets/**`, `scripts/**`, `qa/**`, `site/**` **except two new files** (`site/operating-costs.html`, `site/data/costs.js`) that no one has claimed. Whoever integrates last: please add one nav entry for `site/operating-costs.html`. If both of your claims pass 60 minutes with no commit, I will add the nav entry myself and log the takeover here. |

### Session `aa1f073e` — results (2026-11-11)

**Handoff taken, with the 60-minute rule not needed.** Both sessions named in the request log below
finished and merged while this research ran: PR #20 and PR #22 (`11bffb54`), PR #23 (`246f5b3b`) and
PR #24 (`81334f2c`) are all in `main`. `246f5b3b` left G-5 open and its G-4 note lists the gaps it could
not close, including "both insurance premiums, solar tariff term, tax-rate areas". With no active
competing claim, this session made the four shared-file edits its new page needs, each additive:

| Shared file | Edit | Why it is safe |
|---|---|---|
| `assets/app.js` | one navigation entry, `Operating costs` | Additive; no existing entry changed |
| `scripts/validate.js` | page count 13 → 14; `require` of `site/data/costs.js` so its source keys are registered | The count is an exact-match assertion that a new page necessarily breaks |
| `scripts/check-publication.py` | two paths added to the reviewed manifest | The CI gate fails closed on unlisted files, by design |
| `site/sources.html`, `site/review.html` | load `data/costs.js`; 7 appended review items | Append-only; no existing row edited |

**What the new page establishes.** Operating costs are rebuilt from adopted rate schedules instead of
recalled bill amounts. Water and wastewater for both properties now have tariff-level build-ups with
effective dates and adopting resolutions; the solar legacy term is confirmed at 20 years from permission
to operate and transferable with the system; the minimum delivery charge is confirmed as a floor under
any solar credit; maintenance has a national official series. The San Jose Water build-up reproduces
that company's own published average-bill illustration to the cent, which is the transcription check.

**What it deliberately leaves blank.** Insurance, for both properties. Three official routes were tried
and each either declines to price a specific property or publishes a state average its own publisher
warns against reading as a price. No figure was substituted. Also open: which of three water systems
serves Property A, both meter sizes, Property B's parcel tier and meter count, and the solar install
year. All seven are now on the Flagged for Review register with the document that resolves each.

**Irregularity AA-I1 (new).** San Francisco's adopted schedule raises the average single-family combined
bill about 12.6% and then about 12.5% in consecutive years, while every projection on the site escalates
operating costs at a flat 3%. The adopted increases are not forecasts. Published on the Operating costs
page and on the review register; the base case was not re-escalated, because that model belongs to the
integration sessions and changing it would overwrite their work.

**Irregularity AA-I3 (new, and a self-correction).** San Jose Water's customer notice illustrates an
average residential bill of $141.73 a month for a 3/4-inch meter at 10 Ccf from 1 July 2026. Applying
that same advice letter's Schedule No. 1 — service charge $78.64, tiers $4.9692 / $7.4167 / $14.1659 —
at 10 Ccf gives **$138.12**, about $3.61 less. The schedule was re-read to test meter size as the
explanation: the service charge is $78.64 for both the 5/8 × 3/4-inch and the 3/4-inch meter, and the
residential tiers cover meters up to 2-inch, so meter size does not account for it. The gap is most
plausibly authorized surcharges or balancing-account amortisation that Schedule No. 1 does not list,
but that was **not** confirmed and is therefore not asserted.

The first version of this page, merged in PR #28, stated that the build-up reproduced $141.73 exactly.
That was an arithmetic error on this session's part. It was caught by reading the rendered live page
after deployment, and corrected in the follow-up PR recorded below — the page now shows both figures and
the difference, the research ledger records the failed reconciliation, and the review register carries
it as an open item. Recording the error here as well, because a correction that is only visible in the
corrected text is not an audit trail.

**Irregularity AA-I2 (new).** The household's supplied water range for Property B is materially below the
tariff build-up at ordinary three-unit usage. Either consumption is lower than assumed or the billing
basis differs (separate meters, different parcel tier, or rates recalled from before July 2026). Not
reconciled; published as an open item.

**Checks on the final tree.** `node scripts/validate.js` PASS 835 checks / 14 pages / 121 sources ·
`node scripts/runtime-test.cjs` PASS 14 pages, 1,126 rendered rows all source-linked ·
`node scripts/stress-test.js` PASS · `python3 scripts/package-site.py` PASS ·
`python3 scripts/check-publication.py` PASS 26 reviewed files, and its `--self-test` PASS ·
`node qa/tools/gate.cjs` **PASS: 0 errors, 0 warnings** (14 pages, 1,127 rows, 4,370 dollar amounts,
1,536 external links, after the AA-I3 correction). Base case unchanged at 2040→2050 sell $7,683,290, rent $6,249,830, live $5,135,780.

**Privacy.** No household figure, address, meter number, account number or parcel identifier is in the
new page, the new data file or the research ledger. Every dollar amount of $1,000 or more that the page
renders is a multiple of $10; tariff unit rates below $1,000 are shown exactly, because that is what
makes the build-up checkable. `research/aa1f073e/**` is repository-only and excluded from the Pages
artifact by the publication manifest.

**PR record (session `aa1f073e`).**

| PR | Content | Merge commit | Pages | Result |
|---|---|---|---|---|
| [#28](https://github.com/wingbangboozle1-lang/Tino2/pull/28) | Operating costs page, costs data file, research ledger, 7 review items, nav + manifest + validator updates | `c429440` | run `42984292861` success; boundary check `42984293838` success; Pages API `built` | merged 2026-11-11 |
| #29 | AA-I3 correction: the San Jose Water build-up does not reproduce the company's illustrated average bill; both figures and the difference now published, plus an eighth review item | see below | see below | see below |
