# FRED Treasury yield extract — 16 Nov 2026

Purpose: the recorded-history version of the sale-proceeds entry test on the public guide's
Black swans page. Rate levels only. No household figure, no identifier, no address, no ZIP code.

## What was downloaded

| Column | Series | Publisher / release | Units | Coverage in this file |
| --- | --- | --- | --- | --- |
| `dgs3mo_annual_avg` | DGS3MO — Market Yield on U.S. Treasury Securities at 3-Month Constant Maturity, Quoted on an Investment Basis | Board of Governors of the Federal Reserve System (US), H.15 Selected Interest Rates, via FRED | Percent, not seasonally adjusted | 1982–2026 |
| `dgs2_annual_avg` | DGS2 — Market Yield on U.S. Treasury Securities at 2-Year Constant Maturity, Quoted on an Investment Basis | Board of Governors of the Federal Reserve System (US), H.15 Selected Interest Rates, via FRED | Percent, not seasonally adjusted | 1977–2026 |

These are the two maturities the owner's instruction names for parking sale proceeds
("3M–2Y Treasuries"). The 3-month series is published from 1 September 1981, so the first
complete annual average is 1982; the test window on the public page starts there for that reason.

## How the values were obtained

* CSV endpoint, annual frequency, FRED's own "average" aggregation of the daily observations:
  * `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS3MO&cosd=1970-01-01&coed=2026-12-31&fq=Annual`
  * `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS2&cosd=1970-01-01&coed=2026-12-31&fq=Annual`
  Retrieved 16 Nov 2026 (UTC). Values are transcribed exactly as returned; none is rounded,
  because these are published government rates, not household amounts.
* Series page re-read 16 Nov 2026: `https://fred.stlouisfed.org/series/DGS3MO`. It states the
  source (Board of Governors via FRED), the release (H.15 Selected Interest Rates), units
  (Percent, Not Seasonally Adjusted), frequency (Daily), the observation
  2026-11-12 = 4.32, a chart range starting 1981-09-01, and "Updated: Nov 13, 2026".

## Cross-checks performed in this session

| Check | Expected | Read from the official endpoint | Result |
| --- | --- | --- | --- |
| 3-month annual averages 2007–2012 | same rows as the full-file fetch | 4.48, 1.40, 0.15, 0.14, 0.05, 0.09 | MATCH |
| Latest daily 3-month observation quoted on the guide (13 Nov 2026: 4.32%) | U.S. Treasury par yield table for Nov 2026 | FRED DGS3MO page: 2026-11-12 = 4.32 (FRED publishes the Treasury/H.15 figure one business day late) | MATCH on the value; the dated observation is 12 Nov on this page and 13 Nov on the Treasury table |
| 2-year annual average, 2026 | partial-year average | 4.07 | recorded as a partial year; not used as a forecast |

## Limits of this extract

* An annual average is not a monthly path. The model that reads this file interpolates within
  the year and says so on the page.
* 2026 is a partial year in both columns.
* H.15 bill yields are quoted on an investment basis, so the model compounds them monthly at
  `(1 + y) ** (1/12)` rather than on a discount basis.
* Rates are historical. They are not a projection of what a parked portfolio will earn.
