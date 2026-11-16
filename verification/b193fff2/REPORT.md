# Verification record — session `b193fff2` (16 Nov 2026)

Scope: periodic recheck of the official figures the published guide relies on, as of 16 Nov 2026; enacted law separated from proposals. No household figure, identifier or address is involved. Placeholders only (`Property A`, `Property B`).

## 1. Official primary pages read on 16 Nov 2026

| # | Figure as the guide states it | Official source (primary page, re-opened) | What the page says | Result |
|---|---|---|---|---|
| 1 | Federal estate basic exclusion: $15,000,000 for 2026 deaths; $15,480,000 for 2027 deaths | IRS news release IR-2026-133, 5 Nov 2026 — https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts (Rev. Proc. 2026-35: https://www.irs.gov/pub/irs-drop/rp-26-35.pdf) | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026." | **MATCH** — enacted-by-indexation (statutory inflation adjustment; not a legislative change) |
| 2 | Annual gift exclusion $20,000 (2027), $19,000 (2026) | Same IRS release | "…increases to $20,000, up from $19,000 for calendar year 2026." | **MATCH** |
| 3 | Proposition 19 $1 million amount: $1,044,586 for transfers 16 Feb 2025 – 15 Feb 2027; next adjustment Feb 2027 (amount not yet published) | BOE Letter to Assessors 2025/009, 7 Mar 2025 — https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf (index: https://www.boe.ca.gov/proptaxes/2025.htm) | "…the $1 million amount is adjusted to $1,044,586." Table: 16 Feb 2025 – 15 Feb 2027 = $1,044,586. "The next adjustment … will occur in February 2027." | **MATCH**. The Feb 2027 amount is **not published yet** and is shown on the guide as a carried-forward projection, labelled as such. |
| 4 | 3-month and 2-year U.S. Treasury par yields used for the parking path: 4.32% and 4.88% (13 Nov 2026) | U.S. Treasury Daily Par Yield Curve, November 2026 — https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611 | Row 11/13/2026: 3 Mo 4.32, 2 Yr 4.88. Latest row on the page at read time. | **MATCH** |

Enacted vs proposed: items 1–4 are enacted law or published government data. None of the proposals tracked on the guide's Flagged/law-watch pages was re-checked here; they remain listed as proposals.

## 2. Local gates on the current `main` (`5eddd9a`) and this branch

| Gate | Result |
|---|---|
| `scripts/package-site.py` | PASS — 32 reviewed guide files |
| `scripts/check-publication.py` | PASS — 32 reviewed source files plus build marker |
| `scripts/test-guide.cjs` (after installing `jsdom@26.1.0`, `playwright-core@1.49.1`, `axe-core@4.10.3` into `.cache/test`, as CI does) | PASS — 18 rendered pages, 1,114 source-linked rows, 12,844 checks |
| `scripts/privacy-audit.cjs` | PASS — no raw pre-rounding household token, ZIP or common identifier in packaged source or rendered text |
| `scripts/privacy-gate.py` | PASS — 236 tracked text files, no blocked identifier, no un-rounded household-scale amount, no contact/parcel pattern |
| `scripts/test-model-reference.py` | PASS — 108 configurations, 250 stress years, 1,500 phased years, 20,736 comparisons |
| `scripts/validate.js` | PASS — 1,613 checks across 19 pages and 178 official sources |
| `scripts/build-guide.py`, `scripts/check-generated.py`, `scripts/check-figures.py` | PASS (earlier run this session: 18 generated pages up to date; 39 of 39 ledger records) |
| `scripts/test-browser.cjs` | Not run here — needs Chromium with `libnss3`, absent in this sandbox. Runs in CI on pull requests |

## 3. Live site

`https://wingbangboozle1-lang.github.io/Tino2/` read through the fetch tool on 16 Nov 2026: the homepage serves the 13–15 Nov guide (first-screen "What would change the answer" table, executive summary, reinvestment-risk block). The sandbox cannot reach github.io directly (HTTP 000 from curl); the read-back used the fetch tool.

## 4. Irregularities

- **B-I1 (no change needed).** A short-slug IRS URL for IR-2026-133 returns 404. The correct long-slug URL, which the guide already uses, was re-opened and reads correctly. No published link is broken.
- **B-I2 (standing, not new).** The Proposition 19 amount from 16 Feb 2027 is not published; the BOE letter says the next adjustment is in February 2027. The guide already labels its carried-forward figure as a projection.
- **B-I3 (standing, owner decisions, unchanged).** Pre-rounding history scrub (L-D2) and repository visibility (public) remain owner decisions and are not performed here.
- **B-I4 (environment).** `test-browser.cjs` does not run in this sandbox (no `libnss3`).
