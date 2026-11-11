# Independent session verification — session 14e318a1

Date of checks: 2026-11-11 (UTC). Tree verified: branch `arena/14e318a1-tino2`, base commit `240f255f` (main HEAD, PR #17 merged). Scope: `verification/14e318a1/**` only. Privacy: no personal information appears in this file; no household dollar figure is repeated here; all figures written here are rounded to the nearest $10.

## 1. Automated suite (re-run on the current tree)

| # | Check | Command | Result |
|---|-------|---------|--------|
| 1 | Canonical packaging (privacy allowlist) | `python3 scripts/package-site.py` | PASS — packaged canonical site only; legacy material excluded |
| 2 | Static + model + source-reference validation | `node scripts/validate.js` | PASS — 581 checks across 11 pages and 70 official sources |
| 3 | Stress-path / ownership / privacy / real-dollar tests | `node scripts/stress-test.js` | PASS — 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| 4 | Internal link + table-row source check | `python3 src/check_links.py .` | PASS — 54 pages, 871 table rows, 124 distinct external links (external links not machine-checkable from this sandbox) |
| 5 | Rendered-page runtime test | `node scripts/runtime-test.cjs` | NOT RUN — requires optional dev dependency `jsdom` at `.cache/test/node_modules` (gitignored). Environment note per README, not a site defect. |

Base-case decision output at 2040 inheritance / 2050 endpoint: sell $7,683,290; rent $6,249,830; live $5,196,300 (sell leads on financial value; live excludes monetized housing service).

## 2. Independent spot re-checks against official sources

Each published statement below was compared with an official source. Because this sandbox can reach github.com/api.github.com directly but not agency domains, corroboration was done via web search against the official sources named in `site/data/sources.js`. "Match" means the published statement agrees with the official source text.

| # | Published statement (site) | Official source | Result |
|---|---------------------------|-----------------|--------|
| 1 | 2026 federal basic exclusion $15,000,000 per decedent; Form 706 due 9 months after death | IRS Form 706 instructions / estate and gift tax guidance — basic exclusion $15,000,000 for deaths in 2026, 9-month filing/payment deadline | Match |
| 2 | California requires no estate-tax return for deaths on or after Jan 1, 2005; no CA inheritance tax | California State Controller's Office, California Estate Tax | Match |
| 3 | Prop 19 intergenerational exclusion amount $1,044,586 for Feb 16, 2025 – Feb 15, 2027; biennial FHFA California HPI adjustment; principal-residence only | CA Board of Equalization NR 25-02 and Proposition 19 guidance | Match |
| 4 | San Francisco combined FY2026–27 ad valorem rate 1.18162182% ($1.18162182 per $100) | SF Board of Supervisors FY2026–27 tax-rate adoption minutes (Resolution 524-26) | Match |
| 5 | HUD FY2026 SAFMR benchmarks: Property A ZIP 95014 4BR $6,390 / 3BR $5,870; Property B ZIP 94122 | HUD FY2026 Small Area Fair Market Rent calculation | Match |
| 6 | SF Rent Board allowable increase 1.6% for Mar 1, 2026 – Feb 28, 2027; $59/unit fee; AB 1482 max 8.8% Aug 2026–Jul 2027, sunsets Jan 1, 2030 | SF Rent Board current rates, Rent Board Fee, AB 1482 reports | Match |

Not verified / flagged: exact CBO 2.3% CPI and 4.4% 10-year-yield figures (read from secondary summaries); SF 7% rent ceiling; insurance quotes; household inputs ($3,100,000 / $1,800,000 values, $7,150/mo rent, utility figures) are household planning inputs, not official appraisals.

## 3. GitHub Pages deployment

| Item | Value |
|------|-------|
| Pages status (API) | `built`, source `main` / root, HTTPS enforced |
| Public URL | https://wingbangboozle1-lang.github.io/Tino2/ |
| Canonical pages served | `index.html` + `site/*` (decision, properties, inheritance, estate-tax, san-francisco, sources, review, stress, scenarios, black-swan) |
| Legacy/private pages excluded | `_config.yml` excludes legacy HTML, research, coordination, model source trees |

## 4. Flagged irregularities (non-blocking)

These are recorded on the published `site/review.html` register and are not blockers to merge/deploy:

- 8 High-priority open items: trust instrument/title, date-of-death appraisals, full gross estate + gifts, DSUE/portability, citizenship/residency, parcel tax-rate areas, Prop 19 principal-residence eligibility, taxpayer brackets/NIIT.
- Property A actual combined levy (1.2%) is a hypothetical scenario; parcel TRA rate unverified.
- Historical household tax/assessment bills are withheld from the public build (stricter than the $10-rounding rule).
- Future Prop 19 exclusion amounts, federal exclusion, and pending legislation (H.R.1301, H.R.601, H.R.7034, CA Props 40/42/43, SF File 261020) are scenarios, not forecasts.
- External links cannot be machine-checked from this sandbox; each source link is a manual review route.

No personal names, street addresses, parcel numbers, account identifiers, trust documents, or private records were added. Public Git history and third-party caches may retain earlier exact household figures from prior deployments; see Flagged for Review.

## 5. Session claim

This session claims the final-verification and publication task on branch `arena/14e318a1-tino2`, touching only `verification/14e318a1/**` and the `COORDINATION.md` session-14e318a1 section. No file owned by another session is edited.
