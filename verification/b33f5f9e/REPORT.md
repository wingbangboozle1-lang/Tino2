# Session b33f5f9e — verification report (14 Nov 2026)

Branch `arena/b33f5f9e-tino2`, based on `main` 5327c0c. Scope: tasks X-2 to X-8 in COORDINATION.md.

## 1. Gap audit (X-2) — what the published guide lacked at 5327c0c

| Brief item | State at 5327c0c | State after this session |
|---|---|---|
| Grouped menu | Flat 12-item menu | Four groups: Decide, Property & rules, Evidence & terms, Act (`PAGE_GROUPS` in build-guide.py) |
| Glossary | Absent | `guide/glossary.html`; 16 terms, each linked to an official page |
| One-page printable Attorney & CPA sheet | Absent | `guide/attorney-cpa.html`; print CSS for Letter, placeholders only |
| Deadline timeline | Absent | `guide/timeline.html`; dated steps linked to statute or IRS text |
| Phased entry path and 1929 / 2008 tests | Absent | Black swans page, section "Entry risk after a sale"; model in `scripts/phased_model.py` |
| Reinvestment risk beside headline | Absent | Overview page, next to the executive summary |
| "What would change the answer" on the first screen | Absent | Overview page, above the executive summary |

## 2. Source-to-claim mismatches found and corrected

- Black swans "Changing cycle" row cited the Dec 2022 BLS CPI release, which does not show a 10-year cycle. Now labelled "illustrative"; the CPI link is kept only for the annual rates it supports.
- Black swans "Early crash" row cited the Federal Reserve 2007–09 essay for a path the essay does not contain. Now labelled "illustrative"; the essay is cited for its official magnitudes only.
- Crash paragraph said the Dow Jones average closed 89% below a 3 Sept 1929 peak on 8 July 1932. Neither the index name nor the dates were read in the fetched Fed essay. Now: "an 89 percent decline in stock prices from the 1929 peak to the trough".
- Glossary "basis" and "date of death": the rule text was not previously read. Now read from the IRS FAQ (fair market value on the date of death, with the alternate-valuation exception); the FAQ was opened on 14 Nov 2026.
- Proposition 19 claim periods (one-year homeowners' exemption, three-year exclusion) were not confirmed from BOE text. Removed as dates from the timeline and the attorney sheet; listed on Flagged for Review.
- Form 706 "adjusted taxable gifts" test and "biennially adjusted" Proposition 19 allowance were not read from official text. Removed.
- A bare "$1,000,000" Proposition 19 allowance was removed; the allowance has been adjusted over time and the current amount is not verified.
- Glossary said unconfirmed terms were omitted; the reinvestment-risk label is used on the page. Now stated as undefined and flagged.

## 3. Sources opened for this session (14 Nov 2026)

| Source | Opened | Used for |
|---|---|---|
| federalreservehistory.org/essays/stock-market-crash-of-1929 | Earlier (chunk 0) | 1929 peak-to-trough −89% |
| federalreservehistory.org/essays/great-recession-of-200709 | Search snippet only | 2007–09 S&P 500 −57%, home prices ~−30% (magnitude, not path) |
| home.treasury.gov daily par yield curve, Nov 2026 | Yes, 14 Nov | 13 Nov 2026: 3-month 4.32%, 2-year 4.88%, 10-year 5.15% |
| leginfo RTC §480 | Yes, 14 Nov | (b): trust or death transfers, change-in-ownership statement within 150 days; trustee files where property is held in trust |
| irs.gov/faqs … gifts-inheritances | Yes, 14 Nov | Basis of inherited property: FMV at date of death; alternate-valuation exception |
| leginfo RTC §2617 / §2618 | Earlier | 1 Nov / 10 Dec; 1 Feb / 10 Apr; 10% penalty |
| irs.gov/instructions/i706 | Earlier | Form 706 due 9 months after death; Form 4768 6-month extension; $15,000,000 filing threshold for 2026 |
| boe.ca.gov/prop19/ | Earlier | Family-home transfer concept; value limit structure (no amount stated) |

Other sources in the new pages were verified in earlier sessions and are recorded in the session memory. Anything still unverified is on the Flagged for Review page.

## 4. Checks run on the final tree

| Command | Result |
|---|---|
| `python3 scripts/build-guide.py` then `scripts/check-generated.py` | PASS, 15 generated pages up to date |
| `python3 scripts/package-site.py` | PASS, 28 reviewed guide files packaged; legacy site excluded |
| `python3 scripts/check-publication.py --self-test` | PASS |
| `python3 scripts/check-publication.py --directory _public` | PASS, publication matches 28 reviewed files plus build marker |
| `node scripts/test-guide.cjs` | PASS, 15 rendered pages, 871 source-linked table rows, 11,060 checks |
| `node scripts/privacy-audit.cjs` | PASS (not proof of anonymity) |
| `python3 scripts/check-figures.py` | PASS, 28 ledger records verified; every seven-figure published amount has a ledger record |
| `python3 scripts/test-model-reference.py` | PASS, 108 configurations, 250 stress years, 1,500 phased-investment years, 20,736 comparisons |
| `python3 scripts/test-phased.py` | PASS, 110 checks against an independent tranche reconstruction |
| Public-text scan for addresses, parcel numbers, emails | No matches |

Not run locally: the Jekyll pass `check-publication.py --jekyll` on `_site` (needs the CI Jekyll build). It is part of `.github/workflows/pages.yml` and will run on the PR.

## 5. Merge with session 00503c24 (main at 8c3c739)

After this branch was cut, session 00503c24 merged PRs #89 and #90 to `main`. Both touched the same stress page, generator, and tests. Resolution: its synthetic phased-investment section (Treasury rates 1%, 3%, 5%; simplified 50/50 phase-in) is kept unchanged. This session's entry-risk section follows it and opens with a note that it uses observed yields and the official 1929 and 2008 declines, so the two are not compared directly. The early-crash row keeps its "stylized analogue" wording; the cycle row keeps this session's relabel. The COORDINATION.md blocks of both sessions are kept in order.

## 6. Changes outside the claimed file list

- `scripts/test-guide.cjs`: the approved host list gained `www.federalreservehistory.org` (Federal Reserve history) and `home.treasury.gov` (Treasury par yields). Both are official government publishers, and both are cited for the new stress and entry-test figures. This is a one-line allowlist change, logged here and in COORDINATION.md.

## 7. Open items (also on Flagged for Review)

- Form 1041 due date: not in the IRS text read; secondary sites say 15 April.
- Proposition 19 claim periods: BOE FAQ text not re-read.
- Santa Clara County installment dates: the county page was not re-read; the timeline uses the state dates.
- Federal exclusion ledger label conflict: `FED-EXCLUSION-2026` labels $15,000,000 as the basic exclusion, but the IRS page supports it only as the filing threshold.
- Form 706 basic exclusion table and California estate-tax status: not verified.
- Reinvestment-risk definition: not captured from an official page.
- Crash shapes: illustrative templates built from Fed peak-to-trough declines; not index history.
- Early-crash path and cycle shape: assumptions.

No figure in the new pages is a household value. Every dollar amount is rounded to $10 unless it is an official amount; the one official amount beyond that (the $15,000,000 threshold) has a ledger record.
