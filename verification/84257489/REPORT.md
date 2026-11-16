# Verification report — session `84257489` (branch `arena/84257489-tino2`)

**Checked:** 16 Nov 2026 (UTC). **State read at claim:** `origin/main` = `5eddd9a` (merge of PR #117, session `a489e3a1`). `gh pr list --state open` returned no open pull requests.

**Scope.** Dated recheck of the load-bearing official figures, the publication boundary, and the test suite. No household value, identifier or ZIP code is written in this file. Household inputs remain as rounded in `scripts/analysis_pages.py`, unchanged.

## Official figures re-opened on 16 Nov 2026

| Figure | Value in guide / model | Official source (opened today) | Result |
|---|---|---|---|
| Federal estate basic exclusion, decedents dying in 2026 | $15,000,000 | IRS, "Working Families Tax Cuts – Individuals and workers" (estate tax exclusion for tax year 2026): https://www.irs.gov/newsroom/working-families-tax-cuts-individuals-and-workers | MATCH |
| Federal annual gift exclusion, 2026 | $19,000 per recipient (not yet displayed in the guide) | IRS Rev. Proc. 2025-32, §4.42(1): https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | MATCH (verified; no published figure changed) |
| Proposition 19 intergenerational cap, transfers 16 Feb 2025 – 15 Feb 2027 | $1,044,586 above factored base-year value | BOE Letter to Assessors 2025/009 (7 Mar 2025): https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf | MATCH; next adjustment February 2027 |
| Proposition 19 filing periods | Homeowners' exemption claim within 1 year; exclusion claim within 3 years or before transfer to a third party | BOE Proposition 19 comparison charts: https://www.boe.ca.gov/prop19/ | MATCH (wording as the guide quotes it) |
| U.S. Treasury 3-month par yield, latest official date | 4.32% (13 Nov 2026) | U.S. Treasury Daily Par Yield Curve, Nov 2026 table: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611 | MATCH (13 Nov 2026 row shows 4.32) |
| U.S. Treasury 2-year par yield, same date | 4.88% (13 Nov 2026) | same table | MATCH (13 Nov 2026 row shows 4.88) |

Notes on the yields. The Treasury table posts a business day late. The newest row on the day of this check is 13 Nov 2026. The model's 13 Nov date therefore remains the latest official figure, and it is not updated to an unposted date.

## Irregularities flagged (non-blocking)

| # | Irregularity | Severity | Disposition |
|---|---|---|---|
| V-84-1 | The IRS link in the guide's sources, `https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions-individuals-and-workers`, now serves the page titled "Working Families Tax Cuts – Individuals and workers" (same content, renamed). The old address appears to redirect. | Low | Not edited in this session (a link change needs a generator rebuild). Owner or next integration session should swap the URL to the new address above. |
| V-84-2 | The annual gift exclusion ($19,000, §4.42(1)) is verified here but is not displayed on any published page. The guide's "prior taxable gifts" question has no figure for it. | Low | Recorded as a candidate addition for a future generator change, with the official source above. Not added in this session: the figures ledger (`guide/figures/official-figures.json`) is checked by the build and was left unchanged. |
| V-84-3 | Shell environment: `scripts/privacy-audit.cjs` and `scripts/test-guide.cjs` need `.cache/test` (git-ignored) populated with the pinned packages from `.github/workflows/pages.yml`. Installed for this session with the exact pinned versions. | Info | Resolved locally; CI installs them the same way. |
| V-84-4 | The Prop 19 claim-period wording on secondary sites (e.g., "BOE-19-P within 3 years") is not the same as the BOE comparison chart. The guide quotes the BOE chart, which is correct. Secondary-site form-level detail is not used in the guide. | Info | No action. |

Items still outside this session's reach, unchanged from the board: Git history scrub (owner decision L-D2, administrator action), repository visibility (owner decision), Property A's tax rate area and independent appraisal or comparables (need owner-held documents), and tax-adviser review. None of these can be completed from a session branch.

## Test suite (local, on the claimed branch before any change)

| Check | Result |
|---|---|
| `scripts/check-generated.py` | PASS — 18 generated public pages up to date |
| `scripts/package-site.py` | PASS — 32 reviewed guide files packaged; legacy `site/` excluded |
| `scripts/check-publication.py` | PASS — publication matches 32 reviewed files plus build marker |
| `scripts/privacy-gate.py` | PASS — 236 tracked text files scanned |
| `scripts/test-model-reference.py` | PASS — 108 configurations, 250 stress years, 1,500 phased years, 20,736 comparisons |
| `scripts/test-phased.py` | PASS — 113 checks |
| `scripts/privacy-audit.cjs` | PASS (after installing the pinned `.cache/test` packages) |
| `scripts/test-guide.cjs` | PASS — 18 rendered pages, 1,114 source-linked rows, 12,844 checks |

`test-browser.cjs` needs a Chromium system library that this sandbox lacks; it runs in CI on the pull request.

## Recommendation check

No official figure changed since 15 Nov 2026, so no model input changed. Under the rule "after any input changes, rebuild and check whether the recommendation moved", the recommendation is unchanged. Its status is unchanged too: the published Questions register still answers "not yet", because the priority facts are owner-held and unverified.
