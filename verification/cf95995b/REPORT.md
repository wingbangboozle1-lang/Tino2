# Verification record — session `cf95995b` (17 Nov 2026)

Scope: periodic recheck of the official authorities the published guide relies on, as of 17 Nov 2026; enacted change separated from proposals. No household figure, identifier or address is involved. Placeholders only (`Property A`, `Property B`). No shared site file is changed by this session; published figures remain dated observations (13 Nov 2026) and are not silently republished here.

## 1. Official primary pages re-opened on 17 Nov 2026

| # | Figure as the guide states it | Official source (primary page, re-opened) | What the page says | Result |
|---|---|---|---|---|
| 1 | Federal estate basic exclusion: $15,000,000 for 2026 deaths; $15,480,000 for 2027 deaths | IRS news release IR-2026-133, 5 Nov 2026 — https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts (Rev. Proc. 2026-35: https://www.irs.gov/pub/irs-drop/rp-26-35.pdf) | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026." | **MATCH** — enacted-by-indexation (statutory inflation adjustment; not a legislative change). No change since the 16 Nov recheck. |
| 2 | Annual gift exclusion $19,000 (2026) / $20,000 (2027); non-citizen-spouse gift exclusion $194,000 (2026) / $201,000 (2027) | Same IRS release | "...the first $20,000 of gifts to any person ... are not included ... – up from $19,000 for calendar year 2026." ... "(However, the annual exclusion for gifts to a spouse who is not a citizen of the United States increases to $201,000 for calendar year 2027, up from $194,000 for calendar year 2026.)" | **MATCH** — enacted-by-indexation. No change since the 16 Nov recheck. |
| 3 | Proposition 19 $1 million amount: $1,044,586 for transfers 16 Feb 2025 – 15 Feb 2027; next adjustment Feb 2027 (amount not yet published) | BOE Letter to Assessors 2025/009, 7 Mar 2025 — https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf (index: https://www.boe.ca.gov/proptaxes/2025.htm) | "...the $1 million amount is adjusted to $1,044,586." Table: 16 Feb 2025 – 15 Feb 2027 = $1,044,586. "The next adjustment ... will occur in February 2027." | **MATCH** — enacted (Cal. Const. art. XIII A §2.1(c); RTC §63.2). The Feb 2027 amount is **not published yet**; the guide shows it only as a labelled carried-forward projection. No change since the 16 Nov recheck. |
| 4 | 3-month and 2-year U.S. Treasury par yields used for the parking path | U.S. Treasury Daily Par Yield Curve, November 2026 — https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611 (CSV: .../daily-treasury-rates.csv/all/202611?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611) | Row 11/13/2026: 3 Mo 4.32, 2 Yr 4.88. Row 11/16/2026 (latest at read time, 17 Nov 2026): 3 Mo 4.34, 2 Yr 4.83. | **CHANGED** — market data updated between observations, **not** an enacted law change. The guide's "13 Nov 2026" figures (4.32% / 4.88%) remain accurate as of that dated observation; the latest observation is now 4.34% / 4.83% on 16 Nov 2026. Reported for the owner's republication decision; not silently republished so no frozen test expectation is disturbed. |
| 5 | California Form 540 sensitivity value: 1% Behavioral Health Services Tax (formerly Mental Health Services Tax) on California taxable income over $1,000,000; capital gains taxed as ordinary income; top combined marginal 13.3% (12.3% + 1%) | FTB 2025 Form 540 Personal Income Tax Booklet — https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf | Confirms the 1% surcharge on taxable income above $1,000,000 (Form 540 line 62 for TY2025, renamed Behavioral Health Services Tax), the $1,000,000 threshold not indexed and identical for all filing statuses, and that California taxes capital gains as ordinary income with no lower long-term rate. | **MATCH** — confirms the sensitivity value already in use. Enacted (Prop. 63, 2004; renamed for tax years beginning 2025), not a proposal. No change since prior verification. |

### Enacted vs proposed
Items 1, 2, 3 and 5 are enacted law (items 1, 2, 5 change only by automatic statutory indexation; item 3 by the biennial Prop. 19 FHFA adjustment). None is a new legislative enactment between 16 and 17 Nov 2026. Item 4 is a Treasury market observation, not law. Proposals tracked on the guide's Flagged/law-watch pages (e.g., H.R. 1301, SB 284 as previously logged) remain listed as proposals; none was enacted in this window.

## 2. Local gates on the current tree (read-only baseline, 17 Nov 2026)

| Gate | Result |
|---|---|
| `scripts/check-generated.py` | PASS — 19 generated public pages up to date |
| `scripts/check-figures.py` | PASS — 44 ledger records, 44 verified, 0 explicitly unverified |
| `scripts/package-site.py` | PASS — packaged 33 reviewed guide files; legacy site excluded |
| `scripts/check-publication.py --self-test` | PASS — extra/missing/altered/symlinked/hard-linked files rejected |
| `scripts/privacy-gate.py` | PASS — 254 tracked text files scanned; no blocked identifier or pre-rounding figure |
| `scripts/privacy-audit.cjs` | PASS — no hashed household-input token, property locator or common identifier in packaged source or rendered text |
| `scripts/test-guide.cjs` | PASS — 19 rendered pages, 1,231 source-linked table rows, 13,783 checks |
| `scripts/test-model-reference.py` | PASS — 108 decision configurations, 250 stress years, 1,500 phased-investment years, 20,736 comparisons |
| `scripts/test-browser.cjs` | Not run here — requires Chromium with `libnss3`, absent in this sandbox; runs in CI on pull requests |

## 3. Live site

`https://wingbangboozle1-lang.github.io/Tino2/` serves the current synthetic guide. The sandbox cannot reach github.io directly; read-back uses the fetch tool when needed. No code change was published by this session, so the deployed build already matches this tree.

## 4. Irregularities

- **C-I1 (reported, not republished).** Treasury parking yields moved between the 13 Nov and 16 Nov observations (3 Mo 4.32→4.34; 2 Yr 4.88→4.83). This is market data, not enacted law. Published figures are intentionally left as dated 13 Nov observations; this session flags the new observation rather than silently republishing it, because republishing would ripple through frozen test expectations and is an owner republication decision.
- **C-I2 (standing).** The Proposition 19 amount from 16 Feb 2027 is not yet published (BOE says the next adjustment is February 2027). The guide labels its carried-forward figure as a projection.
- **C-I3 (standing, owner/administrator decisions, unchanged).** Pre-rounding history scrub (L-D2) and repository visibility (public) remain owner/administrator actions and are not performed here.
- **C-I4 (environment).** `test-browser.cjs` does not run in this sandbox (no `libnss3`/Chromium); it runs in CI.
