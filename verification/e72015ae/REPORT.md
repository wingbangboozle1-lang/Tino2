# Verification report — session e72015ae (16 Nov 2026)

Scope: close the official-source items that the public guide left open, set the California gain-tax sensitivity from the official Form 540 text, and re-run the local gates. No household figure is in this file; the household analysis is in the git-ignored `private/` folder.

## 1. Official sources read on 16 Nov 2026

| # | Source | What was read | Result |
|---|---|---|---|
| 1 | FTB 2025 Instructions for Form 540, booklet: https://www.ftb.ca.gov/forms/2025/2025-540-booklet.html | Line 62 (Behavioral Health Services Tax) | Text: if taxable income is more than $1,000,000, compute 1% of the amount above $1,000,000, in whole dollars. The name is "Behavioral Health Services Tax", not "Mental Health". |
| 2 | FTB 2025 Instructions for Form 540, booklet (same URL) | Chunk on conformity to federal law | California does not conform generally to the federal One Big Beautiful Bill Act; adjustments are on Schedule CA. 2025 edition only. |
| 3 | FTB 2025 California Tax Rate Schedules (PDF): https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf | Schedules X, Y, Z | 12.30% top bracket above $742,953 (single or married filing separately), $1,485,906 (joint), $1,010,417 (head of household). 2025 values only. |
| 4 | FTB 2025 Instructions for Form 540, online version: https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html | Page opened | Valid. The guide's link to it resolves. |
| 5 | FTB tax calculator, tables and rates: https://www.ftb.ca.gov/file/personal/tax-calculator-tables-rates.asp | Listing, "Last updated 1/2/2026" | Lists 2025 as current. No 2026 schedules published here. |
| 6 | FTB 2026 Form 540 booklet: https://www.ftb.ca.gov/forms/2026/2026-540-booklet.html | Requested | HTTP 404. The 2026 Form 540 is not available at that address, so 2026 values are not used. |
| 7 | IRS Instructions for Form 706 (Rev. 07/2026): https://www.irs.gov/instructions/i706 | What's New; When To File; Paying the Tax | 2026 basic exclusion $15,000,000; basic credit $5,945,800. Return due 9 months after death. Form 4768 gives an automatic 6-month extension to file. Estate tax is due within 9 months; an extension of time to pay can be requested on Form 4768; sections 6166 and 6163 elections are made in Part III. Portability requires a timely filed return, including within any extension. |
| 8 | IRS Form 4768 "About": https://www.irs.gov/forms-pubs/about-form-4768 | Purposes; recent developments | Part II: discretionary extensions; Part III: extension to pay under section 6161. "Recent developments: None at this time." |
| 9 | IRS Instructions for Form 4768 (Rev. 02/2020): https://www.irs.gov/instructions/i4768 | Automatic extension; extension for cause; extension to pay; interest | Automatic extension: file Form 4768 by the original due date, for 6 months. A separate Form 4768 is needed to request an extension to pay. Interest runs on unpaid estate tax from the original due date regardless of extension. Extension-to-pay requests made after the due date are generally not considered. |
| 10 | SFMTA Proposition H parcel tax: https://www.sfmta.com/getting-around/muni/parcel | At a glance; schedule; key dates | Approved 3 Nov 2026. First charge on the FY 2027–28 property tax bill, mailed fall 2027, in the same two installments. Term 1 July 2027 to 30 June 2042. Inflation adjustment from FY 2028–29. Multifamily up to 5,000 sq ft: $249; above that, $249 plus $0.195 per sq ft over 5,000, capped at $50,000. Key dates are labelled estimates on the page. |

## 2. Not verified (left open, flagged)

| Item | Why open | Status |
|---|---|---|
| FTB sentence stating California has no lower capital-gains rate | Not found in the FTB pages read. Secondary sites quote it. | Flagged (Low). The engine's flat rate is a scenario assumption. |
| 2026 California rate schedules and thresholds | FTB 2026 booklet returns 404; the tables page lists 2025. | Flagged. Secondary-site 2026 figures not used. |
| Form 706 Table of Basic Exclusion Amounts | Not located in the sections read. The $15,000,000 figure is confirmed by What's New. | Flagged |
| Form 1041 fiscal-year convention | Not read in this session. | Flagged; left blank on the timeline |
| Proposition H amount for a specific parcel | Requires parcel type and building area, which are not public. | Flagged. The schedule itself is verified. |
| Prop 19 claim windows and the 2027 allowance | Not read in this session. | Flagged; not used in public output |
| California estate-tax status | Not read in this session. | Flagged |

## 3. Changes made in this session

- `scripts/analysis_model.py`: California gain tax base is now the 2025 top bracket, 12.30% (`OFFICIAL['ca_bracket_top']`); the 9.30% band (`ca_bracket_low`) and the 1% surcharge (`ca_bhst`) are recorded beside it. Sensitivity band: 9.30%–13.30%. Previously 0.133 was used and was not verified. The engine still applies one flat rate to the whole gain; the surcharge applies only to taxable income above $1,000,000, so the flat rate overstates it where the gain is not wholly above that level. The reference test does not model California gain tax, so it is unaffected.
- `scripts/build-guide.py`: Form 4768 source added; Form 706 and Form 4768 row rewritten from the IRS text; new Proposition H billing row ("Fall 2027 · FY 2027–28 bill", dates labelled estimated); the timeline callout narrowed to the Form 1041 fiscal-year point; sensitivity row added.
- `scripts/analysis_pages.py`: Form 706 flagged row closed with citations; California surcharge item closed in part with the Behavioral Health Services Tax name; the stale note giving 0.361 was corrected (the browser model uses a flat combined 36.1% = 23.8% federal + 12.3% California; the engine had used 13.3% and 37.1% before this session); two Low flags added; Form 4768 added to the sources list.
- Rebuilt `guide/**`; repackaged `_public/` (not tracked in Git).

## 4. Gates (local, 16 Nov 2026, after the final rebuild)

| Gate | Result |
|---|---|
| `python3 scripts/build-guide.py` | Ran without error |
| `python3 scripts/check-generated.py` | PASS: 18 generated pages up to date |
| `python3 scripts/check-figures.py` | PASS: 39 ledger records, 39 verified, 0 unverified |
| `python3 scripts/test-model-reference.py` | PASS: 108 configurations, 250 stress years, 1,500 phased-investment years, 20,736 comparisons |
| `python3 scripts/test-phased.py` | PASS: 113 checks |
| `python3 scripts/package-site.py` | PASS: 32 reviewed files |
| `python3 scripts/check-publication.py --self-test` | PASS |
| `python3 scripts/privacy-gate.py` | PASS: 238 tracked text files |
| `node scripts/test-guide.cjs` | PASS: 18 pages, 1,058 source-linked table rows, 12,405 checks |
| `node scripts/privacy-audit.cjs` | PASS |
| `node scripts/validate.js` | PASS: 1,610 checks across 19 pages, 178 sources |
| `node scripts/stress-test.js` | PASS |
| `node scripts/test-browser.cjs` | Not run in this session. CI runs it on the pull request. |

Note: the first `test-guide.cjs` run in this session failed because a stale `_public/` copy still contained a non-official dollar amount in `guide/review.html`. The amount was removed from the source, not allowlisted, and `_public/` was then repackaged.

## 5. Irregularities

| Priority | Item | Next step |
|---|---|---|
| Medium | The browser model and the Python engine disagreed before this session (0.361 vs 0.371). They now agree on the base. The 13.30% sensitivity is engine-only. | None needed for the public site; state the limit on the tax page. |
| Medium | Owner decisions L-D1 (publish rounded household figures) and L-D2 (pre-rounding history scrub) remain open. L-D2 needs a repository administrator. | Owner decision; runbook on the Flagged page |
| Low | Open items listed in section 2. | Recheck periodically against the official sources |
