# Verification report — session `f1a2647b`, 15 November 2026

Scope: every official source this session opened, and every model or page claim it changed.
Each item was opened on 15 November 2026, in this workspace, at the URL listed, and the passage
the guide attributes to it was read on the page itself. Nothing was taken from memory or from a
secondary site. Where an official page did not answer the question, the guide leaves the cell
blank and the item is recorded here as unverified.

A note on what is new in this session: five standing suggestions (S19, S20, S21, S23, S26) were
implemented, so most rows below are the sources that made those changes possible, plus two new
sections on the Real conditions page that are computed from official series.

## 1. Sources opened, line by line

| # | Claim as published | Official page opened 15 Nov 2026 | Passage read | Verdict |
|---|---|---|---|---|
| 1 | The documentary transfer tax does **not** apply to a transfer of realty by reason of the death of any person, outright or in trust for the benefit of any person or entity (Taxes page, Attorney & CPA sheet). | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=11930. | R&T Code §11930: "Any tax imposed pursuant to this part shall not apply to any deed, instrument, or other writing which purports to grant, assign, transfer, convey, divide, allocate, or vest lands, tenements, or realty, or any interest therein, if by reason of such inter vivos gift or **by reason of the death of any person**, such lands, tenements, realty, or interests therein are transferred outright to, or in trust for the benefit of, any person or entity." (Added by Stats. 1996, Ch. 862.) | **Match.** Closes the question prior sessions left open ("not assumed to apply to a transfer at death until an exemption is cited"). The guide now states the statute, keeps the county's requirement that the exemption be cited on the document, and charges the tax on a later sale only. |
| 2 | The county rate is 55 cents per $500, or $110 per $100,000 (0.11%), and a city add-on exists by ordinance (unchanged from prior sessions; re-read for the sell-path change). | https://clerkrecorder.santaclaracounty.gov/recording-documents/recording-real-estate | "computed at a rate of $.55 per $500 or fractional portion of real property value, excluding any liens or encumbrances already of record" | **Match**, unchanged. The 0.11% is now an input to the sale cost rather than a display row only. |
| 3 | California has no lower rate for capital gains; all capital gains are taxed as ordinary income. | https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html | "California does not have a lower rate for capital gains. All capital gains are taxed as ordinary income." | **Match.** |
| 4 | The same rule, in the instructions that implement it. | https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html | Schedule CA (540), line 7a: "California taxes long and short term capital gains as regular income. No special rate for long term capital gains exists." | **Match.** Two official statements were read rather than one. |
| 5 | The 1% tax on taxable income above $1,000,000 is called the **Behavioral Health Services Tax** on the 2025 Form 540 instructions, line 62. | https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html | "Line 62 – Behavioral Health Services Tax. If your taxable income is more than $1,000,000, compute the Behavioral Health Services Tax using whole dollars only: 1. Taxable income from Form 540, line 19. 2. Less: $(1,000,000). 3. Subtotal. 4. Tax rate – 1%: .01. 5. Behavioral Health Services Tax – Multiply line 3 by line 4." | **Match, and a correction.** The guide previously called this the "mental health services tax" and listed it as taken from secondary sources (`FLAGGED_ADDITIONS` in `scripts/analysis_pages.py`). The name on the current instructions is Behavioral Health Services Tax; the flagged row is closed and the name is stated. |
| 6 | The combined top marginal rate on a large gain is 37.1% (20% federal + 3.8% net investment income tax + 12.3% California + 1%). | https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf and the FTB pages in rows 3–5 | Top California rate 12.30% (schedules X/Y/Z), plus the 1% in row 5. | **Computed, not quoted**: the sum is arithmetic on four published rates, and the page says so and calls it a top marginal rate, not an average. The published range is stated as 23.8%–37.1%. |
| 7 | The Proposition 19 allowance is adjusted every other 16 February, beginning 2023, by the change in the FHFA House Price Index for California for the prior calendar year; the 2024 change was 2.15% and the resulting amount is $1,044,586. | https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf | Letter To Assessors 2025/009: "Section 2.1(c)(4) provides that the $1 million amount is to be adjusted every other year, beginning in February 2023… to adjust the one million dollar ($1,000,000) amount… for inflation to reflect the percentage change in the House Price Index for California for the prior calendar year, as determined by the Federal Housing Finance Agency. On February 25, 2025, the Federal Housing Finance Agency (FHFA) announced that the annual percentage change in the House Price Index for California for 2024 was 2.15 percent. Accordingly, the $1 million amount is adjusted to **$1,044,586.**" The letter also tabulates $1,000,000 (16 Feb 2021 – 15 Feb 2023) and $1,022,600 (16 Feb 2023 – 15 Feb 2025). | **Match.** The allowance is now carried forward biennially on that method (S23). The two projected amounts the guide publishes ($1,067,050 for 2027, $1,292,200 for 2045) are ledgered as **explicitly unverified**, because the Board has not published them. |
| 8 | The California house-price index series the Board's method points to. | https://fred.stlouisfed.org/series/CASTHPI | Series page opens as an FHFA all-transactions house price index for California. | **Cited as the series, not as a value.** No future value of the series is published. |
| 9 | Proposition H: first tax on FY 2027–28 bills, inflation adjustment from FY 2028–29, term 1 July 2027 to 30 June 2042, multifamily floor $249 up to 5,000 sq ft, renter pass-through capped at 50% of the tax and $65 a unit a year, applications due 1 June. | https://www.sfmta.com/getting-around/muni/parcel | "San Francisco voters approved Proposition H on November 3, 2026… The first tax will appear on your fiscal year 2027–28 property tax bill, which is mailed in fall 2027." "**How long**: July 1, 2027 through June 30, 2042." "**Annual adjustment**: Amounts rise with inflation starting in fiscal year 2028–29." "Multifamily residential … Up to 5,000 sq ft … $249." "Information for renters: … the pass-through is limited to 50% of the tax, up to $65 per unit per year. It does not apply if the unit is exempt from the tax, or if your base rent was set on or after June 1, 2027." "You must apply on or by June 1 for the upcoming tax bill exemption." | **Match on every element.** The model now applies the official terms (S21). Two things are stated as assumptions, not as official figures: the inflation index (not named on the page) and B's amount (parcel type and building area are not public facts). |
| 10 | The property-tax rate follows the tax rate area; the rate is the 1% maximum levy plus voter-approved bonded indebtedness; there are 816 tax rate areas in FY 2025-26; the first two digits identify the city or unincorporated area. | https://files.santaclaracounty.gov/exjcpb1531/2025-11/tax-rate-book-2025-2026.pdf (linked from https://controller.santaclaracounty.gov/property-tax-distribution/property-tax-rate-book) | "Tax Charge — By law the tax rate is limited to 1% of the assessed value plus amounts required for the payment of principal and interest on voter approved bond indebtedness." "Tax Rate Areas — The County is divided into tax rate areas… The first two digits of each tax rate area identify the area in which the property is located… Total number of Tax Rate Areas in Fiscal Year 2025-26 is 816." Summary table: "1% Maximum Tax Levy 1.00000", "County Retirement Levy 0.03880", "County Library 0.00240". | **Match.** Property A's own rate stays **blank**: no parcel number is published here, and a rate cannot be read without one. The procedure is published instead, and the item is on the Flagged page (S32). |
| 11 | The federal home-sale exclusion tests: owned for at least 24 months of the 5 years before the sale, used as a residence for at least 24 months of the previous 5 years, both within the 5-year period ending on the sale date. | https://www.irs.gov/taxtopics/tc701 | "If you or your spouse owned the home for at least 24 months (2 years) out of the last 5 years leading up to the date of the sale, you meet the ownership test. If you and your spouse used the home as a residence for at least 24 months (2 years) of the previous 5 years, you meet the use test… you must meet both tests during the 5-year period ending on the date of the sale." | **Match.** The exclusion is now applied to the living-then-sell paths (S20). |
| 12 | The share price index used for the decade table is a price index published by the OECD and redistributed by FRED. | https://fred.stlouisfed.org/series/SPASTT01USM661N | "Financial Market: Share Prices for United States… Source: Organization for Economic Co-operation and Development… Units: Index 2015=100, Not Seasonally Adjusted." | **Match.** The guide states that the index is **price only** and excludes dividends, so it understates what an investor earned. |
| 13 | The decade table's other series. | https://fred.stlouisfed.org/series/CPIAUCNS · https://fred.stlouisfed.org/series/ATNHPIUS41940Q · https://fred.stlouisfed.org/series/GS10 | Series pages opened; no individual observation is quoted on the guide, only statistics computed from the committed extract. | **Cited as series.** |

## 2. What the decade table is, and how it is checked

The "What each decade actually did" table on the Real conditions page is **computed on every
build** from `research/data/fred_annual_2026-11-11.csv`, a committed extract of annual averages of
the three series above plus the 10-year Treasury rate. No decade figure is typed into the
generator, so a number cannot drift from the series it came from. The arithmetic:

- average annual inflation = the mean of the year-on-year changes in the annual CPI-U average;
- house prices = a compound annual growth rate between the first and last published year of the
  decade for the San Jose metropolitan area index;
- share prices = the mean of the year-on-year changes in the annual average of the index;
- the Treasury column = the mean of the annual averages of the 10-year constant-maturity rate.

The 1970s house-price cell is **blank**, because the index begins in 1976 and the guide does not
fill a gap it cannot compute. The 2020s row covers 2020 to 2025 only.

The regime replay below it runs the same engine at a 25-year horizon with each decade's own
growth, inflation and share-price rates held flat. Every row is labelled a model output on the
household's rounded inputs, not an official figure, and the 1970s row is not run at all for the
reason above.

## 3. Model changes, and whether the recommendation moved

| Change | Where | Effect on the ranking |
|---|---|---|
| Imputed rent for the living paths, set to the same published benchmark the letting path uses (S19) | `scripts/analysis_model.py`, `guide/data/model.js`; new control on the What-if page | The living paths were previously credited nothing, which biased the comparison toward selling. At 25 years in the baseline the live path moves from about $16.04m to about $23.33m. The **winner does not change** — selling still leads at 10, 25 and 50 years in the baseline — but the closest rival changes from "rent it out" to "live two years, then sell and phase". |
| Primary-residence exclusion switched on for living-then-sell paths, at the $250,000 single-filer amount (S20) | `scripts/analysis_model.py` | Applied only where the household occupies the home for at least 24 of the 5 years ending on the sale. Small effect, in the same direction. |
| Proposition H on its official terms (S21) | `scripts/analysis_model.py`, `guide/data/model.js` | Property B's cost line is now higher from 2028 and stops in 2042, instead of a flat amount forever. |
| Proposition 19 allowance carried forward on the Board's biennial HPI method (S23) | `scripts/analysis_model.py`, `guide/data/model.js` | The allowance at a 2045 transfer rises from $1,044,586 to about $1,292,200, which slightly reduces the reassessed base on the living path. |
| Documentary transfer tax priced into a later sale, and nothing at the inheritance transfer (S26) | `scripts/analysis_model.py` | Reduces the sell paths by 0.11% of the sale price; a small change in the same direction as negotiated sale costs. |
| California gain rate raised from 12.3% to 13.3%, and the public combined rate from 36.1% to 37.1% | `guide/data/model.js`, `scripts/analysis_model.py` | Reduces the sell and mixed paths slightly. |

Break-even points after the changes, on the household's rounded inputs, baseline: the monthly rent
at which living equals selling and phasing is about **$7,540 at 10 years** and about **$11,330 at
25 years**; home-price growth **5.81%** a year at 25 years; equity return **4.90%** a year at 25
years. The published break-even table is generated from the same functions, so it cannot disagree
with the model.

## 4. Tests run after the changes

| Check | Result |
|---|---|
| `python3 scripts/check-generated.py` | PASS — 18 generated public pages are up to date |
| `python3 scripts/check-figures.py` | PASS — 41 ledger records, 39 verified, 2 explicitly unverified |
| `python3 scripts/test-model-reference.py` | PASS — 108 decision configurations, 250 stress years, 1,500 phased-investment years, 20,736 unrounded comparisons |
| `python3 scripts/package-site.py` | PASS — 32 reviewed guide files; legacy site excluded |
| `python3 scripts/check-publication.py --directory _public` | PASS |
| `python3 scripts/privacy-gate.py` | PASS — 232 tracked text files |
| `node scripts/test-guide.cjs` | PASS — 18 rendered pages, 1,089 source-linked table rows, 12,758 checks |
| `node scripts/privacy-audit.cjs` | PASS — no raw pre-rounding household token, ZIP code or identifier in the packaged artifact |
| `node scripts/validate.js` (retained dashboard, never published) | PASS — 1,613 checks, 19 pages, 178 official sources |
| `node scripts/stress-test.js` | PASS |

`node scripts/test-browser.cjs` cannot run in this sandbox (missing `libnss3`); it runs in CI.

## 5. Irregularities and limits found

1. **The inflation index for Proposition H is not named on the SFMTA page.** The page says amounts
   "rise with inflation" from FY 2028–29 and does not say which measure. The model uses 2% and the
   guide states that it is an assumption. Flagged.
2. **Property A's tax rate area remains blank.** The county publishes 816 rates, but the rate
   follows the parcel and the parcel number is not published here. Inferring a rate from a city or
   county average would be an invention, so the cell is blank and the procedure is published
   (S32).
3. **The share-price series is price-only.** It excludes dividends, so the decade table understates
   what an investor earned in every decade. Stated on the page rather than adjusted.
4. **The regime replay holds one decade's rates flat for 25 years**, which no decade in the record
   did. It is a stress test of the assumption, not a forecast, and the page says so.
5. **The 1970s row is not run** in either new table, because the house-price index begins in 1976.
   The cell is left blank rather than back-filled.
6. **Git history was not rewritten.** The owner's brief repeats the request. It is still not done
   here, for the reasons in `COORDINATION.md`: it would force-push roughly 70 remote branches that
   other sessions own, and it cannot reach copies outside GitHub. Repository visibility was also
   not changed, because on a free plan making the repository private would take the Pages site
   down; that is an owner decision (S25), and the runbook is on the Flagged page.
7. **`scripts/runtime-test.cjs` is stale** (pre-existing): it scans `_public/site`, which the
   publisher has not produced since the guide replaced the legacy dashboard. Not repaired here; it
   belongs to the retained dashboard and is not part of CI.
