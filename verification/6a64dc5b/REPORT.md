# Session 6a64dc5b — independent verification and two new pages (12 November 2026)

**Branch:** `arena/6a64dc5b-tino2`, based on `main` = `bfb2268` (merge of PR #42); `main` advanced to `ed9cbbd` during the session and was merged in (see section 6).
**Scope claimed:** (S-2) re-open the official sources that drive the decision and record each result; (S-3) a decision-readiness register at `site/questions.html`; (S-4) a suggestions register with a local-only choice record at `site/suggestions.html`; (S-5) wiring, checks and ledger; (S-6) own PR, merge and Pages confirmation. No published figure, ranking or recommendation was changed.

**Method.** Each source below was opened on 12 November 2026 with the fetch tool and the quoted passage was read on the page itself, not taken from an earlier session's report. Where a page could not be read, the row says so and nothing is inferred. Figures already recorded in `qa/ledger.json` were not duplicated unless this session added a new distinction (P19-12).

## 1. Sources re-opened in this session

| # | Figure or rule checked | Official page | Passage read | Result |
|---|---|---|---|---|
| 1 | Proposition 19 exclusion $1,044,586 for transfers 16 Feb 2025 – 15 Feb 2027 | [BOE NR 25-02](https://www.boe.ca.gov/news/2025/nr-25-02.htm) | "the amount increased by 2.15 percent, from $1,022,600 to $1,044,586" | **PASS** |
| 2 | The cap is adjusted every other year, not annually | [BOE LTA 2026/026](https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf) | Definition 5: "The $1 million is adjusted on February 16, 2023, and every other February 16 thereafter." | **PASS** (model takes one step every second February) |
| 3 | BOE Prop 19 comparison table says "biennially adjusted" | [BOE Prop 19](https://www.boe.ca.gov/prop19/) | Parent-child table: "Value limit of current taxable value plus $1,000,000 (as biennially adjusted)" | **PASS** |
| 4 | Parent-child eligibility: principal residence of both, claim within one year, value test | [Santa Clara County Assessor](https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2) | "both the parents prior to the transfer and at least one child after the transfer must be the principal resident within one year"; "eligible for the homeowners' … exemption … within one year" | **PASS** |
| 5 | 2026 federal basic exclusion $15,000,000 | [IRS, What's new — estate and gift tax](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax) | "increasing the basic exclusion amount to $15,000,000 for calendar year 2026" | **PASS** |
| 6 | 2027 federal basic exclusion $15,480,000; annual gift exclusion $20,000 | [IRS IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026" | **PASS** |
| 7 | Filing-threshold table by year of death | [IRS, Estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax) | Table ends at "2026 \| $15,000,000"; no 2027 row yet | **PASS** (the 2027 figure is on IR-2026-133 only) |
| 8 | California has no estate or inheritance tax for deaths on or after 1 Jan 2005 | [State Controller, California Estate Tax](https://www.sco.ca.gov/ardtax_estate_tax.html) | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return." | **PASS** |
| 9 | An inheritance is not income; income it later produces is taxable | [FTB, Gifts and inheritance](https://www.ftb.ca.gov/file/personal/income-types/gifts-and-inheritance.html) | "If you received a gift or inheritance, do not include it in your income." | **PASS** |
| 10 | Trustee notice within 60 days | [Probate Code §16061.7](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=16061.7.&lawCode=PROB) | (f): "not later than 60 days following the occurrence of the event requiring service" | **PASS** |
| 11 | Home-sale exclusion $250,000 / $500,000 and the two-of-five-year tests | [IRS Topic 701](https://www.irs.gov/taxtopics/tc701) | "you may qualify to exclude up to $250,000 of that gain … up to $500,000 … if you file a joint return" | **PASS** |
| 12 | HUD FY2026 Small Area FMR, ZIP 95014: 4BR $6,390, 3BR $5,870 | [HUD FY2026 SAFMR calculation](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026) | Table: "Efficiency $3,340 \| One-Bedroom $3,800 \| Two-Bedroom $4,440 \| Three-Bedroom $5,870 \| Four-Bedroom $6,390" | **PASS** |
| 13 | San Francisco Rent Board fee $59.00 per dwelling unit, 2026–27; exemption window closes 14 Dec 2026 | [SF Rent Board](https://www.sf.gov/rent-board-fee) | "For the 2026-2027 tax year, the fee is: $59.00 per dwelling unit"; "The deadline to submit a Request for Exemption for the 2027 Rent Board fee is December 14, 2026." | **PASS** |
| 14 | CDI 2026 homeowners survey, Cupertino, 40-year-old home, $1,000,000 dwelling | [CDI survey result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SANTA%20CLARA%20CUPERTINO,HOMEOWNERS,40%20Years,1000000,Y) | "This is not an insurance premium quote"; premiums effective 1 May 2026; lowest $1,543 (Pacific Specialty), highest $6,430 (Grange), with a $2,500 deductible | **PASS** |
| 15 | CBO February 2026 long-run line: CPI 2.3%, PCE 2.0%, real GDP 1.8%, 10-year Treasury 4.3–4.4% | [CBO, By the Numbers](https://www.cbo.gov/system/files/2026-02/61882-By-the-Numbers.pdf) | Economic outlook table: "Consumer price index … 2.3 \| 2.3"; "PCE price index … 2.0 \| 2.0"; "10-year Treasury notes … 4.3 \| 4.4" | **PASS** |
| 16 | Federal Reserve September 2026 projections: PCE inflation 3.7% (2026), 2.3% (2027), 2.1% (2028), 2.0% longer run; real GDP 2.0% longer run | [Fed SEP, 16 Sep 2026](https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm) | Table 1, median column | **PASS** |
| 17 | Social Security Trustees 2026 intermediate assumptions: CPI-W 2.4%, covered wage 3.57%, real interest 2.3% | [2026 Trustees Report, Table II.C1](https://www.ssa.gov/oact/TR/2026/II_C_assump.html) | Table II.C1, economic rows | **PASS** |

**Not re-opened by this session** (carried forward, with the earlier session's link and date on the source page): the Santa Clara County rate book, the San Francisco parcel-tax page, the CDI earthquake and Sunset District survey pages, the FAIR Plan ZIP counts, the HUD FY2025 and Property B lookups, the FHFA/FRED series and the recorded-data CSV, the ballot results page, and the pending-bill pages. These are unchanged by this session and are shown on the site with their own source links and check dates.

## 2. Irregularity found and published on Flagged for Review

**IREG-1 (Low).** The Santa Clara County Assessor's parent-child page says "The $1 million allowance will be adjusted annually beginning in 2023." The Board of Equalization's Proposition 19 page says "biennially adjusted", and Letter to Assessors 2026/026 sets the adjustment on 16 February 2023 "and every other February 16 thereafter". The model follows the Board. Recorded on `site/review.html` with both links; no figure changed.

Observation, not an error: the IRS "Estate tax" page still ends its filing-threshold table at 2026, so the 2027 amount can only be cited from IR-2026-133. The site does that and labels the year.

## 3. Repository review and checks run

| Check | Command | Result |
|---|---|---|
| Model, sources, links, page count | `node scripts/validate.js` | **PASS** — 1,170 checks across 17 pages and 171 official sources; base case 2045 unchanged (sell $9,125,340 / rent $7,395,620 / live $6,068,080) |
| Publication allowlist | `python3 scripts/package-site.py` then `python3 scripts/check-publication.py --self-test` | **PASS** — 30 reviewed public files; rounding rule passed |
| Rendered pages, rows and local links | `node scripts/runtime-test.cjs` | **PASS** — 17 pages, 1,416 rendered rows each with an official link, no runtime errors |
| Privacy scan | `python3 integration/tools/privacy_scan.py` | **0 errors**; the only new warnings are the official CDI survey minimum $1,543, which is an official published amount and is in the ledger (INS-04) |

No name, street address, parcel number, account number or household figure was added. Every dollar amount added to the two new pages is either produced by the published model and rounded to $10 by `fmtMoney`, or an official amount published by a government body ($1,543, $1,044,586, $15,480,000, $20,000, $59.00).

## 4. What the two new pages add

- **`site/questions.html`** — 24 questions in four groups (title and trust; money and estate tax; numbers still guessed; household preferences), 10 answers that official sources do settle, a five-item readiness checklist that stores ticks only in the browser, and a sensitivity table showing what each open input moves in the 2045 comparison. Three items are marked blocking (A1, A2, B1) because no assumption can close them; 16 are open and five are household preferences.
- **`site/suggestions.html`** — 10 suggestions for the decision and 10 for improving the site, each with evidence, effort, expected effect, effect of skipping and a source link; three-way choice per row (do now / ask a professional / not now) stored in `localStorage` only; a record that can be copied or printed; no network calls.

Both pages are reachable from the navigation on every page and from two new cards on the landing page.

## 5. Confirmation

The published ranking is unchanged: for a 2045 inheritance held ten years, selling and reinvesting finishes ahead of renting by $1,729,720 and ahead of living in the house by $3,057,260. Every sensitivity tested on the new page (insurance at the survey high, rent ten per cent lower, home growth 2% or 6.7%, portfolio return 5%, upkeep 1%, tax 37%, the rate-book levy) keeps selling first.

## 6. Note on the concurrent merge

`main` moved to `ed9cbbd` while this session was working, carrying work from sessions `62b76b9d` and `6e6baf25`. Session `6e6baf25` had created `site/suggestions.html` at the same path with a privacy-path comparison, seven ranked improvements and seven questions. That page was merged in, not replaced: every one of its sections is still published, its wording on privacy and on the conditional recommendation was kept in `index.html` and `assets/app.js`, and its two High items remain at the top of `site/review.html`. This session's two suggestion registers, the three-way choice per row and the local-only decision record were added to it, and the link to the full 24-question register was added. The page now has five tables and 37 rows; `gate.cjs` reports 17 pages, 1,416 rows, 0 errors.
