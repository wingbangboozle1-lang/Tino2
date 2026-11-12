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
- **R-I5 (defect, `site/verification.html`; last owner `f16e6e34`).** The Verified facts page shows only ledger topics that are in its list of headings. One verified entry from an earlier session, CF-03 (HUD rent benchmark, FY2024 to FY2026; topic `rent-benchmark`), was therefore counted in the page total but not shown. That heading and the new `economic-baseline` heading were added; `verification/60ca3e1f/check.cjs` now fails if any ledger topic has no 
... output truncated ...
 has no `privacy_scan.py`; manual scan recorded instead |
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
## Session `f2cc9e15` — 2026-11-12 — claim

**State read at claim.** `origin/main` = `052e626` (merge of PR #52) when this block was written. While it sat unpushed, `origin/main` moved to `444be2e` (PRs #55 and #66 merged — both verification-only); this block was then rebased onto `444be2e` keeping both sides; `origin/main` moved again to `4b6a5cd` (PR #58 merged), and again to `5bc7512` (PR #59 merged), and again to `7f9bab5` (PRs #57 and #61 merged — record/verification only); this block was rebased past each the same way. The smoke verification in F-3 was re-run on the `444be2e` tree; PRs #55–#59 add only `verification/**` and `COORDINATION.md`, so the published allowlist artifact is unchanged. `git ls-remote --heads origin` fetched; the only open pull request is **#54** (`arena/9984092e-tino2`, final independent re-verification, verification-only, opened 22:13 UTC, files `verification/9984092e/**` + its own `COORDINATION.md` block). No session block on the board lists an unclaimed task; every prior task is `done` or standing `needs review` (published on the Flagged for Review page). No live claim covers the scope below. This session does **not** touch PR #54, `site/**`, `index.html`, `assets/**`, `scripts/**`, `qa/**`, or `verification/9984092e/**`.

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| F-1 | Claim non-overlapping scope; push at once | done on push of this block | f2cc9e15 | `COORDINATION.md` (this block only) | N/A | — |
| F-2 | **done.** README accuracy pass. The `Structure` section is stale and self-contradictory: `site/questions.html` is listed twice and `site/suggestions.html` three times with mutually inconsistent descriptions, and it omits `site/operating-costs.html`, `site/plan.html`, `site/questions-gate.html`, `site/verification.html`, `site/black-swan.html`, and the data files `gate.js`, `questions.js`, `suggestions.js`, `options.js`, `stress.js`, `costs.js`, `ledger.js`, `history.js`, `history-engine.js`. Rewrite the list from the files actually present; descriptions taken from each page's own meta description / `data-title`, counts re-derived from the data files. No site content changes | done | f2cc9e15 | `README.md` | N/A (documentation of existing files) | — |
| F-3 | **done.** Independent smoke verification of the merged tree from `origin/main`: re-run `validate.js`, `stress-test.js`, `package-site.py`, `check-publication.py --self-test`, `qa/tools/gate.cjs`, `privacy_scan.py`, `src/check_links.py`; record the GitHub Pages deployment state for `origin/main` and its latest build commit via the Pages API; write the result to a report | done | f2cc9e15 | `verification/f2cc9e15/**` (new) | No official page re-opened; no new figure claimed | — |
| F-4 | in progress — PR to `main`, merge without waiting, confirm the Pages build for the merge commit, record the PR link and result as a comment on the PR (a second merge would add a commit authored with the account e-mail, finding F-I1) | claimed | f2cc9e15 | this block + the PR | — | — |

**Rules this session follows.** No personal information in any committed file. No household figure is quoted; only file names, page names and counts re-derived from the tracked files are published. The platform fixes the branch name, so the `session-<id>/<task>` convention appears as the session ID inside `arena/f2cc9e15-tino2`. `git pull --rebase` before every push; conflicts resolved keeping both sides.

**Coordinating note F-C1.** `README.md` is shared, but its last claimed editor (session `55c16cea`) finished and merged (PR #52). PR #54 appends to `COORDINATION.md`; if it merges first, this block is rebased past it and both blocks are kept.

<!-- END block owned by session f2cc9e15 -->

---

## Session `58941d22` — completion record (2026-11-12)

| Task | Status | Owner | File scope |
|---|---|---|---|
| Integration verification and finalization of the executive summary landing, suggestions section, questions/info/answers register, black-swan section, year-by-year projections, comparison, inheritance process, tax law analysis, GitHub Pages site, verification, PR to `main`, merge without waiting, confirm Pages build, read live pages back, record PR/merge in `COORDINATION.md` | done | 58941d22 | `COORDINATION.md`, `index.html`, `site/*.html`, `site/data/*.js`, `assets/app.js`, `qa/ledger.json`, `scripts/validate.js` |

---

## Session `cf976834` — integration and finalization (2026-11-12)

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| I-1 | Coordination: read the board and `git ls-remote`, claim integration scope (executive summary, suggestions section, questions/info/answers register, black-swan section, year-by-year projections, comparison, inheritance process, tax law analysis, GitHub Pages site, verification, PR/merge/record) | **in progress** | cf976834 | `COORDINATION.md` (this block), `index.html`, `site/*.html`, `site/data/*.js`, `assets/app.js`, `qa/ledger.json`, `scripts/validate.js` | N/A | I-C1 below |

**Scope.** Integration and finalization of the executive summary landing (`index.html`), suggestions section (`site/suggestions.html` + `site/data/suggestions.js`), questions/info/answers register (`site/questions.html` + `site/data/questions.js`), black-swan section (`site/black-swan.html` + `site/data/history-engine.js`), year-by-year projections (`site/properties.html` + `site/data/model.js` + `site/data/costs.js`), live vs rent vs sell-and-reinvest comparison (`site/decision.html` + `site/data/options.js`), inheritance process (`site/inheritance.html`), tax law analysis (`site/estate-tax.html`), GitHub Pages site (`_config.yml`, `scripts/validate.js`, `scripts/package-site.py`), verification (`site/verification.html` + `qa/ledger.json`), PR to `main`, merge without waiting, confirm Pages build, read live pages back, record PR/merge in `COORDINATION.md`.

**Coordinating note I-C1.** Because the remote holds only `main` at `69c64d9` and no other session is currently claiming the integration scope, this session claims the full integration and finalization. Small frequent commits, `git pull --rebase` before push, resolve conflicts without discarding others' work.

**Privacy.** No personal information in any committed file; parties and addresses stay placeholders (Property A / Property B); household amounts appear only rounded to $10. Every dollar figure of $1,000 or more on the new pages is a multiple of $10 or a figure a government body publishes (and, where it is new, added to `qa/ledger.json`). Every table row carries an official source link or is left blank and flagged unverified. Nothing is inferred.

<!-- END block owned by session cf976834 -->

---

## Session `cf976834` — integration and finalization (2026-11-12)

| # | Task | Status | Owner | File scope | Sources verified | Irregularities |
|---|------|--------|-------|------------|------------------|----------------|
| I-1 | Coordination: read the board and `git ls-remote`, claim integration scope (executive summary, suggestions section, questions/info/answers register, black-swan section, year-by-year projections, comparison, inheritance process, tax law analysis, GitHub Pages site, verification, PR/merge/record) | **in progress** | cf976834 | `COORDINATION.md` (this block), `index.html`, `site/*.html`, `site/data/*.js`, `assets/app.js`, `qa/ledger.json`, `scripts/validate.js` | N/A | I-C1 below |

**Scope.** Integration and finalization of the executive summary landing (`index.html`), suggestions section (`site/suggestions.html` + `site/data/suggestions.js`), questions/info/answers register (`site/questions.html` + `site/data/questions.js`), black-swan section (`site/black-swan.html` + `site/data/history-engine.js`), year-by-year projections (`site/properties.html` + `site/data/model.js` + `site/data/costs.js`), live vs rent vs sell-and-reinvest comparison (`site/decision.html` + `site/data/options.js`), inheritance process (`site/inheritance.html`), tax law analysis (`site/estate-tax.html`), GitHub Pages site (`_config.yml`, `scripts/validate.js`, `scripts/package-site.py`), verification (`site/verification.html` + `qa/ledger.json`), PR to `main`, merge without waiting, confirm Pages build, read live pages back, record PR/merge in `COORDINATION.md`.

**Coordinating note I-C1.** Because the remote holds only `main` at `69c64d9` and no other session is currently claiming the integration scope, this session claims the full integration and finalization. Small frequent commits, `git pull --rebase` before push, resolve conflicts without discarding others' work.

**Privacy.** No personal information in any committed file; parties and addresses stay placeholders (Property A / Property B); household amounts appear only rounded to $10. Every dollar figure of $1,000 or more on the new pages is a multiple of $10 or a figure a government body publishes (and, where it is new, added to `qa/ledger.json`). Every table row carries an official source link or is left blank and flagged unverified. Nothing is inferred.

<!-- END block owned by session cf976834 -->

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
