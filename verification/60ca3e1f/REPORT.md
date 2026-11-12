# Verification report — session `60ca3e1f`, 12 November 2026

Repository-only report. No personal information. Calculated dollar figures are rounded to $10; exact amounts are those a government body publishes.

## Result

- The published recommendation and every model input are unchanged. Selling Property A soon after inheriting it stays the best plan in every case this session ran.
- Both insurance premiums stay blank. No official body publishes a premium for a particular home.
- New on the site: the state regulator's 2026 premium survey for both survey locations, earthquake rates, FAIR Plan counts for both ZIP codes, the official long-run economic projections beside the model's assumptions, and when to expect the next Proposition 19 amount.
- The repository's six checks pass, and this session's own script passes 78 of 78 checks.

## How to run the checks again

```
python3 scripts/package-site.py
python3 scripts/check-publication.py --self-test
node scripts/validate.js
node scripts/stress-test.js
node scripts/runtime-test.cjs
node qa/tools/gate.cjs
node verification/60ca3e1f/check.cjs
```

| Check | Result on the final tree |
|---|---|
| `package-site.py` | Passed; rounding rule passed |
| `check-publication.py --self-test` | Passed; 28 public files |
| `validate.js` | Passed; 1,129 checks, 15 pages, 171 official sources |
| `stress-test.js` | Passed |
| `runtime-test.cjs` | Passed; 15 pages, 1,327 table rows, each with an official link |
| `qa/tools/gate.cjs` | Passed; 0 errors, 0 warnings |
| `verification/60ca3e1f/check.cjs` | Passed; 78 of 78 (list in `check-results.json`) |

## What `check.cjs` checks

| Part | What it tests | Checks |
|---|---|---|
| 1 | The typed survey figures against a second, separate reading of one official result page | 2 |
| 2 | Internal consistency of all 220 typed homeowners rows: premium rises with the dwelling limit; a higher deductible never costs more; row counts | 3 |
| 3 | Figures in `site/data` against the typed rows; source notes and links; ledger entries; every ledger topic has a heading on the Verified facts page | 33 |
| 4 | Model inputs unchanged; the landing-page figures reproduce; the page helper and the research script agree on 21 model runs; selling wins in each | 11 |
| 5 | Arithmetic on the official series: premium growth, home-price index, consumer prices, FAIR Plan year-on-year changes | 8 |
| 6 | Both premium cells still blank; no e-mail, street address or parcel number in this session's files; rounding | 3 |
| 7 | The packaged Operating costs page rendered with jsdom: no script error, every row linked, the published rows present | 18 |

## Limits of this verification

- **The official pages were read by a page-reading tool and the figures typed in by hand.** The sandbox cannot reach the Department of Insurance servers, so no script can fetch and compare. Part 1 is a second reading of the first 25 of 37 rows of one page (Cupertino, 40 years, $1,000,000). The other seven result pages were read once.
- Part 2 would catch most single typing errors, because each insurer's three premiums must rise in order and each pair of deductibles must fall in order. It would not catch an error that keeps the order.
- The survey is of a hypothetical home. It is not a quote, and it leaves out wildfire surcharges.
- The Congressional Budget Office home-price index is national and ends in 2036.
- Only the cover letter of Board of Equalization letter 2026/026 was read (2 of 11 sections).
- Rendered pages were read as text produced by jsdom. No browser was available, so layout, colour and behaviour on a phone were not checked.

## Official pages opened by this session on 12 November 2026

| Body | Page | What was read |
|---|---|---|
| California Department of Insurance | [2026 survey, Cupertino, 40 years, $1,000,000](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SANTA%20CLARA%20CUPERTINO,HOMEOWNERS,40%20Years,1000000,Y) | All rows, twice for the first 25. Five more homeowners pages and two earthquake pages are linked in `research/60ca3e1f/insurance.md` |
| California Department of Insurance | [Comparison tool start page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:20) | Hypothetical risks; wildfire surcharges not reflected |
| California Department of Insurance | [Survey format and footnotes](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/homeowners-footnotes.cfm) | Standard policy priced by the survey |
| California Department of Insurance | [Survey profiles](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/homeowners-profile.cfm) | Coverage range; no landlord profile |
| California Department of Insurance | [Residential guide](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm) | Vacancy of 60 days; dwelling limit; earthquake offer; FAIR Plan. Sections 1 to 5 of 6 |
| California Department of Insurance | [Wildfire risk report and workbook](https://www.insurance.ca.gov/01-consumers/200-wrr/WildfireRiskInfoRpt.cfm) | Statewide totals only |
| California FAIR Plan | [Policies in force by ZIP code](https://www.cfpnet.com/wp-content/uploads/2026/10/CFP-5-yr-PIF-Zip-FY26-DWE-261020.pdf) | Rows for both ZIP codes and the state total |
| California FAIR Plan | [Key statistics](https://www.cfpnet.com/key-statistics-data/) | Read; not published on the site |
| Congressional Budget Office | [Budget and Economic Outlook 2026 to 2036](https://www.cbo.gov/publication/61882) | Summary |
| Congressional Budget Office | [By the Numbers](https://www.cbo.gov/system/files/2026-02/61882-By-the-Numbers.pdf) | Projection table |
| Congressional Budget Office | [Economic projections data file](https://www.cbo.gov/system/files/2026-02/51135-2026-02-Economic-Projections.xlsx) | Calendar-year sheet: house price index, consumer prices, wages |
| Federal Reserve | [Projections of 16 September 2026](https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm) | Median table |
| Social Security Trustees | [2026 report, section II.C](https://www.ssa.gov/oact/TR/2026/II_C_assump.html) | Table II.C1 |
| Internal Revenue Service | [Release IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) | 2027 amounts; match the site |
| Internal Revenue Service | [What's new, estate and gift tax](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax) | 2026 amount; matches the site |
| Board of Equalization | [Proposition 19 page](https://boe.ca.gov/prop19/) | Rules; match the site |
| Board of Equalization | [2026 Letters To Assessors](https://www.boe.ca.gov/proptaxes/2026.htm) | Full list of titles |
| Board of Equalization | [Letter 2026/026](https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf) | Cover letter only |
| Board of Equalization | [News release NR 25-02](https://www.boe.ca.gov/news/2025/NR-25-02.htm) | Date and size of the last adjustment |

## Still not verified

| Item | Why | Official source to use |
|---|---|---|
| Premium for Property A | Needs the rebuild cost and a written quote | [Department of Insurance: not quotes](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/index.cfm) |
| Premium for Property B | No survey profile for a rented building | [Survey profiles](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/homeowners-profile.cfm) |
| Earthquake premium for either property | The survey gives a rate, not a premium; no decision to buy was supplied | [Residential guide](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm) |
| ZIP-level average premiums | The workbook's ZIP sheets were not visible to the reading tool | [Wildfire risk report](https://www.insurance.ca.gov/01-consumers/200-wrr/WildfireRiskInfoRpt.cfm) |
| Proposition 19 amount from 16 February 2027 | Not published yet | [2026 Letters To Assessors](https://www.boe.ca.gov/proptaxes/2026.htm) |
| A local long-run home-price projection | None found from an official body; the one read is national | [CBO data file](https://www.cbo.gov/system/files/2026-02/51135-2026-02-Economic-Projections.xlsx) |

## Reading the published site (task R-5)

All 15 pages were packaged, rendered to text and scanned by script for error markers, empty cells, stale wording and terms used without an explanation. The landing page and the Operating costs page were read in full, and so were the changed parts of seven other pages (Flagged, Other options, Properties, Black swan, Scenarios, Sources, Verified facts). The other pages were not read line by line.

| # | Defect | File | Last owner | Status |
|---|---|---|---|---|
| R-I1 | Page said the regulator's comparison tool could not be read. It can, by direct address. | `site/operating-costs.html` | `aa1f073e` | Fixed |
| R-I3 | Sources checked on 12 Nov were labelled "Carried forward · needs revalidation". | `site/sources.html` | `0d6ec51e`, `f344fcd1` | Fixed |
| R-I5 | One verified fact (CF-03, HUD rent benchmark) was counted in the page total but not shown, because its topic had no heading. | `site/verification.html` | `f16e6e34` | Fixed; `check.cjs` now tests for it |
| R-D1 | The landing page and one Flagged item said the 20-year solar tariff term was not confirmed. A later item and the Operating costs page record it as confirmed; the unknown is the year the system was switched on. | `index.html`, `site/review.html` | `0d6ec51e`, `f344fcd1` | Fixed (wording only) |
| R-D2 | Two insurance rows said that the tool gives no figure because it is a form. | `site/properties.html` | `0d6ec51e` | Fixed; both amounts stay blank |
| R-D6 | The Flagged page said 37 commits carry the account's e-mail address. That was the count before pull requests #40 and #41 were merged; on 12 Nov at 05:12 UTC the GitHub commit list showed 39 (38 merges and the first commit). Every merge adds one, so the item now says so instead of giving a fixed total. | `site/review.html` | `f344fcd1` | Fixed (wording only) |
| R-D3 | "NOI" is used on the Decision lab page (4 times) and the Properties page (6 times) without being spelled out. Two other pages spell it out once. | `site/decision.html`, `site/properties.html` | `0d6ec51e` | Not fixed; recorded |
| R-D4 | Four Flagged items speak of "this session", "an earlier session" or "a previous audit note", which means nothing to a reader. | `site/review.html` | `0d6ec51e` | Not fixed; recorded |
| R-D5 | The shared footer says "Correction audit: 11 Nov 2026" on every page, although three sessions changed pages on 12 Nov. | `assets/app.js` | `0d6ec51e` | Not fixed; recorded |

The scan found no script error, no "NaN" or "undefined", no missing-source marker and no broken internal link on any page. The only empty cells are the remarks column of the assessment-history table, which is empty by design.
