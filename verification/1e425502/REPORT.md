# Verification record — session 1e425502 (12 November 2026)

Repository-only; not published. No household figure is typed in this folder: every input was read from `site/data/model.js` at run time, and every dollar amount below is rounded to the nearest $10 unless it is an amount published by a government body. Properties are labeled A and B; no personal names, street addresses, parcel numbers, account identifiers, or private documents appear in this folder.

## What was checked

### T-2 Brief-coverage audit (read-only)

Every requirement in the brief was mapped to a published page. All are present on the canonical site (`index.html` + `site/*.html`, 15 pages):

| Brief requirement | Published location | Result |
|---|---|---|
| Executive summary with important details | `index.html` — Bottom line, by-year table, drivers, costs, tax levels, steps, law watch | Present |
| Privacy: anonymize, placeholders, nothing personal on the site | Properties labeled A and B throughout; privacy strip on `index.html`; `scripts/package-site.py` + `qa/tools/gate.cjs` R2 identifier scan; `integration/tools/privacy_scan.py` 0 errors | Present |
| Cupertino inherited vs San Francisco already owned — factored into decision | `site/plan.html` — household comparison, four plans, distinction table | Present |
| Black swan section, 50-year real conditions, growth/inflation never consistent | `site/stress.html` (50-year paths), `site/black-swan.html` (recorded data), `site/scenarios.html` (shock replays), `site/data/history-engine.js` | Present |
| Costs rounded to nearest $10, clear numbers/projections | `site/data/model.js` `round10`/`fmtMoney`; gate R1: 4,620 amounts checked, 0 errors | Present |
| Inherit by trust 2040–2050; local/state/federal law; live/rent/sell + reinvest after taxes | `site/decision.html` (Decision lab), `site/plan.html`, `site/estate-tax.html`, `site/inheritance.html` | Present |
| Property tax, insurance, water, electricity, maintenance on inheriting; value/tax/assessed by year | `site/properties.html` (year-by-year), `site/operating-costs.html`, `site/data/costs.js` | Present |
| Step-by-step inheritance process | `site/inheritance.html` checklist with deadlines | Present |
| Cupertino water $100–$150/mo, solar credit, insurance research | `site/operating-costs.html` + `site/data/costs.js`; household inputs labeled unverified, official tariffs cited | Present |
| Cupertino ZIP 95014 value, tax/assessment history tables | `site/data/model.js` `historyA`; `site/properties.html` rounded history | Present |
| San Francisco ZIP 94122 value, $7,150/mo rent, 3 units, water/electricity, insurance research | `site/san-francisco.html`, `site/data/model.js` `historyB` + `sfAnnual` | Present |
| Best plan and why; maximize profit, lower costs; law changes discussed | `site/plan.html` + `site/sources.html` watchlist | Present |
| Inheritance money over threshold; amount allowed before tax; future projections | `site/estate-tax.html` thresholds by year, headroom, filing | Present |
| No manual input; work line by line from official sources; flag irregularities | This record + `site/review.html` Flagged for Review + `site/verification.html` | Present |
| GitHub Pages live site, clean dashboard, subpages, tables | 15 pages, navigation on every page, runtime-test PASS | Present |
| Every table row has official source link or blank/flagged unverified | `scripts/runtime-test.cjs`: 1,259 rendered rows source-linked; gate R4 PASS | Present |
| Coordination board, non-overlapping scopes, PR merge without waiting, Pages confirm | This block in `COORDINATION.md`; T-6 below | In progress |

No gap was found that requires a site edit. The site already covers every brief item.

### T-3 Automated suite on the final tree (12 Nov 2026)

| Check | Result |
|---|---|
| `node scripts/validate.js` | PASS: 1,086 checks across 15 pages and 151 official sources. Base case 2040→2050: sell $7,683,290, rent $6,249,830, live $5,135,780 |
| `node scripts/stress-test.js` | PASS: 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| `python3 scripts/package-site.py` | PASS: canonical site only; legacy material excluded; rounding rule passed |
| `python3 scripts/check-publication.py --self-test` | PASS: 28 reviewed public files only; internal material excluded |
| `node scripts/runtime-test.cjs` (after `npm install --prefix .cache/test jsdom@26.1.0`) | PASS: 15 rendered pages; 1,259 rendered rows source-linked; no runtime errors or broken local links |
| `node qa/tools/gate.cjs` | PASS: 15 pages · 1,259 table rows (1,250 with own official link, 9 calculated rows with context link only) · 4,620 dollar amounts checked (74 official exact figures) · 325 internal and 1,680 external links · 0 errors · 0 warnings |
| `python3 src/check_links.py .` | 62 pages, 871 table rows, 124 distinct external links, 0 errors |
| `python3 integration/tools/privacy_scan.py` | 0 errors, 133 warnings (all warnings are sub-$10 tariff unit rates or government-published exact figures already in `qa/ledger.json`; no household figure, address, or identifier) |

Base case is unchanged from the prior sessions: 2040→2050 sell $7,683,290, rent $6,249,830, live $5,135,780. The recommendation (sell Property A soon after inheriting, keep Property B) is confirmed by the suite.

### T-4 Official-source re-verification (opened directly 12 Nov 2026)

Each page below was opened in this session and the wording compared with the site's claim. All match; no correction needed.

| # | Claim on the site | Official wording found | Source |
|---|---|---|---|
| 1 | Federal basic exclusion $15,000,000 for deaths in 2026 | "WFTC amends § 2010(c)(3) by increasing the basic exclusion amount to $15,000,000 for calendar year 2026" (Public Law 119-21, signed July 4, 2025) | [IRS — What's new: Estate and gift tax](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax) |
| 2 | 2027 exclusion $15,480,000; gift exclusion $20,000 (2027) / $19,000 (2026) | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026"; "annual exclusion for gifts increases to $20,000, up from $19,000" (IR-2026-133, Nov. 5, 2026) | [IRS IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) |
| 3 | Prop 19: value limit = factored base year value + $1M (biennially adjusted); homeowners' exemption within 1 year; claim within 3 years | "Value limit of current taxable value plus $1,000,000 (as biennially adjusted)"; "File for homeowners' exemption within 1 year of transfer; File claim for exclusion within 3 years or before transfer to third party" | [BOE — Proposition 19](https://boe.ca.gov/prop19/) |
| 4 | Prop 19 amount $1,044,586 for Feb 16, 2025–Feb 15, 2027; one year's California HPI change (2.15%) applied; next adjustment Feb 2027 | "the $1 million amount is adjusted to $1,044,586"; "FHFA announced that the annual percentage change in the House Price Index for California for 2024 was 2.15 percent"; "The next adjustment ... will occur in February 2027" | [BOE LTA 2025/009](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) |
| 5 | No California estate-tax return for deaths on/after Jan 1, 2005 | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return" | [State Controller — California Estate Tax](https://www.sco.ca.gov/ardtax_estate_tax.html) |
| 6 | Inherited basis generally FMV at date of death | "The basis of property inherited from a decedent is generally ... The fair market value (FMV) of the property on the date of the decedent's death (whether or not the executor ... files an estate tax return)" | [IRS — Sale of inherited property FAQ](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances) |
| 7 | California taxes capital gains as ordinary income (no lower rate) | "California does not have a lower rate for capital gains. All capital gains are taxed as ordinary income" | [FTB — Capital gains and losses](https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html) |
| 8 | HUD FY2026 SAFMR ZIP 95014: 3BR $5,870, 4BR $6,390; FY2025: 3BR $5,850, 4BR $6,370 | Table: "Three-Bedroom $5,870 | Four-Bedroom $6,390"; FY2025 floor table lists "$5,850 | $6,370" | [HUD FY2026 SAFMR 95014](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026) |
| 9 | SF Rent Board fee $59.00/unit (2026–27), $29.50 recoverable, exemption deadline Dec 14, 2026, vacant units billed | "$59.00 per dwelling unit"; "you may be able to collect 50% of the fee ... $29.50 per dwelling unit"; "The deadline to submit a Request for Exemption for the 2027 Rent Board fee is December 14, 2026"; "vacant units ... are billed" | [SF.gov — The Rent Board Fee](https://www.sf.gov/rent-board-fee) |

Result: 9 of 9 match. No value was inferred; no blank was filled. Items that remain blank on the site (both insurance premiums, Property A tax-rate area, meter sizes, Property B parcel tier, solar interconnection date, trust type, tenancy terms, Measure H parcel amount until certification) were not re-opened because no official page publishes a property-specific figure for them — they remain correctly flagged as unverified on the Flagged for Review page.

### T-5 Stale PR #3

PR #3 (`arena/8c4d9e77-tino2`, opened 2026-11-10) adds 10 files (311 insertions) including `pages/decision.html`, `pages/law.html`, `pages/projections.html`, `pages/review.html`, `assets/site.css`, `scripts/check_site.py`. Its content is superseded by the integrated canonical site on `main` (15 pages, 1,086 checks, full model, stress tests, gate). Merging it would reintroduce legacy pages that `_config.yml` and `scripts/check-publication.py` deliberately exclude from the Pages artifact. Disposition: close with a handoff comment pointing to `main` and this record; do not merge. Nothing is discarded — the branch remains on the remote for reference.

## Irregularities

| ID | Finding | Status |
|---|---|---|
| T-I1 | Standing High privacy findings from prior sessions (older branches and commit history in the public repository still hold exact household figures; three supplied amounts are already multiples of $10) cannot be fixed by editing the site | Unchanged; remains published on the Flagged for Review page; does not block merge |
| T-I2 | `qa/tools/gate.cjs` and `scripts/runtime-test.cjs` require `.cache/test/node_modules/jsdom`, which is gitignored and absent on a fresh checkout; the CI workflow installs it, but a local run without the install fails with `MODULE_NOT_FOUND` | Noted; this session installed it per the workflow and both checks PASS. No site change needed |
| T-I3 | `integration/tools/privacy_scan.py` reports 133 warnings (sub-$10 tariff rates, government exact figures) with 0 errors | Expected; gate R1 passes because those figures are in `qa/ledger.json` or source notes. No action |
| T-I4 | Live-URL read-back of `wingbangboozle1-lang.github.io` is outside this sandbox's permitted hosts | Not claimed. Deployment is confirmed from the Pages API (`built`, correct commit) and the CI Jekyll build, as in prior sessions |

## Limits of this verification

1. The suite cross-checks the model's arithmetic and the site's structure; it does not verify the household's private inputs (values, rents, bills), which no official source publishes. Those remain labeled unverified planning inputs.
2. Official-source checks above cover the nine highest-stakes rules. The full 151-source register was verified by prior sessions and is carried forward; this session re-opened the nine that the decision turns on.
3. Future thresholds (2028+ estate exclusion, Prop 19 amounts after Feb 2027) are scenarios, not official forecasts, and are labeled as such on the site.

## Publication

See T-6 in `COORDINATION.md` for the PR link, merge commit, and Pages build result.
