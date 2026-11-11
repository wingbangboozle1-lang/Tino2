# Independent post-merge verification — session 457907c1

Date of checks: 2026-11-11 (UTC). Tree verified: branch `arena/457907c1-tino2` merged with `origin/main` at `a841d23` (PR #14). Scope: `verification/457907c1/**` only. Privacy: no personal information appears in this file; no household dollar figure is repeated here; all figures written here are rounded to the nearest $10.

## 1. Automated suite (re-run on the combined tree)

| # | Check | Command | Result |
|---|-------|---------|--------|
| 1 | Canonical packaging | `python3 scripts/package-site.py` | PASS — packaged canonical site only; legacy material excluded |
| 2 | Static + model + source-reference validation | `node scripts/validate.js` | PASS — 581 checks across 11 pages and 70 official sources |
| 3 | Stress-path / ownership / privacy / real-dollar tests | `node scripts/stress-test.js` | PASS — 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| 4 | Rendered-page runtime test | `node scripts/runtime-test.cjs` | PASS — 11 rendered pages; 763 rendered rows source-linked; no runtime errors or broken local links |
| 5 | Internal link + table-row source check | `python3 src/check_links.py .` | PASS — 54 pages, 871 table rows, 124 distinct external links (external links not machine-checkable from this sandbox) |
| 6 | Privacy scan | `python3 integration/tools/privacy_scan.py` | PASS — 0 errors; 42 warnings (all pre-existing unrounded *research-average* figures in other sessions' files; see §4) |

Note on reproducibility: `scripts/runtime-test.cjs` requires `jsdom` at `.cache/test/node_modules` (gitignored). This session installed it locally to run the test; a fresh clone must re-install it before that test runs. This is an environment note, not a site defect.

## 2. Live deployment (GitHub Pages)

| Item | Value |
|------|-------|
| Pages status (API) | `built`, source `main` / root, HTTPS enforced |
| Latest main Pages run at check time | run for `a841d23` — conclusion `success` (build, report-build-status, deploy all passed) |
| Landing page fetch | Live content matches the merged tree: executive summary, base-case recommendation, Property A/B cards, decision preview table with per-row source links, four current-law cards (IRS $15,000,000 exclusion; SCO no CA estate return; Prop 19 formula; 60-day / 150-day / 9-month clocks) |
| Category pages confirmed linked from landing | `site/decision.html`, `site/properties.html`, `site/inheritance.html`, `site/estate-tax.html`, `site/san-francisco.html`, `site/sources.html`, `site/review.html`, `site/stress.html`, `site/scenarios.html`, `site/black-swan.html` |
| Black-swan section (brief requirement) | Present as three cross-linked pages: 50-year stress paths (`stress.html`), recorded-episode shock replays (`scenarios.html`), and recorded-official-data replay + 2,000 seeded 50-year histories (`black-swan.html`), each row source-linked |

## 3. Independent spot re-checks against official sources (V-3)

Every figure below was re-read from the official page on 2026-11-11 and compared with what the published site states. "Match" means the published statement agrees with the official source text.

| # | Published statement (site) | Official source re-read | Result |
|---|---------------------------|--------------------------|--------|
| 1 | 2026 federal basic exclusion $15,000,000 per decedent | IRS, "What's new — Estate and gift tax": P.L. 119-21 increased the basic exclusion amount to $15,000,000 for calendar year 2026 — https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax | Match |
| 2 | California requires no estate-tax return for deaths on or after Jan 1, 2005 | State Controller's Office: "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return." — https://www.sco.ca.gov/ardtax_estate_tax.html | Match |
| 3 | Prop 19 intergenerational exclusion amount $1,044,586 for Feb 16, 2025 – Feb 15, 2027 (biennial FHFA HPI adjustment) | BOE News Release NR 25-02: amount increased from $1,022,600 to $1,044,586 for that window — https://www.boe.ca.gov/news/2025/nr-25-02.htm | Match |
| 4 | San Francisco combined FY2026–27 ad valorem rate 1.18162182% | Board of Supervisors minutes 2026-09-22, File 260971 / Resolution No. 524-26: "combined rate of $1.18162182 on each $100 valuation" for FY ending June 30, 2027 — https://media.api.sf.gov/documents/bag092226_minutes.pdf | Match |
| 5 | SF rent-increase limit 1.6% for Mar 1, 2026 – Feb 28, 2027; File 261020 pending, not enacted | SF Rent Board current-rates report states 1.6% for that period and that File No. 261020 "has not been enacted and is subject to change" — https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit | Match |
| 6 | AB 1482 maximum 8.8% for Aug 1, 2026 – Jul 31, 2027; statute sunsets Jan 1, 2030 | SF Rent Board AB 1482 report: "maximum annual increase … currently 8.8% (5% + 3.8%)"; law "expires on January 1, 2030" — https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482 | Match |
| 7 | HUD FY2026 4-bedroom SAFMR for the Property A ZIP: $6,390/month (3BR $5,870) | HUD FY2026 SAFMR calculation page for ZIP 95014: 3BR $5,870, 4BR $6,390 — https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=95014&year=2026 | Match |
| 8 | HUD FY2026 1BR $2,730 / 2BR $3,310 for the Property B ZIP | HUD FY2026 SAFMR calculation page for ZIP 94122: 1BR $2,730, 2BR $3,310 — https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=94122&year=2026 | Match |
| 9 | Trust notification generally due within 60 days of the triggering event | Cal. Probate Code §16061.7(f): "served not later than 60 days following the occurrence of the event requiring service" — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=16061.7.&lawCode=PROB | Match |
| 10 | Death-of-owner change-in-ownership statement (BOE-502-D) due within 150 days, including trust-held property; Prop 19 claim forms noted | BOE TRA information sheet pub800-9: "R&TC section 480(b) requires a change in ownership statement be filed within 150 days after the date of death by the trustee if the property was held in trust…"; names BOE-19-P / BOE-19-G claim forms — https://www.boe.ca.gov/pdf/pub800-9.pdf | Match |

Not independently re-checked this session (carried forward, already flagged on the Flagged for Review page): parcel-level tax-rate areas, insurance premiums, household utility bills, CBO exact percentages, maintenance benchmarks, rent achievable for Property A.

## 4. Privacy and rounding status of the published tree

| Check | Result |
|-------|--------|
| Exact (unrounded) brief household tax/assessment figures in published + working files | **Not found.** Repo-wide scan for the brief's exact amounts across `*.html`, `*.js`, `*.md`, `*.json`, `*.csv` returns only official FRED series values and $10-rounded planning inputs |
| Privacy scan errors | 0 |
| Privacy scan warnings | 42 — all dollar amounts that are not multiples of $10 in other sessions' files: research-average insurance quotes in `docs/insurance.md`, `docs/research/03-insurance-costs.md`, `pages/insurance.html`, a model-output pair in this `COORDINATION.md` (session d7d62f7a's completion record), and legacy root/`pages/` figures. None is a household bill. Owners: sessions that own those paths (see §5) |
| Household market-value and rent inputs on the landing page | Published as $10-rounded planning inputs explicitly labelled "not an appraisal or verified lease" — consistent with the brief's number rule |
| Personal identifiers (names, addresses, parcel/account numbers) | None found in the canonical `site/**` tree |

## 5. Irregularities found (non-blocking; for the Flagged for Review page owners)

| ID | Finding | Where | Suggested owner |
|----|---------|-------|-----------------|
| V-I-1 | 42 non-$10-rounded dollar amounts (research averages, model outputs) remain in legacy files; 0 are household figures | `docs/**`, `pages/**`, root `flagged.html` / `sources.html`, `COORDINATION.md` lines of session d7d62f7a's record | Path owners (sessions 64131d11 / 7c9c2cc4 / 1dab34fa / d7d62f7a) |
| V-I-2 | `runtime-test.cjs` cannot run on a fresh clone without manually installing `jsdom` into `.cache/test` | `scripts/runtime-test.cjs` (env note only) | Owner of `scripts/**` |
| V-I-3 | External (official) links cannot be machine-checked from this sandbox; each was opened manually by owning sessions; this session re-opened 10 of them (§3) | whole site | Ongoing — revalidation schedule already on `site/sources.html` |
| V-I-4 | Four parallel legacy dashboards still publish beside the canonical `site/` tree; `_config.yml` excludes most legacy paths from Jekyll processing, but the raw files remain in the repository | root `*.html`, `pages/`, `dashboard/` | Final integration session (claimed by `f16e6e34` / `5c9d68b9`) |

## 6. Conclusion

The combined tree at `a841d23` passes the full automated suite (6/6), the live GitHub Pages deployment matches the tree and is healthy (`built`, latest run `success`), privacy scan reports 0 errors, no exact household figure is published, and 10/10 independent spot re-checks of key legal/tax/rent figures match their official sources. Flagged items above do not block publication.
