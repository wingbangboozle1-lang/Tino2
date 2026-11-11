# Session `d9c69069` — independent verification report

**Date:** 2026-11-11 (all access dates are 2026-11-11 UTC)
**Branch:** `arena/d9c69069-tino2`
**Tree verified:** `main` at `660be98` (PR #20, session `11bffb54`, merged 07:49:54 UTC), merged into this branch.
**Role:** read-only independent auditor. This report is the only substantive file this session adds. No file owned by another session was edited; corrections that belong in someone else's file are logged as requests in `COORDINATION.md`.

**Privacy statement.** No personal name, street address, parcel number, account number or contact detail appears in this report. Properties are "Property A" (Cupertino 95014) and "Property B" (San Francisco 94122). Household figures quoted here are already the $10-rounded values the site publishes; no exact household amount is reproduced.

---

## 1. Automated suite re-run on the merged tree

| Check | Command | Result |
|---|---|---|
| Model, syntax, link and source validation | `node scripts/validate.js` | PASS — 737 checks, 13 pages, 100 official sources |
| 50-year stress paths, estate ownership, real-dollar tests | `node scripts/stress-test.js` | PASS |
| Rendered-page gate (JSDOM): rows, source links, dollar rounding, links | `node qa/tools/gate.cjs` | PASS — 13 rendered pages, 963 table rows (951 with their own official link, 12 calculated rows with a context link), 4,194 dollar amounts (54 official exact figures), 254 internal + 1,376 external links, 0 errors, 0 warnings |
| Publication allowlist packaging | `python3 scripts/package-site.py` | PASS |
| Internal links across the whole repository | `python3 src/check_links.py .` | 58 pages, 871 table rows, 124 distinct external links, 0 errors |
| Privacy scanner | `python3 integration/tools/privacy_scan.py` | 0 errors, 102 warnings — see §4 |

`qa/tools/gate.cjs` needs the optional dev dependency `jsdom`, installed outside the repository
(`npm install --prefix .cache/test jsdom`); `.cache/` is gitignored, so the repository stays dependency-free.

Base case reproduced by the model on the merged tree (2040 inheritance, 2050 endpoint):
sell **$7,683,290** · rent **$6,249,830** · live **$5,135,780**.

---

## 2. Independent re-verification against official sources

Every page below was **opened and read by this session on 2026-11-11**, directly (not through a search
result or another session's file). "Wording found" is quoted from the official page.

| # | Figure as published on the site | Result | Wording found on the official page | Official source |
|---|---|---|---|---|
| 1 | Federal basic exclusion for deaths in 2026 = $15,000,000 | **Match** | "WFTC amends § 2010(c)(3) by increasing the basic exclusion amount to $15,000,000 for calendar year 2026." | [IRS — What's new, estate and gift tax](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax) |
| 2 | Federal basic exclusion for deaths in 2027 = $15,480,000 | **Match** | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026." | [IRS IR-2026-133 (5 Nov 2026)](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) |
| 3 | Annual gift exclusion $19,000 (2026) / $20,000 (2027); non-citizen spouse $194,000 / $201,000 | **Match** | "For calendar year 2027, the annual exclusion for gifts increases to $20,000, up from $19,000 for calendar year 2026 … to a spouse who is not a citizen … increases to $201,000 … up from $194,000." | [IRS IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) |
| 4 | No California estate-tax return for deaths on/after 1 Jan 2005 | **Match** | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return." | [State Controller — California Estate Tax](https://www.sco.ca.gov/ardtax_estate_tax.html) |
| 5 | Prop 19 requires the home to be the principal residence of transferor **and** transferee; homeowners' exemption within 1 year; claim within 3 years or before transfer to a third party; no exclusion for other real property | **Match** | Comparison chart, "Proposition 19 (Current Law)" column: "Principal residence of transferor and transferee … File for homeowners' exemption within 1 year of transfer — File claim for exclusion within 3 years or before transfer to third party … Eliminates exclusion for other real property other than the principal residence" | [BOE — Proposition 19](https://boe.ca.gov/prop19/) |
| 6 | Prop 19 adjusted $1 million amount = $1,044,586 for transfers 16 Feb 2025 – 15 Feb 2027; next adjustment Feb 2027 | **Match** | "the $1 million amount is adjusted to **$1,044,586** … for transfers that occur February 16, 2025 through February 15, 2027 … The next adjustment of the $1 million amount will occur in February 2027." | [BOE LTA 2025/009 (PDF)](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) |
| 7 | Prop 19 amount is indexed to the FHFA California house-price index for the prior calendar year (2024: 2.15%) | **Match** | "adjust the one million dollar ($1,000,000) amount … for inflation to reflect the percentage change in the House Price Index for California for the prior calendar year, as determined by the Federal Housing Finance Agency … the annual percentage change … for 2024 was 2.15 percent." | [BOE LTA 2025/009 (PDF)](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) |
| 8 | Prop 13 inflation factor: lesser of California CPI or 2%; 2026-27 factor 1.02 (CCPI +3.307%) | **Match** | "please prepare your **2026** assessment roll using an inflation factor of **1.02**"; table row "2026-27 \| 3.307 \| 2% \| 1.02" | [BOE LTA 2026/002 (PDF)](https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf) |
| 9 | Trustee notification due within 60 days of death | **Match** | §16061.7(f): "The notification by trustee shall be served not later than 60 days following the occurrence of the event requiring service of the notification by trustee" | [Probate Code §16061.7](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=16061.7) |
| 10 | Change-in-ownership statement for property held in trust due within 150 days of death | **Match** | §480(b): "including a transfer through the medium of a trust, the change in ownership statement or statements shall be filed by the trustee (if the property was held in trust) or the transferee … within 150 days after the date of death." | [Revenue & Taxation Code §480](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480) |
| 11 | San Francisco secured property tax rate FY 2026-27 = 1.18162182% | **Match** | "The secured property tax rate for Fiscal Year 2026-27 is 1.18162182%." | [SF Treasurer & Tax Collector](https://sftreasurer.org/property/secured-property-taxes) |
| 12 | SF flat parcel charges FY 2025-26: School Parcel Tax of 2020 $334.38; SFUSD Teacher Support $319.34; SFUSD Facilities $21.50 per unit (multi-family); City College $99; Bay Restoration $12 | **Match** (all five) | "$334.38 parcel tax in FY 2025–26 and adjusted for inflation annually"; "$319.34 parcel tax in FY 2025-26"; "$21.50 per dwelling unit on multi-family residential parcels in FY 2025-26"; "$99 per year and adjusted for inflation annually"; "$12 per year" | [SF Treasurer — Parcel Taxes](https://sftreasurer.org/property/parcel-tax-exemptions-and-special-assessments) |
| 13 | SF allowable rent increase 1.6% (1 Mar 2026 – 28 Feb 2027); 1.4% (2025-26); 1.7% (2024-25) | **Match** (by direct fetch; session `11bffb54` had it via a search result) | Table "Allowable rent increase": "March 1, 2026 – February 28, 2027 \| 1.6%" | [SF Rent Board — Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |
| 14 | Owner move-in relocation: $8,245 per tenant, max $24,733 per unit, plus $5,497 for each elderly/disabled tenant or household with minor children | **Match** (all three, to the cent) | Table row "3/01/26 – 2/28/27 \| $8,245.00 \| $24,733.00 \| $5,497.00" | [SF Rent Board — Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |
| 15 | Board of Supervisors File No. 261020 is **pending, not enacted**: would cap combined banked + capital-improvement increases at 10%/year for increases noticed or petitions filed on/after 15 Sep 2026 | **Match** | "**This legislation has not been enacted and is subject to change.**" | [SF Rent Board — Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) |
| 16 | SF Rent Board fee $59.00 per dwelling unit for 2026-27, due 1 March; paid directly by owners since 2022 | **Match** | "For the 2026-2027 tax year, the fee is: **$59.00 per dwelling unit**"; "owners must pay this fee to the Rent Board directly as of 2022"; "Deadline: **March 1**" | [SF.gov — The Rent Board Fee](https://www.sf.gov/rent-board-fee) |
| 17 | Cupertino water: quantity rate and service charge up about 2.8% from 1 Jan 2026, plus a Valley Water wholesale increase from 1 Jul 2026 | **Match** | "Year 2 of our 2025-27 GRC Filing shows an increase in the quantity rate and service charge of approximately 2.8%, effective January 1"; "Valley Water … is increasing its water rates effective July 1, 2026." | [San Jose Water — 2026 Rates](https://www.sjwater.com/2026Rates) |
| 18 | HUD FY2026 Small Area FMR, ZIP 95014: 4-bedroom $6,390; 3-bedroom $5,870 | **Match** | "Efficiency $3,340 \| One-Bedroom $3,800 \| Two-Bedroom $4,440 \| Three-Bedroom $5,870 \| Four-Bedroom $6,390" | [HUD FY2026 SAFMR calculation, 95014](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026) |

**Not re-opened by this session** (status is the one given by the session that added it; no claim is made here):
SFPUC proposed water/sewer rates, Santa Clara County tax-rate book components, HUD SAFMR for ZIP 94122,
CDI statewide residential insurance experience, IRC §1014 / §121 / §1411 / Form 706 pages, and the
California Secretary of State ballot-measure returns. Two of these were attempted and are recorded in §5.
