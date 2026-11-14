# Verification record — session 12f68358 (14 November 2026)

Repository-only. Scope: task L-2 (official-source verification of rule figures, deadlines and benchmarks used by the new pages) and the irregularities found while doing it. Every value below was read from the source on 14 Nov 2026 unless the row says otherwise. Values that could not be confirmed are left blank on the public pages and listed under "Unverified" and on the Flagged page.

## Read and confirmed

| Item | Official source (link) | What was read | Used on |
|---|---|---|---|
| Federal basic exclusion, 2026 deaths | IRS, Instructions for Form 706 (Rev. July 2026), Table of Basic Exclusion Amounts — https://www.irs.gov/instructions/i706 | $15,000,000 (2026); the table excerpt was read through the IRS search index for the instructions, not the full chunk | Overview, Taxes, Sources |
| Federal basic exclusion, 2027 deaths | IRS news release IR-2026-133, 5 Nov 2026 — https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts | $15,480,000 for decedents dying in 2027, up from $15,000,000 for 2026 | Overview, Taxes, Sources |
| Form 706 due date | 26 U.S.C. §6075(a), Cornell LII copy — https://www.law.cornell.edu/uscode/text/26/6075 (official uscode.house.gov page returned "Page Not Found" on this date) | Returns "shall be filed within 9 months after the date of the decedent’s death" | Timeline, Flagged, Sources |
| Form 706 current revision | IRS, About Form 706 — https://www.irs.gov/forms-pubs/about-form-706 | Revision 0825; instructions 07/2026; ETCL fee change (per the page) | Sources (carried from 13 Nov) |
| Prop 19 value-cap allowance | BOE LTA 2025/009 — https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf | $1,044,586 for transfers 16 Feb 2025 to 15 Feb 2027; next adjustment February 2027 | Taxes, Timeline |
| California income tax brackets (2025, Form 540 schedules) | FTB, 2025 Form 540 Tax Rate Schedules (PDF) — https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf | Schedule X (single): 12.30% above $742,953; Schedule Y (joint): 12.30% above $1,485,906; Schedule Z (head of household): 12.30% above $1,010,417 | Sources, Flagged |
| Santa Clara County secured property tax calendar | County of Santa Clara, Property Tax — https://www.santaclaracountyca.org/Property_Tax.html | First installment due 1 Nov; penalty-free to 10 Dec. Second due 1 Feb; penalty-free to 10 Apr. 30 June is the last day for current-year taxes without added penalty | Timeline, Sources |
| Federal capital-gains rates (2025 taxable years) | IRS Topic 409 — https://www.irs.gov/taxtopics/tc409 | 0%, 15%, 20% bands; collectibles and §1202 at 28%; unrecaptured §1250 at 25% | Glossary, Sources |
| Net investment income tax | IRS Topic 559 — https://www.irs.gov/taxtopics/tc559 | 3.8%; thresholds per Topic 559 | Glossary, Sources |
| Treasury yields, 12 Nov 2026 | FRED DGS3MO and DGS2 — https://fred.stlouisfed.org/series/DGS3MO , https://fred.stlouisfed.org/series/DGS2 | 3-month 4.32%; 2-year 4.86% | Phased entry, Glossary |
| 1929 crash | Federal Reserve History, Stock Market Crash of 1929 — https://www.federalreservehistory.org/essays/stock-market-crash-of-1929 | Dow fell from 381.17 (3 Sep 1929) to 41.22 (8 Jul 1932), about 89%; regained 23 Nov 1954 | Black swans, Phased entry |
| 2007–2009 downturn | Federal Reserve History, The Great Recession — https://www.federalreservehistory.org/essays/great-recession-of-200709 | Real GDP fell about 4.3%; unemployment peaked at 10%; S&P 500 fell 57% (Oct 2007 to Mar 2009) | Black swans, Phased entry |
| San Jose metro home prices | FRED ATNHPIUS41940Q — https://fred.stlouisfed.org/series/ATNHPIUS41940Q | Recomputed from the observations read: Q3 2006 (320.14) to Q3 2009 (235.72) is −26.4%. Q3 1975 (18.60) to Q1 1981 (48.69) is +162% in total, about 19% a year over 5.5 years | Phased entry |
| SF Rent Board, 1 Mar 2026–28 Feb 2027 | SF Rent Board current rates — https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit | Allowable increase 1.6% | Timeline, Property |

## Corrections made in this session

- **California rates** were previously only in secondary sources, which disagreed. The FTB schedule now settles the bracket thresholds. The 1% Mental Health Services Tax above $1 million is still secondary-only and is flagged.
- **Santa Clara County dates** were previously only in secondary sites. The county page now confirms them. The old "unverified" status is replaced by a dated reading on the timeline.
- **Form 706 deadline**: the flagged note previously said the 2022 instructions were read. That was wrong. The 9-month rule is now read in the statute text, and the note records the statute copy used.
- **Prop 19 adjustment** was written as "every other 16 February". The BOE notice gives one next adjustment, in February 2027. Corrected.
- **Unverified rows blanked**: the Form 4768 six-month extension, the payment rule under Form 706, and the Prop H billing date were not read in this session. They are now blank and flagged, not stated as facts.

## Unverified (left blank and flagged)

1. Form 706 payment deadline and Form 4768 extension period (not read in the 07/2026 instructions this session).
2. Prop H billing date for the first FY 2027–28 bill (SFMTA page read only for the amounts).
3. California 1% Mental Health Services Tax above $1 million and the treatment of capital gains as ordinary income: from secondary sources only; the FTB Form 540 schedule does not show them.
4. Homeowners insurance premiums: the CDI survey is an interactive tool that did not load premium rows; no premium figure is stated.
5. Property B's Prop H amount for the household's parcel type (not public; the official floor $249 is shown as the minimum only).
6. 2008 recovery length (66 months) and the 1929 home-price fall (30%): stated as model assumptions, not historical facts.

## Irregularities found in the repository

| # | Finding | Action |
|---|---|---|
| I-1 | `.gitignore` did not exclude `private/`, although the L-3 plan depended on it. | Added `private/` to `.gitignore`; verified with `git check-ignore`. |
| I-2 | `scripts/privacy-audit.cjs` crashed on any inline `<script>` (it assumed every script has a `src`). | Made it evaluate inline script text, as `test-guide.cjs` already does. The audit passes. |
| I-3 | `scripts/test-guide.cjs` host allowlist did not include the official hosts used by new rows (Federal Reserve History, FTB, Santa Clara County, Cornell LII statute mirror). | Added those hosts; each was opened this session. |
| I-4 | The sources page said every link was re-opened on 13 Nov 2026. Rows added on 14 Nov were opened on 14 Nov. | Page text now states both dates. |
| I-5 | The `ftb` source key pointed to the State Controller's estate-tax page while labelled as the FTB. | Kept (the page is official and relevant to estate tax); new `ftbSchedule` key added for the rate schedule. |
| I-6 | `countytaxcollector.org` is a placeholder blog page (carried from earlier notes). | Not used. |
| I-7 | `https://www.sccgov.org/sites/tax/Pages/default.aspx` returned a Cloudflare 522 timeout. | Not used; the county's own property-tax page is cited instead. |
| I-8 | `https://www.ftb.ca.gov/file/personal/tax-rates.html` returned 404 (earlier note). | Replaced by the FTB 2025 Form 540 PDF. |
| I-9 | Open pull request #88 belongs to another session (`arena/83d6cb9b-tino2`). | Not touched. Logged here only. |
| I-10 | A seven-figure modelled amount is shown in the browser only after the page loads. | Figures come from the model, not the official ledger; the check treats them as illustrative. The figure check scans static HTML, so the values are supplied as JSON and formatted in the browser. |

## Figures the public pages must not show

Household figures, parcel numbers, addresses and account numbers. The private analysis is in the git-ignored `private/12f68358/household-analysis.md` only (decision L-D1).
