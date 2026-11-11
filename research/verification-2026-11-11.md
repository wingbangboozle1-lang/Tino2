# Re-verification log — session 70f163d0 (2026-11-11)

Rule applied: a value is "verified" only if read on an official page in this session. Everything else stays flagged. Household amounts are not verifiable from public sources and are published rounded to $10.

## Verified this session (official page read 2026-11-11)

| Item | Value | Official source | Result |
| --- | --- | --- | --- |
| Federal basic exclusion 2026 | $15,000,000 per decedent (P.L. 119-21) | https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax | Confirmed |
| California estate tax | No return for deaths on/after 2005-01-01 | https://www.sco.ca.gov/ardtax_estate_tax.html | Confirmed |
| Prop 19 value cap, 2025-02-16 to 2027-02-15 | $1,044,586 (from $1,022,600); next adjustment 2027-02-16; indexed to FHFA California HPI | https://www.boe.ca.gov/news/2025/nr-25-02.htm | Confirmed. Earlier note that only secondary sources confirmed this is now resolved |
| Prop 19 formula, trust rule, continual use | Excluded amount = factored base-year value + cap; trust vesting at death is the change in ownership; homeowners' exemption within 1 year | https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf and https://www.boe.ca.gov/prop19/ | Confirmed (LTA 2026/026 dated 2026-08-03) |
| HUD FY2026 SAFMR 95014 | 3BR $5,870; 4BR $6,390 (also 2BR $4,440) | https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026 | Confirmed; matches model |
| HUD FY2026 SAFMR 94122 | 1BR $2,730; 2BR $3,310 | https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=94122&year=2026 | Confirmed; matches model |
| SF allowable rent increase | 1.6% (2026-03-01 to 2027-02-28), based on 60% of Bay Area CPI-U | https://www.sf.gov/reports/march-2023/learn-about-rent-increases-san-francisco | Confirmed |
| SF Rent Board fee 2026-27 | $59.00 per dwelling unit; 50% recoverable from tenants | https://www.sf.gov/rent-board-fee | Confirmed; model's two-unit $118 matches |
| SF pending law | File No. 261020 would cap banked + capital-improvement increases at 10%/yr; not enacted | https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit | Watchlist item added |
| CA Nov 3, 2026 ballot (unofficial results, certification due 2026-12-11) | Prop 40 failing, Prop 42 passing, Prop 43 failing | https://electionresults.sos.ca.gov/returns/ballot-measures; guides https://voterguide.sos.ca.gov/propositions/40/ , /42/ , /43/ | Recorded as unofficial |
| FRED series (7) | CPIAUCNS, ATNHPIUS41940Q, ATNHPIUS41884Q, CASTHPI, GS10, MORTGAGE30US, SPASTT01USM661N, annual, through 2025 | https://fred.stlouisfed.org (graph CSV exports) | All 7 re-read in full this session and compared to `research/data/fred_annual_2026-11-11.csv`; no differences |
| CBO Feb 2026 outlook | Deficit 5.8% of GDP 2026, debt 101% -> 120% of GDP by 2036; PCE inflation ~2% from 2030; 10-yr yield rises gradually then stable | https://www.cbo.gov/publication/61882 | Confirmed qualitatively |

## Not verified — remain flagged

| Item | Why |
| --- | --- |
| CBO CPI 2.3% and 10-yr 4.4% | Read from secondary summaries (CRFB, AAF); cbo.gov page confirms direction only |
| SF max annual increase 7% ceiling | Rent Ordinance detail not read on an official page; used as a cap in the scenario engine |
| SF FY2026-27 combined rate 1.18162182% | Cited from the Board of Supervisors minutes; page 1 of 9 of the minutes read, rate table not reached. Earlier sessions recorded 1.18268325% for FY2025-26: discrepancy is consistent with a year-on-year change but should be confirmed |
| Insurance (both properties) | Statewide averages only; no parcel quote |
| Household inputs (values, rents, bills, assessments) | Private; unverifiable by design |
| Dividend add-on 2.0 points, 60/40 mix, 1-pt tax drag | Model assumptions |
| Save Prop 13 / HJTA measure | Secondary sources conflict: one says it qualified for Nov 2026; the official results list Prop 43 (legislature's alternative), so the HJTA measure appears withdrawn. Not verified on an official page |

## Irregularities found

1. **Privacy**: before this session the repo (public) contained the exact household tax and assessment history and exact derived rates in model.js, validate.js and several pages. Current tree rounded to $10; **git history is unchanged** (flag: High, see review page).
2. **Model inconsistency**: Prop 19 cap was indexed at 2% every two years, contrary to BOE's FHFA-HPI method. Corrected.
3. **Tax asymmetry**: sell-and-reinvest ignored tax on portfolio growth while rent/live paid capital-gain tax at the endpoint. Both figures now published; the sell lead narrows from about $1.5M to about $0.5M in the base case and reverses in inflation-led scenarios.
4. **Derived tax ratios** (about 1.34% for A, 2.14% for B) are not official tax rates; the B ratio exceeds the SF ad valorem rate (about 1.18%). Flagged already; recomputed from rounded inputs.
5. **Layer sprawl**: the repository has five independently built site layers (root, site/, pages/, dashboard/, docs) with different appreciation assumptions (3.0–4.0%). Not consolidated here; README names `site/` as canonical.
6. PR #3 remains open from an earlier session and was not touched.
