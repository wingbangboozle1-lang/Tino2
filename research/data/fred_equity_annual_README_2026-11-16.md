# FRED share-price and CPI extract used by the entry test — 16 Nov 2026

Purpose: the recorded-history version of the sale-proceeds entry test on the public guide's
Black swans page. Index levels only — no dollar amounts, no household figure, no identifier.

## What this file holds

| Column | Series | Publisher | Definition used here |
| --- | --- | --- | --- |
| `eq_dec_level_spastt01usm661n` | SPASTT01USM661N — OECD MELODY monthly, United States, share price index (2021 = 100), via FRED | OECD, via FRED | The **December observation** of each year, used as that year's end-of-year price level |
| `eq_annual_avg_spastt01usm661n` | same series | OECD, via FRED | FRED's published **annual average** of the twelve monthly observations, kept here as a cross-check column |
| `cpi_avg_cpiaucns` | CPIAUCNS — Consumer Price Index for All Urban Consumers: All Items in U.S. City Average, via FRED | U.S. Bureau of Labor Statistics, via FRED | Annual average, index level (1982-84 = 100), used only to deflate |

* The December column is the extract already carried in this repository
  (`research/data/fred_annual_2026-11-11.csv`, downloaded 11 Nov 2026). It was re-checked
  line by line on 16 Nov 2026 against the official monthly endpoint
  `https://fred.stlouisfed.org/graph/fredgraph.csv?id=SPASTT01USM661N&cosd=2007-11-01&coed=2009-12-31`:
  2007-12 = 91.882580, 2008-12 = 51.736620, 2009-12 = 67.164700 — **all three match**.
* The annual-average column was read on 16 Nov 2026 from
  `https://fred.stlouisfed.org/graph/fredgraph.csv?id=SPASTT01USM661N&cosd=1970-01-01&coed=2026-12-31&fq=Annual`
  (56 years, 1970–2025; the 2026 row is blank because the year is incomplete).
* The CPI column was re-read on 16 Nov 2026 from
  `https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCNS&cosd=2013-01-01&coed=2026-12-31&fq=Annual`
  for 2013–2025 — every one of the 13 values matches the repository extract
  (232.957, 236.736, 237.017, 240.007, 245.120, 251.107, 255.657, 258.811, 270.970,
  292.655, 304.702, 313.689, 321.943).

## Limits of this extract

* SPASTT01USM661N is a **share price index**: it excludes dividends. The model that reads this
  file therefore applies one stated, invented dividend assumption to the stock legs and labels
  it as an assumption, so that a price-only index does not silently flatter the strategies that
  hold less stock early.
* Year-end sampling understates within-year swings. The 2008 decline reads −43.7% here
  (91.882580 → 51.736620), while the Federal Reserve's own account of the same period reports a
  57% peak-to-trough fall in the S&P 500; the deeper move happened inside the year. The
  template test above the recorded-history test on the same page is what shows the peak-to-trough
  shape, and the two are labelled as different tests.
* Deflation uses annual CPI averages against a December-to-December interval, an approximation
  that is stated wherever a real figure appears.
