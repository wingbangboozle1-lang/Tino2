# Black swan economic scenarios — research note

Session 70f163d0 · 2026-11-11 · generated from `site/data/history-engine.js` (values rounded to $10; household amounts anonymised).

**Status:** scenarios are stress tests, not forecasts. "Replay" scenarios use recorded official data; "Assumption" scenarios are invented and flagged.

## 1. Baselines and where they come from

| Item | Baseline used | Recorded history | Official source |
| --- | --- | --- | --- |
| CPI-U inflation, 1976–2025 (annualized) | 2.3% | 3.6% | https://fred.stlouisfed.org/series/CPIAUCNS |
| CPI-U inflation, 1972–1982 (annualized) | — | 8.7% | https://fred.stlouisfed.org/series/CPIAUCNS |
| CPI-U inflation, 2020–2025 (annualized) | — | 4.5% | https://fred.stlouisfed.org/series/CPIAUCNS |
| San Jose-area home prices, 1976–2025 (annualized) | 3.5% | 6.7% | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| San Francisco-area home prices, 1976–2025 (annualized) | 3.5% | 6.5% | https://fred.stlouisfed.org/series/ATNHPIUS41884Q |
| California home prices, 1975–2025 (annualized) | — | 6.3% | https://fred.stlouisfed.org/series/CASTHPI |
| San Jose-area home prices, 2019–2025 (annualized) | 3.5% | 5.1% | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| San Jose-area home prices, 2024→2025 | — | 0.3% | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| San Jose-area home prices, 2006→2011 (peak to trough, year-end) | — | -26.0% | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| California home prices, 2006→2011 | — | -40.0% | https://fred.stlouisfed.org/series/CASTHPI |
| San Jose-area home prices, 1989→1994 | — | -12.5% | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| US share-price index (price only), 1976–2025 (annualized) | — | 7.6% | https://fred.stlouisfed.org/series/SPASTT01USM661N |
| US share-price index, 2007→2008 | — | -43.7% | https://fred.stlouisfed.org/series/SPASTT01USM661N |
| US share-price index, 2000→2002 | — | -25.6% | https://fred.stlouisfed.org/series/SPASTT01USM661N |
| US share-price index, 1972→1974 | — | -44.9% | https://fred.stlouisfed.org/series/SPASTT01USM661N |
| US share-price index, 1972–1982 (annualized) | — | 2.3% | https://fred.stlouisfed.org/series/SPASTT01USM661N |
| CBO long-run CPI / 10-yr yield | 2.3% / 4.5% | — | https://www.cbo.gov/publication/61882 (exact 2.3% / 4.4% read from secondary summaries — **unverified**) |

## 2. Scenario catalogue

| Scenario | Type | Construction | Source |
| --- | --- | --- | --- |
| Smooth baseline | Baseline | Same constant rates as the Decision lab. Home +3.5%/yr · CPI 2.3% · costs/rent CPI+0.7 pt · equities 7.0% · 10-yr 4.5% | https://www.cbo.gov/publication/61882 |
| Replay of the last 49 years | Official-data replay | 1977–2025 annual data replayed in order from 2027 (then baseline for 2076). San Jose-area home prices, CPI, Treasury yields and equity price index (+2.0 pt dividend assumption) exactly as recorded | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| 1970s-style stagflation | Official-data replay | 1973–1982 CPI, yields and equity prices; home prices from FHFA California index (1976+), CPI before that. Replayed annually | https://fred.stlouisfed.org/series/CPIAUCNS |
| 2008-style housing and equity crash | Official-data replay | 2006–2012 CPI, yields, equities, San Jose-area home prices. San Jose-area index fell about 26% 2006→2011; California index about 40%; US share-price index fell about 44% in 2008 | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| Early-1990s Bay Area bust | Official-data replay | 1990–1996 data. San Jose-area index fell about 12.5% 1989→1994 while CPI rose about 3–4%/yr (real decline about 25%) | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| Equity-only crash (2000–2003 style) | Official-data replay | 2000–2003 data. US share-price index fell about 26% 2000→2002; local home prices kept rising | https://fred.stlouisfed.org/series/SPASTT01USM661N |
| 2021–23 inflation spike | Official-data replay | 2021–2023 data. CPI about 4.7% / 8.0% / 4.1% (annual averages), 30-yr mortgage rate 3.0%→6.8% | https://fred.stlouisfed.org/series/CPIAUCNS |
| Lost decades (flat nominal prices) | Assumption | Stylised; no official US data series supports this exact path. 15 years: home 0%, CPI 0.5%, equities 3.0%, 10-yr 1.5% | https://fred.stlouisfed.org/series/ATNHPIUS41940Q |
| Insurance and climate-cost shock | Assumption | Stylised; premiums rising faster than CPI. 10 years: insurance +12 pt/yr above cost inflation; home prices −3%/yr for 5 years | https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111%3A20 |
| Property-tax regime change (assessments track market) | Assumption | Hypothetical; no such measure is currently on the books. From the shock year onward Property A and B are taxed on current market value | https://www.boe.ca.gov/proptaxes/pdf/pub29.pdf |
| Prop 19 inheritance relief repealed | Assumption | Hypothetical. Living in Property A earns no assessment relief: full reassessment at inheritance | https://boe.ca.gov/prop19/ |
| Compound shock: stagflation → 2008-style crash + insurance shock | Official-data replay + assumption | Back-to-back replays of 1973–82 and 2006–12 with +8 pt/yr insurance shock in the first decade. 17 consecutive stressed years | https://fred.stlouisfed.org/series/CPIAUCNS |

## 3. Results (2045 inheritance, 10-year hold to 2055, shock begins 2042, rent benchmark 4BR)

Nominal dollars at 2055. "Sell (taxed)" liquidates the portfolio at the endpoint and applies the capital-gain scenario rate to all growth (conservative); "Sell (untaxed)" is the lab's original figure.

| Scenario | Property A at inheritance | Sell (untaxed) | Sell (taxed) | Rent then sell | Live then sell | Live + free SF unit | Best (taxed) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Smooth baseline | $5,959,750 | $9,125,340 | $7,959,170 | $7,395,620 | $6,146,150 | $6,603,810 | sellLiq |
| Replay of the last 49 years | $13,683,540 | $26,646,710 | $22,084,150 | $29,533,380 | $27,275,590 | $28,099,980 | rent |
| 1970s-style stagflation | $8,120,090 | $14,913,780 | $12,503,810 | $15,679,910 | $13,219,960 | $13,947,110 | rent |
| 2008-style housing and equity crash | $3,990,000 | $6,021,280 | $5,269,680 | $5,181,060 | $4,010,070 | $4,468,930 | sellLiq |
| Early-1990s Bay Area bust | $4,611,260 | $8,590,160 | $7,181,560 | $5,925,410 | $4,586,080 | $5,096,260 | sellLiq |
| Equity-only crash (2000–2003 style) | $7,275,360 | $11,139,750 | $9,716,150 | $8,760,670 | $7,505,770 | $7,967,220 | sellLiq |
| 2021–23 inflation spike | $6,999,060 | $10,716,680 | $9,347,150 | $8,602,190 | $7,208,950 | $7,711,910 | sellLiq |
| Lost decades (flat nominal prices) | $5,193,580 | $5,610,150 | $5,369,120 | $5,049,020 | $4,099,210 | $4,441,520 | sellLiq |
| Insurance and climate-cost shock | $4,597,840 | $7,040,030 | $6,140,350 | $5,681,180 | $4,465,000 | $4,922,660 | sellLiq |
| Property-tax regime change (assessments track market) | $5,959,750 | $9,125,340 | $7,959,170 | $7,341,920 | $5,741,140 | $6,198,800 | sellLiq |
| Prop 19 inheritance relief repealed | $5,959,750 | $9,125,340 | $7,959,170 | $7,395,620 | $5,821,650 | $6,279,310 | sellLiq |
| Compound shock: stagflation → 2008-style crash + insurance shock | $8,120,090 | $13,238,020 | $11,382,720 | $11,470,660 | $9,236,370 | $9,898,240 | rent |

## 4. Monte Carlo (2,000 paths, 5-year block bootstrap of 1977–2025, seed 20261111)

| History | Inherit | Sell median | Sell taxed median | Rent median | Live+SF median | Sell>Rent (untaxed / taxed) | Sell>Live |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mean-adjusted | 2040 | $7,749,450 | $6,775,700 | $5,937,580 | $5,240,590 | 78% / 65% | 90% |
| Mean-adjusted | 2045 | $8,859,310 | $7,718,710 | $6,996,300 | $6,175,350 | 76% / 62% | 90% |
| Mean-adjusted | 2050 | $10,387,710 | $9,053,520 | $8,106,520 | $7,169,650 | 77% / 64% | 90% |
| Raw | 2040 | $14,510,090 | $12,153,550 | $11,036,570 | $10,074,210 | 79% / 61% | 87% |
| Raw | 2045 | $19,407,210 | $16,204,480 | $14,996,640 | $13,753,510 | 78% / 60% | 88% |
| Raw | 2050 | $26,535,370 | $22,107,600 | $20,037,520 | $18,608,750 | 80% / 62% | 88% |

## 5. Findings

1. **Selling is the more robust default, not a certainty.** On the tax-symmetric basis it finishes ahead of rent-then-sell in roughly two of three random histories and in most scenarios; it loses when inflation or home prices outrun a 60/40 portfolio (1970s-style stagflation, replay of 1977–2025).
2. **Living in Property A never wins financially.** Property B already houses the household; living in A (with the freed SF unit rented) trails the better financial option in every scenario.
3. **The biggest hidden dependency is the legal tax base**, not equities: the 2% Prop 13 cap and the Prop 19 formula. See the policy scenarios.
4. **The lab's original sell advantage was overstated** because the sell case left portfolio growth untaxed while rent and live paid capital-gain tax at the endpoint. Both figures are now published.
5. **Property B is exposed to inflation**: its rent rises at 60% of the Bay Area CPI-U increase while costs track inflation.

## 6. Limits and open flags

See `site/review.html` and `research/verification-2026-11-11.md`.

## 7. Data

- `research/data/fred_annual_2026-11-11.csv` — annual values downloaded from FRED on 2026-11-11.
- `site/data/history.js` — generated by `scripts/build-history.py`.
