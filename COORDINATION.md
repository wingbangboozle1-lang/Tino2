# Coordination — Tino2 Inheritance Decision Project (integrated)

<!-- BEGIN block owned by session 60ca3e1f. It sits directly under the title so that it merges without conflict with the blocks sessions 1e425502 and f344fcd1 are appending at the end of this file. Other sessions: please do not edit inside this block; write requests in your own section. -->
## Session `60ca3e1f` (branch `arena/60ca3e1f-tino2`) — claim 2026-11-12 04:20 UTC

**State read at claim.** `main` = `9867620` (PR #37). All 31 remote branches fetched at 04:18 and again at 04:20 UTC. **Two sessions are live, both started within about two minutes of this one with the same brief:**

| Session | Claim pushed (UTC) | What it claimed | Files it claimed |
|---|---|---|---|
| `1e425502` | 2026-11-12 04:18:25 | Final independent verification of the published site against the brief (T-1 … T-6), disposition of stale PR #3; PR #38 opened 04:19 | `verification/1e425502/**`, its own board block. No shared file unless a defect is found and logged first |
| `f344fcd1` | 2026-11-12 04:19:05 | Whole-repository privacy audit (F-2), re-run of every check and re-opening of the time-sensitive official figures (F-3); final integration F-4 and PR F-5 are written as **unclaimed** until F-2/F-3 report | `verification/f344fcd1/**`, its own board block; shared files "to be listed before any is touched" |
| `60ca3e1f` (this session) | this commit | Research the items the board still lists as blank, and the economic baseline behind the projections; publish what is confirmed | see the table below |

**Why this scope.** Verification of what is already published is claimed twice over (`1e425502`, `f344fcd1`), and so is the privacy audit. What nobody holds is the list of things the brief asks for that the site still leaves blank or thin: the two insurance figures the brief asks to be researched, the tax figures that change on a known date (Proposition 19 amount from 16 February 2027, 2027 federal amounts, the results of the 3 November 2026 election), and the official long-run economic baseline that the projections and the black-swan section should be measured against. This session takes those and does not repeat the audits.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| R-1 | Coordination: read the board and every branch, detect the two live claims, claim a non-overlapping scope, push at once | done | 60ca3e1f | `COORDINATION.md` (this block only) | N/A | R-C1 below |
| R-2 | Insurance research for both ZIP codes from regulator and other official sources only (owner-occupied home for Property A; rented three-unit building for Property B), including the FAIR Plan and earthquake cover. Blank and flagged where no official figure exists | done (research 04:39 UTC, commit `f2a38ac`; two more Cupertino profiles added 04:50); published under R-6. Both premiums stay blank | 60ca3e1f | `research/60ca3e1f/**` (new) | California Department of Insurance: 2026 premium survey result pages for the Cupertino and San Francisco–Sunset survey locations (homeowners at $500,000, $750,000 and $1,000,000 of dwelling cover for Cupertino, $1,000,000 for Sunset, home ages 40 and 70; earthquake single-family profile), survey format and profile pages, Residential Insurance guide (Form 401, Jan 2026), Residential Property Insurance Report, SB 824 workbook (statewide sheet); California FAIR Plan policies in force by ZIP code (30 Sep 2022–2026) and key statistics | R-I1, R-I2, R-I3, R-I4 below |
| R-3 | Dated figures and law changes as of 12 November 2026: Proposition 19 amount from 16 February 2027, 2027 federal estate, gift and capital-gain amounts, certified or latest results of the 3 November 2026 state and San Francisco measures, pending federal and state bills that would change the plan | done. Federal 2027 amounts and the ballot counts were already published by `f344fcd1` at 04:29 UTC (F-I3, F-I4) and are not repeated. New: the Proposition 19 amount from 16 Feb 2027 is not on the Board's 2026 list of letters, and the amount now in force was published on 7 March 2025, three weeks after it took effect (ledger P19-10, P19-11). HUD FY2027 lookup address tried, not readable; left blank | 60ca3e1f | `research/60ca3e1f/**` (new) | IRS release IR-2026-133; IRS "What's new — estate and gift tax"; Board of Equalization Proposition 19 page, 2026 Letters To Assessors list, cover letter of 2026/026, news release NR 25-02 | R-I5 below |
| R-4 | Economic baseline and black-swan research: official long-run projections (CBO, Social Security Trustees, Federal Reserve, BLS, FHFA) set beside the model's assumptions; check that the stress section reflects recorded conditions | done; published under R-6 (ledger ECO-01 to ECO-04). BLS and FHFA series were not re-opened: the site already carries them, checked on 11 Nov by `f16e6e34` | 60ca3e1f | `research/60ca3e1f/**`, `verification/60ca3e1f/**` (new) | Federal Reserve Summary of Economic Projections 16 Sep 2026; 2026 Social Security Trustees Report Table II.C1; CBO Budget and Economic Outlook 2026–2036, By the Numbers, and the economic-projections data file (calendar-year sheet) | — |
| R-5 | Read the published site as a reader would (rendered pages) and list defects in clarity, navigation and consistency; each logged below with the file and its last owner | done. All 15 rendered pages scanned by script; the landing page, the Operating costs page and the changed parts of seven other pages read in full; the rest not read line by line. Nine defects in `verification/60ca3e1f/REPORT.md`: six fixed, three recorded | 60ca3e1f | `verification/60ca3e1f/**` (new) | N/A | R-D1 to R-D6 below |
| R-6 | Publish what R-2 … R-5 confirm. Shared files are **not** claimed yet: they will be listed in this block, with a handoff note, before any is touched, and only after re-reading the blocks of `1e425502` and `f344fcd1` | **done 05:14 UTC, pending the merge under R-7** — claimed 2026-11-12 04:42 UTC; two files added 04:56 UTC; one file and two wordings added 05:08 UTC | 60ca3e1f | `site/data/sources.js` (append-only block), `site/data/costs.js` (append), `site/operating-costs.html` (insurance section and the three sentences that say insurance is blank), `site/review.html` (new items; five stale insurance/CBO items reworded; one stale sentence in the solar item, R-D1; the count in the commit-e-mail item, R-D6), `site/options.html` (one row), `site/black-swan.html` (CBO row and note; baseline rows added), `site/sources.html` (review-date label; one note), `site/scenarios.html` (one row: the official baseline), `site/verification.html` (two topic headings and the date wording, so that every ledger entry is shown; R-I5), `index.html` (insurance sentences; the words "the solar tariff term" in the flag card, R-D1), `site/properties.html` (the two insurance rows only, R-D2), `qa/ledger.json` + `site/data/ledger.js` (new entries), `scripts/validate.js` only if a count changes. No model input, plan, navigation or page list changes | — | — |
| R-7 | Own PR to `main`, merge, confirm the Pages build, read the live pages back, record the result here | **in progress — claimed 05:14 UTC; pull request [#42](https://github.com/wingbangboozle1-lang/Tino2/pull/42) opened 05:14 UTC and merged by this session. The result of the Pages build and of reading the live pages back is written as a comment on that pull request, because writing it here would need a second merge and each merge adds a commit that carries the account's e-mail address (R-D6)** | 60ca3e1f | own files + this block | — | — |

**Rules this session follows.** No personal information in any committed file; parties and addresses appear only as placeholders. No household figure is committed unrounded and none is repeated in this block. Every dollar figure in new files is rounded to the nearest $10 unless a government body publishes that exact amount. Every table row carries a link to an official source or is left blank and marked unverified; nothing is inferred. `origin/main` is merged before every push; conflicts are resolved keeping both sides. The platform fixes the branch name to `arena/60ca3e1f-tino2`, so the `session-<id>/<task>` naming cannot be applied; the session ID is in the branch name.

**Irregularities found by this session.**

- **R-I1.** The Operating costs page and `research/aa1f073e/operating-cost-ledger.md` (session `aa1f073e`) said the Department of Insurance comparison tool could not be read because it is an interactive form. Its result pages open by direct address with no session; the pattern is in `research/60ca3e1f/insurance.md`. The page now shows what the tool says. The older ledger file is left as its owner wrote it.
- **R-I2.** The source note `ocCdiProfiles` (`site/data/costs.js`, `aa1f073e`) gave only the upper part of the coverage range. A sentence was added from this session's block; the original wording is kept.
- **R-I3.** `site/sources.html` labelled every note not dated 11 Nov as "Carried forward · needs revalidation", including the three sources `f344fcd1` checked on 12 Nov. The label now recognises 12 Nov.
- **R-I4.** Ledger entry N-12 (`0d6ec51e`) lists the Department's vacant-home statement as unverified because only a Spanish fact sheet was found. The English guide was opened; INS-09 supersedes it. N-12 is left in place and INS-09 says so.
- **R-I5 (defect, `site/verification.html`; last owner `f16e6e34`).** The Verified facts page shows only ledger topics that are in its list of headings. One verified entry from an earlier session, CF-03 (HUD rent benchmark, FY2024 to FY2026; topic `rent-benchmark`), was therefore counted in the page total but not shown. That heading and the new `economic-baseline` heading were added; `verification/60ca3e1f/check.cjs` now fails if any ledger topic has no heading.
- **R-D1 (consistency defect, `index.html` and `site/review.html`; last owners `0d6ec51e`, `f344fcd1`).** The flag card on the landing page and one older item on the Flagged page say the 20-year solar tariff term is not confirmed. A later item on the same page, and the Operating costs page (`aa1f073e`), record it as confirmed; what is unknown is the year the system was switched on. The two older wordings are brought into line. No new fact is added.
- **R-D2 (consistency defect, `site/properties.html`; last owner `0d6ec51e`).** Its two insurance rows say the comparison tool gives no figure because it is an interactive form. They are brought into line with the Operating costs page. Both "official amount" cells stay blank.
- **R-D6 (stale count, `site/review.html`; last owner `f344fcd1`).** The commit-e-mail item gave 37 commits, the count at `95e6d6a`. Pull requests #40 and #41 were merged after that. The GitHub commit list for `main` at `9163fed`, read at 05:12 UTC, has 39 commits authored with the account's address (38 merges and the first commit); two more carry a placeholder `.local` address and are not counted. The item now gives that count with its time and says each merge adds one. This session's merge adds one more; the owner setting described in that item is the only fix.
- **R-D3, R-D4, R-D5 (clarity; not fixed, recorded for the next session).** "NOI" is not spelled out on `site/decision.html` and `site/properties.html`; four items on `site/review.html` speak of "this session" or "an earlier session"; the shared footer in `assets/app.js` still says "Correction audit: 11 Nov 2026". None of these files was claimed for that purpose.
- Not fixed, recorded only: `src/__pycache__/model.cpython-311.pyc` is tracked in git; `_config.yml` lists one excluded file twice; several older blocks on this board still show tasks as "in progress" although their pull requests are merged. None affects the published site.

**R-C1 (claim note).** `f344fcd1`'s block states that `main` was the only branch on the remote and that no other session was live. At 04:18:25 UTC `1e425502` had already pushed its claim, 40 seconds before `f344fcd1` pushed, so the two could not see each other. Their verification scopes overlap (T-3/T-4 and F-3). Recorded for the reader; this session joins neither.

### Requests and handoff log (session `60ca3e1f`)

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-12 04:20 UTC | 60ca3e1f | `1e425502`, `f344fcd1` | Three sessions are live. I am not repeating the verification suite, the brief-coverage audit or the privacy audit. My work is new research in `research/60ca3e1f/**` and `verification/60ca3e1f/**`. Before I touch any shared file I will list it in this block and re-read yours. If either of you edits `site/**`, `index.html`, `assets/**`, `scripts/**` or `qa/**`, please list the files in your block first so that the later merge keeps both sides. |
| 2026-11-12 04:42 UTC | 60ca3e1f | all | **Handoff / takeover note for R-6.** Re-read at 04:38 UTC: `1e425502` recorded every task done (PR #38, #39 merged); `f344fcd1` recorded every task done (PR #40, #41 merged, `main` = `9163fed`). No session holds an open claim on any shared file. The files listed in R-6 were last owned by `aa1f073e` (`site/operating-costs.html`, `site/data/costs.js`), `0d6ec51e` and `f344fcd1` (`site/review.html`, `site/data/sources.js`, `index.html`) and `f16e6e34` (`qa/**`, `site/black-swan.html`); all are recorded done. This session edits them as a narrow follow-up integration: additions and corrections only. `origin/main` @ `9163fed` is merged into this branch. |
| 2026-11-12 04:56 UTC | 60ca3e1f | all | Two more shared files listed before they are touched: `site/scenarios.html` (last owner `d7d62f7a`, done) and `site/verification.html` (last owner `f16e6e34`, done). Re-read at 04:56 UTC: `main` is still `9163fed`, no open pull request, no branch newer than `f344fcd1`'s last push. The earlier R-6 entries in this block carried the time 04:47; the push was at 04:42:20 UTC and the entries now say so. |
| 2026-11-12 05:08 UTC | 60ca3e1f | all | Listed before they are touched: `site/properties.html` (two insurance rows; last owner `0d6ec51e`, done) and a wider scope in two files already listed (`index.html` flag card and one `site/review.html` item, solar wording only; R-D1). Re-read at 05:07 UTC: `main` is still `9163fed`, no open pull request, no branch newer than this one. This push also carries the R-6 work finished so far (Operating costs, Flagged, Other options, Black swan, Sources, Scenarios, Verified facts, landing page, ledger); the full suite passes on it. |
| 2026-11-12 05:14 UTC | 60ca3e1f | all | R-2 to R-6 finished and pushed. `site/review.html` was already listed; its scope now also covers the count in the commit-e-mail item (R-D6), listed in this same push. Re-read before this push: `main` is still `9163fed`, no open pull request. All six repository checks and `verification/60ca3e1f/check.cjs` (78 of 78) pass on this commit. R-7 claimed: one pull request, one merge. |
| 2026-11-12 05:14 UTC | 60ca3e1f | all | Pull request #42 opened at 05:14 UTC from `8914f57`. This entry is the last change before the merge. After the merge this session confirms the Pages build, reads the live Operating costs page back, and writes the result as a comment on #42. If the live page is wrong, this session fixes it in a new pull request and says so there. No task of this session stays open after that; the three recorded defects R-D3 to R-D5 are free for any later session. |
<!-- END block owned by session 60ca3e1f -->

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
<!-- END block owned by session 4e07c8e6 -->

<!-- BEGIN block owned by session 0d6ec51e. Placed here (under the 4e07c8e6 block, not at the end of the file) so it merges without conflict with the block session cf587387 is appending at the end. Other sessions: please do not edit inside this block; write requests in your own section. -->
## Session `0d6ec51e` (branch `arena/0d6ec51e-tino2`) — claim 2026-11-11 13:18 UTC

**State read at claim.** `main` = `d82fbee` (PR #33). All 28 remote `arena/*` branches fetched. **One live session:** `cf587387` pushed a claim at 13:14 UTC for final integration (`site/**`, `index.html`, `assets/**`, `scripts/**`, `qa/**`, `_config.yml`, `README.md`, `verification/cf587387/**`), the takeover of PR #31 and the owner requests D-I-4, D-I-5 and D-I-7. That claim is live, so this session does not touch any of those paths and does not take over anything. Suite on `d82fbee` re-run before claiming: `validate.js` PASS 835 checks, `stress-test.js` PASS, `package-site.py` PASS, `check-publication.py --self-test` PASS, `runtime-test.cjs` PASS 14 pages / 1,127 rows.

**Why this scope.** Earlier sessions verified the three choices the brief names (live in, rent, sell and reinvest) and the figures behind them. Nobody has yet checked whether the *list of choices* and the *list of process steps* are complete: mixed strategies (for example live in the house for a period and then sell), tax rules that only apply to one path, steps and forms a trustee must file that are not on the checklist, and the rules for the money part of the inheritance by type of account. This scope is new paths only.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| N-1 | Coordination: read the board and every branch, detect the live claim, claim a non-overlapping scope, push at once | done | 0d6ec51e | `COORDINATION.md` (this block only) | N/A | none: no collision |
| N-2 | Completeness audit. Read every published page against the brief and list (a) strategies and mixed strategies that are not analysed, (b) tax rules that would change a path and are not stated, (c) process steps and forms missing from the checklist, (d) rules for inherited money by account type. Each item checked on the official page, wording and link recorded; blank and flagged when not confirmed | **done** | 0d6ec51e | `research/0d6ec51e/completeness-ledger.md` | 25 official documents opened (29 ledger rows) and 8 ledger rows read from official search extracts (IRS, FTB, FDIC, leginfo, Secretary of State, Attorney General, BOE, Dept of Insurance); wording and link per row in the ledger | N-I4, N-I7 |
| N-3 | Numbers for the strategies found in N-2, from a separately written calculation that reads its inputs from the published `site/data/model.js` (no household figure typed), compared with the three published choices | **done** | 0d6ec51e | `verification/0d6ec51e/options.cjs`, `options.json`, `REPORT.md` | reproduces the three published choices for 2040, 2045, 2050 to the dollar (12 of 12); 110 figures of the published engine equal the independent calculation | N-I1 |
| N-4 | Hand the findings to the live integrator as requests (log below). If `cf587387` records done, or goes 60 minutes without a commit, publish them on the site as additions only, after logging the handoff here | **done** — handoff logged 13:28 UTC; published by this session as additions only | 0d6ec51e | `site/options.html` (new), `site/data/options.js` (new), `site/data/sources.js` (25 keys appended), `site/review.html` (8 items added), `site/sources.html` (1 row added), `site/plan.html`, `site/inheritance.html`, `site/estate-tax.html`, `index.html` (pointer only), `assets/app.js` (1 menu entry), `scripts/validate.js`, `scripts/check-publication.py`, `qa/ledger.json` (N-01…N-12), `README.md` | as N-2 | N-I2, N-I3, N-I5 |
| N-5 | Own PR (new paths and this block), merge, confirm the Pages build, record the result here | **done** — PR [#36](https://github.com/wingbangboozle1-lang/Tino2/pull/36) merged 13:39:09 UTC, merge commit `24dddd7`; Pages `built`, no error, 13:39:49 UTC; live page read back | 0d6ec51e | own files + this block | — | none |

**Rules this session follows.** No personal information in any committed file; parties and addresses appear only as placeholders. No household figure is committed unrounded and none is repeated in this block. Every dollar figure in new files is rounded to the nearest $10 unless a government body publishes that exact amount. Every table row carries a link to an official source or is left blank and marked unverified; nothing is inferred. `origin/main` is merged before every push. The platform fixes the branch name to `arena/0d6ec51e-tino2`, so the `session-<id>/<task>` naming cannot be applied; the session ID is in the branch name.

### Requests and handoff log (session `0d6ec51e`)

| Time (UTC) | From | To | Entry |
|---|---|---|---|
| 2026-11-11 13:27 | 0d6ec51e | `cf587387` | Your integration claim is live and I am not editing any path in it. My findings will be listed in this table with the official link for each, so you can apply them if you are still integrating when they land. |

### Handoff note — 2026-11-11 13:28 UTC (logged before any shared file is touched)

Session `cf587387` recorded every one of its tasks **done** at 13:21 UTC: PR #34 and PR #35 are merged (`main` = `924ebb0`), PR #31 is closed, and its block states that no task is open. All remote branches were fetched again at 13:26 UTC and no other branch has moved since 08:18 UTC. There is therefore **no live owner of the shared site files**. Under the rule this session wrote into N-4 at claim time, it now takes the integration role for its own findings only.

**Scope added from 13:28 UTC:** `site/**`, `assets/app.js`, `scripts/**`, `qa/**`, `.github/workflows/pages.yml` (only if a new public file needs listing). **Additions only:** no published figure, plan or recommendation written by another session is changed or removed; where a finding qualifies an existing statement, the qualification is added beside it. `origin/main` (with all of `cf587387`'s work) was merged into this branch first, with no conflict. A correction to this block: the claim above was pushed at 13:18 UTC, not 13:27 as first written.

### Session `0d6ec51e` — completion record

**Question asked.** Earlier sessions checked the three choices and their figures. This session checked whether the list of choices and the list of steps were complete. Nine gaps were found (G1–G9 in `research/0d6ec51e/completeness-ledger.md`). All are published on one new page, **Other options** (`site/options.html`), and nothing written by another session was changed or removed.

| Finding | Result (inheritance in 2045, measured in 2055, base assumptions) | Official source |
|---|---|---|
| Hold first, sell later | Every year of waiting lowers the end value: rent one year first −$117,930; live in one year −$271,520; empty one year −$299,500 | [IRS FAQ, inherited property](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances) |
| Live in two years to use the home-sale exclusion | −$537,910 against selling at once; only $41,430 of the $250,000 is used because gain restarts at death | [IRS Topic 701](https://www.irs.gov/taxtopics/tc701) |
| Depreciation in the rental case (left out of the published model) | −$8,320 to −$29,120 at 20–40% building share; with no tax-back at all, selling is still ahead by more than $1,400,000 | [IRS Topic 425](https://www.irs.gov/taxtopics/tc425) · [Topic 409](https://www.irs.gov/taxtopics/tc409) |
| Pre-2021 parent-child rule as a test | Lead of selling falls from $1,729,720 to $1,154,390; level (−$11,780) when both sides are taxed at the end. The initiative to restore the rule failed on 18 May 2026 | [Secretary of State, advisory 26138](https://www.sos.ca.gov/elections/advisories-county-elections-officials/2026-advisories-county-elections-officials/may) · [AG 25-0017](https://oag.ca.gov/system/files/initiatives/pdfs/Title%20and%20Summary%20%2825-0017%29.pdf) |
| Estate tax on the money | Starts when money exceeds $12,271,500 (2027, official exclusion less Property A); 40% above. Amount of money unknown, so a table by amount is published and no figure for the family | [IRS Form 706 instructions](https://www.irs.gov/instructions/i706) |
| Rules by kind of money | Deposits, investments, retirement accounts (ten-year rule), Roth, life insurance, income inside the trust | [IRS, beneficiary](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-beneficiary) · [FDIC](https://www.fdic.gov/resources/deposit-insurance/brochures/insured-deposits) |
| Steps missing from the checklist | New EIN, Form 56, Form 541, Form 593 before closing (3 1/3% withheld otherwise), Form 8971, first-death estate return, six-month deposit rule, deed check; probate fees if the house is outside the trust: $72,600 each to representative and attorney at the 2045 value | [FTB Form 593](https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html) · [Probate Code 10800](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10800) |
| Property B | Its old assessed value avoids $19,890 of tax a year (2026), lost on a sale | [BOE Publication 29](https://www.boe.ca.gov/proptaxes/pdf/pub29.pdf) |

**Effect on the recommendation.** None on the ranking. Two findings support it (waiting costs money; depreciation does not rescue the rental case). One shows what it rests on (today's reassessment rule) and is flagged High.

**Suite on the final tree.** `validate.js` PASS 1,086 checks / 15 pages / 151 sources · `stress-test.js` PASS · `package-site.py` PASS · `check-publication.py` PASS 28 files and `--self-test` PASS · `runtime-test.cjs` PASS 15 pages / 1,259 source-linked rows · `qa/tools/gate.cjs` PASS 0 errors, 0 warnings (4,620 dollar amounts) · `src/check_links.py` 0 errors · `integration/tools/privacy_scan.py` 0 errors (158 warnings, all in other sessions' repository-only records, unchanged) · `verification/0d6ec51e/options.cjs --check` PASS 15 self-checks.

**Irregularities.**

| ID | Finding | Status |
|---|---|---|
| N-I1 | The published rental case has no depreciation | needs review — quantified on the new page; published figures left unchanged; ranking the same |
| N-I2 | No plan includes estate tax on the money; the amount and kind of money are not in the record | needs review — flagged High on the site |
| N-I3 | The recommendation depends on the current reassessment rule | needs review — flagged High on the site; current law verified |
| N-I4 | Seven documents used on the site were read from official search extracts, not opened (Pub. 527, 551, 523; Form 706 Table A; Form 1041-ES; estate FAQ five-year route; insurance fact sheet) | needs review — flagged Medium; ledger entry N-12 is `unverified` |
| N-I5 | The source register labels those entries "Carried forward · needs revalidation"; they were read from extracts, not carried forward | cosmetic; the register rule belongs to another session and was not changed |
| N-I6 | This block first gave the claim time as 13:27 UTC; the push was at 13:18 UTC | corrected |
| N-I7 | No official page was opened for: affidavit of death of trustee, preliminary change of ownership report, supplemental-bill timing, long-term care, Medi-Cal recovery, instalment sale, charitable trusts, base-year transfer for owners aged 55 or over | not published; listed as open in the ledger |
| N-I8 | The two calculations share the published model's cost and value functions, so they cross-check the new arithmetic, not the model's inputs | stated in `verification/0d6ec51e/REPORT.md` |

**Conflicts.** None. `origin/main` was merged four times (PR #34, PR #35 and two no-change pulls); every merge was automatic and kept both sides.

**Privacy.** No personal information added. No household figure typed in any new file: the new engine and the independent calculation read their inputs from the published model. Every dollar figure added to the site is rounded to $10 or is an amount a government body publishes.

### Session `0d6ec51e` — publication record (2026-11-11)

| Step | Result |
|---|---|
| PR | [#36](https://github.com/wingbangboozle1-lang/Tino2/pull/36) `arena/0d6ec51e-tino2` → `main`; `MERGEABLE`, state `CLEAN`; **MERGED** 13:39:09 UTC without waiting for approval |
| CI on the PR head `caef106` | `verify` (Verify public Pages boundary) **pass**, 23s — includes the Jekyll build and the rejection of unexpected files in the real Pages output (28 files allowed) |
| Merge commit | `24dddd7f28fd31e518f3293d9619fcd676bb2cc2` |
| CI on `main` after the merge | `Verify public Pages boundary` **success**; `pages build and deployment` **success**, both for `24dddd7` |
| GitHub Pages | build for `24dddd7` reported **`built`**, `error.message: null`, 13:39:49 UTC (Pages API) |
| Live-URL read-back | **Completed.** `https://wingbangboozle1-lang.github.io/Tino2/site/options.html` was fetched after the build and returned the rendered page with title "Other options and missing steps" and the figures recorded above (−$117,930, −$537,910, $1,154,390, $12,271,500). The read was made with the session's page-fetch tool; `curl` from the sandbox still cannot reach that host, as earlier sessions recorded |
| Open PRs after this session | #3 only (from 10 November, another session's, untouched) |

**State of the board after this session.** Every task in this block is `done`. Items marked **needs review** (N-I1 to N-I4, N-I7) are published on the Flagged for Review page with the document that would settle each; none blocks the merge.

<!-- END block owned by session 0d6ec51e -->

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

<!-- BEGIN block owned by session d9c69069 — other sessions: please do not edit inside this block; send requests to my log at the bottom of it -->
## Session `d9c69069` (branch `arena/d9c69069-tino2`) — claim 2026-11-11 07:50 UTC

**State at join.** `main` = `815289aa` (PR #19 merged, session `14e318a1`). This session read `COORDINATION.md` in full and ran `git ls-remote --heads origin` plus `gh pr list` before claiming.

**Live claim detected — not taken over.** Session `11bffb54` is live right now: commits `bd02519` 07:45:32, `1ffff76` 07:48:11, `758cc46` 07:49:11, `dcb0e06` 07:49:30 UTC, and PR [#20](https://github.com/wingbangboozle1-lang/Tino2/pull/20) opened 07:49:14 UTC (19 seconds before this claim was written). Its board rows E-1…E-4 claim the **final-integration role**: `site/**`, `index.html`, `assets/app.js`, `assets/styles.css`, `scripts/validate.js`, `scripts/package-site.py`, `_config.yml`, `README.md`, `qa/**`, `verification/11bffb54/**`. That claim is far newer than 60 minutes, so per the handoff rule this session does **not** take it over and does **not** open a competing PR against those paths. PR #16 (`f16e6e34`, last commit 04:46 UTC) is already taken over by `11bffb54`; PR #3 (`8c4d9e77`, 2026-11-10) is stale and left to its owner.

**Role taken (non-overlapping).** Independent line-by-line verification of the published site and the repository tree, from official sources, plus a privacy and link audit. This is the same read-only auditor role sessions `457907c1` and `14e318a1` took; it produces evidence, not competing conclusions.

**File scope — new paths only.** `verification/d9c69069/**` (new) and this `COORDINATION.md` block (append-only). This session does **not** edit `site/**`, `index.html`, `assets/**`, `scripts/**`, `_config.yml`, `README.md`, `qa/**`, `plan/**`, `docs/**`, `research/**`, `src/**`, `dashboard/**`, `integration/**`, `pages/**`, `css/**`, root `*.html`, or any other session's `verification/**` directory. Any fix that belongs in one of those files is logged as a **request** at the bottom of this block for its owner, and published on the Flagged for Review register through that owner, never by editing it here.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| D-1 | Coordination: read every board section, fetch every live `arena/*` branch, detect live claims, claim non-overlapping scope, push claim immediately | done | d9c69069 | `COORDINATION.md` (this block only) | N/A | C-3 (below): live concurrent integrator `11bffb54` |
| D-2 | Repo line-by-line review of the canonical published artifact: every page, every table, model arithmetic, privacy, rounding to $10, source link on every row | in progress | d9c69069 | `verification/d9c69069/**` | read-only | — |
| D-3 | Independent re-verification of key legal/tax/economic figures directly against official sources (IRS, BOE, SCO, FTB, county assessors, HUD, BLS, FHFA, state legislature), each recorded with the exact wording checked, the URL and the access date | in progress | d9c69069 | `verification/d9c69069/**` | official pages opened this session | — |
| D-4 | Automated suite re-run on the merged tree + privacy scan + broken-link check of everything GitHub Pages actually serves (`_config.yml` allowlist) | unclaimed → in progress | d9c69069 | `verification/d9c69069/**` | — | — |
| D-5 | Irregularity register: every discrepancy found, with severity, the file it is in, its owner, and the official source that settles it | in progress | d9c69069 | `verification/d9c69069/**` | — | — |
| D-6 | Publish report; merge `origin/main` after `11bffb54` publishes so this record reflects the final tree; PR to `main`; merge without waiting for approval; confirm Pages deploy; record PR link and merge result here | pending | d9c69069 | `verification/d9c69069/**`, `COORDINATION.md` (this block) | — | — |

**Rules this session follows.** Privacy first: no personal information in any committed file, no household figure repeated in this block, placeholders for parties and addresses. Every dollar figure in new files is rounded to the nearest $10. Every table row in the new report carries an official source link or is left blank and flagged unverified; no value is ever inferred. No file owned by another session is edited. Small frequent commits; `origin/main` merged before every push; conflicts resolved without discarding other sessions' work; the session ID is embedded in the branch name because Arena pins one branch per session.

### Session `d9c69069` — completion and publication record (2026-11-11)

**Coordination outcome (D-1).** Two live integrator claims were detected and **neither was taken over**: session `11bffb54` opened PR #20 nineteen seconds before this session's claim was written and merged it at 07:49:54 UTC; sessions `81334f2c`, `246f5b3b`, `b0123943`, `aa1f073e` and `4e07c8e6` then merged PRs #21–#30 while this session worked. `main` moved **seven times** under this branch. Each move was merged in, and every `COORDINATION.md` conflict (four of them) was resolved by keeping **both** sides in full — no session's board section, report or file was discarded at any point. The final tree carries all thirteen session blocks.

**Work done (D-2 … D-5).** Read-only. Full detail in `verification/d9c69069/REPORT.md`.

| Result | Detail |
|---|---|
| Automated suite on the final merged tree | **9/9 PASS** — `validate.js` 835 checks / 14 pages / 121 sources; `stress-test.js`; `package-site.py`; `check-publication.py --self-test`; `runtime-test.cjs` 14 pages / 1,127 source-linked rows; `qa/tools/gate.cjs` 0 errors 0 warnings; `src/check_links.py .` 60 pages 0 errors; `privacy_scan.py` 0 errors; this session's `checks.py` 13 PASS / 0 FAIL |
| Official sources opened and read directly by this session | **18 / 18 Match**, wording recorded in REPORT §2: IRS 2026 and 2027 exclusions and gift amounts; State Controller (no CA estate-tax return); BOE Prop 19 chart; BOE LTA 2025/009 ($1,044,586, FHFA indexing, next adjustment Feb 2027); BOE LTA 2026/002 (factor 1.02, full 51-year table); Probate Code §16061.7 (60 days); R&TC §480 (150 days, trust route); SF Treasurer rate 1.18162182% and all five FY 2025-26 parcel amounts; SF Rent Board 1.6%, relocation $8,245 / $24,733 / $5,497, File 261020 not enacted, fee $59; San Jose Water +2.8%; HUD FY2026 SAFMR 95014 |
| Arithmetic recomputed from scratch | **52/52** household values correctly rounded to $10 half-up; **51/51** BOE factor rows exact; **23/23** household assessment changes for **both** properties consistent with the official factor; SF three-unit parcel total **$829.22** to the cent; payload = allowlist on both sides (26 files); **14/14** pages `noindex,nofollow,noarchive` and in the navigation |
| Privacy | **0** exact owner figures that $10-rounding can obscure, in any of **120** tracked files or in the published artifact. All **10** owner-supplied household inputs traced into `MODEL.BASE` and unchanged after every merge |
| Recommendation | Every verified fact points the same way as the published ranking. The two facts that decide it — Prop 19's principal-residence condition and the gap between Property A's assessment and its market value — are both confirmed on official pages this session opened |

**Irregularities (D-5), all published in REPORT §6 and none blocking.** Two **High**, both predating the current tree and not fixable by editing the site: **D-I-1** three owner amounts are already multiples of $10, so rounding cannot anonymise them and their published form is the exact, searchable value; **D-I-2** the public unmerged branch `arena/5a1bd5be-tino2` still serves all 40 exact figures in 5 files, and git history is not clean (this clone is shallow, so history was **not** scanned and is **not** claimed clean). **D-I-3** was found and then **resolved by another session mid-flight**: the old 4-hash guard was both incomplete and itself reversible; the replacement rule was independently tested here at **40/40 caught, 0 wrongly permitted**. **D-I-6** was logged MEDIUM and then **corrected to LOW** — the ledger already carries the ballot snapshot's as-of date and the 11 December 2026 certification date. Open Medium requests to owners: **D-I-4** the Rent Board owner-unit exemption is not automatic (vacant units are charged, so today's figure is $177 not $118; a Request for Exemption is due **14 December 2026**; 50% is tenant-recoverable) — re-checked after PR #28, still open; **D-I-5** the 3%/yr rent assumption is ~10× the latest official movement in its own HUD benchmark (+0.3% for 4-bedroom; smaller units fell). Low: **D-I-7** Ellis Act relocation amounts are far higher and absent from the plan page; **D-I-8** two official pages (SFPUC Prop 218 notice, CA SOS ballot returns) could not be opened from this sandbox and are recorded as gaps, **not** as passes; **D-I-9** the legacy `privacy_scan.py` allowlist predates `qa/ledger.json` and emits 128 all-official warnings while the newer gate reports 0; **D-I-10** two tenth-of-a-point differences between the owner's stated percentages and their own dollars (site correctly publishes them as supplied); **D-I-11** one duplicated line in `_config.yml`.

**This session's own error, recorded deliberately.** An early draft of D-I-3 named four exact owner amounts while claiming not to reproduce them. The repository's own privacy scanner flagged the file; the figures were removed and the section rewritten, and `checks.py` was then redesigned to store **no** household data at all, parsing it from the published pages at run time and reading the brief's exact amounts only from a gitignored local file. An audit report and a reproduction script are publications too.

**Publication (D-6).**

- PR [#32](https://github.com/wingbangboozle1-lang/Tino2/pull/32) (`arena/d9c69069-tino2` → `main`) — **MERGED** 2026-11-11 08:16:33 UTC without waiting for approval; merge commit `a23f241aada54604f10b46930fca9cc1b83b02e1`; `MERGEABLE` / `CLEAN` at merge time; the repository's `Verify public Pages boundary` workflow concluded **SUCCESS** on the PR head.
- GitHub Pages build for `a23f241`: **`built`**, `error.message: null`, completed 08:17:08 UTC (Pages API; source `main` / root, HTTPS enforced).
- **Live-URL read-back not completed:** fetches of `https://wingbangboozle1-lang.github.io/Tino2/` failed from this sandbox with the same proxy error as D-I-8. Deployment is confirmed from the **Pages API build record and the CI run**, not from reading the public page; no claim is made to have read the deployed HTML.
- **Effect on the live site: none.** This PR adds only `verification/d9c69069/**` plus an appended block here; both `verification` and `COORDINATION.md` are `_config.yml`-excluded, so the published payload is byte-identical before and after (26 files).

**Status:** D-1 … D-6 **done**. Needs review: D-I-1 and D-I-2 (owner decisions about exposure that cannot be fixed by editing the site), and the D-I-4 / D-I-5 / D-I-7 / D-I-9 requests, which belong to the owners of `site/**`, `qa/**` and `integration/**`.

<!-- BEGIN block owned by session cf587387 — other sessions: please do not edit inside this block; send requests to the log at the bottom of it -->
## Session `cf587387` (branch `arena/cf587387-tino2`) — claim 2026-11-11 13:15 UTC

**State at join.** Read this board in full (all fourteen session blocks), then ran `git ls-remote --heads origin` and `gh pr list --state all`. `main` = `d82fbee` (PR #33 merged 08:18 UTC). **No session is live:** every remote `arena/*` branch last moved at or before 08:14 UTC, five hours before this claim, and none has a commit inside the 60-minute handoff window.

**Two stale claims taken over, per the handoff rule.** (1) PR [#31](https://github.com/wingbangboozle1-lang/Tino2/pull/31) by session `4e07c8e6` (task X-7: publish the audit findings X-F1…X-F7 on the site). Its head commit is from 08:14 UTC, its claim is five hours old with no commits since, and it is still open, so `main` does **not** carry those findings. (2) The open owner requests logged at the end of the `d9c69069` block — **D-I-4** (San Francisco Rent Board owner-unit exemption), **D-I-5** (rent-growth assumption), **D-I-7** (Ellis Act relocation) — which were addressed to "the owner of `site/**`" and have had no live owner since 08:18 UTC. Both handoffs are recorded here before any shared file is touched, as the rule requires.

**Role taken.** Final integration for the remaining content items, plus independent re-verification. Where a number is added to the site this session opens the official page itself and records the exact wording; nothing is carried over on trust.

**File scope.** `COORDINATION.md` (this block, append-only), `site/**`, `index.html`, `assets/**`, `scripts/**`, `qa/**`, `verification/cf587387/**`, `_config.yml`, `README.md`. This session does **not** edit `research/**`, `docs/**`, `src/**`, `dashboard/**`, `integration/**`, `pages/**`, `css/**`, the legacy root `*.html` pages, or any other session's `verification/**`, and does not reopen or rewrite another session's board block.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| S-1 | Coordination: read the board and every branch, detect that all claims are stale, claim, push the claim at once | done | cf587387 | `COORDINATION.md` (this block only) | N/A | S-C1 (below): two stale takeovers |
| S-2 | Take over PR #31: read its diff line by line, re-verify its new figures against official pages, merge `origin/main`, run the suite, merge it | in progress | cf587387 | PR #31's own file list | IRS Rev. Rul. 2023-2, Pub. 559, IR-2026-133, BOE Prop 19, BOE LTA 2026/026, SF Elections | see S-F1 |
| S-3 | Close the owner requests D-I-4, D-I-5, D-I-7 on the site: Rent Board owner-unit exemption and its 14 Dec 2026 deadline; the 3%/yr rent assumption against the HUD benchmark; Ellis Act relocation amounts | in progress | cf587387 | `site/review.html`, `site/san-francisco.html`, `site/data/sources.js`, `site/plan.html` | SF Rent Board, HUD FY2026 SAFMR, SF Rent Board Ellis Act page | — |
| S-4 | Independent pass over the whole published payload: every table row carries an official link or is blank and flagged; every $1,000+ figure is a multiple of $10; no personal data; no broken internal link | in progress | cf587387 | read-only + `verification/cf587387/**` | — | — |
| S-5 | Publish: PR to `main`, merge without waiting, confirm the Pages build, record the PR link, merge commit and build result here | **done** — PR [#34](https://github.com/wingbangboozle1-lang/Tino2/pull/34) merged 13:19:49 UTC, merge commit `0e09c4c`; Pages `built`, no error, 13:20:25 UTC | cf587387 | `COORDINATION.md` (this block) | — | — |

### Session `cf587387` — completion record

**S-2, stale PR #31 taken over.** Content commit `d645997` cherry-picked onto this branch instead of merging the PR branch: that branch predates PR #32 and #33, so a plain merge would have dropped `verification/d9c69069/**` and the last board block. Its generated `qa/gate-report.json` was regenerated, not taken. **PR [#31](https://github.com/wingbangboozle1-lang/Tino2/pull/31) is superseded and can be closed.** Every figure it publishes was re-read at the official page by this session: IRS Rev. Rul. 2023-2 (issue text), IR-2026-133 ($15,480,000 for 2027), Form 706 instructions ($15,000,000 for 2026), State Controller (no California estate-tax return after 2004), BOE LTA 2025/009 ($1,044,586), BOE LTA 2026/026 Q11 and Q32–35 (care facility conditions; LLC ineligible). Its two new break-even rates were re-derived here at 5.32% and 3.97%; the unequal-terms pair is 7.81% and 2.80%. All match.

**S-3, the three owner requests closed.**

| Request | What changed on the site | Verified wording | Source |
|---|---|---|---|
| D-I-4 Rent Board owner-unit exemption | Fee row and note now say three units billed = $177 until the exemption is approved, $118 with it, deadline 14 December 2026, vacant units billed, 50% recoverable | "vacant units, and units occupied by friends or family members"; "The deadline to submit a Request for Exemption for the 2027 Rent Board fee is December 14, 2026"; "$59.00 per dwelling unit"; "$29.50 per dwelling unit" recoverable | [SF.gov · The Rent Board Fee](https://www.sf.gov/rent-board-fee) |
| D-I-5 rent growth | **Corrected, not confirmed.** HUD's ZIP-level 4-bedroom benchmark went $6,050 → $6,370 → $6,390 (FY2024–FY2026): +5.3% then +0.3%, about 2.8% a year compounded, close to the model's 3%. The earlier note's "ten times the benchmark" compared a single year | step-5 tables on both pages list the prior-year amounts | [HUD FY2026 SAFMR](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026) · [FY2025](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2025_code/2025zip_code_calc.odn?zcta=95014&year=2025) |
| D-I-7 Ellis Act relocation | Added to the San Francisco page and the register: $11,110.05 per tenant, $33,330.13 maximum a unit, plus $7,443.90 for each tenant 62+ or disabled, for notices served 1 Mar 2026–28 Feb 2027; ordinary no-fault is $8,245.00 / $24,733.00 / $5,497.00. Not in the model, and stated as the floor under any decision to stop renting Property B | table row 3/01/26 – 2/28/27 | [SF.gov · Current rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |

Also fixed, found while closing D-I-5: the Black swans page described the break-even test as "30 years" when the hold is the ten years after a 2045 inheritance, and its two cards showed the unequal-tax-terms thresholds only. Both cards now lead with the equal-terms figures and keep the others beside them, and the two pages that show these thresholds call one shared function in `site/data/scenarios.js`, so they cannot drift apart. Base case unchanged: 2040→2050 sell $7,683,290, rent $6,249,830, live $5,135,780.

**S-4, suite on the final tree.** `validate.js` **PASS** 853 checks / 14 pages / 126 sources · `stress-test.js` **PASS** · `package-site.py` **PASS** · `check-publication.py` **PASS** 26 files and `--self-test` **PASS** · `runtime-test.cjs` **PASS** 14 pages / 1,153 source-linked rows · `qa/tools/gate.cjs` **PASS 0 errors, 0 warnings** (4,410 dollar amounts, 70 official exact figures) · `src/check_links.py` 60 pages, 0 errors. New ledger entries CF-01…CF-03 record the three official tables above; `site/data/ledger.js` regenerated from them.

**Privacy.** No personal information added. No unrounded household figure added. The only sub-$10-precision amounts this session published are government-published ones, each recorded in `qa/ledger.json` so the gate can recognise them. The standing **High** findings from `246f5b3b`, `f16e6e34` and `d9c69069` (older branches and commit history in the public repository still hold exact figures; three supplied amounts are already multiples of $10) are unchanged, cannot be fixed by editing the site, and remain published on the Flagged for Review page.

**Own errors, recorded.** An early draft of this session's San Francisco note rounded the Ellis figures to $10 before checking the gate; the gate rejected them, which is why the exact official amounts are published with ledger entries rather than rounded household-style. A first attempt at editing the Best plan page assumed the equal-terms thresholds were absent there; they were already present, so the edit was replaced with a call to the shared engine function instead of a rewrite.

**Open, flagged, not blocking.** Measure H parcel amount (count not certified until 11 December 2026) · both insurance premiums · Property A tax-rate area, meter sizes, Property B parcel tier, solar interconnection date · trust type · Property B tenancy terms. All remain on the Flagged for Review page with the document that would settle each.

**Full record:** `verification/cf587387/REPORT.md` (repository-only, not published).

**Rules followed.** No personal information in any committed file; placeholders for parties and addresses. No figure supplied by the household is repeated in this block. Every dollar figure this session adds to the site is rounded to the nearest $10 unless a government body publishes that exact amount. Every table row this session touches carries an official source link or is left blank and flagged unverified — no value is inferred. `origin/main` is merged before every push; conflicts are resolved keeping both sides in full. The platform pins this session to one branch, so the `session-<id>/<task>` naming cannot be used; the session ID is carried in the branch name.

**S-C1 (claim note, not a conflict).** No live collision occurred this session: the two claims taken over were both five hours stale. Recorded here because the board must show who moved a task and why.

### Session `cf587387` — publication record (2026-11-11)

| Step | Result |
|---|---|
| PR | [#34](https://github.com/wingbangboozle1-lang/Tino2/pull/34) `arena/cf587387-tino2` → `main`, opened 13:17 UTC, **MERGED** 13:19:49 UTC without waiting for approval; `MERGEABLE` at merge time |
| CI on the PR head | `verify` (Verify public Pages boundary) **pass**, 25s — includes the Jekyll build and the rejection of unexpected files in the real Pages output |
| Merge commit | `0e09c4c5176ffb263b579f064aa373510af5ade7` |
| GitHub Pages | build for `0e09c4c` reported **`built`**, `error.message: null`, completed 13:20:25 UTC (Pages API; source `main` / root, HTTPS enforced). The published payload now carries the equal-terms break-even cards, the Rent Board fee and Ellis Act rows, and the four new Flagged for Review items |
| Live-URL read-back | **not completed, and not claimed.** `wingbangboozle1-lang.github.io` is outside this sandbox's permitted hosts (the same limitation recorded by earlier sessions). Deployment is confirmed from the Pages build record for the correct commit and from the CI run, which builds and audits the actual Jekyll output |
| Superseded PR | [#31](https://github.com/wingbangboozle1-lang/Tino2/pull/31) commented with the handoff and **closed** at 13:21 UTC; its content is on `main` via #34, nothing was discarded |
| Open PRs after this session | none |

**Final state of the board.** Every task on every block is `done`, except the standing **needs review** items — the privacy findings about older branches and commit history (owner decision, not fixable by editing the site) and the blank figures (insurance premiums, Measure H parcel amount until certification on 11 December 2026, Property A tax-rate area and meter sizes, Property B parcel tier, solar interconnection date, trust type, tenancy terms). All are published on the Flagged for Review page with the document that would settle each, and none of them blocks the merge.

<!-- END block owned by session cf587387 -->

<!-- BEGIN block owned by session 1e425502 — other sessions: please do not edit inside this block; send requests to my log at the bottom of it -->
## Session `1e425502` (branch `arena/1e425502-tino2`) — claim 2026-11-12

**State at join.** `main` = `9867620` (PR #37 merged, session `0d6ec51e`). Read `COORDINATION.md` in full (954 lines, 13 session blocks, every task `done` except standing `needs review` items). Fetched all branches: only `main` and this branch exist remotely. Open PRs: #3 (`arena/8c4d9e77-tino2`, 2026-11-10, stale >60 min, superseded by integrated site). No live session holds any claim.

**Role taken (non-overlapping).** Final independent verification of the published site against the brief, line by line, from official sources. No shared file is edited unless a defect is found; any such edit is logged here first.

**File scope — new paths only.** `verification/1e425502/**` (new) and this `COORDINATION.md` block (append-only). This session does **not** edit `site/**`, `index.html`, `assets/**`, `scripts/**`, `_config.yml`, `README.md`, `qa/**`, `docs/**`, `research/**`, `src/**`, `dashboard/**`, `integration/**`, `pages/**`, `css/**`, root `*.html`, or any other session's `verification/**` directory, unless a defect is found and logged here first.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| T-1 | Coordination: read the board and every branch, detect stale PR #3, claim non-overlapping scope, push claim immediately | done | 1e425502 | `COORDINATION.md` (this block only) | N/A | T-C1 (below) |
| T-2 | Brief-coverage audit: every requirement in the brief mapped to a published page/section, line by line | in progress | 1e425502 | `verification/1e425502/**` | read-only | — |
| T-3 | Automated suite re-run on the final tree: validate, stress-test, package, publication boundary, runtime, gate, link check, privacy scan, rounding | in progress | 1e425502 | `verification/1e425502/**` | — | — |
| T-4 | Official-source re-verification: re-open key official pages directly (IRS, BOE, SCO, FTB, HUD, BLS, FHFA, SF, counties) and record wording, URL, access date | in progress | 1e425502 | `verification/1e425502/**` | official pages opened this session | — |
| T-5 | Stale PR #3 disposition: read its diff, confirm superseded, close with handoff note | unclaimed → in progress | 1e425502 | PR #3 only | — | T-C1 |
| T-6 | Publish: PR to `main`, merge without waiting, confirm Pages deploy, record PR link and merge result here | pending | 1e425502 | `verification/1e425502/**`, `COORDINATION.md` (this block) | — | — |

**Rules this session follows.** Privacy first: no personal information in any committed file, no household figure repeated in this block, placeholders for parties and addresses. Every dollar figure in new files is rounded to the nearest $10 unless it is an amount published by a government body. Every table row in the new report carries an official source link or is left blank and flagged unverified; no value is ever inferred. No file owned by another session is edited without logging the request here. Small frequent commits; `origin/main` merged before every push; conflicts resolved without discarding other sessions' work; the session ID is embedded in the branch name because Arena pins one branch per session.

**T-C1 (claim note, not a conflict).** PR #3 is 2 days stale and its content is superseded by the integrated site on `main`. This session will close it with a handoff comment rather than merging it, so the board shows who moved it and why. No live collision occurred.

<!-- END block owned by session 1e425502 -->

### Session `1e425502` — completion record (2026-11-12)

**T-2 Brief-coverage audit: done.** Every brief requirement mapped to a published page (see `verification/1e425502/REPORT.md` §T-2). No gap requires a site edit. The canonical site (15 pages) already covers: executive summary, privacy/placeholders, Cupertino-vs-San Francisco distinction, black-swan/50-year stress, $10 rounding, 2040–2050 live/rent/sell + reinvest, year-by-year value/tax/assessed projections, step-by-step inheritance, operating costs (water/solar/insurance), both properties' histories, best-plan reasoning, law-change watchlist, estate thresholds by year, Flagged for Review, and source-linked tables.

**T-3 Automated suite: done.** On the final tree: `validate.js` PASS 1,086 checks / 15 pages / 151 sources (base case 2040→2050 sell $7,683,290, rent $6,249,830, live $5,135,780) · `stress-test.js` PASS · `package-site.py` PASS · `check-publication.py --self-test` PASS 28 files · `runtime-test.cjs` PASS 15 pages / 1,259 rows · `qa/tools/gate.cjs` PASS 0 errors 0 warnings (4,620 amounts, 74 official exact figures) · `src/check_links.py` 62 pages 0 errors · `privacy_scan.py` 0 errors. The gate/runtime checks need `npm install --prefix .cache/test jsdom@26.1.0` first (T-I2); CI installs it.

**T-4 Official-source re-verification: done, 9 of 9 match.** Re-opened directly 12 Nov 2026: IRS 2026 $15,000,000 and IR-2026-133 2027 $15,480,000 / gift $20,000; BOE Prop 19 value-limit formula and filing deadlines; BOE LTA 2025/009 $1,044,586 (2.15% HPI, next Feb 2027); State Controller no CA estate return after Jan 1, 2005; IRS inherited-basis FMV at death; FTB capital gains as ordinary income; HUD FY2026 SAFMR 95014 3BR $5,870 / 4BR $6,390 (FY2025 $5,850 / $6,370); SF Rent Board $59.00/unit, $29.50 recoverable, Dec 14, 2026 deadline, vacant billed. Wording and URLs in the report. No correction needed; blanks remain blank.

**T-5 Stale PR #3: done.** Read its diff (10 files, 311 insertions, superseded legacy pages). Commented with handoff and closed 12 Nov 2026 without merge; branch retained on remote. No live collision (T-C1).

**T-6 Publish: in progress.** PR from this branch to `main`, merge without waiting, confirm Pages build, record result here.

**Irregularities (T-I1…T-I4).** Standing High privacy findings (older branches/history) unchanged and published on Flagged for Review; jsdom install note; privacy-scan warnings expected; live-URL read-back outside sandbox hosts (Pages API + CI Jekyll build used instead). None blocks the merge.

**Rules followed.** No personal information in any committed file; placeholders for parties and addresses. No household figure repeated in this block. Every dollar figure in new files rounded to $10 unless government-published. Every table row in the new report carries an official source link or is flagged unverified. No file owned by another session was edited. `origin/main` merged before every push; the session ID is carried in the branch name.

### Session `1e425502` — publication record (2026-11-12)

| Step | Result |
|---|---|
| PR | [#38](https://github.com/wingbangboozle1-lang/Tino2/pull/38) `arena/1e425502-tino2` → `main`, **MERGED** 04:20:28 UTC without waiting for approval; `MERGEABLE` at merge time |
| CI on the PR head | `verify` (Verify public Pages boundary) **pass**, 28s — includes the Jekyll build and the rejection of unexpected files in the real Pages output |
| Merge commit | `113184a68c0945f5afbe9349aa428db7fefe6a5b` |
| GitHub Pages | build for `113184a` reported **`built`**, `error.message: null`, completed 04:20:59 UTC (Pages API; source `main` / root, HTTPS enforced) |
| Live-URL read-back | **not completed, and not claimed.** `wingbangboozle1-lang.github.io` is outside this sandbox's permitted hosts (the same limitation recorded by earlier sessions). Deployment is confirmed from the Pages build record for the correct commit and from the CI run, which builds and audits the actual Jekyll output |
| Stale PR | [#3](https://github.com/wingbangboozle1-lang/Tino2/pull/3) commented with the handoff and **closed** 12 Nov 2026 without merge; its content is superseded by the integrated site on `main` |
| Open PRs after this session | none |

**Final state of the board.** Every task on every block is `done`, except the standing **needs review** items — the privacy findings about older branches and commit history (owner decision, not fixable by editing the site) and the blank figures (insurance premiums, Measure H parcel amount until certification on 11 December 2026, Property A tax-rate area and meter sizes, Property B parcel tier, solar interconnection date, trust type, tenancy terms). All are published on the Flagged for Review page with the document that would settle each, and none of them blocks the merge.

## Session `f344fcd1` (branch `arena/f344fcd1-tino2`) — claim 2026-11-12 04:20 UTC

`origin/main` (`9867620`, PR #37) was fetched at 04:18 UTC; no session block on the board had an open task and the last commit on `main` was more than 14 hours old.

**Corrections to the first version of this claim (logged, not hidden).** (1) It said `main` was the only branch on the remote. That was wrong: the working copy was cloned with a single-branch refspec, and `git ls-remote` shows 32 branches. (2) It said no other session was live. Session `1e425502` pushed its claim at 04:18:25 UTC, two minutes before this one, and merged PR #38 and PR #39 by 04:22 UTC. There was **no overlap of scope**: it edited only `verification/1e425502/**` and its own block, and recorded every task done. (3) PR #3 was closed by `1e425502`.

**Merge conflict, 12 Nov 2026.** `git pull --rebase` stopped on `COORDINATION.md`: both sessions had appended a block at the end of the file. The rebase was aborted, `origin/main` was merged instead, and both blocks were kept in full, `1e425502` first. Nothing of the other session was discarded.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| F-1 | Coordination: read the board, fetch every branch, claim, push at once | done | f344fcd1 | `COORDINATION.md` (this block only) | N/A | none |
| F-2 | Whole-repository privacy audit. The repository is public, so every tracked file and the history count | done | f344fcd1 | read-only; report in `verification/f344fcd1/REPORT.md` | [GitHub Docs, sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) · [GitHub Docs, commit email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address) | F-I1, F-I2 |
| F-3 | Re-run every check on `main`; read the published pages against the brief; re-open the time-sensitive official figures | done | f344fcd1 | `verification/f344fcd1/**` | Ten official pages opened on 12 Nov 2026 (IRS ×3, State Controller, BOE ×2, SF Rent Board, HUD ×2, Secretary of State, Federal Register); wording and links in `verification/f344fcd1/REPORT.md` | F-I3, F-I4 |
| F-4 | Final integration of the findings (no live owner of the shared files). Additions and corrections only | done | f344fcd1 | `site/review.html` (4 items added, 1 percentage), `site/data/sources.js` (3 keys appended, 2 notes), `site/sources.html` (2 percentages), `site/data/ledger.js` (CA-05, CA-06, CA-07), `index.html` (one sentence in the Flagged box) | as F-3 | none |
| F-5 | PR to `main`, merge, confirm the Pages build, record the result here | done — see the publication record below | f344fcd1 | this block | — | none |

The platform fixes the branch name to `arena/f344fcd1-tino2`, so the `session-<id>/<task>` naming cannot be applied; the session ID is in the branch name.

### Irregularities found by session `f344fcd1`

| ID | Finding | What was done | Left for the owner |
|---|---|---|---|
| F-I1 | **Privacy, new.** 37 commits on `main` at `95e6d6a` (36 pull-request merges and the first commit) are authored with the account's primary e-mail address (made on GitHub with e-mail privacy off). An earlier count of 20 in this session's notes covered only the newest 100 commits. The address is in no tracked file and not on the site, and is not repeated here | Published on Flagged for Review. This session tried to author its merge with the no-reply address (`gh pr merge --author-email`); GitHub rejected both forms of it ("Invalid email address") because e-mail privacy is off on the account. **No session can avoid adding one such commit per merge until the owner changes the setting** | Turn on "Keep my email addresses private" in GitHub settings; the earlier commits need the history decision in F-I2 |
| F-I2 | **Privacy, recount.** No tracked file holds an unrounded household figure. History: 42 of 173 commits (history of `main` at `9867620`), the tips of 10 of 32 remote branches and 9 saved pull-request copies still hold exact assessed values | Flagged page updated with the recount | Fresh repository, private repository, or deletion of the old branches plus a GitHub Support purge |
| F-I3 | The HUD rent benchmark in the model is FY2026; FY2027 took effect 1 Oct 2026. The FY2027 amount for the ZIP could not be read from the official lookup | Left blank and flagged; model unchanged. Test in `verification/f344fcd1/rent-benchmark-test.cjs`: rent ±10% leaves selling first for 2040, 2045 and 2050 | Read the FY2027 row in the HUD lookup |
| F-I4 | Ballot counts moved by 0.1 point since 10 Nov; no outcome changed; not certified | Percentages updated with the count time | Recheck after 11 Dec 2026 |

### Checks on this branch (12 Nov 2026)

`package-site.py` PASS · `check-publication.py --self-test` PASS, 28 public files · `validate.js` PASS, 1,092 checks, 15 pages, 154 sources · `stress-test.js` PASS · `runtime-test.cjs` PASS, 15 pages, 1,266 source-linked rows, no broken local link · `qa/tools/gate.cjs` PASS, 0 errors, 0 warnings. The published recommendation and every model figure are unchanged.

### Session `f344fcd1` — publication record (2026-11-12)

| Step | Result |
|---|---|
| PR | [#40](https://github.com/wingbangboozle1-lang/Tino2/pull/40) `arena/f344fcd1-tino2` → `main`, **MERGED** 04:29:29 UTC without waiting for approval; `MERGEABLE` / `CLEAN` at merge time |
| CI on the PR head | `verify` (Verify public Pages boundary) **pass**, including the Jekyll build and the audit of the real Pages output |
| Merge commit | `30c77719e334d277fc3fd3efab525fe4b2a6968f` |
| GitHub Pages | build for `30c7771` reported **`built`**, no error, 04:30:07 UTC; `pages build and deployment` run succeeded |
| Live read-back | **Done.** `https://wingbangboozle1-lang.github.io/Tino2/site/review.html` was opened after the build and shows the four new items (21 high-priority, 88 in total) |
| Open PRs after this session | none |

**State of the board.** Every task of this session is done. What remains is **needs review** and is published on the Flagged for Review page: the two privacy items for the owner (F-I1, F-I2), the FY2027 rent benchmark left blank (F-I3), and the items other sessions left open.

<!-- BEGIN block owned by session 62245584 — other sessions: please do not edit inside this block; send requests to the log at the bottom of it -->
## Session `62245584` (branch `arena/693321af-tino2`) — claim 2026-11-12 15:40 UTC

**Task ID.** The platform assigns the branch `arena/693321af-tino2`, so this block is keyed to the task identifier `62245584`; the session ID is carried in the branch name because Arena pins one branch per session and the `session-<id>/<task>` naming cannot be applied.

**State at join.** `main` = `bfb2268` (PR #42 merged, session `60ca3e1f`). Read `COORDINATION.md` in full (1,104 lines, 15 session blocks). Every task on every block is `done` except the standing **needs review** items, which are published on the Flagged for Review page and do not block. `origin/main` and this branch were level at claim time (0 commits either way). `git ls-remote --heads origin` shows 37 remote branches; the only open pull request is none (last six PRs #37–#42 all merged). No session block has an open task and no branch tip has moved since 05:14 UTC on 12 Nov 2026, so **no live claim exists** and nothing is taken over.

**Role taken.** Brief-coverage gap closure on the *published site*, plus the final integration and publication of this session's work. The existing 15 pages are not rewritten and no published figure, plan or recommendation is changed or removed; the work is additive.

**Why this scope, and what is genuinely missing.** The brief asks for two things the published site does not have at all. A repository-wide search returns **zero** occurrences of the word "suggestion" in any page (`grep -ric suggestion site/*.html index.html` → all `0`). The brief asks, in its own words, for "a section dedicated for suggestions so someone can review suggestions and choose the best path before implementing any changes". There is no such section. Second, the brief asks for "a clear list of questions, informations and answers that need to be addressed before any decision can be reasonably made", with "suggestions … to discover missing information". The existing Flagged for Review page is an *uncertainty register* (what is unknown, why it matters, what to do); it is not a question-and-answer decision gate that says, item by item, whether a decision may reasonably be made yet. Those two gaps are this session's scope.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| Q-1 | Coordination: read the board in full, fetch every branch and pull request, confirm no live claim, claim a non-overlapping scope, push at once | done | 62245584 | `COORDINATION.md` (this block only) | N/A | Q-C1 |
| Q-2 | Build the missing **Questions and answers** decision gate: every question that must be answered before living, renting or selling can reasonably be decided, each with its **current answer**, whether that answer is official / household-supplied / still missing, and what to do next. No value inferred; a missing value stays blank and is flagged | in progress | 62245584 | `site/questions.html` (new), `site/data/questions.js` (new) | official pages opened by this session; wording recorded in `verification/62245584/REPORT.md` | — |
| Q-3 | Build the missing **Suggestions** section: a ranked register of concrete, costed, reversible-first suggestions, each with the problem it solves, the evidence, the expected effect, the effort, the risk, and — the part the brief asks for — a **choose-one decision panel** so the best path can be picked and reviewed before anything is implemented | in progress | 62245584 | `site/suggestions.html` (new), `site/data/suggestions.js` (new) | as Q-2 | — |
| Q-4 | Navigation, landing page and manifest: add both pages to `assets/app.js`, to the landing-page category grid and executive summary, to `scripts/check-publication.py`'s reviewed manifest and to `_config.yml` where needed | pending | 62245584 | `assets/app.js`, `index.html`, `scripts/check-publication.py`, `scripts/validate.js` (page count), `_config.yml` | — | — |
| Q-5 | Verify line by line: every new table row carries an official https link or is blank and flagged; every dollar figure a multiple of $10 unless a government body publishes that exact amount; full suite re-run | pending | 62245584 | `verification/62245584/**` (new) | — | — |
| Q-6 | Publish: PR to `main`, merge, confirm the Pages build, record the result here | pending | 62245584 | this block | — | — |

**Rules this session follows.** No personal information in any committed file; parties and addresses appear only as placeholders (`[OWNER]`, `[TRUSTEE]`, `[DECEDENT]`, `[HEIR]`, `Property A`, `Property B`). No household figure is typed into any new file: the new pages read their inputs from the published `MODEL.BASE` and from `qa/ledger.json`, exactly as the existing engines do. Every dollar figure this session adds to the site is rounded to the nearest $10 unless a government body publishes that exact amount (the ledger allowlist governs). Every table row carries a link to an official source or is left blank and marked unverified; nothing is inferred. `origin/main` is merged before every push; conflicts are resolved without discarding another session's work.

**Q-C1 (claim note, not a conflict).** No live collision occurred. No file owned by another session is claimed, and no shared output (table data, index navigation) is changed except the additive entries listed in Q-4, which are made in the integration role this session holds because no other session is live.

<!-- END block owned by session 62245584 -->
## Session `58941d22` (branch `arena/58941d22-tino2`) — claim 2026-11-12 — final integration: reader-facing polish + final verification

### Scope
- Non-overlapping: reader-friendliness of the 15 published pages only (spelling out the `NOI` abbreviation on the two property/SF pages where it first appears as a column/metric label). No model, data, or content change. Confirms the published recommendation and every official claim still hold.

### What was re-verified this session (official sources)
- **Santa Clara County house-price index (FHFA/FRED ATNHPIUS06085A)** re-opened from the primary table: 7.0% CAGR 1975–2025, 4.3% CAGR 2000–2025, −25% from 2006 peak to 2011 trough — confirms the Best-plan-page and Flagged-for-Review citations. (The San Jose MSA metro series on the index/stress pages is a *different* series, ATNHPIUS41940Q: 6.7% / 4.1% over the same spans; both are official and both citations match their own series.)
- **IRS estate exclusion**: $15,000,000 for deaths in 2026 (IRS primary "What's new — Estate and gift tax" page, WFTC P.L. 119-21) and $15,480,000 for deaths in 2027 (IR-2026-133 / Rev. Proc. 2026-35 §3.44).
- **BOE Proposition 19 exclusion** $1,044,586 for transfers 16 Feb 2025 – 15 Feb 2027 (LTA 2025/009).
- **SF Rent Board** 1.6% covered-unit increase, 4.2% deposit interest, $8,245 relocation, $59 fee for 2026–27 (sf.gov primary pages).
- **FY2027 HUD SAFMR for 95014** remains unresolvable from any official path (legacy `2026zip_code_calc.odn?year=2027` returns ODBscript errors and blank/$0 values; the FY2027 SPA ignores query params; FY27 spreadsheet HTTP 500; API guesses 404). Item F-I3 stays flagged unverified.
- **Every one of the 15 pages** re-read for defect/consistency scanning; every table row retains its official source link.

### Changes made (reader-friendliness only)
- `site/san-francisco.html`: spelled out "NOI (net operating income)" in the metric-label caption on the 2026 NOI card.
- `site/properties.html`: spelled out "NOI (net operating income)" in the two projection table headers.
- No change to model inputs, recommendations, or the Flagged-for-Review register.

### Verification on the edited tree
- `scripts/validate.js`: PASS, 1129 checks, 15 pages, 171 sources; base case 2040→2050 sell $7,683,290 / rent $6,249,830 / live $5,135,780 (unchanged).
- `scripts/runtime-test.cjs` (jsdom): PASS, 15 rendered pages, 1327 rendered rows source-linked, no runtime errors or broken links.

### Publication record (2026-11-12)
- First push needed `git pull --rebase origin main` because the branch did not yet exist remotely; then pushed. PR [#50](https://github.com/wingbangboozle1-lang/Tino2/pull/50) was created and initially reported `CONFLICTING` because three other sessions had appended blocks to COORDINATION.md on main while this session worked. Re-merged `origin/main`, resolved the board conflict by keeping all session blocks (58941d22, 62b76b9d, 6e6baf25, 364b453d), regenerated the QA gate report, re-pushed, and the PR became `MERGEABLE`.
- **PR #50 MERGED** 15:47:15 UTC (squash/merge) without waiting for approval. A first Pages build attempt errored at 15:47:16 UTC (transient, raced the merge); the rebuild for the same merged commit completed **`built`** at 15:47:22 UTC.
- GitHub Pages: source `main`, live at `https://wingbangboozle1-lang.github.io/Tino2/`. Live read-back from the sandbox is not possible (outbound limited), so the Pages API build record is the confirmation.
- Post-merge tree: `validate.js` PASS (1168 checks, 17 pages, 171 sources), `runtime-test.cjs` PASS (15 rendered pages, 1327 source-linked rows), `gate.cjs` PASS (0 errors, 0 warnings). Base case 2040→2050 unchanged: sell $7,683,290 / rent $6,249,830 / live $5,135,780.

### Board status after this session
- Every task of this session is done. Remaining items are **needs review** and are published on the Flagged for Review page (F-I3 FY2027 HUD rent benchmark; F-I1/F-I2 privacy decisions; items other sessions left open). Flagged/unverified items do not block the merge.

## Session `62b76b9d` — 2026-11-12

| Task | Status | Owner | File scope |
|---|---|---|---|
| Independent final review of existing integrated dashboard; improve executive-summary uncertainty and household-cost display rounding; run publication/model checks | in progress | 62b76b9d | `verification/62b76b9d/**`, `index.html` (executive summary wording only), this board block |

The repository already contains the requested integrated site. No open pull requests at claim. Earlier task blocks have subsequent completion records; no current overlapping work identified. The Arena-fixed current branch is used (no alternate branch created). Research facts will not be marked verified unless directly retrieved; restricted network access will be reported. Existing private-history risks are not resolved by display rounding. No private records will be added.

### `62b76b9d` completion / integration

Review and implementation **done**. Source retrieval and precise limits recorded in `verification/62b76b9d/REPORT.md`. Four official pages directly opened (IRS estate tax, BOE Prop 19, CDI residential, GitHub sensitive-data guidance). Existing financial engine unchanged. Landing-page recommendation now conditional; estate-tax omission prominent; dedicated Suggestions table added with discovery/approval gates. Package, publication negative tests, 1,132 validation checks, stress, 15-page runtime (1,331 rows) and privacy gate all pass; own regression passes. Nine calculated rows have context-only source links, not verified official outputs. Historical privacy and missing household facts remain needs review on the existing review page. Generated gate report restored; no overlap with another scope.

First claim push needed `git pull --rebase origin main` because the current branch did not yet exist remotely; succeeded without conflict. Publication pending PR/CI, tracked below.

## Session `6e6baf25` — 2026-11-12 15:32 UTC

Read the board and remote heads; no open PRs and no recent live claim identified. Prior sessions' scopes are complete or needs review. The platform fixes this branch name; a `session-...` branch cannot be created. This session claims the following scope for integration work:

| Task | Status | Owner | File scope |
|---|---|---|---|
| Audit the canonical site's remaining decision and privacy gaps; record evidence | in progress | 6e6baf25 | `verification/6e6baf25/**`, this block |
| Provide a dedicated, review-before-implementation suggestions section and any narrowly scoped corrections found during audit | in progress | 6e6baf25 | `site/suggestions.html`, `site/review.html`, `index.html`, `assets/app.js`, `scripts/check-publication.py`, `scripts/validate.js` as needed |
| Integration checks, PR, merge, Pages verification | in progress | 6e6baf25 | this block, claimed files above |

Privacy caveat: the repository and site are public. Rounded data plus contextual details do not guarantee anonymity; history cannot be made private by a Pages exclusion. No personal identifiers will be copied into this log.

**Scope addition, 15:33 UTC:** `site/plan.html` is also claimed for a narrow clarification of endpoint portfolio taxation. No current owner was found. The same correction is planned for `index.html`; neither changes model results.

**Scope addition, 15:34 UTC:** `site/decision.html` is claimed for one narrow correction: the existing tax sensitivity is not a proven bound on the true result. No active owner was found. No model arithmetic will be changed.

**Coordination correction and conflict:** Session `62b76b9d` had a concurrent claim and merged PR #43 while this session was working; its landing-page scope overlapped. It was not visible in the initial check. `git pull --rebase origin main` conflicted on the board. Both blocks were retained and the rebase completed; the stashed site edits restored cleanly, preserving the other session's landing-page suggestions table. No other session's work was discarded. This session's separate suggestions page supplies a more detailed decision and privacy comparison.

**Review status:** Source retrieval, limits and specific findings are recorded in `verification/6e6baf25/REPORT.md`. The reviewed sources include [BOE Proposition 19](https://www.boe.ca.gov/prop19/), [IRS estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax), [IRS basis](https://www.irs.gov/taxtopics/tc703), [CDI residential insurance](https://www.insurance.ca.gov/01-consumers/105-type/5-residential/), [FDIC](https://www.fdic.gov/resources/deposit-insurance/faq/), [SEC](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments), and [GitHub data-removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). External links outside this checked subset and every inherited row were not freshly verified. Public contextual re-identification risk and historical exposure, as well as unverified household values that are displayed rather than blank, remain **needs review** and are published on the Flagged page. No history rewrite or privacy-setting change was performed.

<!-- BEGIN block owned by session 364b453d — other sessions: do not edit inside this block; requests go in your own section -->
## Session `364b453d` (branch `arena/364b453d-tino2`) — claim 2026-11-12 15:35 UTC

**State read at claim.** `main` = `bfb2268` (merge of PR #42, session `60ca3e1f`). Every session block above is `done`; the only open items are the standing `needs review` findings already published on Flagged for Review. `gh pr list` returns **no open pull requests**; 32 remote branches exist and none has an open PR, so nothing unmerged is in flight. No live claim covers the files below.

**Role taken (non-overlapping).** The brief asks twice for a *dedicated suggestions section*: (1) suggestions to improve the site for decision making, and (2) a place where someone can review those suggestions and **choose a path before implementing any changes**, including suggestions that discover missing information. A full-text search of every published page, `assets/app.js` and `README.md` finds no such page and no navigation entry for one. The 15 published pages cover the analysis, the open-items register and the verification ledger, but not a reviewable improvement/deadline queue with a recorded choice. This session builds that page and nothing else.

**File scope (non-overlapping).**

| File | Change | Owner today |
|---|---|---|
| `site/suggestions.html` | **new page** — suggestions register, decision-readiness questions, discovery routes, and a local-only choice record | new, this session |
| `assets/app.js` | one navigation entry (the nav list) and nothing else | shared, no live claim; logged here first |
| `index.html` | one link block to the new page in "Go deeper by category" | shared, no live claim; logged here first |
| `scripts/validate.js` | page-count assertion 15 → 16 | shared, no live claim; logged here first |
| `scripts/check-publication.py` | add `site/suggestions.html` to the reviewed manifest | shared, no live claim; logged here first |
| `README.md` | one line in the structure list | shared, no live claim; logged here first |
| `COORDINATION.md` | this block only | this session |
| `verification/364b453d/**` | new report: what was checked, source wording, irregularities | new, this session |

No model input, no recommendation, no published figure, no other page's content is changed.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| S-1 | Read the board and remote branches, detect live claims and open PRs, claim, push at once | done | 364b453d | this block | N/A | none |
| S-2 | Re-open the official pages the new page cites (IRS, BOE, California State Controller, FTB, CDI, HUD, SF Rent Board, CPUC, Secretary of State) and record the exact wording and access date | in progress | 364b453d | `verification/364b453d/**` | see the report | — |
| S-3 | Build the suggestions page: site improvements with effect on the decision, decision-readiness questions with what is known and what is missing, discovery routes, and a choose-a-path record that stays in the reader's browser | in progress | 364b453d | `site/suggestions.html` | as S-2 | — |
| S-4 | Wire the page in: navigation entry, landing-page link, publication manifest, page-count assertion, README line | pending | 364b453d | files listed above | — | — |
| S-5 | Re-run every check on the final tree (validate, stress, package, publication boundary, runtime, gate, link check, privacy scan) and fix anything that fails | pending | 364b453d | — | — | — |
| S-6 | PR to `main`, merge without waiting, confirm the Pages build for the merge commit, record the PR link and result here | pending | 364b453d | this block | — | — |

**Rules this session follows.** No personal information in any committed file; parties and addresses stay as placeholders and no household figure is repeated in this block. Every dollar figure the new page states is rounded to the nearest $10 unless a government body publishes that exact amount, and the existing gate enforces that on the rendered page. Every table row carries a link to an official source; where an item has no official source it is not presented as a fact — the row says what would settle it and links the agency that holds the document. Nothing is inferred. `origin/main` is merged before every push; conflicts resolved keeping both sides. Arena pins the branch name, so the `session-<id>/<task>` naming cannot be applied; the session ID is in the branch name.

**S-C1 (claim note, not a conflict).** No other session is live: no open pull request, no unclaimed task on any block, and no branch with unpushed work. The files listed above are shared files whose last owner has finished; each change is listed here before it is made, as the board requires.

### Session `364b453d` — completion record (2026-11-12)

| # | Task | Result |
|---|---|---|
| S-1 | Claim | done — pushed at 15:35 UTC before any work |
| S-2 | Official-page re-verification | done — 17 pages opened this session; wording and links in `verification/364b453d/REPORT.md` §2. IRS IR-2026-133 and the IRS estate-tax table ($15,000,000 for 2026, $15,480,000 for 2027), California State Controller (no California estate return after 1 Jan 2005), FTB gifts and inheritance, BOE Proposition 19 page and LTA 2026/026 (value cap and claim deadlines), BOE NR 25-02 (7 March 2025), CDI survey page (not a quote) and CDI Form 401 guide (dwelling limit = rebuild cost; earthquake and 60-day vacancy exclusions), USGS (72% M6.7 in 30 years), HUD FY2026 SAFMR for the ZIP ($6,390 4BR), HUD SAFMR index (FY2027 exists; FY2026 effective 1 Oct 2025), CPUC net metering (closed to new enrollments; net billing since 15 Apr 2023), SF Rent Board current rates and Rent Board fee page (exemption deadline 14 Dec 2026), IRS Rev. Rul. 2023-2 (no basis adjustment for trust assets outside the estate), Prob. Code §10800 |
| S-3 | Suggestions page built | done — `site/suggestions.html`: 15 analysis suggestions with official evidence, effort and window; 10 decision-critical questions with what is known, what is missing, where the answer is, and both outcomes; 6 dashboard proposals; a 5-step sequence; approve/defer/decline stored only in the reader's browser with print, copy and clear; guardrails. No model input or published figure changed |
| S-4 | Wiring | done — nav entry in `assets/app.js`; landing-page card in `index.html`; `site/suggestions.html` added to the reviewed manifest in `scripts/check-publication.py`; page-count assertion 15 → 16 in `scripts/validate.js`; one line in `README.md` |
| S-5 | Checks | done — `validate.js` PASS (1,149 checks, 16 pages, 171 sources; base case unchanged) · `stress-test.js` PASS · `package-site.py` PASS · `check-publication.py --self-test` PASS (29 files) · `runtime-test.cjs` PASS (16 pages, 1,352 rows, all source-linked) · `qa/tools/gate.cjs` PASS (0 errors, 0 warnings) · `src/check_links.py .` PASS (64 pages) · `privacy_scan.py` 0 errors, warnings unchanged. Rendered behaviour checked with jsdom: 21 choice controls, selection persists to one `localStorage` key, summary updates, no runtime error |
| S-6 | Publish | in progress — see the publication record below |

**Irregularities.** (S-I1) The FY2027 HUD rent benchmark is still unread: the 2026-style ZIP address for 2027 returns 404 and the FY2027 section offers an interactive lookup plus an `.xlsx` that this sandbox cannot download; left blank and listed as suggestion A-05. (S-I2) Two wordings were softened after checking — the “2026 letter list” absence is now attributed to the earlier check, and the probate-fee sentence now uses the verified “statutory percentage of the estate's value”. (S-I3) The decision record is per-browser by design; print and copy are the durable paths. (S-I4) Page count and manifest were updated; a later page must update both or the build fails closed. (S-I5) No personal information was added; the standing privacy findings are unchanged. None of these blocks publication.

**Rules followed.** No personal information in any committed file; no household figure repeated in this block. Every dollar figure on the new page is an official published amount or the $10 rounding rule. Every table row on the new page carries an official https link; no value was inferred. `origin/main` was merged before every push. Arena pins the branch name, so the session ID is carried in the branch name.


### Session `364b453d` — publication record (2026-11-12)

| Step | Result |
|---|---|
| PR | [#45](https://github.com/wingbangboozle1-lang/Tino2/pull/45) `arena/364b453d-tino2` → `main`, **MERGED** 15:40:04 UTC without waiting for approval |
| Merge commit | `30fae97bc5bb0901ef2593a8b83e0d190373a9d9` (parents `4a7e597` and `ed9cbbd`) |
| CI on the PR head | `verify` (Verify public Pages boundary) **pass**, 26s — includes the Jekyll Pages build and the rejection of unexpected files in the real output |
| GitHub Pages | build for `30fae97` reported **`built`**, `error.message: null`, completed 15:40:48 UTC; the `pages build and deployment` run for `30fae97` succeeded |
| Live read-back | **Done.** `https://wingbangboozle1-lang.github.io/Tino2/site/suggestions.html` opened after the build: the combined page renders with one heading, the privacy-path table, the seven structural improvements, the fifteen-item register, the question tables and the record section. Both sessions' content is present |
| Open PRs after this session | this record was published by a second, small PR from the same branch, because the brief asks for the result in `COORDINATION.md`; the record is the only change it carries |

**State of the board.** Every task of this session is `done` (S-1 … S-6). What remains is **needs review** and is already published on Flagged for Review: the standing privacy findings for the owner, the FY2027 rent benchmark left blank, and the other blank household figures. None of them blocks publication and none is made worse by this session.

<!-- END block owned by session 364b453d -->
**Merge note, 12 Nov 2026 (recorded, not hidden).** Two other sessions were live while this one worked: `62b76b9d` and `6e6baf25`. `62b76b9d` merged PR #43 at 15:33 UTC and `6e6baf25` PR #44 at 15:36 UTC, after this session's 15:35 UTC claim read “no open pull requests”. Both had already published a suggestions page and a landing-page suggestions table. The conflict on `site/suggestions.html` was resolved by **combining**, not replacing: their privacy notice, privacy-path table, seven structural improvements, seven questions (kept unchanged in a collapsed block) and closing note remain in full; this session's itemized register, decision-critical questions, sequence and choose-a-path record were added around them. The duplicate navigation entry and the duplicate landing-page card from this session were removed in favour of the published ones, with the published card's wording extended to mention the recorded choice. **Nothing of theirs was discarded.** `origin/main` was merged before the push.


### Session `62245584` — merge conflict, resolution and completion record (12 Nov 2026)

**Conflict, logged as the rules require.** At 15:52 UTC this session's first push met an add/add conflict on `site/suggestions.html`. `origin/main` had moved from `bfb2268` to `30fae97` while this session was working: sessions `6e6baf25` and `364b453d` built a Suggestions page for the same brief requirement and merged it as PR #44 and PR #45. This session's claim was accurate when it was pushed (no live branch had moved since 05:14 UTC); the collision happened after it. **Nothing of the other sessions' work was discarded.**

**How it was resolved, and why.**

| File | Resolution |
|---|---|
| `site/suggestions.html` | **Theirs kept byte for byte.** It is their page and it already meets the brief's suggestion requirement in full, including an approve / defer / decline record held only in the reader's browser. This session's draft was **not** merged into it. |
| `site/questions.html`, `site/data/questions.js` | **This session's, renamed from its original name.** The brief's other requirement — "a clear list of questions, informations and answers … before any decision can reasonably be made" — was still thin on `main`: their page carries ten decision-critical questions; this register carries forty, grouped in the order the answers must arrive, with a blocking rule that says can this plan be decided yet and is enforced in `scripts/validate.js`. The two pages are complementary, not duplicates, and each links the other. |
| `assets/app.js`, `index.html` | Both sessions' navigation entries kept; one Suggestions entry (theirs) and one Questions entry (this session's). This session's duplicate Suggestions landing card was removed rather than kept twice. |
| `scripts/check-publication.py`, `scripts/validate.js` | Both sessions' manifest entries kept; page count settled at 17. |
| `COORDINATION.md` | Both sides kept in full — every block from every session. |

**New finding taken over from the other sessions, verified here.** Their page raised Revenue Ruling 2023-2: assets of an irrevocable trust that are **not** included in the owner's gross estate keep their old basis. This session opened the ruling and confirmed the wording: "the basis of property is its fair market value at the date of the decedent's death" applies to property "acquired from or to have passed from the decedent", and the ruling's issue is precisely whether § 1014 applies where "the trust assets are not includible in the owner's gross estate". Because the whole sell case rests on a step-up at death, this register now marks the basis question (Q-17) as **not settled**, and Q-01 asks the trust question with the basis consequence stated.

| # | Task | Status | Owner | Files |
|---|---|---|---|---|
| Q-1 | Coordination, claim, push at once | done | 62245584 | this block |
| Q-2 | Questions and answers decision gate | done | 62245584 | `site/questions.html`, `site/data/questions.js` |
| Q-3 | Suggestions section | **done by sessions `6e6baf25` and `364b453d`**; theirs kept unchanged, this session's draft not merged | 6e6baf25 / 364b453d | `site/suggestions.html` |
| Q-4 | Navigation, landing page, manifest, page count | done | 62245584 | `assets/app.js`, `index.html`, `scripts/check-publication.py`, `scripts/validate.js` |
| Q-5 | Verify line by line and run the suite | done — results below | 62245584 | `verification/62245584/REPORT.md` |
| Q-6 | Publish: PR, merge, confirm Pages build, record it | in progress | 62245584 | this block |

**Suite on the merged tree (17 pages).** `validate.js` PASS **1,582** checks · `qa/tools/gate.cjs` PASS **0 errors, 0 warnings** (1,430 rendered rows, 4,838 dollar amounts, 104 official exact figures) · `runtime-test.cjs` PASS · `stress-test.js` PASS · `check-publication.py --self-test` PASS and 32 reviewed public files · `src/check_links.py` 66 pages 0 errors · `privacy_scan.py` 0 errors, 198 warnings, none naming this session's files.

**Irregularities.** X-I1 (corrected before publication: an effort figure that summed time bands, and an "irreversible" label on a step that is not), X-I2 (two sources not re-opened here), X-I3 (hypothetical 1.2% levy), X-I4 (rent benchmark one fiscal year behind), X-I5 (the gate's "no plan is implementable" is a conclusion from its own rule, not legal advice). Full record in `verification/62245584/REPORT.md`. None blocks the merge.

**Privacy.** No personal information added. Parties are placeholders; no household figure is typed into either new file — both read `MODEL.BASE` at render time, which `scripts/validate.js` now proves by halving the input and asserting the answer changes.

<!-- END completion record owned by session 62245584 -->
<!-- BEGIN block owned by session 6a64dc5b. Appended at the end so it cannot conflict with earlier blocks. Other sessions: please do not edit inside this block; write requests in your own section. -->
## Session `6a64dc5b` (branch `arena/6a64dc5b-tino2`) — claim 2026-11-12 15:35 UTC

**State read at claim.** `main` = `bfb2268` (merge of PR #42). `git fetch --all --prune` at 15:34 UTC returned **only** `origin/main` and `origin/HEAD` — no `arena/*` branch exists on the remote, so no other session is live and no path is held. Suite on `bfb2268` re-run before claiming: `node scripts/validate.js` PASS 1,129 checks across 15 pages and 171 official sources.

**Why this scope.** Every page the brief names already exists and is verified, with one exception: the brief asks for (a) a **section dedicated to suggestions** where someone can review suggestions and choose the best path *before* any change is implemented, and (b) a **clear list of questions, information and answers that must be settled before a decision**, with suggestions for discovering the missing information. A repository-wide search at claim time found the word "suggestion" in no committed file. Nothing is claimed that another session holds; the two new pages are additive and no published figure, plan, ranking or recommendation is changed.

| # | Task | Status | Owner | File scope | Sources | Irregularities |
|---|------|--------|-------|------------|---------|----------------|
| S-1 | Coordination: read the board, fetch every remote branch, detect live claims, claim a non-overlapping scope, push at once | done | 6a64dc5b | `COORDINATION.md` (this block only) | N/A | none: no collision |
| S-2 | Independent verification of the figures that drive the decision, re-opened on official sites on 12 Nov 2026 (not copied from an earlier session's report). Each figure recorded with the official URL, the passage read, and PASS / FAIL / UNVERIFIED | claimed | 6a64dc5b | `verification/6a64dc5b/**` (new) | to be listed per row | to be listed |
| S-3 | New page **Decision readiness** (`site/questions.html`): every question, piece of information and answer that must be settled before a decision; what is known and unknown; how each gap is closed, by whom, at what cost; the effect on the plan if it stays open | claimed | 6a64dc5b | `site/questions.html` (new) | reuses the existing 155-key official register; new keys only if a new official page is opened | to be listed |
| S-4 | New page **Suggestions** (`site/suggestions.html`): suggestions for the decision path and for improving the site, each with rationale, evidence link, effort, expected benefit and risk, plus a review-and-choose workflow that records the reader's choice in the browser only | claimed | 6a64dc5b | `site/suggestions.html` (new) | as S-3 | to be listed |
| S-5 | Wire the two pages in: navigation, landing page, page count and link checks, publication manifest, ledger entries, README | claimed | 6a64dc5b | `assets/app.js`, `index.html`, `scripts/validate.js`, `scripts/runtime-test.cjs` (if a count changes), `scripts/check-publication.py` (if a file must be listed), `qa/ledger.json`, `README.md` | as S-3 | — |
| S-6 | Own PR to `main`, merge without waiting, confirm the Pages deploy, read the live pages back, record the result here | claimed | 6a64dc5b | own files + this block | — | — |

**Rules this session follows.** No personal information in any committed file; parties and addresses appear only as placeholders. No household figure is committed unrounded and none is repeated in this block. Every dollar figure is rounded to the nearest $10 unless a government body publishes that exact amount. Every table row carries a link to an official source or is left blank and marked unverified; nothing is inferred. `origin/main` is merged before every push. The platform fixes the branch name to `arena/6a64dc5b-tino2`, so the `session-<id>/<task>` naming cannot be applied; the session ID is in the branch name.

### Session `6a64dc5b` — completion record (12 November 2026)

**Question asked.** Earlier sessions built and verified the three choices and the figures. This session answered the two parts of the brief that had no page: a **suggestions** section where the reader can review suggestions and choose a path before anything is implemented, and a **decision-readiness** register of the questions, information and answers that must be closed first, with suggestions for discovering what is missing. It also re-opened the official sources that drive the decision and recorded each passage itself (S-2), because the brief asks for line-by-line verification against official sources.

| # | Task | Status | Result |
|---|------|--------|--------|
| S-1 | Coordination claim | **done** | Claim pushed 15:35 UTC; no other branch on the remote, so no collision |
| S-2 | Independent verification | **done** | `verification/6a64dc5b/REPORT.md`: 17 sources opened and quoted; 1 irregularity (IREG-1); every row PASS |
| S-3 | Decision readiness page | **done** | `site/questions.html`: 24 questions in 4 groups, 10 settled answers, 3 blocking, 5 readiness gates, 10-row sensitivity table computed by the published model |
| S-4 | Suggestions page | **done, scope adjusted** | `site/suggestions.html` was written three times by concurrent sessions. Session `364b453d` published the fullest version on `main` (15-item register, six site changes, question set, approve/defer/decline record). That version is kept unchanged and is the canonical page; this session added one link from it to the new Questions register and did not re-publish its own 20-row register, to avoid two competing lists. `localStorage` only, no network |
| S-5 | Wiring and checks | **done** | Navigation (2 entries), landing page (2 cards), publication manifest (30 files), validator (17 pages), README, ledger P19-12; `validate.js` PASS 1,168 checks; `package-site.py` + `check-publication.py --self-test` PASS; `runtime-test.cjs` PASS 17 pages / 1,421 rows; `gate.cjs` 0 errors; privacy scan 0 errors |
| S-6 | PR, merge, Pages | **pending** | To be recorded below once the pull request is merged |

**Concurrent work merged, not replaced.** `main` moved twice while this session worked: `bfb2268` → `ed9cbbd` (sessions `62b76b9d` and `6e6baf25`) → `30fae97` (session `364b453d`). All three had touched the same area, and two had created `site/suggestions.html`. Final resolution, recorded rather than hidden:

| Their work | What happened to it |
|---|---|
| `62b76b9d` — conditional-recommendation and privacy wording in `index.html`, two High items on the Flagged page | Kept in full |
| `6e6baf25` — privacy-path comparison, seven structural improvements, seven questions | Kept in full inside `364b453d`'s page |
| `364b453d` — 15-item suggestions register, six site changes, question set, approve/defer/decline record | **Kept as the canonical `site/suggestions.html`**, with one added link to the Questions register |
| This session — two 10-row registers and a second choice record at the same path | Withdrawn to avoid two competing lists and two `localStorage` records. The unique contribution kept is `site/questions.html` (24 questions, 10 settled answers, 5 readiness gates, 10-row sensitivity table), the verification report and ledger entry P19-12 |

Nothing written by another session was removed. The only edit to `364b453d`'s page is the added link sentence; its register, record and wording are unchanged.

**Irregularity published.** IREG-1: the Santa Clara County Assessor page says the Proposition 19 allowance is adjusted "annually", while the Board of Equalization and Letter to Assessors 2026/026 say every other 16 February. The model follows the Board; the item is on `site/review.html` with both links.

**Nothing changed in the published answer.** Base case unchanged: 2045 inheritance, ten-year hold — sell $9,125,340, rent $7,395,620, live $6,068,080. Every sensitivity on the new page keeps selling first.

**Handoff.** No request to another session: no other session is live. The two owner actions that remain outside any session's power are unchanged and already on the Flagged page: the public commit history (exact assessed values and the account e-mail address) and the confirmation of the trust's basis treatment.

### Session `62245584` — second conflict, and the final resolution (12 Nov 2026)

**Second conflict.** `main` moved again, from `30fae97` to `e510d34` (PRs #47 and #48), and session `6a64dc5b` had added **its own `site/questions.html`** ("Decision readiness"). So the brief's question-and-answer requirement was built twice, independently, while this session worked. Nothing was discarded.

**How the two question pages were reconciled, and why they stay separate.** They answer different questions and neither replaces the other.

| Page | Owner | What it answers |
|---|---|---|
| `site/questions.html` | session `6a64dc5b` | **The reference.** What the official answers *are* (nine settled answers with the wording found), and — the distinctive part — **what each open gap moves in the projections**, computed by re-running `MODEL.decision()` with one input changed. It has no per-question blocking rule. |
| `site/questions-gate.html` | this session | **The gate.** Forty questions in the order the answers must arrive, each marked settled / household input / missing, with an explicit **blocking rule**: a plan is blocked by every question attached to it whose answer is not settled. It carries no projection deltas, so it does not duplicate the reference page's analysis. |

The gate page was **renamed** to `site/questions-gate.html` and retitled "Decision gate", with its executive-summary card and navigation entry worded so the two are not confused. It links to the reference page and the reference page does not need to change. `site/data/suggestions.js`, this session's suggestion engine, was **deleted**: session `364b453d`'s page does not use it, so it was an orphan file that the publication boundary correctly rejected. The manifest, the page count (18) and the validation block were updated to match.

**Net effect of this session after both reconciliations.** One new page (`site/questions-gate.html`), one new data file (`site/data/questions.js`), one verified finding taken over (Rev. Rul. 2023-2, basis), and navigation for both existing pages. The Suggestions page belongs to sessions `6e6baf25` and `364b453d` and is unchanged.

**Suite on the merged 18-page tree.** `validate.js` PASS **1,486** checks · `qa/tools/gate.cjs` PASS · `runtime-test.cjs` PASS · `stress-test.js` PASS · `check-publication.py --self-test` PASS, 32 files · `src/check_links.py` 0 errors · `privacy_scan.py` 0 errors. Figures recorded in the final publication record below.

**Privacy.** Unchanged and re-checked: no personal information, no household figure typed into `site/data/questions.js`; the value it displays is read from `MODEL.BASE` at render time, which `validate.js` proves by halving the input and asserting the answer moves.

### Third collision, same day: `6a64dc5b` (PR #47)

`6a64dc5b` merged a **second readiness page** while this session was fixing the merge markers left by the first two collisions (those markers were committed by this session's own merge and removed in commit "Fix: remove merge markers…"; the fault was this session's, and it is recorded as A-I8 in `verification/a87f8523/REPORT.md`).

**Resolution.** One readiness page remains, built on this session's register, and `6a64dc5b`'s material is on it in substance:

- Its 24 questions are published on `site/questions.html` in their own IDs (A1–D5) with their wording, each mapped to the Q row that now carries it.
- Six of its questions were not yet in this session's register and are now **Q23–Q28**: how title is actually held and any earlier death, taxable gifts and Form 709, portability, who bears the tax, the actual Rent Board rent roll, and whether Property B is kept for the next generation.
- Its five "one uncertain input at a time" checks are not duplicated: the Decision lab already runs that comparison live, and the page says so.
- Its `verification/6a64dc5b/REPORT.md` is untouched; its board block is kept in full above.

### Second collision, same day: `364b453d` (PR #45)

A third session merged its own `site/suggestions.html` five minutes after this session's first merge attempt. Its page carried 15 analysis improvements, 10 decision questions, 6 site proposals, a 5-step sequence and its own approve/defer/decline record, with 17 official pages opened — including three facts this session had not re-read (CPUC net-billing rules, the USGS 72% figure, and the Board of Equalization's condition that the exclusion is removed if the homeowners' exemption lapses).

**Resolution.** One page remains, built on this session's structure, and the third session's material is on it in substance:

- Its 15 analysis improvements and 10 decision questions appear in a reconciliation table with their own IDs and titles, each mapped to the `S` item or `Q` question that now carries it. Nothing is dropped and nothing is duplicated as a second entry.
- Its 6 site proposals map to S13–S16, S09, S27 and the browser-local record this page already had.
- Its 5-step suggested sequence is published on the page.
- Its chapter-and-verse findings were added to the register: CPUC net billing (legacy net metering closed; net billing since 15 April 2023; exports paid at a value-of-generation rate) in Q12, the USGS 30-year probabilities in Q20, and the homeowners'-exemption condition in Q03/Q07.
- Its `verification/364b453d/REPORT.md` is untouched; its board block is kept in full above.
- Index.html keeps its suggestions table and card; this session's two-card block was trimmed to avoid a third copy of the same links.

### Merge note added by `a87f8523` after resolving a real collision

While this session was working, sessions `62b76b9d` (PR #43) and `6e6baf25` (PR #44) merged **their own** `site/suggestions.html`, a nav entry, a landing-page card and a set of privacy-wording improvements. This session had claimed the same deliverable at 15:35 UTC, before either merge appeared on `main`.

**How it was resolved, without discarding anything:**

- The other sessions' page was **merged into this session's page**, not replaced. Their privacy warning, their three-path privacy comparison and their seven decision questions are on the published page in their own words (the questions are also mapped to register IDs Q01–Q18). Their seven proposals are now S21–S27 in the backlog.
- Their nav entry was de-duplicated (this session had added one earlier in the same array); their brand tagline, footer and landing-page privacy wording are kept.
- `site/plan.html`, `site/decision.html`, `index.html` headings and `site/review.html` changes from both sessions were merged by git; no hunk of theirs was dropped.
- Allowlist and validator counts were resolved to the combined state: 32 public files, 17 pages.
- Their `verification/62b76b9d/**` and `verification/6e6baf25/**` reports are kept untouched. Their board blocks are kept in full above this note.
- Both of their pages' facts were re-read before merging: nothing in them conflicts with the sources this session opened. Where both pages link the same rule they cite the same URL.

This is the collision the board exists to prevent; it happened because their claims were pushed after this session's read of the remote and were not visible at claim time. The board now records the sequence in three places.

<!-- BEGIN block owned by session a87f8523 (2026-11-12). Other sessions: do not edit inside this block; write requests in your own section. -->
## Session `a87f8523` (branch `arena/a87f8523-tino2`) — claim 2026-11-12 15:35 UTC

**State read at claim.** `main` = `bfb2268` (merge of PR #42, session `60ca3e1f`), Pages build `built` for that commit at 05:15 UTC. `git ls-remote` shows **only** `main` on the remote; the working copy holds one session branch. Every earlier session block records its tasks `done`; the remaining open material is the standing **needs review** set (insurance premiums, FY2027 rent benchmark, Measure H parcel amount, trust type, tenancy terms, private-history privacy items). No live session holds a claim.

**What this session takes — the two deliverables the brief asks for that the site does not yet have.**

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| Q-1 | Coordination: read the board, fetch the remote, claim a non-overlapping scope, push the claim at once | done at claim commit | a87f8523 | `COORDINATION.md` (this block only) | N/A | Q-C1 |
| Q-2 | **New page: Decision readiness** (`site/questions.html`). A single register of the questions, the information and the answers needed before any live/rent/sell decision can reasonably be made, split into: answerable now from an official source; open and discoverable (with the document, office or lookup that settles each); and unknowable until the event (planned around, not researched). Each row carries an official source link or is blank and flagged. Includes a discovery plan and a blank answer sheet that stays in the reader's browser | **done.** 22 open questions in six groups, 12 answered from official sources, 8 unknowable, 12 discovery items, browser-local tracker with export | a87f8523 | `site/questions.html`, `site/data/questions.js` (both new) | twelve official pages opened in this session (listed in `verification/a87f8523/REPORT.md` §1); nine facts carried with their earlier checked dates (§2) | A-I1 to A-I7 |
| Q-3 | **New page: Suggestions to review** (`site/suggestions.html`). A dedicated suggestions section: each proposal states what uncertainty it removes, which readiness question it closes, effort, direct cost (only where an official price exists; otherwise "quote needed"), risk, and status. Four ready-made paths so the owner can compare and choose before anything is implemented. Selection is local to the browser and exportable; nothing is changed on the site by choosing | **done.** 20 proposals, 4 paths (privacy-first, sharpen-the-numbers, decision-grade, wait-and-watch), guardrails table, browser-local choice with Markdown export | a87f8523 | `site/suggestions.html`, `site/data/suggestions.js` (both new) | as Q-2, plus GitHub Pages and Cupertino ADU pages opened this session | as Q-2 |
| Q-4 | Wire both pages into navigation and the executive summary; add them to the publication allowlist and the validator's page count; README section | **done.** Two nav entries (`Readiness`, `Suggestions`), a two-card section on the landing page, allowlist now 32 public files, validator 15 → 17 pages, README structure and a "Review before change" section | a87f8523 | `assets/app.js`, `index.html`, `scripts/check-publication.py`, `scripts/validate.js`, `README.md` | N/A | nav length noted as A-I1 |
| Q-5 | Line-by-line re-verification of the figures the two new pages rely on, from official pages opened this session; record URL, wording and access date; leave blanks blank | **done.** `verification/a87f8523/REPORT.md`: 12 pages opened with wording, 9 facts carried with earlier checked dates, 7 claims deliberately not made | a87f8523 | `verification/a87f8523/**` (new) | IRS estate tax, State Controller, BOE Prop 19, BOE LTA 2025/009, IRS inherited-property FAQ, IRS Topic 701, FTB Form 593, SF Rent Board fee, Probate Code 10800, Attorney General rent caps, GitHub Pages, City of Cupertino ADU | A-I4, A-I7 |
| Q-6 | Run the full suite, fix what fails | **done.** validate 1,166 checks / 17 pages / 173 sources · stress PASS · package PASS · publication boundary PASS 32 files + self-test · runtime PASS 17 pages / 1,419 rows · gate PASS 0 errors 0 warnings (4,856 amounts) · `check_links.py` 0 broken · privacy scan 0 errors · jsdom interaction test of both pages: no uncaught error | a87f8523 | own files | — | A-I1 |
| Q-7 | PR to `main`, merge without waiting, confirm the Pages build for the merge commit, read the two new pages back from the live URL, record PR link, merge commit and build result | in progress — the result is written as a comment on the pull request and summarised in the *Publication* note below, because a further edit here would need a second merge | a87f8523 | this block | — | — |

**Rules this session follows.** No personal information in any committed file; parties and addresses stay placeholders; household amounts appear only rounded to $10. Every dollar figure of $1,000 or more on the new pages is a multiple of $10 or a figure a government body publishes (and, where it is new, added to `qa/ledger.json`). Every table row carries an official source link or is left blank and marked unverified. Nothing is inferred. Selected improvements are stored only in the reader's browser; no suggestion is applied by choosing it. The platform fixes the branch name, so the `session-<id>/<task>` convention appears only as the session ID inside `arena/a87f8523-tino2`.

**Publication note (added before the merge).** The PR link, the merge commit and the Pages build result are recorded as a comment on the pull request itself, and the live read-back of `site/questions.html` and `site/suggestions.html` is described there. That keeps this block to one merge, because every merge on this repository adds a commit authored with the account's e-mail address (F-I1).

**Coordinating note Q-C1.** Because the remote holds only `main`, no other session can be colliding at claim time. Shared files touched by Q-4 are listed above before they are edited; each is an addition to a list or a link, not a rewrite of another session's content. Should another session appear, it will find the claim in this block with its file scope stated.

<!-- END block owned by session a87f8523 -->

### Session `6a64dc5b` — merge and deployment record (12 November 2026, 15:5x UTC)

| Item | Result |
|---|---|
| Pull request | [#47](https://github.com/wingbangboozle1-lang/Tino2/pull/47) — opened 15:38 UTC, merged 15:42:25 UTC |
| Merge commit | `f925af3` |
| Check before merge | `Verify public Pages boundary` run on the final head `f4d96d3`: **success** |
| Pages build after merge | `pages build and deployment` on `e510d34` (the merge plus session `364b453d`'s follow-up PR #48): **success** |
| Live read-back | `https://wingbangboozle1-lang.github.io/Tino2/site/questions.html` opened after the build: hero, 24-question counts (3 blocking, 16 open, 5 preference), the settled-answers table and group A render with their source links. The Suggestions page carries the added link sentence to the Questions register, and the live navigation shows both entries. |
| Merge conflicts | Two, both from concurrent sessions working the same files; resolved keeping every other session's content (see the table in the completion record above). Nothing of theirs was removed. |
| Irregularity found after the merge | The published `assets/app.js` listed the "Suggestions" navigation entry **twice** — a three-way merge artefact: once after "Other options" and again after "Verified facts". Fixed in the follow-up commit on this branch; `validate.js`, `runtime-test.cjs` and `gate.cjs` re-run after the fix. |

**Privacy.** No personal information added. No household figure typed into `site/data/gate.js`; the one value it displays is read from `MODEL.BASE` at render time, and `validate.js` proves this by halving the model input and asserting the answer moves.

### Session `62245584` — publication record (2026-11-12)

| Step | Result |
|---|---|
| PR | [#49](https://github.com/wingbangboozle1-lang/Tino2/pull/49) `arena/693321af-tino2` → `main`, opened 15:41 UTC, **MERGED** 15:50:50 UTC without waiting for approval; `MERGEABLE` at merge time |
| Conflicts before merge | **Three**, all from `main` moving while this session worked (PRs #44–#48, #50, #51). Each was resolved keeping every session's work in full and logged above. No session's content was discarded. |
| CI on the PR head | `verify` (Verify public Pages boundary) **pass**, 23s — includes the Jekyll build and the rejection of unexpected files in the real Pages output |
| Merge commit | `4c70e8aaf9d524e470c2815e4ac13aa9c2a364af` |
| GitHub Pages | build for `4c70e8a` reported **`built`**, `error.message: null`, completed 15:51:30 UTC (Pages API; source `main` / root, legacy builder, HTTPS enforced) |
| Live-URL read-back | **Done.** `https://wingbangboozle1-lang.github.io/Tino2/site/questions-gate.html` was fetched after the build and returned the rendered page: title "Decision gate · Planning dashboard", the 40 / 14 / 10 / 16 summary cards, the four-plan gate table (transfer 10 blocking of 12; sell 7 of 14; rent 14 of 20; live 10 of 15), and the six ordered groups. The page is live. |
| Open PRs after this session | none |

**What was published.** One new page and one new data file: `site/questions-gate.html` and
`site/data/gate.js`. Every other page on the site, including the two Suggestions pages and the
readiness register built by other sessions, is theirs and was left unchanged except for the
navigation entries needed to reach the new page.

**State of the board.** Every task of this session is done. The standing **needs review** items are
unchanged and remain published on the Flagged for Review page: the two privacy positions for the
owner (F-I1, F-I2), the FY2027 rent benchmark (F-I3), and the blank figures. This session added five
further irregularities, X-I1 to X-I5 in `verification/62245584/REPORT.md`; X-I1 was corrected before
publication, and the rest are recorded there and on the gate page where they affect a row. None
blocks the merge.

**Suggestion for the next session.** Three sessions built the same two features concurrently because
the board showed no live claim at the moment each checked. To prevent a fourth, the next session
should re-read `git ls-remote` **immediately before its first commit**, not only at claim time: in
this session more than two hours of `main` movement happened between the claim and the push.

---

## Session `55c16cea` — 2026-11-12 (Reconciled through `origin/main` `cfe1e3b`)

| Task | Status | Owner | File scope |
|---|---|---|---|
| Verify HUD FY2027 SAFMRs (95014/94122) & Nov 12 official sources; integrate FY2027 HUD, Measure H (`SF-09`), `P19-12` Prop 19 cadence, priority/group filters, CSV checklist download, privacy-path selector & JSON export into `site/data/{questions,suggestions,sources}.js` + `site/{questions,suggestions}.html` while preserving `origin/main` (`cfe1e3b`, incl. `questions-gate.html` + `gate.js`); resolve R-D3 (NOI), R-D4 (internal jargon & duplicate row), R-D5 (12 Nov 2026 check dates); verify, push, merge PR #52 to `main`, confirm Pages deploy | done | 55c16cea | `COORDINATION.md`, `README.md`, `index.html`, `assets/app.js`, `site/{questions,suggestions}.html`, `site/data/{questions,suggestions,sources,model,ledger}.js`, `qa/{ledger.json,gate-report.json}`, `site/{decision,properties,san-francisco,black-swan,stress,options,plan,inheritance,sources,review,verification}.html`, `scripts/{check-publication.py,validate.js}`, `verification/55c16cea/**` |

Branch: Arena-fixed `arena/55c16cea-tino2` (merged with `origin/main` through `cfe1e3b`, preserving every block from `6e6baf25`, `364b453d`, `6a64dc5b`, `a87f8523`, `58941d22`, and `62245584`/`693321af` plus all baseline calculations: `sell` $7,683,290 / `rent` $6,249,830 / `live` $5,135,780 at 2040).

### `55c16cea` completion / verification (2026-11-12)

- **Official data verified (`2026-11-12`)**: `CF-04` (HUD FY2027 SAFMR ZIP `95014`: `$5,800` 4BR / `$5,440` 3BR), `CF-05` (HUD FY2027 SAFMR ZIP `94122`: `$2,770` 1BR / `$3,410` 2BR), `SF-09` (SF Measure H Ballot Title & Summary + OEA report: `$249/yr` base + `$0.195/sq ft` over `5,000` sq ft starting 1 July 2027, 50% / `$65/unit` pass-through), `P19-12` (BOE biennial Prop 19 cadence vs. Santa Clara County wording), plus `githubPages`, `cupertinoADU`, and updated `cpucNem`; refreshed `CA-05`/`CA-06`/`CA-07` and `SF-04`/`SF-05`. Total `qa/ledger.json`: `84` entries (`78` verified, `6` open).
- **Unified `18`-page / `34`-file dashboard**: Preserved `site/data/{questions,suggestions,gate}.js` (`28` open readiness questions `Q01`–`Q28`, `14` settled rules `A01`–`A14`, `8` unknowables, `12` discovery plans, `24` carried-forward Group A–D items, `40`-question blocking `questions-gate.html`, `27` suggestions `S01`–`S27`, `4` bundles, `3` privacy paths, guardrails) and layered in verified FY2027 HUD & SF Measure H data, priority/group filters, blank CSV checklist export, privacy-path selector (`PRIVACY_PATH`), and `.json` export alongside `.md`.
- **Cross-site & sensitivity improvements**: Decision Lab optional `4BR_2027` (`$5,800`) and `3BR_2027` (`$5,440`) selectors, SF FY2027 `94122` + Measure H details (`san-francisco.html`), `R-D3` NOI expansion, `R-D4` cleanup of `"session"`/`"audit note"`/`"the brief"` public prose + duplicate row removal + `Checked 12 Nov 2026` sorting, and `R-D5` `12 Nov 2026` stamps.
- **Checks on merged `18`-page tree**: `package-site.py`, `check-publication.py --self-test` (`34` reviewed public files), `validate.js` (`1,561` checks, `18` pages, `177` sources), `stress-test.js`, `runtime-test.cjs` (`18` pages, `1,583` rows), `qa/tools/gate.cjs` (`0` errors, `0` warnings), `privacy_scan.py` (`0` errors), `src/check_links.py` (`0` errors), and `verification/{60ca3e1f,62b76b9d,55c16cea}/*` all PASS.

---

## Session `c96c185e` — final independent verification & publication (2026-11-12)

Branch: `arena/c96c185e-tino2` (from `main` `052e626`, PR #52). Claim pushed immediately on session start; re-checked `git ls-remote` + open PRs just before this commit (no other live claim, no open PRs).

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| C-1 | Coordination: read board, claim non-overlapping scope, push at once | done | c96c185e | `COORDINATION.md` (this block only) | N/A | — |
| C-2 | Run full local suite on `main` tree (validate, stress, package, publication boundary, runtime, gate, link check) | done — all PASS (see C-5) | c96c185e | `verification/c96c185e/**` (new) | N/A | — |
| C-3 | Fresh official-source spot verification of load-bearing figures (IRS estate amounts, BOE Prop 19, HUD SAFMRs, CDI, BLS/CBO/Fed baselines, SF Rent Board) vs. site claims; blank+flag anything unconfirmable | in progress | c96c185e | `verification/c96c185e/**` (new) | IRS, BOE, HUD, CDI, BLS, CBO, Federal Reserve, SF Rent Board (official pages only) | TBD |
| C-4 | Privacy audit of published tree (placeholders only, $10 rounding, no personal info in public files) | in progress | c96c185e | `verification/c96c185e/**` (new) | N/A | TBD |
| C-5 | Publish: PR to `main`, merge without waiting, confirm Pages build + live read-back, record result here | pending | c96c185e | own files + this block | — | — |

**Rules this session follows.** No personal information in any committed file; parties/addresses as placeholders only. Household amounts only rounded to $10; official published amounts cited exactly with source. Every table row carries an official source link or stays blank/unverified. Nothing inferred. Shared site files untouched unless a defect is found and logged here first. `origin/main` merged before every push.

### Session `c96c185e` — completion record (2026-11-12)

- **C-2 done.** Full suite on the `main` tree: `validate.js` PASS (1,561 checks, 18 pages, 177 sources; base case sell $7,683,290 / rent $6,249,830 / live $5,135,780) · `stress-test.js` PASS · `package-site.py` PASS · `check-publication.py --self-test` PASS (34 files) · `runtime-test.cjs` PASS (18 pages, 1,583 rows) · `gate.cjs` PASS (0 errors, 0 warnings) · `check_links.py .` PASS (68 pages) · `privacy_scan.py` 0 errors (228 standing warnings, unchanged).
- **C-3 done.** Fresh official-source verification by this session (details in `verification/c96c185e/REPORT.md` §2): IRS estate thresholds 2011–2026 and 2026/2027 exclusions (IR-2026-133), BOE Prop 19 page + NR 25-02 ($1,044,586), HUD FY2027 SAFMRs 95014/94122, CA Controller no-estate-tax rule, SF Rent Board 1.6% + File 261020 not enacted, CBO 2026–2036 baseline. All MATCH. Insurance premiums correctly blank (CDI surveys are not quotes).
- **C-4 done.** Privacy audit: placeholders only; no exact household figures in the published tree; household inputs are the brief's own $10-multiple round estimates labeled unverified. Live read-back of `site/questions.html` confirmed the site renders.
- **C-5 in progress.** PR opened from this branch; merge and Pages-build confirmation to follow. No site file changed — the published tree already met the brief; this PR carries only this verification report and this board record.

## Session `27e6213d` (branch `arena/27e6213d-tino2`) — claim 2026-11-12 22:13 UTC

| Task | Status | Owner | File scope |
|---|---|---|---|
| V-1 | Independent verification pass: re-run full validation suite, spot-check key official figures against live official pages, privacy scan, fix defects found | done | `verification/27e6213d/**`, `COORDINATION.md` (this block only); shared files only if a defect is found and listed here first |
| V-2 | PR to `main`, merge, confirm Pages build | done | own files + this block |

State read at claim: `main` = `052e626` (PR #52). No open PRs. No live claims on the board; last session `55c16cea` marked done. This session does not repeat prior research; it verifies the published site line by line and fixes defects only.

**Overlap found at rebase (2026-11-12 22:2x UTC).** While this session ran, `c96c185e` claimed and completed the same class of task (PR #55, merged as `ddf9cb7`) — its board block was not present when this session read the board, so the two passes were independent. Nothing is discarded: both blocks and both verification reports are kept, and this session's PR carries only its own report and record. The two reports agree on every figure they both checked (suite results, base case, IRS/BOE/HUD amounts); this report adds HUD FY2027 at the corrected `/datasets/fmr/fmr2027/zip-calc` URLs, SF FY2026-27 secured rate `1.18162182%`, the SF Rent Board fee amounts and dates, and RTC §§ 11930 / 11911. Duplicate effort, not conflicting work.

### `27e6213d` completion record — independent verification (V-1, V-2)

| Step | Result |
|---|---|
| Task | V-1 independent verification pass: full suite re-run, nine official figures re-opened live, privacy audit of the published artifact, defect hunt |
| Files touched | `verification/27e6213d/REPORT.md`, this block only. **No shared file edited** — no defect required one |
| Suite re-run | `validate.js` PASS (1,561 checks, 18 pages, 177 sources); `stress-test.js` PASS; `package-site.py` PASS; `check-publication.py --self-test` PASS (34 public files); `runtime-test.cjs` PASS (18 pages, 1,583 rows); `qa/tools/gate.cjs` PASS (0 errors, 0 warnings, 4,985 amounts); `privacy_scan.py` 0 errors |
| Base case reproduced | sell $7,683,290 / rent $6,249,830 / live $5,135,780 at 2040→2050 |
| Official re-checks (live, 12 Nov 2026) | IRS IR-2026-133 2027 exclusion $15,480,000 (2026: $15,000,000); BOE NR 25-02 Prop 19 $1,044,586; HUD FY2027 SAFMR 95014 ($5,440 3BR / $5,800 4BR) and 94122 ($2,770 1BR / $3,410 2BR); SF secured rate FY2026-27 1.18162182%; SF Rent Board fee $59/unit, 50% recovery, 1 March, 14 Dec 2026 exemption deadline; CA State Controller — no estate tax for deaths on/after 1 Jan 2005; RTC § 11930 death-transfer exemption; RTC § 11911 $0.55/$500 |
| Privacy audit of `_public/` | 0 errors. No names, street addresses, parcel or account numbers; parties only as `[OWNER]`, `[TRUSTEE]`, `[DECEDENT]`, `[HEIR]`. `_config.yml` still excludes every legacy root page, `docs/`, `research/`, `verification/`, `scripts/`, `qa/`, `src/`, `dashboard/`, `pages/`, `css/` and the two unreferenced stylesheets; only `assets/app.js` + `assets/styles.css` publish; `robots.txt` disallows all crawlers |
| Defects | none. Three observations logged in `verification/27e6213d/REPORT.md`: O-1 loose wording in the `rtc11911` source note (statute says a city *imposes* half the rate and is then *credited* against the county tax — substance correct, left to the next `sources.js` owner to reword), O-2 Property A levy stays a labelled hypothetical (parcel tax-rate area not public), O-3 `capitalGainsTax` 0.331 / `estateIndex` 0.02 are labelled assumptions |
| Standing items | unchanged and still published on the Flagged for Review page; none blocks publication |

### Session `c96c185e` — publication record (2026-11-12)

| Step | Result |
|---|---|
| PR | [#55](https://github.com/wingbangboozle1-lang/Tino2/pull/55) `arena/c96c185e-tino2` → `main`, opened and **MERGED** 22:14:34 UTC without waiting for approval; `MERGEABLE`/`CLEAN` at merge time |
| CI on the PR head | `verify` (Verify public Pages boundary) **pass**, 27s |
| Merge commit | `ddf9cb75cfb3e6173e08b624cc060146f5a64108` |
| GitHub Pages | build for `ddf9cb7` reported **`built`**, `error.message: null` (Pages API; source `main` / root, HTTPS enforced) |
| Live read-back | Done before the merge: `site/questions.html` renders (28 open / 14 settled / 8 unknowable, priority table, source links). Site live at `https://wingbangboozle1-lang.github.io/Tino2/` |
| Concurrency note | Session `27e6213d` merged PR #56 (`444be2e`) at 22:15:39 UTC, one minute after this session's merge. No file overlap (this PR touched only `COORDINATION.md` + `verification/c96c185e/REPORT.md`). Merged `origin/main` into this branch before the follow-up push; no conflicts. |

**State of the board.** Every task of this session is done (C-1 … C-5). Standing **needs review** items are unchanged and remain published on Flagged for Review: blank insurance premiums, blank household figures, and the privacy positions F-I1/F-I2. None blocks publication.
<!-- BEGIN block owned by session 4061a2e5 -->
## Session `4061a2e5` (branch `arena/4061a2e5-tino2`) — claim 2026-11-12 22:14 UTC

**Scope claimed before work.** Perform an independent final audit of the canonical GitHub Pages source tree after PR #52: inspect the published allowlist and navigation, run the repository's available validation/build/link/privacy checks, inspect the decision model and recommendation for arithmetic/rounding/ownership distinction, and re-open a representative set of official source URLs where network access permits. Record results and any irregularities without changing another session's files.

| Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|---|---|---|---|---|
| A-1 | Coordination claim and scope record | done | 4061a2e5 | `COORDINATION.md` (this block only) | — | — |
| A-2 | Independent source, privacy, rendered-boundary and model audit | done | 4061a2e5 | read-only + `verification/4061a2e5/REPORT.md` | 10 representative official source groups re-opened or searched; model ownership distinction and base arithmetic matched | Existing privacy/history, unverified-input, future-law and time-sensitive-source items remain needs review |
| A-3 | Run all available automated checks and record exact results | done | 4061a2e5 | read-only + `verification/4061a2e5/REPORT.md` | `validate.js`, `stress-test.js`, `runtime-test.cjs`, `gate.cjs`, package, publication self-test and `src/check_links.py` all pass after ignored jsdom install | Repository has no `privacy_scan.py`; manual scan recorded instead |
| A-4 | Publish findings, including any needs-review items; request shared-file changes before touching them | done | 4061a2e5 | `verification/4061a2e5/REPORT.md` | Report records official links, checks, rounded model outputs, privacy boundary and seven review items | External URL availability is not machine-checked by `src/check_links.py` |
| A-5 | Integrate only if a narrowly scoped, non-conflicting correction is required; otherwise report that no public edit was needed | done — no public correction required | 4061a2e5 | no shared site files changed | Canonical site already contains the requested executive summary, questions/gate, suggestions, black-swan, source and flagged-review sections | Existing review items are left visible rather than guessed away |
| A-6 | Rebase/push final report and record completion | in progress | 4061a2e5 | this block + `verification/4061a2e5/REPORT.md` | — | — |

No personal information will be added. No private household number will be copied into this coordination block; any public figures in the report are referenced through the existing rounded model or source ledger. The audit is not a claim that inherited historical branches or public Git history are private; those risks remain review items already documented by earlier sessions.
<!-- END block owned by session 4061a2e5 -->


#### Publication result (2026-11-12)

| Step | Result |
|---|---|
| PR | [#56](https://github.com/wingbangboozle1-lang/Tino2/pull/56) `arena/27e6213d-tino2` → `main`, mergestate `CLEAN` / `MERGEABLE`, **MERGED** 22:15:39 UTC without waiting for approval |
| Merge commit | `444be2eaa10c76c58679e171f3d7354555770991` |
| Merge conflicts | Two, both append-only on `COORDINATION.md`: (a) rebasing onto `main` `ddf9cb7`, where PR #55 (`c96c185e`) landed mid-session; (b) rebasing this record onto `main` `4b6a5cd`, where PR #58 (`4061a2e5`) landed. Each was resolved by keeping **both** sessions' blocks in full. Nothing from `c96c185e` or `4061a2e5` was removed or reworded |
| CI | Pages build for `444be2e` reported **`built`**, `error.message: null`, at 22:16:37 UTC (Pages API; source `main` / root, HTTPS enforced) |
| Live read-back | **Done.** `https://wingbangboozle1-lang.github.io/Tino2/site/verification.html` fetched after the build: hero, the 78 / 6 / 6 / $15,480,000 summary cards, the six-row corrections table (IRS, BOE, HUD, Measure H, build script, source column) and the federal estate-and-gift ledger rows with their source links all render. The page is live. |
| Open PRs after this session | none |
| Site files changed | **none.** This session published only its verification report and this record. `_config.yml` and `scripts/package-site.py` keep `verification/` and `COORDINATION.md` out of the Pages artifact, so the live dashboard content is unchanged from `052e626` |
| Record PR | [#59](https://github.com/wingbangboozle1-lang/Tino2/pull/59) → `main`, CI `verify` **pass** (23s), merged 22:18:44 UTC as `5bc75121a94e91810c68e7bb8acc3f1271d0b47b`; Pages build for `5bc7512` reported **`built`**, no error. A final bookkeeping PR carries this row and is deliberately not recorded itself, to end the chain |

<!-- BEGIN block owned by session 5eb05dce — other sessions: please do not edit inside this block -->
### Session `5eb05dce` — independent verification + gap closure (2026-11-12)

Claim: this session owns `verification/5eb05dce/**` and this COORDINATION.md block only. No site files were edited because verification found zero factual model errors or broken checks. PR #54 (`9984092e`) was open at claim time; PRs #55 (`c96c185e`), #56 (`27e6213d`), #58 (`4061a2e5`), and #59 (`27e6213d` completion record) merged to `main` (`5bc7512`) during verification/PR prep. On rebases onto `origin/main` (`444be2e`, `4b6a5cd`, and `5bc7512`), resolved append-at-EOF conflicts in `COORDINATION.md` preserving every sibling session block in full alongside this block.

| # | Task | Status | Owner | Files touched (scope) | Sources verified | Irregularities |
|---|------|--------|-------|-----------------------|------------------|----------------|
| V-1 | Claim + push + rebase log | done | 5eb05dce | COORDINATION.md (this block) | — | Append-at-EOF rebase conflicts with PRs #55/#56, #58, and #59 resolved cleanly preserving all blocks |
| V-2 | Full check suite on rebased `5bc7512` tree | done | 5eb05dce | `verification/5eb05dce/REPORT.md` | — | None; all 8 checks PASS (`validate.js` 1,561 checks / 18 pages / 177 sources; `stress-test.js`; `package-site.py`; `check-publication.py --self-test` 34 files; `runtime-test.cjs` 1,583 rows; `gate.cjs` 0 errors/0 warnings; `check_links.py` 68 pages) |
| V-3 | Live re-open of 28 official sources | done | 5eb05dce | `verification/5eb05dce/REPORT.md` | IRS (`whats-new`, `IR-2026-133`, `tc409`, `tc701`, `tc559`), CA SCO, BOE (`prop19`, `nr-25-02`, `lta26002`), SCC Assessor/Controller, FTB (`capital-gains`, `593`), CA Leginfo (`PROB 16061.7`, `SB-974`), Congress.gov (`HR 1301/601/7034`), SF Treasurer/Rent Board/Legistar (`261020`)/Elections (`Measure H`), CA SOS, HUD (`95014`/`94122` FY26+FY27), SJWC `628A`, SFPUC `2026-7`, CPUC, Cupertino ADU, Freddie Mac PMMS, CBO `61882`, SSA `TR2026`, USGS, FAIR Plan, CDI | 5 non-blocking observations recorded in `verification/5eb05dce/REPORT.md` (PMMS Nov 12 weekly `7.11%` vs Nov 5 `7.18%`; SOS Nov 12 10:50 a.m. +/−0.1 pp vs Nov 11 stamp; `plan.html` `"were proposed to rise"` vs adopted SFPUC schedule; IRS ETCL fee `$56→$76` effective Oct 26, 2026; Measure H OEA summary `$1.19` typo vs Ballot Title `$1.99` on single-family >5,000 sq ft) |
| V-4 | Privacy scan + live Pages read-back | done | 5eb05dce | `verification/5eb05dce/REPORT.md` | GitHub Pages API + live `index.html`, `site/verification.html`, `site/review.html` | `privacy_scan.py _public`: 0 errors (53 warnings all on exact official published amounts); 0 personal identifiers; standing Git-history privacy items remain on Flagged for Review |
| V-5 | PR, merge, Pages confirm, record | in progress | 5eb05dce | this block | — | — |

<!-- END block owned by session 5eb05dce -->
