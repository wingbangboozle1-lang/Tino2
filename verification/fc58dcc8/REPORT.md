# Verification and Integration Report — Session `fc58dcc8`

**Date:** 2026-11-12  
**Branch:** `arena/fc58dcc8-tino2`  
**Base / Merged `origin/main`:** `9ef5d11` (`PR #54`, `#60`, `#61`, `#62`, `#64` merged cleanly with zero file overlap)

## 1. Scope & Summary

This session conducted a post-publication audit of the live GitHub Pages site (`https://wingbangboozle1-lang.github.io/Tino2/`) and canonical repository tree, directly retrieved previously search-extract-only official documents, upgraded ledger verification coverage without guessing household inputs, fixed cross-page consistency and UX defects, and re-ran the full build, validation, runtime, JSDOM gate, link, and privacy verification suite.

- **Base-case deterministic model outputs unchanged** (`2040 -> 2050`):
  - Sell Property A & invest: **$7,683,290**
  - Rent Property A: **$6,249,830**
  - Move into Property A: **$5,135,780**
  - `2045 -> 2055`: Sell **$9,125,340** / Rent **$7,395,620** / Live **$6,068,080**
  - `2050 -> 2060`: Sell **$10,838,040** / Rent **$8,752,170** / Live **$7,164,510**
- **Canonical ledger (`qa/ledger.json` -> `site/data/ledger.js`)**: `84` entries (`82` verified, `2` strictly unverified/blank: `INS-02` Cupertino earthquake quote, `INS-03` San Francisco earthquake quote). `FED-15`, `UT-02`, `SF-08`, and `N-12` were upgraded from `unverified` / search-extract to directly opened official sources, and `N-11`, `CA-05`–`CA-07`, `UT-04`, `N-04`, and `P19-01` were refreshed against direct official fetches.
- **Official source registry (`site/data/sources.js`)**: `178` official sources (`sfusdPropG` added; direct-read notes recorded for 12 Nov 2026 fetches).
- **Zero unrounded household figures or PII added**: parties and properties appear solely as `[OWNER]`, `[TRUSTEE]`, `[DECEDENT]`, `[HEIR]`, `Property A`, `Property B`.

## 2. Official Sources Directly Retrieved & Checked (12 Nov 2026)

| Ledger / Source ID | Direct Official URL(s) Opened | Directly Verified Fact |
|---|---|---|
| `FED-15` | `congress.gov/bill/119th-congress/house-bill/1301/all-actions`, `senate-bill/587/text/is`, `house-bill/601/all-actions`, `house-bill/7034/all-actions` | All four 119th Congress SALT / estate-tax bills remain at `Introduced` with no committee or floor advancement. |
| `UT-02` | `sjwater.com/grc-2025-27/`, `sjwater.com/2026-rates/` | GRC A.24-01-001 requested average residential bills (3/4-in, 10 Ccf): `$107.44 -> $120.62` (`+$13.18`, `+12.3%`, 2025), `$125.44` (`+$4.82`, `+4.0%`, 2026), `$131.12` (`+$5.68`, `+4.5%`, 2027, excl. surcharges). `2026-rates/` documents the approved Jan 1, 2026 ~`2.8%` increase and July 1, 2026 Valley Water wholesale pass-through. |
| `SF-08` | `sftreasurer.org/property/parcel-tax-exemptions-and-special-assessments`, `sfusd.edu/announcements/2020-10-02-learn-about-upcoming-education-related-ballot-measures`, `sfusd.edu/about-sfusd/sfusd-news/press-releases/2021-11-17-sfusd-will-receive-one-time-123-million-after-lawsuit-challenging-voter-approved-prop-g-measure` | June 2018 Prop G enacted `$298`/parcel (`$320` in FY2020-21) before Nov 2020 Prop J (`$288` + CPI, School Parcel Tax of 2020; `$334.38` FY2025-26) superseded Prop G starting FY2021-22. |
| `N-12` (IRS & CDI) | `irs.gov/publications/p527`, `p523`, `instructions/i706`, `instructions/i1041`, `pub/irs-pdf/p551.pdf`, `pub/irs-drop/rp-25-32.pdf`, `businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes`, `insurance.ca.gov/01-consumers/105-type/5-residential/` | Directly confirmed 27.5-yr GDS residential depreciation & `$25,000` loss phaseout (`$100k–$150k`), Sec. 121 Worksheet 3 recapture & post-2008 nonqualified use, Form 706 Table A (`$345,800` + `40%` over `$1M`) + `$15,000,000` 2026 exclusion (P.L. 119-21) + 2011–2026 filing table + 9-mo/6-mo Form 4768 deadlines + Form 8971 + Rev. Proc. 2022-32 5-yr portability, Pub 551 basis step-up rules, and `rp-25-32.pdf` Table 5 Estates & Trusts brackets (`10% <= $3,300`, `24% $3,300–$11,700`, `35% $11,700–$16,000`, `37% > $16,000`, base `$3,851`). |
| `CA-05`–`CA-07` & SF | `electionresults.sos.ca.gov/returns/ballot-measures` (Nov 12, `10:50 a.m.`), `sfelections.org/results/20261103/index.html` (Nov 10, `4:00 p.m.`) | Exact Nov 12 CA SOS tallies: `Prop 3` `7,356,449` (`60.7%`) / `4,761,939` (`39.3%`); `Prop 40` `5,808,868` (`47.6%`) / `6,400,441` (`52.4%`); `Prop 42` `6,216,097` (`51.4%`) / `5,887,873` (`48.6%`); `Prop 43` `5,057,119` (`42.5%`) / `6,834,825` (`57.5%`). SF Measure H `74.4%` Yes / RTM `79.17%` Yes. |
| `N-11` & `P19-01` | `elections.cdn.sos.ca.gov/ccrov/2026/may/26138jh.pdf`, CA SOS Nov 7, 2025 release (`#1994` / AG `#25-0017`), `boe.ca.gov/proptaxes/2026.htm`, `boe.ca.gov/proptaxes/pdf/lta26026.pdf` | Directly opened CCROV `#26138` (`May 18, 2026`, `919,170` threshold) confirming SOS `#1994` failed qualification; confirmed 2026 LTAs `2026/001`–`2026/044` (none sets Feb 16, 2027 Prop 19 cap yet) and LTA `2026/026` FAQ rules (trusts, legal entities/SMLLCs, life estates, non-pro rata distributions). |
| GitHub | `docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository` | Directly confirmed `git-filter-repo` consequences, fork/clone recontamination, and cached PR-view purge scope. |

## 3. Defects Fixed Across Site & Scripts

1. **`index.html`**: Fixed stale readiness counts (`28` open / `14` answered instead of `30` / `12`) and suggestions counts (`27` proposals / `4` bundles / `3` privacy steps instead of `19` / `3` / `2`).
2. **`site/data/gate.js` & `site/questions-gate.html`**: Updated `Q-23` (`4BR_2027` / `3BR_2027` FY2027 Cupertino SAFMR benchmarks `$5,800` and `$5,440` selectable in model & simulator) and `Q-24` (reclassified `missing` -> `household` reflecting live FY2027 94122 SAFMR `$2,770`/`$3,410` verification while actual Property B unit rent remains unprovided), giving `40` items = `14` settled + `11` household + `15` missing; removed internal `"the brief"` phrasing across `Q-01`–`Q-35` and `questions-gate.html`.
3. **`site/black-swan.html` & `site/data/history-engine.js` & `scripts/validate.js`**: Added FY2027 Cupertino SAFMR rent presets (`4BR_2027` `$5,800/mo`, `3BR_2027` `$5,440/mo`) to the 50-year recorded-history replay and Monte Carlo simulator alongside `4BR`/`3BR` FY2026 benchmarks, plus parity assertions in `scripts/validate.js`.
4. **`site/options.html`**: Clarified direct verification of IRS Pub 523 (`p523`) and Rev. Proc. 2025-32 (`rp-25-32`) Table 5 (`$3,851` base + `37%` over `$16,000`).
5. **`site/properties.html` & `site/plan.html`**: Aligned SFPUC adopted FY2026–2029 water/wastewater schedule wording consistently with `site/operating-costs.html` and `site/verification.html`.
6. **`site/review.html`**: Deduplicated identical `irsEstateTax` row (`95 -> 94` unique items), replaced stale `Suggestions S12` reference with `Suggestions S12 / S21`, generalized commit counts, updated Prop G (`SF-08`), SJWC/SFPUC, Nov 12 SOS, and `N-12` directly-verified statuses while preserving all standing `needs review` privacy, historical-branch, unverified-household-input, and insurance-quote flags.
7. **`site/verification.html` & `site/sources.html` & `qa/ledger.json` & `site/data/ledger.js` & `site/data/sources.js`**: Stripped raw backticks in `verification.html` prose, added Prop G (`SF-08`) + 12 Nov pass table entry, fixed `"household record"` / `sjwater.com/2026-rates/` details in `qa/ledger.json`, regenerated `site/data/ledger.js`, and documented the `178` sources in `site/sources.html`.

## 4. Verification Suite Results (Post-Merge with `origin/main` `9ef5d11`)

- `python3 qa/tools/build_ledger_js.py`: `site/data/ledger.js: 84 ledger entries, 6 series`
- `python3 scripts/package-site.py`: `Packaged canonical site only; legacy material excluded. Rounding rule passed (no household data in the check).`
- `python3 scripts/check-publication.py --self-test`: `PASS: fail-closed tests reject unlisted files, symlinks and missing pages.` / `PASS: 34 reviewed public files only; internal material excluded.`
- `node scripts/validate.js`: `PASS: 1569 checks across 18 pages and 178 official sources.` (`Base case 2040→2050: sell $7,683,290, rent $6,249,830, live $5,135,780.`)
- `node scripts/stress-test.js`: `PASS: 50-year paths, estate ownership, privacy, real-dollar and shock tests`
- `node scripts/runtime-test.cjs`: `PASS: 18 rendered pages; 1584 rendered rows source-linked; no runtime errors or broken local links`
- `node qa/tools/gate.cjs`: `PASS: 18 rendered pages · 1584 table rows (1575 with their own official link, 9 calculated rows with a context link only) · 5006 dollar amounts checked (120 official exact figures) · 559 internal and 2076 external links · 0 errors · 0 warnings`
- `python3 src/check_links.py .`: `68 pages, 887 table rows, 128 distinct external links (not machine-checked from this sandbox)` — `0` broken local links
- `python3 integration/tools/privacy_scan.py`: `0 error(s), 252 warning(s)` (all warnings are official published figures inside prose notes rather than top-level scalar fields, zero PII or unrounded household inputs)
