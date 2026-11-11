# Decision audit — session 4e07c8e6

Date: 11 November 2026. Tree audited: `main` at `a6818a3` (after the two final-integration sessions merged), re-checked at `b9a10f6`.

This folder is repository-only; it is excluded from the published site. It holds no personal information. Every dollar figure is rounded to $10 or is an amount published by a government body.

## Result

**The published answer is confirmed: sell Property A soon after inheriting it, invest the proceeds, keep Property B.**

- A separately written calculation reproduces every headline number on the site to the nearest $10.
- Selling stays ahead when both choices are taxed the same way at the end, though by a third of the headline gap.
- The answer rests on two things that cannot be verified from here: that the trust is of a kind that resets the tax basis at death, and that home prices do not keep outrunning a mixed portfolio.

Seven points the site did not state were found. They are listed below and were added to the site under task X-7.

## 1. Independent recomputation

`recompute.py` rebuilds the three choices from the published inputs in `site/data/model.js`. It shares no code with the site. Run it with `python3 verification/4e07c8e6/recompute.py`; output is in `recompute.json`.

| Inheritance → endpoint | Choice | Site | This audit | Difference |
|---|---|---:|---:|---:|
| 2040 → 2050 | Sell and reinvest | $7,683,290 | $7,683,290 | 0 |
| 2040 → 2050 | Sell, all growth taxed at the end | $6,701,410 | $6,701,410 | 0 |
| 2040 → 2050 | Rent out, then sell | $6,249,830 | $6,249,830 | 0 |
| 2040 → 2050 | Live in, then sell | $5,135,780 | $5,135,780 | 0 |
| 2040 → 2050 | Live in, rent out the Property B unit | $5,530,560 | $5,530,150 | −$410 |
| 2045 → 2055 | Sell and reinvest | $9,125,340 | $9,125,340 | 0 |
| 2045 → 2055 | Sell, all growth taxed at the end | $7,959,170 | $7,959,170 | 0 |
| 2045 → 2055 | Rent out, then sell | $7,395,620 | $7,395,620 | 0 |
| 2045 → 2055 | Live in, then sell | $6,068,080 | $6,068,080 | 0 |
| 2045 → 2055 | Live in, rent out the Property B unit | $6,525,740 | $6,525,270 | −$470 |
| 2050 → 2060 | Sell and reinvest | $10,838,040 | $10,838,040 | 0 |
| 2050 → 2060 | Sell, all growth taxed at the end | $9,453,000 | $9,453,000 | 0 |
| 2050 → 2060 | Rent out, then sell | $8,752,170 | $8,752,170 | 0 |
| 2050 → 2060 | Live in, then sell | $7,164,510 | $7,164,510 | 0 |
| 2050 → 2060 | Live in, rent out the Property B unit | $7,695,070 | $7,694,520 | −$550 |

The only difference is in the last row of each group, about $400 to $550. Cause: the scenario engine grows the Property B unit rent at 1.62% a year (60% of 2.7%), while the model input is 1.6%. It is a labeling inconsistency of 0.02 points, not an error in the result.

The first-year figures also match: for a 2040 inheritance, property tax $61,420 if rented and $45,150 if lived in; cash left after tax from renting $8,360; yearly cost of living there $75,610.

The two published break-even rates were reproduced as well (2045 inheritance): home-price growth 7.81% a year and portfolio return 2.80% a year.

## 2. Does the ranking survive?

Each row changes one thing. "Sell" in this table is the middle case: the yearly tax drag is treated as tax already paid on income, and only the unrealised growth is taxed at the end. 2045 inheritance, 2055 endpoint.

| Test | Sell | Rent | Live | Live + B unit rented | Best |
|---|---:|---:|---:|---:|---|
| Site inputs, no change | $8,425,640 | $7,395,620 | $6,068,080 | $6,525,270 | Sell |
| A tax rate 1.1636% (sum of published components) instead of 1.2% | $8,425,640 | $7,415,780 | $6,090,840 | $6,548,030 | Sell |
| joint return: $500,000 home-sale exclusion | $8,425,640 | $7,395,620 | $6,150,830 | $6,608,020 | Sell |
| depreciation, building = 20% of value (assumption) | $8,425,640 | $7,387,300 | $6,068,080 | $6,525,270 | Sell |
| depreciation, building = 40% of value (assumption) | $8,425,640 | $7,366,500 | $6,068,080 | $6,525,270 | Sell |
| rent 25% above the HUD benchmark (assumption) | $8,425,640 | $7,683,220 | $6,068,080 | $6,525,270 | Sell |
| home prices +5.0% a year (assumption) | $11,074,730 | $10,318,880 | $8,961,460 | $9,418,650 | Sell |
| home prices +6.7% a year (recorded San Jose-area average 1976-2025), portfolio unchanged | $15,026,580 | $15,228,260 | $13,920,420 | $14,377,610 | Rent |
| portfolio +7.0% a year after tax (assumption) | $10,251,710 | $7,407,510 | $5,948,120 | $6,449,110 | Sell |
| portfolio +3.0% a year after tax (assumption) | $6,891,120 | $7,384,860 | $6,176,220 | $6,593,960 | Rent |
| no Prop 19 relief | $8,425,640 | $7,395,620 | $5,821,650 | $6,278,840 | Sell |

What the tests show:

- **Property tax rate, home-sale exclusion, depreciation, a higher rent:** none changes the ranking. Depreciation is close to neutral, because what is deducted during the rental is taxed again at sale at a higher rate.
- **Home prices at the recorded 1976–2025 pace (6.7% a year) with the portfolio left at 5%:** renting comes out ahead for a 2040 or 2045 inheritance. In the same recorded years a mixed portfolio also earned far more than 5%, so this row is a warning about the assumption, not a forecast.
- **Portfolio at 3% a year after tax:** renting comes out ahead. Putting the proceeds in low-yield savings loses the advantage of selling.

### Break-even rates on equal tax terms

The site's break-even cards compare a house that is sold and taxed at the end with a portfolio that is not. With the same treatment on both sides:

| Inheritance year | Home growth at which renting overtakes selling: as published | Same, portfolio growth also taxed | Portfolio return below which renting wins: as published | Same, portfolio growth also taxed |
|---|---:|---:|---:|---:|
| 2040 | 7.47% | 4.95% | 2.83% | 4.03% |
| 2045 | 7.81% | 5.32% | 2.80% | 3.98% |
| 2050 | 8.08% | 5.67% | 2.77% | 3.93% |

The recorded pace for the metro area is 6.7% a year over 1976–2025 and 4.1% over 2000–2025 ([FHFA index via FRED](https://fred.stlouisfed.org/series/ATNHPIUS41940Q)). The 50-year pace is above the equal-terms figure; the 25-year pace is below it.

### Random histories

The site's engine was re-run with five different random seeds, and with the recorded years used as they are instead of re-centred on the model's assumptions.

| Measure | Range over five seeds, three inheritance years |
|---|---|
| Selling finishes first, histories re-centred (as published) | 76% to 80% |
| Selling finishes first, histories as recorded | 78% to 82% |
| Selling beats renting with the portfolio also taxed at the end | 59% to 66% |

The published 78% / 76% / 77% is not an artifact of the seed or of the re-centring.

## 3. Legal mechanics

`LEDGER.md` lists 33 rules with the official page opened today and the wording found: 29 confirmed, 1 differs from the site, 3 left blank.

| Area | Checked against | Result |
|---|---|---|
| Federal threshold: $15,000,000 (2026), $15,480,000 (2027), 40% top rate, Form 706 timing, portability | [IRS](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax), [IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts), [estate FAQ](https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes) | Matches the site |
| No California or local estate, inheritance or gift tax | [State Controller](https://www.sco.ca.gov/ardtax_estate_tax.html), [Rev. & Tax. Code 13301](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=13301) | Matches the site |
| Prop 19 amount $1,044,586 and its one-year indexing | [BOE LTA 2025/009](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) | Matches the site; $1,022,600 × 1.0215 = $1,044,586 |
| Prop 19 formula, one-year move-in, two filings, loss on move-out | [BOE LTA 2026/026](https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf) | Matches the model's formula |
| Basis at death; revocable against irrevocable trust | [IRS FAQ](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances), [Rev. Rul. 2023-2](https://www.irs.gov/pub/irs-drop/rr-23-02.pdf) | Rule matches; trust type unknown (finding X-F2) |
| Capital gains, 3.8% tax, home-sale exclusion | IRS Topics [409](https://www.irs.gov/taxtopics/tc409), [559](https://www.irs.gov/taxtopics/tc559), [701](https://www.irs.gov/taxtopics/tc701) | Matches the site |
| California tax on gains | [FTB](https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html), [2025 schedules](https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf) | **Differs:** the site uses 9.3%; a gain above $1,000,000 in one year reaches 10.3%–12.3%. Lowers rent and live slightly; sell unchanged |
| Trust notice in 60 days; assessor statement in 150 days | [Probate Code 16061.7](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=16061.7), [Rev. & Tax. Code 480](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480) | Matches the site |
| San Francisco rate 1.18162182% for 2026-27 | [SF Treasurer](https://sftreasurer.org/property/secured-property-taxes) | Matches the model input |

## 4. Findings

| ID | Finding | Effect | Official source | Where it was added |
|---|---|---|---|---|
| X-F1 | Break-even rates were published on unequal tax terms (7.8% and 2.8%); on equal terms they are about 5.3% and 4.0% | The choice is closer than the cards suggested. Selling still leads in the base case | [FHFA via FRED](https://fred.stlouisfed.org/series/ATNHPIUS41940Q) | Best plan, Flagged for Review |
| X-F2 | The tax basis resets at death for a revocable trust, not for an irrevocable trust left out of the estate | If the trust is the second kind, a sale at inheritance is taxed on the gain since purchase. Trust type unknown | [IRS Rev. Rul. 2023-2](https://www.irs.gov/pub/irs-drop/rr-23-02.pdf) | Best plan, Inheritance steps, Flagged for Review (High) |
| X-F3 | Prop 19 relief needs the house to count as the parent's home at death; in a care facility it must not be rented outside the immediate family; an LLC never qualifies | Live-in plans only | [BOE LTA 2026/026](https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf) | Best plan, Inheritance steps, Flagged for Review |
| X-F4 | San Francisco Measure H, a yearly parcel tax for Muni, passed in the preliminary count of 3 Nov 2026 (74.4% yes) | New fixed cost for Property B. Amount for its parcel type **not confirmed, left blank** | [SF Department of Elections](https://www.sfelections.org/results/20261103/index.html) | Landing page law watch, San Francisco page, Flagged for Review |
| X-F5 | A house an estate holds for sale is investment property, so sale costs can be a deductible loss; not after rent-free family use | Favors selling without moving in. Up to about $118,360 of tax value for a 2045 inheritance if fully usable; not counted in any result. IRS text is about estates, so flagged | [IRS Publication 559](https://www.irs.gov/publications/p559) | Best plan steps, Flagged for Review |
| X-F6 | The model sells on the day of inheritance; holding costs until closing are not counted | About $9,090 a month for a 2045 inheritance. Does not change the ranking | [BOE Prop 19](https://www.boe.ca.gov/prop19/) | Best plan steps, Flagged for Review |
| X-F7 | Room under the federal threshold was shown only in future dollars | Held today and growing 5% a year unspent, about $7,579,590 fills the room by 2040, $6,390,900 by 2045, $5,374,120 by 2050 | [IRS IR-2026-133](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) | Estate tax page |

## 5. Not confirmed, left blank

| Item | Why | Official route |
|---|---|---|
| Measure H amount for a three-unit parcel, first tax year, tenant pass-through | Only the results page was opened; the measure text was not | [SF Department of Elections](https://www.sfelections.org/results/20261103/index.html) |
| Residential rental recovery period of 27.5 years | Publication 527 not opened in this session; used only as an assumption in the depreciation test | [IRS Publication 527](https://www.irs.gov/publications/p527) |
| Whether the estate rule in Publication 559 applies to a sale by the trustee of this trust | The publication is written for estates | [IRS Publication 559](https://www.irs.gov/publications/p559) |
| State ballot results of 3 Nov 2026 | Read from news reports only in this session; the site cites the Secretary of State | [Secretary of State](https://electionresults.sos.ca.gov/returns/ballot-measures) |

## 6. Checks run on the edited tree

| Check | Result |
|---|---|
| `node scripts/validate.js` | PASS, 846 checks, 14 pages, 124 sources |
| `node scripts/stress-test.js` | PASS |
| `python3 scripts/package-site.py` | PASS, rounding rule |
| `python3 scripts/check-publication.py --self-test` | PASS, 26 reviewed public files |
| `node scripts/runtime-test.cjs` | PASS, 14 pages, 1,144 rows each with an https link, no runtime errors, no broken local links |
| `node qa/tools/gate.cjs` | PASS, 0 errors, 0 warnings |

## 7. Limits of this audit

- Insurance, water, electricity and maintenance figures were not re-researched; session `aa1f073e` owns them.
- The household's own inputs (values, rents, bills) cannot be verified from official sources and were taken as published.
- Official pages were read through a page-fetch tool. Long documents were read in part; the ledger records what was read.
- The middle "sell" case in section 2 assumes three points of the 6% gross return are income taxed each year. That split is an assumption.
