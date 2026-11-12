# Final integration verification — session 9984092e (2026-11-12)

Scope: independent re-verification of the combined 18-page dashboard on `main` `052e626`
(PR #52) before opening the integration PR. No shared site file was changed by this
session; the only committed changes are this report and the `COORDINATION.md` claim /
completion blocks. All dollar figures below are rounded to the nearest $10 unless a
government body publishes the exact amount.

## 1. Check suite (final tree, this session)

| Check | Result |
|---|---|
| `node scripts/validate.js` | PASS — 1,561 checks, 18 pages, 177 official sources. Base case 2040→2050: sell $7,683,290, rent $6,249,830, live $5,135,780 |
| `node scripts/stress-test.js` | PASS — 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| `python3 scripts/package-site.py` | PASS — canonical site only; $10-rounding rule passed |
| `python3 scripts/check-publication.py --self-test` + plain | PASS — 34 reviewed public files only; fail-closed tests reject unlisted files, symlinks and missing pages |
| `node scripts/runtime-test.cjs` (jsdom 26.1.0, installed to `.cache/test`) | PASS — 18 rendered pages, 1,583 rendered rows source-linked, no runtime errors, no broken local links |
| `node qa/tools/gate.cjs` | PASS — 18 pages, 1,583 rows (1,574 with own official link, 9 calculated rows with context link only), 4,985 dollar amounts checked (115 official exact figures), 559 internal + 2,074 external links, 0 errors, 0 warnings |
| `python3 integration/tools/privacy_scan.py` | 0 errors. 228 warnings are all in repository-only `research/` / `verification/` files, none in the packaged `_public` site (the gate above is the authority for the public artifact) |
| `python3 src/check_links.py .` | PASS — 68 pages, 887 table rows, 128 distinct external links (external reachability not machine-checked from this sandbox) |

## 2. Independent arithmetic recomputation

The model in `site/data/model.js` was recomputed from scratch in Python from the
`BASE` inputs (home prices +3.5%/yr, assessments +2%/yr, expenses and rents +3%/yr,
portfolio +5%/yr after tax, 6% sale cost, 33.1% gain tax, $250,000 primary exclusion,
Proposition 19 amount $1,044,586 with one step every second 16 February). Results
match the JavaScript exactly at $10 rounding:

| Inheritance year (10-year hold) | Sell & reinvest | Rent, then sell | Live, then sell | Sell taxed at liquidation (conservative bound) |
|---|---|---|---|---|
| 2040 → 2050 | $7,683,290 | $6,249,830 | $5,135,780 | $6,701,410 |
| 2045 → 2055 | $9,125,340 | $7,395,620 | $6,068,080 | $7,959,170 |
| 2050 → 2060 | $10,838,040 | $8,752,170 | $7,164,510 | $9,453,000 |

2026 real-estate-only headroom: $15,000,000 exclusion − $3,100,000 Property A =
$11,900,000 (Property B is already owned by the heir and excluded from the
decedent's estate). Proposition 19 allowance in 2040: $1,329,005. Winner in the
base case is "sell" for all three inheritance years; the ranking is a result on
assumed returns, not a forecast.

## 3. Official sources re-opened this session (12 Nov 2026)

| Source | What was confirmed | Matches site? |
|---|---|---|
| IRS, What's new — Estate and gift tax | Working Families Tax Cuts (P.L. 119-21) sets the 2026 basic exclusion at $15,000,000 | Yes — `irsEstate`, ledger FED-04 |
| IRS IR-2026-133 (5 Nov 2026) | 2027 basic exclusion $15,480,000; annual gift exclusion $20,000 (up from $19,000) | Yes — `irs2027`, model `estateExclusion2027` |
| California State Controller, California Estate Tax | No California estate-tax return for deaths on or after 1 Jan 2005 | Yes — `caEstate` |
| BOE, Proposition 19 page | Value limit = current taxable value plus $1,000,000 "as biennially adjusted"; homeowners' exemption within 1 year, exclusion claim within 3 years | Yes — `boeProp19` |
| BOE News Release NR 25-02 (7 Mar 2025) | $1,044,586 for transfers 16 Feb 2025–15 Feb 2027 (+2.15% from $1,022,600), adjusted every other year from the FHFA California HPI | Yes — `boeProp19Amount`, `boeLta2025009`, model `prop19Amount` |
| HUD FY2027 SAFMR lookup, ZIP 95014 | 3BR $5,440, 4BR $5,800 (effective 1 Oct 2026); FY2026 floor table shown on the same page | Yes — `hudA2027`, ledger CF-04 |
| SF Rent Board, Current Rates | 1.6% allowable increase 1 Mar 2026–28 Feb 2027; File No. 261020 notice posted 9 Nov 2026 "has not been enacted" | Yes — `sfRent`, `sfRentRates` |

Note on the HUD FY2027 URL: the 2026-style `.odn` ZIP address for 2027 returns 404.
The site correctly links the FY2027 interactive lookup
(`huduser.gov/datasets/fmr/fmr2027/zip-calc?...`), which was re-opened above and
returns the exact figures. No change needed.

## 4. Brief coverage (line by line)

- Executive summary with the answer, reasons and unknowns: `index.html` (hero,
  bottom line, by-year table, four drivers, black-swan check, costs, tax levels,
  steps, law watch).
- Privacy first: placeholder labels Property A / Property B throughout; every
  page carries `noindex,nofollow,noarchive`; packaged `robots.txt` disallows all;
  gate R1/R2 pass on the rendered public site (no e-mail, street address, parcel
  number or SSN pattern; every $1,000+ amount is a multiple of $10 or an official
  published figure). Residual re-identification risk and Git-history exposure are
  published on the Flagged for Review page, not hidden.
- Cupertino vs San Francisco distinction: Property B is modeled as already owned
  by the heir and excluded from the decedent's estate (`estateRow` uses Property
  A only); `site/san-francisco.html` and the plan page carry the rental economics
  (two units rented, third unit available to live in without losing rent income).
- Black-swan section: `site/stress.html` (50-year variable paths),
  `site/scenarios.html` (recorded-decade replays), `site/black-swan.html`
  (recorded data) — 12 scenarios and 2,000 seeded Monte Carlo histories.
- $10 rounding: enforced by `package-site.py` and gate R1; household histories on
  `site/properties.html` are published rounded.
- Inheritance 2040–2050, live / rent / sell after tax: `site/decision.html`
  (interactive lab) and `site/plan.html` (best plan), with year-by-year
  projections of market value, assessed value and property tax on
  `site/properties.html`.
- Operating costs: `site/operating-costs.html` — Cupertino water (household
  ~$130/mo rounded, grown 3%/yr), solar credit held flat (no tariff forecast),
  insurance left blank with the regulator's survey range shown; San Francisco
  water/electricity and landlord insurance likewise.
- Step-by-step inheritance process: `site/inheritance.html` (trust, assessor,
  basis, filing, distribution checklist).
- Estate-tax thresholds and law changes: `site/estate-tax.html` (federal 2026 /
  2027 official amounts, California none, local barred) and the legal watchlist
  on `index.html` + `site/sources.html` (H.R. 1301, Proposition 19 cadence,
  3 Nov 2026 ballot, SF File 261020, Measure H).
- Verification rule: every rendered table row carries an official source link or
  an explicit context-link label (gate R4); the 6 ledger entries that cannot be
  confirmed from an official source (SF-08, INS-02, INS-03, UT-02, FED-15, N-12)
  stay `unverified` with blank values and appear on the Flagged for Review page.
  Nothing was inferred or filled in by this session.
- Coordination / PR / merge: claim pushed before work; this report plus the
  completion block are the only changes; PR to `main` and Pages confirmation
  follow in F-4.

## 5. Irregularities found by this session

- **F-I1 (new, minor).** `privacy_scan.py` reports 228 warnings, all in
  repository-only files (`research/`, `verification/`, and source-note text in
  `site/data/sources.js` / `site/data/ledger.js`). The packaged public site is
  clean under the gate. No action needed for publication; recorded so the
  warning count is not mistaken for a public-site defect.
- **F-I2 (carried forward, not new).** The standing `needs review` items remain
  published on `site/review.html`: public-context re-identification risk,
  Git-history exposure (including the account e-mail in merged commits), the two
  blank insurance premiums (INS-02, INS-03), the SF water-bill and estate-repeal
  items read from search extracts (UT-02, FED-15), and the 2018 parcel-tax item
  (SF-08). None blocks the merge per the brief.
- No defect in model arithmetic, navigation, links or rounding was found. No
  shared site file was edited.
