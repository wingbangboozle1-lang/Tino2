# Verification record — session 330ce4c5 (13 November 2026)

Repository-only; not published. K-3 of the session claim block: line-by-line re-verification of the published guide (`index.html` + 12 `guide/*.html` pages, artifact of decision V-H1, PR #82) against official sources, on branch `arena/330ce4c5-tino2` at `7378ecc`.

## What was checked

| Check | How | Result |
|---|---|---|
| Every external source cited by a published page | Extracted all `href="https://…"` from `index.html` and `guide/*.html` (37 distinct claim-bearing URLs; local assets excluded) and re-fetched each source on 2026-11-13 with the page fetcher | 37 of 37 fetched and read; see the source table below |
| Claim-by-claim comparison | For each URL, the guide rows/claims citing it were compared against the fetched text (amounts, dates, statuses, hedging language) | zero mismatches; every published claim matches its source or is explicitly hedged |
| Inflation statistics (conditions page) | Independent recomputation from FRED `CPIAUCNS` monthly NSA series (1913→2026-10; Oct-2025 missing): annual averages, year-over-year changes, 1991–2025 statistics | reproduces every published figure (table below) |
| Proposition 13 factor statistics (conditions page) | Entered all 51 factors from BOE LTA 2026/002 (1976-77…2026-27) and computed cap count, below-cap count and CAGR | 51 years, 40 at the 2% cap, 11 below, CAGR 1.8136% → published "about 1.81%" ✓ |
| Figures ledger | `scripts/check-figures.py` | PASS: 28 records, 27 verified, 1 explicitly unverified (see I-2); every seven-figure published amount has a record |
| Published-row source rule | `scripts/test-guide.cjs` (row loop: every `tbody` row must carry a link to an approved agency host) | PASS: 796 rows, 10,065 checks, all rows sourced |
| Model and page integrity | baseline `scripts/build-guide.py` + `check-generated.py`, `package-site.py`, `check-publication.py --self-test`, `check-figures.py`, `test-model-reference.py` (108 configs, 250 stress years, 10,236 comparisons), `privacy-audit.cjs` | all PASS on `6d53c27` before any change |

## Independent recomputations

Published claim (conditions page) → independent result:

| Claim | Published | Recomputed | Verdict |
|---|---|---|---|
| Mean annual CPI-U change, 1991–2025 (35 complete years) | 2.62% | 2.6194% | ✓ |
| Range of annual CPI-U change | −0.36% (2009) to 8.00% (2022) | −0.3555% (2009), 8.0028% (2022) | ✓ |
| Years above 3% | 10 of 35 | exactly 10 (1991, 1992, 2000, 2005, 2006, 2008, 2011, 2021, 2022, 2023) | ✓ |
| Selected-year change table (14 rows: 1991, 1995, 2000, 2005, 2008, 2009, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025) | as published in `build-guide.py` line 431 | all 14 reproduce from the page's own published 3-decimal annual averages (`guide/data/conditions.js`), which themselves match full-precision FRED means to ≤0.0003 | ✓ (see I-6 for the 1991 convention note) |
| Prop 13 factor record 1976-77→2026-27 | "hit the full 2% cap in 40 years, was lower 11 times, and compounded at about 1.81% a year" | 40 / 11 / 1.8136% | ✓ |
| 2025 uses eleven months | conditions page notes October 2025 is blank in the series | confirmed: `CPIAUCNS` 2025-10 observation missing (Oct-2025 CPI never collected) | ✓ |

## Source-by-source verdicts (all fetched 2026-11-13)

| # | Source | Guide claim checked | Verdict |
|---|---|---|---|
| 1 | irs.gov …/estate-tax | 2026 filing threshold $15,000,000 (table ends 2026) | ✓ |
| 2 | irs.gov IR-2026-133 (tax year 2027) | 2027 basic exclusion $15,480,000; 2027 gift exclusion $20,000 | ✓ |
| 3 | boe.ca.gov lta25009.pdf | Prop 19 allowance $1,044,586 for 2025-02-16→2027-02-15, adjusted every other February 16; prior amounts $1,000,000 / $1,022,600 | ✓ |
| 4 | boe.ca.gov lta26002.pdf | 2026-27 factor 1.02; full factor table 1976-77…2026-27 (basis for the 40/11/1.81% statistics) | ✓ |
| 5 | asr.santaclaracounty.gov parent-to-child-2 | assessor page says allowance adjusted "annually beginning 2023" — cadence differs from BOE (guide flags this; follows BOE) | ✓ flag accurate |
| 6 | boe.ca.gov/prop19/ | $1,000,000 base "as biennially adjusted"; 3-year claim window; 1-year homeowners'-exemption window | ✓ |
| 7 | sco.ca.gov ardtax_estate_tax | no California estate-tax return for deaths on/after 2005-01-01 | ✓ |
| 8 | sf.gov current-rates | 1.6% rent increase 2026-03-01→2027-02-28; relocation/interest pages; deposit interest 4.2% | ✓ |
| 9 | sfmta.com …/parcel | Prop H approved 2026-11-03; FY2027-28 SFH ≤3,000 sq ft $129 (+$0.42/sq ft over), MF ≤5,000 $249 (+$0.195, cap $50,000); first bill fall 2027; term 2027-07-01→2042-06-30; inflation indexing FY2028-29; exemption portal opens 2026-12-01 | ✓ |
| 10 | sfelections.org results/20261103 | "(Preliminary)", updated 2026-11-10, ~900 ballots left, up to 30 days to certify | ✓ (guide says "preliminary") |
| 11 | freddiemac.com/pmms | 30-yr FRM 7.11% at 11/12/2026 (prior 7.18%, year-ago 6.24%); 15-yr 6.45%; 52-week range 5.98–7.4% | ✓ |
| 12 | cbo.gov/publication/61882 | outlook 2026–2036 (Feb 11 2026): deficit $1.9T FY26; debt 101%→120% GDP; PCE inflation ≈2% by 2030 | ✓ |
| 13 | pubs.usgs.gov fs20163020 | 72% probability of ≥M6.7 quake in SF Bay region before 2043 | ✓ |
| 14 | bls.gov cpi_01122023 | 12 months ending Dec 2022: all items +6.5%, electricity +14.3%, food +10.4% | ✓ |
| 15 | irs.gov gifts-inheritances FAQ | inherited basis = FMV at date of death (or alternate valuation if elected) | ✓ |
| 16 | huduser.gov SAFMR | SAFMRs are ZIP-code FMRs; guide publishes no ZIP-level figures | ✓ |
| 17 | leginfo RTC §480 | 90 days general; 150 days trust/nonprobate; probate → inventory & appraisal; $100/10% penalty | ✓ |
| 18 | leginfo PROB §16061.7 | trustee notice ≤60 days of triggering event | ✓ |
| 19 | irs.gov taxtopics/tc701 | $250,000 / $500,000 home-sale exclusion; 2-of-5-year tests | ✓ |
| 20 | irs.gov rr-23-02.pdf | no §1014 basis adjustment for trust assets not includible in the gross estate | ✓ |
| 21 | fdic.gov insured-deposits | trust owner with 5+ beneficiaries: $1,250,000 per owner, all trust accounts at the same bank (as of 2024-04-01) | ✓ |
| 22 | congress.gov H.R.1301 (+ text) | "Death Tax Repeal Act", introduced 2025-02-13, Ways and Means, not enacted; text repeals estate and generation-skipping transfer taxes | ✓ |
| 23 | sftreasurer.org secured-property-taxes | FY 2026-27 secured rate 1.18162182%; due Dec 10 / Apr 10 | ✓ |
| 24 | boe.ca.gov lta25023.pdf (Pub 800-10) | 1% + voter debt, 2% cap, assessor enrolls lower of factored base year value or market (Prop 8), base resets on change in ownership/new construction | ✓ |
| 25 | irs.gov publications/p527 | rental income, expenses, depreciation; repairs vs improvements; land not depreciable | ✓ |
| 26 | irs.gov retirement-topics-beneficiary | lump sum any time, distributions taxable, 10-year rule for non-eligible designated beneficiaries | ✓ |
| 27 | fred.stlouisfed.org CPIAUCNS (series page + CSV) | monthly NSA CPI-U series behind every inflation figure; 2025-10 blank | ✓ |
| 28 | investor.gov World Investor Week 2026 bulletin (Oct 5 2026) | diversification "can help reduce the risks of investing"; guide row: "Diversification can reduce certain risks but neither guarantees returns nor prevents loss" | ✓ paraphrase-conservative (see I-3) |
| 29 | insurance.ca.gov compare-prem | survey results "are not premium quotes"; homeowners/earthquake surveys available | ✓ |
| 30 | insurance.ca.gov eq-ins | standard homeowners policies do not cover earthquake damage (except fire); CEA mechanics | ✓ |
| 31 | pge.com Solar Billing Plan | monthly statements + annual True-Up; export-credit value set at permission to operate; credits before 2028 | ✓ |
| 32 | cupertino.gov Residents/Utilities/Water | three water systems in Cupertino (California Water Services, San Jose Water Company, City system); City system leased to SJWC through 2036 | ✓ |
| 33 | sfpuc.gov Rates_Schedule_Water_Sewer_2026-7.pdf | water and sewer rate schedules effective FY 2026-27 (from 2026-07-01); two-tier residential structure | ✓ |
| 34 | docs.github.com removing-sensitive-data | history rewrite coordination, PR/cache/clone persistence, GitHub Support for cached views | ✓ |
| 35 | fred.stlouisfed.org ATNHPIUS41940Q | FHFA all-transactions house-price index, San Jose–Sunnyvale–Santa Clara MSA (Q2 2026 = 558.75) | ✓ |
| 36 | boe.ca.gov pdf/pub801.pdf | Prop 19 fact sheet: 1-year residency/exemption, 3-year claim window, value limit = factored base + $1,044,586 (Feb 2025–Feb 2027), BOE-19-P form | ✓ |
| 37 | leginfo SB 284 status (2025-2026) | "official status page lists it in committee; not enacted as of review; proposes changes to family-home transfer rules" | ✓ Active Bill – In Committee Process; last action 2025-07-14 held in Assembly committee; topic "Property taxation: change in ownership: family homes and farms" |

## Irregularities

| ID | Finding | Status |
|---|---|---|
| I-1 | `guide/conditions.html` and `guide/stress.html` both publish `<title>`/`<h1>` "A straight line is not a forecast." — `scripts/build-guide.py` line 451 reuses the stress heading for the conditions page. Titles are otherwise unique per page. | **Defect; routed to K-4** (fix generator heading, regenerate, add a uniqueness assertion to `scripts/test-guide.cjs`) |
| I-2 | Figures-ledger record `SCCTRANSFER-TAX` (Santa Clara County documentary transfer tax $0.55 per $500 ≡ $1.10 per $1,000) was explicitly unverified with a blank source. During this review the official page was found and read: Clerk-Recorder "Recording real estate" states "$.55 per $500 or fractional portion" and city add-ons for San Jose, Palo Alto and Mountain View ($1.65 per $500) | **Verified this session; ledger upgrade routed to K-4** (27/28 → 28/28) |
| I-3 | The SEC bulletin supports "diversification can reduce the risks" but contains no sentence matching "neither guarantees returns nor prevents loss" verbatim; the guide row is a conservative paraphrase | Accepted as hedged paraphrase; no change (the claim weakens, never strengthens, the source) |
| I-4 | Two official pages disagree on the Prop 19 allowance cadence (assessor: "annually beginning 2023"; BOE: every other February 16, LTA 2025/009 applied one step for 2025-02-16→2027-02-15) | Already published on the Flagged page with both links and the resolution "the guide follows the Board" — correct; no change |
| I-5 | SF Proposition H results still labelled "(Preliminary)" by the Department of Elections at re-fetch | Already disclosed on the Flagged page and in the tax table; recheck after certification (next: up to 30 days from 2026-11-03) |
| I-6 | 1991 selected-year change: published 4.24%; full-precision FRED averages give 4.234964% (→ 4.23). The page's own published 3-decimal averages (130.658 / 136.192) give 4.2355% (→ 4.24) | Not a defect: the table is internally consistent with the averages printed beside it; both round within 0.01 pp. Documented, no change |
| I-7 | Guide displays the Prop 19 allowance as "approximately $1,044,590, rounded from the official amount" (official $1,044,586) | Rounding is disclosed on the page and the exact official figure is in the ledger; allowed exception (exact government-published amounts may also be shown exactly) |
| I-8 | Oct-2025 CPI-U is missing from FRED (collection never happened); the guide states 2025 uses eleven months | Disclosed on the page; correct |

## Limits of this verification (read before relying on it)

1. All fetches are point-in-time (2026-11-13). Dynamic pages (Freddie PMMS, SFMTA, elections results, FRED updates) will change; the guide's own "Source review: 13 Nov 2026" date is the freshness stamp.
2. This review verifies that published statements match official sources. It does not re-derive the synthetic model inputs (the decision/stress figures are invented examples by standing decision V-H1); their internal consistency is covered by `test-model-reference.py` and `check-figures.py`.
3. `scripts/test-browser.cjs` cannot run in this sandbox (missing `libnss3`); it runs in CI only.
4. Rows whose facts are unknowable from public sources (household bills, premiums, appraisals, parcel-specific Prop H amounts) are blank or hedged on the Flagged page by design; absence was checked, not filled.
5. Nothing in this folder contains household data; all figures quoted here are official published amounts or statistics recomputed from official series.

## Conclusion

The published artifact is line-by-line consistent with its 37 official sources: zero claim mismatches, all published statistics independently reproduced, every table row sourced to an approved agency host. Two defects were found and are routed to K-4: the duplicated conditions-page heading (I-1) and the upgradable transfer-tax ledger record (I-2). Everything else is either already flagged on `guide/review.html` or documented above as a rounding-convention note.
