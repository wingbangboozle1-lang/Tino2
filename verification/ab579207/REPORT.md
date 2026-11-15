# Verification report, session ab579207 (15 Nov 2026)

Public-safe. This report contains **no household figures**. Owner-supplied values were checked privately (git-ignored `private/ab579207/`) and are described here only by kind of irregularity.

## 1. Official rule and benchmark values re-read this session

Each row was fetched from the official page on 15 Nov 2026. "Match" means the page supports the value the guide and the model use.

| Item | Value used | Official source (link) | Result |
|---|---|---|---|
| Proposition 19 family-home value allowance, transfers 16 Feb 2025 to 15 Feb 2027 | $1,044,586 | [BOE Letter to Assessors 2025/009](https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf) | Match. The allowance is re-set every other February, so later amounts are unknown. |
| Proposition 19 occupancy and claim periods | heir lives in home within 1 year; homeowners' exemption (BOE-266 or BOE-261-G) within 1 year; BOE-19-P within 3 years and before any third-party transfer | [BOE Proposition 19 fact sheet (Pub 801)](https://www.boe.ca.gov/pdf/pub801.pdf) | Match. This closes the open Flagged item on claim periods; the timeline now lists the dates. |
| Federal filing threshold, 2026 death | $15,000,000 | [IRS · Estate tax](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax) | Match. |
| Federal basic exclusion, 2027 death | $15,480,000 (2026: $15,000,000) | [IRS IR-2026-133 (5 Nov 2026)](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts) | Match. |
| Federal estate tax rate above the top bracket | 40% above $1,000,000 of taxable estate | [26 U.S.C. §2001(c), Cornell LII](https://www.law.cornell.edu/uscode/text/26/2001) | Match. |
| California 1% additional tax on taxable income above $1,000,000 | 1% | [Cal. Revenue & Taxation Code §17043 (leginfo)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=17043.&lawCode=RTC) | Match on the rate and threshold. A secondary website uses a different name for this surcharge; the statute text read here uses neither name, so no name is stated in the guide. |
| Home-sale gain exclusion | $250,000 single; $500,000 joint; 2-of-5-year ownership and use tests | [IRS Topic 701](https://www.irs.gov/taxtopics/tc701) | Match. Used only in the private analysis and in the optional engine parameter. |
| Treasury 3-month yield | 4.32% (12 and 13 Nov 2026) | [FRED DGS3MO](https://fred.stlouisfed.org/series/DGS3MO); [U.S. Treasury daily par yield curve, Nov 2026](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611) | Match. |
| Treasury 2-year yield | 4.86% (12 Nov, FRED); 4.88% (13 Nov, Treasury) | [FRED DGS2](https://fred.stlouisfed.org/series/DGS2); Treasury link above | Both match their own date. The model cites 12 Nov and the guide text cites 13 Nov. Labelling only; no value change. |
| FHFA San Jose house price index, latest value | 558.75 (Q2 2026) | [FRED ATNHPIUS41940Q](https://fred.stlouisfed.org/series/ATNHPIUS41940Q) | Match on the latest point. Earlier points in the growth calculation are from the prior ledger (session 12f68358), not re-read here. |
| SF Proposition H parcel tax, FY 2027–28 | $249 for multifamily up to 5,000 sq ft; $0.195 per sq ft above; cap $50,000; first bill fall 2027; inflation adjustment from FY 2028–29; term to 30 June 2042 | [SFMTA Proposition H](https://www.sfmta.com/getting-around/muni/parcel) | Match on schedule and term. The engine held $249 flat without the term end; this is now flagged. |
| Santa Clara County HUD Fair Market Rent (rent benchmark) | not captured | [HUD Fair Market Rents](https://www.huduser.gov/portal/datasets/fmr.html) | **Not verified.** The official page was reached, but the county table is not readable through this tool. Aggregator figures were not used. Left blank. |
| Insurance premiums for either ZIP code | not captured | [CA Department of Insurance, compare premiums](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/) | **Not verified.** No official ZIP-level premium data located. Left blank; owner estimates are kept private. |

## 2. Owner-supplied tables: arithmetic check (kind of result only)

Every printed year-over-year percentage in the owner's two assessment and tax tables was recomputed from the printed values.

- Most printed percentages match within rounding.
- Two printed assessment changes differ from the arithmetic by a few hundredths of a point.
- One 2026 assessed value is a projection (the prior year times the 2% cap factor), not an assessor roll value.
- One tax-to-assessed ratio is higher than the base levy and is not explained by the tables. It needs the secured tax bill.
- Two early rows have no prior-year row to test against.

Official references for checking: [Santa Clara County Assessor](https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2) and [SF Treasurer secured property tax](https://sftreasurer.org/property/secured-property-taxes).

## 3. Engine changes made in this session

- `scripts/analysis_model.py`: optional `home_gain_exclusion` parameter (default 0). Applied only to the two living-then-sell paths. The public engine's outputs are unchanged, confirmed by `test-model-reference.py` (108 configurations, 250 stress years, 20,736 comparisons: PASS).
- `scripts/analysis_model.py`: comment corrected. The 51-year FHFA growth rate is about 6.9% a year, not 6.7%. No value changed.

## 4. Irregularities found (public list; no values)

1. Legacy household files and older Git history contain household figures. Pages does not serve them, but the repository is public. A history rewrite is an owner decision (Flagged, S16–S17).
2. The public calculator taxes living-then-sell paths on the full gain; the primary-residence exclusion is missing from the public default (Flagged, S20).
3. The public calculator has no rent input for the living path, so living carries no imputed rent (Flagged, S19).
4. Prop H is held flat in the engine, with no indexation and no 2042 term end (Flagged, S21).
5. The Proposition 19 allowance is held flat beyond 15 Feb 2027 (Flagged, S23).
6. The estate exclusion after 2027 is a projection, not law (Flagged).
7. Maintenance is a percentage of value in the engine (Flagged, S22).
8. Yield dates differ between the model and the guide text (labelling only).
9. Owner tables: see section 2.

## 5. Checks run on the final tree

- `python3 scripts/build-guide.py` and `python3 scripts/package-site.py`: PASS (31 reviewed files).
- `python3 scripts/check-generated.py`: PASS (17 pages up to date).
- `python3 scripts/check-figures.py`: PASS (28 ledger records, all verified).
- `python3 scripts/test-model-reference.py`: PASS.
- `python3 scripts/check-publication.py --self-test` and live: PASS.
- `node scripts/privacy-audit.cjs`: PASS.
- `node scripts/test-guide.cjs`: PASS (17 rendered pages, 941 source-linked rows, 11,609 checks).
- `python3 scripts/test-phased.py`: PASS.
- Household scan of the published tree (no owner figure, ZIP code or household-derived number): no matches.
