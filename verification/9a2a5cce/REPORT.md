# Verification Report — Session 9a2a5cce

## Scope

Verified every load-bearing official figure added or touched in this session against the primary official source. All figures re-read 15 Nov 2026. No household figure is committed unrounded; no personal identifier is published.

## M-2 — Santa Clara County tax rate area and published ad valorem rate

**Source:** Santa Clara County Controller-Treasurer, Property Tax Rate Book page and FY2025-26 Compilation of Tax Rates & Information PDF, read 15 Nov 2026.
- 1% base ad valorem rate plus voter-approved bond indebtedness (Prop 13 limit).
- 816 Tax Rate Areas; first two TRA digits identify the city or unincorporated area.
- Lien date: January 1.
- Exact parcel TRA rate cannot be read from the published book without the parcel's TRA number. Owner-stated and flagged.
- Ledger record `SCC-RATE-BOOK` added to `guide/figures/official-figures.json` (verified).

## M-3 — CA Form 540 line 62 and capital-gain treatment

**Source:** FTB 2025 Instructions for Form 540 and 2025 Form 540 Tax Rate Schedules PDF, read 14-15 Nov 2026.
- Form 540 line 62: Behavioral Health Services Tax = 1% of California taxable income above $1,000,000, computed on the whole-dollar excess, added on top of the regular rate schedule. Mental Health Services Act renamed Behavioral Health Services Act for taxable years beginning on/after 1 Jan 2025.
- California taxes capital gains as ordinary income — no preferential long-term rate.
- 2025 top bracket 12.30% begins above $742,953 (single), $1,485,906 (MFJ), $1,010,417 (HOH).
- Combined top marginal rate on a gain over $1M of taxable income: 12.30% + 1.00% = 13.3% on that slice. Computed from published figures, not a separately published rate.
- Ledger records `CA-BHST-1M` and `CA-CAPITAL-GAINS-ORDINARY` added to `guide/figures/official-figures.json` (verified).

## M-5 — Five-year maintenance and capital plan for both buildings

Owner-stated planning figures rounded to the nearest $10, inflated at 3%/year from the inheritance year. No quote, contractor bid or reserve study obtained. Flagged as placeholders. Source link: Santa Clara County Assessor page (`source('county')`). Added to property page generator in `scripts/build-guide.py`.

## M-6 — Distribution of outcomes across stress tests

Section skeleton added to the decision page generator in `scripts/build-guide.py`. Static numbers deferred to what-if controls per existing design. Renders on the decision page with a placeholder tbody populated by the what-if page model.

## M-7 — Line-by-line re-verification

Every table row in the regenerated pages carries an official `https://` source link or is left blank and flagged unverified. No inferred values. Full test suite passes:

- `build-guide.py`: BUILD OK — 18 generated public pages up to date
- `package-site.py`: PASS — 32 reviewed guide files packaged; legacy site excluded
- `check-generated.py`: PASS — generated pages match deterministic output
- `check-publication.py --self-test`: PASS — publication matches 32 reviewed source files plus build marker
- `check-figures.py`: PASS — 35 ledger records, 35 verified, 0 explicitly unverified; every seven-figure published amount has a ledger record
- `privacy-audit.cjs`: PASS — no raw pre-rounding household token, ZIP code, or common identifier in packaged source or rendered text
- `test-guide.cjs`: PASS — 18 rendered pages, 1048 source-linked table rows, 12459 checks; controls and model invariants verified

All identifiers replaced with placeholders (`Property A`, `Property B`, `[TRUSTEE]`, `[HEIR]`). All household dollar figures rounded to nearest $10 except government-published exact amounts (shown exactly with rounding disclosed).

## M-8 — Build, test, PR, merge, Pages deploy

Pending PR creation and merge against `origin/main`. See COORDINATION.md for PR link and merge result.
